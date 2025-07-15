# Super-OpenCode Integration PRP

## Context
Transform Super-OpenCode from an AI documentation framework into native opencode custom commands. This requires implementing a two-layer architecture: Go-based TUI command registration and TypeScript tool implementations, while preserving Super-OpenCode's sophisticated command orchestration, persona intelligence, and workflow automation capabilities.

## Research Findings

### OpenCode Architecture Patterns

#### 1. Command Implementation (Go Layer)
Location: `packages/tui/internal/commands/command.go`

```go
// Command structure
type Command struct {
    Name        CommandName
    Description string
    Keybindings []Keybinding
    Trigger     []string  // Text triggers in chat
}

// Command execution in tui.go
func (a appModel) executeCommand(command commands.Command) (tea.Model, tea.Cmd) {
    switch command.Name {
    case commands.AppHelpCommand:
        // Handle command
    }
}
```

#### 2. Tool Implementation (TypeScript Layer)
Location: `packages/opencode/src/tool/tool.ts`

```typescript
export namespace Tool {
  export interface Info<Parameters, Metadata> {
    id: string
    description: string
    parameters: Parameters
    execute(args: Parameters, ctx: Context): Promise<{
      title: string
      metadata: Metadata
      output: string
    }>
  }
}
```

Example implementation: `packages/opencode/src/tool/read.ts`

#### 3. Mode System
Location: `packages/opencode/src/session/mode.ts`

```typescript
export namespace Mode {
  export const Info = z.object({
    name: z.string(),
    model: z.object({
      modelID: z.string(),
      providerID: z.string(),
    }).optional(),
    prompt: z.string().optional(),
    tools: z.record(z.boolean()),
  })
}
```

#### 4. Configuration Extension
Location: `packages/opencode/src/config/config.ts`

Uses Zod schemas with `.strict()` for validation. Can be extended by adding new fields to the schema.

### Super-OpenCode Components to Transform

1. **16 Commands**: analyze, build, implement, improve, test, document, etc.
2. **11 Personas**: architect, frontend, backend, analyzer, security, etc.
3. **Orchestration**: Routing logic, wave system, quality gates
4. **Flag System**: Auto-activation, precedence rules, compression modes
5. **Token Optimization**: Ultra-compressed mode, symbol system

## External Documentation

- Go Bubbletea TUI Framework: https://github.com/charmbracelet/bubbletea
- Bun Documentation: https://bun.sh/docs
- TypeScript Handbook: https://www.typescriptlang.org/docs/
- Zod Schema Validation: https://zod.dev/
- Go Testing: https://golang.org/doc/tutorial/add-a-test
- Bun Test Framework: https://bun.sh/docs/cli/test

## Implementation Plan

### Phase 1: Command Infrastructure (Week 1)

#### Task 1.1: Extend Go Command Registry
File: `packages/tui/internal/commands/command.go`

Add SuperClaude command constants:
```go
const (
    // SuperClaude Commands
    SCAnalyzeCommand    CommandName = "sc_analyze"
    SCBuildCommand      CommandName = "sc_build"
    SCImplementCommand  CommandName = "sc_implement"
    // ... all 16 commands
)
```

Update `LoadFromConfig` function to register commands:
```go
{
    Name:        SCAnalyzeCommand,
    Description: "analyze code/architecture (SuperClaude)",
    Trigger:     []string{"analyze", "sc:analyze"},
    Keybindings: parseBindings("<leader>sa"),
},
```

#### Task 1.2: Handle Commands in TUI
File: `packages/tui/internal/tui/tui.go`

Extend `executeCommand` function:
```go
case commands.SCAnalyzeCommand:
    // Forward to TypeScript via API call
    response, err := a.app.Client.SuperClaude.ExecuteCommand(
        context.Background(),
        opencode.SuperClaudeCommandParams{
            Command: "analyze",
            Args: a.editor.Value(),
        },
    )
```

### Phase 2: TypeScript Implementation (Week 2)

#### Task 2.1: Create SuperClaude Module Structure
```
packages/opencode/src/superclaude/
├── index.ts                  # Main exports and registration
├── commands/                 # Command tool implementations
│   ├── analyze.ts
│   ├── build.ts
│   └── ...
├── personas/                 # Persona mode implementations
│   ├── architect.ts
│   └── ...
├── orchestrator/            # Routing logic
│   ├── router.ts
│   ├── wave.ts
│   └── quality-gates.ts
└── modes/                   # Operational modes
    └── token-efficiency.ts
```

#### Task 2.2: Implement Base Command Tool
File: `packages/opencode/src/superclaude/commands/analyze.ts`

```typescript
import { Tool } from "../../tool/tool"
import { z } from "zod"
import { Orchestrator } from "../orchestrator/router"
import { PersonaManager } from "../personas"

export const AnalyzeTool = Tool.define({
  id: "sc_analyze",
  description: "Multi-dimensional code and system analysis",
  parameters: z.object({
    target: z.string().describe("Target to analyze"),
    flags: z.object({
      code: z.boolean().optional(),
      arch: z.boolean().optional(),
      security: z.boolean().optional(),
      // ... other flags
    }).optional(),
  }),
  async execute(params, ctx) {
    // 1. Parse flags and determine analysis type
    const flags = params.flags || {}
    
    // 2. Auto-activate appropriate persona
    const persona = await PersonaManager.autoActivate({
      command: "analyze",
      flags,
      context: params.target,
    })
    
    // 3. Route through orchestrator
    const result = await Orchestrator.execute({
      command: "analyze",
      params,
      persona,
      ctx,
    })
    
    return {
      title: `Analysis: ${params.target}`,
      metadata: { persona: persona.name, flags },
      output: result.output,
    }
  }
})
```

### Phase 3: Persona System (Week 3)

#### Task 3.1: Extend Mode System
File: `packages/opencode/src/superclaude/personas/index.ts`

```typescript
import { Mode } from "../../session/mode"
import { z } from "zod"

export const PersonaMode = Mode.Info.extend({
  persona: z.string(),
  priorities: z.object({
    primary: z.string(),
    secondary: z.array(z.string()),
  }),
  autoActivation: z.object({
    keywords: z.array(z.string()),
    patterns: z.array(z.string()),
    confidence: z.number(),
  }),
})

export const PERSONAS = {
  architect: {
    name: "architect",
    prompt: "You are a systems architecture specialist...",
    priorities: {
      primary: "maintainability",
      secondary: ["scalability", "performance"],
    },
    autoActivation: {
      keywords: ["architecture", "design", "scalability"],
      patterns: ["system-wide", "architectural"],
      confidence: 0.85,
    },
    tools: {
      // Tool availability
    },
  },
  // ... other personas
}
```

#### Task 3.2: Register Personas as Modes
File: `packages/opencode/src/superclaude/index.ts`

```typescript
import { App } from "../app/app"
import { PERSONAS } from "./personas"

export async function registerSuperClaude() {
  // Register personas as modes
  for (const [key, persona] of Object.entries(PERSONAS)) {
    await App.state("mode").then(modes => {
      modes[`sc_${key}`] = persona
    })
  }
  
  // Register tools
  // ... tool registration
}
```

### Phase 4: Orchestration Engine (Week 4)

#### Task 4.1: Port Routing Logic
File: `packages/opencode/src/superclaude/orchestrator/router.ts`

```typescript
export namespace Orchestrator {
  export async function execute(input: {
    command: string
    params: any
    persona: Persona
    ctx: Tool.Context
  }) {
    // 1. Analyze complexity
    const complexity = analyzeComplexity(input)
    
    // 2. Determine if wave mode needed
    if (complexity.score > 0.7 && complexity.files > 20) {
      return await WaveOrchestrator.execute(input)
    }
    
    // 3. Route to appropriate tools
    const tools = selectTools(input)
    
    // 4. Execute with quality gates
    return await executeWithQualityGates(tools, input)
  }
}
```

### Phase 5: Configuration Extension (Week 5)

#### Task 5.1: Extend Config Schema
File: `packages/opencode/src/config/config.ts`

Add to the Info schema:
```typescript
superclaude: z.object({
  enabled: z.boolean().default(true),
  defaultPersona: z.string().optional(),
  tokenMode: z.enum(["auto", "compressed", "ultra"]).default("auto"),
  waveThreshold: z.number().default(0.7),
  commands: z.record(z.string(), z.object({
    enabled: z.boolean().default(true),
    autoPersona: z.boolean().default(true),
  })).optional(),
}).optional(),
```

## Validation Gates

### TypeScript/Bun Tests
```bash
# Type checking
bun run typecheck

# Unit tests for tools
bun test src/superclaude/commands/*.test.ts

# Integration tests
bun test src/superclaude/integration.test.ts
```

### Go Tests
```bash
# Test command registration
cd packages/tui && go test ./internal/commands/...

# Test TUI integration
go test ./internal/tui/...
```

### End-to-End Tests
```bash
# Test command triggers
bun test e2e/superclaude-commands.test.ts

# Test persona switching
bun test e2e/superclaude-personas.test.ts
```

## Error Handling Strategy

1. **Command Not Found**: Suggest similar commands
2. **Tool Execution Failure**: Graceful degradation with fallback
3. **Persona Activation Error**: Default to base behavior
4. **Wave Orchestration Timeout**: Break into smaller operations

## Gotchas and Considerations

1. **Go-TypeScript Bridge**: The TUI (Go) needs to communicate with TypeScript tools via the API client. Ensure the stainless SDK is regenerated after adding new endpoints.

2. **Trigger Conflicts**: Some SuperClaude triggers might conflict with existing opencode commands. Use "sc:" prefix as fallback.

3. **State Management**: Persona and wave state needs to persist across the session. Use App.state pattern.

4. **Token Limits**: Ultra-compressed mode needs careful implementation to avoid information loss.

5. **Testing Personas**: Personas change behavior dynamically, making testing complex. Use snapshot testing for outputs.

## Implementation Order

1. **Week 1**: Basic command infrastructure and registration
2. **Week 2**: Core command tools (analyze, build, implement)
3. **Week 3**: Persona system and mode integration
4. **Week 4**: Orchestration engine and routing
5. **Week 5**: Configuration, testing, and polish

## Success Criteria

- [ ] All 16 SuperClaude commands work via triggers
- [ ] 11 personas activate intelligently based on context
- [ ] Wave orchestration handles complex operations
- [ ] Token optimization reduces usage by 30-50%
- [ ] Commands feel native to opencode
- [ ] All tests pass
- [ ] Documentation complete

## Confidence Score: 8/10

High confidence due to:
- Clear architecture patterns in opencode
- Well-defined interfaces (Tool.Info, Mode.Info)
- Existing extension points (commands, modes, config)

Moderate risk areas:
- Go-TypeScript communication complexity
- State management across layers
- Testing dynamic persona behavior

The comprehensive context and clear implementation patterns should enable successful one-pass implementation.