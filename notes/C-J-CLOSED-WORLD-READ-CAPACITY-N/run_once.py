#!/usr/bin/env python3
"""Administrative first-run capture, with exclusive output creation.

Run from the repository root. Does not import either scientific program.
Elapsed time and platform metadata do not enter any scientific decision.
"""
import datetime
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

def main():
    script, prefix = map(Path, sys.argv[1:])
    prefix.parent.mkdir(parents=True, exist_ok=True)
    paths = [Path(str(prefix) + suffix) for suffix in (".stdout", ".stderr", ".json")]
    if any(path.exists() for path in paths):
        raise SystemExit("STOP: first-run record already exists")
    record = {
        "script": str(script), "cwd": str(Path.cwd()),
        "command": [sys.executable, "-u", str(script)],
        "python": sys.version, "platform": platform.platform(),
        "architecture": platform.machine(), "timeout_seconds": 2400,
        "environment": {"PYTHONHASHSEED": "0", "LC_ALL": "C"},
        "start_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    env = os.environ.copy()
    env.update(record["environment"])
    started = time.monotonic_ns()
    with paths[0].open("xb") as out, paths[1].open("xb") as err:
        try:
            run = subprocess.run(record["command"], env=env, stdout=out,
                                 stderr=err, timeout=2400, check=False)
            record.update(exit_code=run.returncode, timed_out=False)
        except subprocess.TimeoutExpired:
            record.update(exit_code=None, timed_out=True)
    record["elapsed_ns"] = time.monotonic_ns() - started
    record["end_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with paths[2].open("x") as handle:
        json.dump(record, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(record, sort_keys=True))
    return 124 if record["timed_out"] else record["exit_code"]

if __name__ == "__main__":
    raise SystemExit(main())
