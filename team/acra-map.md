# ACRA+2 Department Map

> Historical reference: maps the original 27-role functional org to ACRA+2 departments.
> The ACRA+2 structure is now the live org (team/ directory). The functional org is archived at reference/legacy-team-org/.

---

## What ACRA+2 Is

ACRA+2 is the department structure of the Execution Layer. It organizes work by customer lifecycle dimension:

| Department | Mission | Analogy |
|-----------|---------|---------|
| **Attract** | Bring the right people in | Traffic department |
| **Convert** | Turn attention into buyers | Revenue department |
| **Retain & Deliver** | Keep members engaged and getting results | Fulfillment department |
| **Ascend** | Move members up the value ladder | Ascension department |
| **Finance** | Track performance and translate data into signals | Numbers department |
| **AI HR** | Build, document, and optimize the AI agent workforce | Team management department |

The +2 are Finance and AI HR — support functions that power all four ACRA dimensions.

---

## Role Mapping

Roles often serve multiple departments. The "Primary" column shows where a role spends most of its execution energy. "Secondary" shows where it also contributes.

### Attract (Traffic Department)

**Mission:** Bring ideal clients into the Revaya ecosystem through content, YouTube, and strategic social media.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| CMO | Strategy + oversight | Channel strategy, content calendar, ICP definition |
| Content Strategist | Content planning | Topic ideation, pillar mapping, calendar management |
| Copywriter | Written content | LinkedIn posts, hooks, blog posts (attract angle) |
| SEO Specialist | Search discoverability | Keyword strategy, blog optimization, YouTube SEO |
| Social Media Manager | Platform execution | Post publishing, community engagement, DM responses |
| Social Media Designer | Visual content | Graphics, carousels, thumbnails |
| Lead Magnet Designer | Asset creation | Lead magnet design, landing page assets |
| Research Analyst | Intelligence | VOC research, Reddit insights, competitive intel |
| YouTube Long-Form platform | Video content | Long-form video production pipeline |
| YouTube Shorts platform | Short video | Repurposed clips from long-form |
| TikTok platform | Short video | Cross-posted from Shorts |
| LinkedIn platform | Professional social | Primary written content channel |

**Starter Pipeline (v1):**
Attract Orchestrator → Content Strategist (topic selection) → Copywriter (draft) → Social Media Designer (visual) → Social Media Manager (publish) → Research Analyst (performance analysis)

---

### Convert (Revenue Department)

**Mission:** Turn attention into signed clients through copywriting, offer design, and sales sequences.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| CRO | Strategy + oversight | Conversion strategy, funnel optimization |
| Account Executive | Sales execution | Discovery calls, proposals, close |
| SDR | Outreach | Prospecting, first contact, qualification |
| Sales Enablement | Sales infrastructure | Proposals, scripts, objection handling docs |
| Copywriter | Sales copy | Sales page, email sequences, VSL scripts (convert angle) |
| Creative Director | Conversion assets | Sales page design, proposal presentation |

**Starter Pipeline (v1):**
Convert Orchestrator → SDR (prospect + qualify) → Account Executive (discovery + proposal) → Copywriter (sales materials) → Account Executive (close) → CRO (analyze and optimize)

---

### Retain & Deliver (Fulfillment Department)

**Mission:** Deliver the work. Delivery is retention. Keep clients engaged and getting results.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| COO | Ops oversight | Workflow design, capacity planning |
| AI Consultant | Delivery | AIOS builds, client sessions, recommendations |
| Project Manager | Coordination | Project tracking, milestone management, client comms |
| Account Manager | Relationship | Ongoing client check-ins, satisfaction, renewals |
| Website Developer | Technical delivery | Website builds (InfluencerOS, Dale, Darko, etc.) |
| QA Engineer | Quality | Testing, review, pre-launch checks |

**Starter Pipeline (v1):**
COO Orchestrator → Project Manager (kickoff + plan) → AI Consultant or Website Developer (execute) → QA Engineer (review) → Account Manager (deliver + check in) → Project Manager (close + offboard)

---

### Ascend (Ascension Department)

**Mission:** Move existing clients and community members up the value ladder through upgrade offers and deeper engagement.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| CRO | Ascension strategy | Upsell timing, upgrade offer design |
| Account Executive | Upgrade conversations | Identifying and pitching upsells |
| Account Manager | Relationship intel | Flags clients ready to ascend |
| CMO | Nurture content | Content that keeps engaged clients moving toward next offer |

**Starter Pipeline (v1):**
CRO Orchestrator → Account Manager (flag ascension candidates) → Account Executive (upsell conversation) → Copywriter (upgrade offer materials) → CRO (track and optimize)

---

### Finance (Numbers Department)

**Mission:** Track business performance, KPIs, and financial health. Translate data into strategic signals. Feed Metrics and Monitoring.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| CFO | Financial strategy | Financial health, pricing decisions, investment calls |
| Finance Analyst | Data tracking | Revenue tracking, KPI dashboards, expense monitoring |
| Data Analyst | Analysis | Performance analysis, trend identification, anomaly detection |

**Data feeds:**
- Finance Analyst → updates `metrics/business-kpis.md` weekly
- Data Analyst → queries `data/intel.db`, Airtable for performance analysis
- Both → surface signals to CFO for strategic decisions and to Learning Loops

**Starter Pipeline (v1):**
CFO Orchestrator → Finance Analyst (weekly data pull + KPI update) → Data Analyst (trend analysis) → CFO (strategic interpretation) → Learning Loops (signals for reflection)

---

### AI HR (Team Management Department)

**Mission:** Build, document, and optimize the AI agent workforce. Keep the AI workforce running at peak performance. See `team/ai-hr-protocol.md` for full responsibilities.

| Role | Primary Function | Pipeline Contribution |
|------|----------------|----------------------|
| CTO | AI HR lead | AI agent strategy, system architecture decisions |
| AI Engineer | Implementation | Agent creation, skill building, MCP integrations, subagent pipelines |

**Note:** AI Engineer also contributes to all four ACRA departments by building the pipelines those departments run on.

**Starter Pipeline (v1):**
CTO Orchestrator → AI Engineer (build or update agent) → CTO (review and approve) → AI HR Protocol (document in subagent KB)

---

## Cross-Department Roles

These roles appear in multiple ACRA dimensions by design:

| Role | Departments | Why |
|------|-------------|-----|
| Copywriter | Attract, Convert | Writes both content (attract) and sales materials (convert) |
| Account Executive | Convert, Ascend | Closes new clients and upsells existing ones |
| Account Manager | Retain & Deliver, Ascend | Manages relationships and flags ascension opportunities |
| CMO | Attract, Ascend | Drives both inbound content and nurture for existing clients |
| CRO | Convert, Ascend | Optimizes both first-sale and upsell conversion |
| Research Analyst | Attract (primarily) | Cross-commissioned by any team |
| AI Engineer | AI HR + all departments | Builds the pipelines all departments run on |

---

## Using This Map

**When routing work:**
- Content creation → Attract department
- Sales or proposal work → Convert department
- Client delivery or website builds → Retain & Deliver
- Upsell conversations → Ascend department
- Revenue tracking or KPI updates → Finance department
- Building new agents or updating role files → AI HR department

**In `/build-guide`:**
Today's focus task should be attributed to one primary ACRA department. This tells you which team is "on the field" today.

**In `/review` AIOS Weekly Synthesis:**
Check which ACRA departments were active this week and which were idle. Idle = gap or appropriate? Investigate before accepting idle as fine.
