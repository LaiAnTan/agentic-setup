# Template for docs/designs/YYYY-MM-DD-<slug>.md

One file per piece of work. Fill in only the stages being run; delete the rest.
Keep each section short; diagrams over paragraphs. This file is a working record: code
pointers are fine here, but the living docs it folds into follow the CLAUDE.md writing rules.

```markdown
# <Feature or project name>: design

Status: product ⏳ · architecture ⏳ · program design ⏳ · slices ⏳ · done ⏳
Started: <date> · Last updated: <date>

## Product
**Problem:**
**Users and flows:**
**Behaviour and edge cases:**
**Success looks like:**
**Out of scope:**

## Architecture
<component diagram>

| Component | Owns | Talks to |
|---|---|---|

**Contracts:**
**Data model:**
**Constraints:**
**Decisions:** (each: choice, options considered, why, source links; significant ones
become `docs/decisions/` notes when the design is done)

## Program design
**File layout:**
**Types:** (code block)
**Key functions:** (code block, signatures only)
**Call flow:** <sequence diagram>
**Errors and config:**
**Deleted:**

## Slices
- [ ] 1. <name>: delivers … · repo … · check: …
- [ ] 2. <name>: delivers … · repo … · depends on 1 · check: …

## Change log
- <date>: <what changed in the design and why>
```

Update the status line and change log whenever a stage is approved or the design changes.
