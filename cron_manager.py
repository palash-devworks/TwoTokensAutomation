"""
Cron Job Management for TwoTokens Automation
Handles installation, removal, and management of cron jobs for scheduled tasks.
"""

import os
import tempfile
from subprocess import run, PIPE, CalledProcessError
from pathlib import Path

class CronManager:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.cron_comment = "# TwoTokens Automation"
        self.script_path = os.path.abspath("twotokens")
    
    def get_current_crontab(self):
        """Get current crontab content"""
        try:
            result = run(["crontab", "-l"], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return ""
        except CalledProcessError:
            return ""
    
    def install_cron_jobs(self):
        """Install cron jobs for all configured tasks"""
        current_crontab = self.get_current_crontab()
        
        # Remove existing TwoTokens cron jobs
        lines = current_crontab.split('\n')
        filtered_lines = []
        skip_next = False
        
        for line in lines:
            if line.strip() == self.cron_comment:
                skip_next = True
                continue
            elif skip_next and line.strip().startswith('#'):
                skip_next = False
                continue
            elif skip_next and 'twotokens' in line:
                skip_next = False
                continue
            else:
                skip_next = False
                if line.strip():
                    filtered_lines.append(line)
        
        # Add new cron jobs
        new_crontab_lines = filtered_lines.copy()
        
        for task in self.event_manager.config["tasks"]:
            new_crontab_lines.append(f"{self.cron_comment}")
            new_crontab_lines.append(f"# Task: {task['name']}")
            cron_command = f"{task['schedule']} {self.script_path} task execute \"{task['name']}\""
            new_crontab_lines.append(cron_command)
            new_crontab_lines.append("")  # Empty line for readability
        
        # Write new crontab
        new_crontab = '\n'.join(new_crontab_lines)
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.crontab') as f:
                f.write(new_crontab)
                temp_file = f.name
            
            result = run(["crontab", temp_file], capture_output=True, text=True)
            os.unlink(temp_file)
            
            if result.returncode == 0:
                self.event_manager.log_message(f"Installed {len(self.event_manager.config['tasks'])} cron jobs")
                print(f"Successfully installed {len(self.event_manager.config['tasks'])} cron jobs")
            else:
                self.event_manager.log_message(f"Failed to install cron jobs: {result.stderr}")
                print(f"Failed to install cron jobs: {result.stderr}")
        
        except Exception as e:
            self.event_manager.log_message(f"Error installing cron jobs: {str(e)}")
            print(f"Error installing cron jobs: {str(e)}")
    
    def remove_cron_jobs(self):
        """Remove all TwoTokens cron jobs"""
        current_crontab = self.get_current_crontab()
        
        lines = current_crontab.split('\n')
        filtered_lines = []
        skip_next = False
        removed_count = 0
        
        for line in lines:
            if line.strip() == self.cron_comment:
                skip_next = True
                continue
            elif skip_next and line.strip().startswith('#'):
                skip_next = False
                continue
            elif skip_next and 'twotokens' in line:
                skip_next = False
                removed_count += 1
                continue
            else:
                skip_next = False
                if line.strip():
                    filtered_lines.append(line)
        
        # Write updated crontab
        new_crontab = '\n'.join(filtered_lines)
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.crontab') as f:
                f.write(new_crontab)
                temp_file = f.name
            
            result = run(["crontab", temp_file], capture_output=True, text=True)
            os.unlink(temp_file)
            
            if result.returncode == 0:
                self.event_manager.log_message(f"Removed {removed_count} cron jobs")
                print(f"Successfully removed {removed_count} cron jobs")
            else:
                self.event_manager.log_message(f"Failed to remove cron jobs: {result.stderr}")
                print(f"Failed to remove cron jobs: {result.stderr}")
        
        except Exception as e:
            self.event_manager.log_message(f"Error removing cron jobs: {str(e)}")
            print(f"Error removing cron jobs: {str(e)}")
    
    def list_cron_jobs(self):
        """List current cron jobs"""
        current_crontab = self.get_current_crontab()
        
        if not current_crontab.strip():
            print("No cron jobs found.")
            return
        
        print("Current cron jobs:")
        print("-" * 50)
        
        lines = current_crontab.split('\n')
        twotokens_jobs = []
        other_jobs = []
        
        in_twotokens_section = False
        current_job = {}
        
        for line in lines:
            if line.strip() == self.cron_comment:
                in_twotokens_section = True
                current_job = {}
                continue
            elif in_twotokens_section and line.strip().startswith('# Task:'):
                current_job['name'] = line.replace('# Task:', '').strip()
                continue
            elif in_twotokens_section and 'twotokens' in line:
                current_job['schedule'] = line
                twotokens_jobs.append(current_job)
                in_twotokens_section = False
                continue
            elif line.strip() and not line.startswith('#'):
                other_jobs.append(line)
        
        if twotokens_jobs:
            print("TwoTokens Automation Jobs:")
            for job in twotokens_jobs:
                print(f"  - {job.get('name', 'Unknown')}")
                print(f"    {job.get('schedule', 'Unknown schedule')}")
            print()
        
        if other_jobs:
            print("Other Cron Jobs:")
            for job in other_jobs:
                print(f"  {job}")
        
        if not twotokens_jobs and not other_jobs:
            print("No cron jobs found.")
    
    def validate_cron_schedule(self, schedule):
        """Validate cron schedule format"""
        parts = schedule.split()
        if len(parts) != 5:
            return False, "Cron schedule must have 5 parts: minute hour day month weekday"
        
        # Basic validation - could be more comprehensive
        ranges = [
            (0, 59),   # minute
            (0, 23),   # hour
            (1, 31),   # day
            (1, 12),   # month
            (0, 7)     # weekday (0 and 7 are both Sunday)
        ]
        
        for i, part in enumerate(parts):
            if part == '*':
                continue
            
            try:
                if '-' in part:
                    start, end = part.split('-')
                    start, end = int(start), int(end)
                    if start < ranges[i][0] or end > ranges[i][1] or start > end:
                        return False, f"Invalid range in position {i+1}: {part}"
                elif ',' in part:
                    values = [int(v) for v in part.split(',')]
                    for val in values:
                        if val < ranges[i][0] or val > ranges[i][1]:
                            return False, f"Invalid value in position {i+1}: {val}"
                else:
                    val = int(part)
                    if val < ranges[i][0] or val > ranges[i][1]:
                        return False, f"Invalid value in position {i+1}: {val}"
            except ValueError:
                return False, f"Invalid format in position {i+1}: {part}"
        
        return True, "Valid cron schedule"