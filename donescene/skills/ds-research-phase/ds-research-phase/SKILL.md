---
name: ds-research-phase
description: Deep technical research for a phase before planning.
---

<objective>
Research the technical approach for a specific phase by analyzing the codebase, reading documentation, and exploring implementation options.
</objective>

<process>
1. Read `.ds/ROADMAP.md` to understand the phase.
2. Read `.ds/ARCHITECTURE.md` (if it exists) for codebase context.
3. Analyze relevant source files to understand existing patterns.
4. Research:
   - **Implementation approaches:** What are the options? Pros/cons of each.
   - **Library choices:** What existing packages can help?
   - **Codebase integration:** How does this fit with existing architecture?
   - **Risks:** What could go wrong? Performance, security, compatibility.
5. Produce a research report at `.ds/RESEARCH-PHASE-[N].md` with:
   - Recommended approach with justification
   - Alternative approaches considered
   - Key decisions that need user input
   - Estimated complexity
6. Suggest running `/ds-plan [N]` after the user reviews the research.
</process>
