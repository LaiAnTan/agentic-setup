---
name: brainstorm
description: Brainstorm hard until the idea is right. Use when the user wants to brainstorm, explore options, or is still unsure what to build or how. Loops through researched options, push-back and quick tests, keeps a running log, can "go wide" with several competing agents, and ends with a decision brief that the design skill starts from.
---

# Brainstorm until it's right

Design is a straight line; brainstorming is a loop. Spread out to many ideas, test them, throw
most away, and keep going until the user says it's right. Don't rush to converge, and don't
just agree: your job is to find the best answer, not to please.

## Files
Work in the repo's `docs/designs/` (or the current folder if there's no repo yet):
- `YYYY-MM-DD-<slug>-brainstorm.md`: the running log, from `log-template.md`.
- `YYYY-MM-DD-<slug>-brief.md`: the decision brief, from `brief-template.md`, written on "lock it".

Show everything visual in **one brainstorm artifact** (Claude's artifact tool): the options as
cards with a small diagram each, then the current leaning. Update it only when the user asks to
see it or on "lock it"; each round, update the log alone. Never keep the same content in more
than one doc. Agents without an artifact tool write a self-contained HTML page next to the log
and open it.
No Mermaid code blocks in chat.

## 1. Frame
Before any ideas, restate in a few lines:
- the problem, and who has it;
- what "right" looks like: the criteria a good answer must meet, in order of importance;
- hard constraints (time, money, stack, skills, hosting);
- what's already decided, and what's open.

Ask the user to correct it, and wait. The criteria are what every option is judged against later.

## 2. Spread out
Research first (current docs, real benchmarks, known issues, how others solved it), then give
3–5 options that are **genuinely different**, not variations of one idea. At least one should
be unusual: a different framing of the problem, or "don't build it, do X instead".

For each option: what it is in one line, how it scores on the criteria, the biggest risk,
roughly how much work, and source links. Say which one you'd pick and why. Number them so the
user can answer "mix 1 and 3".

## 3. React and push back
The user picks, mixes or rejects. Then, on whatever they're leaning towards:
- name its weakest assumption and how it would fail;
- give the strongest case for the best option they're *not* choosing;
- ask the one question whose answer would change the decision most.

If they're still unsure between options, go to step 4 rather than debating.

## 4. Test cheaply
When a question can be answered by trying, try instead of arguing: a throwaway prototype, a
quick calculation, a small benchmark, or reading how a real project did it. Tests live in
`/tmp/<slug>/`, never inside the repo, and are deleted afterwards with only the result logged.
A test likely to run longer than about 10 minutes goes in its own session, not a background
subagent (subagents die with the session). Show the evidence (screenshot, numbers, output).

## 5. Log every round
Update the log after every round: options considered, what was rejected and **why**, test
results, current leaning, open questions. Never bring back a rejected idea without saying
what has changed. If the chat gets long or a new session starts, re-read the log first.

Then loop back to step 2 or 3, whichever fits.

## Going wide
When the user says "go wide", read `arena.md` and run it. Also suggest it (and run it only on
a yes) when about three rounds have passed without the options narrowing.

## Lock it
Only when the user says "lock it" (or clearly approves a final direction):
- write the decision brief from `brief-template.md`;
- update the artifact to show the final direction;
- offer to start the `design` skill from the brief, telling the user which design stages the
  brief already covers.
