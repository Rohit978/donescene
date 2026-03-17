---
name: ds-map
description: Analyze codebase and generate ARCHITECTURE.md
---

<objective>
Scan the current project's file structure, key modules, and dependencies to produce a comprehensive `.ds/ARCHITECTURE.md` document that future agents can reference for context.
</objective>

<process>
1. List the project root directory recursively (max depth 3).
2. Identify the tech stack from `package.json`, `requirements.txt`, `Cargo.toml`, or similar.
3. Read the top-level entry files (e.g., `main.py`, `index.ts`, `app.js`) to understand the app structure.
4. Read any existing README or docs.
5. Generate `.ds/ARCHITECTURE.md` with these sections:
   - **Overview:** What the project does (1-2 sentences).
   - **Tech Stack:** Languages, frameworks, databases.
   - **Directory Structure:** Annotated tree of key folders.
   - **Key Modules:** Brief description of each major module/package.
   - **Data Flow:** How data moves through the system.
   - **Entry Points:** Where execution starts.
   - **Dependencies:** Key external libraries and their purpose.
6. Update `.ds/AGENTS.md` with any structural patterns discovered.
7. Notify the user the map is complete.
</process>
