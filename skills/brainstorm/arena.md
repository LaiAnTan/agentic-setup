# Going wide: the arena

Several agents each develop a different approach as strongly as they can, without seeing each
other's work, so they don't all anchor on the same first idea. A separate judge then compares
them against the user's criteria.

## Set up
Pick three directions (tell the user which before starting):
- if the user is torn between options, one agent per option;
- otherwise three angles: **simplest** (least to build and run), **most robust** (fewest ways to
  fail), **most ambitious** (best result if it works).

## Contenders
Start one subagent per direction, in parallel if your agent can start subagents; otherwise
work through them one after another, starting each from the brief below and not from the
others' results. Give each the same brief:
- the frame (problem, criteria, constraints) and the relevant part of the log, including what
  was already rejected and why;
- its direction, and the instruction to make the strongest honest case for it;
- research before proposing, with sources;
- return: the approach in a few lines, how it meets each criterion, the biggest risk and how
  to reduce it, rough effort, and what it would take to test it cheaply.

## Judge
Start a separate subagent (or do it yourself, fresh, if you can't) as the judge. It gets the
frame and the three results, not the chat history. It:
- scores each against each criterion, with one line of reasoning per score;
- points out claims that look unsupported;
- proposes one or two merged options that take the best parts.

## Report
Update the brainstorm artifact with the contenders side by side and the judge's merged
options, add the results to the log, then go back to "React and push back" with the user.
