# RAY-PICK-KERNEL consolidation: second audit, one-point criterion, synthetic detection (2026-08-20)

```text
STATUS:      NON-CANONICAL INCUBATION ADDENDUM 2 under this lock (#374)
ORIGIN:      second independent owner-side analysis, audited and consolidated
             with the first addendum by an agent session on the owner's
             instruction; new attack instruments run this session
AUDIT BASIS: Public Canon v54 ACTIVE, unchanged since the first addendum
             (main 483591d at audit time, SHA256SUMS 5 of 5 OK)
GATES:       J1-J8 crosswalk updated below; no J7 outcome claimed
FIREWALL:    no RH proof or evidence claim, no Canon, Registry, Frontier, or
             status movement, no L1-L6 lift; synthetic results are model
             statements, never statements about zeta
LABELS:      candidate grade only; process note: this lock froze on Public
             Canon v46, any future formal step re-gates against the current
             head first
```

## 0. Falsifiers first (new rows only; FA1-FA5 of addendum 1 stand)

```text
FB1  kills the recursion row A11: a pair (m,n) where
     2c J[m,n] + J[m-1,n] + J[m,n-1] != delta_{n0} M_m/m! + delta_{m0} M_n/n!.
FB2  kills the one-point criterion A10: a proof that J_N(c) PSD for all N
     is compatible with an off-critical zero, or a finite non-PSD J_N(c)
     while RH holds.
FB3  kills the Li bridge domain row A12: an off-critical zero configuration
     whose Li-Abel series converges beyond R = min |1 - 1/rho|, or a proof
     that R = 1 fails to imply the absence of off-critical zeros.
FB4  kills the endpoint identity A13: numerical or algebraic failure of
     4 lambda_1 - lambda_2 = 2 lambda_1 + sum_rho rho^-2 (unconditional)
     or of its RH form sum_{gamma>0} |rho|^-4.
FB5  kills the synthetic readouts: irreproducibility of the pinned breaker.
```

## 1. Convergence of the two audits

The second analysis and the first addendum agree on every candidate-T row:
Hadamard form, ell^2 involution model, ray equivalence for any parameter set
with a finite interior accumulation point, fixed-sequence determinant chain,
orbit mechanism with multiplicity-free negative index, unconditional
positivity of the diagonal, prime-side display for sigma > 1, single-moment
F verdict, narrowed scalar limit gate. Corrections of the second analysis
accepted into the record:

```text
C10  computational warning: the D_N chain at a_n = 1 + 1/n is severely
     ill conditioned; float sign readings prove nothing; certified work
     needs normalized kernels, LDL with interval arithmetic. The N <= 8
     witness of addendum 1 survives (pivot 1.3e-35 against a dps-40 noise
     floor ~1e-48) but the chain is the wrong instrument beyond small N.
C11  one off-critical quadruple {alpha, -alpha, conj alpha, -conj alpha}
     creates TWO nontrivial tau-orbits (upper and lower); the exact negative
     vector generally lies outside any finite span, so the theorem gives no
     effective bound on the first negative dimension.
C12  closed orbit contribution (verified):
     M_orb(a) = 4a (a^2 - x^2 + y^2) / |a^2 - (x+iy)^2|^2 > 0 for a > 1/2,
     the sharp form of the unconditional diagonal.
C13  boundary honesty at a = 1/2: the Dirichlet series no longer converges
     absolutely at s = 1; "prime-side without regularization" holds on the
     open ray a > 1/2, the endpoint aggregates go through continuation.
C14  the Suzuki operator route must go through canonical Weyl (Herglotz)
     functions Q_R, not bare characteristic functions with real zeros;
     gates S1-S5 adopted verbatim (canonical choice, positive residues,
     stable affine normalization, definedness at the nodes, limit is Q_xi
     and not merely a function with the same poles). Reported: the paper's
     own conjectural limit concerns normalized characteristic functions
     e^phi(R,z) W(R,theta;z) -> z^2 xi(1/2-iz)/xi'(1/2-iz), so the
     dictionary from that object to Q-functions is part of the gate.
```

## 2. Audit findings on the second analysis (this session)

```text
D1  Li bridge domain caveat. The identity
        M(a) = (1-r)^2 sum_{n>=1} lambda_n r^{n-1},  r = (a-1/2)/(a+1/2),
    is exact as stated only for r < R, where R = min_rho |1 - 1/rho| is the
    radius of the Li-Abel series; R = 1 iff there is no off-critical zero,
    and for r >= R the left side is the analytic continuation. So the
    unqualified boxed identity of the analysis needs this domain clause.
    R itself is another packaging of the criterion. On realistic heights
    the deficit is thin: an off-critical zero at height 14.13 with offset
    0.25 gives 1 - R = 1.25e-3.
D2  The margin of the first minor is razor thin for the true zeta:
    |c M'(c)| / M(c) measured 0.998844 (c = 0.6), 0.996802 (c = 1),
    0.930283 (c = 5). Endpoint limit exact:
        ratio -> (lambda_2 - 2 lambda_1)/(2 lambda_1) = 0.999197...,
    margin -> (4 lambda_1 - lambda_2)/(2 lambda_1) = 8.03e-4.
D3  Endpoint identity (A13, candidate-T, two lines): unconditionally
        4 lambda_1 - lambda_2 = 2 lambda_1 + sum_rho rho^-2,
    and under RH this equals sum_{gamma>0} |rho|^-4 = S4 in the upper
    convention of this lock. Numerically 3.71e-5, matching the S4 partial
    sums. The endpoint of det J_1 therefore measures the fourth-power rung
    of the S2 tower of #373: the derivative matrices at a = 1/2 read the
    S_{2k} aggregates.
D4  Whether J_1(c) >= 0 is unconditionally provable (an RH-empty fixed-N
    row, like the diagonal) is open; the synthetic data below show small-N
    detection is possible for low defects, so fixed-N rows are weak but not
    automatically empty. Only the full family carries RH.
D5  The [F as formulation] guard on "real spectrum gives Pick" is accepted;
    both earlier texts already conditioned on Weyl functions, the guard
    prevents the misreading, S1-S5 are the real content.
```

## 3. candidate-T (A10 one-point criterion, A11 recursion)

The one-point derivative criterion of the second analysis is verified:

```text
RH  <=>  J_N(c) = [ (1/(m! n!)) d^{m+n} K_ray/da^m db^n |_{a=b=c} ]_{m,n<=N}
         PSD for every N,   at any fixed c > 1/2.
```

Proof as in the ray theorem with derivative vectors u_m = v_c^{(m)}/m!,
u_m(alpha) = (-1)^m sqrt(m_alpha)/(c - conj alpha)^{m+1}: orthogonality to
all u_m kills all Taylor coefficients of the Cauchy transform at c, hence
d = 0 (completeness); the rest is the involution argument unchanged. The
map a -> v_a is norm-analytic near c (nearest singularity at distance
>= c - 1/2), so the Taylor-coefficient matrix is the Gram-with-J of the u_m.

NEW (this session, A11): multiplying K(a,b)(a+b) = M(a) + M(b) and matching
Taylor coefficients gives the closed recursion

```text
2c J[m,n] = delta_{n0} M_m/m! + delta_{m0} M_n/n! - J[m-1,n] - J[m,n-1],
J[-1,.] = J[.,-1] = 0,   M_k = M^{(k)}(c),
```

so the whole family J_N(c) is a finite exact function of the derivative
moments M_0..M_N at the single point, which the prime side supplies for
sigma = c + 1/2 > 1:

```text
M^(k)(c) = (-1)^k k! (s^-(k+1) + (s-1)^-(k+1)) + psi^(k)(s/2)/2^(k+1)
           + (-1)^(k+1) sum_{n>=2} Lambda(n) (log n)^k / n^s,   s = c + 1/2.
```

Zero-side form used for crosschecks and the synthetic model:
J[m,n] = (-1)^(m+n) sum_alpha m_alpha (c-alpha)^-(m+1) (c+alpha)^-(n+1).

Engineering honesty: at s = 3 the Lambda tail (sieve 3e6) swamps |M_k| for
k >= 9, and near s = 3/2 much earlier; the entries are exactly prime-side
in principle, but certified high derivatives need better tail handling than
the raw Dirichlet series. One-point pivots decay roughly geometrically at
~1e-3 per step (scale set by the first zero, ((c-1/2)/gamma_1)^2-ish):
far better than the collapsing chain, still ~3 digits per order, so
certified runs need precision linear in N.

## 4. Witness run (floats, labeled; no assertion rests on it)

```text
script          witness_jn_point.py    (project, claude/)
sha256(script)  e028f9db538c800590df3d4d6d841dbab9bd1e1157ddabe7017502d63fd096c4  (10219 bytes)
sha256(stdout)  6e39d1114dcd56e864a0e62763d2f63bbb5fbea6aa9390ea7d7322ac3b570a49  (1267 bytes)
P0 PASS  Cauchy-integral Taylor of M at c=1 vs direct (1e-62)
P1 PASS  recursion reproduces the closed J_1(c); det J_1(1) = 3.398e-6 > 0
P2 PASS  prime path vs analytic path for M_k at c = 5/2, k <= 12, within
         Lambda tails; sharp for small k, tail-dominated for large k
P3 PASS  |c M'(c)| < M(c) on the grid (margins in D2)
P4 PASS  J_16(1) LDL pivots all positive, p_16 = 6.1e-54
P5 PASS  zero-side sums vs recursion (500 zeros; (0,0) within zero tail,
         higher entries limited only by the 15-digit zero list)
P6 PASS  Li bridge at r = 0.15, 0.30 within budgets; lambda_1 zero-sum
         consistent with 1 + euler/2 - log(4 pi)/2
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC, Linux x86_64, CPython 3.11.15, mpmath 1.4.1; exit 0
```

## 5. Synthetic detection breaker (model only, labeled)

Model: 120 true on-line ordinates plus injected off-critical quadruples in
alpha-coordinates (+-x, +-y); kernel and J built from the zero-side forms;
sequential LDL pivots; chains at dps 300, J at dps 300; control clean.

```text
script          breaker_offcritical_detection.py    (project, claude/)
sha256(script)  8095138569d581baf66d5b09e593e3c31b712a7d7742d0a724428660a30f4b17  (6953 bytes)
sha256(stdout)  401486fa19e79a5149135bb519c26c621889d260888e88eb95ed5c585394640a  (2336 bytes)

injected (x, y)        I1 ray 1+1/n     I2 spread 0.4      I3 J_N(1)
(0.10, 14.1347)        N*=8  (-6e-36)   N*=8  (-1e-21)     N*=8  (-3e-23)
(0.25, 14.1347)        N*=7  (-4e-30)   N*=7  (-4e-19)     N*=7  (-6e-20)
(0.40, 14.1347)        N*=7  (-2e-29)   N*=7  (-3e-18)     N*=7  (-3e-19)
(0.25, 30)             N*=21 (-1e-121)  N*=21 (-2e-49)     N*=21 (-8e-69)
(0.25, 60)             none by N=24     none by N=24       none by N=48
double 14.13+60        N*=7, negs 2 of expected 4 (the height-60 pair
                       stays hidden at these sizes)
control (no injection) all pivots positive in all three instruments
negative count         exactly 2 per detected quadruple (= 2 orbits), as
                       predicted; multiplicity never multiplies the count
```

Readings, stated on the model only:

```text
R1  The mechanism is demonstrated end to end: off-critical orbits produce
    finite negative pivots, in every instrument, with the predicted count.
R2  Detection cost is height-driven and offset-blind: N* = 7-8 at height
    14.13 for every offset tried, N* = 21 at height 30, undetected by
    N = 48 at height 60. Empirically N* grows at least linearly in the
    defect height. This quantifies the house rank doctrine: a certified
    finite J_N(1) >= 0 is a height-bounded statement, roughly comparable
    to classical zero verification up to height ~2N, with entries from
    primes; it is not, and cannot be, RH progress by itself.
R3  Instrument choice moves the precision demand, not the detection size:
    all three instruments fire at the same N*, but the chain carries the
    signal at -1e-30 while spread nodes carry it at -1e-19. Practical
    order: spread nodes or one-point derivatives; never the 1+1/n chain.
R4  Li-Abel radius mechanism confirmed: R = 0.9131 for a synthetic low
    quadruple (x=0.40, y=2); the bridge partial sums converge at r = 0.80
    and diverge at r = 0.95 (0.088 -> 44.1 against a finite kernel value
    0.750), exactly the D1 caveat.
```

## 6. Citation state after both audits

```text
SETTLED    arXiv:2606.09096 is v1, submitted 2026-06-08; three metadata
           surfaces plus the second analysis concur; the earlier v2 /
           2026-08-17 dating is withdrawn from the record.
REPORTED   the section 7.7 display U = pi^(-1/2) Phat D, G = pi^(-1)
           Phat* Phat with the missing 1/pi in the displayed Gram identity,
           and Theorem 4.2 of arXiv:2301.00421v3 carrying the correct
           normalization: now reported by two independent sessions with
           consistent quotes; this session twice attempted direct
           re-verification (proxy rate limits, page truncation) and keeps
           the row at reported grade. Given the U/G display, the 1/pi in
           the Gram identity is forced, so the row is one look away from
           closing. Falsifier unchanged.
VERIFIED   arXiv:2301.05779v2 rows as in addendum 1.
```

## 7. Updated crosswalk (second analysis table, adopted with edits)

```text
J1 self-adjoint reflection form   candidate-T   realized by the involution J
J2 Cauchy tests                   candidate-T   complete ray family; endpoint
                                                aggregates = S2/lambda_1 rows
J3 single-function no-go          T-grade fact  diagonal unconditionally > 0
J4 polarized form                 candidate-T   K_ray(a,b); J_N(c) is its
                                                one-point polarization
J5 two-variable identifiability   candidate-T   from completeness
J6 origin of the 1/rho weight     PARTIAL       Li generating function and
                                                Cayley resolvent dictionary
J7 source positivity              O             the wall, unchanged
J8 breaker                        PASS AFTER CORRECTIONS (C10-C14, D1-D5)
```

## 8. Next targets

```text
T1 [O, the wall]  Euler-side proof of J_N(1) >= 0 for all N. Via A11 this
   is now a moment problem: the recursion-generated matrices from the
   prime-side sequence M_k(1) must be PSD. Under RH the entries are the
   polarized moments of a measure on the Cayley circle image of the
   critical line; the suggested frame is the trigonometric moment problem
   there, which connects this lock to the house Toeplitz branch. Any
   attempt must respect the R2 height bound: nothing finite closes it.
T2 [O]  canonical finite Weyl construction with gates S1-S5 and scalar
   convergence Q_R(i a_n) -> Q_xi(i a_n), or equivalently convergence of
   the finite resolvent moments at the single point c = 1 (then A10+A11
   finish). Includes the dictionary from e^phi W to Q-functions.
T3 [O, new small lane]  effective detection bound: prove, first on the
   model class, that a certified J_N(1) >= 0 excludes off-critical zeros
   below an explicit height f(N) (the data suggest f(N) ~ 2N). This would
   turn finite certified runs into honest height certificates with
   prime-side inputs.
T4 [recon]  endpoint ladder: det J_1 endpoint reads S4 (D3); check whether
   higher principal minors at a -> 1/2 read the S_{2k} tower, tying the
   one-point criterion to the #373 aggregates rung by rung.
```

## 9. What this consolidation does not do

No J7 verdict, no probe, no registry, frontier, Canon, or RH movement, no
claim on zeta from any synthetic run. The lock's frozen PREREG and BREAKER
stay untouched; the v46-basis re-gate note stands for any future formal
step. RH remains O.
