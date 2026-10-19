# Stage: Architecture

Goal: agree on the big pieces and how they talk, so later code can't drift into a tangle.

Draft:
- **Components**: the main parts (services, modules, repos, external systems) and what each
  one owns. One line each. Every piece of state has exactly one owner.
- **Contracts**: how components talk: APIs, events, function boundaries, file formats.
  Include the shape of the data that crosses each boundary.
- **Data model**: entities, key fields, relationships, where they're stored, and the rules
  that must always hold (invariants).
- **Constraints**: performance targets, cost or quota limits, security and privacy,
  hosting, compatibility, deadlines.
- **Tech choices**: only where a new choice is needed. Give concrete options with research
  and sources, then a recommendation (per the global rules).
- **Risks**: what's most likely to go wrong or be hard to change later.

Diagrams: a component diagram (who calls whom) and, if there's real data, an ER diagram.

For changes to an existing codebase: show the current architecture first, then what changes.
Follow existing patterns unless there's a stated reason not to.

Stop and ask the user to approve or correct before moving to program design.
