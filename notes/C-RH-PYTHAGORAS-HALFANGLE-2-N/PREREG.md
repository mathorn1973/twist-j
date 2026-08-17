# PREREG C-RH-PYTHAGORAS-HALFANGLE-2-N

```text
STATUS:      NON-CANONICAL INCUBATION
AUTHORITY:   none
ISSUE LOCK:  #355
TARGET LINE: PUBLIC
LAYER:       analytic/number-theoretic only; no L1-L6 physical lift
PREDECESSOR: #354 STOP, source equation incomplete
```

## Frozen primary source

Masatoshi Suzuki, `Aspects of the screw function corresponding to the Riemann zeta-function`, arXiv:2206.03682v4, PDF equation (1.1), page 1.

For `t >= 0`, freeze exactly

```text
Psi(t) = A_full(t) - P(t),

P(t) = sum_(n<=e^t) Lambda(n)/sqrt(n) (t-log n),

A_full(t) = 4(e^(t/2)+e^(-t/2)-2)
            + (t/2)[psi(1/4)-log pi]
            + (1/4)[C - e^(-t/2) Phi(e^(-2t),2,1/4)],

C = pi^2 + 8 Catalan = zeta(2,1/4).
```

Imported classical theorem only: Suzuki Theorem 1.7, `RH iff Psi(t)>=0 for every real t`.

No zero-side series, RH assumption, or positive Weil form may be used as input to a positive construction.

## Frozen objects

For `t >= 0` define

```text
A0(t) = 4(e^(t/2)+e^(-t/2)-2),
A(t)  = 4 sinh(t/4),
R_inf(t) = A_full(t)-A0(t),

b_n(t) = sqrt(Lambda(n)) n^(-1/4) sqrt((t-log n)_+).
```

## Gates

G1 PRIME AMPLITUDE

Prove exactly

```text
Lambda(n)/sqrt(n) = [sqrt(Lambda(n)) n^(-1/4)]^2
P(t) = sum_n b_n(t)^2.
```

G2 ARCHIMEDEAN PERFECT SQUARE

Prove exactly

```text
A0(t) = A(t)^2 = [4 sinh(t/4)]^2.
```

No statement that `A_full` is itself this square is allowed.

G3 LOCAL-LEG BREAKER

For `L>0`, let `h_L(t)=(|t|-L)_+`, `g_L=-h_L`, and

```text
G_L(t,u)=g_L(t-u)-g_L(t)-g_L(-u)+g_L(0).
```

Test the exact `2 x 2` principal matrix at `t=L/2`, `u=3L/2`. A negative determinant falsifies independent delayed-leg positivity.

G4 FULL ARCHIMEDEAN CORRECTION

Starting only from the frozen `R_inf`, derive a valid exact convergent/renormalized representation. Any cancellation involving a divergent harmonic series must be performed before termwise interpretation. Determine whether `R_inf` is positive, negative, indefinite, or naturally a difference of positive objects.

G5 HALF-ANGLE CANONICITY

For a complex Hilbert inner product, analyze quadratic polarization by phases. Determine the complete condition on phase pairs that reconstruct both real and imaginary cross terms. `zeta_8=sqrt(i)` is selected only if a separately stated and justified minimal/balanced condition forces it up to trivial symmetries. Otherwise record non-uniqueness.

G6 ONE-LEVEL-UP

Search for a manifestly positive block Gram object with an exact non-circular Schur complement equal to `Psi` or the full Suzuki kernel on a frozen test class. The target defect may not be inserted by definition. All blocks, domains, inverses, quotients, and maps must be independently defined.

G7 DERIVATIVE / CONVEX-DUAL DIAGNOSTIC

It is permitted to derive exact piecewise formulas from the prime-power knots `t=log n`, including derivatives and Legendre transforms of the explicitly known archimedean terms. Such formulas are candidate-T only if proved symbolically; finite prime sweeps are candidate-C diagnostics only.

## Status discipline

Only candidate-T, candidate-D, candidate-C, or exact F results may be recorded. No RH/GRH proof, Weil positivity, J-native carrier, Born/decoder promotion, physical reading, SI statement, or L1-L6 lift is authorized.
