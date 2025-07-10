---
layout: default
title: Installation Guide
---

# Installation Guide

## Prerequisites

Before installing TwoTokens Automation, ensure you have:

- **Python 3.7+** installed
- **Unix-like system** (Linux, macOS)
- **Cron daemon** (typically pre-installed)
- **Git** for cloning the repository

## Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/palash-devworks/TwoTokensAutomation.git
cd TwoTokensAutomation
```

### 2. Install Dependencies

```bash
pip3 install python-dateutil
```

### 3. Run Setup

```bash
./setup.sh
```

The setup script will:
- Make scripts executable
- Create initial TwoTokens.md file
- Install default cron jobs
- Display available commands

## Manual Installation

If you prefer to set up manually:

### 1. Make Scripts Executable

```bash
chmod +x twotokens setup.sh
```

### 2. Install Python Dependencies

```bash
pip3 install python-dateutil
```

### 3. Initialize Configuration

```bash
# Create initial file
./twotokens update

# View default tasks
./twotokens task list

# Install cron jobs
./twotokens cron install
```

## Verification

Verify your installation:

```bash
# Check version and help
./twotokens --help

# List scheduled tasks
./twotokens task list

# View cron jobs
./twotokens cron list

# Check log file
cat twotokens.log
```

## Configuration

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

## Troubleshooting

### Permission Issues

If you encounter permission errors:

```bash
chmod +x twotokens setup.sh
```

### Python Dependencies

If `python-dateutil` installation fails:

```bash
# Using pip
pip install python-dateutil

# Using conda
conda install python-dateutil

# Using system package manager (Ubuntu/Debian)
sudo apt-get install python3-dateutil
```

### Cron Issues

If cron jobs don't install:

```bash
# Check if cron service is running
sudo service cron status

# Install cron if missing (Ubuntu/Debian)
sudo apt-get install cron

# Start cron service
sudo service cron start
```

### Log Permission Issues

If log file creation fails:

```bash
# Create log file manually
touch twotokens.log
chmod 644 twotokens.log
```

## Uninstallation

To remove TwoTokens Automation:

```bash
# Remove cron jobs
./twotokens cron remove

# Remove files
cd ..
rm -rf TwoTokensAutomation
```

## System Requirements

| Component | Requirement |
|-----------|-------------|
| Operating System | Linux, macOS, Unix-like |
| Python | 3.7 or higher |
| Disk Space | ~10 MB |
| Memory | ~50 MB |
| Network | Optional (for GitHub features) |

## Next Steps

After installation:

1. **[Create your first event](usage/#event-management)**
2. **[Set up custom tasks](usage/#task-management)**
3. **[Configure notifications](usage/#notifications)**
4. **[Explore advanced features](api/)**

## Support

If you encounter issues during installation:

- Check the [troubleshooting section](#troubleshooting)
- [Open an issue](https://github.com/palash-devworks/TwoTokensAutomation/issues) on GitHub
- Review the [contributing guide](contributing/) for development setup