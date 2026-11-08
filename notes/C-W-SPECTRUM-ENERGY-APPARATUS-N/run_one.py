#!/usr/bin/env python3
"""Retain one immutable first audit attempt; never overwrite a run."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import platform
import subprocess
import sys


def now():
    return datetime.now(timezone.utc).isoformat()


root = Path(__file__).resolve().parent
choice = sys.argv[1]
scripts = {'primary': 'verify.py',
           'independent': 'agents/sources_review/verify_independent.py'}
rel = scripts[choice]
freeze = json.loads((root/'SOURCE_FREEZE.json').read_text())
expected = {r['path']: r['sha256'] for r in freeze['files']}
source = root/rel
digest = sha256(source.read_bytes()).hexdigest()
assert digest == expected[rel], 'source differs from pre-run freeze'
run = root/'runs'/choice
run.mkdir(parents=True, exist_ok=False)
command = [sys.executable, str(source), str(run/'certificate.json')]
record = {'implementation': choice, 'source': rel, 'source_sha256': digest,
          'runner_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'command': command, 'started_at_utc': now(), 'state': 'started',
          'python': sys.version, 'platform': platform.platform(),
          'machine': platform.machine()}
record_path = run/'attempt.json'
record_path.write_text(json.dumps(record, indent=2)+'\n')
with (run/'stdout.txt').open('wb') as stdout, (run/'stderr.txt').open('wb') as stderr:
    try:
        proc = subprocess.run(command, cwd=root, stdout=stdout, stderr=stderr,
                              timeout=60, check=False)
        record.update(returncode=proc.returncode, state='completed')
    except subprocess.TimeoutExpired:
        record.update(returncode=None, state='timeout')
record['finished_at_utc'] = now()
if (run/'certificate.json').exists():
    data=(run/'certificate.json').read_bytes()
    record.update(certificate_sha256=sha256(data).hexdigest(),
                  certificate_bytes=len(data))
record_path.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record))
sys.exit(0 if record['returncode'] == 0 else 1)
