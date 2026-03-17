---
name: ds-insert-phase
description: Insert an urgent phase between existing phases and renumber.
---

<objective>
Insert a new phase at a specific position in the roadmap and renumber all subsequent phases.
</objective>

<process>
1. Read `.ds/ROADMAP.md`.
2. Ask the user WHERE to insert the phase (e.g., "after Phase 3") and WHAT it should do.
3. Insert the new phase at the requested position.
4. Renumber all subsequent phases sequentially.
5. Update any task references in `.ds/tasks.json` if they reference phase numbers.
6. Notify the user of the updated roadmap.
</process>
