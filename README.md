# TwoTokens Automation 🚀

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey)](https://github.com/palash-devworks/TwoTokensAutomation)
[![Website](https://img.shields.io/badge/Website-GitHub%20Pages-blue)](https://palash-devworks.github.io/TwoTokensAutomation/)

A powerful command-line tool for automating event management, file updates, and task scheduling with intelligent cron job integration. Perfect for managing meetups, conferences, and recurring automation tasks.

## ✨ Features

- 📅 **Comprehensive Event Management** - Create, track, and manage events with sponsors, directors, teams, and topics
- 🔄 **Automatic Task Scheduling** - Generate pre-event and post-event tasks automatically
- ⏰ **Intelligent Cron Integration** - Seamlessly schedule and manage cron jobs
- 📝 **File Automation** - Automated TwoTokens.md file management with timestamps
- 🔔 **Smart Notifications** - Automated reminders for sponsors, teams, and stakeholders
- 📊 **Activity Logging** - Comprehensive logging with timestamps for auditing
- ⚙️ **Configuration-Driven** - Flexible JSON-based configuration system

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ 
- Unix-like system (Linux, macOS)
- Cron daemon (typically pre-installed)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/palash-devworks/TwoTokensAutomation.git
   cd TwoTokensAutomation
   ```

2. **Install dependencies**
   ```bash
   pip3 install python-dateutil
   ```

3. **Setup the system**
   ```bash
   ./setup.sh
   ```

## 📚 Usage

### Event Management

**Create a new event with full details:**
```bash
./twotokens event add "Summer Tech Meetup" "2025-08-15 18:00" \
  --sponsor "TechCorp" \
  --director "Alice Johnson" \
  --team "Bob Smith" "Carol Wilson" \
  --topic "AI in Finance" \
  --description "Quarterly meetup discussing AI applications"
```

**List all events:**
```bash
./twotokens event list
./twotokens event list --status scheduled  # Filter by status
```

**View upcoming events:**
```bash
./twotokens event upcoming
```

**Update event details:**
```bash
./twotokens event update 1 --sponsor "NewSponsor" --topic "Updated Topic"
```

### Task Management

**Add custom scheduled task:**
```bash
./twotokens task add "daily-report" "python generate_report.py" "0 9 * * *"
```

**List all scheduled tasks:**
```bash
./twotokens task list
```

**Execute a task immediately:**
```bash
./twotokens task execute "daily-update"
```

### File Management

**Update TwoTokens.md file:**
```bash
./twotokens update
./twotokens update --content "Custom content here"
```

### Cron Job Management

**Install all cron jobs:**
```bash
./twotokens cron install
```

**List current cron jobs:**
```bash
./twotokens cron list
```

**Remove TwoTokens cron jobs:**
```bash
./twotokens cron remove
```

## ⚙️ Configuration

The system uses `config.json` for configuration:

```json
{
  "twotokens_file": "TwoTokens.md",
  "log_file": "twotokens.log",
  "tasks": [...],
  "events": [...],
  "settings": {
    "timezone": "local",
    "email_notifications": false,
    "log_retention_days": 30
  }
}
```

## 🔔 Automatic Event Scheduling

When you create an event, the system automatically generates:

1. **Sponsor Reminder** - 7 days before event
2. **Team Preparation Notice** - 3 days before event  
3. **Final Reminder** - 1 day before event
4. **Post-Event Update** - 1 day after event completion

All tasks are automatically scheduled as cron jobs and can be customized via configuration templates.

## 📅 Cron Schedule Format

Use standard cron format: `minute hour day month weekday`

| Schedule | Description |
|----------|-------------|
| `0 9 * * *` | Daily at 9 AM |
| `0 */6 * * *` | Every 6 hours |
| `0 0 * * 0` | Weekly on Sunday at midnight |
| `0 0 1 * *` | Monthly on the 1st at midnight |
| `*/15 * * * *` | Every 15 minutes |

## 🏗️ Architecture

The system consists of three main components:

- **TaskEventManager** - Core task and file management
- **EventManager** - Event lifecycle and scheduling
- **CronManager** - Cron job installation and management

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Email/Slack notification integrations
- [ ] Web dashboard interface
- [ ] Event templates and recurring events
- [ ] Integration with calendar systems (Google Calendar, Outlook)
- [ ] Advanced reporting and analytics
- [ ] Docker containerization
- [ ] REST API for remote management

## 🐛 Issues & Support

Found a bug or have a feature request? Please [open an issue](https://github.com/palash-devworks/TwoTokensAutomation/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for the automation community
- Inspired by the need for simple yet powerful event management
- Thanks to all contributors and users

---

**Made with [Claude Code](https://claude.ai/code)** 🤖