# SUZUKI GLOBAL DIAGONAL-KERNEL IDENTIFICATION

```text
STATUS: NON-CANONICAL candidate-T algebra / candidate-D cross-source reading
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

Freeze Suzuki's Fourier orientation and normalize the carrier map explicitly:

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
A_0 : L2(0,infinity) -> H_minus,
A_0 psi = (2 pi)^(-1/2) (F psi)^sharp
```

is an antiunitary bijection for Suzuki's unnormalized Fourier transform. The
fixed `(2 pi)^(-1/2)` is part of the map and is not allowed to vary between the
two carriers.

## 3. Exact kernel identity

Suzuki's `K` is an isometric involution, so

```text
V(0)
 = {psi in L2(0,infinity) : K psi in L2(0,infinity)}.
```

Let an arbitrary `psi in L2(0,infinity)` be given and put

```text
eta = A_0 psi = (2 pi)^(-1/2)(F psi)^sharp in H_minus.
```

By Suzuki's definition,

```text
F K psi = sqrt(2 pi) Theta eta.
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
A_0[V(0)]
 = ker( Q M_Theta Q |_(H_minus) ).
```

Define, for any unimodular boundary multiplier `u`, the extended
diagonal-block kernel in this Hardy orientation by

```text
S_diag(u)=ker(Q M_u Q |_(H_minus)).
```

Then exactly

```text
V(0) antiunitarily-isomorphic to S_diag(Theta_xi).
```

No RH assumption enters this identity.

**Status:** candidate-T, exact Hilbert-space algebra from the two source
definitions.

## 4. Match to the abstract Connes--Consani kernel after orientation transport

Connes--Consani decompose multiplication by a **quasi-inner** boundary function
`u` with respect to the Hardy space and its orthogonal complement and define
the associated Sonin space as the kernel of the diagonal lower block

```text
u_22=(1-P)u(1-P).
```

Their critical-line/left-Hardy convention and Suzuki's upper-`z` convention
must first be related by the explicit coordinate/reflection antiunitary. After
that transport, in the orientation frozen above, this is

```text
u_22 = Q M_u Q |_(H_minus).
```

Therefore the right side of Section 3 has precisely the same abstract
diagonal-block kernel formula, extended here to Suzuki's **global xi boundary
phase** `Theta_xi`:

```text
V(0)  ~=_antiunitary  S_diag(Theta_xi).
```

Unconditional boundary unimodularity of `Theta_xi` does not establish the
quasi-inner hypothesis under which Connes--Consani use the name Sonin space.
Thus this is not an identification of Suzuki's RH-dependent de Branges space
with a semilocal Connes space. It is an exact identification with an extended
diagonal-block kernel of the same formula.

**Status:** candidate-T for the displayed kernel algebra and candidate-D for
the cross-source category reading. This does not identify any finite
semilocal carrier with Suzuki's carrier.

## 5. Standard Toeplitz form

Let

```text
J_H : H_plus -> H_minus,
J_H f=f^sharp.
```

For `eta=J_H f`, the diagonal-kernel condition

```text
Theta eta in H_plus
```

is equivalent after applying `sharp` to

```text
Theta^sharp f in H_minus.
```

On the real boundary Suzuki has

```text
Theta^sharp=Theta^(-1)=conjugate(Theta).
```

Therefore

```text
V(0) != {0}
 <=> S_diag(Theta_xi) != {0}
 <=> ker T_(conjugate(Theta_xi)) != {0},
```

where

```text
T_g=P M_g |_(H_plus)
```

is the ordinary Toeplitz operator on `H2(C_+)`.

This places Suzuki's unconditional nontriviality question directly inside the
standard Toeplitz-kernel problem.

**Status:** candidate-T, exact unitary/antiunitary rewrite.

## 6. Exact factorization criterion, stated without importing a theorem name

For any unimodular boundary symbol `g`,

```text
ker T_g != {0}
```

if and only if there exist nonzero Hardy functions

```text
f_+ in H_plus,
f_- in H_minus
```

such that

```text
g f_+ = f_-.
```

Factoring the two Hardy functions into inner and outer parts is the starting
point for a Wiener--Hopf / inner--outer description of `g`. Conversely any
typed factorization with the displayed Hardy memberships immediately supplies
a nonzero Toeplitz-kernel vector.

Applied to

```text
g=conjugate(Theta_xi),
```

this is exactly the analytic factorization wall behind `V(0)!=0`.

The standard Toeplitz-kernel literature sharpens this to canonical
inner--outer/maximal-vector forms; no such strengthening is imported here.
This records a concrete Wiener--Hopf factorization formulation for the global
xi phase, not a solution of it.

**Status:** candidate-T, direct equivalence from the Toeplitz definition.

## 7. Why one known critical zero does not solve the problem

Suzuki defines, for zeros `gamma` of

```text
A(z)=xi(1/2-i z),
```

the meromorphic functions

```text
F_gamma(z)
 = sqrt(m_gamma/pi) i(1+Theta(z))/(2(z-gamma)).
```

These functions exist in his unconditional zero expansion. However the later
statement

```text
F_gamma = Fourier(psi_gamma),
psi_gamma in V(0),
```

is made in the RH-dependent model-space section and uses the orthogonality /
model-space structure available when `Theta` is inner.

The RH-dependent source step cannot be used unconditionally to infer that a
known real zero furnishes a vector in `V(0)`. The missing condition is precisely
Hardy membership of a candidate and its `conjugate(Theta)`-transformed image.

**Status:** `STOP` for the unsupported inference
`ONE-CRITICAL-ZERO -> V(0) NONZERO`; no no-go theorem says that every possible
zero-based construction must fail.

## 8. Immediate consequence: Suzuki's open problem is a global diagonal/Toeplitz problem

Suzuki remarks that proving or disproving

```text
V(0) != {0}
```

unconditionally is an interesting problem, and reduces it to the existence of
an eigenfunction of the isometric involution `K` inside `L2(0,infinity)`.

By Sections 3 and 5, this is exactly

```text
S_diag(Theta_xi) != {0}
```

or equivalently

```text
ker T_(conjugate(Theta_xi)) != {0}.
```

This nontriviality is necessary under RH and is not known to be sufficient:

```text
construct one nonzero f in H_plus such that
conjugate(Theta_xi) f lies in H_minus.
```

A positive result would solve Suzuki's unconditional nontriviality question but
would not establish innerness of `Theta_xi`, vanishing of the opposite Hardy
escape `Q M_Theta P`, the Weil norm identity, or RH.

**Status:** candidate-D reformulation of the open problem; no RH implication is
claimed beyond Suzuki's stated one-way fact that `V(0)={0}` would contradict RH.

## 9. Why the semilocal Sonin filtration is now relevant but not automatically sufficient

For a finite place set `F`, Connes--Consani use, in their source orientation,

```text
u(F)=rho_inf product_(p in F_fin) rho_p
```

and prove that

```text
S_CC(u(F))=ker(Q M_(u(F)) Q)
```

is infinite-dimensional; these spaces form an inductive system under specified
injective multiplier maps as finite places are added. They are not asserted to
be literal inclusions, nor are their off-diagonal blocks automatically
intertwined.

After the orientation transport of Section 4, the present identity puts the
desired global target in the same abstract diagonal-kernel category:

```text
finite stage:  S_CC(u(F)),
global target: S_diag(Theta_xi).
```

Here `S_CC` names the source Sonin space for quasi-inner `u(F)`. This does NOT
identify its inductive limit with `S_diag(Theta_xi)`. The earlier
source comparison only excludes the literal generator-/spectrum-preserving
identification of the named CCM de Branges spaces with `H(E_xi)`; it does not
exclude every abstract isometry, limit, compression, quotient, or defect
relation.

One deferred question is now narrower:

```text
Can one transport a nonzero vector through the finite Sonin filtration into
S_diag(Theta_xi) by a separately constructed Wiener--Hopf/intertwining factor?
```

## 10. Abstract transport lemma

Let `u` and `U` be unimodular boundary functions. Suppose there exist bounded
multipliers `D,N` (or closed multipliers on an explicitly common invariant
domain, with every displayed product in `L2`) with

```text
U D = N u
```

and the following Hardy-preservation properties in the frozen orientation:

```text
D H_minus subset H_minus,
N H_plus  subset H_plus.
```

Then multiplication by `D` maps the extended diagonal kernels forward:

```text
D : S_diag(u) -> S_diag(U).
```

Proof. If `eta in S_diag(u)`, then `eta in H_minus` and `u eta in H_plus`. By the
preservation assumptions,

```text
D eta in H_minus,
U D eta = N u eta in H_plus.
```

Hence `D eta in S_diag(U)`.

This is the abstract mechanism behind the Connes--Consani finite-place
injections, where the quotient between consecutive scattering functions is
written as a numerator/denominator pair.

**Status:** candidate-T, elementary Hardy-space lemma at the stated bounded or
typed-domain scope.

## 11. Deferred GLOBAL-SONIN-WIENER-HOPF comparison (not a gate)

Frozen G3 remains UNDECIDED, so G4 and G6 are blocked. No new #357 gate is
opened or executed here. After the frozen order and outcome-blind G0
classification permit it, a separately locked comparison could ask:

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

Then every nonzero `eta_F in S_CC(u(F))` with `D_F eta_F !=0` produces a nonzero
vector

```text
D_F eta_F in S_diag(Theta_xi) ~= V(0).
```

If all domain/orientation and non-annihilation requirements were proved, this
would be a prime/archimedean-to-global-xi bridge and would settle Suzuki's
unconditional nontriviality question.

It would **not** prove RH. The RH wall would remain the stronger statement that
`Theta_xi` is inner / its opposite Hardy escape vanishes, together with the
Weil metric identification.

## 12. Falsifiers for a later separately locked comparison

The proposed later comparison fails if:

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

## 13. Current hierarchy

```text
local Euler factor / gamma factor
    -> exact boundary-unitary scattering factors
    -> finite semilocal quasi-inner u(F)
    -> infinite-dimensional S_CC(u(F)) with inductive maps
    -> [deferred GLOBAL-SONIN-WIENER-HOPF comparison]
    -> S_diag(Theta_xi) ~= V(0) ~= ker T_(conjugate Theta_xi)
    -> [RH-equivalent condition which implies nontriviality]
       Theta_xi inner / opposite Hardy escape zero
    -> RH.
```

The new middle equality `S_diag(Theta_xi) ~= V(0)` is exact. Calling the global
kernel a Connes--Consani Sonin space would additionally require quasi-innerness,
which is not imported. The transport arrow is unproved and is not a #357 gate.
It also does not prove G3 or absorb the corrected signed pole pair. No public
scientific status moves.
