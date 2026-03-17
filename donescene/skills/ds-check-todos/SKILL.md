---
name: ds-check-todos
description: List pending todos and select one to work on.
---

<objective>
Display all pending todos from `.ds/todos.md` and optionally promote one to a task in `tasks.json`.
</objective>

<process>
1. Read `.ds/todos.md`. If it doesn't exist, tell the user they have no todos.
2. Display all unchecked `- [ ]` items as a numbered list.
3. Ask the user if they want to:
   a. **Promote** a todo to a real task → Add it to `.ds/tasks.json` with a priority and mark the todo as `[x]`.
   b. **Delete** a todo → Mark it as `[x]` with note "removed".
   c. **Keep browsing** → Do nothing.
</process>
