---
layout: default
title: API Reference
---

# API Reference

Complete command-line interface reference for TwoTokens Automation.

## Main Commands

### twotokens

Main entry point for all operations.

```bash
twotokens [--config CONFIG_FILE] <command> [options]
```

**Global Options:**
- `--config` - Path to configuration file (default: config.json)

## File Management

### update

Update the TwoTokens.md file with current timestamp.

```bash
twotokens update [--content CONTENT]
```

**Options:**
- `--content` - Custom content for the file

**Examples:**
```bash
# Basic update with timestamp
twotokens update

# Custom content
twotokens update --content "Project milestone reached!"
```

## Task Management

### task add

Add a new scheduled task.

```bash
twotokens task add <name> <command> <schedule>
```

**Parameters:**
- `name` - Unique task name
- `command` - Command to execute
- `schedule` - Cron schedule format

**Examples:**
```bash
twotokens task add "daily-backup" "cp important.txt backup/" "0 2 * * *"
twotokens task add "weekly-report" "python report.py" "0 9 * * 1"
```

### task list

List all scheduled tasks.

```bash
twotokens task list
```

**Output:**
- Task index, name, command, schedule
- Creation timestamp and description (if available)

### task remove

Remove a task by index.

```bash
twotokens task remove <index>
```

**Parameters:**
- `index` - Task index from `task list` command

### task execute

Execute a specific task immediately.

```bash
twotokens task execute <name>
```

**Parameters:**
- `name` - Task name to execute

## Event Management

### event add

Create a new event with full details.

```bash
twotokens event add <name> <date> [options]
```

**Parameters:**
- `name` - Event name
- `date` - Event date and time (YYYY-MM-DD HH:MM)

**Options:**
- `--sponsor` - Event sponsor name
- `--director` - Event director name
- `--team` - Team members (multiple values allowed)
- `--topic` - Event topic
- `--description` - Event description

**Examples:**
```bash
# Basic event
twotokens event add "Team Meeting" "2025-07-20 14:00"

# Full event details
twotokens event add "Annual Conference" "2025-09-15 09:00" \
  --sponsor "TechCorp" \
  --director "Jane Doe" \
  --team "John" "Alice" "Bob" \
  --topic "AI Revolution" \
  --description "Annual technology conference"
```

### event list

List all events with optional filtering.

```bash
twotokens event list [--status STATUS]
```

**Options:**
- `--status` - Filter by status (scheduled, completed)

**Examples:**
```bash
# All events
twotokens event list

# Only scheduled events
twotokens event list --status scheduled
```

### event update

Update event details.

```bash
twotokens event update <id> [options]
```

**Parameters:**
- `id` - Event ID

**Options:**
- `--name` - Update event name
- `--date` - Update event date (YYYY-MM-DD HH:MM)
- `--sponsor` - Update sponsor
- `--director` - Update director
- `--team` - Update team members
- `--topic` - Update topic
- `--description` - Update description
- `--status` - Update status

**Examples:**
```bash
# Update sponsor
twotokens event update 1 --sponsor "New Sponsor"

# Update multiple fields
twotokens event update 1 --sponsor "Corp" --topic "New Topic"
```

### event delete

Delete an event and its associated tasks.

```bash
twotokens event delete <id>
```

**Parameters:**
- `id` - Event ID to delete

### event notify

Send notifications for an event.

```bash
twotokens event notify <target> <event_name>
```

**Parameters:**
- `target` - Notification target (sponsor, team, all)
- `event_name` - Name of the event

**Examples:**
```bash
twotokens event notify sponsor "Annual Conference"
twotokens event notify team "Team Meeting"
twotokens event notify all "Important Event"
```

### event complete

Mark an event as completed.

```bash
twotokens event complete <event_name>
```

**Parameters:**
- `event_name` - Name of the event to complete

### event upcoming

List upcoming events in the next 30 days.

```bash
twotokens event upcoming
```

## Cron Job Management

### cron install

Install cron jobs for all scheduled tasks.

```bash
twotokens cron install
```

**Behavior:**
- Removes existing TwoTokens cron jobs
- Installs new cron jobs for all tasks
- Preserves other cron jobs

### cron remove

Remove all TwoTokens cron jobs.

```bash
twotokens cron remove
```

**Behavior:**
- Only removes jobs created by TwoTokens
- Preserves other cron jobs

### cron list

List current cron jobs.

```bash
twotokens cron list
```

**Output:**
- TwoTokens automation jobs
- Other system cron jobs

## Configuration Format

### config.json Structure

```json
{
  "twotokens_file": "TwoTokens.md",
  "log_file": "twotokens.log",
  "tasks": [
    {
      "name": "task-name",
      "command": "command-to-run",
      "schedule": "cron-schedule",
      "description": "Task description",
      "created": "2025-07-10T10:00:00",
      "event_id": 1,
      "task_type": "pre_event"
    }
  ],
  "events": [
    {
      "id": 1,
      "name": "Event Name",
      "date": "2025-07-25T18:00:00",
      "sponsor": "Sponsor Name",
      "director": "Director Name",
      "team": ["Member 1", "Member 2"],
      "topic": "Event Topic",
      "description": "Event description",
      "status": "scheduled",
      "created": "2025-07-10T10:00:00",
      "tasks": ["task1", "task2"]
    }
  ],
  "settings": {
    "timezone": "local",
    "email_notifications": false,
    "log_retention_days": 30
  },
  "event_templates": {
    "pre_event": [...],
    "post_event": [...]
  }
}
```

## Cron Schedule Format

Standard cron format: `minute hour day month weekday`

### Schedule Examples

| Format | Description |
|--------|-------------|
| `* * * * *` | Every minute |
| `0 * * * *` | Every hour |
| `0 9 * * *` | Daily at 9 AM |
| `0 9 * * 1` | Every Monday at 9 AM |
| `0 9 1 * *` | First day of month at 9 AM |
| `0 9 1 1 *` | January 1st at 9 AM |
| `*/15 * * * *` | Every 15 minutes |
| `0 */6 * * *` | Every 6 hours |
| `0 9-17 * * 1-5` | 9 AM to 5 PM, weekdays |

### Time Ranges

- **Minutes**: 0-59
- **Hours**: 0-23
- **Days**: 1-31
- **Months**: 1-12
- **Weekdays**: 0-7 (0 and 7 = Sunday)

### Special Characters

- `*` - Any value
- `,` - Value list (1,3,5)
- `-` - Range (1-5)
- `/` - Step values (*/15)

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid arguments |
| 3 | Configuration error |
| 4 | Permission error |
| 5 | File not found |

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `TWOTOKENS_CONFIG` | Configuration file path | config.json |
| `TWOTOKENS_LOG_LEVEL` | Log level (DEBUG, INFO, ERROR) | INFO |
| `TWOTOKENS_TIMEZONE` | Timezone for scheduling | local |

## Error Handling

### Common Error Messages

**Configuration Errors:**
- "Configuration file not found" - Check config.json exists
- "Invalid JSON format" - Validate JSON syntax
- "Missing required field" - Check configuration structure

**Permission Errors:**
- "Permission denied" - Check file permissions
- "Cannot write to log file" - Check log file permissions
- "Cron access denied" - Check cron permissions

**Scheduling Errors:**
- "Invalid cron format" - Check schedule syntax
- "Task already exists" - Use unique task names
- "Event not found" - Check event ID/name

### Debugging

Enable debug mode:
```bash
export TWOTOKENS_LOG_LEVEL=DEBUG
twotokens task list
```

Check logs:
```bash
tail -f twotokens.log
```

Validate configuration:
```bash
python -m json.tool config.json
```

## API Integration

### Webhook Support

Tasks can trigger webhooks:
```bash
twotokens task add "webhook-notify" \
  "curl -X POST -H 'Content-Type: application/json' -d '{\"message\":\"Task completed\"}' https://hooks.example.com/webhook" \
  "0 9 * * *"
```

### External Scripts

Execute external scripts:
```bash
twotokens task add "external-script" \
  "python /path/to/script.py --param value" \
  "0 */6 * * *"
```

### Environment Passing

Pass environment variables:
```bash
twotokens task add "env-task" \
  "ENV_VAR=value /path/to/script.sh" \
  "0 12 * * *"
```