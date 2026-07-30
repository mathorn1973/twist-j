# Entropy recon status at Public Canon v28

```text
STATUS:      NON-CANONICAL ANALYSIS NOTE
AUTHORITY:   none
PUBLIC BASIS: Public Canon v28
MAIN:        3161cbc764f547c95a80c3bd5028acf71c2ef524
TAG:         canon-v28
CONTENT:     86a046007f89a64a696d013112a44f02e624dd2e
CANON SHA:   4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
CANON BYTES: 154316
RECON MERGE: 39d9a88f3249310ed33df3f2a1172ef169456ead
```

This note supersedes the authority sentence and the final work-list reading of
`notes/ENTROPY-SELECTION-RECON.md`. It does not replace that note's exact finite
results, source and target implementations, or scope fences.

## 1. Public inputs now in force

The current public rows relevant to this lane are:

```text
ENTROPY-LIVING-SET       C
ENTROPY-MIRROR-LAW       C
ENTROPY-COUNT-MATCH      C
ENTROPY-LAYER-BRIDGE     O / STOP
COLOR-TORSOR-HOLONOMY    T
```

`P-ENTROPY-LAW-REDUCTION-1` is merged on public `main`. Inside the exactly
equivariant Route A class it proves, proof-first,

```text
Law_W(P)  <=>  P_* mu = Uniform(R).
```

It constructs no map and leaves `ENTROPY-LAYER-BRIDGE [O]` open. Negative
closure of that row still requires the complete theorem `A_A = empty`.

## 2. Exact finite state of the recon

The fixed-`F_2`, fixed-`r=2` cell-sector finite horizons are closed through
`2..7`:

```text
2..4   417/1250
2..5   1459/2500
2..6   5939/7500
2..7   6877/7500
```

At horizon `2..7` the exact ordinary and special costs at scale 48 are

```text
ordinary = 220
special  = 260
624*220 + 260 = 137540
137540/150000 = 6877/7500.
```

The ordinary lower certificate has 1181 nodes: 236 branch nodes, 190 exact
rational-dual leaves, and 755 exact Hall-infeasible leaves. These numbers are
certified by the live replay and the notes, not by incidental integer strings
inside the JSON certificate files.

The exact prefix-tree dichotomy is also closed inside this declared ansatz:

```text
sup_H o_H < infinity
    <=>
there exists a compatible chain with sum_r d_r < infinity.
```

The transition-local kill shot is falsified. The isolated transitions
`4->5`, `5->6`, and `6->7` have zero nontrivial holonomy and each admits a
zero-cost potential. Any divergence proof must use a global capacity dual or
bands reaching far enough backward to include inherited levels and anchor
capacity.

## 3. Corrections binding all successor work

### 3.1 The source count 629 is scoped to `r >= 2`

For a constant cycle of length `m` at substitution level `r`, the component
count on the dyadic factor is

```text
gcd(2^r,m) = 2^min(r,v_2(m)).
```

For the source orbit spectrum `1^1 4^1 20^156`,

```text
c_source(r) = 1 + gcd(2^r,4) + 156*gcd(2^r,20)
            = 158   at r=0
            = 315   at r=1
            = 629   at every r>=2.
```

The recon carrier starts at `r=2`, so 629 is valid on the whole declared
range. Every successor statement must state `r >= 2` explicitly.

### 3.2 The target is 312 separate torsors

`COLOR-TORSOR-HOLONOMY [T]` says that each of the 312 generic attractor halves
is separately a free `D_5` torsor of ten points. The singlet half is the five
reflection axes, isomorphic as a `D_5`-set to `D_5/C_2`.

The target half is therefore

```text
312 copies of the regular D_5-set  disjoint union  D_5/C_2,
312*10 + 5 = 3125.
```

No 312-point object is called a torsor.

### 3.3 Uniform pushforward is conditional, not automatic from equivariance

Exact equivariance alone forces the output sheet and reduces `Law_W`; it does
not force `P_*mu = Uniform(R)`.

For the depth-five fiberwise-bijective ansatz, uniform pushforward follows only
after both of these facts are proved:

1. normalized Haar probability on `O_(K,lambda)` pushes through
   `pi_5: O_(K,lambda) -> O/lambda^5` to uniform probability on the 3125
   cosets;
2. for almost every `kappa`, the fiber map
   `B_kappa: O/lambda^5 -> H_(kappa_-1)` is a bijection.

The Haar clause has a short proof: translations act transitively on the finite
cosets and normalized Haar assigns equal mass to translates, hence each coset
has mass `1/3125`. Together with the Thue-Morse one-letter masses `1/2,1/2`, a
fiberwise bijection then gives mass `(1/2)(1/3125)=1/6250` to every recurrent
state. The two clauses must remain visible in any preregistration.

### 3.4 One common cocycle is load bearing

The proposed Mackey obstruction compares two representations of one common
`D_5` cocycle. A block-dependent Mackey subgroup changes the problem.

For one subgroup `M <= D_5`, the numbers of `M`-orbits are:

```text
M       regular D_5-set   D_5/C_2   total over target half
D_5             1             1       313
C_5             2             1       625
C_2             5             3       1563
{1}            10             5       3125
```

All eight subgroups are covered: `D_5`, `C_5`, five conjugate reflection
subgroups `C_2`, and the trivial subgroup. The five `C_2` subgroups have the
same orbit counts but must still be enumerated individually.

The mixed equation

```text
312*a + b = 629,
a in {1,2,5,10}, b in {1,3,5}
```

has the unique solution `(a,b)=(2,5)`. It requires `C_5` on the generic
regular blocks and the trivial subgroup on the singlet. One common Mackey
range cannot realize that pair. This is the exact point to prove or break.

## 4. Current work list

The old final list in `ENTROPY-SELECTION-RECON.md` is stale after horizon 7.
The current list is:

1. **Open:** record explicit closed-walk obstruction certificates rather than
   only propagation consistency failures.
2. **Closed at finite scope:** exact horizons `2..4` through `2..7`.
3. **Open:** collars with radius beyond the fixed `r=2` ansatz. The current
   dichotomy decides no `r>2` collar class.
4. **Open:** orbit counting, transfer equivalence, and canonicity under a
   frozen admissible gauge.
5. **Open:** regularity and the full pushforward theorem.
6. **Open contracts:** transfer-family equivalence, regularity class and
   quantifier, and unambiguous living-fiber notation `L_kappa`.
7. **Open, and carrying no breaker credit:** `C-ENTROPY-MACKEY-OBSTRUCTION-4-N`
   was preregistered, run by the primary route, and attacked by an
   independently authored frozen breaker. That breaker is now
   **RETIRED IN FULL** by owner ruling; see
   `OWNER-RULING-BREAKER-MACKEY4-1.md` and the adjudication in
   `MACKEY4-BREAKER-RESULT.md`. Its outputs keep discovery-history and
   diagnostic value and are not declared false, but they earn zero breaker
   credit. Every load-bearing value of the candidate therefore rests on the
   primary route alone until a live successor instrument re-establishes it.
8. **Open, and load bearing:** the common-cocycle premise of that candidate.
   Breaker gate `B13` was shown to have no discriminating power: it reports a
   common cocycle on a synthetic target built to have none, because its
   marking is per component. `S7` and `F6` therefore rest on the primary's
   `T02` alone. The successor gate is preregistered and frozen:

   ```text
   PREREG-BREAKER-MACKEY4-2.md
   sha256 45192f7fcbe3b1699f69ccd35351c8a8ddc756e488a2f01ee0d0491e197f03e6
   14504 bytes, frozen 2026-07-30, instrument mackey4_cocycle.py absent
   ```

   It requires one global `D_5` given as explicit permutations of the
   recurrent core, prior to and independent of any component, a gauge set
   declared before the run, and three mandatory synthetic controls that the
   gate must reject, reject, and accept respectively. The session that wrote
   that preregistration is disqualified from implementing it.
9. **Settled by owner ruling, 2026-07-30:** `PREREG-BREAKER-MACKEY4-1` is
   retired in full, not only `E9`. The frozen clause retires the breaker id,
   no severability for individual gates was frozen, and confining the
   retirement to `E9` would introduce severability after the result was known.
   `PREREG-BREAKER-MACKEY4-2` is the sole live successor instrument and is not
   amended by the ruling. Recorded in `OWNER-RULING-BREAKER-MACKEY4-1.md`.
10. **Open, and newly load bearing:** full retirement leaves the entire source
    side without a live instrument. `PREREG-BREAKER-MACKEY4-2` is scoped to
    the target; it re-establishes `E4`, `E6`, `E7`, `E8`, `E9`, and the menu
    `E10-E12`, but not `E1`, `E2`, `E3`, `E5` or `E13`. After that successor
    runs, `629` at `r >= 2` still rests on the primary route alone while the
    menu rests on two. Closing that half of the obstruction needs a companion
    preregistration under its own identifier, scoped to `E1`, `E2`, `E3`,
    `E5`, `E13`, with a source presentation distinct from the primary's
    lambda-digit arithmetic. It is disjoint from item 8 and may run in
    parallel. Not yet opened.
11. **Next attack:** run item 8, open and run item 10, then extend the finite
    horizon.

No item above closes the public entropy bridge. No finite restricted no-go is
silently promoted to `A_A = empty`.
