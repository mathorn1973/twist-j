# RAY-PICK-KERNEL addendum (attack 2026-08-19, audited and posted 2026-08-20)

```text
STATUS:      NON-CANONICAL INCUBATION ADDENDUM under this lock (#374)
ORIGIN:      owner attack result (parallel owner session), independently audited,
             corrected, and posted by an agent session on the owner's instruction
AUDIT BASIS: Public Canon v54 ACTIVE, main 483591d, STATUS/POLICY/AGENTS/CORE/
             FRONTIER reread, canon/SHA256SUMS 5 of 5 OK, tag canon-v54 and
             content commit 0bfd67b4 confirmed ancestors of main
GATES:       context for J2 and J6 and the frozen source facts; no J7 outcome is
             claimed; the J4 cross-Gram lane is untouched
FIREWALL:    no RH proof or evidence claim, no Canon, Registry, Frontier, or
             status movement, no L1-L6 lift, no zero table inside any assertion
LABELS:      candidate grade only (candidate-T, candidate-D, candidate-C);
             nothing here is a public row; bare T labels from the attack draft
             are relabeled candidate-T per incubation discipline
```

## 0. Falsifiers first

```text
FA1  kills candidate-T A3: a finite a_1..a_N > 1/2 with [K_ray(a_i,a_j)] not PSD
     while RH holds, or PSD proved compatible with an off-critical zero.
FA2  kills candidate-T A4: a nontrivial orbit {alpha, tau alpha} whose vector
     e_alpha - e_(tau alpha) is not a J-eigenvector of eigenvalue -1.
FA3  kills candidate-T A5: RH false with all D_N > 0, or RH true with some D_N <= 0.
FA4  kills the single-moment F verdict: an unconditional proof of
     (1/pi)||G_a||^2 = M(a)/a on a set of a with a finite interior accumulation
     point that does not already prove RH.
FA5  kills the A9 route (not the implication): a proof that scalar convergence
     Q_R(i a_n) -> Q_xi(i a_n) on a_n = 1 + 1/n cannot hold for the finite
     self-adjoint extensions of the 2606.09096 construction.
```

## 1. Objects, in the frozen conventions of this lock

```text
X(z)       = xi(1/2 + z), even, entire, order 1, X(0) = xi(1/2) != 0.
alpha      = rho - 1/2 over zeros of xi, multiplicity m_alpha; |Re alpha| < 1/2
             strictly (no zeros on Re s = 1); the zero multiset is invariant
             under alpha -> -alpha and alpha -> conj(alpha), multiplicities kept.
tau alpha  = -conj(alpha).  In the lock coordinate rho = 1/2 - i z this is
             exactly z -> conj(z), the frozen reflection of Q_W.
M(a)       = X'(a)/X(a) = (xi'/xi)(1/2 + a), real analytic for a > 1/2.
K_ray(a,b) = (M(a) + M(b))/(a + b),  a, b > 1/2.
```

The whole addendum is one change of carrier: instead of the two-variable
cross-Gram of J4, take the one-parameter Cauchy family

```text
h_a(z) = 1/(a + i z) = 1/((a + 1/2) - rho),   a > 1/2,
```

and evaluate the lock's frozen reflection pairing on it. Exactly, with
absolutely convergent sums throughout:

```text
Q_W-pattern:  sum_z m_z h_a(z) conj(h_b(conj z)) = sum_alpha m_alpha /((a - alpha)(b + alpha))
                                                 = K_ray(a, b).
```

So K_ray is the reflection pairing of Cauchy tests, and the J2 target sits at
the endpoint: at a = b = 1/2 the pairing is sum m/(rho(1-rho)) = 2 lambda_1
(the sum stays absolutely convergent at the endpoint), the rho <-> 1-rho
symmetric closure of the 1/rho aggregate. For a > 1/2 no
regularization is involved anywhere (B6-clean): every entry is finite and has
the honest prime-side display of section 6 with sigma = a + 1/2 > 1.

## 2. candidate-T (A1, Hadamard form)

```text
K_ray(a,b) = sum_alpha m_alpha / ((a - alpha)(b + alpha)),   a, b > 1/2,
```

absolutely convergent. Proof. X is even of order 1, so X(z) =
X(0) prod_pairs (1 - z^2/alpha^2) absolutely; logarithmic differentiation
termwise gives M(a) = sum_pairs 2a/(a^2 - alpha^2). For one pair {alpha, -alpha}
the two partial fractions

```text
(a+b)/((a-alpha)(b+alpha)) = 1/(a-alpha) + 1/(b+alpha)
(a+b)/((a+alpha)(b-alpha)) = 1/(a+alpha) + 1/(b-alpha)
```

sum to 2a/(a^2-alpha^2) + 2b/(b^2-alpha^2), which is the pair's contribution to
M(a) + M(b). Summing pairs and dividing by a + b gives the display; absolute
convergence from sum 1/|alpha|^2 < infinity and |a - alpha| >= a - 1/2 > 0.
No conditional summation is used anywhere.

## 3. candidate-T (A2, the ell^2 model)

On ell^2 of the distinct zero locations define

```text
v_a(alpha) = sqrt(m_alpha)/(a - conj(alpha)),      (J f)(alpha) = f(-conj(alpha)).
```

J is well defined (m_(tau alpha) = m_alpha), is a self-adjoint unitary
involution, and

```text
K_ray(a,b) = < J v_a, v_b >.
```

Completeness lemma. If d is orthogonal to v_a for all a in a set A subset
(1/2, infinity) with a FINITE accumulation point, then the Cauchy transform
C_d(w) = sum d(alpha) sqrt(m_alpha)/(w - alpha), analytic on C minus the zero
set, vanishes on A, hence identically (identity theorem on a connected open
set); reading off residues gives d = 0. So span{v_a : a in A} is dense.

Correction to the attack draft: the accumulation point must be finite and lie
in the analyticity domain. A set marching only to infinity does not qualify.
The fixed sequence a_n = 1 + 1/n qualifies (accumulation at 1).

## 4. candidate-T (A3 equivalence, A4 mechanism, A5 determinant chain)

```text
RH  <=>  [K_ray(a_i, a_j)]_(i,j=1..N) PSD for every finite choice a_i > 1/2
    <=>  D_N = det [K_ray(a_i, a_j)]_(i,j=1..N) > 0 for every N, a_n = 1 + 1/n.
```

Proof. (=>) Under RH every alpha is fixed by tau, so J = I and the matrix is
the Gram matrix of v_(a_1)..v_(a_N); Cauchy vectors at distinct points are
linearly independent (a vanishing finite rational combination cannot vanish at
infinitely many zeros), so the Gram matrix is positive definite and every
D_N > 0.

(<=) PSD on all finite subsets of A gives < J f, f > >= 0 on the closed span
of {v_a : a in A}, which is all of ell^2 by section 3 whenever A has a finite
accumulation point; in particular for the fixed sequence. A self-adjoint
involution with a nonnegative form is the identity: for any nontrivial orbit
{alpha, tau alpha},

```text
J (e_alpha - e_(tau alpha)) = -(e_alpha - e_(tau alpha)),
```

an explicit negative direction (A4). So J = I, hence -conj(alpha) = alpha for
every zero, hence Re rho = 1/2. For the determinant chain: a non-PSD principal
submatrix sits inside the N-th leading block, so by Sylvester some leading
minor D_M with M <= N is <= 0.

Negative index. The negative index of the kernel equals the number of
nontrivial tau-orbits of distinct zero locations (each orbit contributes one
-1 direction; multiplicities do not multiply the count).

Prior-art boundary, stated so nothing is oversold. The forward direction is
classical in substance: under RH, M is a positive real function and the
half-plane Nevanlinna kernel of any such function is PSD. The converse from
the ray alone can also be assembled classically: Nevanlinna-Pick interpolation
at the real nodes plus the identity theorem forces M to extend positive-real
to the full right half plane, which forbids poles with Re alpha > 0, and the
functional symmetry kills the left side; the scalar half-plane criterion
Re (xi'/xi)(s) > 0 on Re s > 1/2 iff RH is Lagarias 1999. What this carrier
adds is not the equivalence as such but (i) the explicit mechanism, one
negative direction per off-critical orbit, with the negative index counting
orbits, (ii) the fixed one-parameter determinant chain D_N, and (iii) the
strictly prime-side entries of section 6. No claim of novelty beyond that.

## 5. candidate-T (A6, the lock's H2 difference is a projection norm)

In the model of section 3, with v = v_(1/2) (the endpoint Cauchy vector,
v(alpha) = sqrt(m_alpha)/conj(1 - rho)) and P_minus = (I - J)/2 the projector
onto the -1 eigenspace of J:

```text
||v||^2 = sum m/|rho|^2 = 2 S2,        < J v, v > = sum m/(rho(1-rho)) = 2 lambda_1,
S2 - lambda_1 = ||P_minus v||^2  >=  0,
```

and P_minus v = 0 forces every orbit trivial (the entries of v never vanish and
v(alpha) = v(tau alpha) rearranges to alpha = tau alpha). Hence

```text
S2 = lambda_1  <=>  RH,
```

with the defect S2 - lambda_1 exactly the squared negative-part projection of
the 1/rho-type Cauchy vector. This is the frozen #373/#374 aggregate
S2 - lambda_1 >= 0 with its equality case and mechanism attached. The
equivalence itself is presumably classical folklore; the projection-norm form
of the defect is the useful new packaging for this lock. Upper-half
convention: S2 = sum_(gamma>0) 1/|rho|^2, full-zero sums are twice, per the
frozen PREREG convention.

## 6. candidate-T (A7, prime side)

For sigma = a + 1/2 > 1, absolutely convergent:

```text
M(a) = 1/sigma + 1/(sigma - 1) - (1/2) log pi + (1/2) psi(sigma/2)
       - sum_(n>=2) Lambda(n)/n^sigma.
```

Every entry of K_ray on the ray a > 1/2 is therefore a two-term archimedean
block plus an honest von Mangoldt sum in its convergence range: B6-clean, no
Perron factor, no regularization, no zero input. Engineering remark, labeled:
convergence of the Lambda sum slows toward a = 1/2; the criterion is exact,
not a fast numerical scheme.

Audit addition (unconditional diagonal). Each zero quadruple contributes
2(a-x)/((a-x)^2+y^2) + 2(a+x)/((a+x)^2+y^2) > 0 to M(a) for a > 1/2 > |x|,
so M(a) > 0 on the whole ray REGARDLESS of RH. Consequences: D_1 > 0 always;
the diagonal of K_ray carries no RH information; any falsity witness is
necessarily off-diagonal, consistent with the mechanism living in orbit
differences, and the scalar Lagarias criterion restricted to the real axis is
unconditionally true, which is why the matrix upgrade is the minimal
RH-complete object on this ray.

## 7. Junction to Suzuki's G_1 (verified today against 2301.05779v2)

Verified verbatim this session: G_n(z) = H_n(1/2 - iz) (1.7); Theorem 1.1
lambda_n = (1/(2 pi)) ||G_n||^2 (1.8), restated for n = 1 as (4.1); the
expansion (3.6) G_n = sum_gamma sqrt(pi m_gamma) [1 - (1 - 1/rho)^n] F_gamma,
whose n = 1 weight is exactly 1/rho. So the J2/J6 vector 1/rho is Suzuki's
G_1 up to his model-space basis, and lambda_1 = (1/(2 pi)) ||G_1||^2 is his
norm identity. Also verified verbatim: the stated obstacles, integrals
"difficult to handle without using the general theory of model spaces which
can be applied under the Riemann hypothesis", and the necessity to "deal with
the zeros of xi(s) + xi'(s) whose relation to the zeros of xi(s) is unclear".
The attack draft's paraphrase "cannot remove the off-diagonal Gram" is
replaced by these verbatim quotes.

## 8. candidate-D (A8, the Laplace family and the single-moment F)

Owner derivation, not independently re-derived in this audit: for
h_a(t) = e^(-a t) 1_(t>0) the transform closes to

```text
G_a(z) = (i/2) [ (1 + M(a)) - (1 - M(a)) Theta(z) ] / (z + i a),   Theta = E#/E,
(1/pi) ||G_a||^2 - M(a)/a
    = ((1 - M(a)^2)/(2a)) [ Theta(i a) - (a/pi) integral_R Re Theta(x) /(x^2 + a^2) dx ].
```

Audit consistency check, exact witness: M(1/2) = lambda_1 = 1 + euler/2
- (1/2) log(4 pi), confirmed to 41 digits (witness W3 below), so at a = 1/2
the family identity (1/pi)||G_(1/2)||^2 = M(1/2)/(1/2) = 2 lambda_1 is
exactly Suzuki's (1.8)/(4.1). F verdict, as a general mechanism, kept from
the attack draft and sharpened: one scalar equality at one point cannot
rigidify a meromorphic object; by contrast the same equality on a set of a
with a finite interior accumulation point forces (identity theorem, Poisson
integral analytic in Re a > 0 against Theta(i a) meromorphic) removability of
the upper poles of Theta and hence RH via the owner-cited Proposition 3.1.
The Li sequence lambda_n is the Taylor jet of this family at a = 1/2: one
moment versus the whole pole channel. Status of the two displays above:
candidate-D pending an independent re-derivation; FA4 is their falsifier.

## 9. candidate-T (A9, the narrowed limit gate toward 2606.09096)

If Q_R are Nevanlinna functions of the finite self-adjoint extensions in the
screw-function construction, then their half-plane Pick kernels are PSD at
the nodes i a_n by definition, and entrywise scalar convergence

```text
Q_R(i a_n) -> Q_xi(i a_n),   a_n = 1 + 1/n,
```

already suffices for RH: PSD passes to entrywise limits, and section 4 needs
only the fixed sequence. This is a genuinely weaker gate than locally uniform
convergence of characteristic functions or a two-variable Gram identity.
Honesty clause: the full arithmetic difficulty now lives inside the countable
scalar limit; this narrows the gate, it does not open it.

## 10. Citation audit

```text
VERIFIED   arXiv:2301.05779v2, Li coefficients as norms of functions in a
           model space: (1.7), (1.8), (4.1), (3.6), obstacle quotes as in
           section 7.
VERIFIED   arXiv:2606.09096 exists, M. Suzuki, Weil's quadratic form via the
           screw function, submitted 2026-06-08; this lock's frozen source.
UNCONFIRMED, CORRECTED TO v1   the attack draft cites a v2 dated 2026-08-17.
           Three metadata surfaces consulted today (the arxiv abstract page
           and two independent mirrors) show only the 2026-06-08 submission
           and no revision. This addendum therefore cites 2606.09096 (v1) and leaves
           the v2 / 2026-08-17 dating to the owner to re-pin; the falsifier is
           one look at whether arxiv.org/abs/2606.09096v2 resolves.
OWNER-REPORTED, NOT REVERIFIED HERE   the section 7.7 operator display
           U = pi^(-1/2) Phat D, G = pi^(-1) Phat* Phat with an allegedly
           missing 1/pi in the displayed Gram identity
           (1/pi) integral S_x conj(S_y) = g(x-y) - g(x) - g(-y) + g(0);
           and Theorem 4.2 of arXiv:2301.00421v3 carrying the correct 1/pi.
           The full-text fetch path from this session was rate limited; the
           claim is decidable by one look at the displays and is left at
           owner-reported grade with that falsifier.
OWNER-REPORTED   the reminder of the classical equivalence RH iff Q_xi is
           Nevanlinna in arXiv:2206.03682; the equivalence itself is classical
           (Hermite-Biehler circle; scalar half-plane form Lagarias 1999) and
           nothing here depends on the pointer.
```

## 11. Engineering witness (floats, labeled; no assertion rests on it)

```text
script          witness_kray_ray_pick.py   (archived in the project, claude/)
sha256(script)  946f602c5b359a72ac4c0f534b78f24c9816d97e5d98629c1eca34feca5d5fce  (4979 bytes)
sha256(stdout)  110cb645f666cd0292b9258b784f4e5c3fa9accd8a1d7ae0930c71d9feaff09b  (1016 bytes)
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC, Linux x86_64, CPython 3.11.15, mpmath 1.4.1; exit 0
W1 PASS  Hadamard identity vs first 500 zeros at three (a,b), residual equal
         to the engineering tail estimate 2.3e-3
W2 PASS  D_1..D_8 > 0 for a_n = 1 + 1/n (D_8 = 1.1e-134 > 0), min eigenvalue
         4.4e-37 > 0 at dps 40
W3 PASS  M(1/2) = lambda_1 = 0.0230957..., agreement 8.6e-42
W4 PASS  M(a) > 0 on a grid in (1/2, 10] (diagonal unconditional positivity)
W5 PASS  prime/archimedean display vs direct xi'/xi at sigma = 2, 3 within
         the Lambda tail bounds (1.0e-6, 5.0e-13)
```

All decimals above are computed witnesses, not conclusions.

## 12. Corrections applied to the attack draft

```text
C1  completeness needs a finite accumulation point (section 3); stated.
C2  bare [T] labels relabeled candidate-T; no public probe has run.
C3  diagonal of K_ray is unconditionally positive; all RH content is
    off-diagonal; Lagarias 1999 named as the scalar prior art (section 6).
C4  prior-art boundary of the equivalence stated (section 4): both directions
    are classically assemblable; the contribution is the mechanism, the fixed
    determinant chain, and the prime-side carrier, not the equivalence as such.
C5  the Sylvester step in the D_N direction made explicit.
C6  multiplicity bookkeeping made explicit (sqrt(m) in v_a, m preserved by
    tau); negative index counts orbits of locations, multiplicity-free.
C7  the paraphrase of Suzuki's obstacles replaced by verbatim quotes
    (section 7); the 2606.09096 v2 date and the 7.7 normalization left at
    owner-reported grade with an explicit falsifier (section 10).
C8  transport-mangled displays (missing equality signs) restored.
C9  new section 5: the lock's aggregate S2 - lambda_1 identified as
    ||P_minus v_(1/2)||^2, giving the equality case S2 = lambda_1 iff RH
    with the same orbit mechanism.
```

## 13. What this addendum does not do

No SOURCE, PARTIAL, RECONSTRUCTION, F, or STOP verdict of the lock's J7 bar
is claimed or moved. The J4 cross-Gram lane and its breaker are untouched.
No registry, frontier, Canon, or RH status changes. The open obligations
stand as frozen: a proof of global PSD of K_ray from the Euler side without
zero input, or the scalar limit gate of section 9; and an independent
re-derivation of the section 8 displays.
