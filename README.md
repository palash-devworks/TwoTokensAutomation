# TwoTokens Automation

A command-line tool for automating TwoTokens.md file management and scheduling tasks with cron jobs.

## Quick Start

1. **Setup**: Run the setup script to initialize the system
   ```bash
   ./setup.sh
   ```

2. **Update TwoTokens.md**: Manually update the file
   ```bash
   ./twotokens update
   ```

3. **List scheduled tasks**: View all configured tasks
   ```bash
   ./twotokens task list
   ```

## Commands

### File Management
- `./twotokens update` - Update TwoTokens.md file with current timestamp
- `./twotokens update --content "Custom content"` - Update with custom content

### Task Management
- `./twotokens task add <name> <command> <schedule>` - Add new scheduled task
- `./twotokens task list` - List all scheduled tasks  
- `./twotokens task remove <index>` - Remove task by index
- `./twotokens task execute <name>` - Execute specific task

### Cron Job Management
- `./twotokens cron install` - Install/update all cron jobs
- `./twotokens cron remove` - Remove all TwoTokens cron jobs
- `./twotokens cron list` - List current cron jobs

## Configuration

Edit `config.json` to customize:
- `twotokens_file`: Path to the TwoTokens.md file
- `log_file`: Path to log file
- `tasks`: Array of scheduled tasks

## Cron Schedule Format

Use standard cron format: `minute hour day month weekday`

Examples:
- `0 9 * * *` - Daily at 9 AM
- `0 */6 * * *` - Every 6 hours  
- `0 0 * * 0` - Weekly on Sunday at midnight
- `0 0 1 * *` - Monthly on the 1st at midnight

## Default Tasks

The system comes with two pre-configured tasks:
1. **daily-update**: Updates TwoTokens.md daily at 9 AM
2. **weekly-backup**: Creates weekly backup every Sunday at midnight

## Logs

All operations are logged to `twotokens.log` with timestamps for auditing and debugging.