# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TwoTokensAutomation is a command-line tool for automating TwoTokens.md file management and scheduling tasks with cron jobs. The system provides event management capabilities with automated scheduling.

## Development Commands

- `./setup.sh` - Initialize the automation system and install cron jobs
- `./twotokens update` - Update TwoTokens.md file
- `./twotokens task list` - List all scheduled tasks
- `./twotokens cron install` - Install/update cron jobs
- `./twotokens cron list` - List current cron jobs

## Repository Structure

- `twotokens` - Main CLI script (Python)
- `cron_manager.py` - Cron job management functionality
- `config.json` - Configuration file with tasks and settings
- `setup.sh` - Setup script for system initialization
- `TwoTokens.md` - Target file for automation (created by system)
- `twotokens.log` - Log file for operations

## Architecture

The system consists of three main components:

1. **EventManager** (`twotokens:EventManager`): Core functionality for task management, file operations, and logging
2. **CronManager** (`cron_manager.py:CronManager`): Handles cron job installation, removal, and validation
3. **CLI Interface** (`twotokens:main`): Command-line interface with subcommands for different operations

## Configuration

The system uses `config.json` for configuration:
- `twotokens_file`: Target file path (default: TwoTokens.md)
- `log_file`: Log file path (default: twotokens.log)
- `tasks`: Array of scheduled tasks with name, command, and cron schedule

## Common Tasks

- Add new scheduled task: `./twotokens task add "task-name" "command" "cron-schedule"`
- Execute task immediately: `./twotokens task execute "task-name"`
- Install cron jobs: `./twotokens cron install`
- View logs: `cat twotokens.log`