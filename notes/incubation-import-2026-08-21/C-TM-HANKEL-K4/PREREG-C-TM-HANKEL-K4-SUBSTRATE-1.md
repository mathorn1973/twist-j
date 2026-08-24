# PREREG C-TM-HANKEL-K4-SUBSTRATE-1

```text
CANDIDATE:    C-TM-HANKEL-K4-SUBSTRATE-1
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
TARGET LINE:  public, mathorn1973/twist-j, on a later separate probe
PUBLIC BASIS: Public Canon v43, main 981aa1b9c8bc7ecd084346e099f014f3fc78847c
              tag canon-v43, CONTENT_COMMIT 320324f0def8ac9af89d0f128dbd7ab6548df55b
              CANON_SHA256 a52d0c266024dd492b56f6ad3a1121e3bccd0a0563b86176cab0118bc8e4991c
              canon/SHA256SUMS 5 of 5 OK on a fresh clone at freeze time
CONSUMED:     TM-HANKEL-DIVISOR-BRIDGE [T], TM-HANKEL-SQUAREFUL-RANK-NOGO [T],
              TM-HANKEL-EXTREMAL-WITT-SKELETON [T], TM-HANKEL-K2-TRANSFER [T],
              TM-HANKEL-K3-UNIVERSAL-TRANSFER [F],
              TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION [C]
LAYER:        L1 only. No L2-L6 lift is claimed or tested.
ONE SESSION:  this document claims the candidate id.
```

## Inheritance rule, frozen

This candidate inherits NO hypothesis from k = 3. It does not assume that
the two-scalar law, the rigidity trichotomy, the pair-Schur mechanism, or
quadratic invariant sufficiency survive at k = 4. The k = 3 machinery is
available as a tool and as a contrast, never as a premise. Every k = 3
number quoted below is quoted as the value to be broken, not extended.

## Notation

`t(n) = (-1)^(s_2(n))` with `t(1) = -1`, `c = mu * t`. For an odd
squarefree prime set `P` with `k = |P|`, subsets `S,T` of `P`,
`n_S = product_(p in S) p`, `K_P(S,T) = c(n_S n_T)`,
`Kxor_P(S,T) = c(n_(S XOR T))`, `R_P = K_P - Kxor_P`,
`W(S,T) = 2^(|T|-|S|)` for `S` a subset of `T` and 0 otherwise. `P` is
EXTREMAL when `t(n_Z) = (-1)^(|Z|+1)` for every `Z subseteq P`. Inertia is
printed with named fields `NEG ZERO POS`.

Abstract substrate at `k = 4`: the cell multi-index of the pair `(S,T)` is
`m in {0,1,2}^4` with `m_i = [i in S] + [i in T]`. The extremal binary face
`{0,1}^4` is fixed by extremality; the free squareful cells are
`X_4 = {0,1,2}^4 minus {0,1}^4`, `|X_4| = 65`, each carrying a free sign.
`K` is linear in those 65 signs. A table is BALANCED when its `K` inertia
is `NEG 8 ZERO 0 POS 8`; any other inertia is a FAILURE. The cell order is
the code order `27 m_1 + 9 m_2 + 3 m_3 + m_4`, ascending. `S_4` acts by
permuting coordinates; the ten orbit types are the multisets of `m`.

`2^65` is not enumerable. Nothing below is quantified over the whole
substrate, and no census of the substrate is claimed at any point.

## Field 1. EQUATION (the frozen question and its gates)

The frozen question is the minimal invariant information that decides the
`k = 4` transfer. It is attacked from below: every gate either derives an
exact structural bound or exhibits an exact witness that raises the
information lower bound. Sufficiency of any layer is NOT a gate here.

```
A  SUBSTRATE SPLIT (derivation, exhaustively checked)
   Because W is subset-monotone, the (S,T) entry of W^T M W depends only
   on cells (S',T') with S' subseteq S and T' subseteq T; hence a cell m
   can appear in the weight-at-most-w block only if sum(m) <= 2w. For
   w = 2 the weight-at-most-2 block of K in the W basis therefore sees
   exactly the cells with sum(m) <= 4, and no other cell, at every k.
   Gated at k = 4: that criterion holds cell by cell over all 65 cells
   with no exception in either direction; the count is 34 present and 31
   absent; the general count sum_(a>=1, 2a+b<=4) C(k,a) C(k-a,b)
   evaluates to 15 at k = 3, reproducing the sealed k = 3 substrate, and
   to 34 at k = 4. The weight-at-most-2 block has 11 directions
   (empty, 4 singletons, 6 pairs).

B  ORBIT-TYPE RELEVANCE (exact witnesses, information lower bound)
   For an orbit type O, a RELEVANCE WITNESS is an exact pair of tables
   differing in exactly one cell of type O whose K inertias differ. Each
   witness proves that no decision procedure may discard type O. Gated:
   the set of the ten orbit types for which a witness is found within the
   frozen search of Field 3, reported exactly, with the tables printed as
   65-bit patterns. No claim of irrelevance is made for a type without a
   witness; absence of a witness is recorded as open.

C  LINEAR INSUFFICIENCY (exact witness)
   A LINEAR COLLISION is an exact pair of tables with identical ten
   `S_4` orbit sums and different K inertia. Such a pair is produced by
   construction: flipping one cell of type O from +1 to -1 and another
   cell of the same type from -1 to +1 preserves every orbit sum
   identically. Gated: whether such a pair exists in the frozen search,
   and if so the pair, its common sum vector, and the two inertias.

D  QUADRATIC LAYER, EXPLORATORY ONLY
   The canonical quadratic layer of the sealed skeleton has 109 entries
   (10 orbit sums, 78 Gram pairings among the twelve [31] copies, 15
   among the five [22] copies, 6 among the three [211] copies; no
   circulation scalar exists at k = 4 because [1111] is absent). Gated:
   whether the frozen search contains a pair with identical 109-entry
   quadratic vector and different K inertia. A found pair FALSIFIES
   quadratic sufficiency at k = 4 and is reported as such. NOT finding
   one proves nothing and is reported as exactly that, with the searched
   count stated; no sufficiency claim may be derived from it, at any
   size of search.

E  REAL WITNESSES (exact arithmetic, no abstraction)
   The extremal quadruples with n <= 10^8 are enumerated exactly, their
   K inertia computed by two independent exact paths, and the balanced
   and failing counts reported. Separately: whether any odd prime s
   <= 20000 extends the k = 3 canonical falsifier {5, 101, 293} to an
   extremal quadruple, and if so the inertia of that quadruple. The
   count of extremal quadruples found is reported exactly whatever it is,
   including zero.
```

## Field 2. CODE

`verify_tm_hankel_k4_substrate_1.py`, written after this file is frozen
and its SHA-256 recorded. Python standard library only; exact integer and
Fraction arithmetic only; no float in any assertion; deterministic stdout;
no wall clock, no hostname, no machine identifier; run from its directory
with

```text
env -i PATH="$PATH" HOME="$HOME" LC_ALL=C LANG=C \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_tm_hankel_k4_substrate_1.py
```

Two platforms, byte-identical stdout required: Ubuntu 24.04 x86_64 and
Debian 13 aarch64. Inertia is computed by a fraction-free leading-minor
path with a characteristic-polynomial fallback, and every reported witness
is confirmed by both paths independently.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. The carrier is the divisor
lattice of odd squarefree integers, the binary digit word, and the finite
abstract cell tables.

The abstract search of gates B, C, D is a FINDING DEVICE, not evidence.
Its domain is frozen here, before any execution:

```text
seed family    x_0 = 1; x_(n+1) = (6364136223846793005 x_n + 1442695040888963407)
               mod 2^64, an exact integer recurrence with no library
               randomness; the n-th base table is the 65-bit pattern
               b_n = (x_(2n+1) mod 2^33) + 2^33 * (x_(2n+2) mod 2^32),
               bit j giving the sign of the j-th cell in code order,
               1 meaning -1.
base tables    b_0 .. b_1999, exactly 2000 tables.
structured     for each base table, the ten single-cell flips at the
               lexicographically first cell of each orbit type (gate B),
               and for each orbit type the sum-preserving double flip at
               the lexicographically first +1 cell and first -1 cell of
               that type when both exist (gate C, and the same pairs are
               tested for gate D).
seeded         additionally the all-plus table, the all-minus table, and
               the four tables obtained by embedding the k = 3 canonical
               falsifier pattern of 147965 = 5 . 101 . 293 on each
               3-subset of the four coordinates with the remaining cells
               set to +1.
```

If a gate fires inside this domain, the witness is exact and self
certifying and the search method is irrelevant to its validity. If a gate
does not fire, the result is "not found in the declared domain" and
nothing else.

## Field 4. SYSTEMATICS

```
S1  polarization: t(1) = -1 fixed; the opposite convention negates every
    sign table and swaps inertia components.
S2  scope: gate A is a derivation checked exhaustively over the 65 cells.
    Gates B, C, D quantify over the frozen finite domain of Field 3 only,
    never over the substrate; the word "exists" is used, never "every".
S3  independence: witnesses are confirmed by two exact inertia paths;
    gate A is checked against the sealed k = 3 substrate as a control,
    which must reproduce 15 present cells and the four absent types.
S4  contrast, not inheritance: k = 3 values appear only as printed
    controls. No k = 3 law is evaluated at k = 4 anywhere in this
    candidate.
```

## Field 5. FAILURE THRESHOLD

Zero tolerance on gate A: any cell violating the `sum(m) <= 4` criterion
in either direction, or a count other than 34 present and 31 absent, or a
k = 3 control other than 15, fires the candidate. Gates B, C, D, E cannot
fire the candidate by returning empty; they fire it if a reported witness
fails its independent recomputation, or if the two inertia paths disagree
anywhere. A defect in the verifier rather than in a gated claim is an
integrity STOP, archived with both hashes, and the candidate is dead under
this id. No threshold moves after this freeze.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Not claimed anywhere: any statement about zeta zeros,
the Riemann hypothesis, Weil positivity or explicit formulae; anything
about the infinite operator beyond finite compressions; any J coupling,
p = 5 selection, physical reading, or L2-L6 lift; any census, sufficiency,
or universal statement over the k = 4 substrate; any inheritance of the
k = 3 two-scalar law or quadratic sufficiency. The output of this
candidate is a record, and at most a later promotion proposal, never a
registry row.
