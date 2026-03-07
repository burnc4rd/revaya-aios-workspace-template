# Image Prompt Guide

> Reference for writing AI image prompts for [YOUR_NAME]'s content.
> Read this whenever a post or concept needs an image — LinkedIn posts, YouTube thumbnails, or carousel headers.
> Last updated: 2026-03-03

---

## When to Use This Guide

- [YOUR_NAME] asks for an image prompt to take to an image generator herself
- `/draft-post` Step 6: generating or prompting a post image
- `/develop` Stage 2: developing YouTube thumbnail concepts into ready-to-use prompts
- Any time the request is "write me a Midjourney/Ideogram/DALL-E prompt for this"

---

## Platform Specs

| Use Case | Dimensions | Notes |
|----------|-----------|-------|
| LinkedIn post image | 1200 × 628 px (1.91:1) | Landscape. Keep subject centered — LinkedIn crops on mobile. |
| LinkedIn square image | 1080 × 1080 px (1:1) | Square shows better on mobile feed. |
| YouTube thumbnail | 1280 × 720 px (16:9) | Bold. Large text. Face visible and expressive (if using). |
| LinkedIn carousel (cover) | 1080 × 1080 px | Square. First card is the hook — make it count. |
| YouTube Shorts thumbnail | 1080 × 1920 px (9:16) | Vertical. Shorts now shows thumbnails — subject top-centered, text readable at small size. |
| TikTok cover frame | 1080 × 1920 px (9:16) | Vertical. TikTok shows first frame as cover — design within center 1080×1350 "safe zone" to avoid UI cropping. |

---

## [YOUR_NAME]'s Brand Style Notes

**Tone:** Professional but warm. Not corporate, not casual — founder energy.
**Colors:** No strong brand palette yet — lean into neutrals, deep blues/teals, warm whites. Avoid generic stock-photo pastels.
**Face:** [YOUR_NAME]'s face in images = higher engagement. When prompting realistic scenes, note "professional, approachable, mid-40s woman" or plan to swap in a real photo.
**Text in images:** Limit to 4–6 words max. Should COMPLEMENT the post headline (different information, not a repeat).
**Avoid:** Stock-photo clichés (handshakes, laptops in coffee shops, pointing at whiteboards). Generic "business professional" vibes.

---

## Generator: Ideogram (Recommended for thumbnails + text-in-image)

**Best for:** YouTube thumbnails, LinkedIn images with text overlays, carousel covers, graphics with bold typography
**Access:** ideogram.ai — free tier available
**Why:** Text rendering is dramatically better than other generators. Use when the image needs readable words.

### Prompt Structure

```
[Subject / scene description], [mood/lighting], [style], [color palette], --ar [ratio] --v 2
```

### Text-in-Image Syntax (Ideogram-specific)

Wrap text in quotes within the prompt:

```
"YOUR TEXT HERE" [rest of description]
```

### LinkedIn Post Image — No Text

```
[What the image represents], clean composition, professional, [mood], soft natural lighting,
editorial photography style, warm neutral tones, [specific visual detail], 16:9 ratio
```

**Example (for a post about AI overwhelm):**
```
Person sitting at desk surrounded by glowing screens and notification bubbles,
thoughtful expression, overwhelmed but composed, cinematic lighting, editorial photography style,
muted blue and warm amber tones, 16:9 ratio
```

### LinkedIn Post Image — With Text Overlay

```
Clean background with [scene element], [color], minimalist composition,
"YOUR 4-6 WORD TEXT" in bold white sans-serif, lower-thirds placement, 16:9 ratio
```

**Example:**
```
Deep navy blue gradient background with subtle circuit pattern texture,
"MOST AI PROJECTS FAIL HERE" in bold white sans-serif, centered bottom-third,
professional, modern design, 16:9 ratio
```

### YouTube Thumbnail

```
[Subject — person or scene], expressive [emotion] face, bold "TEXT OVERLAY" in [color] sans-serif,
high contrast, bright colors, dramatic lighting, YouTube thumbnail style, 16:9 ratio
```

**Example:**
```
Professional woman, wide-eyed curious expression, bold "I WAS WRONG" in yellow sans-serif top right,
clean blue background, high contrast, dramatic lighting, YouTube thumbnail style, 16:9 ratio
```

---

## Generator: DALL-E / ChatGPT (Good backup, fast, no text)

**Best for:** Conceptual imagery, scene-setting, abstract ideas — when you don't need text in the image
**Access:** ChatGPT Plus (Image generation tab) or API
**Limitation:** Text rendering is poor — don't ask DALL-E to add words to an image

### Prompt Structure

DALL-E responds well to descriptive, natural language. Skip the parameter syntax.

```
[Scene description]. [Mood and atmosphere]. [Style]. [Color palette].
[What NOT to include]. Photorealistic / Illustration / etc.
```

### LinkedIn Post — Photorealistic

```
[Specific scene that represents the post's core idea]. Professional but warm lighting.
Editorial photography aesthetic. [Color mood]. Clean composition, no clutter.
No text overlays. No stock photo clichés.
```

**Example:**
```
A small business owner reviews workflow diagrams pinned to a wall, looking focused and in control.
Modern home office. Warm morning light. Editorial photography aesthetic. Muted tones with pops of blue.
Clean composition. No text overlays. Not a generic stock photo.
```

### LinkedIn Post — Conceptual/Abstract

```
Abstract visual metaphor for [concept]. [Style — geometric, painterly, minimal].
[Colors]. Professional and modern. Suitable for a LinkedIn article header.
No text, no people, no clichés.
```

**Example (for "automation"):**
```
Abstract representation of interconnected nodes and automated workflows.
Clean geometric illustration style. Deep teal and warm gold palette.
Professional and modern. No text, no robots, no generic gears.
```

---

## Generator: Midjourney (Highest quality — use when you want premium imagery)

**Best for:** High-quality brand photography style, editorial portraits, premium visual aesthetics
**Access:** Discord — /imagine command. Requires paid subscription (~$10/month basic).
**Note:** Best quality generator but requires Discord. Worth it for hero images and premium content.

### Prompt Structure

```
/imagine [description], [style keywords], [camera/lens], [lighting], [color grade], --ar 16:9 --v 6.1 --style raw
```

### LinkedIn Editorial Portrait Style

```
/imagine professional woman, founder energy, thoughtful expression, [scene context],
natural window light, editorial portrait photography, shot on Sony A7IV, 85mm lens,
warm neutral tones, not stock photo, --ar 3:2 --v 6.1 --style raw
```

### YouTube Thumbnail (Midjourney)

```
/imagine [person or scene], expressive reaction face, [emotion],
bold graphic design composition, high contrast, vivid colors,
YouTube thumbnail aesthetic, --ar 16:9 --v 6.1
```

### Brand Scene / Concept

```
/imagine [scene description], cinematic, editorial photography, professional but warm,
[specific color palette], shallow depth of field, 35mm lens, --ar 16:9 --v 6.1 --style raw
```

---

## Prompt Writing Process

When asked to write an image prompt:

1. **Identify the generator** — Ideogram (default), DALL-E, or Midjourney
2. **Identify the use case** — LinkedIn post, YouTube thumbnail, carousel cover
3. **Extract the core visual idea** from the post hook or concept title
4. **Decide: face or no face** — human presence increases engagement; abstract works for concept posts
5. **Decide: text in image or not** — if yes, use Ideogram. Draft 4-6 word text overlay.
6. **Write the prompt** using the framework above
7. **Present:** formatted prompt ready to copy-paste, plus a one-line note on what the visual achieves

### Quick Reference — What Image Type Fits What Post?

| Post Type | Image Approach |
|-----------|---------------|
| Transformation/story post | Human scene, emotional, Ideogram or Midjourney |
| Operational problem post | Relatable scene (overwhelm, fire-fighting), or text-on-color |
| Framework/list post | Text overlay with key phrase, minimal background (Ideogram) |
| YouTube thumbnail | Bold, face-forward, text overlay — Ideogram first |
| Lead magnet promo | Clean product mockup or "free resource" graphic — Ideogram |
| Personal journey | Portrait-style or scene — Midjourney for quality |

---

## Vertical Thumbnails (YouTube Shorts + TikTok Cover)

Shorts and TikTok use 9:16 vertical format. Design rules are different — the subject must be top-centered, text in the middle or lower third.

### Ideogram — Shorts/TikTok Thumbnail

```
Vertical portrait composition, [subject centered top third],
[expression — match the hook emotion],
"TEXT OVERLAY" in bold [color] sans-serif [placement: center or lower third],
clean [color] background, high contrast, YouTube Shorts style, 9:16 ratio
```

**Example:**
```
Vertical portrait composition, professional woman looking directly at camera,
curious raised-eyebrow expression, top-centered framing,
"WRONG TOOL" in bold yellow sans-serif center placement,
clean dark blue background, high contrast, YouTube Shorts style, 9:16 ratio
```

### TikTok Cover Frame (from Ideogram)

```
Vertical composition, [subject in center safe zone],
[emotional expression matching hook], minimal background,
"HOOK TEXT" in large bold white sans-serif,
safe zone: keep all content within center 80% of height, 9:16 ratio
```

**Key difference from Shorts:** TikTok crops the top and bottom slightly — keep subject and text within the center 80% of the vertical frame.

---

## Output Format When Asked for a Prompt

```
**Image Prompt: [Generator Name]**

[paste-ready prompt]

**What this achieves:** [1 sentence — why this visual serves the post/concept]
**Specs:** [dimensions or ratio to use]
**Tip:** [any generator-specific note, e.g., "click V2 on the grid for variations"]
```
