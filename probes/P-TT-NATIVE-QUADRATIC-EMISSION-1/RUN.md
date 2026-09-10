# P-TT-NATIVE-QUADRATIC-EMISSION-1 local run record

Date: 2026-09-10

Status: local formal exact run, one architecture. This record does not by
itself satisfy the public two-architecture computation gate and changes no
Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: a8e35e95d8adb891a28233779f2547a2441d70f1
verifier_sha256: 0834461e61788dd9221f90af8769fbdc74e80005fc11b19486843ecbe49e0416
command: python3 probes/P-TT-NATIVE-QUADRATIC-EMISSION-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: e66a90283d718825c0aa3190cf4c7f955b1cab709dd602cac20c4f89b40e18ac
stdout_bytes: 558
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e464b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: e5e75500ab88cf0e2a9e877e3134d85b832411baf2bb546a25a062cd881a5eb3
PREREG bytes:  9651
PREREG blob:   c830c92de61f263a9817d94ab1f9be98a8e9e1a5
verify sha256: 0834461e61788dd9221f90af8769fbdc74e80005fc11b19486843ecbe49e0416
verify bytes:  17707
verify blob:   73b267205a03f6582af8b2d3993cea43110c6fb4
EXPECTED sha256: e66a90283d718825c0aa3190cf4c7f955b1cab709dd602cac20c4f89b40e18ac
EXPECTED bytes:  558
```

`PREREG.md` was pushed first. The accepted `verify.py` was then pushed at the
pin commit above. Before the first formal execution, the public branch ref was
read back at exactly the pin commit and both public files were read back from
that ref. Only static inspection and Python bytecode compilation occurred
before the pin.

The execution environment was

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The execution environment available to this session could not make an outbound
DNS clone of GitHub. The first formal invocation therefore executed the exact
pinned verifier bytes after public connector readback rather than from a fresh
network clone. A second invocation placed the same pinned files at the exact
repository-relative path in a materialized repository-root layout and used the
canonical command printed above. The two x86_64 invocations had byte-identical
stdout and empty captured stderr. This second invocation is same-architecture
reproduction only, not independent confirmation and not the public gate.

The pull-request workflow performs the required clean GitHub checkouts and
replays the unchanged verifier on x86_64 and aarch64. Those jobs, not the local
materialization, decide the repository computation gate.

## Accepted local result

```text
TM4_LANGUAGE 10 FACTORS PASS
TM4_MASSES 0110=1/6 1001=1/6 OTHER8=1/12 PASS
ORIENTATION_OVERLAPS u0=w2-w0 u1=w3-w1 PASS
QUADRATIC_SOURCE_CLASS O2+REFLECTION+TIME_SWAP NULLITY=1 PASS
EMISSION Phi=b1^2-b0^2=H1-H0 KAPPA_ABS=1 PASS
K1_PACKETS STATIC=4 ACTIVE=6 CLASSES={1: 4, 0: 4, 2: 2} PASS
ZERO_START h0=h1=0 h2=Phi UNIQUE_RECURRENCE PASS
LOCAL_WORK_AND_CONSTRAINTS exact symbolic + rational fixtures PASS
SPIN_TYPES c(1)=0 c(2)=-3 PASS
NO_NEW_DIMENSIONLESS_SOURCE_COEFFICIENT PASS
EXACT_ASSERTIONS 2010
RESULT PASS; TT-SOURCE STATUS NOT CHANGED BY THIS PROBE
```

The assertion count is the number of exact `require` calls. Several calls
compare complete rational vectors or coefficient systems and are not counts of
independent theorems. Universal claims are carried by `PROOF.md`; the verifier
is an exact audit of their frozen algebraic and finite surfaces.
