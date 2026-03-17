---
name: ds-pause
description: Save state for session handoff.
---

<objective>
Create a context handoff document so a future agent session (or a different human) can instantly understand the project state and resume work.
</objective>

<process>
1. Read `.ds/tasks.json`, `.ds/progress.txt`, and `.ds/ROADMAP.md`.
2. Generate `.ds/HANDOFF.md` with:
   - **Current State:** What milestone/phase we're on, what percentage is complete.
   - **Last Completed Task:** What was just finished.
   - **Next Task:** What should be done next.
   - **Known Issues:** Any failed tasks or unresolved bugs.
   - **Important Context:** Key gotchas or decisions from `AGENTS.md` and `progress.txt`.
3. Notify the user that the handoff is saved. They can close the session safely.
4. Tell them to run `/ds-resume` when they come back.
</process>
