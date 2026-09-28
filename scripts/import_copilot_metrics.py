#!/usr/bin/env python3
"""Summarize a Copilot usage metrics export (D4 and D9 cross-check).

Section 8 of the v2 spec recommends comparing the D4 and D9 answers with
telemetry before presenting results. This script reads the reports of
the GitHub Copilot usage metrics API or its NDJSON export [6]:

- 28-day aggregate reports (enterprise-28-day, organization-28-day),
  which wrap daily records in ``day_totals``
- 1-day aggregate reports (enterprise-1-day, organization-1-day)
- per-user reports (*-users-1-day, *-users-28-day), one record per user

It keeps the latest day and reports active users and the AI adoption
phases (No Cohort, Phase 1 "Code first", Phase 2 "Agent first",
Phase 3 "Multi-agent"). Licensed seats are not part of these reports;
pass them with --seats or --seats-file (the response of the Copilot
user management API, which has ``total_seats``).

Writes saida/telemetria.json. The v2 reports compare it with D4-Q1 and
D9-Q1 when the file is present.

Usage:
    python3 scripts/import_copilot_metrics.py report.json [more.ndjson]
        [--seats N | --seats-file seats.json] [--out saida]
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASES = ("No Cohort", "Phase 1", "Phase 2", "Phase 3")
ACTIVE_KEYS = {
    "daily": "daily_active_users",
    "weekly": "weekly_active_users",
    "monthly": "monthly_active_users",
    "monthly_agent": "monthly_active_agent_users",
    "monthly_chat": "monthly_active_chat_users",
}


def read_records(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = [json.loads(line) for line in text.splitlines()
                if line.strip()]
    items = data if isinstance(data, list) else [data]
    out = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if isinstance(item.get("day_totals"), list):
            out += [d for d in item["day_totals"] if isinstance(d, dict)]
        else:
            out.append(item)
    return out


def phase_name(entry: dict) -> str | None:
    name = str(entry.get("phase") or "").strip()
    for phase in PHASES:
        if name.lower().startswith(phase.lower()):
            return phase
    number = entry.get("phase_number")
    if isinstance(number, int) and 0 <= number < len(PHASES):
        return PHASES[number]
    return None


def summarize(records: list[dict], seats: int | None) -> dict:
    aggregates = [r for r in records if "user_login" not in r
                  and "user_id" not in r and r.get("day")]
    users = [r for r in records if "user_login" in r or "user_id" in r]
    latest = max(aggregates, key=lambda r: r["day"]) if aggregates else None
    phases = {p: 0 for p in PHASES}
    active = {k: None for k in ACTIVE_KEYS}
    day = None
    if latest:
        day = latest["day"]
        for key, field in ACTIVE_KEYS.items():
            active[key] = latest.get(field)
        for entry in latest.get("totals_by_ai_adoption_phase") or []:
            name = phase_name(entry)
            if name:
                value = entry.get("users_in_phase_28d",
                                  entry.get("total_engaged_users"))
                phases[name] += int(value or 0)
    elif users:
        days = [u.get("day") for u in users if u.get("day")]
        day = max(days) if days else None
        latest_users = [u for u in users if u.get("day") == day] or users
        for u in latest_users:
            name = phase_name(u.get("ai_adoption_phase") or {})
            if name:
                phases[name] += 1
    population = sum(phases.values())

    def share(n: int) -> float | None:
        return round(n / population, 3) if population else None

    code = phases["Phase 1"] + phases["Phase 2"] + phases["Phase 3"]
    agent = phases["Phase 2"] + phases["Phase 3"]
    monthly = active["monthly"]
    return {
        "report_day": day,
        "active_users": active,
        "seats": seats,
        "phases": phases,
        "population": population,
        "shares": {
            "code_first_or_higher": share(code),
            "agent_first_or_higher": share(agent),
            "multi_agent": share(phases["Phase 3"]),
            "monthly_active_of_seats": round(monthly / seats, 3)
            if monthly is not None and seats else None,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", help="JSON or NDJSON reports")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--seats", type=int, help="licensed Copilot seats")
    group.add_argument("--seats-file", help="Copilot seats API response")
    ap.add_argument("--out", default=str(ROOT / "saida"))
    args = ap.parse_args()
    records = []
    for name in args.files:
        records += read_records(Path(name))
    seats = args.seats
    if args.seats_file:
        seats = json.loads(Path(args.seats_file).read_text(
            encoding="utf-8")).get("total_seats")
    summary = summarize(records, seats)
    if not summary["population"] and summary["active_users"]["monthly"] \
            is None:
        print("✗ No Copilot usage metrics records found.", file=sys.stderr)
        return 1
    result = {
        "metadata": {
            "generated_at": datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_files": [Path(f).name for f in args.files],
            "records": len(records),
            "reference": "GitHub Copilot usage metrics [6]",
            "script": "scripts/import_copilot_metrics.py",
        },
        **summary,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "telemetria.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"✓ {out / 'telemetria.json'}: day {summary['report_day']}, "
          f"phases {summary['phases']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
