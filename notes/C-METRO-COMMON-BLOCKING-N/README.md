# METRO-REDUCTION-CALCULUS, obligation D: common q^k blocking

- **Working item:** C-METRO-COMMON-BLOCKING-N
- **Owner item:** METRO-REDUCTION-CALCULUS [O], obligation D only
- **Author:** A. M. Thorn, drafted with an AI agent session
- **Date:** 22 September 2026
- **Scope:** PUBLIC, NON-CANONICAL; no authority. The row stays O and STOP.
- **Scientific ceiling:** candidate-T for the written statements D1 to D3 and
  L0; candidate-C for the census. L5 only.

Basis: Public Canon v91, section 15, `main = canon-v91 = 11b66d4`,
`canon/SHA256SUMS` 5 of 5 OK.

The preregistration (`PREREG.md`) and the verifier (`verify.py`) were hashed
before their first execution in a non-public incubation record. They are
reproduced here byte for byte. The intended public route is a probe,
P-METRO-COMMON-BLOCKING-1, pinned from these same verifier bytes with a
known-result disclosure.

## Result

```text
RESULT PASS, FAILURES 0 (none of the falsifiers F1 to F5 fired)
break check: BREAK_RESULT PASS
```

The candidate decides blocking inside the declared encoding family ENC4 (MSD or LSD
digit order; empty word or "0" for zero), with one block length k for every
coordinate:

Here "commuting" means cross-coordinate commutation only:
`delta_(i,u) delta_(j,v) = delta_(j,v) delta_(i,u)` whenever `i != j`.
Digit maps within the same coordinate need not commute. Every commutation
statement below and the census use this convention.

```text
D1  Blk_k is an admitted arrow of section 15 exactly when Pre_blk(P,k) holds,
    and a finite automaton decides Pre_blk exactly.
D2  Under Pre_blk the whole stream family over allowed starts is transported,
    so every decision and terminal value that is a function of it, in
    particular Adm_direct and its terminal L, is unchanged. Blk_k maps
    commuting tuples to commuting tuples.
D3  The augmented MSD blocking Blk#_k (one flag bit per coordinate) is exact
    with no precondition and preserves commutation.
```

The unconditional rule admitting every same-carrier blocking is invalid.
Individual same-carrier instances satisfying `Pre_blk` remain admissible:

- **W-D1** breaks the pointwise stream. With `q = 2`, `a = 1`, swap/identity
  digit maps, MSD-E0 and `k = 2`, `Stream_P(0,1) = 0` but
  `Stream_Blk(0,1) = 1`.
- **W-D2** is a commuting tuple (inside `C_dim`) whose box averages
  alternate `(0,1)`, `(1,0)`, so it is INADMISSIBLE. After `Blk_2` it becomes
  `ADMISSIBLE(PROBABILITY(1,0))`.

The proposed unconditional rule would purport to admit a map that changes
a frozen decision. The witnesses reject that proposed rule; they do not
fire the negative clause of the unchanged registered parent, whose four
arrows do not yet include blocking. The candidate admissible construction
must carry `Pre_blk` or, for MSD only, the augmentation. This is a proposal
for obligation D, not a public closure or an amendment of the four
currently registered arrows.

## Written arguments

**L0, flattening.** Take the super-digits of `enc_(q^k)(n)`, each written as
its length-k base-q word with zeros kept. Their concatenation is
`0^rho enc_q(n)` under MSD and `enc_q(n) 0^rho` under LSD, with
`rho = (-|enc_q(n)|) mod k`. For zero under Z0, `enc_(q^k)(0) = "0"` gives
`0^k = 0^(k-1) "0"`. Under E0 both sides are empty.

**D1.** By L0 the blocked run on input `n` is the unblocked run on the padded
words. `Pairs_i` is built from exactly those two runs taken jointly.
Coordinate `i` is advanced by `D_i(pad(v))` on the blocked side and `D_i(v)`
on the unblocked side, over all canonical words `v`. The padding depends on
`v` only through `|v| mod k`, and canonicity is a regular constraint. The
joint reachable set is therefore computed exactly by a finite search over
`(x, y, rho, |v| mod k, prefix flag)`, and
`Pairs_a = {(state_Blk(s,n), state_P(s,n))}`. `Pre_blk` says that `w` agrees
on every such pair, which is pointwise stream intertwining for every allowed
start and every input.

**D2.** The decision of section 15 is a function of the stream family, so it
is transported. Each blocked map `Delta_(i,U) = D_i(word_k(U))` is a
composition of the maps of coordinate `i`. If the maps of different
coordinates commute, so do these compositions.

**D3.** The flag `f_i` records whether coordinate `i` has started. While
`f_i = 0`, the first super-digit acts by its word with the leading zeros
stripped. Under MSD that reproduces the canonical `enc_q(n_i)` exactly: under
Z0, zero gives "0", and under E0 zero gives no letters and the flag stays 0.
Every later super-digit acts by its full word. Induction on the super-digits
gives `state_Blk#((s,0),n) = (state_P(s,n), f(n))`. Different coordinates act
on different flag bits through commuting maps.

**W-D2, all-m argument.** The start is `e`, both first-coordinate digit maps
are the transposition of `e,o`, and both second-coordinate maps are identity.
Every integer `n_1` in `[2^m, 2^(m+1))` has exactly `m+1` binary digits.
Thus every point in `R((2^m,0),(2^m,2^m))` has state `e` for odd `m` and
state `o` for even `m`, independently of `n_2`. The normalized box averages
are exactly `(1,0)` and `(0,1)` respectively, for every integer `m >= 0`.
The subsequences of arbitrarily large translated boxes therefore have
different limits, violating the required uniform translated-box convergence.
Each first-coordinate two-digit blocked map is two swaps, hence identity;
every second-coordinate blocked map is also identity. The blocked stream
is consequently constant `(1,0)` on every input and every box, which proves
its admissibility and terminal value. The finite verifier checks `m=2..8`;
it audits this all-m argument rather than proving infinite alternation.

## Census (candidate-C, finite range)

Box B1: `q = 2`, `a = 1`, `S = {0,1,2}`, `A0 = S`, all digit maps and all
binary outputs, 5832 tuples. Box B2: `q = 2`, `a = 2`, `S = {0,1}`,
`A0 = {0}`, 1024 tuples, of which 232 are commuting.

| box | convention | k = 2, Pre_blk true | k = 3, Pre_blk true |
|---|---|---|---|
| B1 | MSD-E0 | 2964 | 2940 |
| B1 | MSD-Z0 | 2532 | 2832 |
| B1 | LSD-E0 | 2736 | 2628 |
| B1 | LSD-Z0 | 2592 | 2604 |
| B2 | MSD-E0 | 768 (190 commuting) | 768 (190) |
| B2 | MSD-Z0 | 740 (186) | 804 (194) |
| B2 | LSD-E0 | 604 (170) | 604 (170) |
| B2 | LSD-Z0 | 642 (174) | 642 (174) |

Break check (`break_check_pairs.py`) on both boxes: 5832 plus 2048
tuple-convention-k cases, 0 mismatches. The automaton pair set equals the
realized pair set. Every realized pair lies in it (brute force below a
horizon), and every automaton pair is realized by an explicit input.

## Owner decisions a fold would need

```text
O-D1  confirm ENC4 and the reading "one k for every coordinate"
O-D2  admit Blk_k under Pre_blk for ENC4 and Blk#_k for MSD only as the
      proposed fifth arrow's two explicitly scoped constructions
O-D3  forbid the unconditional rule that admits every same-carrier
      blocking, witnessed by W-D1 and W-D2; retain individual instances
      satisfying Pre_blk, and supply the new entry's exact scope and
      witnesses if extending obligation B's catalogue
```

The LSD augmented construction is out of scope. For LSD only `Pre_blk` is
decided.

These are recommended owner decisions for a later public procedure and
fold. This note adopts no registry change. Any formal public probe must
disclose the known incubation and review outputs before its pin; importing
these files is not a formal public run.

## Files

```text
PREREG.md             8927801241e9d80b1a226dcde8eb5f362ace8abe3535bb0be6cc961e17da2feb
verify.py             01cc83c7ee605793eac5388db2af43538388590a192025f5a04589c910a888a5
STDOUT.txt            17233b6b7f04af2c2e76836c22213615c666588f3ecedfcf0d894d6cbf684134
break_check_pairs.py  cd51f53923ee683318206cf1675ba0b9a6ab8edf619e6f731f043c3e41ad2eed
BREAK_STDOUT.txt      70e223c12de02fdb5f067b60e58e4f7fd75c127f2c662eae8f33285a547e0d07
```

`break_check_pairs.py` differs from the incubation copy only in its import
line, which now points at its own directory. Its output is unchanged.

`verify.py` uses the Python standard library only, with integers and
`fractions.Fraction` and no float. Run from any directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 verify.py
```

The supplied incubation record reports byte-identical `STDOUT.txt` on three
runs:

- x86_64, Python 3.11, about 55 s (two runs);
- aarch64, Python 3.12, 24 s.

This is well inside the 120 s public budget.

An additional pre-publication review reports the same 2099-byte stdout on
Linux x86_64, Python 3.13.5, exit 0 and empty stderr. It also reproduced
`BREAK_STDOUT.txt` (130 bytes). These are disclosed non-canonical replays,
not public two-architecture gate records or blind independent confirmation.
The frozen preregistration, verifier, break checker and both stdout files
are unchanged by this publication review.
