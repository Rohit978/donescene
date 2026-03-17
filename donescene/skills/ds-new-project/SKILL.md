---
name: ds-new-project
description: Initialize a new project with deep context gathering and SPEC.md.
---

<objective>
Guide the user through a structured questioning flow to deeply understand their project idea, then generate `.ds/SPEC.md` (requirements), `.ds/ROADMAP.md` (milestones and phases), and scaffold the DoneScene tracking files.
</objective>

<process>
## Step 1: Deep Questioning (Max 5 questions)
Ask the user about:
1. **What** — What does the project do? Who is the target user?
2. **Tech Stack** — Any preferences? (Language, framework, database)
3. **Scope** — What is the MVP? What can wait for v2?
4. **Constraints** — Deadlines, performance requirements, existing code?
5. **Testing** — How should we verify correctness? (unit tests, manual, CI)

## Step 2: Generate SPEC.md
Create `.ds/SPEC.md` with:
- **Project Name & Description**
- **Target Users**
- **Core Features (MVP)**
- **Tech Stack**
- **Non-Functional Requirements** (performance, security)
- **Out of Scope (v2+)**

## Step 3: Generate ROADMAP.md
Create `.ds/ROADMAP.md` breaking the MVP into sequential milestones, each with phases:
```markdown
# Roadmap
## Milestone 1: Core Foundation
- Phase 1: Project setup and configuration
- Phase 2: Data models and database
- Phase 3: Core API endpoints
## Milestone 2: User Interface
- Phase 4: Component library
- Phase 5: Main pages
```

## Step 4: Scaffold DoneScene
Run `/ds-init` to create `.ds/tasks.json`, `AGENTS.md`, and `progress.txt`.

## Step 5: Route to Planning
Tell the user to run `/ds-plan 1` to plan Phase 1.
</process>
