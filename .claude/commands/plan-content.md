# Plan Content

> Social media manager agent. Generates or updates the rolling multi-platform content calendar.
> Balances pillar ratios, IFP/ICP split, and platform cadence across a full month.

## Variables

request: $ARGUMENTS (optional — e.g., "April 2026", "next 2 weeks LinkedIn only", or leave blank for next full month)

---

## Instructions

You are generating or updating your content calendar. Read strategy and existing calendar before generating anything.

### Step 1: Load context

Read:
- `context/content-engine/content-strategy.md` — pillars, ratios, platform cadence, audience split
- `context/content-engine/calendar.md` — what's already planned or posted (do not duplicate)

Check `outputs/content-engine/research/` for any recent research briefs (last 30 days). If relevant briefs exist, use their content angles to populate post slots.

### Step 2: Determine scope

If a specific month or timeframe was provided, generate for that period.
If no scope provided, generate the next full month (4 weeks from today).

### Step 3: Generate the calendar

Apply the 4-3-2-1 framework:

**4 posts/week on LinkedIn:**
| Day | Post Type | Pillar |
|-----|-----------|--------|
| Monday | Operational Problem | Pain-first, ICP-leaning |
| Wednesday | Lived Experience | Authority, Expert-Led |
| Thursday | Practical Value | Framework or how-to |
| Saturday | Personal Journey or Lead Magnet | Growth/TAM, IFP-leaning |

(If starting at 3x/week: Mon, Wed, Sat)

**Pillar balance targets across the month:**
- Operational Problems: 40%
- Lived Experience: 30%
- Practical Value: 20%
- Personal Journey: 10%

**Audience split:**
- 60% IFP posts (reach, broad, relatable)
- 40% ICP posts (conversion, specific pain, discovery call direction)

**Other platforms (add when relevant):**
- YouTube: 1x/week if in active production phase
- TikTok/Shorts: 3-5x/week from YouTube clips
- Blog: 1-2x/month from YouTube scripts

**Lead magnet slot:**
- Once a lead magnet exists: flag one Saturday post per month as the lead magnet promo post
- Mark with [LEAD MAGNET PROMO] in the calendar

### Step 4: Output the calendar

Format as a table:

```
| Date | Day | Platform | Content Type | Pillar | Theme | Angle / Topic | Target | Status |
```

Include one-line rationale for each post slot explaining why that angle fits that slot.

### Step 5: Update files

Update `context/content-engine/calendar.md` with the new month.
Save a copy to `outputs/content-engine/calendar/YYYY-MM.md`.

Report back:
1. The calendar table
2. Any post slots that need research before drafting (flag with [NEEDS RESEARCH])
3. Which post is the highest priority to draft first
