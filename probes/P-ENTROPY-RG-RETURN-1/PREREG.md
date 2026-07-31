# P-ENTROPY-RG-RETURN-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete finite decision surface for the
fixed-point tower of the renormalized block maps of the driven kernel: the
scales that carry a fixed state, the exact identity of the fixed sets, the
multiplier at every fixed state, and the arithmetic clock those scales obey.
It contains no formal gate output and earns no scientific status. Formal
execution is forbidden until this document and the accepted verifier are
committed, pushed, and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-RG-RETURN-1
public lock:      branch probe/P-ENTROPY-RG-RETURN-1 is the claim of record
                  for this session; no public issue could be opened from the
                  session that authored this probe, so the branch push is the
                  collision claim and an issue is left to the repository owner
owner:            A. M. Thorn
branch:           probe/P-ENTROPY-RG-RETURN-1
path:             probes/P-ENTROPY-RG-RETURN-1/
action layer:     L5 finite kernel structure; no L6 measure lift; no lift
                  of any kind is named
scientific state: candidate finite C facts only; no live H or O row of the
                  registry closes, moves, or is touched by this probe
```

The authority base is Public Canon v28, tag `canon-v28`, content commit
`86a046007f89a64a696d013112a44f02e624dd2e`, Canon SHA-256
`4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c`,
Canon byte count 154316, `canon/SHA256SUMS` verified 5 of 5 OK against a
fresh clone of `main` at `3161cbc764f547c95a80c3bd5028acf71c2ef524`.
The completed public probes P-ENTROPY-BRIDGE-2, P-ENTROPY-BRIDGE-3 and
P-ENTROPY-MIRROR-1 are inputs by reference. This verifier independently
rebuilds every object it needs and imports nothing.

## Why this probe exists

`ENTROPY-BLOCK-HALVING [C]` establishes that the renormalized block maps are
exactly two-to-one on the recurrent core: coarse graining here is
irreversible, so the block maps form a semigroup rather than a group. A
coarse-graining semigroup is normally read through its fixed points and the
spectrum of its linearization there. The public registry carries no such row.
This probe supplies the missing finite object, and the answer is not the
expected one: outside two exceptional scales the block maps have no fixed
state at all, and where fixed states exist their linearization is the
identity, so no expanding or contracting datum exists to be read.

## Definitions frozen before execution

The public `F_5^6` kernel, its five involutive affine generators with the
public constants

```text
S_VEC = (2,1,2,1)   U_VEC = (0,1,0,-1)
C_D   = (2,1,3,4,1,1)   V_E = (0,0,0,0,1,0)
```

the selector `i = (z_6(psi) + 2 theta) mod 5` with
`z_6(psi) = sum_k psi_k mod 5`, the branch maps `F_0, F_1`, and the
Thue-Morse driver `theta_n = s_2(n) mod 2`. States are encoded base five in
the coordinate order `(p1, p4, p1', p4', q, r)`.

Rebuild the recurrent components by the public warmup-400 window-300 census.
Let `R` be the recurrent support and let the living halves be

```text
H_eps = Im(F_eps | R),   eps in {0,1}.
```

Composition is read right to left. The level-`k` block maps are

```text
Phi^(0)_eps   = F_eps,
Phi^(k+1)_eps = Phi^(k)_(1-eps) o Phi^(k)_eps,
```

equivalently the composition along the Thue-Morse substitution word
`subst^k(eps)` with the first letter applied first.

Every generator is affine with a state-independent linear part `L_g`. Along
the `2^k` substeps of `Phi^(k)_eps` starting at `x`, the multiplier is the
ordered product

```text
M_k^eps(x) = L_(g_m) ... L_(g_2) L_(g_1),    g_1 the first substep,
```

equivalently the chain rule
`M_(k+1)^eps(x) = M_k^(1-eps)(Phi^(k)_eps(x)) . M_k^eps(x)`. The spectrum is
reported as the characteristic polynomial `det(xI - M)` over `F_5`, monic of
degree six, printed as the coefficient tuple `c0..c6` low degree first.

Fixed states are counted on `R`. Fixed states of the same map lying outside
`R` are counted separately and reported as the off-core count; both counts
are gated.

The scale range is `k = 0..14`, both letters. That is four complete periods
of the structure claimed below and one scale beyond.

## Frozen claims and gates

Carrier audit. A failure here is a STOP, not a result: it would mean the
basis or the implementation is wrong, and nothing below would be evaluable.

```text
G01 CENSUS      the recurrent core has 6250 states on 313 components, 312 of
                size 20 and one of size 10, pairwise disjoint
G02 HALVES      H_0 and H_1 are disjoint, 3125 states each, their union is
                the core, and each F_t maps the core into the core
G03 AFFINE      every generator equals its linear part plus its constant on
                all 15625 states, exhaustively
G04 LINPARTS    every linear part is an involution of determinant 1
G05 CHARPOLY    the characteristic polynomial routine reproduces a frozen
                companion sextic, (x - 1)^6 at the identity, and (x + 1)^6
                at minus the identity
G06 WORD        the doubling recursion equals the literal substitution-word
                composition for k = 0..6, both letters
G07 MULTWALK    the multiplier recursion equals the literal ordered substep
                product at the first ten fixed states of each (k, eps) with
                k = 0..8
G08 HALVING     the image of the level-k block map on the core has exactly
                3125 states for every k = 0..14 and both letters
```

Science gates. A failure here is a fired falsifier: first class, merged, and
never repaired by moving a threshold.

```text
G09 K0-CENTRES  at k = 0 each letter has exactly one fixed state on the
                core; for eps = 0 it is 3 (C_D + V_E) = (1,3,4,2,1,3) and
                for eps = 1 it is 3 C_D = (1,3,4,2,3,3); both lie in the
                size-10 component; each has exactly 125 fixed states off the
                core; the multiplier at each is exactly minus the identity,
                characteristic polynomial (x + 1)^6; and no state of F_5^6
                is fixed by both letters
G10 RETURN      at every scale k = 1 mod 4 in range, that is k = 1, 5, 9, 13,
                the fixed set of Phi^(k)_eps is exactly the opposite living
                half H_(1-eps), 3125 states meeting all 313 components, the
                multiplier at every one of them is exactly the identity with
                characteristic polynomial (x - 1)^6, and the off-core fixed
                count is 3125 at k = 1 and 0 at k = 5, 9, 13
G11 EMPTY       at every remaining scale k = 2..14, that is every k with
                k mod 4 in {0, 2, 3} and k > 0, the block map has no fixed
                state on the core and none off it
G12 HALF-LAW    every fixed state lies in the half H_(eps xor (k mod 2)),
                for every k = 0..14 and both letters
G13 CLOCK       the scales carrying a full-half return are exactly the
                scales whose block length satisfies 2^k = 2 mod 5, namely
                k = 1, 5, 9, 13; the scales with 2^k = 1 mod 5, namely
                k = 0, 4, 8, 12, carry no full-half return
```

The only multiplier matrices realized at any fixed state in the whole range
are the identity and its negative. This is printed as a measurement and is
implied by G09 and G10 together.

## Six frozen preregistration fields

```text
equation:     gates G01 to G13 exactly as stated above, on the declared
              carrier, at the declared scales, with the declared conventions.

code:         verify.py in this directory. Python 3 standard library only;
              exact integer arithmetic over F_5 and over Z; no float appears
              anywhere in the file; one process; no filesystem writes; no
              network; deterministic output independent of hash seed,
              architecture, and interpreter minor version; target runtime
              under 120 s.

carrier:      the public F_5^6 kernel constants above, the Thue-Morse driver
              on a 1024-tick prefix, the warmup-400 window-300 recurrent
              census, and the dyadic scales k = 0..14. No external data, no
              file is read, every object is rebuilt inside the verifier.

systematics:  1. the composition convention is frozen above, word order with
                 the first letter applied first, and the multiplier order is
                 the matching chain rule; the opposite convention was tested
                 in the disclosed pre-pin development and returns the same
                 tower with the two letters exchanged at odd k, so no gate
                 here is convention-dependent in substance;
              2. fixed states are counted on the core and off it separately
                 and both counts are gated, so no count can hide in the
                 complement;
              3. the multiplier is a linear datum only; the block maps are
                 affine, and no statement about their affine part beyond the
                 fixed-state condition is made or implied;
              4. matrix products are memoized for speed only; every reported
                 object is exact and memoization cannot change a value;
              5. G03 is exhaustive over all 15625 states rather than sampled;
              6. the range is finite by construction; nothing here asserts
                 any behaviour at k > 14.

failure
threshold:    any gate FAIL. Every comparison is exact. No tolerance, no
              adaptive range, scale, component, or convention is permitted.
              A carrier-audit failure (G01 to G08) is a STOP and the probe
              records it as such. A science-gate failure (G09 to G13) is a
              fired falsifier, recorded and merged, and the threshold is not
              moved afterwards.

action layer: L5 finite kernel structure. A passing two-architecture run can
              earn C for this declared carrier and this declared range and
              nothing else. It cannot promote any open row, and it licenses
              no lift.
```

## Falsifier map

A census, half, disjointness or containment mismatch fires G01 or G02. A
non-affine generator, a non-involutive or non-unimodular linear part, or a
characteristic-polynomial self-test failure fires G03 to G05. A disagreement
between the doubling recursion and the literal word, or between the
multiplier recursion and the literal substep product, fires G06 or G07. An
image other than 3125 at any scale fires G08. A wrong count, wrong state,
wrong component, wrong off-core count, wrong multiplier, or a state fixed by
both letters at k = 0 fires G09. A return scale whose fixed set is not
exactly the opposite living half, or which contains one non-identity
multiplier, or whose off-core count differs from the frozen value, fires
G10. Any fixed state at any scale with k mod 4 in {0, 2, 3} and k > 0 fires
G11. A fixed state outside its declared half fires G12. A nonempty scale
outside the residue class 2^k = 2 mod 5, or a full-half return at a scale
with 2^k = 1 mod 5, fires G13. Every fired result is retained and merged.

## Environment and formal execution

```text
cd <repository root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-RG-RETURN-1/verify.py
```

The first formal run occurs only after the remote preregistration pin is read
back. It runs on a neutral Ubuntu 24.04 Linux environment on aarch64. Its
exact stdout becomes `EXPECTED.txt`; `RUN.md` records the neutral platform
and architecture fields with the pin and file hashes and never a machine
nickname. The required check then reruns the pinned verifier on GitHub
`ubuntu-latest` x86_64 and compares hashes and exact bytes. Because the two
legs are different architectures, byte-identical output satisfies the
two-architecture computation gate; the resulting claim is nevertheless a
computation and stays at `C`. `RESULT.md` is added only after the formal
record exists. The registry, frontier and Canon are not edited by this probe.

## Pre-pin development disclosure

This preregistration is not a blind prediction and does not present itself as
one. The structure it freezes was found in an incubation candidate,
`C-RG-FIXEDPOINT-1`, dated 2026-07-31, which carries no public status, is not
evidence, and whose output is not copied into this probe. Disclosed in full:

```text
1  the incubation candidate preregistered the opposite hypothesis, that the
   block maps have a nonempty fixed set at every scale k = 0..12. That
   hypothesis was FALSIFIED by its own pinned run. The falsification stands,
   was archived rather than repaired, and is the reason the present gates are
   written around emptiness instead of existence. No threshold was moved:
   the present document is a new freeze of a different statement, not a
   relaxation of the old one.
2  the candidate lane ran one independent break pass with a separately
   written engine, literal per-state walks, numeric multiplier columns, and
   the opposite composition convention. It found no divergence.
3  the candidate range was k = 0..12; the break pass reached k = 14 for the
   core counts only, and a further non-formal pre-pin computation supplied
   the off-core counts and multiplier spectra at k = 13 and 14. The range
   k = 0..14 frozen here is therefore fully known to the author in advance.
4  the exact file pinned here as verify.py was executed once before the pin,
   non-formally, on x86_64, to establish that it compiles, exits zero,
   writes no stderr, and completes well inside the runtime budget. That run
   carries no public status and its stdout is not copied into this probe.
```

What the public probe adds over the incubation lane, and the only thing it
claims to add: an immutable public pin of the exact statement, an exact
verifier any reader can run, a first formal execution on aarch64 after that
pin, and an independent rerun on x86_64 by the required check, with
byte-identical stdout. That, and not the discovery, is what earns the status.

## Out of scope, explicitly

- no continuum limit, scaling limit, or critical exponent of any kind;
- no monotone function of scale, no C-function, no positivity statement;
- no measure, no L6 statement, no ergodic or almost-everywhere claim;
- no all-scale law: every statement is bounded by k <= 14 by construction;
- no periodic-point census beyond fixed points;
- no physical reading of the residue class 2^k mod 5 and no identification
  of it with any registered physical quantity; the coincidence with the
  order of the ramified digit unit is arithmetic and is stated as such;
- no claim about the affine part of the block maps;
- no registry, frontier, Canon, or release edit in this probe.

Any one of those requires a separate public proof, probe, or later fold.
