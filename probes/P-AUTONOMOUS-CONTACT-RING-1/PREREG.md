# P-AUTONOMOUS-CONTACT-RING-1

NON-CANONICAL / L1 / prospective exact contact-law probe.
Owner: A. M. Thorn, autonomous-contact closure session, 2026-11-08.
Reservation: https://github.com/mathorn1973/twist-j/issues/1966.
Base: main 629a9d4058501f938dc91a690c3eb59a914493d1, ACTIVE Public Canon v110.
Declared content: c8197bcc807de1f62248463aec77f7ac7ab46f85.

## 1. Question and equation

Can one fixed local contact law, without a stored contact word, write an
unknown source sign into a completely blank receiver and determine its
entire subsequent retention and erasure behavior?

Let O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2, and

    C(x,y)=(x,y)                         if x-y is not in 2O;
    C(x,y)=((x+y+rho*(x-y))/2,
            (x+y-rho*(x-y))/2)          otherwise.

On an even marked ring of N>=4 cells, let

    M0 = {(0,1),(2,3),...,(N-2,N-1)},
    M1 = {(1,2),(3,4),...,(N-1,0)}.

All contacts within one matching are simultaneous and disjoint. Put
b_n=1 exactly when nu_2(n) is even. With K_b=C_{M_b}, the complete forward law is

    F_N(n,z) = (n+1, K_{b_n}(z)), n>=3.

The bit is the indicator of the native fired letter b on the canonical
synchronized chart: adjacent Thue-Morse bits differ exactly when nu_2(n) is
even. This equation uses that projection only. No identification with the
complete native U carrier, or cross-layer lift, is claimed.

## 2. Carrier, source family, reading and predicted continuation

The full carrier is {n>=3} x O^N. The counter is unbounded. For the primary
family take N=8, n=3, a in {-1,+1}, z_1=2a, z_5=-2a, and every other cell
exactly zero. Only these two source cells depend on a. No receiver, hidden
memory, matching table or controller contains a. The ring has sum zero,
Hermitian account h=8, and proper half-trace account E=16.

The same construction is predicted to have a nine-state ring-value class
for every even N>=8 and every nonzero odd integer a. The nine states and
their complete transition tables are frozen in CONTRACT.md. Both signs in
the primary family have the same complete account, not merely the same
readout account. There is no preparation theorem for the source family.

The single-cell reader is fixed on all O: BLANK if y=0, otherwise
VALUE(Tr(y)/5), a tagged exact rational value. Equality means tag equality
and ordinary rational equality; a nonzero zero-trace cell reads VALUE(0),
not BLANK. Context keys are the fixed cell address and fixed marked geometry.
No time, source label or contact phase is available to this reader. On the
declared receiver states the value is an integer. No physical L5 reading
or uniqueness among all possible readings is asserted.

For the primary right receiver z_2, the predicted readable boundaries are
n=4,5,6,7,8,9, all with VALUE(a). At n=3 and n=10 it is literally zero.
There are six readable boundaries and five elapsed ticks between the first
and last. The continuing law erases the right record in tick 9. At n=10
only the ring values have returned; the complete clock-plus-ring state has
not. Left and right fixed receivers together also decode a throughout all
eight nonbase states of the nine-state class.

Each K_b is a bijection preserving sum, full Hermitian account, proper
half-trace account and each labelled residue modulo 1-j. Its inverse is
K_b^4. F_N is injective, with an exact predecessor on its image n>=4; it is
not onto the initial clock slice n=3.

## 3. Accepted code and custody

The scientific source set is PREREG.md, CONTRACT.md, PROOF.md, verify.py and
break.py in this directory. The first two documents are frozen before code
construction and handed over through a Git commit. That document commit is
not the execution pin. The full source set, including the accepted verifier,
must then be committed, pushed and read back before any scientific execution.
Record that full pin and all five source hashes in RUN.md. Do not amend,
rebase, force-push or modify a frozen source to repair an outcome.

The primary author may read the canonical primitives and the frozen analytic
review. The independent breaker receives only the frozen PREREG.md and
CONTRACT.md plus the normative repository instructions. It must not read
verify.py, PROOF.md, primary output or primary implementation messages before
its own break.py is frozen in Git. It implements a separate five-coefficient
cyclic arithmetic. The primary uses four-coefficient polynomial reduction.
Both are frozen before comparison. This is independent implementation of a
disclosed predicted contract, not blind discovery of the prediction.

Both implementations expose audit() returning the precisely specified
report in CONTRACT.md. The accepted verify.py runs its own audit, loads the
frozen break.py, runs its audit and requires exact report equality. It prints
one deterministic JSON object and a final newline. The breaker also has an
independent command-line entry point that prints its report. Neither program
uses floating point, randomness, network, scientific imports from other
probes, external data or file writes. Reading the frozen breaker source is
the verifier's only runtime file dependency.

Static source reading, hashing, AST parsing and compilation are permitted
before the full pin. Importing or executing either scientific module is not.
No scientific dry run has been performed for this candidate.

## 4. Finite data and exact inventory

The complete inventory and serialization are frozen in CONTRACT.md:

- 6561 pair inputs from all four-coefficient tuples in {-1,0,1}^4 squared;
- 13122 four-cell matching cases from the nine-symbol cell alphabet;
- 4320 nine-state transition cases, covering N in {8,10,12}, every even
  translation, all odd a from -15 through 15, all nine states and both bits;
- 514 primary boundaries from both source signs, n=3 through n=259, with
  complete backward recovery of both 256-tick histories;
- two controls: a completely zero ring and the declared even-source leakage;
- native-bit comparison for n=1 through 8192 and all observed factor counts
  of lengths 1 through 64 in that fixed prefix.

Finite inventories are audits of the accompanying analytic statements, not
exhaustions of the unbounded carrier. The all-time nine-state theorem,
inverse, finite propagation and zero entropy bounds are argued in PROOF.md.
New trajectory and audit digests are not known before execution.

## 5. Systematics and failure threshold

Tolerance is zero. Any arithmetic disagreement, wrong complete state or
transition, lost account/sum/residue, wrong reader tag/value, missing case,
failed inverse, failed odd-family guard, incorrect control, native-bit
disagreement, factor-bound violation or unequal independent report fails
the corresponding prediction. No failing input is removed and no threshold
is moved. A nonzero exit, timeout or nonempty stderr is not a pass; preserve
the pin and follow the repository's result/abandoned-pin rules.

Run assertions enabled under standard-library Python 3. Remove inherited
PYTHON* and TWISTJ* environment variables, then set PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC. Run the pinned verify.py from
the repository root, with the repository's 600-second verifier limit. Record
exact stdout as EXPECTED.txt and neutral platform metadata in RUN.md. The
unchanged repository checkers must replay it. Public computation evidence
requires the same head, verifier hash and exact EXPECTED bytes on the
required x86_64 and aarch64 Python 3.12 jobs and their aggregate check.

## 6. Action layer, status and exclusions

Action layer: L1 state. The law is a candidate-D construction. A completed
finite audit initially supplies candidate-C evidence; the independent
algebraic and counting arguments may support candidate-T at their stated
scope. All remain NON-CANONICAL pending review and a separate public fold.
This probe edits no Canon, registry, policy, workflow or existing gate.

The geometry, two-color marking, association b->M_b, initial clock and source
preparation are declared model data. Translation by two cells is a symmetry;
translation by one swaps the two matchings. This is not a unique law derived
from J, a derivation of physical space, a native-apparatus closure, permanent
archive, new source preparation, indefinite independent renewal, positive
entropy, Born statistics, photon identification or physical time.

The entropy statement concerns a fixed finite-valued local reader producing
one symbol per native tick, including no-event ticks, and allowed to inspect
the clock only through b_n. It covers a finite ring at fixed proper account
and an infinite line at fixed finite total proper account. It does not cover
an arbitrary read of n, a growing uncounted memory, infinite total account,
an information-bearing infinite background, or arbitrary sparse event-only
resampling. The infinite line is a declared mathematical extension, not an
empirical claim about the size of the physical plenum.
