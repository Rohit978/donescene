---
name: ds-execute
description: Execute ONE pending task from `.ds/tasks.json` using the DoneScene Protocol.
---

<objective>
Execute EXACTLY ONE pending task from `.ds/tasks.json`, verify it, update decentralized memory, commit to git, and stop.
</objective>

<process>
## Step 1: Read Protocol
Read `ds-protocol.md` in the project root. Follow its constraints.

## Step 2: Read Task Queue
Read `.ds/tasks.json`. Sort by `priority` (lowest number first). Pick the first task where `"status": "pending"`.
- If NO tasks are pending, notify the user that all tasks are complete and stop.

## Step 3: Load Decentralized Memory
Before writing any code:
1. Read `.ds/AGENTS.md` for global project rules.
2. Check if directories in `files_to_edit` contain local `AGENTS.md` files. If so, read them.
3. Read `.ds/progress.txt` to understand what previous agents have done.

## Step 4: Execute the ONE Task
Write the code to complete the selected task. Do NOT work on any other task.

## Step 5: Verify (Self-Healing Loop)
Run the task's `verification_command` in the terminal.

**If it PASSES:** Proceed to Step 6.

**If it FAILS:**
1. Read the error output carefully.
2. Fix the code based on the error.
3. Run the verification command again.
4. Repeat up to **3 times maximum**.
5. If it still fails after 3 attempts:
   - Run `git checkout -- .` to revert ALL changes.
   - Append to `.ds/progress.txt`: `FAILED: [Task ID] - [Error summary]. Reverted.`
   - Update `tasks.json` status to `"failed"`.
   - Stop and notify the user.

## Step 6: Git Commit
```
git add .
git commit -m "ds: [Task ID] - [Task description]"
```

## Step 7: Write Memory
1. **Local `AGENTS.md`:** Append discoveries to the modified folder's `AGENTS.md`.
2. **Global `AGENTS.md`:** If the learning is project-wide, append to `.ds/AGENTS.md`.
3. **Progress Log:** Append to `.ds/progress.txt`:
```
## [Timestamp] - [Task ID]
- Completed: [what was done]
- Files changed: [list]
- Learnings: [key discoveries]
---
```

## Step 8: Update Queue
Change the task's status from `"pending"` to `"passed"` in `.ds/tasks.json`.

## Step 9: Stop
Output: `<promise>COMPLETE</promise>`
Tell the user how many tasks remain and to run `/ds-execute` again.

**CRITICAL: Do NOT continue to the next task. STOP HERE.**
</process>
