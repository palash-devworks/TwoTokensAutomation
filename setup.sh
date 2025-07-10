#!/bin/bash

# TwoTokens Automation Setup Script
# This script sets up the TwoTokens automation system and installs cron jobs

set -e

echo "🚀 Setting up TwoTokens Automation..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3 first."
    exit 1
fi

# Make the main script executable
chmod +x twotokens

# Create initial TwoTokens.md file if it doesn't exist
if [ ! -f "TwoTokens.md" ]; then
    echo "📄 Creating initial TwoTokens.md file..."
    ./twotokens update
fi

# Install cron jobs
echo "⏰ Installing cron jobs..."
python3 -c "
import sys
sys.path.insert(0, '.')
from cron_manager import CronManager
import json

# Load event manager
class MockEventManager:
    def __init__(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)
    
    def log_message(self, message):
        print(message)

event_manager = MockEventManager()
cron_manager = CronManager(event_manager)
cron_manager.install_cron_jobs()
"

echo "✅ Setup complete!"
echo ""
echo "Available commands:"
echo "  ./twotokens update                    - Update TwoTokens.md file"
echo "  ./twotokens task list                 - List all scheduled tasks"
echo "  ./twotokens task add <name> <cmd> <schedule> - Add new task"
echo "  ./twotokens cron list                 - List current cron jobs"
echo "  ./twotokens cron install              - Install/update cron jobs"
echo "  ./twotokens cron remove               - Remove all cron jobs"
echo ""
echo "Example schedules:"
echo "  '0 9 * * *'     - Daily at 9 AM"
echo "  '0 */6 * * *'   - Every 6 hours"
echo "  '0 0 * * 0'     - Weekly on Sunday at midnight"
echo "  '0 0 1 * *'     - Monthly on the 1st at midnight"
echo ""
echo "📋 Current scheduled tasks:"
./twotokens task list