"""Sync Airtable Content Pipeline → published_content SQLite table.

Pulls all records with Status = "Posted" from the Airtable Content Pipeline
and upserts them into data/content.db published_content table. This feeds
the 7-day context aggregator so /develop always has current post history.

Run manually or add to a daily schedule.

Usage:
    python scripts/content/sync_airtable.py              # Sync all Posted records
    python scripts/content/sync_airtable.py --dry-run    # Show what would sync, don't write
"""

import json
import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))

from dotenv import load_dotenv
load_dotenv(WORKSPACE_ROOT / ".env")

AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN", "")
BASE_ID = "YOUR_AIRTABLE_BASE_ID"
TABLE_ID = "tblBOkOJLYRfM0q53"

# Field IDs from Airtable
FIELD_MAP = {
    "Name":              "fldOaedSiYq5t5TdM",  # Post title/hook (text)
    "Status":            "fldXXXXXXXXXXXXXX",  # We filter by this
    "Publish Date":      "fldYYYYYYYYYYYYYY",  # YYYY-MM-DD
    "Platform":          "fldZZZZZZZZZZZZZZ",  # LinkedIn, YouTube, etc.
    "Post Body":         "fld111111111111",      # Post content (for description)
    "Impressions":       "fld222222222222",
    "Reactions":         "fld333333333333",
    "Comments":          "fld444444444444",
    "Saves":             "fld555555555555",
    "Total Engagement":  "fld666666666666",
    "Engagement Rate %": "fld777777777777",
}

# We'll pull all fields by name dynamically — more reliable than hardcoding IDs
AIRTABLE_API_URL = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"


def fetch_posted_records() -> list[dict]:
    """Fetch all records where Status = 'Posted' from Airtable."""
    try:
        import urllib.request
        import urllib.parse
    except ImportError:
        print("Error: urllib not available")
        return []

    if not AIRTABLE_TOKEN:
        print("Error: AIRTABLE_TOKEN not found in .env")
        return []

    records = []
    offset = None

    while True:
        params = {
            "filterByFormula": "{Status} = 'Posted'",
            "pageSize": "100",
        }
        if offset:
            params["offset"] = offset

        url = AIRTABLE_API_URL + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {AIRTABLE_TOKEN}"},
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            print(f"Error fetching from Airtable: {e}")
            return records

        records.extend(data.get("records", []))
        offset = data.get("offset")
        if not offset:
            break

    return records


def _parse_record(record: dict) -> dict | None:
    """Parse an Airtable record into a published_content row dict."""
    fields = record.get("fields", {})
    airtable_id = record.get("id", "")

    # Title (Name field — usually the hook/first line)
    title = fields.get("Name", "").strip()
    if not title:
        return None

    # Published date
    pub_date = fields.get("Publish Date", "")
    if isinstance(pub_date, str) and "T" in pub_date:
        pub_date = pub_date[:10]  # strip time if present
    if not pub_date:
        # Try to extract from record creation date
        created = record.get("createdTime", "")
        pub_date = created[:10] if created else "2026-01-01"

    # Platform
    platform_raw = fields.get("Platform", "")
    if isinstance(platform_raw, list):
        platform = platform_raw[0].lower() if platform_raw else "linkedin"
    else:
        platform = str(platform_raw).lower() if platform_raw else "linkedin"
    if not platform:
        platform = "linkedin"

    # Description (Post Body — truncated)
    description = fields.get("Post Body", "") or ""
    if len(description) > 500:
        description = description[:500] + "..."

    # Metrics
    metrics = {}
    for key in ["Impressions", "Member Reach", "Reactions", "Comments", "Saves",
                "Total Engagement", "Engagement Rate %", "Profile Visits"]:
        val = fields.get(key)
        if val is not None:
            metrics[key.lower().replace(" ", "_").replace("%", "pct")] = val

    return {
        "platform": platform,
        "external_id": airtable_id,
        "title": title,
        "published_date": pub_date,
        "url": None,
        "description": description or None,
        "metrics": metrics if metrics else None,
    }


def sync(dry_run: bool = False) -> None:
    """Sync Airtable Posted records into published_content table."""
    from scripts.content.db import get_connection, init_db
    from scripts.content.writer import log_published_content

    print("Fetching Posted records from Airtable...")
    records = fetch_posted_records()
    print(f"Found {len(records)} posted records")

    if not records:
        print("Nothing to sync.")
        return

    if dry_run:
        for r in records:
            parsed = _parse_record(r)
            if parsed:
                print(f"  Would sync: {parsed['published_date']} | {parsed['platform']} | {parsed['title'][:60]}")
        return

    # Init DB if needed
    conn = init_db()

    # Get existing external_ids to avoid duplicates
    existing = set(
        row[0]
        for row in conn.execute(
            "SELECT external_id FROM published_content WHERE external_id IS NOT NULL"
        ).fetchall()
    )

    inserted = 0
    skipped = 0
    for record in records:
        parsed = _parse_record(record)
        if not parsed:
            skipped += 1
            continue

        if parsed["external_id"] in existing:
            skipped += 1
            continue

        log_published_content(conn, parsed)
        inserted += 1

    conn.close()
    print(f"Sync complete: {inserted} inserted, {skipped} skipped (already synced or no title)")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    sync(dry_run=dry_run)
