---
name: ds-list-assumptions
description: Surface planning assumptions for a phase.
---

<objective>
List all assumptions the AI is making about the approach for a phase so the user can validate or correct them before planning.
</objective>

<process>
1. Read `.ds/ROADMAP.md` and `.ds/SPEC.md`.
2. For the requested phase, list assumptions about:
   - Tech stack and libraries to use
   - Architecture patterns to follow
   - File/folder structure
   - Testing approach
   - Integration with existing code
3. Present as a numbered list. Ask the user to confirm, reject, or modify each assumption.
4. Save confirmed assumptions to `.ds/PHASE-[N]-ASSUMPTIONS.md`.
</process>
