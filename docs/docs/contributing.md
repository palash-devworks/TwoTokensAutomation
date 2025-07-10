---
layout: default
title: Contributing Guide
---

# Contributing to TwoTokens Automation

Thank you for your interest in contributing! This guide will help you get started.

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. Include:

- **Clear title** describing the issue
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Environment details** (OS, Python version)
- **Log files** or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the enhancement
- **Use case** explaining why it would be useful
- **Possible implementation** approach
- **Alternative solutions** considered

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following our standards
4. Add tests if applicable
5. Update documentation
6. Commit with clear messages
7. Push and create a Pull Request

## 🛠️ Development Setup

### Local Environment

```bash
# 1. Fork and clone
git clone https://github.com/yourusername/TwoTokensAutomation.git
cd TwoTokensAutomation

# 2. Install dependencies
pip3 install python-dateutil

# 3. Make scripts executable
chmod +x twotokens setup.sh

# 4. Run setup
./setup.sh

# 5. Test installation
./twotokens --help
```

### Testing Your Changes

```bash
# Basic functionality tests
./twotokens update
./twotokens task list
./twotokens event list

# Create test event
./twotokens event add "Test Event" "2025-12-31 23:59" \
  --sponsor "Test Sponsor" \
  --topic "Testing"

# Verify cron integration
./twotokens cron install
./twotokens cron list
```

## 📝 Coding Standards

### Python Style

- Follow **PEP 8** guidelines
- Use **meaningful names** for variables and functions
- Add **docstrings** to functions and classes
- Keep functions **focused and small**
- Use **type hints** where appropriate

### Code Example

```python
def create_event(name: str, date: str, sponsor: str = None) -> dict:
    """
    Create a new event with specified details.
    
    Args:
        name: Event name
        date: Event date in ISO format
        sponsor: Optional sponsor name
        
    Returns:
        dict: Created event object
        
    Raises:
        ValueError: If date format is invalid
    """
    # Implementation here
    pass
```

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good examples
git commit -m "Add email notification support for events"
git commit -m "Fix cron schedule validation for edge cases"
git commit -m "Update README with new installation instructions"

# Avoid
git commit -m "Fix bug"
git commit -m "Update stuff"
```

### Documentation

- Update README for new features
- Add docstrings to new functions
- Update API documentation
- Include usage examples

## 🏗️ Project Structure

```
TwoTokensAutomation/
├── twotokens              # Main CLI script
├── event_manager.py       # Event management system
├── cron_manager.py        # Cron job management
├── config.json           # Default configuration
├── setup.sh              # Setup script
├── docs/                 # Documentation and website
│   ├── index.md          # Homepage
│   ├── _config.yml       # Jekyll configuration
│   └── docs/             # Documentation pages
├── README.md             # Project overview
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
└── CLAUDE.md            # Development guide
```

## 🎯 Areas for Contribution

### High Priority

#### Email/Slack Integrations
Add notification backends for popular services:

```python
# Example integration structure
class NotificationBackend:
    def send_notification(self, message: str, recipients: list):
        raise NotImplementedError

class SlackBackend(NotificationBackend):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def send_notification(self, message: str, recipients: list):
        # Implementation
        pass
```

#### Event Templates
Create configurable event templates:

```json
{
  "templates": {
    "conference": {
      "pre_event_days": [14, 7, 3, 1],
      "post_event_days": [1, 7],
      "default_tasks": [...]
    }
  }
}
```

#### Error Handling
Improve error messages and recovery:

- Better validation messages
- Graceful error recovery
- User-friendly error explanations

#### Testing Framework
Add comprehensive test suite:

```python
import unittest
from event_manager import EventManager

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager("test_config.json")
    
    def test_create_event(self):
        # Test implementation
        pass
```

### Medium Priority

#### Web Dashboard
Simple web interface for management:

- Flask/FastAPI backend
- React/Vue.js frontend
- REST API endpoints

#### Calendar Integration
Connect with popular calendar systems:

- Google Calendar API
- Outlook Calendar API
- iCal format support

#### Advanced Scheduling
More flexible scheduling options:

- Relative scheduling (X days before event)
- Business day awareness
- Holiday exclusions

### Nice to Have

#### Docker Support
Containerization for easy deployment:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["./twotokens", "cron", "install"]
```

#### Plugin System
Extensible architecture:

```python
class Plugin:
    def on_event_created(self, event):
        pass
    
    def on_task_executed(self, task):
        pass
```

## 🧪 Testing Guidelines

### Manual Testing

Before submitting:

1. **Basic Operations**
   ```bash
   ./twotokens update
   ./twotokens task list
   ./twotokens event list
   ```

2. **Event Lifecycle**
   ```bash
   # Create event
   ./twotokens event add "Test" "2025-12-31 12:00"
   
   # Verify tasks created
   ./twotokens task list
   
   # Test notifications
   ./twotokens event notify all "Test"
   
   # Complete event
   ./twotokens event complete "Test"
   ```

3. **Cron Integration**
   ```bash
   ./twotokens cron install
   ./twotokens cron list
   ./twotokens cron remove
   ```

### Error Scenarios

Test error handling:

- Invalid date formats
- Missing permissions
- Corrupted configuration
- Network failures

## 📋 Development Workflow

### Feature Development

1. **Create Issue**
   - Describe the feature
   - Discuss implementation approach
   - Get feedback from maintainers

2. **Fork and Branch**
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Implement**
   - Write code following standards
   - Add tests
   - Update documentation

4. **Test Thoroughly**
   - Manual testing
   - Edge cases
   - Error scenarios

5. **Submit PR**
   - Clear description
   - Link to issue
   - Request review

### Bug Fixes

1. **Reproduce Bug**
   - Create minimal test case
   - Document exact steps

2. **Fix Implementation**
   - Minimal changes
   - Address root cause
   - Add regression test

3. **Verify Fix**
   - Test original scenario
   - Test related functionality
   - Check for side effects

## 🔍 Code Review Process

### For Contributors

- **Self-review** before submitting
- **Respond promptly** to feedback
- **Update based** on suggestions
- **Ask questions** if unclear

### Review Criteria

- **Functionality** - Does it work as intended?
- **Code Quality** - Is it clean and maintainable?
- **Testing** - Is it adequately tested?
- **Documentation** - Is it properly documented?
- **Compatibility** - Does it break existing functionality?

## 🚀 Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes

### Release Checklist

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Test on multiple platforms
- [ ] Update documentation
- [ ] Create GitHub release
- [ ] Update website

## 📞 Getting Help

### Communication Channels

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - General questions and ideas
- **Pull Request Reviews** - Code-specific discussions

### Response Times

- **Issues** - Within 48 hours
- **Pull Requests** - Within 72 hours
- **Security Issues** - Within 24 hours

## 🎉 Recognition

Contributors are recognized in:

- **CONTRIBUTORS.md** file
- **Release notes**
- **GitHub contributors graph**
- **Special mentions** for significant contributions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to TwoTokens Automation!** 🚀

Your contributions help make event automation better for everyone.