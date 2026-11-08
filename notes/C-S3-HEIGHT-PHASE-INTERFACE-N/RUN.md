# First bounded search receipt

NON-CANONICAL / L1. Experiment S3-EIGHT-SLOT-BFS-1.
Prospective public source pin:7406c1468bd344b6aac311099097a64ff970ff22.
All six source files were fetched through the public repository API at this
pin and compared byte-for-byte and by Git blob with the clean local checkout
before the first scientific execution. No frozen source changed.

Command from repository root:
```text
python notes/C-S3-HEIGHT-PHASE-INTERFACE-N/search.py
```

Environment: Windows11 build10.0.26300, architecturex86_64 (AMD64),
Python3.12.10, assertions enabled, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1, LC_ALL=C,LANG=C,TZ=UTC.
Operational subprocess timeout120seconds.
Start2026-11-08T11:15:00.961362+00:00.
Measured elapsed approximately0.640seconds.
Exit0; stderr0bytes; no timeout.
Scientific executions at this pin:1; no retry, amended source or discarded run.

search.py:7110bytes, SHA256
04a1cc8a90a5f5cc18c6c80bcf71b475b01e9a734ef455cd0574bdcb77638f4c.
Exact stdout EXPECTED.txt:449bytes, one ASCII JSON line with LF, SHA256
b7dcf988c9a6bbcdc900e0fd60f6f8c8c7e8f3720316e118441d276d91c4378a.
Captured stdout bytes were copied directly; no newline normalization.

Result INCONCLUSIVE / DEPTH_CAP.
Visited12853 distinct five-state tuples, maximum discovered depth6.
Fully expanded3290 nodes;9563 depth-six nodes remained unexpanded.
Generated92120 common contact transitions, including66022 identity
transitions and13246 already-seen successors.
Scalar decisions:81890 admissions and378710 refusals across five inputs.
These are search counters, not per-cut invariant assertions.
No candidate was found, so the found-word replay and inverse-audit branch
was NOT exercised. Root invariant assertions did execute.
The searched node order has SHA256
0158b2b9e1ba6398b1ea19f6c6e54233854d9436fac55395c5ea5d943c6be3a1.

Because every node of depth<6 was fully expanded and all newly discovered
depth-six nodes were goal-tested, this run found no common word of length
at most6 in this exact eight-slot contact-only class. Deduplication preserves
shortest reachability. The protocol still classifies the overall search as
INCONCLUSIVE: longer paths and other stocks were not decided.

Only one architecture ran. Same-session source review and this replay do
not constitute independent scientific acceptance or a formal public gate.
