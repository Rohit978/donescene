---
name: ds-complete-milestone
description: Archive a completed milestone and prepare for the next.
---

<objective>
Verify all phases in the current milestone are complete, archive the milestone data, and prepare for the next milestone.
</objective>

<process>
1. Read `.ds/tasks.json` and confirm all tasks for the current milestone have `"status": "passed"`.
2. If any tasks are still pending or failed, warn the user and list them.
3. If all complete:
   a. Create `.ds/archive/milestone-[N]-[date]/` directory.
   b. Copy the current `tasks.json` and `progress.txt` into the archive.
   c. Reset `tasks.json` to an empty array for the next milestone.
   d. Append a completion summary to `progress.txt`.
4. Update `.ds/ROADMAP.md` to mark the milestone as ✅ complete.
5. Notify the user to run `/ds-new-milestone` or `/ds-plan` for the next phase.
</process>
