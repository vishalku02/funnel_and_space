# Update log — guidance redesign

Living doc for the changes we want to make to the explorable. We started this
after feedback that the piece (1) opens too broad, (2) doesn't convey the
fish-eye idea as clearly as Wattenberger's original, and (3) has interactivity
(the checkboxes) that doesn't do anything.

The through-line of the redesign: **the four camps are one zoom axis.** In the
narrowest frame learning looks individual; as you pull back it becomes social,
then cultural. That is exactly Wattenberger's "same thing at different levels of
abstraction," applied to learning. We teach the zoom *gesture* the way she does
(simple example first, then hold it all at once) — but on our own character, not
a borrowed warm-up.

---

## Status — shipped (2026-06-11)

The redesign is **built and live in `index.html`** (committed + pushed to
`origin/main`; hosting via GitHub Pages at
`https://vishalku02.github.io/funnel_and_space/` once the repo is public).

**The arc, end to end:**

1. **Cold open** — "Everyone has their own view of education" + first capture
   (what comes to mind when you think about the word "education"?).
2. **Meet Irfan** (he/him) — likes being outside, looking after things; plants the
   seed (of curiosity). *(positionality/Biesta beat commented out — too abstract up
   front.)*
3. **The stuck moment** — working through fractions, gets stuck; the wide
   establishing shot (`new_imgs/scene-master.png`).
4. **Cascade** — "There are at least four ways to look at this one moment": a scrub
   slider panning through four nested crops (`scene-act/face/table/world`), four
   bubbles as quiet indicators. Each beat = camp + question + one-line creed.
5. **Instinctive pick** — "In this moment, how would you help?": 8 unlabeled helps
   (prototype set, verbatim), pick one → reveals your default lens; the other
   camps fill in as tap-to-open cards. Static affirm line: "None of the four is
   wrong, they just attend to different questions in the same moment."
6. **Lens turn** (re-level + Wattenberger) — "Each of these perspectives is
   true… a perspective held alone becomes a crop of education." Quote, our take,
   citation, then the bridge line.
7. **Fish-eye** — "Try the fish-eye lens yourself": Irfan-at-the-peephole image,
   then Mode 5 — drag the lens over `images/camp-situated.jpg`, normal (tunnel) vs
   fish-eye (focus + the other three curving in at the rim).
8. **Quadrant** — "Where is the field spending its attention?": drag products onto
   a 2D map, centre-of-gravity dot reveals the tilt (the robust single-board
   build).
9. **Final capture** — "what comes to mind now…" (the first→final drift).
10. **Close** — the tree, the closing line, our quote ("The focus was never what
    troubled us. It was a focus that mistook itself for a whole that was shared."
    — Vishal & Yoyo), then thanks to Amelia Wattenberger.

**Voice / copy conventions now in force:**

- Learner is **Irfan** (he/him). Education = the broad word, at the bookends;
  learning = the four theories, in the body.
- **No em-dashes** in rendered copy (commas/colons instead). Softer, flowing
  sentences; declarative titles carry no trailing period.

**Tracking: removed.** The clickstream plumbing (`/log`, `/snapshot`, session +
snapshot bookkeeping, per-event `track()` calls) was stripped for static hosting —
no failed requests. Save buttons still give "saved" feedback but transmit nothing.
**Re-addable later** behind a backend endpoint (serverless function / Apps Script)
without changing the interactions.

**Standalone prototypes retired** (`camp-interactions`, `presentation-modes`,
`quadrant-sort`, `fisheye-prototypes`). `quadrant-v2.html` kept locally as an
untracked sandbox (not committed, not hosted).

**Pending:** none blocking. Optional later: re-add data collection; revisit the
title ("…for Learning" vs "…for Education"); the cognitive cascade beat leans
hardest on its label if it ever reads flat.

---

## Decided changes

### 1. The camera-move cascade (replaces the four-camp checklists)

The lens section becomes **one camera pulling back from a single frozen moment**:
Maruko stuck on the last step of a fraction problem. Each beat widens the frame;
more enters the picture. The load-bearing mechanic:

> **Each zoom demotes the previous frame from "the whole picture" to "a detail."**

That demotion is the felt argument — what one camp calls the whole story, the
next reveals as a single detail inside a larger one.

The pull-back, level by level:

1. **Tightest crop — the act.** Her finger on the stylus, the wrong step, the red
   mark. This *is* the problem. → *what can she do?* (**behaviorist**)
2. **Pull back to her face.** The wrong mark is now just a symptom; there's a mind
   behind it with a misconception. The "problem" became a clue. →
   *what does she understand?* (**cognitive**)
3. **Pull back to the table.** An empty chair beside her, fraction tiles she isn't
   using, a partner she could be arguing with. Her stuckness is partly "she's
   doing this alone." → *how does she participate?* (**situated**)
4. **Pull all the way out.** The table sits in a classroom, a home, a community —
   and which math counts as real math, whose questions get asked, is set out here.
   Working alone was never just her choice. → *whose knowledge counts?*
   (**sociocultural**)

**Why this solves the honesty problem:** behaviorist→cognitive isn't a *social*
step (both are the individual), but framed as a *camera move* it still reads as
one continuous pull-back — act → person → room → world. The camera zooms, not the
social scale, so the sequence stays monotonic.

**The cold of absence (visual direction).** Pulling back should reveal what's
*missing* before it reveals warmth: the empty chair, no one at the tiles, the
empty classroom. The zoom-out aches because each wider frame shows another thing
that should be there and isn't.

**Image first, then the informative label.** Each beat lands as image first — a
beat to feel the empty desk — then the *teaching* label arrives: camp name +
question + one clear sentence (see the label section below). The image is not a
substitute for the teaching; it carries it.

**The kicker** is now the *closer* (after the sort — see Arc below). The cascade
teaches the levels *sequentially*; the kicker holds them *all at once*. It is the
idea we leave the learner with: the field holds a single lens, but *you* can hold
all four. See "Kicker: how to hold all four at once" for the form options.

**What this replaces:** the four `.checklist` blocks (behaviorist / cognitive /
situated / sociocultural) whose only feedback was "we feel the same way." The
scroll/zoom *is* the interaction now; no checkbox needed.

### Copy decisions (cascade)

- **The pivot line** from hook into the cascade: **"There are at least four ways to
  look at this one moment."** Keep exactly this. *Drop* the follow-up "Watch what
  changes as we pull the camera back" — it's stage-direction, tells the reader the
  mechanic, and breaks the spell. The frame should state, not instruct.

### 2. Rename Maya → Maruko

Done in `index.html` visible copy. Left as-is (internal ids, not user-facing):
`data-scene="meet-maya"` and the image filename `images/meet-maya.jpg`. Rename
those too if/when we touch the art pipeline.

---

## On the label question (REVISED — labels should teach)

Reversed an earlier call. The piece's actual failure is **too little guidance**,
not too much — it is nearly all narrative and never clearly informs the reader
what the four camps are. Wattenberger is the model: she is *expository but warm*.
The fish is friendly and concrete, but it serves a plainly-stated idea ("we think
about the same information at different levels of abstraction"). She is relentlessly
clear; clarity is the whole game, and the fish just lowers the barrier to it.

So **Maruko is our fish** — a friendly, concrete entry point *in service of clear
information*, not a substitute for it. Our mistake was letting the narrative
*replace* the teaching instead of *carrying* it.

Each cascade beat becomes a small **information card** that genuinely teaches the
camp:

- the **image** — the nested crop (the ache: empty chair, untouched tiles), now
  *annotated* to show what this lens foregrounds
- the **camp name** (behaviorist) — a real label now, not a hidden tag
- the **question** (what can she do?)
- **one clear, friendly sentence** of what this lens believes learning *is*

The discipline — the Wattenberger middle — is **maximally clear, minimally wordy**.
One concrete sentence per camp, warm, never a textbook paragraph. Draft creeds:

- **Behaviorist** — watches what she *does*. Learning is the behavior you can see,
  drilled until it holds.
- **Cognitive** — looks for the idea *underneath*. Learning is the model forming in
  her head.
- **Situated** — looks at the *table*. Learning is something you do with people and
  tools, not alone in your head.
- **Sociocultural** — looks at the *whole world* around her. Learning is cultural,
  and which knowledge counts is never neutral.

Two layers of information run at once: **per-beat** (what THIS lens sees) and
**across-beats** (how each lens demotes the last — the relationship is itself the
payload: no single lens is complete). Both should be explicit and guided now, not
left to inference.

**Consciously revising the old "no upfront definitions" guardrail.** That instinct
was right to fear dry textbook prose, but it overcorrected into withholding —
which is the no-guidance problem. The fix is Wattenberger's middle path: clear
plain sentences fixed to concrete, friendly visuals.

---

## Open questions / still to think about

- **Opening:** how exactly to start (wordless zoom hook?) and where the broad
  "what is education" capture lives now — leaning: move it to the end so it
  doesn't lead, keeping the first-vs-final drift for the Stat 292 study.
- ~~**Kicker form:** concentric fish-eye warp vs. side-by-side panels vs.
  continuous scroll-driven zoom.~~ RESOLVED → scene-based fish-eye (Mode 5). See
  Session synthesis.
- **Cascade drive:** scroll-driven (each scroll beat widens) vs. button/click —
  leaning slider/scrub (Option 3's mechanic). See Session synthesis.
- ~~**Art (now informative):** the cascade needs four nested crops of the *same*
  moment (act → person → table → world), each *annotated* to show what that lens
  foregrounds (label the empty chair, the untouched tiles). Current `camp-*.jpg`
  images are separate scenes, not nested annotated crops — need new art.~~ DONE →
  delivered in `new_imgs/` as true nested crops. Annotations DROPPED for
  simplicity — see "Art delivered" in Session synthesis.
- **How hard to pivot from hook to exposition:** how fast we leave the narrative
  open and name "four ways to look at this one moment" (the jump-to-maps move).
- ~~**Product sort:** give it a payoff (reveal the field clusters at the zoomed-in
  rings) or cut it.~~ RESOLVED → replaced by the quadrant (the payoff *is* the
  center-of-gravity tilt). See Session synthesis.
- **First-person turn** ("my learning at different levels") — save for the end as
  the reader applies the zoom to their own world?

---

## Session synthesis (2026-06-11) — locking the arc + the lens finale

Two parallel inputs converged here: a generative meeting with **Carol** and a
prior co-piloting session (the update log above). They agree on the spine and
disagree productively on one thing. This section records what we locked.

### What Carol pushed on

- **The relational layout was never visualized.** Her core critique: the camps
  read as four cards you could "just rotate" — nothing shows how they sit in
  relation to each other or the strength of their interplay. She first assumed
  cognitive connected to situated/sociocultural and asked whether magnitude of
  connection was conveyed. It wasn't.
- **Not grounded in a scene.** "What does this look like then?" — hard to feel
  the practicality without a concrete moment. (Same conclusion as the cascade
  above, reached independently → high confidence.)
- **Make the lens movable** — move it over things, something pops up, you see
  what's around it; the lens "asks different questions."
- **Circles, not squares** — squares feel rigid; circles give fluidity.
- **Sharpen the concept:** fish-eye ≠ "different perspectives." It's *different
  perspectives acknowledging each other* — you hold your own values while seeing
  where others sit in relation to you.
- **Be humble in framing** — "four possible ways to conceptualize" learning, not
  authoritative camps.
- **Audience:** anyone tunnel-visioned — the $5M AI-tutor VC, but also CMU
  learning-engineering researchers.

### The one real tension (and how we resolved it)

The **cascade** says the camps are *nested* (one zoom axis; wider = contains the
last). The **lens/madhhab** framing says they are *co-equal* (four interpretive
methods around one shared source, none wider/truer). A monotonic zoom-out quietly
argues **wider = truer**, which contradicts the thesis and would alienate the
behaviorist/cognitivist readers we want to reach.

**Resolution — use both, in sequence:**

1. **Cascade as the teaching spine.** Sequential zoom is the best pedagogy; keep
   it to *teach* the four lenses.
2. **A re-level beat** right after the cascade — one sentence that flattens the
   zoom into four co-equal questions. The camera move is revealed as just *one
   path through* the lenses, not a hierarchy. Draft: *"The pull-back made it feel
   like each view replaces the last. It doesn't. They're four questions asked of
   the same moment."*
3. **The fish-eye finale holds them all at once** (the kicker, now scene-based).

### The madhhab analogy (design DNA, not explicit framing)

The four Sunni madhhabs are four interpretive methodologies applied to **one
shared source**, differing in *usul* (first principles), not in goal. Mapping:

- shared source (Quran) ↔ **the shared scene**: a learner, learning
- *usul* (interpretive method) ↔ each camp's **epistemic commitment** (what counts
  as evidence of learning)
- *ikhtilaf* (legitimate disagreement, "a mercy") ↔ **perspectives acknowledging
  each other** — Carol's exact point
- *isnad* (chain back to the source) ↔ the fish-eye **situating one question
  within the others**, all anchored to the same moment

This answers Carol's relational critique *through the shared scene* — the camps
aren't related spatially in a diagram, they're related as four readings of one
source. Keep it as structure (shared source → four lenses → mutual recognition),
not stated framing — gesture at it in a footnote at most.

### The lens finale — design decision (Mode 5)

**One fish-eye lens, four anchor points. Do NOT build four lenses.** A
"behaviorist fish-eye" contradicts the thesis — the camp isn't *in* the lens,
it's *where you're looking*. Four lenses would re-create the silos we argue
against. One instrument, different focal points, periphery always populated.

The lens does what Wattenberger's does, plus our layer:

- **the image responds first** — the region under the lens enlarges/sharpens (the
  red mark grows, annotation appears) — *image first, then label*
- **the focal question renders in full** at the lens center: camp name, the
  question, and a one-sentence creed
- **the periphery curves** — the other three questions sit small at the rim, each
  positioned *in the direction of its anchor in the scene*. The periphery is a
  compass pointing at where the other camps live in this same moment.

**Spatial anchors in the scene:**

- **stylus / the wrong mark** → *behaviorist* (what can she do?)
- **her face** → *cognitive* (what does she understand?) — anchor on the face, not
  "the brain"; keeps it concrete and filmable
- **empty chair / unused tiles / the peer** → *situated* (how does she participate?)
- **edges + background** (poster, textbook, teacher's desk, the room itself) →
  *sociocultural* (whose knowledge counts?). Sociocultural is the *frame*, not a
  thing in it — dragging to the margins to find it is itself a tiny lesson.

**The contrast = two lens states in sequence, not two lens options:**

- **Beat 1 — the tunnel lens.** A plain magnifier first. Drag over the stylus: the
  behaviorist question appears, everything outside dims to near-black. The other
  questions don't exist. Copy: *this is the lens most of edtech is holding right
  now.*
- **Beat 2 — the swap.** The lens upgrades to the fish-eye. Same scene, same drag —
  now the periphery curves in and the other three questions never leave. The
  reader feels the difference *in their hands*. Mirrors Wattenberger's portrait →
  wide-angle → fish-eye arc, and says "tunnel vision is bad" without saying it.
  Build cost is near-zero: same lens code with periphery rendering switched off.

### The locked arc

> Meet Maruko → **cascade (slider)** → **instinctive pick** → **re-level beat** →
> **tunnel lens → fish-eye swap** → **quadrant sort** → final capture → tree close.

**REORDERED 2026-06-11 — cascade now leads, pick follows.** Teach first: the
cascade is light, image-forward, and gives an intuitive read of how the camps see
one moment before we ask anything of the reader. The instinctive pick then lands
as a *conscious* "even now, which would you reach for?" rather than the old
"catch yourself unaware" gotcha — gentler, and it **sets up the re-level**: the
lens you just grabbed doesn't beat the others; that's the point. (The rejected
*deferred*-reveal is still rejected; the pick's reveal is immediate.)

### The four swaps against the current `index.html`

Mapped to the prototype files (`camp-interactions.html`, `presentation-modes.html`,
`quadrant-sort.html`):

1. **Cascade ← the zoom-out slider** (`camp-interactions.html` Option 3). It's
   already the cascade skeleton — tick-snapping, nested-rings position indicator,
   crossfading frames. Steal the **"unit of analysis: ___"** line for each beat's
   info card — sharpest teaching language in any prototype.
2. **Instinctive pick** (`camp-interactions.html` Option 1) — DONE (first cut).
   Now sits **after the cascade** (see REORDER note): "What would you reach for?"
   → pick one unlabeled help → reveal "you reached for the ___ lens" + creed →
   the four camps fill in as cards (yours pre-opened + tagged; tap the others to
   see what each *would* have grabbed). We **kept the tap-to-reveal-the-others**
   beat (Vishal liked it). **All 8 prototype options, verbatim** (2 per camp,
   interleaved so camps aren't grouped, with the prototype's fuller descriptions)
   — Vishal saw the intentionality in the original set and wanted it kept whole;
   an earlier 6-option trim was reverted. List is **data-driven** (`PICK_OPTIONS`
   in `index.html`) so swapping a help or rebalancing camps is a one-line edit.
   The "tap to see what each would have grabbed" subtext was **removed** (the UI
   makes it clear). NOTE: prototype copy uses British spelling ("behaviour",
   "practises") — kept verbatim per request; flagged for possible normalization.
   Tracks `pick_choose` / `pick_reveal_open` / `pick_restart`;
   `instinctive_pick` added to the snapshot (the reader's default lens — key
   study data). The earlier "trim the four camp cards" note is **reversed** —
   those cards are the bit Vishal wanted to keep.
3. **Quadrant** (`quadrant-sort.html`) **replaces the dead product-bin sort**. The
   old sort had no payoff; the quadrant *is* a payoff — products land *between*
   camps, the center-of-gravity dot reveals "the field leans here." The thesis
   (the money is tilted) gets **discovered by the reader's own hands**. Quietly
   redeems the relational-field idea we'd dropped — the axes give Carol's
   "where camps sit in relation" as scaffolding for an activity, not an authored
   diagram. Keep one humility line: *a map, not the map.* Bonus: continuous (x,y)
   placements are far richer Stat 292 data than four bins.
4. **Mode 5** (`presentation-modes.html`) is the **finale, unchanged** — the lens
   design above. Transplant the iris prototype's *focus-arrives-from-a-direction*
   instinct: the rim chip nearest the lens swells into focus as you drag toward it.

**Cut entirely:** Option 2 (subsumed by the cascade), Option 4 (the quadrant does
its job without reintroducing ✓/✗ right-wrong framing), the iris widget's
card-switch machinery, and presentation Modes 1–4 (rings/pills/axes).

**Rejected idea (recorded so we don't revisit):** a *deferred* reveal on the
instinctive pick (pick early, reveal later). Breaks the interaction contract
(nothing happens on pick) and is incoherent (picking help for a child not yet
met). The pick comes *after* Meet Maruko and the reveal fires *immediately*.

### Build order (art is the critical path)

1. **Art first** — everything downstream depends on the four nested crops of the
   *same* moment. One generation session: the widest scene, then derive crops, so
   all four frames are pixel-consistent. Compose the anchors deliberately into the
   wide scene (her low-center, chair left, wall/board upper background) with enough
   visual quiet that lens anchors don't fight. Mode 5's rim chips work because the
   periphery is text; the cascade works because the periphery is image.
2. **Swap A (cascade)** — DONE (first cut). Replaced the four `.checklist`
   sections with one `data-scene="cascade"` section: the four nested crops stacked
   and crossfaded so stepping through them *reads* as a continuous pan-out. Drive
   = a **scrub slider** as the sole control (drag = continuous crossfade between
   adjacent crops); the **four bubbles** under it are quiet indicators that there
   are four to see — they light up + gently widen as you scrub (still clickable as
   a bonus, but no longer arrow-stepped). Each beat paints a text card (camp name + question +
   one creed sentence). New `track('cascade_view', {level, camp})` event added.
   The per-camp **helps are preserved** un-rendered in `<template id="camp-helps">`
   (seed for the instinctive pick + quadrant) — not deleted, not a rotting
   comment. Still to refine: image aspect ratios differ (act is landscape, world
   is portrait) so `object-fit:contain` letterboxes some beats — the pan isn't
   pixel-continuous yet; revisit once we see it in motion.
3. **Swap C (Mode 5)** — DONE. Ported `presentation-modes.html` Mode 5 into the
   `data-scene="fisheye"` section, replacing the old abstract four-cards-around-a-
   center widget (its CSS/HTML/JS all removed). Normal lens darkens all but the
   focus (tunnel vision); fish-eye keeps the focus sharp + the other three curve
   in as rim gist-chips. Base = `images/camp-situated.jpg` (4:3) — Vishal liked the
   prototype's actual scene (two kids / the partner) and wanted it kept **verbatim**,
   so anchors/gist/zoom are the prototype's originals (NOT the master). Note: this
   scene is itself a *situated* picture, so the beh/soc anchors point at regions
   that don't literally depict those camps — accepted on purpose; Vishal finds the
   scene strong. (`scene-master.png` is now unused in `index.html` but kept as the
   canonical wide frame.) Per-camp colours from the prototype were **dropped** to
   keep the restrained sage palette (lens = sage in fish mode, white in normal;
   chip labels + panel name = sage). Tracking: `fisheye_toggle` on each switch,
   `fisheye_focus` only when the lens crosses into a new camp's anchor (not every
   move). Anchors (`look:[x,y]` % in `FISH_CAMPS`, prototype-verbatim):
   beh=worksheet[68,72], cog=head[42,38], sit=table[58,55], soc=room[30,68].
4. ~~**Swap B (re-level beat)**~~ DONE / not needed as its own beat — the re-level
   is already two existing sentences: the pick's static line + the `lens-turn`
   opener ("each alone is a crop… the other views fall out of frame"), which
   bridges straight into the fish-eye. See REORDER note.
5. **Quadrant** — IN PROGRESS as a standalone prototype before slotting in.
   `quadrant-sort.html` was buggy on Safari: it lifts each chip to
   `position:fixed` and **reparents it to `<body>` mid-drag** while holding a
   pointer-capture — Safari drops the capture on reparent, so the drag stutters.
   New `quadrant-v2.html` reworks it: **one positioned board holds chips + field,
   no reparenting, no `position:fixed`**; drag sets `left/top`, drop flips a
   `placed` flag; geometry via `offsetLeft/offsetTop`; chips spring home on a miss;
   survives resize. Payoff kept (closeness bars + "the field leans here" COG dot).
   Vishal to test on Safari; slot into `index.html` (replacing the bin-sort) once
   it feels solid. **DONE — ported into `index.html`** (replaced the
   `data-scene="product-sort"` bin-sort with `data-scene="quadrant"`). Styles
   scoped under `.quadrant`; added `--c-beh/cog/sit/soc` camp tints to `:root`
   (quadrant only — rest of the piece stays restrained). Tracking upgraded to
   continuous data: `session.sort[name]={x,y,camp}` + `sortOrder` rows with x,y,
   and `quadrant_place` / `quadrant_remove` / `quadrant_reset` events (richer than
   the old four-bin counts). Hint copy: "…centre of gravity of everything you
   placed — in other words, your perspective on the field's current tilt."
   `quadrant-v2.html` kept as the standalone source/sandbox.

**Arc now built end-to-end** in `index.html`: cold-open → meet Maruko → cascade →
instinctive pick → re-level (existing copy) → fish-eye (Mode 5) → quadrant →
final capture → tree close. Remaining open items live in the "Open questions"
list up top (opening/capture placement, first-person turn, etc.).

Also a writing task: the Option 1 helps must be balanced so **no camp's option
reads as the obviously-correct grab**.

### Carry-through constraints (don't break these)

- **Protect the tracking layer** through every swap — anonymous clickstream
  (session id, toggles, fish-eye focus/toggle, sort placements, text saves,
  snapshots) is the Stat 292 instrument.
- Keep the **first-vs-final capture** drift intact.
- Don't let the "whose knowledge counts" beat re-import the real **Maya** as the
  sociocultural avatar — the camps belong to no one in the scene.

### Open questions resolved this session

- **Product sort:** RESOLVED — replaced by the quadrant (payoff, not cut).
- **Kicker form:** RESOLVED — the scene-based fish-eye warp (Mode 5) wins; it
  *embodies* the thesis rather than displaying it.
- **Cascade drive:** RESOLVED → scrub slider is the sole control; the four bubbles
  are passive indicators (light up + widen as you scrub). Arrows removed. Built in
  `index.html`. Scroll-driving can still be layered later.

### Art delivered (2026-06-11)

Generated via the proven workflow (one master scene → each beat re-attaches the
master + "the same scene, drawn tighter to X"). They are **true nested crops of
one continuous pan-out**, not separate scenes — the camera-move cascade works
literally now. Files in `new_imgs/` (renamed from the upload's working names):

- `scene-master.png` — the canonical wide frame; **doubles as the Mode 5 lens
  base** (all four anchors visible at workable size: hand, face, empty chair,
  wall/window).
- `scene-act.png` — tightest crop, hand + screen: ½ + ¼ = ¾ marked with a **red
  ✗**, boxed answer, progress dots, sage in the fraction bars. (**behaviorist**)
- `scene-face.png` — pulled to her in three-quarter. (**cognitive**)
- `scene-table.png` — full table, the **empty chair** + untouched tiles.
  (**situated**)
- `scene-world.png` — pulled all the way out: room, ceiling light, teacher's
  desk, board. (**sociocultural**)

Continuity held: the **empty chair** survives master → table → world (the
"cold of absence" lands), and the **red wrong-mark** replaced the old
checkmark/success cue. Fruit-red (#9c3b2e) is now a second, very sparing accent
meaning *the error*; sage stays the living accent.

**Annotation overlays: DROPPED.** Earlier idea was faint code/SVG layers (the
cognitive thought-web, the sociocultural vignettes) over the clean crops.
Cut for simplicity — empty paper *is* the aesthetic, and overlays would clutter
the quiet and re-introduce the "diagram" feel Carol pushed us away from. The
composition already teaches (red ✗ = observable behavior, posture = the mind,
empty chair = missing partner, room = the deciding frame); the text card carries
the precision. **Back-pocket exception:** the **cognitive** beat leans hardest
on its text label (visually closest to its neighbors). If it tests flat once
wired, the targeted fix is a single faint thought-web on `scene-face.png` only —
not a system across all four. Do not build it pre-emptively.

### One more change from Vishal:  — DONE (2026-06-11)

The learner is now **Irfan** (he/him) throughout `index.html`: meet-intro, cascade
beats + alt text + scrub aria, instinctive-pick data, fish-eye data, the preserved
`#camp-helps` template, and the CSS comments. Verified: no residual
`Maruko`/`she`/`her` referring to the learner. (`data-scene="meet-maya"` id and the
`images/meet-maya.jpg` filename left as internal, per the earlier rename note.)

**Other copy/structure changes this pass:**

- **Positionality beat commented out** (the "brilliant people / something feels off
  / Biesta learnification" framing) — too abstract/quick up front; the piece now
  goes cold-open capture → straight into meeting Irfan. Preserved as an HTML
  comment for reference.
- **Pick heading**: "What would you reach for?" → **"In this moment, how would you
  help?"**; the "she's still stuck…" subtext line **removed** (grid alone).
- **Pick affirm line**: → "None of the four is wrong, they just attend to different
  questions in the same moment."
- **Lens-turn message** (humbler, "perspectives" not "them"): "Each of these
  perspectives is true. None is the wrong way to look. An issue arises, however,
  when a perspective is held alone: it becomes a crop of education, and the other
  perspectives fall out of frame."
- **Fish-eye heading**: "Holding them all at once." → **"Try the fish-eye lens
  yourself."** (+ subtext "…now the lens is in your hands, and you choose where to
  look.").
- **Blockquote moved**: the Vishal & Yoyo quote left the fish-eye section and now
  sits in the tree-close, directly above the "With thanks to Amelia Wattenberger…"
  footnote (poetic closing line kept). End reads: tree image → closing line →
  Vishal & Yoyo quote → Amelia credit.
- **Ending**: confirmed the piece ends on the final hypothesis capture, then the
  tree-close bun (first-vs-final drift preserved).

#### Original note (kept for the name's meaning)

change the learners name to Irfan: meaning: the wisdom gained through lived experience and mistakes. In Arabic, عِرفان
tanslates to "knowledge," "recognition," or "gnosis" (experiential wisdom). it fits our story: Unlike dry, academic knowledge (Ilm), Irfan specifically refers to wisdom gained through discovery, awareness, and personal experience. It is the perfect philosophical concept for a child who learns what is right by first getting it wrong.The English/Modern Feel: Irfan functions excellently as a gender-neutral name in modern fiction. It has a soft but intelligent cadence, sounding similar to names like Rowan or Kieran, but with a rich Arabic heritage. Also, update the pronouns to he/him please.