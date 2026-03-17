---
name: ds-audit-milestone
description: Review milestone completion quality against original intent.
---

<objective>
Compare implemented work against the original SPEC.md and ROADMAP.md to identify gaps, regressions, or deviations.
</objective>

<process>
1. Read `.ds/SPEC.md` for original requirements.
2. Read `.ds/ROADMAP.md` for planned phases.
3. Read `.ds/progress.txt` for what was actually done.
4. Run ALL verification commands from completed tasks in `.ds/tasks.json`.
5. Produce an audit report:
   - **Requirements Met:** List of spec items that are implemented and verified.
   - **Gaps Found:** Requirements from SPEC.md that are missing or incomplete.
   - **Regressions:** Previously passing tasks that now fail verification.
   - **Recommendations:** Specific tasks to close gaps.
6. Save the report to `.ds/AUDIT-[milestone].md`.
7. If gaps are found, suggest running `/ds-plan-gaps` to generate fix tasks.
</process>
