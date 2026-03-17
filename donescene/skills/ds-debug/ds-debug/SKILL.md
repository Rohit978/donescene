---
name: ds-debug
description: Systematic debugging with 3-strike rule.
---

<objective>
Debug a reported issue using a structured, methodical approach. Apply the 3-strike rule: if 3 fix attempts fail, escalate to the user rather than spiraling.
</objective>

<process>
1. **Reproduce:** Ask the user to describe the bug or paste the error. Run the failing command to confirm.
2. **Diagnose:** Read relevant source files, stack traces, and `.ds/AGENTS.md` for known gotchas.
3. **Fix Attempt 1:**
   - Identify the root cause. Apply the minimal fix.
   - Run the verification command. If it passes → commit and log to `progress.txt`. Done.
4. **Fix Attempt 2 (if attempt 1 failed):**
   - Re-read the error. Try a different approach.
   - Run verification. If it passes → commit and log. Done.
5. **Fix Attempt 3 (if attempt 2 failed):**
   - Try a fundamentally different strategy.
   - Run verification. If it passes → commit and log. Done.
6. **Escalate (if all 3 failed):**
   - Revert ALL changes: `git checkout -- .`
   - Append detailed failure analysis to `.ds/progress.txt` including all 3 approaches tried.
   - Notify the user: "3-strike limit reached. Here is what I tried and why it failed. Manual intervention needed."
</process>
