---
name: ds-remove-phase
description: Remove a phase from the roadmap with safety checks.
---

<objective>
Remove a phase from `.ds/ROADMAP.md` after confirming it has no completed work, and renumber remaining phases.
</objective>

<process>
1. Read `.ds/ROADMAP.md` and `.ds/tasks.json`.
2. Identify the phase the user wants to remove.
3. **Safety Check:** If ANY tasks associated with this phase have `"status": "passed"`, warn the user that completed work exists and ask for explicit confirmation.
4. If confirmed (or no completed work):
   a. Remove the phase from `ROADMAP.md`.
   b. Remove associated tasks from `tasks.json`.
   c. Renumber subsequent phases.
5. Log the removal in `.ds/progress.txt`.
6. Notify the user of the updated roadmap.
</process>
