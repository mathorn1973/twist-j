# Arithmetic review and scale boundaries

**NON-CANONICAL, L1. Analytical candidate-T material only.**

Date: 2026-10-25. Owner: A. M. Thorn, session
`C-FULL-RECORD-SCALE-LIFT-N`, public claim
[#1771](https://github.com/mathorn1973/twist-j/issues/1771).
This is a separately reasoned analytical review within the same authoring
session. It is not external independent acceptance. No scientific executable,
simulation or formal gate was run. No public scientific status is assigned.

## 1. Sources and prior-work boundary

The authority input is Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, specifically
[`HOMOGENEOUS-CAPTURE-CURRENT-RECORD`](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
Its one-pair, one-token-or-pulse, one-receiver sector and synchronized
macrostep are unchanged. The authority audit is separate from this review.

The reviewed attachment is `twist_full_record_bridge/PROOF.md`, SHA-256
`e9ac1a0dbc4b29eb7551584fc0af1a160985ce926bfdd79ef3a7b588878a80c2`.
Its numbered review obligations refer to its accompanying `REVIEW.md`.

The coefficient localization and per-port integer/exponent representation
already appear in
[#1739, COHERENT-W-LOCALIZED-RING-CLOSURE](https://github.com/mathorn1973/twist-j/blob/5ce14091995dfdc0e57fe7b256b72aed6f16ac3e/notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md).
Moreover, the whole-carrier numerator 25, its sharper ideal-valued
minimality, the stationary-output reduction obstruction and coherent
occupied-memory continuation were already recorded in
[#1741, OPERATOR_EXTENSION.md](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322548).
That analytical file has declared length 21326 bytes and SHA-256
`32bc15afbe1fca4d94a4ea22dfe13f02727df93b3ade9f931655801d765fc3aa`.
It is a public issue record, not a reachable Git pin or formal-run evidence.
These statements are inherited inputs and independently rederived here,
not newly claimed discoveries.

## 2. Review of the inherited arithmetic claims

Put `O=Z[t]`, `t=zeta_20`, `zeta=t^4`, `i=t^5`, and let `B` be the
complete coordinate basis, including carrier and occupied-memory labels.
Write `M_raw=direct_sum_B O`, `M_amp=direct_sum_B O[1/5]`,
`A=25 U_rec`. Direct sums mean finite support.

For `M=I+2iX`,

\[
M\otimes M=I+2i(X\otimes I+I\otimes X)-4X\otimes X.
\]

Both `e1-e4` and `i(e2-e3)` are annihilated by the middle sum and are
minus-one eigenvectors of `X tensor X`. Hence the actual object coin
`M_2=(M tensor M)/5` fixes both contact directions. With the canonical
contact vectors `alpha,gamma`,

\[
D=5(C-I)=-2(P_\alpha+P_\gamma)
       +4(|\gamma\rangle\langle\alpha|-|\alpha\rangle\langle\gamma|).
\]

The half in every outer product is canceled by its coefficient. Thus `D`
is integral over `O`, and the fixed-direction identity makes `Wcal D`
integral too. The exact canonical order gives

\[
25U=\zeta^{-2}(25\mathcal R\mathcal W+5\mathcal R\mathcal W D),
\qquad U_{\rm rec}=\mathcal T U\mathcal T^*.
\]

Here `5 Rcal` and `5 Wcal` are integral, and `Tcal` is a permutation
preserving arrangement. This proves integrality in all four arrangement
blocks, without adjoining `sqrt(2)` and without changing gate order.

A specific pulse matrix entry is obtained from
`(R,r,x,coin,bank)=(0,10,0,e1,1)` to `(-1,10,0,e1,1)`.
The object contributes `1/5`; `V_11=(1-4 exp(ik))/5` contributes the
unique same-position coefficient `1/5`. Contact and receiver calibration
are inactive. The full entry is `zeta^(-2)/25`. Thus every positive integer
clearing the full matrix is divisible by 25. More generally a scalar
`kappa in O` clears it exactly when `kappa in 25 O`, as already stated
in #1741. No change-of-basis minimum is asserted.

Finite propagation gives finite rows and columns, including for the
adjoint. Unitarity therefore proves the algebraic identities

\[
A^\dagger A=AA^\dagger=625I.
\]

Stationary output rows all contain a factor 5: their free contribution
is `25W`, and their contact contribution is `5 Wcal D`. The receiver
permutation does not change arrangement. A far token basis transition
has coefficient `5 zeta^(-2)`, so the common rational-5 divisor of these
rows is exactly 5, not 25.

| Attachment obligations | Analytical disposition |
| --- | --- |
| 1-4: order, contact halves, fixed directions, mixed blocks | Verified by the displayed canonical factorization. |
| 5-7: receiver permutation and denominator sharpness | Verified in the same fixed coordinate basis. |
| 8: finite support and adjoint | Both follow from the finite gate ranges and finite local coin dimensions. |
| 9: arithmetic versus Hilbert preparations | Finite arithmetic states are a proper domain; arbitrary complex references enter only through tensor extension of the operator identity. |
| 15: stationary residue loss | Verified for every output row, including pulse-to-token conversion and occupied labels. |
| 16: raw height | Its growth is conditional on that chosen arithmetic account, not a physical work theorem. |
| 17: native and physical boundaries | No original-six-pentit derivation, physical energy selection, preparation or precision-cost closure follows. |

No blocking arithmetic defect was found within these stated scopes.
Spectral obligations 10-14 belong to the separate spectral review.

## 3. Primitive common-scale chart and its exact inverse

For a nonzero vector `a in M_raw`, define

\[
\nu_5(a)=\max\{k\ge0:a\in5^kM_{\rm raw}\}.
\]

This is common rational-5 divisibility, not a prime valuation on
`Q(zeta_20)`. In particular no multiplicativity statement is used.
Every nonzero `q in M_amp` has a unique representation `q=5^(-m)a`
with `m in Z` and `nu_5(a)=0`. Represent zero separately.

For primitive `a`, put `s=nu_5(Aa)`. Since `A` is integral, `s>=0`.
Since `625a=A^dagger Aa`, integrality of the adjoint and primitivity
give `s<=4`. The exact representative update is

\[
(m,a)\longmapsto(m+2-s,\;Aa/5^s).
\tag{A1}
\]

If `a'=Aa/5^s`, then `A^dagger a'=5^(4-s)a`, with divisibility
exactly `4-s`. Applying (A1) with `A^dagger` recovers `(m,a)`.
Thus this chart gives a bijection, with zero fixed, reading precisely
the automorphism `U_rec` on `M_amp`.

All five divisibilities occur. Choose basis supports whose forward and
backward one-step neighborhoods avoid contact and receiver:

| `s` | Primitive input and reason |
| --- | --- |
| 0 | Pulse basis `e_p`; `Ae_p` has a unit entry. |
| 1 | Token basis `e_t`; `Ae_t` has exact common factor 5. |
| 2 | Token vector with object coin `e1-e4`; the coin fixes it, so the output has exact common factor 25. |
| 3 | `A^dagger e_t/5`; it is primitive and its image is `125 e_t`. |
| 4 | `A^dagger e_p`; it is primitive and its image is `625 e_p`. |

This chart is not a bounded-range update of its coefficient representatives.
Indeed take `a=e_t` above and add a pulse basis vector `p` arbitrarily far
away in configuration space, with disjoint one-step output supports.
Then `b=a+p` agrees with `a` on an arbitrarily large neighborhood of the
token support, but `s(a)=1` and `s(b)=0`. The normalized output near that
support is `Ae_t/5` for `a` and `Ae_t` for `b`. The scale increments are
1 and 2 respectively. The decoded amplitude update remains the original
finite-range operator. The obstruction concerns this global normal form.

## 4. A full-model extremal precision witness

Start with a unit pulse basis vector `e` having
`R=0,r=1,coin=3,x=0,bank=2`, carrier label `j` and memory label `k`.
Coin indices here are one-based. Consider after `n>=0` macrosteps the
endpoint `R=0,r=n+1,coin=3,x=n,bank=2`.

Each step changes `r` by at most one. Reaching this endpoint forces coin
3 and relative displacement `+1` at every step. Therefore `R=0` throughout,
and contact and its phase never act on a contributing path. Reaching
`x=n` likewise requires a pulse displacement `+1` every step. In the
canonical Fourier convention all such outputs have bank 2, and

\[
V_{22}(k)=(1-4e^{-ik})/5.
\]

The initial bank 2 therefore fixes the pulse coefficient to `-4/5`
at every step; the object diagonal coefficient is `1/5`. The unique
path has amplitude

\[
\frac{(-4\zeta^{-2})^n}{25^n}.
\tag{A2}
\]

The identity `U_rec^n=Tcal U^n Tcal^*` makes the final labels `(j,k)`
for `n<100` and `(k,j)` for `n>=100`. This includes arbitrary occupied
labels and changes no coefficient in (A2).

Thus `A^n e` is primitive for every `n`, and (A1) has `s=0` and
`m_n=2n` on this trajectory. Its least positive integer denominator is
exactly `25^n`: sufficiency follows from integrality of `A^n`; necessity
follows from (A2), coprimality of 4 and 5, and `O intersect Q=Z`.

The decoded trace account
`Tr(sum_b conjugate(q_b) q_b)` stays 8, and the active occupation charge
stays 10. Every bounded spectral reading of `U_rec` has a conserved
distribution on this trajectory. These facts do not bound its exact
denominator depth. This is a pulse basis preparation, not the canonical
capture packet or a safe-window preparation. The amplitude magnitude
in (A2) is `(4/25)^n`; consequently this argument supplies no fixed-error
approximation lower bound or thermodynamic work lower bound.

## 5. No nonzero additive fixed-exponent five-residue factor

Let `G` be any abelian group killed by `5^q` for one fixed integer
`q>=1`, and let `Pi:M_amp -> G` be additive. Multiplication by `5^q`
is onto `M_amp`, so every `x` has `y=x/5^q` in that same module. Hence

\[
\Pi(x)=\Pi(5^q y)=5^q\Pi(y)=0.
\tag{A3}
\]

This includes finite-support or unrestricted spatial fields over `F_5`,
and fields over `Z/(5^q)`, with their additive groups. It applies before
any dynamic intertwining is required, and separately to each member of
a time-indexed family of additive readings with the same complete domain.

It does not exclude nonlinear digit readings with carries, readings on a
restricted preparation domain, raw integer-cover residues, or a newly
specified native network. A canonical digit reading is generally not
additive: its carry data are precisely what (A3) cannot discard.
No classification of all nonlinear native factors is asserted.

## 6. Arithmetic implementation guard

The power basis `1,t,...,t^7` is not orthonormal for the trace account.
Its Gram matrix is `G_ab=Tr(t^(b-a))`: the diagonal is 8; odd differences
give zero; differences `+/-2,+/-6` give 2; difference `+/-4` gives -2.
The operator adjoint means conjugation `t -> t^(-1)` followed by
transposition of configuration indices. A plain Euclidean transpose on
eight integer coordinates must not replace it.

The findings above are analytical candidate results for subsequent
independent acceptance. They supply neither a two-architecture computation
gate nor an original-TWIST or physical-resource derivation.
