# C-RAPIDITY-GOLDEN-LADDER-1. Draft preregistration: the golden unit ladder of diagonal rapidity evaluations

```text
CANDIDATE ID:   C-RAPIDITY-GOLDEN-LADDER-1
DATE:           2026-08-27
SESSION:        agent lane claude/grh-zeta-split-orientation-lq2sh8
                (successor turn; the lane's first PR #588 is merged)
TARGET ROW:     none opened. This is a DRAFT preregistration for a future
                probe aimed at the growing-mode clause of
                TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]; that row is
                untouched and nothing here is pinned, locked, or run
                formally. No public issue is claimed by this note.
PARENTS:        probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1 (the integral
                rapidity lift and its local factors);
                probes/P-O5-SQUAREFREE-CORE-1 (candidate row
                O5-SQUAREFREE-CORE: the squarefree core s_5, merged, no
                canon status yet);
                probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1 (candidate row
                O5-DEDEKIND-GRH-DIVISOR-READ: the GRH pole-read, merged,
                no canon status yet);
                notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1 (the GRH channel
                dictionary, NON-CANONICAL);
                canon rows ARITHMETIC-RAPIDITY-DECOMPOSITION [T],
                SPLIT-PRIME-RAPIDITY-CLASS [T],
                J-RAPIDITY-TERNARY-SHELL-CENSUS [T].
LAYER:          L1 exact arithmetic and exact Z[phi] algebra, plus two
                labeled classical prime-density imports [T-lit] in the
                abscissa readings of section 6. No analytic estimate is
                claimed, no continuation, no decoder, measure, physical,
                SI, or L2-L6 lift.
AUTHORITY:      none. NON-CANONICAL candidate document per POLICY.md.
                No public T/D/C/H/O/F status is created here.
                RH remains [O]. GRH(zeta_F) is not claimed. No summatory
                estimate of any kind is claimed.
```

## 0. What this draft delivers

```text
1  The diagonal evaluation family of the registered integral rapidity
   lift: X_p -> t for one common t, well defined on unordered
   orientation pairs by star symmetry.                    [candidate-T]
2  An integrality selection theorem: the diagonal evaluations with all
   values in Z are exactly t = +-phi^(2k), the norm-plus-one unit
   lattice; tau = t + t^-1 = +-L_2k, by the registered Pell identity
   L_n^2 - 5F_n^2 = 4(-1)^n at even index.                [candidate-T]
3  The ladder anchors, all already registered or merged elsewhere:
   tau = 2 gives exactly mu (the registered augmentation); tau = -2
   reads the signed ternary census (-1)^b 3^a on squarefree n; the
   shell rung tau = 3 is exactly the merged squarefree core
   s_5 = mu a_F 1_((n,5)=1). The mu rung is the UNIQUE squarefree-
   supported rung of the full-lift ladder (2 - tau = 0 iff tau = 2).
                                                          [candidate-T]
4  The layer decomposition: with B_a(x) the inert-signed count of
   squarefree n <= x carrying exactly a split prime factors, every
   squarefree-restricted ladder sum is the polynomial
   sum_a (1-tau)^a B_a(x), and finitely many rungs recover every layer
   exactly by Vandermonde inversion at the distinct integer nodes
   1 - tau.                                               [candidate-T]
5  Exact connecting units between the full-lift ladder and the shell
   ladder [candidate-T], with their honest boundaries: the split
   deviation starts at T^2 (closed form 1 - (tau-1)^(e-1)), and the
   inert Mobius mass blocks any transfer below abscissa 1 (abscissa
   readings via labeled classical prime-density imports [T-lit]). The
   two ladders are separate objects.
6  A draft six-field skeleton for a future formal probe
   (P-RAPIDITY-GOLDEN-LADDER-1, name suggested), NOT pinned here, with
   the growing-mode frame stated as [H] and fenced.
7  A draft exact verifier: 10/10 gates, exact Z[phi] arithmetic, five
   breakers firing at frozen witnesses, stdout pinned. The tau = 2
   readouts reproduce the classical Mertens values M(10^3) = 2,
   M(10^4) = -23, M(10^5) = -48 as an internal cross-witness.
```

Nothing below Re(s) = 1 is claimed anywhere in this note. There is no
cancellation statement, no asymptotic, and no analytic continuation.
The entire content is exact L1 algebra plus one clearly fenced [H]
frame for a future lane.

## 1. Notation and frozen inputs

- `F = Q(sqrt5)`, `O_F = Z[phi]`, `phi^2 = phi + 1`, `chi_5` the
  quadratic character mod 5; split means `chi_5(p) = 1`, non-split
  means inert or `p = 5`. `L_n` and `F_n` are the Lucas and Fibonacci
  numbers; even-index Lucas values are `2, 3, 7, 18, 47, 123, 322, ...`
  with `L_2(k+1) = 3 L_2k - L_2(k-1)`.
- The integral rapidity lift `bold_mu` is the registered object of
  J-IDEAL-RAPIDITY-CHARACTER-LIFT [T]: local factor
  `((1-X_p T)(1-X_p^-1 T))/(1-T)` at split `p`, `1-T` at non-split
  `p`; on prime powers `bold_mu(p) = 1-X_p-X_p^-1` and
  `bold_mu(p^k) = 2-X_p-X_p^-1` for `k >= 2`; every value is invariant
  under every `X_p -> X_p^-1` (immediate from the registered local
  factor, which is symmetric in `X_p <-> X_p^-1`), and
  `aug(bold_mu(n)) = mu(n)` for every `n`.
- The registered unit lattice: O_F^x/{+-1} = <phi> with
  `eta(phi^n) = n log phi` and the Pell alternator
  `L_n^2 - 5 F_n^2 = 4(-1)^n` (ARITHMETIC-RAPIDITY-DECOMPOSITION [T]).
- The merged squarefree core (probes/P-O5-SQUAREFREE-CORE-1,
  candidate row O5-SQUAREFREE-CORE, not yet canon):
  `s_5(n) = mu(n) a_F(n) 1_((n,5)=1) = (-2)^omega(n)` on squarefree
  pure-split `n`, zero otherwise, with the two-sided theta > 1/3
  summatory transfer to the public channel O_5.
- Rationale for the vocabulary "rung k": the evaluation point
  `t = phi^(2k)` sits at the lattice point `2k log phi` of the
  registered rapidity lattice.

## 2. The diagonal evaluation family [candidate-T]

For `t` invertible in a commutative ring, the diagonal evaluation
`ev_t` sends every `X_p` to the same `t`. Because every `bold_mu(n)` is
star invariant and every local factor is symmetric under
`X_p -> X_p^-1`, the value `ev_t(bold_mu(n))` depends on `t` only
through

```text
tau = t + t^-1,
```

and is unchanged under `t -> t^-1`. The evaluation therefore never
selects one of the two conjugate prime ideals above a split prime: it
is well defined on the unordered orientation pairs of
SPLIT-PRIME-RAPIDITY-CLASS [T]. Explicitly, the full-lift ladder value
`m_tau(n) = ev_t(bold_mu(n))` is multiplicative with local table

```text
split p:      m_tau(p) = 1 - tau,   m_tau(p^e) = 2 - tau  (e >= 2),
non-split p:  m_tau(p) = -1,        m_tau(p^e) = 0        (e >= 2).
```

The shell ladder is the squarefree pure-split restriction with its own
Dirichlet series:

```text
sigma_tau(n) = (1-tau)^omega(n)  on squarefree pure-split n, else 0,
Sigma_tau(s) = prod_(chi_5(p)=1) (1 + (1-tau) p^-s).
```

## 3. Integrality selection: the ladder is forced [candidate-T]

Let `t` lie in `F^x`. Then

```text
ev_t(bold_mu(n)) is in Z for every n   <=>   t = +-phi^(2k), k in Z.
```

Proof. The value at a split prime is `1 - tau`, so integrality forces
`tau = t + t^-1` to lie in `Z`; then every local value `1-tau`, `2-tau`,
`-1`, `0` is an integer, so the condition is also sufficient. Now
`t` is a root of `X^2 - tau X + 1`. If `t` is rational, a rational root
of a monic integer polynomial with constant term 1 is `+-1 = +-phi^0`.
Otherwise `X^2 - tau X + 1` is the minimal polynomial of `t`, so `t` is
an algebraic integer unit of `O_F` with `N(t) = 1`. The units of `O_F`
are `+-phi^m`, and `N(phi^m) = (-1)^m`, so `m` is even. Conversely
`t = +-phi^(2k)` gives `tau = +-(phi^(2k) + phi^(-2k)) = +-L_2k`, an
integer. QED.

The admissible values are therefore exactly

```text
tau in { L_2k } union { -L_2k } = {2, 3, 7, 18, 47, ...} union
                                  {-2, -3, -7, -18, -47, ...},
```

and by the even-index case of the registered Pell identity, the
integers `m >= 0` with `m^2 - 5 b^2 = 4` solvable are exactly the
even-index Lucas values (gate V01 enumerates this to 322). The ladder
is not a modeling choice: the house's own unit group is what selects
it, and `k` runs over the registered rapidity lattice.

There is no orientation content in the choice: `phi^(2k)` and
`phi^(-2k)` are the same rung.

## 4. Anchors and the uniqueness of the mu rung [candidate-T]

```text
tau = 2  (k = 0, t = 1):    m_2 = mu exactly, for every n.
tau = -2 (t = -1):          on squarefree n, m_(-2)(n) = (-1)^b 3^a,
                            the inert-signed ternary census weight of
                            J-RAPIDITY-TERNARY-SHELL-CENSUS [T].
tau = 3  (k = 1, shell):    sigma_3 = s_5, the merged squarefree core,
                            coefficient by coefficient.
```

The first line is the registered augmentation read through the
evaluation family: `t = 1` IS the augmentation. The third line ties the
ladder to the merged core: `1 - L_2 = -2`. Between them sits nothing:
by the local table, `m_tau(p^e) = 2 - tau` for split `e >= 2`, so

```text
m_tau is supported on squarefree integers  <=>  tau = 2.
```

The mu rung is the unique squarefree-supported rung of the full-lift
ladder. Every other rung carries a split prime-power tail with the
constant coefficient `2 - tau != 0`.

A closed-form remark, exact and elementary: with
`t = phi^(2k)`, the split local factor evaluates to

```text
(1 - phi^(2k) T)(1 - phi^(-2k) T)/(1 - T) = (1 - L_2k T + T^2)/(1 - T),
```

a constant integer Satake-type pair `(phi^(2k), phi^(-2k))`. For
`k >= 1` this pair is not unitary (`|phi^(2k)| > 1`), the same pair at
every split prime. No Hecke-character or tempered identification is
possible for these rungs (a unitary character has local parameters of
absolute value 1), and a cuspidal GL(2) identification is excluded by
any unconditional sub-1/2 bound toward Ramanujan applied at p = 11
[T-lit; e.g. the Kim-Sarnak 7/64 bound: phi^2 > 11^(7/64)]. None is
claimed. The family `L_2k = D_k(3)` is the Dickson orbit of `L_2 = 3`;
this is elementary algebra, not automorphy.

## 5. The layer decomposition and the finite inversion [candidate-T]

For squarefree `n`, write `a(n)` for the number of split prime factors
and `b(n)` for the number of non-split prime factors (inert primes and
5). Define the layers

```text
B_a(x) = sum over squarefree n <= x with a(n) = a of (-1)^(b(n)).
```

Then, because `m_tau(n) = (1-tau)^(a(n)) (-1)^(b(n))` on squarefree
`n`, the squarefree-restricted ladder sums are exact polynomial reads
of the layers:

```text
sum_(n<=x) mu^2(n) m_tau(n) = sum_(a>=0) (1-tau)^a B_a(x),
```

for every admissible `tau`, with the sum finite:
`a <= A(x) <= log x / log 11`. At `tau = 2` this is Mertens:
`sum_a (-1)^a B_a(x) = M(x)`.

The nodes `1 - tau` at distinct rungs are distinct integers
(`-1, -2, -6, -17, -46, ...` on the positive family and
`3, 4, 8, 19, 48, ...` on the negative family), so the Vandermonde
system at any `A(x) + 1` rungs is invertible over Q, and

```text
{ ladder sums at rungs k = 0..A(x) }  <=>  { layers B_0(x)..B_A(x) },
```

by exact finite linear algebra (gate V07 performs the inversion at
`x = 20000`, where `A(x) = 3`, and recovers every layer exactly). The
inverse Vandermonde constants grow with `A(x)`; no uniformity claim of
any kind is made about them.

This is the exact content of the slogan: the diagonal ladder is the
moment transform of the split-count layers, and Mobius is its `tau = 2`
edge. Any mechanism that controls the ladder jointly in `k` controls
every layer, and conversely; both directions are pure linear algebra
at each fixed `x`.

## 6. Connecting units and honest boundaries [candidate-T]

The full-lift and shell ladders are related coefficientwise by

```text
m_tau = sigma_tau * w_tau,
```

where `w_tau` is multiplicative with non-split local factor `1 - T`
and split local factor, in exact closed form,

```text
[(1 - tau T + T^2)/(1 - T)] / (1 + (1-tau) T):
  coefficient of T^e is  1 - (tau-1)^(e-1)  for e >= 1
  (0 at T, 2-tau at T^2, tau(2-tau) at T^3, ...).
```

Two exact boundaries, stated so that nobody quotes the ladder past
them. The algebra (the closed form above and the identity
`m_tau = sigma_tau * w_tau`) is candidate-T and gated; the abscissa
readings attached to it use the classical prime-density facts that
`sum p^-s` over the split primes, and over the inert primes, diverges
for real `s < 1` [T-lit, via `L(1,chi_5) != 0`], and are labeled as
such:

```text
1  The split deviation of w_tau starts exactly at T^2, so the split
   part of w_tau is at best an abscissa-1/2 unit -- and for k >= 2 not
   even that: by the closed form its l1 abscissa is
   max(1/2, log(L_2k - 1)/log 11), which already exceeds 1 from
   tau = 18 on.
2  The non-split part of w_tau is the full inert Mobius factor, whose
   l1 mass has abscissa 1 [T-lit import above]. Therefore NO summatory
   transfer below abscissa 1 exists between m_tau and sigma_tau at any
   rung k >= 1, in either direction, by this convolution route.
```

At `tau = 2` the split factor of `w_2` is exactly 1, and
`m_2 = sigma_2 * (non-split Mobius)` is the trivial split/non-split
factorization of mu. The theta > 1/3 transfer of the merged core
belongs to the shell object `sigma_3 = s_5` and to O_5, not to the
full-lift rung `m_3`; this note does not extend it.

## 7. Draft six fields for a future probe (NOT pinned)

Everything in this section is a draft skeleton. It is not a
preregistration, carries no pins, and a formal probe must re-freeze all
of it after its own collision scan and a fresh public issue.

```text
probe (suggested):  P-RAPIDITY-GOLDEN-LADDER-1
EQUATION (draft)
  The selection theorem of section 3; the anchor identities and the
  squarefree-support uniqueness of section 4; the layer identity and
  finite Vandermonde inversion of section 5; the connecting units and
  both boundary statements of section 6. All at L1, exact.
CODE (draft)
  An exact verifier in the shape of the draft verifier below: stdlib
  only, exact integers, exact Z[phi] pairs, exact Fractions; no float,
  no zero table, no analytic input. The formal run must adopt the
  clean-interpreter preflight of P-O5-SQUAREFREE-CORE-1
  (PYTHON_STARTUP_CLEAN before the scientific command), per the
  abandonment record of P-O5-DEDEKIND-GRH-READ-1.
CARRIER (draft)
  The registered integral rapidity lift, diagonal unit evaluations,
  Lucas/Fibonacci integers, layer counts B_a(x), exact rational linear
  algebra.
SYSTEMATICS (draft)
  Unordered orientation pairs; star symmetry makes every evaluation
  orientation-free; k indexes the registered rapidity lattice; the
  ladder is forced by integrality, not chosen.
THRESHOLD (draft)
  All gates exact; breakers at frozen witnesses; byte-identical stdout
  on two architectures; exit zero; empty stderr.
LAYER
  NOT_APPLICABLE. L1 arithmetic only.
```

The [H]-grade frame the lane would eventually serve, stated once and
fenced: TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] leaves admissible "a
uniform growing-mode diagonal route h=h(N) with explicit approximation
and transfer error". The golden ladder is a concrete candidate family
of diagonal modes: rung k = 0 is the target augmentation, and by
section 5 controlling the rungs jointly is exactly controlling the
layers B_a(x). Whether shell structure supplies joint control with
usable constants is OPEN; this note proposes the frame and proves the
exact algebra, nothing more. Any future closure must obey the row's own
fence: no zeta-zero statement, no equivalent Mertens estimate, and no
target bound may enter as input. Layer-count asymptotics
(Landau/Sathe/Selberg-Delange territory: integers with omega(n) = a)
are occupied classical ground; an import audit is owed before any
analytic statement about B_a(x) is even proposed, and none is made
here.

## 8. Non-claims

```text
1  No RH, GRH, zero-location, cancellation, o(x), or O(x^theta)
   statement is made for any ladder sum, any layer B_a(x), or any
   other object. The readouts of gate V09 are exact integers and gate
   nothing analytic.
2  TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] is untouched. The layer
   equivalence of section 5 is finite linear algebra at fixed x; it is
   not a transfer mechanism, has no uniformity in x, and closes
   nothing.
3  No Hecke, automorphic, or spectral identification: the constant
   Satake-type pairs of rungs k >= 1 are non-unitary and equal at
   every split prime; characters and tempered objects are excluded
   outright and the cuspidal GL(2) case by a sub-1/2 Ramanujan-type
   bound at p = 11 (section 4, [T-lit]); the Dickson/Lucas structure
   is elementary.
4  No orientation is selected anywhere (star symmetry, section 2), and
   Mobius parity is not identified with a permutation sign on any
   orientation fiber (fence inherited from P-O5-SQUAREFREE-CORE-1).
5  No probability, Haar, physical, SI, decoder, or L2-L6 reading.
6  No canon file is edited; no probe is opened; no issue is claimed;
   no registry row is proposed by this note. Section 7 is a draft
   skeleton only.
7  The merged candidate rows cited (O5-SQUAREFREE-CORE,
   O5-DEDEKIND-GRH-DIVISOR-READ) have no canon status yet; citing them
   here adds no evidence to them and borrows none.
```

## 9. Draft verifier and pins

Exact-integer and exact Z[phi] arithmetic, stdlib only, no floats;
gates V01-V10 as listed in the file header. The note text is
intentionally unpinned (review wording may move); the executable and
its archived stdout are pinned.

```text
verifier:  C-RAPIDITY-GOLDEN-LADDER-1_verifier.py
sha256:    020209da354da08f506bc3d99fdd5abdc61dbdcb65942a6719fee91707157b6c
bytes:     16199
stdout:    stdout_rapidity_golden_ladder_1.txt
sha256:    138c1a1ba1de0f5556d9d175b8cc818191e52594beab0a07fe19a5aa234c1aba
bytes:     1490
run:       LC_ALL=C PYTHONHASHSEED=0 TZ=UTC python3 <verifier>
platform:  Linux x86_64, CPython 3.11.15, exit 0, stderr empty
result:    VERIFY RESULT 10/10 ALL PASS
```

Selected frozen readouts (exact integers; readout only, no claim):

```text
sum mu^2 m_tau, tau=2:    x=10^3: 2      x=10^4: -23     x=10^5: -48
  (equal to M(x); classical values reproduced as a cross-witness)
sum mu^2 m_tau, tau=3:    x=10^3: 24     x=10^4: 75      x=10^5: 483
sum mu^2 m_tau, tau=7:    x=10^3: 252    x=10^4: 647     x=10^5: -4473
sum mu^2 m_tau, tau=18:   x=10^3: 2034   x=10^4: -6855   x=10^5: -279792
sum sigma_3 (= s_5):      x=10^3: -103   x=10^4: -381    x=10^5: -925
layers B_a(10^5):         B_0=-363  B_1=-53  B_2=339  B_3=77
```

## 10. Break attempts

```text
BR1  Wrong Lucas value: replacing tau = 3 by tau = 4 in the shell rung
     breaks sigma = s_5 at first difference n = 11 (gate V10).
BR2  Replacing the inert local sign -1 by +1 breaks m_2 = mu at first
     difference n = 2 (gate V10).
BR3  Evaluating at an odd unit power (t = phi or phi^3): the value
     tau = t + t^-1 has a nonzero phi-component, so integrality fails,
     exactly as the selection theorem predicts (gate V10; the
     registered alternator N(phi) = -1 is the reason).
BR4  Pell near-misses m = 4 and m = 8 admit no solution of
     m^2 - 5b^2 = 4 (gate V10): the rung set has no extra members
     below 322.
BR5  Vandermonde with a repeated node is singular (gate V10): distinct
     rungs are genuinely needed for the layer inversion.
BR6  Reading the layer equivalence as progress on the bridge row:
     blocked by the row's non-circularity fence and by non-claim 2;
     the equivalence is per-x linear algebra with non-uniform
     constants.
BR7  Identifying the ladder with an L-function family: blocked for
     characters and tempered objects by the non-unitary constant
     Satake pair, and for cuspidal GL(2) by a sub-1/2 Ramanujan-type
     bound at p = 11 (section 4).
```

## 11. Live falsifiers and posture

```text
F-a  Any exact disagreement in gates V01-V08, or a breaker not firing
     at its frozen witness, fires against the corresponding
     candidate-T assertion of sections 2-6; the fired gate is
     archived, not moved.
F-b  A demonstration that some t in F^x outside +-phi^(2k) makes every
     ev_t(bold_mu(n)) an integer falsifies the selection theorem of
     section 3.
F-c  A squarefree-supported rung with tau != 2 falsifies the
     uniqueness statement of section 4.
F-d  An exact counterexample to the layer identity or to the
     invertibility of the node Vandermonde falsifies section 5.
F-e  If the prior-art audit of section 7 finds the layer/moment frame
     already occupied in the exact form proposed, the frame demotes to
     a citation and the lane narrows to what remains new; the exact
     algebra of sections 2-6 is unaffected.
```

Posture: this note requests nothing. If the owner opens the lane, the
path is: fresh public issue and collision scan; a formal probe
freezing sections 2-6 as its EQUATION field with a two-architecture
verifier grown from the draft below; the [H] frame of section 7 stays
outside the probe's claim set until a mechanism exists. This note
remains NON-CANONICAL either way.
