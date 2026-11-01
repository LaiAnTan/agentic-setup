# Stage: Vertical slices

Goal: an order of work where every step is small, works end to end, and is checked before the
next one starts.

A vertical slice is a thin piece that cuts through every layer it needs (UI, API, logic,
storage) and does something real. Not horizontal ("all the types", then "all the API",
then "all the UI"): models tend to plan horizontally, so check for it and rewrite it.

Slice 1 is usually a walking skeleton: the thinnest path from input to output, wired up for
real, with everything else stubbed.

For each slice, write:
- **Delivers**: what works after this slice that didn't before, in user terms.
- **Repos and files**: where the change lands.
- **Depends on**: earlier slices, or other repos that must land first.
- **PR**: one PR per slice, small enough to review in one sitting.
- **Check**: the agreed proof that it works: tests to add or pass, a command and its expected
  output, a metric and its target, or a screenshot of a specific state. Agree on this now,
  not after the code exists.

Also cover:
- **Order**: a numbered list or a dependency diagram. Riskiest or most uncertain slice as
  early as possible.
- **Multi-repo coordination**: which repo's change lands first, how contracts stay
  compatible in between (versioning, feature flags, backwards-compatible fields),
  and how to roll back.
- **Done**: what's true when all slices have landed.

Write the slices into the design file as a checklist so progress is tracked there.

Stop and ask the user to approve the plan before building slice 1.
