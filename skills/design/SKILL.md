---
name: design
description: Design before building. Use for anything significant - a big feature, a refactor, a new project, multi-repo work, or changes to core logic, state, data, money, security or public APIs. Walks through product, architecture, program design and vertical slices, stopping for the user's approval at each stage, and records the design in docs/designs/.
---

# Design before building

Agents are fast at implementing and bad at noticing that a design is decaying. The fix is to
agree on decisions *before* code exists, so each PR is quick to review because it matches what
was already approved. You draft each stage; the user reviews and approves it.

## 1. Size the work and pick stages

| Work | Stages |
|---|---|
| Medium feature, contained refactor | program design → slices |
| Big feature, cross-cutting refactor | architecture → program design → slices |
| New project, multi-repo, or unclear problem | product → architecture → program design → slices |

Say which size you chose and why in one line. The user can add or skip stages.

## 2. Gather context first
Before drafting anything: read `docs/README.md` and the living docs it points to, any open
designs in `docs/designs/`, the relevant code and git history for the area. For choices
between tools or approaches, research (docs, benchmarks, known issues) and give concrete
options with sources. Don't design from assumptions.

## 3. Run each stage
Create the design file `docs/designs/YYYY-MM-DD-<slug>.md` from `template.md` (set up the
`docs/` layout from the global rules first if the repo doesn't have it). When you create
`docs/designs/`, also add a `design-preview` entry to the project's `.claude/launch.json` (create
the file if needed, keep any existing entries) so the built pages open in the preview pane:

```json
{ "name": "design-preview", "runtimeExecutable": "python3",
  "runtimeArgs": ["<this skill's folder>/scripts/preview.py", "docs/designs"], "port": 4319 }
```

The design markdown is the only source. For a long design, start each stage in a fresh session
that reads the design file first, rather than carrying one long chat. For each stage, read its
stage file below (in this skill's folder):

- `product.md`: problem, users, behaviour, out of scope
- `architecture.md`: components, contracts, data, jobs, invariants, failures
- `program-design.md`: types, signatures, file layout, call flow
- `slices.md`: build order, repos, PRs, and the check for each slice

Then:

**a. Clarify first.** If a brainstorm brief (`docs/designs/*-brief.md`) exists for this work,
start from it and don't re-ask what it settled. If there's none and the problem itself is still
fuzzy, suggest running the `brainstorm` skill first. Before drafting, tell the user in a few
lines what you understand this stage has to decide, list your assumptions, and ask whether
anything needs clarifying (use AskUserQuestion, if your agent has it, for concrete choices).
Wait for their answer before drafting.

**b. Draft in the markdown only.** Write that stage's section of the design file, with Mermaid
fences for diagrams. Keep sentences short; one idea per diagram. End the section with its
decisions and open questions, numbered, each with your recommended answer.

**c. Review before asking for approval.** Check the draft against these and fix what you find:
- Is any rule decided in two places?
- Can two workers (processes, jobs, users, requests) grab the same thing at once?
- Which numbers are guesses, and how will each be measured?
- What is the smallest first release?
- What depends on someone else (another team, service, approval or account)?

**d. Build and publish.** Rebuild the page from the markdown and republish it:

    python3 <this skill's folder>/scripts/build_artifact.py docs/designs/<file>.md

This writes `<file>.html` next to the markdown. Publish it with the Artifact tool, using the
same file path each time so the link stays the same. Never edit the HTML or the artifact by
hand; change the markdown and rebuild. Agents without an artifact tool start the
`design-preview` server and open the page there instead.

**When stopping**, link the artifact and the markdown, and repeat the numbered questions in chat
so the user can answer "2: yes". Do not start the next stage until the user approves this one.
If they change something, update the markdown and rebuild, not just the chat.

## 4. Build slice by slice
After the slice plan is approved:
- Build one slice at a time; each ends with its agreed check passing and the proof shown.
- One PR (or commit, if the user doesn't use PRs) per slice, described per the global rules.
- If implementing shows the design is wrong, stop and propose the change to the design
  instead of quietly drifting from it. Update the design file when a change is agreed.
- Tick off slices in the design file as they land, so a later session can pick up from it.

## 5. Finish
When the last slice lands, fold the outcome back so the living docs stay the source of truth:
- Update the repo's `docs/product.md`, `docs/architecture.md` and any topic docs (not this
  skill's stage files) to describe the system as it now is, following the global rules' docs writing rules.
- Add any new difficult or project-specific terms to `docs/glossary.md`.
- Turn each significant decision into a `docs/decisions/NNNN-<slug>.md` note.
- Mark the design file done and add it to `docs/README.md`. Don't rewrite it afterwards.
- Show the user what changed in the living docs.
