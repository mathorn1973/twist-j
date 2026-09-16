# J is not a Weil number: the golden scale, the Gauss weight, and the Carlitz rank-one wall

```text
STATUS       NON-CANONICAL note; no status motion; no Registry row; no Canon fold;
             no verifier permission; no probe opened
BASIS        Public Canon v87, tag canon-v87, main fd512f50d90382124e7c00afa926c8083fd56e06
CONTENT      41c8d4229b71437f09957d959975dc1772e95806
CANON.md     sha256 a2517c6d8efb1969a7258f94d9874cca3b5b9beb1aecdfd2e39b56f33961a917, 634207 bytes
SHA256SUMS   5 of 5 OK at the basis above
DATE         2026-09-16
LAYER        L1 exact algebra in Q(zeta_5) and F_q[t], plus three labeled imports;
             no L2 to L6 lift, no physical reading, no SI quantity
COMPUTATION  notes/J-WEIL-WEIGHT-AND-CARLITZ-RANK-2026-09-16.check.py, 21/21 PASS,
             byte-identical stdout on x86_64 and arm64, audit input only (see section 1)
ISSUE LOCK   none; a note only
LABELS       every fact below is candidate-T inside a NON-CANONICAL note; no public
             T is claimed or created
REVISION     rev2, 2026-09-16, after owner review of PR #1022; the five corrections
             are listed in section 11; the check script and its pins are unchanged
```

## 1. What this note is and is not

This note records four exact facts and one review comment. All four facts
are elementary; three of them are new to this repository as statements, one is
already recorded in prior notes and is quoted only because the others rest on
it. Every fact carries the label candidate-T and lives in a NON-CANONICAL
note; nothing here is a public T.

It is not a probe. The arithmetic below was performed in conversation before
any preregistration, so under POLICY section 3 it cannot be pinned under any
identifier used here. A successor may preregister `P-J-WEIL-WEIGHT-1` fresh,
with the falsifiers of section 8, and would then own the computation-grade
record. The attached script is an audit input, not evidence.

No RH progress is claimed anywhere in this note. Section 6 says what the facts
mean for the RH lanes, and it is entirely negative.

## 2. Collision scan and what is already held

Remote heads, `probes/`, `canon/REGISTRY.tsv` and `notes/` were scanned at the
basis above.

Already in the Canon:

- `J-PROJECTIONS [T]`: `|J| = 1/phi`, `arg J = 2 pi/5` in the principal
  embedding.
- `ALPHA-PREFACTOR-UNIFICATION [T]`: the Gauss sum
  `tau = zeta - zeta^2 - zeta^3 + zeta^4 = 2 phi - 1 = sqrt5`, `tau^2 = 5`.
- `CYCLOTOMIC-CLASS-NUMBER-ONE [T]`, `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]`
  (total ramification locus of full quartic cyclotomic fields is exactly
  `{(K_5,5),(K_8,2)}`), `AXIOM-PROJECTION-DICTIONARY [D]`,
  `PENTAGON-NORMALIZATION [T]` (a normalization identity, not a Weil
  realization).

Already in notes: the moduli split `|sigma_a(J)| = phi^(-chi_5(a))` appears in
`notes/incubation-import-2026-08-21/C-SPLIT-UNIT/PREREG-C-SPLIT-UNIT-1_2026-08-01.md`
(gates E1, E2), in the audit of `notes/C-HERM2-BORN-CONE-1/`, and as gate Q10 of
`notes/C-CM-2I-QCARRIER-1/verify_cm_2i_qcarrier.py`. The GRH taxonomy for
`Q(zeta_5)` is in `notes/C-J-DEDEKIND-WEIL-ROAD-N.md`; the `zeta_F = zeta L(s,chi_5)`
reading for `F = Q(sqrt5)` is in `notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1/`. The
CM5 Hodge and Tate lane (`notes/HODGE-TATE-CM5-*`) works with Frobenius on a
CM abelian surface and does not state the Weil-weight classification below.

Unmerged and not touched by this note: `notes/rh-program-dependence-v87-2026-09-16`
(a Canon patch proposal fixing the program-level RH statement as the ordinary
RH for `zeta(s)`); section 7 is a comment on it, not an edit of it.

New here: the Weil-weight classification of the axiom data (section 4), the
Kronecker argument that a unit which is a Weil number must be a root of unity
(section 4), and the Carlitz rank-one census (section 5). No prior note,
probe or branch in this repository mentions Carlitz cyclotomic function
fields.

## 3. Fact 1: the conjugate moduli of J are the quadratic character

In `Z[zeta_5]`, with `chi_5` the quadratic character modulo 5,
`phi = -zeta^2 - zeta^3` and `phi^-1 = zeta + zeta^4`:

$$
\sigma_a(J) = \chi_5(a)\,\zeta^{a}\,\varphi^{-\chi_5(a)}, \qquad a = 1,2,3,4,
$$

$$
|\sigma_a(J)|^2 = \varphi^{-2\chi_5(a)} \in \{\,2-\varphi,\ 1+\varphi\,\} = \{\varphi^{-2},\ \varphi^{2}\}.
$$

Script gates A1 to A5. The first display is an identity in `Z[zeta_5]`, not a
numerical statement; the second is its norm to `Z[phi]`. The golden modulus of
`J` is therefore the quadratic character modulo 5 written multiplicatively.
This is the fact already held in the notes listed in section 2.

## 4. Fact 2: Weil weights of the axiom data

Import (definition). An algebraic integer `alpha` is a Weil `q`-number of
weight `w` if `|sigma(alpha)| = q^(w/2)` for every complex embedding `sigma`.

- The Gauss element `Gamma = zeta - zeta^2 - zeta^3 + zeta^4` satisfies
  `Gamma^2 = 5`, `sigma_b(Gamma) = chi_5(b) Gamma` and `|sigma_b(Gamma)|^2 = 5`
  for every `b`. It is a Weil 5-number of weight 1. Gates B1 to B3.
- Embedding by embedding, `sigma_a(J) = [chi_5(a) zeta^a] . [phi^(-chi_5(a))]`.
  The first factor has modulus 1 in every embedding and is a root of unity in
  `mu_10`; the second is the golden scale. Gate B4. This is a per-embedding
  factorization, equivalently the polar factorization in `K tensor R`, and
  not a factorization inside `K = Q(zeta_5)`: the quadruple
  `chi_5(a) zeta^a` is not the Galois orbit of any single element of `K`,
  since `sigma_2(zeta) = zeta^2` while the quadruple carries `-zeta^2`. No
  single global weight-0 factor in `K` is claimed.
- `J` itself is not a Weil `q`-number of any weight, for any `q`. Two proofs.
  (i) Its conjugate moduli take two values, gate A5. (ii) `N(J) = 1`, so a
  Weil weight would have to be 0, so all conjugates would have modulus 1, so
  by Kronecker's theorem (import) `J` would be a root of unity; but
  `J^k != 1` for `1 <= k <= 10` and the only roots of unity in `Q(zeta_5)`
  are `mu_10`. Gate B5, B6.

Consequence, stated at the level of the algebra only. `J` cannot serve
directly as a Frobenius eigenvalue of one pure weight, because its
conjugate moduli are not equal; `Gamma` can, with weight 1; the golden scale
is exactly the part whose log-modulus is the nonconstant character
`-chi_5(a) log phi`. The modulus projection of `AXIOM-PROJECTION-DICTIONARY [D]`
is that non-Weil part. This excludes one specific use of `J` (a pure-weight
eigenvalue) and nothing more; it does not exclude Frobenius or trace-formula
methods applied to other data of the program, and it is not a statement
about zeros.

## 5. Fact 3 and Fact 4: rank-one census in number fields and in Carlitz function fields

### 5.1 Number fields

Import (Dirichlet). The unit group of `Z[zeta_n]` has rank `phi(n)/2 - 1` for
`n >= 3`, torsion `mu_n` or `mu_2n`. The rank is 1 exactly when `phi(n) = 4`,
that is `n in {5, 8, 10, 12}`. Import (Hasse unit index; Washington,
Introduction to Cyclotomic Fields, chapter 4): the index
`Q = [E : mu E^+]` of the subgroup generated by roots of unity and real units
is 1 when `n` is a prime power and 2 otherwise. Hence the clean factorization
`unit = (root of unity) . (real fundamental unit)^k` holds for every unit
exactly at the prime-power conductors `5` and `8`; at `n = 12` it holds only
up to index 2, the unit `1 - zeta_12` being a witness (its square, not it,
is a root of unity times `2 - sqrt3`). The prime-power conductors of rank 1
are exactly `5` and `8`, in agreement with
`QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]`. The compositum
`Q(zeta_40)` of `Q(zeta_5)` and `Q(zeta_8)` has degree 16 and unit rank 7:
`J = zeta_5 phi^-1` keeps its single scale there, and so does every unit of
the two subfields, but the unit group as a whole needs seven independent
scales, so the reading "one phase, one scale" is not available for a general
unit of the compositum. Gates C1 to C4.

The reading "one phase, one scale" of every unit of the ring is therefore
available exactly at `n = 5` and `n = 8`, and at no cyclotomic field above
degree 4.

### 5.2 Carlitz cyclotomic function fields

Import (Hayes 1974; Rosen, Number Theory in Function Fields, chapter 12). For
`A = F_q[t]`, `K = F_q(t)` and `M in A` nonconstant, the `M`-th Carlitz
cyclotomic field `K(Lambda_M)` has degree `Phi(M) = |(A/M)^x|`, is geometric
(constant field `F_q`), and the infinite place of `K` splits in it into
`Phi(M)/(q-1)` places, each with ramification index `q - 1` and residue
degree 1. Hence, by the function-field Dirichlet theorem, the integral closure
of `A` in `K(Lambda_M)` has unit rank `Phi(M)/(q-1) - 1` and unit torsion
`F_q^x`.

Elementary census. Rank one means `Phi(M) = 2(q - 1)`. Every prime-power
factor of `M` contributes at least `q - 1` to `Phi(M)`, with equality only
for a linear prime to the first power, so:

- one prime factor `P^e` of degree `d`: `d >= 2` is impossible since
  `q^d - 1 > 2(q - 1)` for `q >= 2`; `d = 1` forces `q^(e-1) = 2`, so
  `q = 2`, `e = 2`;
- two prime factors: `(q-1)^2 <= 2(q-1)` forces `q <= 3`; `q = 3` gives
  `PQ` with both linear and simple; `q = 2` gives `P^2 Q` with exactly one
  extra factor of `q`;
- three or more prime factors: impossible (`F_2` has two linear primes,
  `F_3` gives `(q-1)^3 = 8 > 4`).

Complete list of rank-one Carlitz rungs:

```text
q = 2   M = t^2, (t+1)^2, t^2 (t+1), t (t+1)^2
q = 3   M = t (t+1), t (t+2), (t+1)(t+2)
q >= 4  none
```

Gate D1 enumerates the shapes for eleven values of `q`; gates D2 to D5
recompute `|(A/M)^x|` by a gcd count over every monic `M` of small degree
for `q = 2, 3, 5, 7` without using the multiplicative formula, an independent
code path; gate D6 lists `Phi(M)` for the four smallest shapes over `F_5`
(4, 20, 24, 16; never 8).

Consequence, at the level of the algebra only. Over `F_5`, the residue
characteristic of the program, there is no Carlitz cyclotomic ring of unit
rank one, and in every Carlitz cyclotomic ring the multiplicative torsion is
the constant field `F_q^x` while the Carlitz torsion `Lambda_M` is additive.
Within this class (Carlitz cyclotomic extensions of `F_q(t)`, integral
closure of `F_q[t]`, so `S = {infinity}`), the object "root of unity divided
by a single fundamental unit" that defines `J` in `Z[zeta_5]` (and its silver
sibling in `Z[zeta_8]`) has no counterpart at `q = 5`, and where a rank-one
rung exists (`q = 2`, `q = 3`) its phase is at most a sign. This is a
statement about the named class only; other base curves, larger `S`, or
Drinfeld modules of higher rank are not covered and may behave differently.
Inside the class, the wall between the carry world `Z` and the carry-free
world `F_q[t]`, named "genus" in the carry lane, has the sharper name "unit
rank and torsion type" on the side of units.

## 6. What this means for the RH lanes

Plain and negative.

1. Cyclotomic ascent does not help. `zeta_(Q(zeta_n))(s)` is the product of
   `L(s,chi*)` over the primitive characters `chi*` attached to the characters
   modulo `n`; the trivial character has conductor 1 and contributes `zeta(s)`
   itself (the imprimitive `L(s,chi_0 mod 5) = (1 - 5^-s) zeta(s)` is not the
   factor). Every floor above adds L-functions and never removes the Riemann
   zeta function. RH for `Q(zeta_5)` contains RH.
2. Among the axiom data, `Gamma` and the per-embedding phase admit a single
   Weil weight and `J` does not, so `J` itself is excluded as a pure-weight
   Frobenius eigenvalue. Section 4. This excludes that one role; it does not
   exclude Frobenius or trace-formula methods elsewhere in the program.
3. In the class of Carlitz cyclotomic extensions of `F_q(t)` the rank-one rung
   does not exist at `q = 5`. Section 5.2. Other function-field analogues are
   not covered.
4. The three walls already recorded in the RH lanes (Li and Toeplitz capacity,
   the Hankel detection ceiling, the Widder depth) are untouched.

Nothing here moves `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` or
`LAMBDA-COCYCLE-ANGLES [H]`.

## 7. Comment on the open RH-PROGRAM-DEPENDENCE proposal, rev2

The proposal `notes/canon/RH-PROGRAM-DEPENDENCE-PATCH-2026-09-16.md`
(PR #1021, branch `notes/rh-program-dependence-v87-2026-09-16`) resolves its
decision 1 as the ordinary RH for `zeta(s)` and nothing stronger.

Rev1 of this section said that any physical reading of `|J|` is "exposed to"
`L(s,chi_5)` and hence to `zeta_F`, `F = Q(sqrt5)`. That was an
over-statement and is withdrawn. What Fact 1 proves is that the conjugate
moduli of `J` are the character `chi_5` in exponential form. It does not prove
that any registered reading depends on the location of the zeros of
`L(s,chi_5)`, and `AXIOM-PROJECTION-DICTIONARY [D]` establishes no such
dependence.

The program's own arithmetic makes the distinction exact.
`J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]` gives, at formal Euler-factor
scope for `Re(s) > 1`,

$$
\frac{1}{\zeta(s)} = C_0(s)\,O_5(s), \qquad
C_0(s) = L(s,\chi_5)\,\frac{L(2s,\chi_5)}{\zeta(4s)}\,\frac{1-5^{-s}}{1-5^{-4s}},
$$

so `L(s,chi_5)` cancels in the product and survives only in the separate
split channel `O_5`, where its zeros appear as poles (this is the reading of
`notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1/`). Two targets therefore exist:
the ordinary RH controls the product, that is the full Moebius sum; RH for
`zeta_F` is the ordinary RH together with a hypothesis on the zeros of
`L(s,chi_5)`, and is needed only by a reading that consumes the separate
channel `O_5` rather than the product.

As far as the registry at Public Canon v87 shows, no registered row consumes
`O_5` separately: `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` bounds the
augmentation sum, which is the product, and the O5 cluster itself is
unregistered (PR #1021, section 4). Hence the ordinary RH is the correct
program-level condition, as PR #1021 proposes, and `zeta_F` remains a
separate research target. The exact test that would
change this: a registered row whose physical output is proved to depend on the
polar structure of `O_5` alone, not on `C_0 O_5`. Until such a row exists,
adding `L(s,chi_5)` to the program condition would be a further commitment
adopted by choice, not a derived necessity. This note proposes no row, no
edge and no wording, and edits no branch.

## 8. Falsifiers for a successor probe

If `P-J-WEIL-WEIGHT-1` is opened, with a fresh pin before any run:

```text
F1  some a in {1,2,3,4} with |sigma_a(J)|^2 not in {2 - phi, 1 + phi}   (Z[phi])
F2  some b in {1,2,3,4} with |sigma_b(Gamma)|^2 != 5                    (Z[phi])
F3  some k in 1..10 with J^k = 1                                        (Z[zeta_5])
F4  some monic M in F_5[t] with |(F_5[t]/M)^x| = 8                      (F_5[t])
```

Each is decided by exact arithmetic in the named ring. None involves a float,
a zero of any L-function, or a threshold.

## 9. Imports

- Dirichlet's unit theorem, number-field and function-field forms.
- Kronecker's theorem: an algebraic integer all of whose conjugates have
  modulus 1 is a root of unity.
- Hayes 1974, explicit class field theory for rational function fields;
  Rosen, Number Theory in Function Fields, chapter 12, for the splitting of
  the infinite place in `K(Lambda_M)`.
- The definition of a Weil `q`-number of weight `w`. That Gauss sums occur as
  Frobenius eigenvalues (Weil 1949) is background for section 4 and is not
  used in any gate.

## 10. Pins

```text
script   notes/J-WEIL-WEIGHT-AND-CARLITZ-RANK-2026-09-16.check.py
         sha256 1d681d9a384344f1f3a2560924adf636f4025ede059be36a7828bb5cfafe59e5, 11421 bytes
command  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
         python3 notes/J-WEIL-WEIGHT-AND-CARLITZ-RANK-2026-09-16.check.py
result   21/21 PASS, exit 0, stderr empty
stdout   sha256 9ab69d8a01a618e995110802617b487d8cf3324d8091888ad0fbe30c2b85782b, 2125 bytes
env      leg 1: Ubuntu 24.04, x86_64, CPython 3.12.3
         leg 2: macOS, arm64, CPython 3.9.6; stdout byte-identical to leg 1
         (same sha256 and byte count), exit 0, stderr empty
         two architectures agree, but the run came after the computations
         were performed in conversation, so this is an audit input and not a
         preregistered record; no probe status is claimed
```

## 11. Review record, rev2

Owner review of PR #1022 (2026-09-16) accepted in full; the check script and
its pins in section 10 are unchanged.

1. Section 7: the coupling of `|J|` to `chi_5` does not make any registered
   reading depend on the zeros of `L(s,chi_5)`; the dictionary row establishes
   no such dependence; `L(s,chi_5)` cancels in `C_0 O_5 = 1/zeta` and survives
   only in the separate channel `O_5`. The "exposed to `zeta_F`" claim is
   withdrawn; the ordinary RH stands as the program condition.
2. Section 5.1: unit rank 7 in `Q(zeta_40)` concerns the whole unit group;
   `J` keeps its single scale there. The clean factorization
   `unit = root of unity . real unit` holds for every unit exactly at
   prime-power conductors (Hasse unit index 1); at `n = 12` it fails by
   index 2.
3. Section 4: the weight-0 factor is defined per embedding, in
   `K tensor R`, and the quadruple `chi_5(a) zeta^a` is not a Galois orbit of
   one element of `K`; no single global Weil factor in `K` is claimed.
4. Sections 4 and 6: non-Weilness of `J` excludes only its direct role as a
   pure-weight eigenvalue, not Frobenius methods in general; the Carlitz
   census excludes rank one only inside the named class of function fields.
5. Section 6: the Dedekind zeta factorization uses primitive characters; the
   principal character modulo 5 gives `(1 - 5^-s) zeta(s)`, not `zeta(s)`.
