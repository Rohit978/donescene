---
name: ds-resume
description: Restore context from last session.
---

<objective>
Read the handoff document and restore full project context so the agent can continue work seamlessly.
</objective>

<process>
1. Read `.ds/HANDOFF.md` (created by `/ds-pause`).
2. Read `.ds/tasks.json` and `.ds/AGENTS.md` for current state.
3. Display a summary of where we left off:
   - Last completed task
   - Next pending task
   - Any known issues
4. Suggest the next action: `/ds-execute` to continue, `/ds-debug` if there are failures, or `/ds-progress` for overview.
</process>
