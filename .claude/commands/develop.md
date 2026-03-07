# /develop — Develop Content Concept

> Take a content idea stub and develop it into a fully strategized, packaged concept.

## Variables

$ARGUMENTS (the stub ID like "#5", or a raw idea to capture and develop in one go)

## Instructions

You are running the **Develop** step of the Content Pipeline. Take a captured idea and turn it into a fully developed content concept with strategic positioning, audience alignment, packaging, and offer mapping.

### Setup — Load Context

1. **Read the idea:**
   - If given an ID (#N): query `SELECT * FROM content_ideas WHERE id = N` via the content database
   - If given raw text: capture it as a stub first (classify channel + format), then develop

2. **Read content strategy docs** (ALWAYS read all of these):
   - `content/strategy.md` — platform, cadence, pillars, audience split, competitive positioning
   - `content/brand-and-audience.md` — brand positioning, target audience segments, proof points
   - `content/offers-and-funnels.md` — offers, funnels, audience → offer alignment, CTAs
   - `content/packaging-strategy.md` — title/thumbnail/hook frameworks (used for both YouTube AND LinkedIn)

3. **Scan inspiration library** (check for relevant examples):
   - `content/inspiration/linkedin/` — LinkedIn post examples and hooks worth referencing
   - `content/inspiration/youtube/` — YouTube title/thumbnail examples
   - `content/inspiration/frameworks/` — posting frameworks and content systems

   If any examples match the concept's channel or topic, reference them in packaging ("This hook pattern is inspired by [source]"). Don't copy — adapt and make it yours.

4. **Build the 7-day context window:**
   ```bash
   .venv/bin/python3 -c "
   import sys; sys.path.insert(0, '.')
   from scripts.content.context_aggregator import build_context_window, format_context_for_prompt
   context = build_context_window(days=7)
   print(format_context_for_prompt(context))
   "
   ```
   Read the output — this tells you:
   - Recent published content (what's already been covered so you don't repeat it)
   - Recent meetings (themes, client pain points, insights worth referencing)
   - Current pipeline state (what's already queued)

---

### Stage 1: STRATEGIC POSITIONING (Present and confirm)

Using the idea + context window + strategy docs, develop the strategic frame:

1. **Audience alignment** — Which segment does this serve? What specific problem does it solve for them?
2. **Authority angle** — Why is you THE voice on this topic? (Reference brand positioning and proof points)
3. **Offer alignment** — Which offer does this drive toward? What's the CTA path? (Reference offers-and-funnels.md)
4. **Narrative fit** — How does this connect to what's been published recently? (Reference context window)
5. **Funnel position** — awareness / consideration / conversion
6. **Content pillar** — Which of the 4 pillars

**STOP. Present the strategic frame concisely. Ask: "Does this positioning feel right? Any angle changes?"**

---

### Stage 2: PACKAGING (Present and confirm)

The packaging stage adapts based on the channel for this idea.

#### For YouTube

Use the full packaging framework from `content/packaging-strategy.md`:

1. **Want vs. Need analysis** — What does the viewer WANT? What does the video actually give them (NEED)? How do we frame the NEED as the path to the WANT?
2. **3-5 title options** — Each using 2+ viral title elements from the packaging strategy. Include element tags (e.g., [curiosity + authority]).
3. **2-3 thumbnail concepts** — Each with:
   - Emotion (from the emotion mapping in packaging-strategy.md)
   - Text overlay (2-4 words, COMPLEMENTARY to title — different information)
   - Visual element (icon, screenshot, symbol)
   - Layout (face-left recommended)
   - **Image prompt** — Read `content/image-prompts.md` and write a ready-to-paste Ideogram prompt for this concept
4. **Complementarity check** — Confirm title and thumbnail provide different information
5. **Hook strategy** — How title + thumbnail + opening 30 seconds work together

#### For TikTok / YouTube Shorts (channel: tiktok_shorts)

Use the short-form packaging framework from `content/packaging-strategy.md` (Short-Form section):

1. **Hook trio** — The first 1-3 seconds are the packaging. Develop 2-3 options, each with:
   - **Spoken line** (what you say on camera — pattern interrupt, bold claim, direct address)
   - **On-screen text overlay** (3-6 words, DIFFERENT information than spoken line)
   - **Visual setup** (what the viewer sees — expression, scene, screen capture)
2. **Content arc** — Setup (0-10s) → Tension (10-30s) → Payoff (30-60s) → CTA (last 5s)
3. **Caption** — TikTok (1-3 lines + 3-5 hashtags + CTA) and Shorts (1 tight line)
4. **Source type** — Is this original, a LinkedIn repurpose, or a long-form clip?
5. **Thumbnail/cover frame** — For Shorts, suggest the best still frame or Ideogram prompt (9:16 vertical, read `content/image-prompts.md`)

Use the Short-Form Packaging Output Format from packaging-strategy.md.

#### For LinkedIn

Use the LinkedIn packaging approach (hooks are the equivalent of titles+thumbnails):

1. **3-5 hook lines** — The first 1-2 lines before "see more." Each should stop the scroll. Apply the same viral elements from packaging-strategy.md adapted for text.
2. **Visual concept** — What image, graphic, or carousel card accompanies the post? If an AI-generated image is appropriate, read `content/image-prompts.md` and include a ready-to-paste Ideogram prompt.
3. **Format recommendation** — Post, article, carousel, or short video. With reasoning.
4. **Authority signal stack** — Which of Proof / Competence / Clarity / Teachability does this hit? Must hit at least 2.

#### For All Channels

- Packaging must be **complementary** — visual and text provide different information
- **Want test:** Does this call out something the audience actively wants?
- **Scroll-stop test:** Would this make you stop scrolling?

**STOP. Present packaging options. Ask: "Which direction feels strongest? Any adjustments?"**

---

### Stage 3: STORE & FINALIZE

After the user confirms:

1. **Assign priority score (1-10):**
   - Strategic value (serves business goals, drives to active offer?)
   - Timeliness (news hook, trending topic?)
   - Demand signals (from context window — audience questions, meeting themes)
   - Production effort (format complexity, prep required)
   - Gap (not already covered recently)

2. **Write to database:**
   ```bash
   .venv/bin/python3 -c "
   import sys, json; sys.path.insert(0, '.')
   from scripts.content.db import get_connection
   from scripts.content.writer import write_developed_idea

   idea = {
       'id': EXISTING_ID_OR_NONE,
       'title': 'Selected primary title or hook',
       'hook': 'Opening hook / first line',
       'description': 'Full concept description',
       'audience': 'Target audience description',
       'format_type': 'FORMAT',
       'channel': 'CHANNEL',
       'topics': 'comma,separated,topics',
       'source_type': 'develop',
       'title_options': json.dumps([
           {'text': 'Title/Hook A', 'elements': ['curiosity', 'authority']},
           {'text': 'Title/Hook B', 'elements': ['list', 'timeliness']},
       ]),
       'thumbnail_concepts': json.dumps([
           {'emotion': 'confidence', 'text_overlay': '2-4 words', 'visual': 'description'},
       ]),
       'funnel_position': 'awareness',
       'content_pillar': 'PILLAR',
       'audience_segment': 'SEGMENT',
       'offer_alignment': 'OFFER',
       'cta_path': 'CTA description',
       'proof_points': json.dumps([
           {'type': 'performance', 'text': 'Specific proof point'},
       ]),
       'authority_angle': 'Why you own this topic',
       'production_status': 'developed',
       'priority_score': 8,
       'research_json': json.dumps({'context_window': '7d'}),
       'developed_by': 'develop',
   }

   conn = get_connection()
   idea_id = write_developed_idea(conn, idea)
   conn.close()
   print(f'Saved as concept #{idea_id}')
   "
   ```

3. **Write concept doc:**
   Save the full concept to `content/concepts/{id}-{slug}.md` with all positioning, packaging, and strategy details.

4. **Regenerate pipeline:**
   ```bash
   .venv/bin/python3 scripts/content/generate_pipeline.py
   ```

5. **Report:**
   - Saved as concept #ID
   - Concept doc written to `content/concepts/`
   - Primary title/hook + channel + format
   - Priority score
   - Next step by channel:
     - LinkedIn: "Ready to draft. Run `/draft-post #ID` to write the full post."
     - YouTube: "Ready to script. Run `/develop #ID script` to outline the script when ready."

---

### Critical Rules

- **Interactive** — Present strategic positioning, wait for confirmation. Present packaging, wait for confirmation. Never blast through all stages.
- **Context-first** — Always reference what the 7-day context window tells you. "You posted about X on Monday, so this piece should angle toward Y to avoid overlap."
- **Platform-appropriate** — LinkedIn hooks ≠ YouTube titles (though the psychology is the same). Apply the right format.
- **Complementary packaging** — Title/hook and visual must provide DIFFERENT information.
- **Want vs. Need** — Always frame content as what they WANT, deliver what they NEED.
- **CTA alignment** — Every piece of content should have a clear path to an offer, even if subtle.
- **your voice** — Direct, warm, grounded. Specific. No banned words.

$ARGUMENTS
