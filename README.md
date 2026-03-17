# DoneScene

**DoneScene (DS)** is a structured task-planning and execution protocol for AI-assisted coding inside [Antigravity](https://antigravity.dev). Install via pip, and all 22 `/ds-*` slash commands become available in your Antigravity editor.

## Install

```bash
pip install git+https://github.com/rohittce/donescene.git
```

After install, run the skills installer:

```bash
donescene
```

This copies the 22 skill folders into `~/.gemini/antigravity/skills/`. Restart Antigravity, type `/ds`, and you're ready!

### Update to Latest

```bash
pip install --upgrade git+https://github.com/rohittce/donescene.git
donescene --force
```

### Uninstall

```bash
donescene --uninstall
pip uninstall donescene
```

## Available Commands

| Command | Description |
|---|---|
| `/ds-init` | Scaffold DoneScene into a project |
| `/ds-map` | Analyze codebase and generate ARCHITECTURE.md |
| `/ds-plan` | Decompose requirements into atomic tasks |
| `/ds-execute` | Execute one pending task |
| `/ds-verify` | Validate completed task with proof |
| `/ds-debug` | Systematic debugging with 3-strike rule |
| `/ds-new-project` | Initialize a new project with deep context |
| `/ds-new-milestone` | Create a new milestone with phases |
| `/ds-discuss-phase` | Clarify phase scope before planning |
| `/ds-research-phase` | Deep technical research for a phase |
| `/ds-add-phase` | Add a new phase to the current milestone |
| `/ds-insert-phase` | Insert an urgent phase between existing ones |
| `/ds-remove-phase` | Remove a phase from the roadmap |
| `/ds-list-assumptions` | Surface planning assumptions |
| `/ds-plan-gaps` | Create phases to close audit gaps |
| `/ds-audit-milestone` | Review milestone completion quality |
| `/ds-complete-milestone` | Archive milestone and prepare for next |
| `/ds-add-todo` | Capture an idea or task as a quick todo |
| `/ds-check-todos` | List and work on pending todos |
| `/ds-progress` | Show current project position and status |
| `/ds-pause` | Save state for session handoff |
| `/ds-resume` | Restore context from last session |

## Quick Start

```bash
# 1. Install
pip install git+https://github.com/rohittce/donescene.git
donescene

# 2. In any project, initialize DoneScene
#    (type in Antigravity chat)
/ds-init

# 3. Map the codebase
/ds-map

# 4. Plan your tasks
/ds-plan

# 5. Execute tasks one at a time
/ds-execute
```

## License

MIT
