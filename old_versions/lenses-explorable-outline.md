# Four Lenses on Learning
### An explorable explanation — design outline

A project by Vishal and Yoyo
Educ 432 (Explorable Explanations) · Stat 292 (Statistical Models of Language and Text), Stanford
Final due 6/10/2026

---

## Current status (as built — updated 2026-06-01)

This outline is realized in `lenses.html`. The design is preserved below as the rationale; this section records what was actually built and where the build went past or settled the outline.

| Beat | Status | As-built notes |
|---|---|---|
| 0 — Cold open | ✅ Done | Fresh case chosen: **Alex**, six weeks into learning to code, stuck on a Karel-style loop exercise, in a course built around a community they haven't used. Question: *"What does Alex need right now?"* Captures Answer 1. |
| 1 — Lens-switcher | ✅ Done | Cursor-as-lens with custom SVG cursors; interactive scene with clickable elements; per-lens sidebar (foregrounded / noise / recommends / cannot see); page tints to the active lens. **Built beyond the outline:** three switchable cases — Alex, Maya, Devi (adult learner at a music jam) — not one. Soft 2-lens nudge before continue. |
| 2 — Catalogue + generate | ✅ Done | 2D map; axes *individual ↔ system/collective* (X) and *observable performance ↔ inferred meaning* (Y); 9 pinned patterns with profile cards; add-your-own modal (name, description, lens checkboxes, click-to-place). |
| 3 — Positionality | ✅ Done | Same map; 3 sequential markers (*your design instinct · where you learned best · your current work or practice*); pinned patterns kept faintly visible (opacity ~0.18); free-text reflection captured. |
| 4 — Design-bench | ✅ Done | 4 context options; 5 sliders (directionality, scaffolding, group structure, tool reliance, cultural specificity); live dot on the map; four live lens-readings; commit step (trade-off + predicted failure); closing reflection recalls the cold-open answer. |
| Data persistence | ❌ Not built | In-memory only (`window.lensSession`) + console-log. No backend. |
| IRB | ❌ Outstanding | Required before any public release that collects real answers. |

**Capture, as built:** Answer 1 (Beat 0, *what does Alex need*), Answer 3 (Beat 3 reflection), `tradeoff` + `failure` (Beat 4 commit), Answer 5 (Beat 4 closing *what does Alex need now*), plus structured: lenses tried, user-added patterns, three positionality coordinates, design context, slider settings, and computed dot position. (This differs slightly from the original capture table further down, which listed a Beat-2 self-added-pattern name as Answer 2; the build instead captures the added pattern as structured data.)

---

## Purpose, in one sentence

Help learners see that the four perspectives in learning science (Behaviorist, Cognitive, Situated/Distributed, Socio-cultural) work as **different lenses on the same situation**, each foregrounding what the others treat as background — and use that awareness to design and evaluate learning experiences with deliberate balance for context.

---

## Learning outcomes

### Primary LO *(Evaluate + Create)*

The learner will be able to **evaluate** any learning experience by reading it through four perspectives — Behaviorist, Cognitive, Situated/Distributed, and Socio-cultural — and **design** more deliberately by choosing which perspectives to foreground for a given learner and context, recognizing that no single design pattern (ITS, CoP, lecture, microworld, etc.) is universally correct.

### Sub-LOs (mapped to beats)

1. **Analyze — Lens-switcher beat.** Given one learning situation, the learner can produce four distinct readings (one per perspective), identifying what each lens foregrounds and what it treats as noise.

2. **Analyze + Apply + Create — Catalogue + generate beat.** The learner can locate common design patterns (ITS, CoP, lecture, microworld, apprenticeship, MOOC, hackerspace, peer-review study group, ~9 total) on the four-perspective map, add at least one pattern from personal experience, and explain where patterns cluster, where the map is sparse, and why.

3. **Evaluate — Mapping / positionality beat.** The learner can locate their own design instincts on the same map, and articulate where their default perspective shapes what they notice and what they miss.

4. **Apply + Create + Evaluate — Design-bench beat.** Given a specific learner and context, the learner can propose a design move that consciously balances at least two perspectives, name the trade-off they accepted, and predict what failure mode the un-foregrounded perspectives would flag.

### Through-line (metacognitive)

The learner will be able to **articulate** that observations and design judgments are never theory-neutral: the perspective doing the observing or designing co-constructs what counts as a problem, a strength, a success, or a failure.

---

## The four perspectives at a glance

Wording drawn directly from `POVs of learning science.pdf` and Hari's lecture slide.

| Perspective | Where learning lives | What counts as evidence | Designer's question | Failure mode |
|---|---|---|---|---|
| **Behaviorist** | The individual; in observable behavior | Performance on decomposed skill tasks; mastery | "What skills must they demonstrate, and to what level?" | Treats meaning, identity, context as noise; can train compliance without understanding |
| **Cognitive** | Inside the individual mind; in mental structure | Inferred from CTA, problem-solving traces, cognitive models | "What schemas need to form? Which prerequisites are missing?" | Abstracts the learner from social/cultural context |
| **Situated / Distributed** *(Pea)* | Across the system: learner + tools + peers + activity | Participation, intellectual practice, tool fluency, transfer | "What practice are they joining? Who and what are they thinking with?" | Without scaffolding, novices flounder — "lofty without directionality" |
| **Socio-cultural** | In cultural communities; in identity repertoires | Participation in cultural practices; whose knowledge counts as knowledge | "Whose objective is this? What does mastery mean here, for whom?" | Can become critique without proposing anything to build |

These are not competing claims about facts. They are different commitments about *what learning is for* and *what success looks like*. The explorable's whole job is to let the learner feel that — and use it.

---

## Architecture: five beats

A short cold open, four interactive beats, capture throughout.

| # | Beat | Purpose | Capture |
|---|---|---|---|
| 0 | **Cold open** | Ground the framework in one specific learner before vocabulary lands | Answer 1 (free text) |
| 1 | **Lens-switcher** | Wait-what — same situation, four readings | Lens-trying behavior |
| 2 | **Catalogue + generate** | Named design patterns as landmarks; learner adds their own | Self-added pattern, placement |
| 3 | **Mapping / positionality** | Place yourself on the map | Three personal coordinates + observation |
| 4 | **Design-bench + reflection** | Use what you've seen — design a system, name the trade-off | Slider state, trade-off, predicted failure, Answer 2 |

Beats 2 and 3 share a canvas (the 2D map); only the overlay prompts differ. That keeps the felt structure at four.

---

## Beat 0 — Cold open

**Purpose.** Ground the abstraction in one specific person before any vocabulary lands.

**Scenario.** One short, simple, ambiguous moment with one learner. ~100 words, plain prose. *Resolved (as built):* a fresh case — **Alex**, six weeks into learning to code, stuck for an hour on a loop exercise (moving a small robot through a grid), in a course built around a community Alex hasn't used. Two more cases (Maya; Devi, an adult at a music jam) are selectable in Beat 1.

**On screen.**
- The scenario
- One open question: *"What do they need right now?"*
- Free text field + continue

**Capture.** Answer 1.

---

## Beat 1 — Lens-switcher *(the wait-what)*

**Purpose.** Demonstrate that four perspectives read the same situation differently. Let the learner feel the difference, not be told it.

### Scene composition

The Beat 0 scenario is now rendered as a small interactive scene with discrete clickable elements:

- The **learner** (figure)
- The **tool/system** they're using (app, worksheet, instrument, IDE)
- The **surrounding people** (peers, teacher offstage, family)
- A **recent observable behavior** (Maya drew in the margin / the violinist played the same bar 12 times)
- A **recent inferred state** (paused, confused, focused, frustrated)
- The **cultural setting** (school, home, online community)

Each element holds annotations that change based on the active lens.

### The lens UX

**Recommendation: Cursor-as-lens with subtle canvas-tint shifts on switch.**

A toolbar at the bottom or side holds four lens icons. The learner picks one up (click or drag); the cursor becomes that lens icon. As they hover over scene elements, lens-specific annotations appear in-place. The active lens also drives a permanent sidebar (the *global* reading of the scene) and a quiet palette tint across the canvas (the *feel* of being inside this lens).

**Why this combination:**

- *Cursor-as-lens* makes the lens an embodied object the learner wields, not a passive button. Direct manipulation, low cognitive overhead, high agency.
- *Subtle canvas tint* does the work that full-canvas re-renders would do, without the build cost of four full re-renders. The whole world tilts a little when you switch.
- *Permanent sidebar* ensures the learner doesn't miss the global reading by failing to hover — accessibility + completeness.

### Alternatives considered

| Option | Strength | Why not primary |
|---|---|---|
| **Flashlight** (drag a spotlight) | Strong "hidden in plain sight" metaphor | Dimming everything else is visually heavy; the metaphor subtly conflicts with the message (lenses *change what counts*, not *reveal what's dark*) |
| **Full canvas re-render** | Maximum wait-what; each lens commits to its grammar | 4× the build effort; risks losing the "same situation" recognition |
| **Side-by-side comparison** | Direct comparison | Doesn't scale to four; each lens gets too small |
| **Layered overlay (toggle multiple)** | Shows perspectives can combine | Visual noise; loses the punch of single-lens commitment |

### Per-lens treatment

| Lens | Cursor icon | Palette tint | Annotation style | What gets foregrounded |
|---|---|---|---|---|
| **Behaviorist** | Reticle / crosshair | Cool grey-blue (cf. M3 dashboard) | Clinical sans, data badges | Observable behaviors, attempts, time, mastery threshold |
| **Cognitive** | Magnifying glass / brain-bubble | Soft pastel violet | Thought-bubble shapes, schema diagrams | Mental network, prereqs, sense-making failures, conceptual leaps |
| **Situated / Distributed** | Web / constellation | Warm earth green/tan (cf. M8 tree) | Connection lines, glow on tools and peers | Activity-in-progress, tools-in-play, who's nearby, what's offstage |
| **Socio-cultural** | Kaleidoscope / overlapping circles | Deeper warm purple-red | Marginal labels, "whose?" questions | Cultural framings, contested objectives, identity repertoires |

### Sidebar contents (per active lens)

- **Foregrounded:** which elements are bright; which are faded
- **What this lens sees:** 2–3 bullets
- **What this lens treats as noise:** 2–3 bullets
- **What this lens would recommend:** 1 sentence
- **What this lens cannot see:** 1 sentence

### Required interaction

The learner must try at least 2 lenses before continuing. Soft nudge (the *continue* button stays slightly dim until 2 lenses tried), not a hard gate.

### Touch and keyboard fallback

- **Touch:** tap a lens to equip; tap a scene element to reveal annotation; sidebar updates.
- **Keyboard:** `1/2/3/4` to swap lenses; tab through elements; enter to reveal.

### Capture

- Which lenses were tried; time per lens; which elements were inspected per lens.

---

## Beat 2 — Catalogue + generate *(map landmarks + add your own)*

**Purpose.** Show that named design patterns occupy particular regions of the 4-perspective map. Let the learner add patterns from their own life — turning the catalogue from something consumed into something co-constructed.

### The canvas

A 2D map drawn from the POVs PDF's axes:

- **X-axis — Unit of learning:** *individual* ↔ *system / collective*
- **Y-axis — Kind of evidence:** *observable performance* ↔ *inferred meaning / identity*

The four perspectives are placed as soft cloud-shaped regions (matching the visual register of Hari's lecture slide):

| Quadrant | Perspective |
|---|---|
| Bottom-left (Individual + Observable) | **Behaviorist** |
| Top-left (Individual + Inferred meaning) | **Cognitive** |
| Bottom-right (Collective + Observable) | **Situated / Distributed** |
| Top-right (Collective + Inferred meaning) | **Socio-cultural** |

### Pre-pinned design patterns (medium-thick, ~9)

Chosen to populate the map *unevenly* on purpose — clustering in two corners, conspicuous gap in the bottom-right, a few brave ones in the middle. The unevenness IS the finding.

| Pattern | Approximate placement |
|---|---|
| Intelligent tutoring system (ITS) | Upper-left |
| Khanmigo / AI chat tutor | Upper-left, slightly right |
| One-on-one human tutor (Bloom 1984) | Upper-left |
| Traditional lecture | Lower-left |
| Mastery-based microworld (PhET, ncase) | Upper-left/center |
| Apprenticeship | Lower-right |
| Community of practice (Discord study group) | Center-right / upper-right |
| Family kitchen-table / land-based learning | Upper-right |
| Peer-review workshop / book club | Upper-right, slightly left |

### Interaction

1. **Inspect:** hover/click each pinned pattern → small card pops with its profile across the four lenses (what it foregrounds, what it misses, predictable failure mode).
2. **Add your own:** "Add one of your own from your life." Modal:
   - Name *("the YouTube rabbit hole," "my undergrad lab," "the bouldering gym")*
   - One-line description
   - Drag-to-place on the map
   - Quick 4-lens check: which lenses does this pattern foreground? *(checkboxes)*
   - What would the un-foregrounded lenses say is missing? *(one short text field)*
3. The learner's additions persist through the session.
4. *(Optional, requires IRB conversation)* pooled additions across players become a collective constellation — feeds Stat 292 directly.

### Capture

- Self-added pattern(s): name, description, placement (x,y), lens-foregrounding selections, what's-missing text.

---

## Beat 3 — Mapping / positionality *(place yourself)*

**Purpose.** Personalize the map. Where does the learner instinctively design or evaluate from?

**Shared canvas with Beat 2.** Same 2D map; only the overlay prompts change. (Catalogue patterns can stay visible as faint pinned dots in the background, or be hidden for focus — to test.)

### Prompts (sequential, light)

1. *"Where on the map do you instinctively design or evaluate learning from?"* — drag a personal marker.
2. *"Where did you learn best, in your own life?"* — drag a second marker.
3. *"Where is your current work or practice?"* — drag a third marker.
4. The three markers are revealed together. One short prompt: *"What do you notice about your three points?"* (free text)

### Capture

- Three coordinates + the free-text observation (Answer 3 for Stat 292).

---

## Beat 4 — Design-bench + reflection *(use what you've seen)*

**Purpose.** Apply. Have the learner deliberately design a system by manipulating variables, observe where it lands, read what the four lenses say.

### Context picker

*"Design for:"*

- A 10-year-old learning fractions
- A junior developer learning to debug
- An adult learning a language as a hobby
- A grad student learning research methods
- *(Custom: free-text context, capped at ~50 chars)*

### Variables (sliders)

Each slider's range is suggestive, not absolute. All produce live changes to the dot on the map.

| Variable | Low end | High end |
|---|---|---|
| **Directionality** | Emergent | Prescribed pathway |
| **Scaffolding for novices** | Throw them in | Explicit task decomposition |
| **Group structure** | Solo | Large community (discrete: solo, 1:1, small group, large) |
| **Tool reliance** | Human-only | AI/system-driven |
| **Cultural specificity** | Universal "right answer" | Situated / intersectional |

### Live output

- A dot slides across the 2D map as sliders change.
- When the dot nears a named pattern, that pattern's card briefly highlights *("you're approaching ITS territory")*.
- Each of the four lenses shows a one-line reading of the current configuration: what it foregrounds, what it would flag.

### Commit move

After the learner settles on a configuration:

- *"Lock your design."*
- *"Name the trade-off you accepted."* (short text)
- *"Predict what failure mode the un-foregrounded perspectives will flag."* (short text)

### Closing reflection

> At the start, when you read about [the cold-open scenario], you wrote:
> *[Answer 1]*
>
> Knowing what you know now, what do they need?

Free text → Answer 5 (closing distal).

### Capture

- Slider settings, final dot coordinates, named trade-off, predicted failure mode, Answer 5.

---

## Data capture (for Stat 292)

Five free-text answers per consenting player:

| # | Source | Prompt | Distality |
|---|---|---|---|
| 1 | Beat 0 | "What do they need right now?" | Most distal (pre-frame) |
| 2 | Beat 2 | Self-added design pattern name + description | Meta-vocabulary |
| 3 | Beat 3 | "What do you notice about your three points?" | Proximal / personal |
| 4 | Beat 4 | Named trade-off + predicted failure mode | Proximal / applied |
| 5 | Beat 4 | "What do they need now?" | Closing distal (post-frame) |

Plus structured:

- Coarse profession category (optional)
- Lenses tried in Beat 1 + time per lens
- Pinned-pattern interactions in Beat 2
- Added-pattern placement + lens selections
- Three personal map coordinates from Beat 3
- All slider settings + dot position from Beat 4

### Consent + IRB

Consent flow on first screen, optional, skippable. IRB exemption arranged with EDUC 432 / Stat 292 course staff before any public release.

---

## Voice and visual direction

### Voice

Window, not stage. Plain serif body, small system-ui sans for labels and captions. No em dashes. No performed lyricism. Definitions of perspectives appear in-place as lens readings, not as upfront didactic prose.

### Palette

Warm paper-and-pencil base (carrying forward the Maya piece's foundation), with each lens having a quiet color signature so switching feels like the world tilts:

- Behaviorist: clinical grey-blue (echo of M3 cold dashboard)
- Cognitive: soft pastel violet
- Situated / Distributed: warm earth green/tan (echo of M8 tree)
- Socio-cultural: deeper warm purple-red

### Type

- Body: Georgia / serif
- Labels: system-ui sans, `letter-spacing: 0.14em`, uppercase
- Questions: large and calm, never bold

### Motion

Slow, ease-out, settle softly. No snap except where lens-switching reveals an annotation.

### Sound *(optional final pass)*

Quiet ambient under the lens-switcher; brief click on each lens equip; near-silence in cold open and reflection.

---

## Build milestones

Roughest-to-finest, matching the discipline of the earlier Maya handoff doc.

### M0 — Spine gray-box *(the go/no-go)*

- All five beats wired with placeholder text and minimal styling
- Lens-switcher as four buttons that just change the sidebar text (no cursor magic yet)
- 2D map as a static SVG with placeholder dots
- Design-bench sliders that capture state (don't yet drive a dot)
- All five captures wired to an in-memory state object
- Cold-open answer recalls in the closing reflection
- **Done when:** you can play start-to-finish, your two answers appear back-to-back, and you can test the structure on people before any art lands.

### M1 — Lens UX

- Cursor-as-lens with custom SVG icons; per-element annotations on hover; sidebar transformation; subtle palette tint per lens
- Touch and keyboard fallbacks
- **Done when:** a player who has never seen the script can switch lenses and feel that each one is doing different work.

### M2 — Map: pinned patterns + add-your-own

- 9 pre-pinned patterns with profile cards
- Add-your-own modal with drag-to-place
- Three positionality markers (Beat 3) on the same canvas
- **Done when:** a tester places one of their own and explains where they put it without prompting.

### M3 — Design-bench

- Sliders live-drive the dot on the map
- Live lens-readings update with slider state
- Pattern-proximity highlights
- Commit-trade-off capture
- **Done when:** dialing the sliders produces visibly distinct system positions and the four lens-readings shift meaningfully.

### M4 — Polish, sound, accessibility, IRB

- Color contrast pass (WCAG AA — Week 8)
- Text descriptions for screen readers; keyboard nav verified
- Sound (Week 7-style ambient + click)
- IRB exemption confirmation; consent flow tested
- **Done when:** a player on a phone with a screen reader can complete it; sound feels intentional, not decorative.

---

## Guardrails (easy to break — do not violate)

1. **No "right" lens.** The piece is not arguing that any one perspective is superior. Every design pattern is presented as a deliberate emphasis with its own integrity and predictable failure mode.
2. **No upfront definitions.** Perspectives reveal themselves *through* their lens readings, not through textbook intros.
3. **Don't punish the un-balancer.** A player who locks in a "pure ITS" design still gets a respectful lens read of their choice. The point is awareness of trade-offs, not a moral judgment.
4. **The catalogue is not exhaustive.** Pre-pinned patterns are conspicuously unevenly distributed; the learner-added patterns are part of the catalogue, not a footnote.
5. **The metacognitive through-line stays implicit.** The piece should not say "every observation is theory-laden." It should let the player notice that on their own through the lens-switcher.

---

## What this explorable is NOT

- Not a critique of ITS or a championing of CoP.
- Not a quiz; no "right" answer.
- Not a textbook; no upfront didactic prose.
- Not a personality test; the positionality beat is reflective, not categorical.

---

## Open decisions

1. **Cold-open case** — *Resolved (as built):* fresh case (Alex), with Maya and Devi also selectable in Beat 1.
2. **Pooling added patterns across players** — *Still open.* Not built yet; depends on the IRB conversation.
3. **Lens cursor visuals** — *Resolved (as built):* custom SVG cursors per lens.
4. **Whether the probe-v1 LO animation appears as a Beat 0 prelude.** *Still deferred* per current scope.
5. **Catalogue placement during Beat 3** — *Resolved (as built):* kept faintly visible (opacity ~0.18) for continuity.

---

## Companion files

- `POVs of learning science.pdf` — perspective definitions (course wording)
- `schools of thought.md` — author's own synthesis of the four schools and convergence points
- `maya-explorable-script.md` + `maya-build-handoff.md` — earlier iteration, useful for voice rules and palette
- `EDUC 432 Explorables lecture slides/` — design dimensions, Bloom's verbs, exemplars
- `probes/probe-v1.html` — earlier Beat 2 journey animation (currently deferred)

---

*End of outline. Window, not stage.*
