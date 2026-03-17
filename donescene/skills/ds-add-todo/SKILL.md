---
name: ds-add-todo
description: Capture an idea or task as a quick todo.
---

<objective>
Quickly add a note or task idea to `.ds/todos.md` without interrupting the current workflow.
</objective>

<process>
1. Take the user's input (the todo text).
2. Append to `.ds/todos.md` (create if it doesn't exist):
```
- [ ] [timestamp] — [user's todo text]
```
3. Confirm it was saved. Do NOT switch to planning or execution mode.
</process>
