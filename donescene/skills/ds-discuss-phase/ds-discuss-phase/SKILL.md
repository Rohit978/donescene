---
name: ds-discuss-phase
description: Clarify phase scope through adaptive questioning before planning.
---

<objective>
Have a focused conversation with the user to clarify the scope, constraints, and acceptance criteria of a specific phase before running `/ds-plan`.
</objective>

<process>
1. Read `.ds/ROADMAP.md` to understand the phase the user wants to discuss.
2. Read `.ds/SPEC.md` and `.ds/AGENTS.md` for project context.
3. Ask 3-5 targeted questions about:
   - **Scope boundaries:** What is IN and OUT of this phase?
   - **Technical approach:** Any preferred libraries, patterns, or constraints?
   - **Acceptance criteria:** How will we know this phase is done?
   - **Dependencies:** Does this phase depend on prior phases being complete?
   - **Edge cases:** Any known tricky scenarios to handle?
4. Summarize the discussion as a phase brief and save to `.ds/PHASE-[N]-BRIEF.md`.
5. Suggest running `/ds-plan [N]` to generate tasks based on the discussion.
</process>
