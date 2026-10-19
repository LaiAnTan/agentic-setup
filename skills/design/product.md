# Stage: Product

Goal: agree on *what* we're building and *why* before anyone thinks about *how*.

Draft, in plain language:
- **Problem**: what's wrong or missing today, and for whom. 2–3 sentences.
- **Users and main flows**: who uses it and the 2–5 things they do, step by step.
- **Behaviour**: what should happen, including edge cases and failure cases
  (empty, slow, invalid input, offline, no permission).
- **Success**: how we'll know it works. Prefer something measurable
  (a metric, a target number, a scenario that must pass).
- **Out of scope**: what we're deliberately not doing now.
- **Mockups**: for anything with UI, a rough sketch, wireframe or screenshot of a prototype.

Show a user-flow diagram (Mermaid flowchart) when there's more than one path.

Avoid: technology choices, file names, code. Those come later.

Stop and ask the user to approve or correct before moving to architecture.
