# Super-OpenCode v3 🚀
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/grimmolf/super-opencode)
[![GitHub issues](https://img.shields.io/github/issues/grimmolf/super-opencode)](https://github.com/grimmolf/super-opencode/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/grimmolf/super-opencode/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/grimmolf/super-opencode)](https://github.com/grimmolf/super-opencode/graphs/contributors)

A framework that extends OpenCode with specialized commands, personas, and intelligent orchestration.

**📢 Status**: Initial release, fresh out of beta! Bugs may occur as we continue improving things.

## What is Super-OpenCode? 🤔

Super-OpenCode enhances OpenCode for development work by adding:
- 🛠️ **16 specialized commands** for common dev tasks (some work better than others!)
- 🎭 **Smart personas** that usually pick the right expert for different domains 
- 🔧 **MCP server integration** for docs, UI components, and browser automation
- 📋 **Task management** that tries to keep track of progress
- ⚡ **Token optimization** to help with longer conversations

This is what we've been building to make development workflows smoother. Still rough around the edges, but getting better! 😊

## Current Status 📊

✅ **What's Working Well:**
- Installation suite (rewritten from the ground up)
- Core framework with 9 documentation files 
- 16 slash commands for various development tasks
- MCP server integration (Context7, Sequential, Magic, Playwright)
- Unified CLI installer for easy setup

⚠️ **Known Issues:**
- This is an initial release - bugs are expected
- Some features may not work perfectly yet
- Documentation is still being improved
- Hooks system was removed (coming back in v4)

## Key Features ✨

### Commands 🛠️
We focused on 16 essential commands for the most common tasks:

**Development**: `/sc:implement`, `/sc:build`, `/sc:design`  
**Analysis**: `/sc:analyze`, `/sc:troubleshoot`, `/sc:explain`  
**Quality**: `/sc:improve`, `/sc:test`, `/sc:cleanup`  
**Others**: `/sc:document`, `/sc:git`, `/sc:estimate`, `/sc:task`, `/sc:index`, `/sc:load`, `/sc:spawn`

### Smart Personas 🎭
AI specialists that try to jump in when they seem relevant:
- 🏗️ **architect** - Systems design and architecture stuff
- 👨‍💻 **senior-developer** - Main programming work (default)
- 🎯 **frontend** - UI/UX wizardry 
- ⚙️ **backend** - Server-side systems
- 🔬 **analyzer** - Code quality checks
- 📝 **documentation** - Docs that actually help
- 🔍 **code-reviewer** - Spots issues before they happen
- 🌐 **devops** - Infrastructure and deployment
- 🛡️ **security** - Security vulnerability finder
- ⚡ **performance** - Speed optimization
- 🧪 **qa** - Testing strategies

### MCP Servers 🔧
Pre-configured integrations:
- **context7** - Documentation and example access
- **sequential** - Sequential code analysis
- **magic** - UI component generation 
- **playwright** - Browser automation

### Operational Modes 💫
- **Task Management** - Keeps track of what's being worked on
- **Introspection Mode** - AI thinks step-by-step 
- **Token Efficiency** - Compressed outputs for longer chats

## Installation 📦

### Prerequisites
- Python 3.8+
- OpenCode installed and configured
- macOS, Linux, or Windows

### Cleanup (if upgrading)
If you're coming from Super-OpenCode v2, you'll need to clean up first:

1. Delete old files:
   - `~/.opencode/CLAUDE.md`
   - `SuperOpenCode/`

2. Remove MCP server configs from `claude_desktop_config.json`

### Quick Start

```bash
# Clone the repository
git clone https://github.com/grimmolf/super-opencode.git
cd super-opencode

# Run the installer
python3 SuperOpenCode.py install --quick
```

This quick install gives you:
- Core framework
- Essential commands
- Basic MCP servers

### Installation Options

**Minimal Install** (just the basics):
```bash
python3 SuperOpenCode.py install --minimal
```

**Developer Profile** (recommended for most):
```bash
python3 SuperOpenCode.py install --profile developer
```

**Full Installation** (everything):
```bash
python3 SuperOpenCode.py install
```

**See what's available**:
```bash
python3 SuperOpenCode.py install --list-components
```

The installer handles everything: framework files, MCP servers, and OpenCode configuration.

## How It Works 🔧

Super-OpenCode enhances OpenCode through:

1. **Framework Files** - Documentation installed to `~/.opencode/` that guides how the AI responds
2. **Command System** - Slash commands that trigger specialized workflows
3. **Persona Intelligence** - Domain experts that activate based on context
4. **MCP Integration** - External tools for enhanced capabilities

Most of the time it plays nicely with OpenCode's existing stuff. 🤝

## Getting Help 🆘

- **Issues**: Found a bug? [Open an issue](https://github.com/grimmolf/super-opencode/issues)
- **Questions**: Check existing issues first
- **Contributing**: PRs welcome! See CONTRIBUTING.md

## Customization 🎨

### Disable Specific Features
You can turn off personas or MCP servers you don't need by editing the config files.

### Custom Personas
After installation, you can customize Super-OpenCode by editing:
- `~/.opencode/PERSONAS.md` - Modify persona behaviors
- `~/.opencode/COMMANDS.md` - Customize command workflows

## Troubleshooting 🔍

**Installation fails?**
```bash
python3 SuperOpenCode.py install --diagnose
```

**Need to uninstall?**
```bash
python3 SuperOpenCode.py uninstall
```

**Want to update?**
```bash
python3 SuperOpenCode.py update
```

## Project Structure 📁

```
Super-OpenCode/
├── SuperOpenCode.py          # Main installer CLI
├── SuperOpenCode/            # Framework files  
│   ├── Core/                # Core behaviors
│   ├── Commands/            # Command definitions
│   └── Hooks/               # (Placeholder for v4)
├── setup/                   # Installation system
│   ├── base/               # Base classes
│   ├── components/         # Component installers
│   ├── core/               # Core utilities
│   ├── operations/         # CLI operations
│   └── utils/              # Helper utilities
└── profiles/               # Installation profiles
```

## FAQs 🤷

**Q: Does this work with other AI tools?**  
A: Currently OpenCode only, but v4 will have broader compatibility.

**Q: Can I use this without MCP servers?**  
A: Yes! Use `--minimal` install or disable them in config.

## Super-OpenCode Contributors

[![Contributors](https://contrib.rocks/image?repo=grimmolf/super-opencode)](https://github.com/grimmolf/super-opencode/graphs/contributors)

---

**Note**: This is an early release. We're actively improving things based on feedback. Your patience and bug reports are appreciated! 🙏

## Star History

<a href="https://www.star-history.com/#grimmolf/super-opencode&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=grimmolf/super-opencode&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=grimmolf/super-opencode&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=grimmolf/super-opencode&type=Date" />
 </picture>
</a>