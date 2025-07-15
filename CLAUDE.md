# CLAUDE.md

This file provides guidance to AI assistants when working with code in this repository.

## Project Overview

Super-OpenCode is a framework that extends OpenCode with specialized commands, personas, and intelligent orchestration. It provides 16 slash commands, 11 AI personas, and integration with external tools to enhance development workflows.

## Common Development Tasks

### Installation and Setup
```bash
# Install SuperClaude framework
python3 SuperClaude.py install --quick

# Install with specific profile
python3 SuperClaude.py install --profile developer

# Check system requirements
python3 SuperClaude.py install --diagnose

# List available components
python3 SuperClaude.py install --list-components

# Update existing installation
python3 SuperClaude.py update

# Create backup
python3 SuperClaude.py backup --create
```

### Development Commands
This project provides Claude Code slash commands, not traditional CLI tools:
- `/sc:implement` - Feature implementation
- `/sc:build` - Build and compilation workflows
- `/sc:test` - Testing workflows
- `/sc:analyze` - Code analysis
- `/sc:improve` - Code improvement
- `/sc:document` - Documentation generation

## High-Level Architecture

### Framework Structure
```
SuperClaude/
├── SuperClaude.py          # Main installer CLI entry point
├── SuperClaude/            # Framework documentation files
│   ├── Core/              # Core behavior docs (COMMANDS.md, FLAGS.md, etc.)
│   ├── Commands/          # 16 slash command definitions
│   └── Hooks/             # Hook system (placeholder for v4)
├── setup/                 # Installation system
│   ├── base/             # Base installer classes
│   ├── components/       # Component installers (core, commands, mcp)
│   ├── core/             # Core utilities (config, registry, validator)
│   ├── operations/       # CLI operations (install, update, uninstall, backup)
│   └── utils/            # UI, logging, security utilities
└── profiles/             # Installation profiles (quick, minimal, developer)
```

### Key Architecture Concepts

1. **Component System**: Modular installation system where each component (core, commands, mcp, hooks) can be installed independently with dependency resolution.

2. **Framework Documentation**: The `SuperOpenCode/Core/` directory contains behavior documentation that gets installed to `~/.opencode/` to guide OpenCode's behavior:
   - `CLAUDE.md` - Entry point with @includes
   - `COMMANDS.md` - Command definitions and execution patterns
   - `FLAGS.md` - Flag system and auto-activation rules
   - `PERSONAS.md` - 11 specialized AI personas
   - `MCP.md` - MCP server integration patterns
   - `ORCHESTRATOR.md` - Intelligent routing system
   - `MODES.md` - Operational modes (task management, introspection, token efficiency)

3. **Installation System**: Python-based installer that:
   - Validates system requirements
   - Resolves component dependencies
   - Backs up existing installations
   - Configures Claude Code's MCP settings

4. **Command System**: 16 specialized slash commands that enhance Claude Code with:
   - Wave orchestration for complex operations
   - Persona auto-activation based on context
   - MCP server coordination
   - Quality gates and validation

5. **Persona System**: Domain-specific AI behaviors:
   - Auto-activation based on context and keywords
   - Specialized decision frameworks
   - MCP server preferences
   - Cross-persona collaboration

## Key Implementation Details

### Installation Flow
1. `SuperClaude.py` serves as the unified CLI entry point
2. Operations are handled by modules in `setup/operations/`
3. Components are discovered and registered via `ComponentRegistry`
4. Installation validates requirements, resolves dependencies, and executes component installers
5. Framework files are copied to `~/.opencode/` and MCP servers are configured

### Component Dependencies
- `commands` depends on `core`
- `mcp` depends on `core`
- `hooks` depends on `core` (placeholder for v4)

### Configuration Management
- `ConfigManager` handles JSON configuration files
- `Validator` checks system requirements and dependencies
- `SettingsManager` manages Claude Code configuration updates

### No Traditional Testing Infrastructure
This project is a framework/configuration for Claude Code, not a traditional Python application. The `/sc:test` and `/sc:build` commands are definitions for Claude Code to use, not actual test runners or build scripts.

## Important Notes

1. **Framework, Not Application**: SuperClaude is documentation and configuration that guides Claude Code's behavior, not a standalone application.

2. **Version 3.0**: Fresh release with simplified architecture. Hooks system removed (coming in v4).

3. **MCP Integration**: Supports Context7 (documentation), Sequential (analysis), Magic (UI components), and Playwright (browser automation).

4. **Wave System**: Complex operations can use multi-stage orchestration with compound intelligence.

5. **Token Optimization**: Built-in compression and efficiency modes to handle longer conversations.