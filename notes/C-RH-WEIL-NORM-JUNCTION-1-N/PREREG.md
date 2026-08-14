# PREREG C-RH-WEIL-NORM-JUNCTION-1-N

```text
STATUS:       NON-CANONICAL INCUBATION
ISSUE LOCK:   #374
PUBLIC BASIS: Public Canon v46
LAYER:        analytic/operator-theoretic only
```

## Frozen problem

Find, or kill, an exact prime-defined junction between

```text
ordinary/conjugate norm pairing   -> S2 = sum_(gamma>0) 1/|rho|^2
functional reflection pairing     -> lambda_1
H2 difference                     -> S2-lambda_1 >= 0.
```

No zero table or RH assumption is allowed.

## Frozen source conventions

Suzuki zero coordinate `z` is defined by

```text
rho = 1/2 - i z.
```

For Fourier transforms `h_j=hat(v_j)`, use exactly Suzuki's convention

```text
Q_W(v1,v2)
 = sum_(z in Gamma) m_z h1(z) conjugate(h2(conjugate(z))).
```

The ordinary target at the same coordinate is

```text
N(h)=sum_(z in Gamma) m_z |h(z)|^2.
```

At the Cauchy target `h(z)=1/(1/2-i z)=1/rho`, the full-zero versions are twice the upper-half-plane quantities used in #373.

For the pair-correlation leg use only the corrected v2 Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh formulas.

## Gates

J1 through J8 are frozen in issue #374 and incorporated by reference. In addition:

### J4a exact cross-Gram definition

For each finite zero window define

```text
Z_x(t)=sum_rho x^(rho-1/2)/(1-(rho-(1/2+it))^2),
G_T(x,y)=(2/pi) integral_R Z_x(t) conjugate(Z_y(t)) dt.
```

`G_T` is a Hermitian positive-semidefinite Gram kernel by definition. Derive its double-zero expansion before assigning any meaning to its exponent coordinates.

### J5a no compression by reconstruction

If knowing `G_T(x,y)` on an open two-variable set uniquely reconstructs the complete finite zero window, classify that as `RECONSTRUCTION`, not as a compressed source theorem. A useful `SOURCE` must identify the diagonal and functional-reflection aggregates by fixed operations that do not first solve for every zero.

## Decision

```text
SOURCE          fixed prime-side operations produce both pairings
PARTIAL         exact junction structure found but a source operation remains missing
RECONSTRUCTION  source family determines all zeros and only then the target
F               frozen class cannot supply the junction
STOP            source, domain, convergence, or typing incomplete
```

No status change follows from any outcome.