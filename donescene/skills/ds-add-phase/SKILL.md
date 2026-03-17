---
name: ds-add-phase
description: Add a new phase to the end of the current milestone in the roadmap.
---

<objective>
Append a new phase to the current milestone in `.ds/ROADMAP.md`.
</objective>

<process>
1. Read `.ds/ROADMAP.md` to identify the current milestone and its last phase number.
2. Ask the user what the new phase should accomplish (if not already stated).
3. Append the new phase at the end of the current milestone with the next sequential number.
4. Notify the user. Suggest `/ds-plan [N]` to plan the new phase.
</process>
