---
name: ds-verify
description: Validate completed tasks with proof of correctness.
---

<objective>
Run verification commands for all `"passed"` tasks in `.ds/tasks.json` and produce a verification report.
</objective>

<process>
1. Read `.ds/tasks.json`.
2. For each task with `"status": "passed"`:
   a. Run its `verification_command` in the terminal.
   b. Record PASS or FAIL with the output.
3. If any task FAILS verification:
   - Mark it back to `"status": "pending"` in `tasks.json`.
   - Append the failure details to `.ds/progress.txt`.
4. Generate a verification summary table showing Task ID, Description, and Result.
5. Notify the user of results. If all pass, confirm the milestone is verified.
</process>
