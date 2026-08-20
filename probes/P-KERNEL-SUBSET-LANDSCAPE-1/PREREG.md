# P-KERNEL-SUBSET-LANDSCAPE-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

The complete connectivity landscape of the kernel letter subsets. The
dichotomy is carried by the subset-generic restatement below of the lemma
chain already public in KERNEL-CONNECT-ALL-K [T]
(probes/P-KERNEL-CONNECT-ALL-K-1); the verifier decides the 32-entry
dimension table exactly and audits the chain's finite instances. The
result is exposed before execution: the connected subsets are exactly
acde and abcde.

## Public identity, authority, and action layer

```text
probe:           P-KERNEL-SUBSET-LANDSCAPE-1
public claim:    issue #449
probe owner:     A. M. Thorn / delegated session cleanup-batch-2026-08-20
branch:          probe/P-KERNEL-SUBSET-LANDSCAPE-1
basis:           Public Canon v54, main 70e1c480, tag canon-v54,
                 SHA256SUMS 5 of 5 OK
action layer:    L1 (state). No layer lift, no measure, no dynamics
                 claim, no canon edit by this probe.
lineage:         carries in the incubation candidate
                 C-KERNEL-SUBSET-LANDSCAPE-1 (2026-07-18) with its
                 Amendment 1: the original lower-bound clause
                 5^(k(6 - dim U_S)) FIRED against an exhaustive count
                 (25 demanded, 2 found for S = bcde at k = 2) and is not
                 asserted here; the public negative branch claims at
                 least two components and nothing more. The fired clause
                 is first-class lane history, archived, threshold unmoved.
```

## Falsifier, first

An exhaustive exact component count at any k >= 2 for any subset S that
contradicts the dichotomy (one component with dim U_S < 6, or more than
one component with dim U_S = 6), or an exact recomputation of any table
entry differing from the pinned value. Operationally: any pinned gate
FAIL on rerun.

## The six fields

```text
EQUATION     for every S subset of {a,b,c,d,e}, with the two-way CSUM
             ring transvections present: (F_5^6)^k is a single component
             for every k >= 2 iff dim U_S = 6; dim U_S < 6 gives at
             least two components for every k >= 2. U_S is the smallest
             <M_g : g in S>-invariant subspace of F_5^6 containing
             {v_g : g in S strictly affine}. Decided table:
             dim U_S = 6 exactly for S in {acde, abcde}.
CODE         probes/P-KERNEL-SUBSET-LANDSCAPE-1/verify.py, stdlib only,
             integers mod 5, no float anywhere, deterministic, under
             120 s, run from repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      the frozen kernel model of KERNEL-CONNECT-ALL-K [T]: the
             five letters in the verbatim forms of the public witness
             reproduce/kernel-connectivity, diagonal action on cells
             indexed by Z_k, plus the two-way CSUM ring transvections.
SYSTEMATICS  the letters and the decision structure are inherited
             verbatim from the public probe; four table entries (acde,
             cde, cd, c) and the bcde entry were disclosed exploration
             of the incubation lane and bind nothing; the k = 2
             exhaustive count 2 for bcde is candidate-lane history, not
             public evidence, and the public claim does not use it.
THRESHOLD    any gate FAIL kills the probe. Exact equality only.
LAYER        L1. One proposed T row; no live row moves.
```

## The written proof (subset-generic lemma chain)

The chain of KERNEL-CONNECT-ALL-K [T] uses exactly two properties of the
generating set: the letters are affine involutions g(x) = M_g x + v_g,
and the ring transvections are present. Restated for an arbitrary subset
S, with U_S as above:

Confinement. U_S contains v_g and is M_g-invariant for every g in S, so
every letter maps U_S into itself; the transvections add cell contents
and preserve membership of every cell in U_S. Hence the orbit of 0 in
(F_5^6)^k lies in the box (U_S)^k, for every k >= 1.

Extraction. For any diagonal letter D_g and ring transvection product
S_Q, the commutator [D_g, S_Q] is the exact translation by
(1 - Q1) tensor v_g: the linear parts cancel and only the seed survives.
Linear letters (v_g = 0) give the identity; strictly affine letters
yield nonzero translations with cell components in U_S. At k >= 2 the
ring transvections produce every coordinate pattern delta_i.

Transport. Conjugating the extracted translations by letters closes the
cell factor to all of U_S, and the ring transvections spread the seeds
to every cell, so the generated group contains every translation of
(U_S)^k. If dim U_S = 6 this is every translation of the full space:
one component for every k >= 2. If dim U_S < 6, the box (U_S)^k is a
proper invariant subset containing the orbit of 0, so its nonempty
complement is not reachable from 0: at least two components. Both
branches together are the dichotomy; connectivity is read off the table.

The superseded stronger lower bound is not part of the claim (see
lineage); the corrected consequence stops at "at least two".

## Proposed fold edits (a later sealed fold, not this probe)

Registry, one row (tab-separated; canon section 3, the kernel and the
census):

```text
KERNEL-SUBSET-LANDSCAPE	T	for every subset S of the five kernel letters, with the two-way CSUM ring transvections present, the coupled power (F_5^6)^k is a single component for every k >= 2 iff dim U_S = 6, and dim U_S < 6 gives at least two components; the exact 32-entry table of dim U_S is decided, monotone under inclusion, and the connected subsets are exactly acde and abcde; the letter a is necessary (dim U_cde = 4, dim U_bcde = 5) and b is never needed	3. The kernel and the census	probes/P-KERNEL-SUBSET-LANDSCAPE-1	an exhaustive exact component count at any k >= 2 contradicting the dichotomy, or a table entry recomputing differently
```

Frontier: no change. Ledger delta: claims +1, T +1. The row is the
sharpness companion of KERNEL-CONNECT-ALL-K [T]: that row connects with
acde; this row says exactly which subsets connect and why a is
load-bearing while b is inert.

## Non-claims

No dynamics, no measure, no selection law, nothing about the single-cell
census beyond what KERNEL-CELL-COMPONENTS [C] registers (the k = 1
component counts and this k >= 2 classification are different objects).
No exact component counts on the negative branch beyond "at least two".
