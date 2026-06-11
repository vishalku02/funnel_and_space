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
- **Kicker form:** concentric fish-eye warp vs. side-by-side panels vs.
  continuous scroll-driven zoom.
- **Cascade drive:** scroll-driven (each scroll beat widens) vs. button/click.
- **Art (now informative):** the cascade needs four nested crops of the *same*
  moment (act → person → table → world), each *annotated* to show what that lens
  foregrounds (label the empty chair, the untouched tiles). Current `camp-*.jpg`
  images are separate scenes, not nested annotated crops — need new art.
- **How hard to pivot from hook to exposition:** how fast we leave the narrative
  open and name "four ways to look at this one moment" (the jump-to-maps move).
- **Product sort:** give it a payoff (reveal the field clusters at the zoomed-in
  rings) or cut it.
- **First-person turn** ("my learning at different levels") — save for the end as
  the reader applies the zoom to their own world?
