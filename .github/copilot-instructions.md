Repository Copilot Instructions

This repository includes developer guidance and agent-friendly conventions. When interacting with GitHub Copilot (Copilot Chat) in the context of this repository, follow these conventions so your suggestions and workflows match project expectations.

1. Project purpose
- This project is a modern Python cookiecutter template with strict type/check/lint/test requirements and agent-friendly docs in `.copilot/` and `/.github/copilot-instructions.md`.

2. Interaction rules (required)
- Do not end a session with a simple closing message. Always ask the user what to do next.
- Before finishing any task, ask a clear next-step question in Copilot Chat and present 3–5 actionable options (examples below).
- Provide options tailored to context, e.g. load a skill, explore the codebase, add a feature, write tests, create documentation, or create a PR.
- Repeat: after the user picks an option and the requested work is done, immediately ask what to do next again. Continue until the user explicitly says they are finished.

3. Example next-step options
- "Run the test suite and report failures"
- "Create a PR with these changes"
- "Add unit tests for X"
- "Refactor Y for readability/performance"
- "Explore code to find where Z is implemented"

4. Codebase exploration
- For repo searches or structural questions, prompt Copilot Chat with explicit queries (e.g., "Find files that define X, list file paths and key lines").
- If OpenCode subagents are available, prefer the `explore` subagent for broad searches and pattern discovery; otherwise instruct Copilot Chat with a clear search prompt.

5. Developer notes
- The repository also contains `.copilot/` and `.claude/` folders with more detailed rules, skills, and templates. Use those for deeper guidance.
- Any automated recommendations that change files should be followed by the "ask what to do next" step before committing or pushing.

Last updated: 2026-02-21
