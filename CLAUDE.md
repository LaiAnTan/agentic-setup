# How I work

I work across a lot of things: web apps, backends, simulations, data/ML, systems code, infra.
I iterate fast with short messages. Keep up with that pace, but don't let speed hide bugs or
leave code I can't follow.

## Sizing the work
- **Small change** (a fix, a tweak, one function or component): just do it, then report.
- **Feature**: say in 2–4 lines what you'll change and which files, then do it.
- **Anything significant** (a big feature, a refactor, a new project, multi-repo work, or changes
  to core logic, state, data, money, security or public APIs): use the `/design` skill. Don't
  write implementation code until I've approved the design it produces.
- If I give you several things at once, do them as separate slices, not one big change.

## When I'm vague
- My wording is loose. If two readings would give noticeably different results, pick the likelier
  one, say which in one line, and move on. Ask only if a wrong guess would cost real work.
- When I ask for ideas, opinions or a choice (tech stack, library, approach, design), research
  first: current docs, real benchmarks, known issues, how others solved it. Then give numbered,
  concrete options (named tools/versions or specific designs), each with its trade-offs, what
  it would mean in my project, and links to the sources. Say which one you'd pick and why.
  Don't pad the list with options you wouldn't seriously consider.
- For big or uncertain changes, prototype first and keep it easy to revert.

## Taste
- Simple and minimal by default. Cutting is usually the right answer, in code, UI and writing.
- Nothing should read as AI-generated: no generic template UI, filler copy, or boilerplate
  comments and docs that restate the code.
- Keep what I last approved unless I ask; don't redesign around a small request.

## Code
- Subtract before you add. Prefer the smallest change that does it; delete dead code, unused
  dependencies and anything you replaced.
- Fix root causes. No swallowed errors, no casts or `any` to silence the type checker, no
  weakening or editing tests/checks to make them pass.
- Follow the conventions already in the repo before introducing new patterns or libraries.
- Tunable numbers (thresholds, timings, odds, sizes) live in one named config, not scattered.

## Proving it works
- Run the project's typecheck/lint/tests/build before saying you're done.
- Check the change the way it is actually used: run the function, hit the endpoint, run the
  script on real input, open the UI (desktop and mobile width if it's a web page).
- If there's a numeric target (accuracy, latency, a game's odds), measure it and report the
  number; don't eyeball it.
- Never report done on something you haven't actually run or seen.
- Show me the proof, don't just claim it: screenshots for UI, before/after metrics or command
  output for logic and performance, the actual request/response for APIs.

## Explaining
- Prefer a diagram over a wall of text: flows, architecture, data models, state machines,
  before/after. Use Mermaid or an image, plus a few lines of text for what the diagram can't say.
- Lead with the answer; keep prose short and skimmable.

## Reporting back
- End with a short list: what changed, which files, anything you guessed or didn't verify.

## Docs
Layout, in every project:
- `docs/README.md`: index, one line per doc.
- **Living** (always match the code; update them in the same change as the code):
  `product.md`, `architecture.md`, `glossary.md`, `<topic>.md` deep dives, `guides/` how-tos.
- **Records** (dated, never rewritten): `designs/YYYY-MM-DD-<slug>.md` from `/design`,
  `decisions/NNNN-<slug>.md` for "chose X over Y because…".
- `public/`: only docs meant for end users.

Writing:
- Write for a person reading top to bottom: explain concepts, behaviour and reasons in prose
  and diagrams. Don't scatter file paths, line numbers or function names through the text.
- Use simple words and short sentences. Explain with plain terms and examples first; bring in a
  technical term only when it's needed, and say what it means the first time.
- Keep difficult or project-specific terms in `docs/glossary.md` (term, plain-language meaning,
  example), and link a term to its entry the first time a doc uses it. Add new terms as they appear.
- Put code pointers in one short **"Where in the code"** section at the end of each doc:
  concept → folder or module. No line numbers (they go stale). Agents can search from there.
- Inline code only for things a reader would actually type or look up: commands, config keys,
  public API names.

Serving: for projects with a web UI, render `docs/` at `/docs` in dev only, with Mermaid
diagrams, excluded from production builds. Serve `docs/public/` in production only if I ask.

## Git
- One commit per slice with a plain message. "push" means commit what's done and push to the
  current branch.
- Never make a repo public, delete branches, rewrite history or force-push without asking.

## Pull requests
Write the description for a reviewer who hasn't seen our chat. Plain language, short, skimmable:
- **Title**: what it does, in plain words (not the branch name).
- **Why**: the problem or goal, 1–3 sentences.
- **What changed**: a few bullets by behaviour, not a file-by-file list. Add a diagram if the
  flow or structure changed.
- **Proof**: the screenshots, metrics or command output that show it works.
- **Review guide**: where to start reading, the risky parts, any decisions or trade-offs made.
- **Not done / follow-ups**: anything left out or unverified.
Keep each PR to one slice; if the description needs to cover several unrelated things, split the PR.
