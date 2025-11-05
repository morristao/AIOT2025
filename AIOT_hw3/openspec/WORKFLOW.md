# OpenSpec workflow — quick guide for this project

This short file explains the OpenSpec workflow (based on `openspec/AGENTS.md`) and how to work with the AI assistant for `aiot_hw3`.

1. Read project context
- Always start by reading `openspec/project.md` to understand purpose, tech stack, data sources, and developer links.

2. Create a change proposal
- Choose a verb-led `change-id`, e.g., `add-spam-classification` or `add-svm-variant`.
- Scaffold a change directory under `openspec/changes/<change-id>/` containing:
  - `proposal.md` (why, what, impact, links)
  - `tasks.md` (implementation checklist)
  - `specs/` with delta files (per capability)

3. Author spec deltas
- Use `## ADDED Requirements`, `## MODIFIED Requirements`, etc.
- Each Requirement must include at least one `#### Scenario:`.

4. Validate and request review
- Run (or ask the assistant to run) `openspec validate <change-id> --strict` (if you have the CLI) or perform a manual review.
- When ready, open a PR and request review; do not start implementation prior to approval unless explicitly agreed.

5. Implementation
- Follow `tasks.md` sequentially. Mark tasks as completed in the file.
- Keep changes small and testable. Add unit tests and a short smoke test.

6. Archiving
- After deployment, move the change to `openspec/changes/archive/YYYY-MM-DD-<change-id>/` and update `openspec/specs/` if the capability changed.

How to ask the AI assistant
- Use the Copilot prompts in `openspec/copilot_prompts.md`.
- Example requests:
  - "Create change proposal for adding a Streamlit demo page that uses the saved model"
  - "Scaffold tasks and minimal tests for `add-spam-classification`"
  - "Explain the OpenSpec validation errors for `add-spam-classification`"

Notes specific to this repo
- Project links and demo info are in `openspec/project.md`.
- The baseline dataset is the Packt dataset (Chapter 3). Cite it in proposals that rely on the data.

*** End of guide
