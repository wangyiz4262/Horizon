"""Skip a run when today's Horizon briefing has already been delivered.

The workflow declares a primary schedule slot plus a catch-up slot, because
GitHub's ``schedule`` event is best-effort: slots are regularly delayed by
hours and can be dropped entirely. This guard makes the redundant slots safe to
keep. A run exits early when another run of this workflow already delivered
(``conclusion == "success"``) or is still in flight for the current UTC day.

A manual ``workflow_dispatch`` run bypasses the check with ``force: true``.

The guard fails open: if the runs API cannot be queried, the run proceeds, so a
delivery is never lost to an API hiccup.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any, Iterable

WORKFLOW_PATH = ".github/workflows/daily-summary.yml"
API_ROOT = "https://api.github.com"
IN_FLIGHT = {"queued", "in_progress", "waiting", "requested", "pending"}


def decide(runs: Iterable[dict[str, Any]], run_id: str, force: bool) -> tuple[bool, str]:
    """Return (skip, reason) for the current run."""
    if force:
        return False, "force input set on manual dispatch"

    for run in runs:
        if str(run.get("id")) == str(run_id):
            continue
        if run.get("path") != WORKFLOW_PATH:
            continue
        status = run.get("status")
        if status in IN_FLIGHT:
            return True, f"run {run.get('run_number')} is still {status}"
        if run.get("conclusion") == "success":
            return True, f"run {run.get('run_number')} already succeeded today"

    return False, "no run has delivered today"


def fetch_runs_today(repo: str, token: str, today: str) -> list[dict[str, Any]]:
    """Fetch every workflow run created on ``today`` (UTC) for ``repo``."""
    runs: list[dict[str, Any]] = []
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "Horizon-Delivery-Guard/1.0",
    }
    for page in range(1, 6):
        url = f"{API_ROOT}/repos/{repo}/actions/runs?created={today}&per_page=100&page={page}"
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            batch = json.loads(response.read().decode("utf-8")).get("workflow_runs", [])
        runs.extend(batch)
        if len(batch) < 100:
            break
    return runs


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    force = (os.environ.get("FORCE") or "").strip().lower() in {"true", "1", "yes"}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if not repo or not token:
        skip, reason = False, "GITHUB_REPOSITORY/GITHUB_TOKEN unavailable; proceeding"
    else:
        try:
            skip, reason = decide(fetch_runs_today(repo, token, today), run_id, force)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError) as exc:
            skip, reason = False, f"guard query failed ({exc}); proceeding"

    print(f"Delivery guard: date={today} skip={skip} ({reason})")

    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"skip={'true' if skip else 'false'}\n")
    else:
        print("GITHUB_OUTPUT not set; skipping output write.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
