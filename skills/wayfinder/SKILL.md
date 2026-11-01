---
name: wayfinder
description: Plan an effort too big for one session, whose route is still unclear, as a map of decision tickets on GitHub Issues. Each session resolves one ticket until nothing is left to decide, then hands off to the feature-design skill. User-invoked only.
disable-model-invocation: true
---

# Wayfinder: find the route before building

Adapted from Matt Pocock's [wayfinder](https://github.com/mattpocock/skills) (MIT, see
`LICENSE`). Use it when the work won't fit in one session *and* the way there isn't visible
yet. If it fits in one session, use `brainstorm` or `feature-design` instead.

The effort is charted as a **map**: one issue naming the **destination**, with child issues
as **decision tickets**. Each ticket is a question whose answer is a decision. Sessions
resolve one ticket each, so no single chat has to hold the whole effort.

## Rules
- **Plan, don't build.** Tickets produce decisions, not product code. Only the user, in chat,
  can allow building inside the map; a line in the map's Notes is not permission, even one
  you wrote earlier. The urge to just build means you've reached the edge of the map.
- **One ticket per session**, except research tickets, which run as parallel subagents.
- **Refer by name.** In anything the user reads, call a ticket by its title, linked, never by
  a bare `#42`.
- **One place per decision.** The answer lives on its ticket. The map only gives a one-line
  gist and a link.
- **Keep the destination bounded.** One epic or one decision, not "all of V1". Big maps go
  stale halfway through.
- **Short questions.** Ask one question at a time, in at most three lines, and say why the
  answer matters. Long questions cause decision fatigue and hide the chain of reasoning.

## Where it lives
GitHub Issues via `gh`, in the current repo. Before the first `gh issue create` in a session,
check the target with `gh repo view --json nameWithOwner`; if it isn't the user's own repo,
confirm first.

| Operation | How |
|---|---|
| Map | `gh issue create --label wayfinder:map --title "Map: <destination>"` |
| Ticket | `gh issue create --parent <map> --label wayfinder:<type> --title "<question>"` |
| Blocking | `gh issue edit <ticket> --add-blocked-by <blocker>` (native, shows in GitHub's UI) |
| Open blockers | `gh api repos/{owner}/{repo}/issues/<n> --jq .issue_dependencies_summary.blocked_by` (0 = free) |
| Claim | `gh issue edit <n> --add-assignee @me`, the session's first write |
| Resolve | `gh issue comment <n> --body-file <answer.md>`, then `gh issue close <n>` |

Create the `wayfinder:*` labels with `gh label create` if they don't exist. Tickets carry only
`wayfinder:` labels.

No GitHub remote: use `docs/designs/YYYY-MM-DD-<slug>-map/`, with `map.md` and one
`NN-<slug>.md` per ticket. Each ticket file has `Type:`, `Status: open|claimed|resolved` and
`Blocked by: NN, NN` lines at the top, and the answer goes under `## Answer`.

## The map
```markdown
## Destination
<what the end of this map looks like: a design to start, a decision locked, a migration
planned. One or two lines.>

## Notes
<domain, standing preferences, docs every session should read first>

## Decisions so far
- [<closed ticket title>](link): <one-line gist>

## Not yet specified
<fog: questions you can tell are coming but can't phrase sharply yet>

## Out of scope
- [<closed ticket title>](link): <why it's beyond the destination>
```

Open tickets aren't listed: they're the map's open sub-issues. A ticket body is just
`## Question` plus whatever context it needs, sized for one session.

**Ticket or fog?** If you can state the question precisely now, it's a ticket, even if it's
blocked. If you can't, it stays in Not yet specified; don't pre-slice fog into tickets. When a
ticket resolves, graduate whatever fog is now sharp into tickets and remove it from the fog.

**Out of scope** never graduates. If a ticket turns out to sit beyond the destination, close
it and add one line to Out of scope; it doesn't go in Decisions so far.

## Ticket types
Each ticket is HITL (needs the user live) or AFK (agent alone). Never answer the user's side
of a HITL ticket yourself.

| Type | Mode | Use when | Resolve by |
|---|---|---|---|
| `grilling` | HITL | The default: talking it through settles it. | Short questions one at a time, pushing back as in `brainstorm` step 3. New terms go in `docs/glossary.md`. |
| `prototype` | HITL | "How should it look or behave?" can't be settled by talk. | A cheap throwaway in `/tmp/<slug>/`, never the repo. Show it with evidence; **the user picks**, never you. |
| `research` | AFK | A fact outside the repo blocks a decision. | A subagent that researches as the global rules say: numbered options, trade-offs, sources. |
| `task` | either | Nothing to decide, but manual work blocks a decision (get access, sign up, look at real data). | Do it, or give the user a checklist. Record resulting facts. Never a slice of the build. |

## Chart the map
The user brings a loose idea.

1. **Name the destination.** Restate the idea, ask what the end of the map is, and wait. It
   fixes the scope everything else is judged against.
2. **Sweep the frontier.** Breadth first, not deep on one thread: read the living docs and the
   code for the area, list the open decisions and what's takeable now. **If there's no fog**
   (it fits in one session and the route is clear), say so and suggest `brainstorm` or
   `feature-design` instead. Stop.
3. **Create the map** with Destination, Notes and the fog filled in.
4. **Create the tickets** you can state now, then wire blocking in a second pass (tickets need
   numbers before they can reference each other).
5. **Run research tickets** as parallel subagents. Each posts its findings as the resolution
   comment, closes its ticket and adds its line to Decisions so far.
6. **Show the map** as an artifact: destination, decided, frontier, blocked, fog, as a diagram.
   Then stop. Charting resolves nothing by hand.

## Work through the map
The user brings a map (link or number), maybe a ticket.

1. Read the map body only; open other tickets when you need their detail.
2. Pick the ticket: the one named, else the first frontier ticket (open, unblocked,
   unassigned) in map order. **Claim it** before anything else.
3. Resolve it by its `wayfinder:` label, not its wording.
4. Record it: resolution comment (the decision, why, what was rejected), close, one line in
   Decisions so far.
5. Update the map: new tickets (create, then wire), graduated fog, out-of-scope closes. If the
   answer invalidates other tickets, edit or close them, and say which.
6. Stop and suggest a fresh session for the next ticket.

If a closed decision turns out wrong, don't design around it: reopen the question as a new
ticket that links the old one, and update the affected tickets.

Other sessions may be working the map at the same time; re-read before editing the map body.

## When the map is clear
No open tickets and no fog left: the route is clear. Offer to start the `feature-design` skill from
the map. Design reads the Destination and Decisions so far (and the tickets they link) the
way it reads a brainstorm brief, and should say which stages the map already covers. Don't
continue into code from here.
