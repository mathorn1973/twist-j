# P-TT-NATIVE-QUADRATIC-EMISSION-1 local run record

Date: 2026-09-10

Status: accepted local formal exact run, one architecture. This record does not
by itself satisfy the public two-architecture computation gate and changes no
Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: a8e35e95d8adb891a28233779f2547a2441d70f1
verifier_sha256: 3e05906a2113305ae21de00c5eb306a139e913d0d6f7d6a12369feb5fbaab692
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
verify sha256: 3e05906a2113305ae21de00c5eb306a139e913d0d6f7d6a12369feb5fbaab692
verify bytes:  17699
verify blob:   6f838218ad880cda5e98839da0d20f8f2f1398ac
EXPECTED sha256: e66a90283d718825c0aa3190cf4c7f955b1cab709dd602cac20c4f89b40e18ac
EXPECTED bytes:  558
```

`PREREG.md` was pushed first. The accepted `verify.py` was then pushed at the
pin commit above. Only static inspection and Python bytecode compilation
occurred before that pin.

## Custody correction retained

The first local execution attempted after the public pin used a local draft
whose SHA-256 was

    0834461e61788dd9221f90af8769fbdc74e80005fc11b19486843ecbe49e0416

and whose byte count was 17707. The public pinned blob was instead 17699 bytes
with Git blob

    6f838218ad880cda5e98839da0d20f8f2f1398ac.

The difference was exactly eight unused source bytes: the local draft assigned
`freq4 = tm_factor_theorem()` while the public pin calls
`tm_factor_theorem()` directly. The returned value is not used. The attempted
local draft run is therefore excluded from the formal evidence record even
though it produced the same stdout. The pinned verifier was not edited,
resumed, amended or repinned.

The exact public pinned bytes were then reconstructed from the public blob
readback and independently checked against both its public Git blob identifier
and public byte count. Their SHA-256 is the value recorded in the machine
fields above. Those exact bytes were placed at the repository-relative probe
path in a materialized repository-root layout and executed with the canonical
command above.

The accepted execution environment was

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
TERM=dumb
```

The accepted exact-pinned execution exited zero, captured empty stderr, and
matched `EXPECTED.txt` byte for byte. A direct execution of the same exact
pinned blob also produced the same stdout. Both are one x86_64 environment and
therefore only same-architecture reproduction.

The session environment could not make an outbound DNS clone of GitHub. No
fresh-local-clone claim is made. The pull-request workflow performs the
required clean GitHub checkouts and replays the unchanged public verifier on
x86_64 and aarch64. Those jobs decide the repository computation gate.

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
