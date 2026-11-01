# Signs of slop

Each line is a sign and its fix. Use it to audit a redesign and to check your own result.
Adapted from unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0,
with additions from impeccable by Paul Bakaus.

A brief or a real brand can ask for any of these on purpose; then it isn't slop. The ones
marked **ban** are never earned back.

## Color and surfaces
- Hue-to-hue gradients (purple → blue, violet → pink) on backgrounds, cards, buttons → one neutral surface, accent only where it means something
- Gradient text → solid text; emphasis from size or weight
- Colored glows and zero-offset colored halos → remove; depth from surface steps and hairlines, shadows with an offset and soft blur
- Radial washes and blurred blobs behind content → remove
- Neon borders → hairline at 6–10% of the text color
- Five near-identical tints for text → three text roles from one ramp
- Everything highlighted → one accent, once or twice per screen
- Glass cards as decoration → plain raised surface with a hairline
- Colored `border-left` thicker than 1px on cards, callouts, list items → remove
- Hard offset shadows (`4px 4px 0`) in a world that isn't neobrutalist → soft neutral shadow or none
- Light or dark picked by category → picked from the scene it's used in

## Type
- Headings at 800–900 weight → 400–500, hierarchy from size
- `UPPERCASE TRACKED LABELS` → sentence case
- An eyebrow or kicker label above a heading → **ban**, delete it
- Many sizes and weights → a few sizes, two weights
- Mixed number formats (`$48,210` beside `$124,860.40`) → one format, tabular figures
- Negative tracking on small text → zero or slightly open
- Italic for emphasis → color or weight
- Mono as a costume for "technical" → mono only for code, data and measurements
- A default face nobody chose (Inter, DM Sans, Space Grotesk, Plus Jakarta…) where the brand is free → a face that fits the character
- Body lines wider than about 75 characters → 65–75ch

## Icons
- Emoji as icons, labels or status → one line icon set or nothing
- ✨ for anything AI → remove, or a plain icon where it explains something
- Icons in many sizes and colors → one size, one stroke, text color
- Unicode glyphs standing in for icons → real icons

## Spacing
- Arbitrary values (`mt-[13px]`) → steps on the 4px grid
- Rows in one list with different heights or gaps → one height, one gap
- Groups closer to their neighbours than to their own items → tighter inside, looser between
- Uneven padding in sibling cards → one padding
- More space below a heading than above it → more above

## Copy
- Greeting headlines (`Welcome back, Sam! 👋`) → the page or period as the title
- Exclamation marks → plain statements
- Changes without a reference (`+12%!!`) → `+12% vs last month`
- `Search anything...` → `Search`
- Supercharge, seamless, unlock, magic, revolutionize, AI-powered → what it actually does
- Periods on labels and buttons → none
- `$123,456`, `[X]`, lorem ipsum → plausible data or a labelled placeholder
- `Trusted by 10,000+ teams`, star rows with no source → ask if it's real; quiet and specific, or gone

## Components
- Glowing pills for counts, plans, shortcuts → quiet mono text or a keycap
- `PRO`, `New ✨`, `Beta 🚀` everywhere → remove, or one quiet text badge
- Everything a full pill → radius by size, nested radius math
- Rainbow or glowing chart bars, uppercase day labels → one or two series, muted grid, one highlight
- Sparklines and mini bars on every stat card → the number, its label, its change
- Equal cards side by side with the same layout → one main element, varied widths
- Same-size icon + heading + text cards as the page structure → fewer, more specific sections; never nested cards
- The hero-metric template (big number, small label, supporting stats) → show the thing itself
- Section numbers `01 / 02 / 03` that carry no meaning → remove
- A modal for a task that needs no interruption → inline
- Logo as a gradient tile, glossy orb or glowing dot → flat glyph in one color, or the wordmark alone
- Browser defaults left in (selection color, focus ring, scrollbars, caret) → themed from the palette

## Heroes and landing pages
- A pill badge above the headline (`✨ Introducing X 2.0`) → remove
- A headline that fits any product → what this product does, with its own nouns
- Everything stacked and centered → asymmetric split, or text over a large product view
- Three or more buttons, or avatars and chips under them → one primary, one secondary
- Floating blobs, grids, glowing lines behind the hero → plain ground or one real visual
- Feature cards with emoji, bold title and a vague line → fewer features, concrete copy

## Visuals
- Glossy 3D blobs, chrome shapes, nebulas → the product, or one concrete metaphor for it
- Robots, glowing brains, circuit lines for AI → show what the AI produces
- Text or fake buttons baked into an image → real text in the page
- An image with a hard edge and a different black → matched ground, soft mask
- A visual on every section → one, usually the hero
- A circle or polygon mask faking a subject's outline → a real cut-out, or no effect

## Motion
- `animate-pulse`, pings, breathing glows on things that aren't live → static
- `transition-all`, `hover:scale` on cards → color or surface step on hover, tiny scale on press
- Bouncy springs on simple UI → one ease-out curve
- Everything flying in on load → one short fade and rise, small stagger
- Parallax and floating loops → static
- Animating width, height, top, left → transform and opacity

## The template it falls back to
Not slop, but what a cleaned-up screen becomes when nobody decided anything:
- Pure grey page, Inter, white text, old brand color on one button → ramp tinted toward the world, accent from it
- A hero visual that's an empty box or stock picture → product preview in code, or an image from the world
- Every product getting the same layout, type and palette → let the direction choose
