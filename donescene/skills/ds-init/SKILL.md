---
name: ds-init
description: Scaffold the DoneScene Autonomous Protocol into the current directory.
---

<objective>
Initialize the current directory with the DoneScene (DS) tracking folders and protocol files.
</objective>

<process>
1. Create a `.ds/` folder in the current project root.
2. Create `.ds/tasks.json` with an empty task template including `id`, `priority`, `description`, `files_to_edit`, `verification_command`, and `status` fields.
3. Create `.ds/progress.txt` with header: `# DoneScene Progress Log`.
4. Create `.ds/AGENTS.md` with sections for Codebase Patterns and Gotchas.
5. Create `ds-protocol.md` in the project root with the core protocol rules.
6. Notify the user that DoneScene is initialized and they should run `/ds-plan` to generate tasks.
</process>
