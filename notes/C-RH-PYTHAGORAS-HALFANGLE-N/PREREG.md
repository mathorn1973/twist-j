# PREREG C-RH-PYTHAGORAS-HALFANGLE-N

```text
STATUS:      NON-CANONICAL INCUBATION
AUTHORITY:   none
ISSUE LOCK:  #354
TARGET LINE: PUBLIC
LAYER:       analytic/number-theoretic only; no L1-L6 physical lift
```

## Frozen source identity

Primary analytic source for the first attack:

Masatoshi Suzuki, `Aspects of the screw function corresponding to the Riemann zeta function`, arXiv:2206.03682, current arXiv text dated 2026-03-22.

Use only the exact prime-side definition

```text
Psi(t) = 4(e^(t/2)+e^(-t/2)-2)
         - sum_(n <= e^t) Lambda(n)/sqrt(n) (t-log n),   t >= 0,
```

and Suzuki Theorem 1.7, `RH iff Psi(t) >= 0 for every real t`, as an imported classical theorem. No zero-side series may be used to prove a positive result in this incubation.

## Frozen exact rewrite targets

For `t >= 0`, define

```text
A(t) = 4 sinh(t/4),
P(t) = sum_(n <= e^t) Lambda(n)/sqrt(n) (t-log n),
b_n(t) = sqrt(Lambda(n)) n^(-1/4) sqrt((t-log n)_+).
```

Target R1:

```text
4(e^(t/2)+e^(-t/2)-2) = A(t)^2.
```

Target R2:

```text
P(t) = sum_n b_n(t)^2 = ||b(t)||_(ell^2)^2.
```

Imported consequence R3, only after R1-R2:

```text
RH iff ||b(t)||_(ell^2) <= A(t) for every t >= 0.
```

This is a reformulation, not an RH proof.

## Falsification-first questions

F1 LOCAL SCREW LEG. Test the naive claim that one delayed prime-power term is itself a positive screw/Gram kernel. For `h_L(t)=(|t|-L)_+`, polarize with `g=-h_L`. An exact negative principal minor or determinant falsifies independent-leg positivity.

F2 HALF-ANGLE CANONICITY. A specific `zeta_8=sqrt(i)` phase is not admitted merely because `1/4` occurs in amplitudes. Determine whether reconstructing a complex bilinear cross term from quadratic norm readings uniquely or minimally requires the pair `zeta_8, zeta_8^-1`, or whether an unrestricted phase family works equally. If no canonical selector is proved, record the zeta_8 link only as analogy or a compatibility witness.

F3 ONE-LEVEL-UP. Search for a non-circular block Gram object whose Schur complement equals the Suzuki scalar/kernel defect. The desired defect may not be inserted as a block by definition. Domains, positive blocks, and inverses must be explicit.

F4 ARCHIMEDEAN AMPLITUDE. Search for a natural larger amplitude carrier whose norm is exactly `A(t)^2` and in which the prime vector `b(t)` appears as an orthogonal projection or contractive image by an independently defined map. Defining the map from `b/A` is circular.

## Allowed computation

Exact symbolic arithmetic, integer/rational identities, and algebraic manipulation only for theorem-bearing results. Floating point may be used only as a labeled diagnostic witness and cannot decide any gate.

## Status discipline

Record only:

- candidate-T: exact derivation or theorem with complete proof;
- candidate-D: exact reformulation/dictionary resting on imported theorem(s);
- candidate-C: finite exact computation at stated scope;
- F: exact falsification within a frozen candidate class.

No RH, GRH, Weil positivity, J-native carrier, Born/decoder, physical, SI, or L1-L6 promotion is authorized.
