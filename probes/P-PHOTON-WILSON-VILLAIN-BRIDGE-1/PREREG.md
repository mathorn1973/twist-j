# P-PHOTON-WILSON-VILLAIN-BRIDGE-1

Status: `PREREGISTERED / UNRUN` at this file state.

```text
public claim issue:  #692
successor program:   PHOTON-MASSLESS-PHASE (non-canonical until fold)
target claim:        PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP
branch:              probe/P-PHOTON-WILSON-VILLAIN-BRIDGE-1
path:                probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1/
owner:               A. M. Thorn / current Codex owner session
action layer:        L4 one-face algebra only
proposed status:     T by the universal proof below; verifier is an audit
```

This probe creates no Canon, Registry, Frontier, dependency, gate, program,
or status change. A later sealed fold alone may consume its result.

## 1. Authority and lineage

The claim was opened against this verified authority:

```text
STATE:          ACTIVE
CANON:          Public Canon v71
TAG:            canon-v71
main:           7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
CONTENT_COMMIT: a77d720433c19976f9ab663d023ec9364eac34eb
CANON_SHA256:   0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
CANON_BYTES:    369836
policy run:     33313400934 PASS
```

The released roughening lock in issue #201 is not resumed. The sealed
`P-PHOTON-KAPPA-LEMMA-1` and the falsified `PHOTON-WINDOW-PROOF` are neither
reopened nor dependencies. This is a new narrow equality obstruction, not a
roughening certificate.

## 2. Equation, families, and allowed bridge

Put `phi=(1+sqrt(5))/2` and use the unnormalised `Z_5` Fourier transform

```text
(Ff)(k) = sum_(a=0)^4 f(a) zeta_5^(-ak).
```

The public one-face datum from `PHOTON-WINDOW-COORDINATES [T]` is

```text
w = (4, phi^2, phi^-2, phi^-2, phi^2),
Fw = (10,5,0,0,5) = 5(2,1,0,0,1).
```

For a vector and its transform define the unordered bi-support invariant

```text
Sigma(f) = sort(|supp f|, |supp Ff|).
```

Freeze exactly two finite-coupling families.

### Wilson family

For `beta>=0`,

```text
W_beta(a) = exp(beta cos(2 pi a/5)).
```

### Villain family

For `t>0`, freeze its character coefficients and position vector by

```text
(F V_t)(k) = sum_(n in Z) exp(-t(k+5n)^2),

V_t(a) = (sqrt(pi/t)/5)
         sum_(n in Z) exp(-pi^2(n-a/5)^2/t).
```

Define the automorphism action and the allowed direct bridge orbit by

```text
(P_u f)(a) = f(u a mod 5),  u in F_5^x,
O(f) = {c P_u F^epsilon f : c>0, u in F_5^x, epsilon in {0,1}}.
```

The composition order is exactly the displayed order. The frozen class is
the closure of positive normalization, `Z_5` automorphisms, and optional
Fourier exchange because the unnormalised transform obeys

```text
F P_u = P_(u^-1) F,
F^2 = 5 P_(-1).
```

Thus every word in the three generators reduces to one element of `O(f)`,
and every displayed element is such an allowed word.

No parameter limit, projective closure, translation, convolution, blocking,
domination, inequality, RG map, comparison theorem, or universality relation
is admitted.

The target theorem is that for every frozen finite parameter and every
allowed bridge operation, `w` is not the transformed positive multiple of a
Wilson or Villain vector.

## 3. Written universal proof

### 3.1 Public Fourier datum

For a symmetric five-vector `(x0,x1,x2,x2,x1)`, its `k`th transform is

```text
x0 + x1 (2 cos(2 pi k/5)) + x2 (2 cos(4 pi k/5)).
```

Use

```text
2 cos(2 pi/5) = (-1+sqrt(5))/2,
2 cos(4 pi/5) = (-1-sqrt(5))/2,
phi^2=(3+sqrt(5))/2,
phi^-2=(3-sqrt(5))/2.
```

Substitution gives `Fw=(10,5,0,0,5)`. Hence

```text
Sigma(w) = (3,5).
```

### 3.2 Wilson positivity

For `z=zeta_5^a`, expand without importing a Bessel table:

```text
exp((beta/2)(z+z^-1))
 = sum_(r,s>=0) (beta/2)^(r+s) z^(r-s)/(r!s!).
```

Finite Fourier summation therefore gives

```text
(F W_beta)(k)
 = 5 sum_(r,s>=0; r-s == k mod 5)
       (beta/2)^(r+s)/(r!s!).
```

The double series is absolutely convergent for every finite `beta`, as the
product of two exponential series. The outer Fourier sum is finite, so the
series and Fourier summation may be interchanged.

For `beta>0` every summand is nonnegative and the term `(r,s)=(k,0)`
is strictly positive for each `k=0,...,4`. Thus both `W_beta` and its
transform have full support and `Sigma(W_beta)=(5,5)`. At `beta=0`,
`W_0=(1,1,1,1,1)` and `F W_0=(5,0,0,0,0)`, so
`Sigma(W_0)=(1,5)`.

### 3.3 Villain positivity and Poisson identity

Every displayed character coefficient is strictly positive for `t>0`, since
it is an absolutely convergent sum of positive terms. To derive the
position-side display rather than assume it, inverse Fourier transform and
combine `m=k+5n`:

```text
V_t(a) = (1/5) sum_(m in Z) exp(-t m^2) exp(2 pi i a m/5).
```

For completeness, derive the needed Poisson identity at this exact Gaussian.
Put

```text
G_t(xi) = integral_R exp(-t x^2) exp(-2 pi i xi x) dx.
```

The integral and its `xi` derivative converge absolutely and uniformly on
compact `xi` intervals. Differentiating under the integral and using
`x exp(-t x^2)=-(1/(2t)) d(exp(-t x^2))/dx` gives

```text
G_t'(xi) = -(2 pi^2 xi/t) G_t(xi).
```

Integration by parts has zero boundary term because of Gaussian decay.
Moreover `G_t(0)>0` and, by squaring the integral and using polar coordinates,
`G_t(0)^2=pi/t`. The unique ODE solution is therefore

```text
G_t(xi) = sqrt(pi/t) exp(-pi^2 xi^2/t).
```

Now define the Schwartz function and its periodisation

```text
h_a(x) = exp(-t x^2) exp(2 pi i a x/5),
H_a(x) = sum_(m in Z) h_a(x+m).
```

The function and every derivative decay faster than any inverse power. Hence
the periodisation and its differentiated series converge absolutely and
uniformly on `[0,1]`, and its `n`th Fourier coefficient may be integrated
term by term. Unfolding the intervals gives

```text
integral_0^1 H_a(x) exp(-2 pi i n x) dx
 = G_t(n-a/5).
```

The coefficient sequence is absolutely summable by the displayed Gaussian
formula, so the Fourier series converges absolutely and uniformly to `H_a`.
Evaluating it at zero yields the specific Poisson identity

```text
sum_(m in Z) exp(-t m^2) exp(2 pi i a m/5)
 = sqrt(pi/t) sum_(n in Z) exp(-pi^2(n-a/5)^2/t).
```

Substitution into the inverse `Z_5` Fourier formula proves the displayed
position-side Villain expression. Every summand in the original character
coefficient sums and in the resulting position-space Gaussian sums is
strictly positive for `t>0`; hence every position entry and character
coefficient is strictly positive and `Sigma(V_t)=(5,5)`.

### 3.4 Obstruction

Positive normalization and a `Z_5` automorphism preserve both support sizes.
Fourier exchange swaps them, so it preserves their unordered pair. Since

```text
(3,5) != (5,5) and (3,5) != (1,5),
```

no allowed finite-coupling Wilson or Villain bridge equals `w`. This proves
the target for every frozen parameter, not merely for sampled couplings.

## 4. Accepted code

```text
file:    probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1/verify.py
bytes:   7388
sha256:  30af41ce20eb122405b130a8cb21bd4d55e1b0b53a749f57f655241179e19cc8
```

The accepted verifier uses only the Python standard library, `Fraction`, and
an exact two-coordinate implementation of `Q(sqrt(5))`. It uses no floating
point, analytic approximation, randomness, network, subprocess, clock, input
file, or write. It audits the finite Fourier arithmetic and the combinatorial
support consequences of the universal written proof; it is not the source of
the analytic theorem.

Before the immutable pin, syntax compilation and static review alone are
permitted. The formal command after pin and public readback is

```text
python3 probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1/verify.py
```

from the repository root under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
```

## 5. Systematics and prior exposure

The verifier freezes:

```text
G01 full support and golden reciprocity of w;
G02 exact transform (10,5,0,0,5);
G03 Fourier-square normalization on the symmetric datum;
G04 target bi-support (3,5);
G05 one explicit positive Wilson-series term in every residue;
G06 exclusion of beta>0 and beta=0 Wilson support pairs;
G07 positive-term witnesses on both Villain sides and support exclusion;
G08 all four Z5 automorphisms preserve bi-support;
G09 Fourier exchange preserves unordered bi-support;
G10 complete frozen-family support exclusion;
S01 replacing the two exact Fourier zeros destroys this support obstruction;
S02 beta=0 endpoint control;
S03 fresh-state transcript determinism.
```

The exact public Fourier zeros, the finite-coupling positivity obstruction,
the likely `FINITE-COUPLING-NONMEMBER` outcome, and the inapplicability of a
direct Wilson/Villain equality were exposed in public notes before this pin.
They are preparation, not evidence. No third-party bytes or theorem table is
consumed.

## 6. Outcomes, falsifier, and layer firewall

```text
FINITE-COUPLING-NONMEMBER
  the universal written proof is complete and every audit, execution,
  transcript, security, and architecture gate passes;

FINITE-COUPLING-MEMBER
  an exact admitted family, finite parameter, scale, automorphism, and
  Fourier flag give equality;

STOP
  authority, collision, family, endpoint, transform convention, equivalence,
  proof completeness, pin, integrity, transcript, security, or architecture
  requirements fail, or an auxiliary positivity, Poisson, or support lemma is
  exactly refuted without producing an admitted equality.
```

A failing runtime audit is `STOP` until independently diagnosed; it is not by
itself a scientific counterexample. No numerical threshold or tolerance
exists.

Action layer is `L4` only: one finite face-weight vector and its character
transform. A same-layer decision gate may later own this result, but this
probe creates no Canon gate. It performs no L4-to-L6 lift.

The theorem does not exclude a broader action class, a limit point,
domination, comparison, RG or universality bridge. It proves or refutes no
Gibbs measure, thermodynamic limit, roughening, Coulomb phase, massless pole,
propagator, continuum, polarization, apparatus, physical readout, or photon.
Those remain separate obligations of `PHOTON-MASSLESS-PHASE`.

## 7. Immutable sequence

1. Commit and push exactly `PREREG.md` and `verify.py`; never amend, rebase,
   squash, or force-push the pinned history.
2. Record pin commit, parent, hashes, bytes, blobs, and remote byte readback in
   issue #692.
3. Only then execute the accepted command once in a clean Linux-compatible
   checkout at the pin.
4. On exit 0 and empty stderr, add exact `EXPECTED.txt`, neutral `RUN.md`, and
   `RESULT.md` without changing either pinned file.
5. Push the additive result commit and open one PR changing this directory
   only. Require byte-identical x86_64 and aarch64 jobs before review and
   merge without squash or rebase.

No execution is authorized at this file state before the remote pin readback.
