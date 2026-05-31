# What is education for?
### An explorable explanation — full script and visual bible

A project by Vishal and Yoyo.
Educ 432 (Explorable Explanations) · Stat 292 (Statistical Models of Language and Text), Stanford.

---

## How to read this document

There are two voices in here, and they are deliberately different.

**Screen voice** is what the player actually reads. It is plain, simple, honest. Short declarative sentences. No em dashes, no performance, no edge. The feeling comes from the situation, the art, and the music — never from the words straining to be poetic. When you see `ON SCREEN:` blocks, that text is close to final and should change only to get simpler, never fancier.

**Brief voice** is everything else — the staging notes, the visual bible, the camera grammar. This is written richly and concretely on purpose, because an artist or a coding agent needs specific, buildable detail. Vivid here is useful. Vivid on screen is not.

If on-screen text ever starts performing the feeling, the fix is the same phrase we used while writing this: *window, not stage.*

---

## The spine, in one sentence

A tree cannot grow in a void. Learning cannot grow outside human relationship. Humans are not who learning is *for* — they are the medium learning happens *in*.

The whole piece exists to let the player arrive at that on their own, by sitting with one ten-year-old, and to never once say it as a claim.

## The two questions

The piece runs on two recurring questions, and they do different jobs.

- **"What is education for?"** — the *far* question. Asked first (most abstract, the whole field) and last (after the player has been up close). This is the bookend. It carries the scope idea: everyone is right inside their own frame, and we rarely zoom back out.
- **"What does Maya need right now?"** — the *near* question. Asked three times, word for word, around one child. This is the spine. The player watches their own answer drift, and that drift is the argument.

## What we capture (for the Stat 292 analysis)

Five free-text answers per consenting player, plus optional profession:

1. "What is education for?" — opening (most distal)
2. "What does Maya need right now?" — at meeting her
3. "What does Maya need right now?" — after the support screen
4. "What does Maya need right now?" — at the close
5. "What is education for?" — closing (distal again, post-journey)

This gives two distal bookends and three proximal points: a clean trajectory in embedding space across **levels of distal-ness**, which is exactly the thing being studied. The doodle is never analyzed. It is the one input the system cannot read, by design.

---

## Global world

**The container.** The whole thing feels like a quiet notebook or a picture book you are turning through. Warm paper. Hand-touched, not chrome. The author voices (Biesta, Holmes, Edelman) live in the *margins* of these pages as small pencil notes — periphery of attention, which is itself the curriculum-as-attention point, made physical. It ends on a bulletin board: the player's own pinned drawing beside the makers' note and the final concept art.

**The motion grammar — counterpoint zoom.** The conceptual camera pulls *out* across the whole piece (from a single narrow form to the whole living tree — this is the scope/fish-eye idea). The emotional camera pulls *in* (from "education," an abstraction, down to one specific child). These run at the same time and against each other. As you widen to see the whole system, you also fall for one kid. Hold both. That tension is the felt experience.

**The two palettes.** The world is warm. The *system* is cold. The only cold screen is the tutoring software (M3). The coldness should never be narrated; it is carried entirely by color, type, and layout, so that when the player returns to warm paper afterward they feel the temperature change in their body.

| | Warm world | Cold system |
|---|---|---|
| Background | `#fdf6ee` (paper) | `#f0f4f6` (screen grey-blue) |
| Primary text | `#2d2420` (ink) | `#4a6a7a` (terminal blue) |
| Mid text | `#6a5a4e` | `#7a9aaa` |
| Faint | `#a09080` / `#c0b0a0` | `#cddde5` (rule) |
| Accent | `#c4a882` (tan) / `#9a7850` (tan-dark) | none — flat |
| Living accents (tree only) | soil-green `#6a7a52`, leaf `#c4a882`, fruit `#b8553c` | — |
| Type | Georgia / serif | Courier / monospace |

**Type rules.** Serif for everything human (questions, narration, Maya). Monospace only inside the system. System-ui sans, tiny and tracked-out, only for labels and captions (`letter-spacing: 0.14em`, uppercase). Questions are large and calm (~30px), never bold.

**Sound (later).** Pensive, gorgeous, sparse. The reference points are the quiet exploration cues of Zelda and the between-scene piano of Avatar. Music is warm everywhere *except* M3, where it thins to near silence or a faint electrical hum, then warmth returns at M4. Silence is a tool. The doodle moment and the final tree should have the most music; the system screen should have the least.

---

# PART ONE — THE SCRIPT

Each scene gives the staging (brief voice), the exact on-screen text (screen voice), the interaction, and what we capture.

---

## Screen 0 — Consent (optional, skippable)

**Staging.** Bare warm paper. No imagery yet. This screen earns trust by being plain and honest, because the whole piece will later argue against treating people as data. We practice what we preach in the first ten seconds.

> **ON SCREEN:**
> One optional thing before we start.
>
> I'm studying how people's view of education changes as they move through this. If you tell me what you do, I'll keep that along with the few lines you write here. No name. Nothing else.
>
> You can skip this and everything works exactly the same. You can read the why at the end.
>
> `I do this: [ ________________ ]`   `[ continue ]`   `[ skip ]`

**Interaction.** Profession is free text but stored as a coarse category (avoid re-identifying rare titles). Skipping sets a no-collect flag for the whole session.
**Capture.** Profession (optional). Consent flag.

---

## Screen 1 (M1) — The far question

**Staging.** This is the most abstract moment in the piece, so it gets the most abstract image: a cold, flat, top-down diagram of concentric rings, drawn like a system schematic or a target. The player does not know it is a tree seen from above. It reads as clinical, map-like — the way the field looks at education, as a system to optimize. Slow, quiet. One question, centered.

> **ON SCREEN:**
> What is education for?
>
> `[ text field ]`
> `press enter when you're ready`

**Interaction.** Free text, enter to continue.
**Capture.** Answer 1 (most distal).

---

## Screen 2 (M2) — Meet Maya, and leave her something

**Staging.** The cold rings fall away and we land on warm paper, close. The conceptual camera has zoomed *in* — from "education" to one child. This is the first warmth in the piece and it should feel like relief after the schematic. Text is plain. Her doodle space waits in the margin, empty, until the player fills it.

> **ON SCREEN:**
> Meet Maya. She's ten.
>
> She's a really hard worker. For three weeks she's been working through the same page in her homework on fractions.
>
> She gets the first step right almost every time. But then she stops at the same place each time, just before the end. It's unfortunate, because lately in class she's stopped raising her hand.
>
> In the corner of every worksheet, she draws.
>
> *Leave something in the corner with her.*
> `[ small drawing canvas ]`   `[ skip ]`

*(After the player draws or skips — the doodle appears in the margin and stays there for the rest of the piece. Skip falls back to the horse.)*

> What does Maya need right now?
> `[ text field ]`

**Interaction.** Drawing canvas (simple freehand, one color, no labeling, no "what is this?"). Then the open question.
**Capture.** Answer 2. The doodle is saved as the player's asset but **never analyzed**.

> *Margin glint (pencil, right edge): "learnification" — Gert Biesta, on education shrinking until it means only "learning."*

---

## Screen 3 (M3) — What the system sees

**Staging.** Hard cut to cold. The entire screen becomes the tutoring software looking at Maya. No narration, no caption, no "the same session two ways." The player just arrives inside the machine's view of the child they just met. The contrast is against *their own answer two screens ago* — they wrote something human about her; here is how she is logged. Monospace, grey-blue, flat, tracked-out labels. The music thins almost to nothing.

> **ON SCREEN (rendered as a software dashboard):**
> ```
> LEARNER #4417            UNIT 4.3  Equivalent Fractions
>
> Mastery estimate ........ 0.41   ▼ below target
> Days on current item .... 19
> Hints requested ......... 37
> Attempts ................ 52
> Engagement .............. LOW
> Off-task events ......... 14   flagged
>
> RECOMMENDED ACTION
>   › re-serve prerequisite 4.2
>   › increase hint frequency
>   › notify instructor dashboard
> ```
> `[ continue ]`

**The silent detail.** The "14 off-task events, flagged" are Maya drawing in the corner. The system sees her most human act as an error to correct. We never say this. The player who notices, notices. The player who does not still feels the chill.
**Interaction.** A single flat "continue." Nothing here is warm or clickable-feeling.
**Capture.** None.

> *Margin glint (pencil): "the pathway may be personalized, but not the destination." — Holmes et al., 2022.*

---

## Screen 4 (M4) — What would you give her

**Staging.** Warm paper returns. Relief again. The player has just seen Maya reduced to a number; now they are invited to help, and they will want to. The four options are all real, good things — and all of them are system features. None of them is "sit with her." The menu can only sell trunk; it cannot sell soil. That incompleteness is the whole argument, so **do not ever add a human-contact checkbox.**

> **ON SCREEN:**
> Maya uses a tutoring app at school. It watches how she does and changes the lessons to fit her.
>
> What support would you give her?
> `☐ Have her teacher look over her progress each week`
> `☐ Send her parents a weekly progress report`
> `☐ Add a discussion forum to the app`
> `☐ Give her fifteen minutes with a human tutor each week`
>
> Maya sits next to four of her friends in class. It's unfortunate, because lately she hasn't really talked to any of them.
>
> What does Maya need right now?
> `[ text field ]`

**The quiet rhyme (do not point at it).** Four supports on the menu; four friends beside her. The system offers four mechanisms, life offers four people, and neither reaches her.
**Interaction.** Checkboxes (the player will likely check all — that generosity is the setup, not a trap). Then the open question.
**Capture.** Answer 3. (Optionally: which boxes were checked — mild, useful, but keep it out of the way.)

---

## Screen 5 (M5) — She improves

**Staging.** The system succeeds on its own terms. Numbers tick up; Maya "finishes." And what we show for that success is a bare, dry trunk — bark, no canopy, no soil, no leaves. The least living part of a tree, presented as the win. This is the hollow-trunk image we agreed on. Minimal words. Let the dryness do it.

> **ON SCREEN:**
> A few weeks later, Maya finished the page. Her scores went up. She moved on to the next one.
>
> *(the trunk: tall, bare, dry)*

**The silent argument.** Every metric is green. The image is dead wood. Success by the numbers looks like the part of the tree with nothing growing on it. We are not saying the supports were bad or that improvement is bad. We are saying this is not yet a tree.
**Interaction.** Scroll / continue. No question here; this is a held breath.
**Capture.** None.

> *Margin glint (pencil, late): Biesta — if education is only preparation, are we teaching for a world that will still exist?*

---

## Screen 6 — The near question, last time

**Staging.** The conceptual camera finally begins its big pull-back. The bare trunk is still on screen, and the view starts to widen — soil coming in below, air and light above. As it opens, the question returns one final time, unchanged.

> **ON SCREEN:**
> What does Maya need right now?
> `[ text field ]`

**Interaction.** Free text.
**Capture.** Answer 4 (final proximal).

---

## Screen 7 — Your words

**Staging.** The player's three answers to the same question rise onto the page in order, labeled only by moment. No commentary. The piece does not interpret the drift; it just shows it. For a player whose answers barely moved, three steady lines is its own honest statement and is never framed as a failure.

> **ON SCREEN:**
> When you met her, you wrote:
>   *[ answer 2 ]*
>
> After you saw who was around her:
>   *[ answer 3 ]*
>
> Just now:
>   *[ answer 4 ]*
>
> Your words.

**Interaction.** Hold. A beat. Then the reveal continues into the tree.

---

## Screen 8 — The tree (the one place the piece may speak)

**Staging.** The pull-back completes and tips. The flat cold rings from the very first screen rotate and bloom into the tree seen from the side — alive, warm, soil and canopy and light. The labels that were blank schematic rings at the start now fill in. This is the only moment the piece is allowed to name its idea, and it does so as art, like a between-scene title card, not as a sentence of argument. A player who is moved can linger and study it. A tired player can simply close.

> **ON SCREEN (over the concept art, labels resolving in):**
> soil, air, light.
> the things a tree can't grow without.
>
> we never named them.
> you might have, by now.

**Interaction.** Static, lingerable. The art is studied, not clicked.

---

## Screen 9 — The board

**Staging.** Everything comes to rest on a bulletin board. The player's untouched doodle is pinned beside the makers' note and the concept art. The player is not shown a conclusion; they are looking at a wall they helped make. Their unreadable mark sits beside the words as an equal. The far question is asked one last time and pinned with the rest.

> **ON SCREEN (pinned, in order of size — art and doodle largest):**
>
> *[ the tree concept art ]*   *[ the player's doodle ]*
>
> What is education for?
> `[ text field ]`
>
> *(smaller card, pinned in the corner:)*
> Hi, I'm Vishal. I made this with my dear friend Yoyo as a project for Educ 432 (Explorable Explanations) and Stat 292 (Statistical Models of Language and Text) at Stanford.
> If you said yes to sharing your words and what you do, I'll use them to study how people's view of education shifts as the question moves from far away to up close, by looking at how the answers move in neural embedding space.
> Your responses are anonymous. You can change your mind: `[ opt out ]`

**Interaction.** Final free text (the closing bookend). Then rest.
**Capture.** Answer 5 (closing distal). The feeling lands first; the housekeeping sits quietly underneath.

---

# PART TWO — THE VISUAL BIBLE

Deep visual direction, scene by scene. Written so you can draw it by hand or hand it to a coding agent. Each scene: the space, the composition, the color and type, the texture, the motion, and the one thing that must not break.

---

## The world's materials (applies everywhere)

- **Paper.** The warm background is not flat `#fdf6ee` fill — give it the faintest paper tooth: a 2–3% noise or a very soft fiber texture, barely visible, so it reads as a held object rather than a webpage. Edges of "pages" can have a hair of shadow as if the sheet is lifting.
- **Ink.** Body text sits like ink on that paper — `#2d2420`, never pure black. Slight warmth.
- **Pencil margins.** Author glints are in a softer grey-brown (`#a09080`), smaller, set in the right or left margin, as if annotated by hand. They never interrupt the column; you can read the whole piece without them.
- **The doodle.** Drawn in a single warm graphite tone. Once made, it lives in the same fixed margin spot on every subsequent page, like a sticker the player placed. It is never recolored, never animated, never interpreted. It is the only thing on screen that the design itself refuses to touch.
- **Motion easing.** Everything moves slowly and settles softly (ease-out, 0.6–0.9s). Nothing snaps. The one exception is the cut into M3, which is hard and immediate.

## Camera grammar (the through-line a three.js build should encode)

Think of one continuous vertical axis. At the top, far above, is the abstraction ("education," the rings seen from straight overhead). At the bottom is the soil. The whole piece travels down this axis and then the camera tips from looking-down to looking-from-the-side.

- **M1:** camera pointed straight down the axis. We see rings (a tree's plan view) but read them as a flat schematic.
- **M2–M5:** we are down at ground level with Maya, the camera close and intimate, the axis temporarily forgotten. Conceptually we have zoomed *out* in scope (we now know the abstraction has a real child under it) while the shot has zoomed *in* emotionally.
- **M6–M8:** the camera pulls back and **tips ninety degrees**, from looking down (rings) to looking from the side (tree). The same geometry that read as a cold target now reads as a living thing. This rotation is the climax and should be one continuous, slow, breathtaking move, ideally with sound swelling for the first time in full.

---

## M1 — The rings (cold schematic)

- **Space.** Dead center, symmetrical, a lot of empty paper around it. Feels like the title plate of a technical manual.
- **Composition.** Three concentric rings plus a small dark core dot. Thin strokes. At this stage the rings are **unlabeled or labeled only with cold, generic schematic text** (e.g. faint tick marks, a coordinate feel). The player must not yet suspect a tree. It could even read as a target, a dartboard, an optimization landscape contour map.
- **Color.** Resist warm here. Use the cold palette or a desaturated version of the warm one — greyed tan, thin blue-grey rules. The first real warmth is deliberately withheld until Maya.
- **Type.** The question in calm serif, large, above or below the rings. One line of faint sans instruction.
- **Motion.** Rings draw on slowly, like a compass tracing them. The core dot last. Then stillness while the player types.
- **Must not break.** No green, no leaves, no life. This image has to be *re-met* at the end as a tree; if it looks alive now, the ending reveal dies.

## M2 — Maya, warm, close

- **Space.** We drop from the centered schematic to an off-center, intimate page. Think of a single page of a picture book: text left or center, the margin (right) reserved and slightly indented for the doodle.
- **Composition.** Generous line spacing. The eye moves text → "she draws" → empty margin box → (player draws) → question. The empty margin should quietly invite before it is named.
- **Color.** Full warmth arrives here for the first time. Paper `#fdf6ee`, ink `#2d2420`, a single tan rule or accent. The warmth itself is the emotional event after the cold rings.
- **The canvas.** Small, bordered faintly (`#e8ddd0`), one graphite stroke weight, no color picker, no tools, no undo-clutter. The smaller and plainer the better — it should feel like the corner of a worksheet, not an app. On commit, the stroke "settles" into the margin with a soft fade.
- **Motion.** Text fades in a line at a time, slowly, so the player reads at the pace of someone being introduced to a child. Nothing rushes.
- **Must not break.** The doodle is the player's, made *for her*. Framing must stay other-directed ("leave something with her"), never "draw your favorite animal." And the moment must never be gamified.

## M3 — The system's view (the only cold screen)

- **Space.** The cold fills the entire frame, edge to edge. No warm paper border. The player is *inside* the machine now, not looking at it on a page.
- **Composition.** A dashboard. Left-aligned monospace rows, dot-leaders to the values, a boxed "recommended action" block. Cold, aligned, efficient. It should look competent and well-designed *as software* — this is not a strawman; good ed-tech looks like this. The horror is that it is good at what it does.
- **Color.** `#f0f4f6` field, `#4a6a7a` text, `#cddde5` rules. The "▼ below target" and "flagged" in a slightly more saturated alert tone but still cold. No warm pixel anywhere.
- **Type.** 100% monospace. Tracked-out sans only for the column header.
- **Motion.** Hard cut in (no fade — the abruptness is the point). Values can tick/populate quickly and mechanically, the opposite of M2's slow human fade. Music drops out here.
- **Must not break.** No narration, no caption telling the player it is cold. The "14 off-task events flagged" line is the buried heart — it must be present and must never be explained. Let it sit.

## M4 — The offer

- **Space.** Warm paper returns, and the relief should be palpable after M3. Same picture-book intimacy as M2.
- **Composition.** The four checkboxes as a clean, calm list. Below a small breath of space, the friends line. Then the question. The checkboxes are visually pleasant and easy to say yes to — we *want* the generosity.
- **Color.** Warm. Checked boxes get the tan accent, a small warm confirmation — the player's kindness lighting up.
- **Motion.** As each box is checked, a soft, warm tick. After the fourth, a small pause before the friends line appears, so the generosity is felt *before* the ache.
- **Must not break.** Every option is a system feature; none is human contact. The list is complete-looking but incomplete in truth. Adding a "spend time with her" option would collapse the entire piece.

## M5 — The hollow trunk

- **Space.** We begin to feel the vertical axis again. The trunk stands alone, centered, tall, with empty space above where a canopy should be and nothing below where soil should be.
- **Composition.** A single bare trunk. No branches, or a few stubbed, bare ones. The negative space above it is loud — the eye expects a canopy and finds sky-less blank.
- **Color & texture.** This is where the earlier caution lives: the trunk must read as the **driest, least alive** thing in the whole piece. Grey-brown bark, cracked, matte, no highlights. Contrast it later against the lush tree. Green metrics (✓, "scores up") can sit beside it in cold system-tone, so the win and the deadness share the frame.
- **Motion.** Metrics tick up briskly (system rhythm). Then everything stops and we just hold on the dry trunk, longer than is comfortable. The discomfort is the content.
- **Must not break.** Do not prettify the trunk. If it looks like a strong, handsome tree-in-progress, the player reads the trunk as the goal — the exact inversion we are fighting. It must look like success that feels like nothing.

## M6–M8 — The pull-back, the words, the tree

This is one continuous move; treat it as a single sequence.

- **M6 (the question over the widening).** As the camera starts pulling back from the trunk, soil tones bleed in at the bottom, light at the top. The final "what does Maya need" sits over this opening view. The player answers as the world is quietly coming alive around the dead trunk.
- **M7 (your words).** The three answers rise like things being lifted into light. Plain serif, generously spaced, each on its own line with its quiet label. "Your words." sits last and smallest. No effects, no flourish — the content is the player's own sentences, which need nothing added.
- **M8 (the tip and bloom).** The big one. The camera completes its pull-back and **rotates from overhead to side view.** As it tips:
  - the flat concentric rings resolve into depth and become the tree's structure — outer ring → the spread of soil-and-air (the medium), middle ring → the tree's living body (learning), core → the trunk (the form);
  - **soil** grows in at the base, dark and rich, roots reaching into it;
  - **canopy** opens at the top, leaves in tan/`#c4a882`, a few fruit in `#b8553c`;
  - the dead trunk from M5 is revealed to have been *part of this tree all along* — now with a canopy above and soil below, it stops looking dead, because it was never meant to stand alone;
  - **labels resolve in** for the first time: soil/air/light = the medium; the words "soil, air, light" appear as the only permitted statement.
  - one fruit falls, slowly, and lands in the soil. (This is the loop: what you learn returns to the human ground it came from. Do not explain it. Let it fall.)
- **Color.** This is the warmest, most alive frame in the entire piece — the full living palette, soil-green, leaf-tan, fruit-red, warm light. Maximum contrast with M1's cold rings and M5's dead trunk.
- **Sound.** Music reaches its fullest here, for the first and only time at full warmth.
- **Must not break.** The rings-to-tree must be legibly the *same object* rotating, not a cross-fade between two unrelated images. The player should feel "oh — it was a tree the whole time, I was looking straight down at it." That recognition is the entire emotional and intellectual payload.

## M9 — The board

- **Space.** Pull back once more to reveal everything pinned on a warm cork or paper board.
- **Composition.** A gentle hierarchy: the tree concept art and the player's doodle are the two largest pinned pieces, side by side as equals. The final question and its field sit among them. The credit/consent card is smaller, pinned in a corner — present, honest, not the focus.
- **Color & texture.** Warm board, soft pin shadows, the doodle on its own slightly tilted scrap of paper so it reads as a real thing the player made and placed.
- **Motion.** Items settle onto the board with soft pin-drops. The doodle settles last, a small spotlight of attention, then released.
- **Must not break.** The doodle and the makers' note are equals on the wall. The player is a co-author here, not an audience. End on feeling; let logistics sit underneath.

---

# PART THREE — THE CONCEPT-ART SPEC (rings ↔ tree)

The M1 rings and the M8 tree are two views of one model. This section is the full anatomy, so the concept card can be labeled with real depth, and so the optional overlay layer has something to build from. Reference sketch: `tree-rings-anatomy.svg` (this folder). An earlier two-view rough also exists: `tree-rings-two-views.svg`.

## The two views, briefly

- **Plan view (overhead, M1):** concentric rings. Outer = relationship / the medium. Middle = learning. Core = the forms. At M1 these are unlabeled and cold — a schematic, a target.
- **Elevation view (side, M8):** the same object as a tree. The medium is soil below plus air and light above, which is *why* it was the outer ring — it surrounds. Learning is the tree's whole vertical body. The forms are the trunk core.
- **Why the tree is the destination, not the rings:** the rings can only show "around." They cannot show "below *and* above." The tree shows that relationship brackets learning on both ends, and that the fruit returns to the ground. The rings are the impoverished map; the tree is the territory. Start cold and flat; end warm and alive.

## The tree, fully labeled

Every element carries a meaning, a role in the converge/diverge rhythm, and a visual treatment. On the M8 card these appear as quiet pencil labels a lingering player can study — never as narration.

| Element | Label on the card | What it means | Rhythm | Visual treatment |
|---|---|---|---|---|
| **Soil** | the medium (humanity) | The human ground. Relationship, the broader process of living that learning sits inside. Where we come from and what we return to. | the origin and the destination | Dark, rich, textured, alive. Lushest element alongside the canopy. Named only at the very end. |
| **Roots** | where we each begin | Each person's own twisted, unique experience, drawn up out of the human ground. Many, and all different. | **diverge** (many) | Many fine roots, each shaped differently, spreading wide into the soil. |
| **Trunk** | the shared objective · the scaffold | The learning outcome. The funnel. The convergent anchor everyone gathers to. Necessary, but the part that looks *least* alive — bark, sealed off, the one stretch not touching soil or air. | **converge** (the one) | Driest, most matte element. Grey-brown bark, cracked, no highlights. The caution lives here: it must never look like the point. |
| **Canopy** | what we make together | Co-construction. Community of practice. The branching back out into open air once the scaffold is shared. | **diverge** (many again) | Lush, branching, open to the light. Leaf-tan, the most generous shape on the page. |
| **Leaves & fruit** | what comes of it | The meaning and understanding produced *after* the objective became a scaffold rather than a destination. | the yield | Many leaves; a few warm-red fruit nested in the canopy. |
| **Falling fruit** | and it returns | What you learn falls back into the human ground and re-seeds. Knowledge builds on knowledge. The tree is one community of practice; its fruit starts the next. | **re-seed** (new divergence) | A single fruit caught mid-fall, between canopy and soil. |
| **Air & light** | the medium, above | Relationship surrounds from above too. The canopy lives *in* it. With the soil, it brackets learning on both ends. | surrounds | Soft warm light from the top; a simple sun glyph. |

## The breathing (the whole tree is one converge/diverge cycle)

Read bottom to top and back into the ground:

**roots (diverge) → trunk (converge) → canopy (diverge) → fruit into soil (re-seed → new roots).**

The tree is the converge/diverge rhythm drawn as a single living thing. And it stands the means/end inversion up on its feet: the **trunk** looks like the point, but its whole job is to hold up the canopy and the fruit; the **soil** looks like mere backdrop, but it is both the origin and the destination. The form is the means. The medium is the end.

## What gets named, and when

- **M1:** rings are blank, cold, unlabeled.
- **M2–M5:** nothing is named. The player does all the meaning-making.
- **M8:** the labels resolve — but the only words the piece *says aloud* are "soil, air, light." The fuller anatomy (roots, trunk, canopy, fruit, the rhythm) appears as studyable pencil labels on the concept card, like the cutaway diagrams between scenes in Avatar or the title plates in a good picture book. The tired player sees a beautiful tree and closes. The curious player reads the entire diagram and finds the argument waiting there, having never been preached.

## The optional overlay layer (a side path, never the spine)

The different learning "shapes" overlay onto the tree so each camp can recognize itself — and then notice what it is missing. Build this only as an opt-in zoom the curious can choose. It is never on the resting card and never on the main road, because *cataloguing the shapes is not the same as feeling what Maya needs.*

- **One-on-one ITS tutoring → a very narrow trunk (a tube).** Master to student, a fast narrow channel straight to the objective. Quick to the trunk, little canopy, barely touching soil. *All trunk.*
- **Classroom / small group → a wider funnel-trunk.** Many students converged into one shared objective. A wider mouth feeding the same trunk.
- **Tube with a fan → a narrow trunk that opens at the top** into a horizontal spread of directions (individualized destinations). Still narrow, but branching at the very end.
- **Community of practice → an open ring (the space).** It can sit at *any height*: low, scaffolded around the trunk and its objective; or high, once everyone already shares the trunk, where the canopy itself *becomes* the community of practice.

**The teaching move the overlays enable:** zoom in on any one camp and let them feel seen, then pull back out to show they are one part of the same tree. A pure ITS overlay is all trunk — no soil, no canopy. An undirected community of practice can be all canopy with no trunk to stand on. Neither is wrong; each is simply missing the rest of the tree. This is point 1 — everyone right within their scope, nobody recognizing each other — dramatized instead of asserted, which is exactly why it has to stay optional and gentle.

## How it shows up as the M8 concept card (build note)

- The **hero** is the labeled elevation tree, warm and fully alive.
- A small **overhead-rings inset**, cornered, reads "the same tree, from above" — closing the loop back to M1.
- The **overlay variants** live one layer deeper, reachable only if the player chooses to explore; they are not on the resting card.

---

# PART FOUR — THE MARGIN GLINTS

Short, attributed, a clause each, in pencil-grey in the margin. They are optional texture. Read together by a curious player, they quietly show three thinkers reaching the same wall in three different vocabularies that never quite met — which *is* the "everyone is right, nobody recognizes each other" point, never asserted.

- **Near M2/M3:** Biesta — on "learnification," education shrinking until it means only learning.
- **Near M3/M4:** Holmes et al., 2022 — "the pathway may be personalized, but not the destination."
- **Near M4:** Edelman — funnels, tubes, and spaces as three design mentalities.
- **Near M5 (late):** Biesta — if education is future-proofing, are we teaching for a world that will still exist?

Keep them as glints, not blocks. Never more than a clause. Never in the main column.

---

# PART FIVE — DATA & CONSENT (practice what the piece preaches)

- Collect profession (coarse category) + the five free-text answers, only with the up-front yes. Never the doodle.
- The warm-timeline / cold-log distinction in M3 applies to *us*: be the warm timeline. Transparent, anonymized, opt-out honored.
- Because this collects written responses from the public for analysis, treat it as human-subjects research: email the Educ 432 / Stat 292 course staff this week and get the IRB determination (most likely exemption) before any public release. To the statistician you want as a recommender, "I sorted the IRB exemption before launch" reads as thinking like a researcher.

---

# PART SIX — OPEN DECISIONS (still yours to make)

1. **The reveal pace in M7** — show all three answers at once (cleaner) or one at a time with a breath between (more affecting, slight sentimentality risk). Leaning all-at-once.
2. **M3 detail** — do we let the player hover/expand a row to see "off-task event → drawing in margin," making the buried heart findable, or keep it fully buried? Leaning fully buried.
3. **Music entry** — does any music play under M1, or does the first sound arrive only with Maya in M2, so warmth and sound arrive together? Leaning sound-with-Maya.
4. **The opening rings** — fully abstract/target-like, or faintly tree-suggestive so the ending reveal has a "of course" rather than a "wait, what"? Leaning fully abstract, trusting the tip to land it.
5. **Doodle at the end** — confirmed untouched. (Decided.)

---

*End of script. Window, not stage.*
