---
name: ds-plan-gaps
description: Create phases to close all gaps identified by milestone audit.
---

<objective>
Read the audit report from `/ds-audit-milestone` and automatically generate new tasks in `.ds/tasks.json` to close identified gaps.
</objective>

<process>
1. Read the latest `.ds/AUDIT-*.md` file.
2. Extract all gaps and regressions listed.
3. For each gap, create a new task in `.ds/tasks.json` with:
   - A clear description referencing the original requirement
   - The files likely to need changes
   - A verification command
   - Status: `"pending"`
4. Present the new tasks to the user for review.
5. Suggest running `/ds-execute` to begin closing gaps.
</process>
