#!/usr/bin/env python3
"""Summarize DORA delivery metrics per service (D9-Q2 cross-check).

D9-Q2 asks whether lead time, deployment frequency, change failure rate
and time to restore are tracked and compared before and after AI
adoption [2], [3], [5]. This script reads a CSV or JSON export with one
row per service and period:

    service, period, deployment_frequency, lead_time_hours,
    change_failure_rate, time_to_restore_hours

``period`` is ``baseline`` (before AI adoption) or ``current``. A
service counts as measured when its current row has the four metrics,
and as compared when its baseline row has them too.

With --services (the number of services in scope), the share of
compared services gives the level the evidence supports for D9-Q2,
using the section 4 coverage bands. Without it, the report shows the
counts and does not cap the answer. The script uses no benchmark
thresholds: it checks measurement coverage, not delivery performance.

Writes output/dora-metrics.json. The v2 reports compare it with D9-Q2
when the file is present.

Usage:
    python3 scripts/import_dora_metrics.py metrics.csv [more.json]
        [--services N] [--out output]
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = ("deployment_frequency", "lead_time_hours",
           "change_failure_rate", "time_to_restore_hours")
PERIODS = ("baseline", "current")


def read_rows(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8-sig").strip()
    if not text:
        return []
    if path.suffix.lower() == ".csv":
        return list(csv.DictReader(text.splitlines()))
    data = json.loads(text)
    if isinstance(data, dict):
        data = data.get("rows") or data.get("services") or []
    return [r for r in data if isinstance(r, dict)]


def to_number(value) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(str(value).strip().replace(",", "."))
    except ValueError:
        return None


def collect(rows: list[dict]) -> dict:
    """Service -> period -> metric values (later rows win)."""
    services: dict = {}
    for row in rows:
        name = str(row.get("service") or "").strip()
        period = str(row.get("period") or "").strip().lower()
        if not name or period not in PERIODS:
            continue
        values = {m: to_number(row.get(m)) for m in METRICS}
        services.setdefault(name, {})[period] = values
    return services


def complete(values: dict | None) -> bool:
    if not values:
        return False
    return all(values.get(m) is not None for m in METRICS)


def medians(services: dict, period: str) -> dict:
    out = {}
    for metric in METRICS:
        vals = [s[period][metric] for s in services.values()
                if complete(s.get(period))]
        out[metric] = round(statistics.median(vals), 3) if vals else None
    return out


def summarize(services: dict, total: int | None) -> dict:
    measured = [n for n, s in services.items()
                if complete(s.get("current"))]
    compared = [n for n in measured
                if complete(services[n].get("baseline"))]
    if total is not None:
        total = max(total, len(services))

    def share(count: int) -> float | None:
        return round(count / total, 3) if total else None

    return {
        "services_total": total,
        "services_listed": len(services),
        "services_measured": len(measured),
        "services_compared": len(compared),
        "shares": {"measured": share(len(measured)),
                   "compared": share(len(compared))},
        "medians": {p: medians(services, p) for p in PERIODS},
        "services": [{"service": n, **{p: services[n].get(p)
                                       for p in PERIODS}}
                     for n in sorted(services)],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", help="CSV or JSON exports")
    ap.add_argument("--services", type=int,
                    help="number of services in scope")
    ap.add_argument("--out", default=str(ROOT / "output"))
    args = ap.parse_args()
    if args.services is not None and args.services < 1:
        print("✗ --services must be 1 or more.", file=sys.stderr)
        return 1
    rows = []
    for name in args.files:
        rows += read_rows(Path(name))
    services = collect(rows)
    if not services:
        print("✗ No DORA metrics rows found (need service and period "
              "columns).", file=sys.stderr)
        return 1
    summary = summarize(services, args.services)
    result = {
        "metadata": {
            "generated_at": datetime.datetime.now(
                datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_files": [Path(f).name for f in args.files],
            "rows": len(rows),
            "reference": "DORA delivery metrics [2], [3], [5]",
            "script": "scripts/import_dora_metrics.py",
        },
        **summary,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "dora-metrics.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"✓ {out / 'dora-metrics.json'}: "
          f"{summary['services_measured']} measured, "
          f"{summary['services_compared']} compared, "
          f"total {summary['services_total'] or 'not given'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
