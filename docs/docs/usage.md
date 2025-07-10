---
layout: default
title: Usage Examples
---

# Usage Examples

## Event Management

### Creating Events

Create a comprehensive event with all details:

```bash
./twotokens event add "Annual Tech Conference" "2025-09-15 09:00" \
  --sponsor "TechCorp Inc" \
  --director "Sarah Johnson" \
  --team "Mike Chen" "Emily Davis" "Alex Rodriguez" \
  --topic "Future of AI and Machine Learning" \
  --description "Annual conference featuring latest trends in AI/ML"
```

Create a simple event:

```bash
./twotokens event add "Weekly Standup" "2025-07-15 10:00" \
  --topic "Sprint Planning"
```

### Managing Events

List all events:

```bash
# All events
./twotokens event list

# Only scheduled events
./twotokens event list --status scheduled

# Only completed events
./twotokens event list --status completed
```

View upcoming events:

```bash
./twotokens event upcoming
```

Update event details:

```bash
# Update sponsor
./twotokens event update 1 --sponsor "New Sponsor Corp"

# Update multiple fields
./twotokens event update 1 \
  --sponsor "Updated Sponsor" \
  --topic "New Topic" \
  --description "Updated description"
```

Delete an event:

```bash
./twotokens event delete 1
```

### Event Notifications

Send notifications manually:

```bash
# Notify sponsor
./twotokens event notify sponsor "Annual Tech Conference"

# Notify team
./twotokens event notify team "Annual Tech Conference"

# Notify all stakeholders
./twotokens event notify all "Annual Tech Conference"
```

Mark event as completed:

```bash
./twotokens event complete "Annual Tech Conference"
```

## Task Management

### Creating Tasks

Add custom scheduled tasks:

```bash
# Daily backup
./twotokens task add "daily-backup" \
  "tar -czf backup-$(date +%Y%m%d).tar.gz important-files/" \
  "0 2 * * *"

# Weekly report
./twotokens task add "weekly-report" \
  "python generate_report.py" \
  "0 9 * * 1"

# Monthly cleanup
./twotokens task add "monthly-cleanup" \
  "find /tmp -type f -mtime +30 -delete" \
  "0 3 1 * *"
```

### Managing Tasks

List all tasks:

```bash
./twotokens task list
```

Execute a task immediately:

```bash
./twotokens task execute "daily-backup"
```

Remove a task:

```bash
./twotokens task remove 3
```

## File Management

### Updating TwoTokens.md

Basic update with timestamp:

```bash
./twotokens update
```

Update with custom content:

```bash
./twotokens update --content "# Project Status

Last updated: $(date)

## Current Sprint
- Feature development in progress
- Testing phase starting next week
- Release planned for end of month

## Team Updates
- New team member joining Monday
- Sprint review scheduled for Friday"
```

## Cron Job Management

### Installing Cron Jobs

Install all scheduled tasks:

```bash
./twotokens cron install
```

### Viewing Cron Jobs

List current cron jobs:

```bash
./twotokens cron list
```

### Removing Cron Jobs

Remove all TwoTokens cron jobs:

```bash
./twotokens cron remove
```

## Cron Schedule Examples

| Schedule | Description | Example Use Case |
|----------|-------------|------------------|
| `0 9 * * *` | Daily at 9 AM | Morning standup reminder |
| `0 */6 * * *` | Every 6 hours | System health check |
| `0 0 * * 0` | Weekly on Sunday midnight | Weekly backup |
| `0 0 1 * *` | Monthly on 1st at midnight | Monthly report |
| `*/15 * * * *` | Every 15 minutes | Frequent monitoring |
| `0 18 * * 1-5` | Daily at 6 PM (weekdays) | End-of-day summary |
| `0 8 1,15 * *` | 1st and 15th at 8 AM | Bi-monthly meeting |

## Advanced Workflows

### Conference Planning Workflow

```bash
# 1. Create main conference event
./twotokens event add "DevCon 2025" "2025-10-15 09:00" \
  --sponsor "DevCorp" \
  --director "Conference Manager" \
  --team "Marketing Team" "Tech Team" "Logistics Team" \
  --topic "Full Stack Development" \
  --description "Annual developer conference"

# 2. Add custom preparation tasks
./twotokens task add "venue-booking-reminder" \
  "echo 'Check venue booking status'" \
  "0 9 * * 1"

./twotokens task add "speaker-confirmation" \
  "python check_speaker_confirmations.py" \
  "0 10 */3 * *"

# 3. Install all automation
./twotokens cron install

# 4. Monitor progress
./twotokens event upcoming
./twotokens task list
```

### Team Meeting Automation

```bash
# Weekly team meeting
./twotokens event add "Weekly Team Sync" "2025-07-21 14:00" \
  --director "Team Lead" \
  --team "Developer 1" "Developer 2" "Designer" \
  --topic "Sprint Review and Planning"

# Add meeting preparation tasks
./twotokens task add "meeting-prep-reminder" \
  "./twotokens event notify team 'Weekly Team Sync'" \
  "0 13 * * 1"

# Add agenda preparation
./twotokens task add "agenda-prep" \
  "echo 'Prepare meeting agenda' >> meeting-notes.txt" \
  "0 12 * * 1"
```

### Project Status Updates

```bash
# Automated status updates
./twotokens task add "daily-status-update" \
  "./twotokens update --content 'Daily Status: $(date) - All systems operational'" \
  "0 17 * * 1-5"

# Weekly summary
./twotokens task add "weekly-summary" \
  "python generate_weekly_summary.py > weekly-report.md" \
  "0 18 * * 5"
```

## Integration Examples

### Slack Integration

```bash
# Add Slack notification task
./twotokens task add "slack-reminder" \
  "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"Event reminder!\"}' YOUR_SLACK_WEBHOOK_URL" \
  "0 9 * * *"
```

### Email Notifications

```bash
# Email reminder script
./twotokens task add "email-reminder" \
  "echo 'Event reminder' | mail -s 'TwoTokens Reminder' user@example.com" \
  "0 8 * * *"
```

### Git Integration

```bash
# Automated git operations
./twotokens task add "daily-commit" \
  "cd /path/to/repo && git add . && git commit -m 'Daily auto-commit: $(date)'" \
  "0 23 * * *"
```

## Monitoring and Logs

### Viewing Logs

```bash
# View all logs
cat twotokens.log

# View recent logs
tail -f twotokens.log

# Search logs
grep "ERROR" twotokens.log
```

### System Health Check

```bash
# Check system status
./twotokens task list | wc -l  # Count active tasks
./twotokens cron list          # Verify cron jobs
./twotokens event upcoming     # Check upcoming events
```

## Best Practices

1. **Regular Backups**: Set up automated backups of configuration
2. **Log Monitoring**: Regularly check logs for errors
3. **Task Naming**: Use descriptive names for tasks
4. **Event Planning**: Create events well in advance
5. **Testing**: Test tasks manually before scheduling
6. **Documentation**: Document custom tasks and workflows

## Troubleshooting

### Common Issues

**Task not executing:**
```bash
# Check cron jobs are installed
./twotokens cron list

# Verify task exists
./twotokens task list

# Test manual execution
./twotokens task execute "task-name"
```

**Permission errors:**
```bash
# Fix script permissions
chmod +x twotokens

# Fix log file permissions
touch twotokens.log
chmod 644 twotokens.log
```

**Configuration issues:**
```bash
# Verify configuration
cat config.json | python -m json.tool

# Reset to defaults
mv config.json config.json.backup
./setup.sh
```