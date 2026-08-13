# ARCHIMEDEAN ESCAPE DEFECT

```text
STATUS: NON-CANONICAL incubation result
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Source projection identity

Let `P` be the Hardy projection in the Connes--Consani archimedean model and
write

```text
P1      = 1-P,
P_hat   = Fourier P Fourier^*,
P1_hat  = 1-P_hat.
```

Let `U_inf` denote multiplication by the archimedean scattering phase
`rho_inf` on the critical line. The source identity is

```text
U_inf^* P U_inf = P1_hat.
```

This is an unconditional unitary-conjugacy statement. No RH input appears.

## 2. The prolate pair is an escape operator

Define the one-sided escape block

```text
B = P U_inf P1 : P1 H -> P H.
```

Then exactly

```text
B^* B
 = P1 U_inf^* P U_inf P1
 = P1 P1_hat P1.
```

Thus the positive contraction `P1 P1_hat P1` of the prolate pair is literally
the squared defect/escape operator of the unitary archimedean scattering
channel.

If `lambda_n^2` are the eigenvalues of the prolate compression
`P1 P1_hat P1`, then the singular values of the scattering escape block `B`
are exactly `|lambda_n|`.

**Status:** candidate-T, exact operator identity from the source projection
relation.

## 3. The trace remainder at the identity is escape energy

Connes--Consani write the trace-remainder kernel in the form

```text
delta(rho) = Tr(theta(rho^(-1)) P1_hat P1),
```

where `theta` is the scaling representation. At `rho=1`, cyclicity of the trace
on the positive trace-class compression gives

```text
delta(1)
 = Tr(P1_hat P1)
 = Tr(P1 P1_hat P1)
 = Tr(B^*B)
 = ||B||_HS^2.
```

Therefore the nonzero remainder which blocked the correction-free Sonin
identification is not an arbitrary added term. At the identity it is exactly
the Hilbert--Schmidt escape energy of the same lossless scattering split.

For general scaling,

```text
delta(rho)=Tr(theta(rho^(-1)) P1_hat P1)
```

is the scaling correlation of this defect pair. It is not generally a plain
nonnegative norm at each `rho`; the positivity used in the source is the
coupled trace/prolate construction.

**Status:** candidate-T for `rho=1` escape-energy identity and for the exact
scaled trace-correlation formula; no pointwise positivity of `delta(rho)` is
asserted.

## 4. Pythagoras at the one-sided cutoff

The output of `U_inf` on the input half-space `P1 H` splits orthogonally as

```text
U_inf P1 = P1 U_inf P1 + P U_inf P1.
```

Hence

```text
(P1 U_inf P1)^*(P1 U_inf P1) + B^*B = P1.
```

This is an exact operator Pythagoras:

```text
inside^* inside + escape^* escape = identity on the input half-space.
```

The prolate compression is the escape square in this decomposition.

This gives a source-level realization of the informal phrase `Pythagoras one
level up`: the relevant positive object is the orthogonal decomposition of a
unitary scattering output, while the Weil/phase-delay object is obtained after
differentiating or taking a relative trace.

**Status:** candidate-T, general Hilbert-space identity.

## 5. Relation to the earlier no-go

`TRACE-REMAINDER-DOMINATION-NOGO.md` proved that the source trace remainder
cannot be paid for separately by the two pole squares below the first-prime
threshold. There is no contradiction.

The present identity shows why separate domination was the wrong operation:
`delta` belongs to the **escape leg of a coupled unitary split**. The source
positivity transfers pieces between the inside and escape channels through the
prolate geometry. It is not a scalar inequality `delta <= pole capacity`.

## 6. Relation to the localized Suzuki carrier

`COMPRESSED-DELAY-GENERATOR.md` independently constructed, for the interval
projection `P_a`, the isometric output column

```text
W_a(tau)
 = [ P_a U_F(tau) P_a ; (1-P_a)U_F(tau)P_a ],

W_a^*W_a=I,
-i W_a^*W_a'=P_a[-i U_F^*U_F']P_a.
```

The current one-sided archimedean identity is the source-resolved version of
the second row of that column when the geometric cutoff is a Hardy half-space.

The remaining comparison is therefore not whether an escape defect exists. It
is to expand the **two-sided finite interval** projection `P_a` as the
difference of two translated Hardy half-space projections and identify all
cross terms.

## 7. Next gate: TWO-SIDED-HARDY-ESCAPE

Let `H_c` be the time-domain projection onto `(-infinity,c)` and

```text
C_a=H_a-H_(-a)
```

be the interval projection onto `(-a,a)`. For a translation-invariant unitary
scattering operator `U`, define

```text
B_left  = H_(-a) U C_a,
B_right = (1-H_a) U C_a.
```

The total escape satisfies

```text
B_a^*B_a = B_left^*B_left + B_right^*B_right.
```

Each row expands into shifted one-sided Hardy blocks plus cross terms spanning
the gap `2a`.

The next result must derive those cross terms exactly and decide whether they
match the finite-interval/prolate correction and the frozen pole channels. A
coefficient or sign mismatch is a falsifier of the current G6 intertwiner
route.
