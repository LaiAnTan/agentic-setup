---
name: ui-design
description: Design how something looks - a screen, page, dashboard, app UI, component, landing page, product mockup or feature illustration - or redesign one that looks generic or AI-made. Works on a Claude artifact design canvas, with directions side by side, then builds the approved design in code. Use when the user asks to design, redesign, restyle, polish, mock up or "unslop" a UI. For system or architecture design, use the `feature-design` skill instead.
---

# UI design

Built from ideas in [impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus,
[unslop](https://github.com/heydamir/unslop) by Damir Sokolovsky (@heydamir, CC BY 4.0), and
[Stageshow](https://github.com/benjitaylor/skills) by Benji Taylor.

Generated UI fails the same way every time: purple gradients, glows, emoji labels, uneven
spacing, and a layout any product could have. Cleaning that up isn't enough, because a clean
screen that could belong to anyone is just the next template. The goal is a screen only this
product could have: quiet everywhere, rich in one or two places that matter.

## The canvas
All design work happens on a **Claude artifact design canvas**, never as loose HTML files or
straight into the codebase.

- Start one with the Artifact tool: `action: "quickstart"`, `intent: "design"`, then create
  from the Design type it names and follow that type's instructions for files and format.
  One canvas per piece of work; revise it in place rather than starting new ones.
- Lay it out so it reads like a design review: a title note per row, options side by side,
  desktop and phone artboards next to each other, states (empty, loading, error) in a row
  below the main screen.
- The canvas's own instructions say not to check your work unless asked. **This skill asks:**
  after each build, open the canvas in the browser pane and look at every artboard once. Fix
  what that one look shows, then look again at most once more.
- Reasons and option notes go in your reply, never inside an artboard.
- Agents without an artifact tool: build the same artboards as one self-contained HTML page
  in the scratchpad and open it.

## 1. Pick the mode and size
**Mode** is what success looks like for the person using it:
- **Persuade**: they decide and act (landing, pricing, marketing). Bold, committed, one scene.
- **Operate**: they get a task done (app, dashboard, settings, admin). Precision and restraint;
  familiar patterns earn their place; the brand lives in details.
- **Read**: they understand something (docs, articles, changelogs). Structure first.
- **Show**: the work is the point (portfolio, gallery, product illustration). The artifact leads.

Pick it from the surface, not the company: a dev tool's landing page is Persuade.

**Size** decides how much you invent:
- **New surface or new look**: the full process below.
- **Redesign**: first audit it against `slop.md`, one line per sign with where it is. Heavy
  slop gets the full process. Light slop gets a polish: fix only what the audit found and keep
  the existing palette, type and layout. No slop: say so, suggest at most three refinements
  with exact values, and stop. Never change a good screen just to make it different.
- **Add to an existing screen**: keep its look; decide only content, hierarchy and states.

Say the mode and size in one line.

## 2. Brief
Read the product first: the docs, the existing UI, the code that renders it. Then ask two or
three questions that would change the result most, state your likely answer to each, and wait:
- who reaches this screen, in what situation, and what they must do or understand;
- what real content and data it carries, at its smallest and largest;
- what's uniquely true of this product that a competitor couldn't claim;
- what must not change.

Skip what's already obvious. Never ask for colors or "which style do you like".

## 3. Direction
Write five lines, derived from the product, never from trends:
- **Product**: what it does and for whom, in one plain sentence.
- **Character**: two or three concrete words, like `calm, exact, a little warm`. Not clean,
  modern, sleek, minimal or premium; those describe every template.
- **World**: the place or material the product belongs to. A notes app lives near paper and
  ink, a monitoring tool near instruments and night shifts. The world tints the neutrals,
  picks the accent and supplies the visual.
- **Moments**: one or two places that get rich color and craft, chosen from the content: the
  main chart, a rendered object, the product preview in a hero.
- **Signature**: one small detail only this product would have, used everywhere it fits.

Light or dark comes from one sentence about the scene: who uses it, where, under what light.

For a new look, put **three directions** on the canvas as hero artboards of equal size and
care, each a different world from the audience's life, plus one plain "category standard"
option for when the user wants the familiar. Avoid the looks generated UI always lands on
(cream ground with a serif and terracotta; near-black with one neon accent; editorial
hairlines with tracked mono labels; flat saturated ink with hard offset shadows) unless the
brief asks for one. If someone could guess your look from the product's category alone,
rework it.

**Stop and wait** for the user to pick or mix before building more. Changing direction later
means redoing everything.

## 4. Build on the canvas
Build the chosen direction at real sizes: pages at 1280–1440 wide plus a phone artboard at
390, each a redesign for its width, not a squeeze. Work in passes across the whole screen, in
this order, because each one changes how the next reads:

1. **Spacing**: everything on a 4px grid; same thing, same size; space inside a group smaller
   than between groups; one-off values replaced.
2. **Color**: one neutral ramp tinted toward the world; three text roles; one accent used
   rarely; rich color only inside the moments; borders as 6–10% hairlines; depth from surface
   steps, not glows.
3. **Icons**: one line set (the project's, else lucide), one size, one stroke, text colors.
   No emoji as icons.
4. **Copy**: cut taglines, helper text and secondary labels; if a screen needs them to make
   sense, fix the layout. Headlines say what it does for whom; no greetings, exclamation marks, hype words
   or unverifiable claims; changes say what they compare to; plausible data, never `123,456`.
5. **Type**: one family plus at most one partner; two weights; hierarchy from size and color;
   sentence case; tabular numbers in one format.
6. **Layout**: keep the content and its order; one primary and one secondary action; apps
   keep app proportions; a hero is a scene or an asymmetric split, not everything centered.
7. **Details**: nested radius (inner = outer − padding); one main chart, the rest smaller and
   different in kind; stat cards are numbers, not mini charts; every state designed.
8. **Visuals**: one strong visual where it helps, usually only the hero. A product preview in
   code beats a generic image. If you can't make the right image, leave a labelled slot.
9. **Motion**: only motion that explains something; one easing curve; one entrance at most;
   animate transform and opacity only. Note it on the canvas; build it in code.

`slop.md` has the full sign → fix list for checking the result.

### Product mockups and illustrations
When the artboard shows a product (a hero preview, feature card, bento tile, demo):
- It reads as a real product, simplified. Real words only on what the story is about, about
  three to seven strings; quiet placeholder bars for the rest.
- Frame with intent: the window or phone fills at least two thirds of the frame and runs off
  an edge. No window floating with even air on four sides, no plate behind it.
- One focal object; the eye knows where to land. At most one satellite (a smaller card or
  phone overlapping the edge).
- An animated demo tells one thing in three to five beats and a payoff, and every cursor move
  has a cause. Its first frame, the one most people see, tells the story on its own.
- Never invent another company's logo or copy its identity; borrow interactions only.

## 5. Check
Look at every artboard (see The canvas) and check:
- contrast: body text 4.5:1, large text 3:1, including small grey labels;
- every sign in `slop.md` is gone, and none of the template looks crept back in;
- states: hover, focus, disabled, loading, empty, error;
- the phone artboard has no overflow, cut text or text under 11px;
- real `<button>`, `<a>`, `<label>` even in a mockup; icon-only buttons have labels.

Then send the canvas link with a few lines: the direction, what changed per pass, anything
assumed or left as a placeholder, and any claims the user must confirm are real.

## 6. Build it in code
Only after the user approves the canvas. The canvas is the spec: build it in the project's
own stack and components, tokens in one place, then check the real UI at desktop and phone
width and show screenshots next to the canvas artboards. If the build has to differ from the
canvas, update the canvas or say why.

## Don't
- Don't rename the product or change what it does; keep a real logo. Redraw a slop logo flat.
- Don't swap one trend for another (glass, grain, neon, bento) when removing decoration.
- Don't invent features, data, testimonials or numbers. Use `[YOUR PRICE]`-style placeholders.
- Don't build in code before the canvas is approved, unless the user says to skip it.
