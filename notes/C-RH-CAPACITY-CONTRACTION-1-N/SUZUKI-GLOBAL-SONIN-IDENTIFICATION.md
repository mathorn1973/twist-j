# SUZUKI GLOBAL SONIN IDENTIFICATION

```text
STATUS: NON-CANONICAL incubation result / cross-source exact synthesis
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Source boundary

Suzuki, `On the Hilbert space derived from the Weil distribution`, defines

```text
K = F^(-1) M_Theta J F,
(JF)(z)=F^sharp(z),
V(0)=L2(0,infinity) intersect K L2(0,infinity).
```

Section 5 is written under RH when identifying `F(V(0))` with the classical
model space `K(Theta)`. However Suzuki later states explicitly that the space
`V(0)` itself can be constructed unconditionally, and Remark 5.2 asks whether

```text
V(0) != {0}
```

can be proved or disproved unconditionally.

The identification below uses only the boundary-unitary definition of `K`, the
Paley--Wiener Hardy decomposition, and the algebraic relation
`F K psi = Theta (F psi)^sharp`. It does not use innerness of `Theta`, real zero
locations, or the RH-dependent model-space equality.

## 2. Hardy decomposition and the sharp antiunitary

Freeze the Fourier orientation used by Suzuki:

```text
H_plus = F L2(0,infinity) = H2(C_+),
H_minus = H_plus^perp,
P = projection onto H_plus,
Q = 1-P.
```

The sharp operation

```text
F^sharp(z)=conjugate(F(conjugate(z)))
```

maps boundary values antiunitarily between the two Hardy halves. Therefore

```text
A : L2(0,infinity) -> H_minus,
A psi = (F psi)^sharp
```

is an antiunitary bijection, up to the fixed Fourier normalization constant.

## 3. Exact kernel identity

Let `psi in L2(0,infinity)` and put

```text
eta = A psi = (F psi)^sharp in H_minus.
```

By Suzuki's definition,

```text
F K psi = Theta eta.
```

Hence

```text
K psi in L2(0,infinity)
```

if and only if

```text
Theta eta in H_plus.
```

Since `eta in H_minus=QH`, the latter condition is exactly

```text
Q M_Theta Q eta = 0.
```

Consequently

```text
A[V(0)]
 = ker( Q M_Theta Q |_(H_minus) ).
```

Define, for any unimodular boundary multiplier `u`, the Sonin kernel in this
Hardy orientation by

```text
S(u)=ker(Q M_u Q |_(H_minus)).
```

Then exactly

```text
V(0) antiunitarily-isomorphic to S(Theta_xi).
```

No RH assumption enters this identity.

**Status:** candidate-T, exact Hilbert-space algebra from the two source
definitions.

## 4. Exact match to the Connes--Consani definition

Connes--Consani decompose multiplication by a quasi-inner boundary function
`u` with respect to the Hardy space and its orthogonal complement and define
the associated Sonin space as the kernel of the diagonal lower block `u_22`.
In the orientation above,

```text
u_22 = Q M_u Q |_(H_minus).
```

Therefore the right side of Section 3 is precisely their abstract Sonin-space
construction, now applied to Suzuki's **global xi boundary phase** `Theta_xi`:

```text
V(0)  ~=_antiunitary  S(Theta_xi).
```

This is not an identification of Suzuki's RH-dependent de Branges space with a
semi-local Connes space. It is an identification of Suzuki's unconditional
intersection space with the same **kernel construction** used by Connes--Consani.

**Status:** candidate-T cross-source dictionary. Novelty, if any, is only the
explicit observation that the two published definitions coincide after the
sharp/Fourier orientation is written out.

## 5. Immediate consequence: Suzuki's open nontriviality problem is a global Sonin problem

Suzuki remarks that proving or disproving

```text
V(0) != {0}
```

unconditionally is an interesting problem, and reduces it to the existence of
an eigenfunction of the isometric involution `K` inside `L2(0,infinity)`.

By Section 3, this is exactly

```text
S(Theta_xi) != {0}.
```

Thus the first global bridge target is strictly weaker than RH:

```text
construct one nonzero vector eta in H_minus such that
Q M_(Theta_xi) Q eta = 0.
```

A positive result would solve Suzuki's unconditional nontriviality question but
would not establish innerness of `Theta_xi`, vanishing of the opposite Hardy
escape `Q M_Theta P`, the Weil norm identity, or RH.

**Status:** candidate-D reformulation of the open problem; no RH implication is
claimed beyond Suzuki's stated one-way fact that `V(0)={0}` would contradict RH.

## 6. Why the semilocal Sonin filtration is now relevant but not automatically sufficient

For a finite place set `F`, Connes--Consani use

```text
u(F)=rho_inf product_(p in F_fin) rho_p
```

and prove that

```text
S(u(F))=ker(Q M_(u(F)) Q)
```

is infinite-dimensional; these spaces form an inductive system as finite
places are added.

The present identity puts the desired global target in **exactly the same
kernel category**:

```text
finite stage:  S(u(F)),
global target: S(Theta_xi).
```

This does NOT identify their inductive limit with `S(Theta_xi)`. The earlier
`DIRECT-SONIN-LIMIT-IDENTIFICATION` shortcut remains F: Suzuki explicitly notes
that the associated de Branges constructions have different generators and
spectral properties.

The legitimate question is now narrower:

```text
Can one transport a nonzero vector through the finite Sonin filtration into
S(Theta_xi) by a separately constructed Wiener--Hopf/intertwining factor?
```

## 7. Abstract transport lemma

Let `u` and `U` be unimodular boundary functions. Suppose there exist
multipliers `D,N` with

```text
U D = N u
```

and the following Hardy-preservation properties in the frozen orientation:

```text
D H_minus subset H_minus,
N H_plus  subset H_plus.
```

Then multiplication by `D` maps Sonin kernels forward:

```text
D : S(u) -> S(U).
```

Proof. If `eta in S(u)`, then `eta in H_minus` and `u eta in H_plus`. By the
preservation assumptions,

```text
D eta in H_minus,
U D eta = N u eta in H_plus.
```

Hence `D eta in S(U)`.

This is the abstract mechanism behind the Connes--Consani finite-place
injections, where the quotient between consecutive scattering functions is
written as a numerator/denominator pair.

**Status:** candidate-T, elementary Hardy-space lemma.

## 8. New exact gate: GLOBAL-SONIN-WIENER-HOPF

The next non-circular construction is therefore:

For a finite semilocal stage `F`, find `D_F,N_F`, independently of RH and zero
locations, such that

```text
Theta_xi D_F = N_F u(F)
```

on the critical boundary, with

```text
D_F H_minus subset H_minus,
N_F H_plus  subset H_plus.
```

Then every nonzero `eta_F in S(u(F))` with `D_F eta_F !=0` produces a nonzero
vector

```text
D_F eta_F in S(Theta_xi) ~= V(0).
```

This would be a genuine prime/archimedean-to-global-xi bridge and would settle
Suzuki's unconditional nontriviality question.

It would **not** prove RH. The RH wall would remain the stronger statement that
`Theta_xi` is inner / its opposite Hardy escape vanishes, together with the
Weil metric identification.

## 9. Hard falsifiers

The proposed gate fails if:

1. `D_F,N_F` are defined using zeros of `xi`, RH, or innerness of `Theta_xi`;
2. the factorization exists only by writing the tautological quotient
   `Theta_xi/u(F)` with no Hardy factorization theorem or explicit formula;
3. `D_F` does not preserve `H_minus` or `N_F` does not preserve `H_plus`;
4. the constructed `D_F` annihilates every vector of the finite Sonin space;
5. convergence is asserted from the raw Euler product in `Re s<=1`, contrary
   to `SEMILOCAL-IMPEDANCE-LIMIT-NOGO.md`;
6. a direct isomorphism of the semilocal inductive-limit Hilbert space with
   Suzuki's `K_0`, `H(E_xi)` or `V(0)` is assumed;
7. the factorization is normalized after inspecting the desired target vector.

## 10. Current hierarchy

```text
local Euler factor / gamma factor
    -> exact lossless scattering cells
    -> finite semilocal quasi-inner u(F)
    -> infinite-dimensional S(u(F)) with inductive maps
    -> [OPEN GLOBAL-SONIN-WIENER-HOPF]
    -> S(Theta_xi) ~= V(0)
    -> [stronger OPEN] Theta_xi inner / opposite Hardy escape zero
    -> RH.
```

The new middle equality `S(Theta_xi) ~= V(0)` is exact. The transport arrow into
it is open. No public scientific status moves.
