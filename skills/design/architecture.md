# Stage: Architecture

Goal: agree on the big pieces and how they talk, so later code can't drift into a tangle.

This is real system design, not a summary. Keep the project's own names for things (services,
tables, queues, modules) and explain each in a **Terms** list at the top of the section.

Draft:
- **Terms**: each project-specific name used below, with a few plain words on what it is.
- **Components**: the main parts (services, modules, repos, external systems) and what each
  one owns. One line each. Every piece of state has exactly one owner.
- **Contracts**: how components talk: APIs, events, function boundaries, file formats.
  Include the shape of the data that crosses each boundary.
- **Data**: entities, key fields, relationships and where they're stored.
- **Jobs**: background, scheduled or queued work: what triggers it, what it reads and writes,
  how often, and what happens if it runs twice or overlaps.
- **Invariants**: the rules that must always hold, and which component enforces each one.
- **Failures**: what happens when each dependency is slow, down or returns bad data, and how
  the system recovers.
- **Constraints**: performance targets, cost or quota limits, security and privacy,
  hosting, compatibility, deadlines.
- **Tech choices**: only where a new choice is needed. Give concrete options with research
  and sources, then a recommendation (per the global rules).
- **Risks**: what's most likely to go wrong or be hard to change later.

Diagrams: a component diagram (who calls whom) and, if there's real data, an ER diagram.

For changes to an existing codebase: show the current architecture first, then what changes.
Follow existing patterns unless there's a stated reason not to.

Stop and ask the user to approve or correct before moving to program design.
