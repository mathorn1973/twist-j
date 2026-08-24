# P-TM-SHEET-SYNCHRONIZING-GRAPH-1 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / NO FORMAL RUN`

This document freezes one exact L1 probe for the new candidate claim
`TM-SHEET-SYNCHRONIZING-GRAPH`, carried in from the incubation lane as
`C-TM-SHEET-SYNCHRONIZING-GRAPH-1`. It contains no verifier output and earns
no scientific or Canon status. Formal execution is forbidden until this
document and `verify.py` are committed, pushed, and read back from the public
remote as one immutable initial pin.

## Public identity, authority, and action layer

```text
program owner:       C-TM-SHEET-SYNCHRONIZING-GRAPH-1 (incubation candidate)
target claim:        TM-SHEET-SYNCHRONIZING-GRAPH (new registry row on fold)
probe:               P-TM-SHEET-SYNCHRONIZING-GRAPH-1
public lock:         issue #417
public lock URL:     https://github.com/mathorn1973/twist-j/issues/417
probe owner:         A. M. Thorn
branch:              probe/P-TM-SHEET-SYNCHRONIZING-GRAPH-1
path:                probes/P-TM-SHEET-SYNCHRONIZING-GRAPH-1/
initial base:        cef0a08cec219a41333b36fbfe0a0e4dc780045f
Public Canon tag:    canon-v51
content commit:      bf25cde49bca33a5bb93ecdf50b641f0042b5211
Canon SHA-256:       eb0f6aacb04c405f36ae1e8ece4c6c58c416884fa15fe017c2ee64bb240abec4
Canon bytes:         257459
action layer:        L1 only
```

Lineage and novelty boundary, none of which is a logical premise:
`KERNEL-Z6-SYNCHRONIZATION [T]` displays the sheet table this probe
re-derives and owns the moving-layer theorem; `RAMIFIED-TM-LIFT [T]` supplies
the phase dictionary quoted in clause 8; `FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT [T]`
is cited in clause 5 as a partition coincidence only;
`TIME-CUT-READING [D]`, `CENSUS-Z5-SHEET [C]`, `QUADRATIC-DECODER-DATA [O]`,
and `MINIMAL-READ-DERIVATION [O]` are excluded from the premises and are not
moved, strengthened, or interpreted by this probe.

## Result exposure

Every clause below was already observed in two non-formal single-platform
project runs, both x86_64, recorded with the artifacts:

```text
recon note      RECON-DECODER-PAIR-RELATIONAL_2026-08-18.md
                sha256 6a8ce86e9cd71ddbc7f7ceb8c39711c2de7c3bfdfc16a8408258fcc295545bc4
recon verifier  recon_decoder_pair_sheet_automaton.py
                sha256 66ce8da62714c010597f8fe507c0e7130f83c9681aa22f2e4e11344d6286f51b
recon stdout    sha256 ae1ae198674b001c71124dab1470b40ddc527321f2ec25c51b724d1d92329b57
audit note      AUDIT-EXTERNAL-RELATIONAL-REVIEW_2026-08-18.md
                sha256 6f79494037a45d925d559cee36d509c73f09fc4f01f8f8f9addaeef05b3caf36
audit checker   audit_relational_review_checks.py
                sha256 5e58b880a4be2da2d0ce7527a46e5b5bf7aa3652a3121b692183114daaed2d83
audit stdout    sha256 c2dd0dfc55de8e43608e2b1a5861be9018f775966cd4b257419b0e160786a19d
```

This probe is therefore a pinned confirmation and adversarial audit, not
blind discovery. No equation, carrier, systematic, threshold, output route,
or scope may move in response to the exposed conclusions. The frozen verifier
has never been executed; before the pin it was checked by `py_compile` only.

## Falsifier first

A single exact counterexample to any one of clauses 1 through 8 below
falsifies the candidate: a binary word violating the reset equivalence of
clause 1; a transformation-automaton or support-quotient count or
identification of clause 2 failing; a factor of the Thue-Morse language of
length at most 16 outside the mu^4 construction of clause 3, or a factor
count differing from the frozen row; a failure of any w* fact of clause 4;
a leaf-transformation, preimage-partition, or quadratic-class value of
clauses 5 and 6 differing; a Thue-Morse factor of length 9 whose composed
map is not the frozen constant, or any violation of the invariant-graph
clause 7; or a sign-law mismatch in clause 8.

An environment or argument defect, an unpinned sentinel, an exception, a
nonzero exit on a valid route, nonempty stderr, or a cross-architecture byte
mismatch is `STOP`, not `FALSIFIED`. Exit code map: 0 pass, 1 STOP,
2 FALSIFIED.

## The six frozen fields

### 1. Equation

Let `T_0 = (0,4,0,4,4)` and `T_1 = (2,1,1,3,1)` act on `F_5`, derived inside
the verifier from the five declared generator involutions on `X = F_5^6` and
the selector `sigma = (z_6 + 2 theta) mod 5`. A word `w = w_1 ... w_k` acts
in temporal order, `T_w = T_(w_k) o ... o T_(w_1)`, and `R(w) = T_w(F_5)`.
`theta_n = s_2(n) mod 2`; `L_TM` is the factor language of `(theta_n)`.
The eight clauses:

```text
1  for every finite binary word w, |R(w)| = 1 iff w contains 011 or 110;
   the minimal synchronizing words are exactly 011 and 110; R(11) = {1,3}.
2  the transformation automaton with identity start has exactly 9 states
   and 8 nonempty-word maps; the support quotient has 7 states and exactly
   two 2-to-1 identifications: on support {0,4} the maps (0,4,0,4,4) and
   (0,4,4,4,4), on support {1,2} the maps (2,1,2,1,1) and (2,1,1,1,1); the
   quotient is well defined on every support class.
3  the factors of L_TM of length at most 16 are exactly the factors of
   mu^4(ab), ab in {00,01,10,11}, mu(0) = 01, mu(1) = 10; the factor counts
   for lengths 1..16 are 2 4 6 10 12 16 20 22 24 28 32 36 40 42 44 46;
   every factor of length 9 synchronizes.
4  the unique nonsynchronizing factor of length 8 is the palindrome
   w* = 10100101, the unique 11-free factor of length 8; no 11-free factor
   of length 9 to 16 exists; for k in 3..16 a factor fails to synchronize
   iff it contains no 11; the unique two-sided neighborhood is 1 w* 1.
5  T_w*(0) = 2 and T_w*(z) = 1 for z != 0; the preimage partition is
   {0} | F_5^x, the zero orientation of the field cut theorem, as a
   partition coincidence only.
6  eps(T_w*(z)) = 1 iff z = 0, where eps is the quadratic-class bit,
   eps(1) = eps(4) = 0 and eps(2) = eps(3) = 1; R(01) = R(w*) = {1,2} while
   T_01 = (2,1,2,1,1) differs from T_w*; the pre-final maps are (0,4,0,4,4)
   and (0,4,4,4,4), of equal support {0,4}.
7  over the two-sided Thue-Morse subshift, the skew product
   (theta, z) -> (S theta, T_(theta_0) z) has the invariant graph
   z = 4 + 2 theta_(-1); every factor of length 9 composes to the constant
   map with value 4 + 2 u_last, so the graph is the unique invariant graph,
   unconditionally; the canonical start 011 reaches it in exactly 3 letters
   and the bound 9 is sharp, witnessed by |R(w*)| = 2.
8  (4 + 2 theta) mod 5 = (-(-1)^theta) mod 5 for theta in {0,1} and along
   theta_n for n < 2048; on the graph the quadratic-class bit is removed by
   a 2-to-1 merge at every synchronization edge and the clock bit survives
   only as the sign inside {1,4}.
```

### 2. Code

`verify.py`, Python standard library only, exact integer arithmetic, no
float anywhere, reads no files, no arguments, canonical ASCII stdout with
final newline, empty stderr, runtime under 120 seconds from the repository
root under:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Gate list, in order: I01 runtime; C01 carrier; C02 generators; C03 sheet
table; A01 transformation automaton; A02 minimal reset; A03 reset theorem
(direction A on all seven subset states, direction B by the pattern-free
product graph with the frozen node count 7, brute force over all 32766
binary words of length at most 14); L01 Thue-Morse pairs; L02 mu^4 language
with prefix equality for lengths at most 12 and prefix containment for
lengths 13 to 16 against the 65536 prefix; L03 nonsync table
2 4 4 5 4 3 2 1 0 0 0 0; W01 w* facts; W02 leaf transformations; W03
quadratic-class cut; G01 invariant graph; G02 sign law; then `RESULT PASS`.

### 3. Carrier or data

`X = F_5^6` with the five declared generator involutions and the selector;
the induced pair `T_0, T_1` on the sheet coordinate; the Thue-Morse word
`theta_n = s_2(n) mod 2` with its 65536 prefix and the exact `mu^4` block
language; the two-sided Thue-Morse subshift for clause 7. No external data.

### 4. Systematics

Temporal composition order as declared in the equation field. The 9-state
count includes the identity start state; the monoid of nonempty-word maps
has 8 elements. The language-exactness proof is the block argument: every
factor of length at most 16 lies in a concatenation of two adjacent mu^4
blocks, and every such concatenation is mu^4 of an occurring pair; the
prefix comparison is a consistency gate and is frozen at equality for
lengths at most 12 and containment for lengths 13 to 16, so no gate rests
on prefix completeness beyond the audited range. The brute-force reset
bound is 14. Prior exposure is declared above; both prior runs are one
architecture family, so this probe supplies the first second-architecture
leg at pull-request time.

### 5. Failure threshold

Any single exact counterexample to any clause fires the falsifier and exits
2 with a `FALSIFIED` line naming the gate. All frozen constants above are
thresholds and may not move. Integrity defects exit 1 with a `STOP` line
and are not scientific falsifications.

### 6. Action layer

L1 only. No claim, output, or reading of this probe lifts to L2 through L6.
No D_clock completeness, uniqueness, or totality; no counter
reconstruction; no census meaning for the value pair {1,4}; no
physical-irreversibility, probability, or measure reading; no recovery of
the four-phase lift value.
