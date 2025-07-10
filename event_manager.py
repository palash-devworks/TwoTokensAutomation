"""
Event Management for TwoTokens Automation
Handles event creation, tracking, and automatic task scheduling for events.
"""

import json
import os
from datetime import datetime, timedelta
from dateutil.parser import parse as date_parse

class EventManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from JSON file"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {
            "events": [],
            "event_templates": self.get_default_templates()
        }
    
    def save_config(self):
        """Save configuration to JSON file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get_default_templates(self):
        """Get default event task templates"""
        return {
            "pre_event": [
                {
                    "name": "sponsor_reminder",
                    "command": "./twotokens event notify sponsor \"{event_name}\"",
                    "days_before": 7,
                    "description": "Send sponsor reminder 1 week before event"
                },
                {
                    "name": "team_preparation",
                    "command": "./twotokens event notify team \"{event_name}\"",
                    "days_before": 3,
                    "description": "Send team preparation notice 3 days before"
                },
                {
                    "name": "final_reminder",
                    "command": "./twotokens event notify all \"{event_name}\"",
                    "days_before": 1,
                    "description": "Send final reminder 1 day before event"
                }
            ],
            "post_event": [
                {
                    "name": "post_event_update",
                    "command": "./twotokens event complete \"{event_name}\"",
                    "days_after": 1,
                    "description": "Update event status and create summary"
                }
            ]
        }
    
    def create_event(self, name, date, sponsor=None, director=None, team=None, topic=None, description=None):
        """Create a new event with all details"""
        try:
            # Parse the date
            if isinstance(date, str):
                event_date = date_parse(date)
            else:
                event_date = date
                
            # Create event object
            event = {
                "id": self.generate_event_id(),
                "name": name,
                "date": event_date.isoformat(),
                "sponsor": sponsor,
                "director": director,
                "team": team if isinstance(team, list) else [team] if team else [],
                "topic": topic,
                "description": description,
                "status": "scheduled",
                "created": datetime.now().isoformat(),
                "tasks": []
            }
            
            # Add to config
            if "events" not in self.config:
                self.config["events"] = []
            self.config["events"].append(event)
            
            # Generate automatic tasks
            self.generate_event_tasks(event)
            
            self.save_config()
            return event
            
        except Exception as e:
            raise ValueError(f"Error creating event: {str(e)}")
    
    def generate_event_id(self):
        """Generate unique event ID"""
        existing_ids = [event.get("id", 0) for event in self.config.get("events", [])]
        return max(existing_ids, default=0) + 1
    
    def generate_event_tasks(self, event):
        """Generate automatic tasks for an event"""
        event_date = date_parse(event["date"])
        templates = self.config.get("event_templates", self.get_default_templates())
        
        # Pre-event tasks
        for template in templates.get("pre_event", []):
            task_date = event_date - timedelta(days=template["days_before"])
            task_name = f"{event['name']}_{template['name']}"
            
            # Create cron schedule for the task date
            schedule = f"{task_date.minute} {task_date.hour} {task_date.day} {task_date.month} *"
            
            # Format command with event details
            command = template["command"].format(
                event_name=event["name"],
                event_id=event["id"],
                sponsor=event.get("sponsor", ""),
                director=event.get("director", ""),
                topic=event.get("topic", "")
            )
            
            task = {
                "name": task_name,
                "command": command,
                "schedule": schedule,
                "event_id": event["id"],
                "task_type": "pre_event",
                "description": template["description"],
                "created": datetime.now().isoformat()
            }
            
            event["tasks"].append(task["name"])
            
            # Add to main tasks list if it exists
            if "tasks" not in self.config:
                self.config["tasks"] = []
            self.config["tasks"].append(task)
        
        # Post-event tasks
        for template in templates.get("post_event", []):
            task_date = event_date + timedelta(days=template["days_after"])
            task_name = f"{event['name']}_{template['name']}"
            
            schedule = f"{task_date.minute} {task_date.hour} {task_date.day} {task_date.month} *"
            
            command = template["command"].format(
                event_name=event["name"],
                event_id=event["id"],
                sponsor=event.get("sponsor", ""),
                director=event.get("director", ""),
                topic=event.get("topic", "")
            )
            
            task = {
                "name": task_name,
                "command": command,
                "schedule": schedule,
                "event_id": event["id"],
                "task_type": "post_event",
                "description": template["description"],
                "created": datetime.now().isoformat()
            }
            
            event["tasks"].append(task["name"])
            self.config["tasks"].append(task)
    
    def list_events(self, status_filter=None):
        """List all events, optionally filtered by status"""
        events = self.config.get("events", [])
        
        if status_filter:
            events = [e for e in events if e.get("status") == status_filter]
        
        if not events:
            print("No events found.")
            return
        
        print("Events:")
        print("-" * 80)
        
        for event in events:
            event_date = date_parse(event["date"])
            print(f"ID: {event['id']} | {event['name']}")
            print(f"Date: {event_date.strftime('%Y-%m-%d %H:%M')}")
            print(f"Status: {event.get('status', 'unknown')}")
            
            if event.get('sponsor'):
                print(f"Sponsor: {event['sponsor']}")
            if event.get('director'):
                print(f"Director: {event['director']}")
            if event.get('team'):
                print(f"Team: {', '.join(event['team'])}")
            if event.get('topic'):
                print(f"Topic: {event['topic']}")
            if event.get('description'):
                print(f"Description: {event['description']}")
            
            if event.get('tasks'):
                print(f"Associated Tasks: {len(event['tasks'])}")
            
            print("-" * 80)
    
    def get_event(self, event_id):
        """Get event by ID"""
        for event in self.config.get("events", []):
            if event.get("id") == event_id:
                return event
        return None
    
    def update_event(self, event_id, **updates):
        """Update event details"""
        event = self.get_event(event_id)
        if not event:
            return False
        
        # Update allowed fields
        allowed_fields = ["name", "date", "sponsor", "director", "team", "topic", "description", "status"]
        for field, value in updates.items():
            if field in allowed_fields:
                event[field] = value
        
        event["modified"] = datetime.now().isoformat()
        self.save_config()
        return True
    
    def delete_event(self, event_id):
        """Delete an event and its associated tasks"""
        event = self.get_event(event_id)
        if not event:
            return False
        
        # Remove associated tasks
        task_names = event.get("tasks", [])
        if "tasks" in self.config:
            self.config["tasks"] = [
                task for task in self.config["tasks"] 
                if task.get("name") not in task_names
            ]
        
        # Remove event
        self.config["events"] = [
            e for e in self.config["events"] 
            if e.get("id") != event_id
        ]
        
        self.save_config()
        return True
    
    def notify_sponsor(self, event_name):
        """Send notification to sponsor"""
        print(f"📧 Sponsor notification sent for event: {event_name}")
        # In a real implementation, this would send actual notifications
        
    def notify_team(self, event_name):
        """Send notification to team"""
        print(f"👥 Team notification sent for event: {event_name}")
        
    def notify_all(self, event_name):
        """Send notification to all stakeholders"""
        print(f"📢 All stakeholders notified for event: {event_name}")
        
    def complete_event(self, event_name):
        """Mark event as completed and create summary"""
        for event in self.config.get("events", []):
            if event["name"] == event_name:
                event["status"] = "completed"
                event["completed"] = datetime.now().isoformat()
                self.save_config()
                print(f"✅ Event '{event_name}' marked as completed")
                return
        print(f"❌ Event '{event_name}' not found")
    
    def get_upcoming_events(self, days_ahead=30):
        """Get events happening in the next N days"""
        cutoff_date = datetime.now() + timedelta(days=days_ahead)
        upcoming = []
        
        for event in self.config.get("events", []):
            event_date = date_parse(event["date"])
            if datetime.now() <= event_date <= cutoff_date:
                upcoming.append(event)
        
        # Sort by date
        upcoming.sort(key=lambda x: date_parse(x["date"]))
        return upcoming