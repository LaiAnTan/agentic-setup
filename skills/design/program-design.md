# Stage: Program design

Goal: settle the shape of the code before writing it, so review later is "yes, that's what we
agreed" rather than redesigning in the PR.

Draft:
- **File layout**: new and changed files/modules, one line on each one's job.
- **Types**: the key types, interfaces and schemas, written out as real code in the project's
  language (signatures and fields only, no bodies).
- **Functions**: the important public functions/methods with signatures and a one-line
  description of what each does and what it returns or throws.
- **Call flow**: for the main flows, the call stack from entry point down to storage/IO.
  Use a Mermaid sequence diagram.
- **Errors**: where errors are caught, what the user sees, what gets logged.
- **Config**: tunable numbers and settings, and where they live.
- **What gets deleted**: code this replaces. Prefer subtracting to adding.

Keep it to what a reviewer needs to recognise the code later. Don't write implementations.

Open the section with two pictures before any signatures: "reused / new / deleted" and "what
happens step by step" for the main flow, then errors in plain words. Signatures come after, for
the reviewer who needs them.

For refactors: show before and after for the layout and call flow, and state what behaviour
must stay exactly the same and how that will be checked.

Stop and ask the user to approve or correct before planning slices.
