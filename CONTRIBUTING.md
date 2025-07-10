# Contributing to TwoTokens Automation

Thank you for your interest in contributing to TwoTokens Automation! We welcome contributions from everyone.

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow:

- Be respectful and inclusive
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the behavior
- Expected behavior vs actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant log files or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear and descriptive title
- A detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- Consider if there are alternative solutions

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** if applicable
4. **Update documentation** if needed
5. **Ensure all tests pass**
6. **Create a pull request** with a clear title and description

## Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/TwoTokensAutomation.git
   cd TwoTokensAutomation
   ```

2. **Install dependencies**
   ```bash
   pip3 install python-dateutil
   ```

3. **Run the setup**
   ```bash
   ./setup.sh
   ```

4. **Test your changes**
   ```bash
   ./twotokens --help
   ./twotokens task list
   ```

## Coding Standards

### Python Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

### Commit Messages
- Use clear and meaningful commit messages
- Start with a capital letter
- Use imperative mood ("Add feature" not "Added feature")
- Reference issues when applicable (#123)

### Testing
- Test new features thoroughly
- Ensure existing functionality still works
- Test edge cases and error conditions

## Project Structure

```
TwoTokensAutomation/
├── twotokens              # Main CLI script
├── event_manager.py       # Event management system
├── cron_manager.py        # Cron job management
├── config.json           # Configuration file
├── setup.sh              # Setup script
├── README.md             # Project documentation
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT license
└── CLAUDE.md            # Development guide
```

## Areas for Contribution

We welcome contributions in these areas:

### High Priority
- **Email/Slack Integrations** - Add notification backends
- **Event Templates** - Configurable event templates
- **Error Handling** - Improve error messages and recovery
- **Testing** - Add comprehensive test suite
- **Documentation** - Improve and expand documentation

### Medium Priority
- **Web Dashboard** - Simple web interface
- **Calendar Integration** - Google Calendar, Outlook integration
- **Advanced Scheduling** - More flexible scheduling options
- **Reporting** - Event and task analytics
- **Configuration Validation** - Better config validation

### Nice to Have
- **Docker Support** - Containerization
- **REST API** - Remote management API
- **Plugin System** - Extensible plugin architecture
- **Multi-language Support** - Internationalization

## Questions?

If you have questions about contributing, please:

1. Check existing issues and discussions
2. Create a new issue with the "question" label
3. Reach out to the maintainers

Thank you for contributing to TwoTokens Automation! 🚀