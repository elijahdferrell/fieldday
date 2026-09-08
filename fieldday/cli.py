"""CLI entry for FieldDay — organize messy lawn-job titles into a day plan."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

from fieldday.planner import MissingAPIKeyError, plan_jobs


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Organize messy lawn-job titles into a clean day plan."
    )
    parser.add_argument(
        "jobs_file",
        nargs="?",
        default="jobs.txt",
        help="Path to a text file with one job title per line (default: jobs.txt)",
    )
    args = parser.parse_args()

    path = Path(args.jobs_file)
    if not path.is_file():
        print(f"Error: jobs file not found: {path}", file=sys.stderr)
        sys.exit(1)

    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    jobs = [line for line in lines if line]

    if not jobs:
        print("Error: no jobs found in the file (empty or only blank lines).", file=sys.stderr)
        sys.exit(1)

    try:
        plan = plan_jobs(jobs)
    except MissingAPIKeyError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    print(plan)


if __name__ == "__main__":
    main()
