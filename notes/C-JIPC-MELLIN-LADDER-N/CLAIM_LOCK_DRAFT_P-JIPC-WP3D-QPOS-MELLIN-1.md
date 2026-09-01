# Claim-lock issue draft — NOT POSTED

Status: DRAFT / NOTES LANE / NON-CANONICAL. Prepared text of the
public claim-lock issue for the probe below, in the current house
form (cf. issue #731). Before posting, the maintainer (1) re-runs the
authority readback and fills `BASE_COMMIT` with the full SHA of
public `main` at lock time, (2) re-runs the collision scan and
updates the scan sentence and dispositions, (3) computes the final
`verify.py` SHA-256 and replaces the placeholder below, and (4) drops
this header.
Depositing this file claims nothing.

---

**Title:** `[PROBE CLAIM] P-JIPC-WP3D-QPOS-MELLIN-1: rational-slice Mellin package with public Beta-midpoint and Machin bridges`

## Authority readback

```text
STATE:          ACTIVE
CANON:          Public Canon v74
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v74
TAG_OBJECT:     796b09aef958a9021b93cff0df7f300ef95f5337
TAG_TARGET:     05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT: 2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:   2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:    389246
BASE_COMMIT:    <full SHA of public main at lock time>
```

The declared tag target and content commit are ancestors of current
public `main`; the normative Canon digest agrees with `STATUS.md`.
Public Canon v74 remains unchanged by this lane.

## Predecessor disposition and result exposure

There is no predecessor probe. The only public parent is the merged
probe `P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1` (claim issue #566,
PR #569, merge commit `9a4b479b0a7a9ce39772f77f16dd363602ec72c7`,
RESULT status candidate-T / L1 / Public Canon unchanged), consumed
for its frozen Machin-series Cauchy name `p_M = 16 A_5 - 4 A_239` and
its dressed seed tuples only; no WP3E theorem is a premise (the
well-definedness of `A_q` is re-proven inside the probe).

Internal JIPC artifacts (WP3B/WP3C/WP2 archives, private lineage
gate maps, `PI_ATAN_GAUSS_TYPED_IDENTITY`) and the notes-lane drafts
under `notes/C-JIPC-MELLIN-LADDER-N/` are discovery context at most:
not evidence, not premises, not edges of the proof graph. The bridge
source is `PUBLIC_SELF_CONTAINED` (Claim Q6 of the preregistration).

The owner has seen the internal rational-slice identities under the
historical label `QPOS_CORE_IDENTITIES = NO_COUNTEREXAMPLE_FOUND`.
This probe is therefore result-exposed, proof-first: the written
proofs Q1-Q8 carry every universal statement; the verifier is a
finite exact audit of a frozen bounded surface and has never been
executed (`DEV_EXECUTION = NONE`).

Collision search before this lock (2026-09-01, to be repeated at
lock time): no ref named `probe/P-JIPC-WP3D-QPOS-MELLIN-1` among the
remote heads; the only JIPC refs are
`probe/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1` and the two notes-lane
draft branches. Search for `WP3D` and `QPOS` returns the non-formal
notes lineage #571, #572 and #775 plus the closed WP3E parent claim
#566/PR #569; these are discovery deposits or the named parent, not
competing claim locks. `probes/` contains only WP3E in this family,
and no registry row, object lock, formal issue or claim lock names
this probe. The current state and disposition of every returned item
must be rewritten from a fresh search immediately before posting.

## Public claim lock

```text
probe:          P-JIPC-WP3D-QPOS-MELLIN-1
branch:         probe/P-JIPC-WP3D-QPOS-MELLIN-1
path:           probes/P-JIPC-WP3D-QPOS-MELLIN-1/
owner:          A. M. Thorn
layer:          L1 exact rational algebra and real analysis only
target:         rational-slice Mellin package on Q_{>0}: seed existence with
                algorithmic tail moduli, product identity, square-root-free
                duplication, public bridge C(1/2)^2 = p_I, public Machin
                bridge p_I = p_M, dressed slice Ehat*Ohat = Chat typed to p_M
mode:           result-exposed; written proof carries universal statements;
                verifier is audit
verify_sha256:  <SHA-256 of the final verify.py; the verifier bytes are final
                before this lock and do not change at the pin>
prereg_sha256:  recorded in a comment on this issue at pin time, after the
                locked authority tuple and BASE_COMMIT are copied into PREREG.md
```

No Canon, Registry, Frontier, dependency, gate, workflow, release or
existing-probe byte is changed by this probe.

## Frozen scientific scope

Q1. `C, B, E, O` exist on `Q_{>0}` with output-form modulus
    algorithms (`D_b(r) = 2^(-ceil(c(b+1+c)/a))`, schedules for
    `C, E, O, B`); scope of the modulus claim: bare seeds only.
Q2. `C(1) = 1`; `C(s+1) = s C(s)`; B-SPLIT, B-PARTS, B-REC; symmetry;
    `E(s) = (1/2) C(s/2)`; the join `O(s) = E(s+1)` (a proven node,
    never a definition).
Q3. `C(p) C(q) = C(p+q) B(p,q)` on `Q_{>0}^2` (compact square step
    for `p, q >= 1`, uniform tail, finite descent).
Q4. `B(p,p) = 2^(1-2p) B(1/2,p)` (rational-square cut substitution,
    two-step diagonal descent).
Q5. `C(p) C(p+1/2) = 2^(1-2p) C(1/2) C(2p)`, square-root-free.
Q6. Public bridge `C(1/2)^2 = p_I := 4 int_0^1 dt/(1+t^2)` via the
    Beta-midpoint route inside the primary graph.
Q7. Public Machin bridge `p_I = p_M` (`A(1/q) = A_q`, addition law
    by `C^1` substitution, three exact compositions).
Q8. Dressed slice `Ehat(s) Ohat(s) = Chat(s)` on `Q_{>0}` typed to
    `p_M`; `Ehat(1) = 1`, `Ohat(1) = Chat(1) = 1/p_M`.
Scale falsifier: three residual detectors at `lambda = 2`.

## Reading-family discipline (POLICY.md §4)

`NOT_APPLICABLE`: this probe proposes no family of physical readings,
no decoder, no selection and no occurrence clause. The only
uniqueness statements it asserts are mathematical and name their
class and equivalence explicitly:

1. the unique real common point of the nested alternating rational
   Machin intervals `hull(S_(q,N), S_(q,N+1))` — class: real numbers
   contained in every such hull; equivalence: equality in `R`;
2. the unique positive real `n`-th root of a positive real — class:
   positive reals `y` with `y^n = x`; equivalence: equality in `R`.

## Integrity requirements

The accepted `verify.py` is newly authored from the frozen statements
above and imports no predecessor code. Standard library only,
exactly one import (`from fractions import Fraction as Fr`), deterministic
exact arithmetic, no floating point anywhere (no `** 0.5`, no
`math.sqrt`, no float or complex literal), no `ast.Div` (integer `//`
and the `Fraction` constructor are the only quotients), no random,
network, file, subprocess, dynamic import, `eval` or `exec`. It reads
no file, argument, stdin, environment variable or clock, and writes
nothing but stdout. `EXPECTED.txt` is the only stdout artifact; no
transcript with a forbidden suffix will be requested (POLICY.md §7
allowlist is never invoked).

Preflight before the single formal execution (integrity check, not
a scientific gate):

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
required: exit 0; stdout exactly PYTHON_STARTUP_CLEAN plus LF; stderr empty
```

`RUN.md` records neutral public metadata only (operating system,
architecture, Python version); no machine nickname, hostname,
private address or fleet label.

## Firewalls

No effective holomorphic seeds (owned by WP3E), no identity beyond
the rational slice, no meromorphic continuation, no functional
equation, no Fourier or Poisson theory, no Gamma object, no circle
constant (Q7 identifies two internal Cauchy names of one constant;
no circular reading is introduced), no archimedean place, no WP2
obligation, no L2-L6 lift; SAMPLING NOT PROVIDED. The gate names of
the private JIPC lineage do not exist in Public Canon and none is
created.

## Decision rule

```text
CONFIRMED (candidate-T, L1)
    The written proofs Q1-Q8 close the universal clauses, the pinned
    verifier completes from its immutable pin with the frozen stdout
    (last line RESULT PASS), no frozen falsifier fires, and the
    x86_64/aarch64 workflow reproduces the same EXPECTED.txt bytes.
    Selected in RESULT.md; never pronounced by the verifier.

SCIENTIFIC-FIRED
    One exact mathematical counterexample to a frozen Q1-Q8 statement
    on the audited surface: a ring equality on the lattice, a failed
    exact Machin witness, a failed exponent-form identity, or a failed
    integer modulus inequality. Recorded, preserved, folded.

BOUNDED-AUDIT-C
    The audit completes RESULT PASS but the written universal proof is
    not accepted as theorem-grade in review: exactly the frozen finite
    surface stands (including only the four-pair D_b plus bare-C
    schedule sample), no universal claim.

STOP
    Before pin: authority, collision, exactness, security, metadata or
    hash integrity fails and no formal probe is created. After a
    completed formal gate: stdout-byte, transcript or architecture
    integrity fails; the completed evidence is preserved and RESULT.md
    records integrity STOP.

ABANDONED-PIN
    After the immutable pin, readback, static audit, preflight, timeout,
    nonzero exit, nonempty stderr, resource cap, negative-control or
    gate-5 integrity failure prevents the formal gate from completing.
    Preserve unchanged PREREG.md and verify.py; add only RESULT.md with
    `Status: ABANDONED`, no EXPECTED.txt and no RUN.md. The identifier is
    consumed and must never be reused or resumed.
```

`CONFIRMED` registers no public claim and changes nothing in Public
Canon v74; any registration is a separate fold decision.

## Formal order

1. This lock freezes the identifier, single branch, path,
   owner, layer, mode and `verify_sha256`; the verifier bytes are
   final before the lock.
2. Create only `probe/P-JIPC-WP3D-QPOS-MELLIN-1` and its one probe
   directory from the exact base above; move the draft `PREREG.md`
   and the never-executed `verify.py` there. Convert every draft
   marker to `PREREGISTERED / UNRUN / NON-CANONICAL`, insert this
   issue number, state that the pin SHA is recorded externally, and
   copy this locked authority tuple and `BASE_COMMIT` byte for byte.
3. Before any import or execution, commit and push the complete
   `PREREG.md` and `verify.py` as the immutable pin; record the full
   pin commit and `prereg_sha256` as a comment on this issue. No
   second remote branch or attempt ref is created.
4. Read both remote blobs back and record exact commit, SHA-256,
   bytes, LF and final LF on this issue; repeat the static audit (FZ7)
   on those read-back bytes.
5. Run the preflight; only after public readback execute the pinned
   verifier formally once in a deterministic environment.
6. After a completed run add only `EXPECTED.txt`, `RUN.md`, and
   `RESULT.md`. If no run completes after the pin, add only the
   mandatory `RESULT.md` with `Status: ABANDONED`, with no
   `EXPECTED.txt` or `RUN.md`.
7. Open one probe-only pull request. The completed route requires
   byte-identical x86_64 and aarch64 jobs plus aggregate `check` and
   manual security review. Never amend, rebase, squash, force-push,
   rename, resume or reuse this probe after the pin.
