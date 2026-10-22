# Publication replay record

**NON-CANONICAL, candidate-C audit at L1.** Same-architecture reproduction
of the incoming result-exposed scripts, not a formal public probe gate.

## Environment and execution

- Operating system: Linux.
- Architecture: x86_64.
- Python: 3.13.5.
- SymPy: 1.14.0 (`verify.py` only; `trace_check.py` uses the standard library).
- Interpreter isolation: `python3 -I`, with an empty external working directory.
- Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
- Both complete scripts were inspected before execution.
- All scientific assertions use exact symbolic, rational or finite-field
  arithmetic; there is no floating tolerance or random sample.

## verify.py

Command: `python3 -I <note-directory>/verify.py`.
Exit code: 0; stderr: 0 bytes.
Stdout: 639 bytes, exactly equal to `EXPECTED.txt`.

- Script SHA-256: `b229c43c0906bdd735b75442b26e5a42aded027785e5bbbae8006988e367a630`.
- Stdout SHA-256: `d397d857f214603cbefe33d0bafae987be5ccf0ee867a5135417fc89978fe5db`.

## trace_check.py

Command: `python3 -I <note-directory>/trace_check.py`.
Exit code: 0; stderr: 0 bytes.
Stdout: 226 bytes, exactly equal to `TRACE-EXPECTED.txt`.

- Script SHA-256: `ba0c849d38501ab6ea9aabaa53f010404d0147c84d586db447d1c2c3473b9a1a`.
- Stdout SHA-256: `01bdfe059fffc197a62fa09eb2527630865c7220b7394ed5cd72dabcd8ddd649`.

The transfer program reports nine check groups. The separate trace program
checks all nine ordered pairs of the three basis vectors. These are not counts
of independent physical tests. Bilinearity extends the trace identity beyond
the basis; the finite output is an audit of that written reasoning.

No new scientific script is executed by notes-only repository CI. Its required
two-architecture repository checks do not constitute a two-architecture replay
of this mathematics. The packet certifier and full first-order verifier were
not run. No external blind breaker, physical experiment, formal probe pin,
canonical promotion, source-branch merge or public release is claimed.
