# PROMO C-RH-PYTHAGORAS-HALFANGLE-2-N

```text
STATUS: NON-CANONICAL PROMOTION PACKAGE
AUTHORITY: none
ISSUE: #355
PROMOTION: not executed
```

## What survived incubation

The useful result is stronger than the initial scalar square rewrite. On every finite Suzuki window, the complete source-side screw kernel has an explicit Krein-Gram factorization built only from pole, prime-power, and Gamma/Hurwitz data. No zero ordinate and no RH assumption enters this factorization.

### Candidate public theorem A: half-argument prime atoms

With Suzuki spectral variable

```text
s = 1/2 - i xi,
w = s/2 = 1/4 - i xi/2,
```

the square-root prime-power atom

```text
alpha_n(xi) = sqrt(Lambda(n)) n^(-w)
```

satisfies exactly

```text
|alpha_n|^2 = Lambda(n)/sqrt(n),
phase(alpha_n) = exp(i xi log(n)/2).
```

Thus the quarter-power amplitude and half-phase are the modulus and phase of the same half-argument Dirichlet atom. The archimedean completion simultaneously uses `Gamma(s/2)=Gamma(w)`.

Potential status after independent review: `T` at the stated analytic identity scope. No RH consequence by itself.

### Candidate public theorem B: source-side windowed Krein-Gram factorization

For every `a>0` and `|t|,|u|<=a`, construct explicit feature curves `X_(+,a)` and `X_(-,a)` from:

```text
pole:       one positive and one negative hyperbolic scalar feature,
primes:     half-angle sine/cosine features after truncating the original
            locally finite kernel at log n <= 2a,
Gamma:      positive OU increment features and one negative Brownian counterterm.
```

Then exactly

```text
G_g(t,u)
 = <X_(+,a)(t),X_(+,a)(u)>
   - <X_(-,a)(t),X_(-,a)(u)>.
```

The prime truncation occurs before the positive/negative split; no global infinity-minus-infinity Hilbert direct sum is claimed.

Potential status after independent review: `T` for the exact windowed factorization at Suzuki's source scope. No RH status movement.

### Candidate public theorem C: Gram-domination / contraction equivalence

For arbitrary feature curves `X_+,X_-`, the difference kernel

```text
K=<X_+,X_+>-<X_-,X_->
```

is positive semidefinite iff there exists a contraction from `closure(span X_+)` to `closure(span X_-)` carrying every `X_+(t)` to `X_-(t)`.

Combined only downstream with Suzuki's imported screw-positivity criterion, RH is equivalent to existence of such contractions on every finite window. This is a reformulation, not a proof.

Potential status: `T` for the abstract Gram lemma; `D` for the RH reformulation resting on Suzuki.

### Candidate public theorem D: the exact role of sqrt(i)

For the conjugate half-phase copies `E_+,E_-`, the normalized even/odd transform is

```text
U = 1/sqrt(2) [[1,1],[-i,i]],
U^*U=I,
det U=i.
```

The determinant-one lift requires a scalar `lambda` with `lambda^2=-i`; equivalently, up to the central sign and conjugation convention, an eighth-root phase `zeta_8=sqrt(i)` supplies the unique central correction into `SU(2)`.

This is a genuine exact appearance of the eighth root in the half-angle parity transform. It does not select a fixed eighth-root value for the variable prime phase and it does not affect Gram norms.

Potential status: `T` as pure two-channel complex linear algebra. No Born/decoder/RH bridge is asserted.

## Exact negative results to carry

1. The predecessor `C-RH-PYTHAGORAS-HALFANGLE-N` is integrity STOP because its frozen source equation omitted two archimedean terms.
2. One delayed prime-power screw leg is indefinite; the frozen two-point determinant is `-L^2/4`.
3. Bilinear reconstruction alone does not select `zeta_8`; `(3+4i)/5` is an exact competing phase witness.
4. No independent contraction can map one prime leg's sine half-angle trajectory to its cosine trajectory or vice versa. Hence a local `SU(2)` block, including its central eighth-root phase, cannot prove positivity.

## The actual next theorem target

Do not open a public RH theorem probe from the identities above. The scientifically meaningful next construction is:

```text
For each a>0, construct directly from the explicit source-side channels a
contraction / unitary colligation / block-Gram completion T_a such that
T_a X_(+,a)(t)=X_(-,a)(t) for all |t|<=a, prove ||T_a||<=1 without RH,
zero ordinates, or an already-positive Weil form, and prove compatibility
of the construction as a increases.
```

Because the local prime-by-prime contraction is exactly impossible, any surviving construction must globally mix prime quadratures and/or the pole/Gamma boundary channels.

A pointwise map defined from the desired inequality is circular and forbidden.

## Promotion boundary

None of the above changes RH, GRH, Weil positivity, the public lambda-cocycle lane, the Born/measure layer, the decoder, or any physical TWIST-J dictionary. Any public promotion requires a separate claim lock, collision review, independent mathematical audit, and a normal Canon fold.