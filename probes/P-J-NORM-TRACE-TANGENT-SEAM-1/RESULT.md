# P-J-NORM-TRACE-TANGENT-SEAM-1 result

Date: 2026-08-29

## Decision

```text
T at frozen L1 proof scope
```

**Local evidence gate: COMPLETE. Public Canon and Registry status: unchanged. Repository two-architecture checks: pending.**

The exact written proof closes T1 to T4. The pinned standard-library verifier returned `ALL PASS`; the same-session adversarial checker returned `BREAKER NO BREAK`. Both were repeated byte-identically with empty stderr. The proof, not the finite audit, carries the theorem status at the probe scope.

## The exact seam

For every finite separable extension `E/Q`,

```text
T_E^1 := ker(N_E/Q : Res_E/Q G_m -> G_m),
d(N_E/Q)_1=Tr_E/Q,
Lie(T_E^1)=ker(Tr_E/Q),
dim T_E^1=[E:Q]-1.
```

For `K=Q(zeta_5)` in the integral basis `(j,j^2,j^3,j^4)`,

```text
Tr(sum_a x_a j^a)=-sum_a x_a,
Lambda_rel:=O_K intersect ker Tr ~= A_3,
Lambda_rel/5Lambda_rel ~= ker(sum:F_5^4->F_5).
```

The final term is the 125-point carrier already owned by `TRACEKERNEL-RESIDUAL-FORM [T]`. This probe adds its integral tangent origin and does not take ownership of the existing residual form.

## J inside norm one

The public unit obeys

```text
J phi=j,
J=j phi^-1,
|sigma_1(J)|=phi^-1,
|sigma_2(J)|=phi,
N_K/Q(J)=1.
```

Its normalized complex-place logarithmic modulus vector is

```text
(-2 log phi,+2 log phi),
```

with zero sum. Exact multiplicative closure therefore permits an internal exchange of scale between the two complex places.

## The decisive firewall

The norm-one group and trace-zero space are not the same global object:

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

Their exact relation is tangent-at-identity:

```text
Lie(ker N_K/Q)=ker Tr_K/Q.
```

For real points,

```text
T_K^1(R) ~= R_(>0) x S^1 x S^1,
dim_R T_K^1(R)=3,
```

while inherited `J-HARMONIC-SEAM [T]` gives

```text
O_K^*=mu_10 x <phi>,
rank O_K^*=1.
```

Three real Lie directions are not three free integral scale axes.

## What survives falsification-first controls

The raw number three does not select five. Every quartic field and the split etale algebra `Q^4` have norm-one dimension three. An embedding order gives coordinates, not a physical orientation. The probe starts from public `K` and `J`; it derives neither. No space, force, decoder, apparatus, event, measure, probability, observer, SI, or L2-L6 claim follows. No global decoder uniqueness or reading-family selection follows.

## Interpretive consequence

```text
candidate-D wording:
Unity is not enlarged by an added external coordinate.
One global closure equation determines one coordinate inversely,
while the remaining coordinates vary relationally inside the closure.
```

This wording is a reading of the theorem. It is not an additional T claim.

## Reproducibility state

```text
final pin:       06572b7b9c59ffcccacbe14d0e163b79e4ae57cb
verifier sha256: 0f6eaf58024ab9a48be68422e4b84b6c74628418debc76cf9da65c3eb20c403b
stdout sha256:   35eed8bd25608414804228fae3d7beb7c947e56846be7761885867eb8e76c069
local x86_64:    PASS, empty stderr, repeated byte-identically
breaker:         NO BREAK, same-session only
GitHub x86_64:   PENDING
GitHub aarch64:  PENDING
aggregate check: PENDING
Canon fold:      not started
```

The next public step is review and repository CI on the one-probe pull request. Any Registry or Canon fold is a later separate action.
