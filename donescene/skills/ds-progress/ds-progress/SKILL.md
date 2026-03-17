---
name: ds-progress
description: Show current project position and task status.
---

<objective>
Display a dashboard showing the current state of the DoneScene project: which tasks are done, pending, and failed.
</objective>

<process>
1. Read `.ds/tasks.json`.
2. Read `.ds/ROADMAP.md` (if exists).
3. Calculate:
   - Total tasks, passed, pending, failed
   - Current milestone and phase
   - Completion percentage
4. Display a formatted dashboard:
```
⚔️ DoneScene Progress
━━━━━━━━━━━━━━━━━━━━
📊 Tasks: 5/12 complete (41%)
✅ Passed:  5
⏳ Pending: 6
❌ Failed:  1
📍 Current: Milestone 1, Phase 3
━━━━━━━━━━━━━━━━━━━━
```
5. List the next 3 pending tasks.
6. Suggest the next action (e.g., `/ds-execute`, `/ds-debug`, `/ds-plan`).
</process>
