# P-CARRY-ARITY-CIRCUIT-1 formal run record

pin_commit: 4234d5ef9e9720aa29b355a9aef15b0e529f59f9
base_commit: 4d8558356f2f945b34e9f7fece323771d266585a
prereg_sha256: d36f804b1a397d7bb5291ad48cbc9ba046f6bdaf27824e08bd8288d06c6e4ebf
verifier_sha256: 8c77db1e149c56c06452b7267ac0ab1e59e3c15a4d8ee29d8f597c8c31874073
command: python3 probes/P-CARRY-ARITY-CIRCUIT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Linux
architecture: x86_64
python: 3.13.5
clean_checkout: yes
architecture_gate: local x86_64 leg complete; required GitHub x86_64 and aarch64 byte-identical jobs pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 1f751aa0ce1773a218862eb47d6973884f9079fba9891d92778844207ceae329
stdout_bytes: 378
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
public_lock: issue 314

The executed verifier was byte-checked against the immutable pin before the
run. A separate notebook-wrapper preflight was excluded from evidence because
that wrapper injected unrelated Python-startup instrumentation into stderr;
the pinned verifier itself was unchanged. The formal shell execution recorded
above used the frozen neutral environment and produced empty stderr.
