# P-U-PREPARATION-EVENT-RECORD-1 preregistration

Status: FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED / L1 ONLY.
Owner: A. M. Thorn, Codex-preparation-record-20260906. Date: 2026-09-06.
Public claim: [issue #866](https://github.com/mathorn1973/twist-j/issues/866).
Branch: `probe/P-U-PREPARATION-EVENT-RECORD-1`.
Directory: `probes/P-U-PREPARATION-EVENT-RECORD-1/`.

## Authority, exposure and prospective custody

Authority is ACTIVE Public Canon v78, fetched public main
`65caa1c7221cb772a68f87409ac1f16082d6e92f`, content commit
`767b136713ae12f5f30869642852dcb8a3f671b0`, tag `canon-v78`.
CANON.md has 473631 bytes and SHA-256
`82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5`.
Tag/content ancestry, all normative hashes, local policy and Canon checks
and successful main workflow 34032334168 were confirmed. Open issues,
probes, registry and explicit remote heads were scanned before this claim.
The existing U-INDUCED-2 draft and issues #539, #830, #832 and #834 keep
their distinct ownership. No sealed probe is reused or resumed.

All analytical predictions below were exposed before execution. The raw
closure of piston sum and apparatus sum is also exposed in the unmerged
NON-CANONICAL null-anatomy note at commit
`e43b458337f2ce93dd0700c77e8391910e00d59b`; its status and broad physical
language are not inherited. The registered U-INDUCED-CHANNEL theorem is
explicitly one-tick only. The new native claim is complete all-time source
observability, readiness classification, tail retention and downstream
factorization, not discovery of that raw closure.

The positive construction combines exposed algebraic QDD data, Cartesian
incidence and the sealed causal phase decoder. Its fixed analyzer was designed
with the known QDD formula in view. It is an algebraic implementation with
no probability input, NOT a blind prediction, independent physical
preselection certificate or derivation of Cartesian incidence from U.
The chosen ordering and resources are frozen before its formal comparison.

No accepted new verifier has been executed or imported before the pin.
Only source inspection, algebra, writing, static parsing and review precede
it. Freeze PREREG.md, PROOF.md, NATIVE-PROOF.md, INCIDENCE-PROOF.md and
verify.py in one fresh commit; push and read back their exact bytes before
execution. Record the pin and hashes in RUN.md. Never amend, rebase, squash
or force-push this pin. A subsequent result cannot repair a pinned defect.

## Field 1: equations and the two explicitly different interfaces

Use unchanged native checkpoints `x=(p1,p4,p1p,p4p,q,r)` in F5^6,
`kappa=sum(x[:4]) mod 5`, `z=sum(x) mod 5`, and

    theta_n=popcount(n) mod 2,
    U(n,x)=(n+1,g_((z+2*theta_n) mod 5)(x)).

The five generators, with every component reduced modulo five, are

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

### I. Native apparatus: complete observable source factor

The source is the four pistons p and the apparatus is `A=(q,r)`. Each
experiment fixes one of all 25 ready values A independently of p. The
reader receives the ordered apparatus history, optionally the common driver
and common times, but no piston, source-dependent context or extra source
initialization. Every generator closes on `Q=(z,q,r)` by

    a: (z,q,r),             b: (-z,-q,-r),
    c: (2-z,1-q,-r),        d: (2-z,1-q,1-r),
    e: (3-z,2-q,1-r).

Thus every native apparatus history depends on p only through kappa, for
every common driver word. For fixed-origin Thue-Morse (initial bits 011),
the complete all-time equivalence of sources is already decided by
`(A0,A1,A2)`. Of 25 ready states:

- 21 distinguish all five kappa values already at A1;
- (0,0), (3,3), (1,3) need A2 to distinguish all five;
- (3,0) permanently identifies kappa=2 with kappa=4, and distinguishes
  the remaining three values already at A1.

Across all initial quotient states, the prefix-class counts through times
0,1,2,3 are respectively 25,121,124,124. Source-function recovery is
possible if and only if the function factors through the described quotient.
The sufficient reader uses the two-step prefix, not an unbounded search.

All z3=1. Thereafter corresponding apparatus updates are common bijections,
so apparatus tails from tick 3 agree if and only if A3 agrees. Each of the
four exceptional readies above has four tail classes; the other 21 have
five. Three source distinctions visible at tick 2 are therefore transient.

No history processor with a common source-independent initial state can
create a missing distinction in its chosen reader, output symbol or stored
record. This holds even with unbounded processing memory and the complete
history as input. The same-kappa supported sources p=1000 and p=2400 have
QDD LOW weights 1/16 and 1/96. The sources p=0000 and p=1400 have different
support tags. Both witness pairs have identical apparatus histories for
every ready and common driver, while their full native states never merge:
they always use the same bijective generator. These are port-observability
counterexamples, distinct from the previously sealed native-head merger.

### II. Retained-source incidence reader and fresh external cells

This interface explicitly admits additional resources that I does not:
capture the balanced source vector `v=ell(p)`, `ell=(0,1,2,-2,-1)`, before
the original head can be erased; keep it fixed; admit complete Cartesian
incidence of each integer channel; supply an ordered causal clock buffer
and fresh writable cells. No feedback to U is allowed.

Set `s=sum(v)`, `Qv=sum(v_i^2)`, `d_ij=v_i-v_j` for i<j. The one fixed
analyzer has 31 signed integer channels: s and five copies of each of the
six d_ij. Freeze this potential slot order independently of the individual
source:

1. slots 0,...,63: LOW, row and column 0,...,7 in lexicographic order;
2. the next 480 slots: HIGH, pairs (i,j) in lexicographic order, then copy
   0,...,4, row 0,...,3, column 0,...,3;
3. slots 544,...,1023: empty padding.

A LOW slot is occupied iff both its indices are below |s|; a HIGH slot for
(i,j) is occupied iff both are below |d_ij|. All slots are whole objects.
One available causal length-2560 Thue-Morse window supplies the phase
`rho=n mod 1024` by the inherited local-parity recursion. At each natural
tick the reader addresses exactly slot rho. It emits that occupied slot's
LOW or HIGH label, or SILENT if empty. The zero source has no occupied slot
and is tagged ZERO_SUPPORT, never normalized and never assigned an event.

The complete counts in each 1024-tick period are

    N_LOW=s^2,
    N_HIGH=5*sum_(i<j)(v_i-v_j)^2,
    N_ACCEPTED=20*Qv-4*s^2.

For nonzero v the last quantity is positive and the accepted LOW ratio is
`s^2/(4*(5*Qv-s^2))`, the exposed QDD algebraic weight. The proof covers
every fixed source and every ordinary prefix length after buffer warmup.
No reduced ratio, target weight or probability-keyed memory enters the
constructor. This is not claimed to be an independently selected physical
meaning of QDD.

For each emitted label e, a fresh cell has alphabet {BLANK,LOW,HIGH} and
the controlled permutation swaps BLANK with e and fixes the third symbol.
The source/control remains unchanged. Append a complete accepted record
containing captured v before/after, recovered phase, fine slot descriptor,
nonzero channel sign, coarse label and the BLANK-to-label cell transition.
Preserve every older record and cell. An event-free tick writes no cell.
An idempotent read returns the record (or its first cell); it does not step
the source or append again. The full post-state includes the retained source,
clock buffer and ordered record. The cell permutation is reversible; the
supply/append of fresh storage is an explicit resource, not a reversible
closed native dynamics or a derived physical apparatus reset.

This defines one mathematical symbol per accepted tick and an explicit
stored record. It does not establish quantum collapse, exclusive physical
occurrence or the Born distribution of first outcomes of repeated fresh
preparations. For v=1000, phase 0 is an occupied LOW slot and phase 64 an
occupied HIGH slot: selecting only one of these phases each cycle yields
all LOW or all HIGH despite the ordinary accepted ratio 1/16. No inference
to arbitrary invocation calendars or first-event trial laws is allowed.

## Field 2: accepted exact code and frozen finite coverage

The accepted verify.py is self-contained standard-library Python, using
integers, finite tuples and Fraction only. It imports no source verifier,
uses no floats, random input, network, subprocess, external data or file
writes, and emits deterministic ASCII JSON with one final LF. Its accepted
source has 30007 bytes and SHA-256
`74c767060cd4c908d48cc52cb078f8ac7e42987fd8d3290b63895db26cd980fd`,
recorded before the joint public pin.

The frozen audit domains are:

- all 15625 native checkpoints under all five generators for involution,
  bijection and quotient identities, and under both selector bits;
- all 125 quotient states through the first three TM ticks; all 125^2
  ordered pairs for full-history and tail equivalence; every ready-state
  class and its minimum observation horizon;
- all 25 ready values and all 625 piston tuples, forming observation
  classes before evaluating target records; every resulting class's QDD
  LOW/support data, complete five-field record count using the inherited
  common-sign equality lemma, and both fixed witness pairs for every ready;
- all four legal parent pairs expanded to blocks of length 4096 and every
  offset 0,...,4095, giving all 16384 generating contexts for the length-2560
  phase window; test the recovered endpoint modulo 1024 in every context,
  compare substitution blocks with literal popcount, and check native
  z-history bit reconstruction and the +1 endpoint shift in every context;
- all 625 sources and every one of 1024 phase addresses for the fixed
  31-channel, 544-slot universe; exact channel/count/Gram identities,
  single-symbol output, support disposition and QDD comparison;
- both nonblank controls on all three cell states, with swap involution,
  fresh write, nondestructive read and old-record preservation; also the
  SILENT identity on all three cells, and rejection of LOW/HIGH occupied
  cells for source 1000 at phases 0 and 64;
- seven retained balanced source vectors: 0000, (1,0,0,0), (1,-1,0,0),
  (2,2,2,2), (2,2,-2,-2), (-1,1,0,0), (2,1,1,2). For each source and
  initial phase 0 or 64, begin at n0=3072+phase with a genuine length-2560
  window ending at n0-1, then capture exactly 1024 consecutive native bits.
  Audit every causal phase, output, complete record, fresh write and replayed
  read, first-record retention, and exact counts at every intermediate prefix
  and at the complete cycle. The source is fixed throughout.
  Include the explicit phase-0 versus phase-64 invocation counterexample.

All seven record-audit sources also test empty-buffer UNAVAILABLE, illegal
constant-zero complete windows and nonbinary short/complete windows. Rejected
nonbinary acquisitions must preserve the old state and retain the rejected
input. The exact case inventory is frozen by the accepted source above.
The six required groups are A (native factor), B (observation quotient),
C (causal phase), D (source incidence), E (complete records) and F (target
comparison after classification and the fixed witness controls).

The universal claims rest on the separate proofs. Finite trajectories and
the 16384 factor contexts audit them; no sample substitutes for an infinite
equivalence or limit. Every group must finish. Exact mismatches are retained
as FALSIFIED; exceptions or missing groups produce STOP.

## Field 3: carriers, equality, contexts and sources

In I, histories have literal ordered equality. The complete class consists
of all functions of the admitted apparatus transcript, including nonlinear
readers and processors with unbounded history or memory. A common initial
processor state and common clock/calendar are allowed; source-dependent
initialization, piston inspection, intervention or a different port is not.
When z is explicitly added as a port, it reveals kappa already at tick zero;
even that larger port still fails both same-kappa witnesses. Distinguish this
augmented port from the A-only classification.

In II, source equality is equality of the four signed integers; slot,
symbol and record equality are literal, with records ordered. The analyzer,
slot order, buffer length, control permutations and interpretation of
occupied slots are fixed across all sources. Sources may share occupied
slots; there is no requirement to assign different behavior to the same
fully specified (v,window) input. Context never receives a numerical QDD
probability. The model has one complete fixed algorithm, not a claimed
complete physical family or physical uniqueness result.

The clock buffer is chronological and causal, with finite warmup returning
UNAVAILABLE and no event. Full non-native words are outside its legal input
carrier; source capture/order and availability of native words are explicit
premises. Repeated query is not repeated acquisition. Keeping v after its
head is lost, or appending records permanently, is additional observer
storage. ZERO_SUPPORT, SILENT, UNAVAILABLE and BLANK are distinct types:
source support, no addressed event, incomplete observation, and fresh cell.

All mathematical source files and the two unmerged public comparison refs
are identified by exact bytes in PROOF.md. They supply exposed generator,
QDD, phase and incidence facts at their existing scope, not physical status.
The accepted verifier imports none at runtime. No external dataset or new
third-party material is introduced.

## Field 4: systematics and first-run custody

Risks include confusing the piston sum with quadratic source shape,
one-tick or finite-sample separation with complete histories, complete
history with a late tail, a common ready with a source-keyed ready, retained
source data with a native register, cell availability with endogenous
writing, or fixed-source counting with independent trial occurrence.
The two-interface declaration, complete quotient proof, early/late tables,
explicit source and tape ownership, and invocation counterexample address
these risks. This is a result-exposed proof audit, not blind confirmation.

After public pin/readback, from a clean repository root on Linux or a
Linux-compatible environment, run

    python3 probes/P-U-PREPARATION-EVENT-RECORD-1/verify.py

with `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Capture separate raw stdout/stderr outside the worktree. Require zero exit,
empty stderr and unchanged pinned bytes, then save the actual stdout as
EXPECTED.txt and record neutral environment, pin, hashes and sizes in RUN.md.
Both required GitHub x86_64/aarch64 Python 3.12 replays must match the one
EXPECTED byte for byte. No old output is substituted and no pinned source
is repaired after execution.

## Field 5: failure threshold and dispositions

Zero mathematical mismatches are allowed. Any failure of quotient closure,
claimed history or tail equivalence, source-class completeness or witness
identity falsifies the corresponding native statement. A supported source
whose declared incidence counts, addressed label, ratio or record differs
from the frozen equations falsifies the corresponding conditional statement.
So does failure of a claimed phase identity, controlled cell permutation,
old-record persistence or positive support/zero-support distinction.

A completed run with a mathematical discrepancy is FALSIFIED and keeps
EXPECTED/RUN/RESULT. A bad pin/source hash, implementation defect, exception,
nonzero exit, nonempty stderr, missing group, undeclared input or unnamed
layer lift is integrity STOP, not success. If no valid gate completes, keep
the pin, close this consumed identifier ABANDONED under POLICY and give any
corrected experiment a new identifier. Preserve genuine mathematical
negatives rather than recasting them as technical failures.

The native port's inability to reproduce QDD is a predicted negative
conclusion, not a defect to repair by adding a hidden source input. Conversely,
the conditional constructor passing is not evidence that its extra resources
have been realized natively or selected physically.

## Field 6: action layer and scientific boundary

L1 only: finite algebra, deterministic words, ordinary counting limits and
symbolic record transformations. No physical L5 record, L6 probability
measure or cross-layer promotion is adopted. No Canon, owner, workflow or
sealed-probe file is modified.

The native branch settles exactly which preparation information its complete
port history can carry. The positive branch makes a full conditional
source-to-symbol-to-storage implementation concrete, including the extra
resources. It is not a proof that U forces its analyzer, incidence access,
physical preparation calendar, exclusive outcome, post-measurement state
or fresh-cell supply. The unchanged native no-write theorem remains confined
to fixed finite-window readers after all their input is synchronized; it is
not generalized to arbitrary counter-dependent readings or early transients.
QDD-INSTRUMENT-APPARATUS, its physical O1/O2 children and the full physical
decoder remain open at their existing scope.
