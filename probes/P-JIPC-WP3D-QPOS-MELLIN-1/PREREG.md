# P-JIPC-WP3D-QPOS-MELLIN-1 preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**. Public claim lock
#777 was opened before this pin. The accepted `verify.py` may be
read, parsed, compiled and inspected statically, but it has never
been imported or executed. This complete `PREREG.md` and
`verify.py` are committed together; the full immutable pin SHA is
recorded externally on issue #777 and, after a completed run, in
`RUN.md`.

```text
PROBE_ID            P-JIPC-WP3D-QPOS-MELLIN-1 (claimed by issue #777)
MODE                PROOF-FIRST / RESULT-EXPOSED
ACTION_LAYER        L1 (exact rational algebra and real analysis only)
THEOREM_CARRIER     WRITTEN_PROOF_NOT_FINITE_AUDIT
ORIGINAL_DRAFT_DATE 2026-08-26
PREREG_DATE         2026-09-01
AUTHOR_OF_RECORD    A. M. Thorn
OWNER               A. M. Thorn
CLAIM_LOCK          #777
PIN                 EXTERNAL (the immutable commit containing these bytes;
                    full SHA recorded on issue #777 and, on the
                    completed-run route, in RUN.md)
DEV_EXECUTION       NONE (verify.py syntax-checked only; never run)
```

## Authority pin

```text
STATE:          ACTIVE
CANON:          Public Canon v74
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v74
TAG_OBJECT:     796b09aef958a9021b93cff0df7f300ef95f5337
TAG_TARGET:     05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT: 2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:   2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:    389246
BASE_COMMIT:    1cf954b4c7f9fed1b3ad1cd724b493714369de37
```

Provenance record. The notes-lane basis tuple was first written
against Public Canon v65, moved to v72 on 2026-08-31 by owner
decision, and moved to v74 on 2026-09-01 while still unclaimed and
unrun. Public claim lock #777 refroze the complete tuple above and
the exact lock-time `BASE_COMMIT`; this preregistration copies those
locked values unchanged. The parent
`P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1` merged at
`9a4b479b0a7a9ce39772f77f16dd363602ec72c7` and is an ancestor of
the base. No TWIST-J Registry row is consumed. `DEV_EXECUTION`
remains `NONE`.

## 0. Aim, parents, and the provenance fence

This probe proves the **rational-slice Mellin package**: on the
positive rationals, the seed families `C, B, E, O` exist with
algorithmic tail moduli and satisfy the product identity, the
square-root-free duplication, a **self-contained public bridge**
`C(1/2)^2 = p_I`, the **public Machin bridge** `p_I = p_M`, and the
dressed slice `Ehat(s) Ohat(s) = Chat(s)` typed to `p_M`.

Public parent (definition only, no theorem consumed):

```text
P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1
  merged at 9a4b479b0a7a9ce39772f77f16dd363602ec72c7
  consumed surface: the frozen Machin-series Cauchy name
    p_M = 16 A_5 - 4 A_239,  A_q = the unique common point of the
    alternating intervals with a_(q,n) = 1/((2n+1) q^(2n+1)),
  and the dressed seed tuples E=(2,1,0,1), O=(2,1,1,1), C=(4,2,0,2).
```

Only the *name* is consumed: the well-definedness of `A_q` (existence
and uniqueness of the common point) is re-proven inside this probe
(Q7 Step 0), so no WP3E theorem is a premise.

**Reading-family discipline (POLICY.md §4): NOT_APPLICABLE.** This
probe proposes no family of physical readings, no decoder, no
selection and no occurrence clause. The only uniqueness statements it
asserts are mathematical and name their class and equivalence:
(1) the unique real common point of the nested alternating rational
Machin intervals `hull(S_(q,N), S_(q,N+1))` — class: real numbers
contained in every such hull; equivalence: equality in `R`
(Q7 Step 0); (2) the unique positive real `n`-th root of a positive
real — class: positive reals `y` with `y^n = x`; equivalence:
equality in `R` (TCB item 7). No other uniqueness is claimed.

**Provenance fence.** No private artifact is a premise: the internal
WP3B/WP3C/WP2 lineage, `PI_ATAN_GAUSS_TYPED_IDENTITY`, and the
notes-lane files under `notes/C-JIPC-MELLIN-LADDER-N/` are discovery
context at most — not evidence, not premises, not edges of the proof
graph. The bridge source of this probe is

```text
BRIDGE_SOURCE_QPOS = PUBLIC_SELF_CONTAINED (Claim Q6 below)
```

## 1. Frozen constants

```text
F_I  := integral_0^1 dt/(1+t^2)      (this probe's integral name)
p_I  := 4 F_I
p_M  := 16 A_5 - 4 A_239             (public WP3E Machin name)
```

`F_I` is a compact Riemann integral of a continuous rational
integrand; it exists by the TCB alone. `p_I` and `p_M` carry distinct
Cauchy names; their equality is **Claim Q7**, never an assumption.
No identification with any circle, Gaussian, Gamma, SI, physical, or
library constant is made or implied.

## 2. TCB — `RATIONAL_MELLIN_TCB/v1` (positive list, self-contained)

1. Exact `Z`/`Q` arithmetic, finite search, exact inequalities.
2. The complete ordered real field; monotone completeness; the
   Archimedean property and cofinality of rational cuts.
3. The compact oriented Riemann integral of continuous functions on
   rational and real compact intervals: linearity, additivity,
   positivity, the fundamental theorem of calculus, and continuity
   of partial integrals of continuous integrands on compact
   rectangles.
4. Compact Fubini on rectangles: for a continuous integrand on
   `[a,b] x [c,d]`, the two iterated integrals agree; the square
   splits along its diagonal (zero content) into two triangles.
5. One-dimensional `C^1` substitution with positive derivative on
   compact intervals; affine reflection.
5a. The derivative calculus of finite combinations on intervals:
   sum, product, quotient away from zeros of the denominator
   (in particular derivatives of rational functions), and
   composition with affine maps; the derivatives of `exp` (item 6)
   and of rational powers (item 7) compose accordingly.
6. The real exponential by its power series, with the rational tail
   envelope `sum_(k>N) R^k/k! <= (R^(N+1)/(N+1)!) / (1 - R/(N+2))`
   for `N+2 > R`, the product law `exp(x+y) = exp(x) exp(y)`,
   positivity, derivative, and the elementary bounds `exp(x) >=
   x^m/m!` for `x >= 0` and every integer `m >= 0`.
7. **POW-RAT** (rational powers of positive reals), with the full
   derivation graph:
   `POLYNOMIAL_CONTINUITY_AND_UNBOUNDEDNESS ->
   POSITIVE_NTH_ROOT_EXISTENCE_BY_SUPREMUM ->
   ROOT_UNIQUENESS_AND_ORDER -> ROOT_CONTINUITY ->
   POW_RAT_DERIVATIVE`; the derivative by the direct telescoping
   identity `z_h - z = h / sum_(j=0)^(n-1) z_h^(n-1-j) z^j`; the
   explicitly registered chain rule; the law package
   (representation independence, `x^(r+r') = x^r x^(r')`,
   `(xy)^r = x^r y^r`, `(x^r)^(r') = x^(r r')`, `x^(-r) = 1/x^r`);
   monotonicity and continuity on `(0,inf)`; and the zero-limit
   certificate: for `r = m/n > 0` and `0 < eps <= 1`,
   `0 < x < eps^n  =>  x^(1/n) < eps  =>  x^(m/n) <= x^(1/n) < eps`,
   with the convention `x^0 = 1`. Realizing `x^r` through
   `exp(r log x)`, a logarithm, or an irrational exponent is outside
   the class.
8. **TRUNC-0**: two-ended compact cuts `int_delta^R` with monotone
   limits at both ends, `C(s) = sup_N C_(1/N,N)(s)` over rational
   cuts; the cofinality lemmas for the cut nets `(delta,R) ->
   (delta^2, R^2)` and, for every fixed positive real constant `a`,
   `(delta,R) -> (a delta, a R)`.

Nothing else. In particular: no Gamma or Beta theory, no circle
constant, no trigonometry, no complex variable, no Fourier, no
Poisson, no Tonelli on infinite regions, no Lebesgue theory, no
logarithm.

## 3. Definitions (no cross-reading)

For rational `s > 0`, as two-ended cut limits in the sense of TRUNC-0:

```text
C(s)   = integral_0^inf x^(s-1) e^(-x) dx
B(p,q) = integral_0^1  u^(p-1) (1-u)^(q-1) du
E(s)   = integral_0^inf x^(s-1) e^(-x^2) dx
O(s)   = integral_0^inf x^(s-1) * (x e^(-x^2)) dx
```

`O` reads the odd seed `x e^(-x^2)` independently; defining
`O := E(s+1)` is forbidden cross-reading — the equality is the
proven join node (Q2d). Dressed seeds, weight `p_M`:

```text
Ehat(s) = 2 integral_0^inf e^(-p_M x^2) x^(s-1) dx
Ohat(s) = 2 integral_0^inf e^(-p_M x^2) x^s     dx
Chat(s) = 4 integral_0^inf e^(-2 p_M r^2) r^(2s-1) dr
```

The quadratic form of `Chat` is primary; the linear form is the
proven pullback (Q8a).

## 4. Claims and written proofs

Throughout, `s = a/c`, `p`, `q` are positive rationals in reduced
form; `k`-type symbols are integers. Every improper integral is a
TRUNC-0 limit; the order compact cuts -> limit -> moduli is binding,
and no tail symbol appears before the limit object exists.

### Q1 — Seed existence with algorithmic tail moduli

**Claim.** `C(s)`, `B(p,q)`, `E(s)`, `O(s)` exist, are finite and
positive, and carry the output-form modulus algorithms below: given
target `2^(-b)` they output explicit rational `(delta, R)` with
`0 <= X - X_(delta,R) <= 2^(-b)`.

**Proof.** Cut estimates first. For rational `0 < eps < delta <= 1
<= R < T` and integer `k >= s-1`:

```text
(M0')   0 <= int_eps^delta x^(s-1) e^(-x) dx <= (delta^s - eps^s)/s
(Minf') 0 <= int_R^T x^(s-1) e^(-x) dx <= (k+2)! (1/R - 1/T)
```

(M0') by `e^(-x) <= 1` and FTC with primitive `x^s/s` (POW-RAT).
(Minf') by `x^(s-1) <= x^k` for `x >= 1` and the series bound
`e^x >= x^(k+2)/(k+2)!`, so `x^k e^(-x) <= (k+2)!/x^2`, and FTC with
primitive `-1/x`. The cut net is monotone and bounded above by
`1/s + (k+2)!`; monotone completeness gives `C(s) = sup_N
C_(1/N,N)(s)` with `0 < C(s) < inf`, and only now, as limits of the
cut estimates, the moduli

```text
(M)  0 <= C(s) - C_(delta,R)(s) <= delta^s/s + (k+2)!/R .
```

Universal envelope: for reduced `r = a/c > 0` define

```text
D_b(r) := 2^(-ceil(c(b+1+c)/a)),   then   D_b(r)^r / r <= 2^(-(b+1)),
```

since `D_b(r)^r <= 2^(-(b+1+c))` (ceiling) and `1/r = c/a <= c <=
2^c`. All exponent comparisons are integer comparisons on `2`-powers.

Algorithms (each output is an explicit rational pair):

```text
C(s):    delta_b = D_b(s),          R_b = (k+2)! 2^(b+1),  k = ceil(s-1)
E(s):    delta_b = D_b(s),          R_b = l_E! 2^(b+1),
         k_E = ceil(s-1), l_E = ceil((k_E+2)/2)
O(s):    delta_b = D_b(s+1),        R_b = l_O! 2^(b+1),
         k_O = ceil(s),   l_O = ceil((k_O+2)/2)
B(p,q):  delta_b = D_(b+1)(p),      delta'_b = D_(b+1)(q)
```

For `E`, `O` the Gaussian tail uses `e^(x^2) >= x^(2l)/l!` with
`2l >= k+2`, so `x^k e^(-x^2) <= l!/x^2` on `x >= 1` and the tail is
`<= l!/R`. For `O` the lower cut is `int_0^delta x^s dx =
delta^(s+1)/(s+1) <= 2^(-(b+1))` with `delta = D_b(s+1)`; if
`s = a/c` is reduced then `s+1 = (a+c)/c` is reduced. For `B` the
modulus output is the pair `(delta, delta')`. At the lower end, on
`(0,1/2]` the co-factor obeys `(1-u)^(q-1) <= max(1, 2^(1-q)) <= 2`
for every `q > 0`, so the cut contributes
`<= 2 D_(b+1)(p)^p / p <= 2^(-(b+1))`. At the upper end the roles of
`p` and `q` swap: on `[1/2,1)` the co-factor obeys
`u^(p-1) <= max(1, 2^(1-p)) <= 2` and the cut `delta'_b =
D_(b+1)(q)` bounds the `(1-u)`-factor's contribution by
`2^(-(b+1))`; equivalently, apply the lower-end estimate to `B(q,p)`
under the reflection `u -> 1-u` (Q2). Each total is `<= 2^(-b)`.
Scope: the modulus label covers the bare seeds `C, B, E, O` only;
the dressed seeds carry existence (Q8) but no modulus claim.
**QED Q1.**

### Q2 — Anchors, recurrences, join

**Claim.** `C(1) = 1`; `C(s+1) = s C(s)`;
`B(p,q) = B(p+1,q) + B(p,q+1)`; `q B(p+1,q) = p B(p,q+1)`; hence
`B(p+1,q) = p/(p+q) B(p,q)` and `B(p,q+1) = q/(p+q) B(p,q)`;
`B(p,q) = B(q,p)`; `E(s) = (1/2) C(s/2)`; and the join
`O(s) = E(s+1)`.

**Proof.** (a) `C(1)`: FTC gives `e^(-delta) - e^(-R) -> 1`.
(b) REC: `d/dx (x^s e^(-x)) = s x^(s-1) e^(-x) - x^s e^(-x)`
(POW-RAT power rule + product rule), FTC on `[delta,R]`; the
boundary terms carry rational certificates `delta^s -> 0` (zero-limit
certificate) and `R^s e^(-R) <= (k+2)!/R^2 -> 0` with integer
`k >= s`. (c) B-SPLIT is the pointwise algebra
`u^(p-1)(1-u)^(q-1) = u^p (1-u)^(q-1) + u^(p-1)(1-u)^q` on cuts;
B-PARTS is FTC for `d/du (u^p (1-u)^q)` with vanishing boundary
certificates `delta^p, (delta')^q -> 0`; B-REC follows by solving
the two linear relations. Symmetry is the affine reflection
`u -> 1-u` on cuts. (d) E-PULL: the substitution `y = x^2` on
`[delta,R]` (positive `C^1`) maps cuts to `[delta^2, R^2]` and gives
`E_(delta,R)(s) = (1/2) C_(delta^2,R^2)(s/2)` using
`(y^(1/2))^(s-1) y^(-1/2) = y^(s/2-1)` (POW-RAT laws); the squared
cut net is cofinal (TCB 8), so the limits agree. (e) JOIN: on every
cut `x * x^(s-1) = x^s` (POW-RAT additivity), so the integrands of
`O(s)` and `E(s+1)` coincide and the limits are equal. **QED Q2.**

### Q3 — Product identity on the rational slice

**Claim (MP).** `C(p) C(q) = C(p+q) B(p,q)` for all rational
`p, q > 0`.

**Proof.** *Step 1 (compact step, `p, q >= 1`).* For `r >= 1` the
integrand `x^(r-1)` extends continuously to `x = 0` with value `0`
for `r > 1` and `1` for `r = 1` (zero-limit certificate; convention
`x^0 = 1`), so `C_(0,R)(r)` is a proper compact integral, identified
with the TRUNC-0 limit through (M0'). The product of the two compact
integrals is an iterated integral by linearity, and compact Fubini
identifies it with the rectangle integral

```text
C_(0,R)(p) C_(0,R)(q) = II_([0,R]^2) x^(p-1) y^(q-1) e^(-(x+y)) dy dx,
```

using the exponential product law `e^(-(x+y)) = e^(-x) e^(-y)`. The
square splits along the zero-content diagonal into the triangles
`{y <= x}` and `{y >= x}`.

*Lower triangle.* For fixed `x` in `(0,R]` substitute `y = x t`,
`t` in `[0,1]`, `dy = x dt` (positive `C^1`), and use the base
product law `(x t)^(q-1) = x^(q-1) t^(q-1)`:

```text
int_0^x y^(q-1) e^(-(x+y)) dy
  = x^q int_0^1 t^(q-1) e^(-x(1+t)) dt .
```

The `x = 0` edge is a zero branch (inner integral over a degenerate
interval). The resulting two-variable integrand
`x^(p+q-1) t^(q-1) e^(-x(1+t))` is continuous on `[0,R] x [0,1]`
for `p, q >= 1` (`t^(q-1)` at `t=0` and `x^(p+q-1)` at `x=0` by the
continuous extension above, `p+q >= 2`), so compact Fubini permits
the swap:

```text
II_(y<=x) = int_0^1 t^(q-1) [ int_0^R x^(p+q-1) e^(-x(1+t)) dx ] dt .
```

The inner integral, by the linear positive substitution
`w = x(1+t)` and the base product law
`x^(p+q-1) = w^(p+q-1) (1+t)^(-(p+q-1))`:

```text
int_0^R x^(p+q-1) e^(-x(1+t)) dx
  = (1+t)^(-(p+q)) C_(0,R(1+t))(p+q) .
```

*Uniform tail.* For `p+q >= 2` the gap is a pure upper tail:
`0 <= C(p+q) - C_(0,R(1+t))(p+q) = int_(R(1+t))^inf <= (k+2)!/
(R(1+t)) <= (k+2)!/R` with integer `k >= p+q-1`, uniformly for `t`
in `[0,1]` since `1+t >= 1` (Minf' in the limit). The weight
`t^(q-1) (1+t)^(-(p+q)) <= 1` on `[0,1]`. Continuity in `t` of the
partial integral is TCB item 3. Hence

```text
| int_0^1 t^(q-1)(1+t)^(-(p+q)) [C(p+q) - C_(0,R(1+t))(p+q)] dt |
   <= (k+2)!/R -> 0 ,
```

and no dominated convergence and no Tonelli on an infinite region is
used anywhere. The upper triangle is the same computation with the
roles of `x, y` exchanged (substitute `x = y t`), producing
`t^(p-1)`. Since `C_(0,R)(p) C_(0,R)(q) -> C(p) C(q)` (monotone
convergent factors), the limit of the split is exactly

```text
(TRI)  C(p) C(q) = C(p+q) [ int_0^1 t^(q-1)(1+t)^(-(p+q)) dt
                          + int_0^1 t^(p-1)(1+t)^(-(p+q)) dt ] .
```

*Step 2 (midpoint pullback, still `p, q >= 1`).* The substitution
`u = t/(1+t)`, `du = (1+t)^(-2) dt`, positive `C^1`, maps `[0,1]`
onto `[0,1/2]`; inversely `t = u/(1-u)`, `1+t = (1-u)^(-1)`. The
exact form identity

```text
t^(q-1) (1+t)^(-(p+q)) dt = u^(q-1) (1-u)^(p-1) du
```

holds by the POW-RAT law package: the `(1-u)`-exponent is
`-(q-1) + (p+q) - 2 = p-1`. The first bracket of (TRI) is therefore
`int_0^(1/2) u^(q-1)(1-u)^(p-1) du`; the second, after the affine
reflection `u -> 1-u`, is `int_(1/2)^1 u^(q-1)(1-u)^(p-1) du`. For
`p, q >= 1` the `B`-integrand is continuous on `[0,1]`, the two
halves are proper compact integrals, and their sum is `B(p,q)`. The
diagonal `t = 1` maps to the midpoint `u = 1/2`; the diagonal split
of the square IS the midpoint split of Beta. This proves (MP) for
`p, q >= 1`. The identity (TRI) and the midpoint split are asserted
in this range only.

*Step 3 (finite descent to all of `Q_(>0)^2`).* Suppose (MP) holds
at `(p+1, q)`. Then by REC and B-REC:

```text
p C(p) C(q) = C(p+1) C(q) = C(p+q+1) B(p+1,q)
            = (p+q) C(p+q) * p/(p+q) * B(p,q) = p C(p+q) B(p,q),
```

and division by `p > 0` gives (MP) at `(p, q)`. The second argument
descends symmetrically. For arbitrary rational `p, q > 0` choose
finite integer shifts into the region `>= 1` and apply finitely many
descent steps. **QED Q3.**

### Q4 — Beta half identity

**Claim (B-HALF).** `B(p,p) = 2^(1-2p) B(1/2, p)` for all rational
`p > 0`.

**Proof.** *Step 1 (`p >= 1`).* By the base product law
`(u(1-u))^(p-1) = u^(p-1) (1-u)^(p-1)`, so
`B(p,p) = int_0^1 (u(1-u))^(p-1) du` is proper for `p >= 1`. The
affine substitution `u = (1+v)/2`, `du = dv/2`, with
`u(1-u) = (1-v^2)/4` and the base laws
`((1-v^2)/4)^(p-1) = 4^(1-p) (1-v^2)^(p-1)` gives

```text
B(p,p) = 4^(1-p) * (1/2) int_(-1)^1 (1-v^2)^(p-1) dv
       = 4^(1-p) int_0^1 (1-v^2)^(p-1) dv
```

by the reflection `v -> -v`. Now the cut substitution `v = w^(1/2)`
on `[eta, 1]` (POW-RAT, positive `C^1`, derivative
`(1/2) w^(-1/2)`), with `eta` running over rational squares
`eta = eps^2` so that `w`-cuts stay rational:

```text
int_(eps)^1 (1-v^2)^(p-1) dv = (1/2) int_(eps^2)^1 w^(-1/2) (1-w)^(p-1) dw .
```

Boundary certificates: on the `v`-side
`0 <= int_0^eps (1-v^2)^(p-1) dv <= eps` since the integrand is
`<= 1` for `p >= 1`; on the `w`-side
`0 <= int_0^(eps^2) w^(-1/2)(1-w)^(p-1) dw <=
int_0^(eps^2) w^(-1/2) dw = 2 eps` by FTC with primitive
`2 w^(1/2)` (exact rational value at the rational-square cut). For
`p >= 1` the factor `(1-w)^(p-1)` extends continuously to `w = 1`
(zero-limit certificate on the base `1-w`), so the one-ended
`w`-limit coincides with the two-ended TRUNC-0 value; the squared
cut net `{eps^2}` is cofinal (TCB 8). Letting `eps` run to `0`:

```text
int_0^1 (1-v^2)^(p-1) dv = (1/2) B(1/2, p),
```

hence `B(p,p) = 4^(1-p) * (1/2) B(1/2,p) = 2^(1-2p) B(1/2,p)`.

*Step 2 (diagonal descent, `p < 1`).* The diagonal cannot be
descended by one B-REC step; the two-step chain is

```text
B(p+1, p)   = (1/2) B(p,p)
B(p+1, p+1) = p/(2p+1) B(p+1, p)
B(1/2, p+1) = 2p/(2p+1) B(1/2, p)
```

(all instances of B-REC). Substituting B-HALF at `p+1 >= 1`:

```text
B(p,p) = 2(2p+1)/p * B(p+1,p+1)
       = 2(2p+1)/p * 2^(-1-2p) * 2p/(2p+1) * B(1/2,p)
       = 2^(1-2p) B(1/2,p);
```

the powers of two cancel exactly. A finite integer shift covers all
rational `p > 0`. **QED Q4.**

### Q5 — Square-root-free duplication

**Claim (DUP).** `C(p) C(p+1/2) = 2^(1-2p) C(1/2) C(2p)` for all
rational `p > 0`.

**Proof.** Two instances of (MP) — at `(p,p)` and at `(1/2,p)`, both
available by Q3 — give `B(p,p) = C(p)^2 / C(2p)` and
`B(1/2,p) = C(1/2) C(p) / C(p+1/2)`, dividing by the positive
quantities `C(2p)`, `C(p+1/2)` (Q1). Substituting into (B-HALF) and
cancelling the positive `C(p)` yields (DUP). No square-root symbol
occurs; `C(1/2)` is a first-class object. **QED Q5.**

### Q6 — Public bridge (self-contained)

**Claim (BRIDGE-PUB).** `C(1/2)^2 = p_I`, and `C(1/2) > 0`.

**Proof.** *Step 1.* `B(1/2,1/2) = 2 int_0^(1/2)
u^(-1/2)(1-u)^(-1/2) du` in the TRUNC-0 sense, by the reflection
`u -> 1-u` applied to cuts. *Step 2.* On `t`-cuts `[eps^2, 1]`
(rational squares), the substitution `u = t/(1+t)` (positive `C^1`,
mapping onto `[eps^2/(1+eps^2), 1/2]`) obeys the exact form identity

```text
u^(-1/2) (1-u)^(-1/2) du = t^(-1/2) (1+t)^(-1) dt ,
```

by the POW-RAT half-power laws: `u^(-1/2) = t^(-1/2)(1+t)^(1/2)`,
`(1-u)^(-1/2) = (1+t)^(1/2)`, `du = (1+t)^(-2) dt`. Boundary
certificate: `0 <= int_0^(eps^2) t^(-1/2)(1+t)^(-1) dt <=
int_0^(eps^2) t^(-1/2) dt = 2 eps` (FTC, primitive `2 t^(1/2)`,
rational at rational-square cuts); the image cuts are cofinal. Hence

```text
B(1/2,1/2) = 2 int_0^1 t^(-1/2) (1+t)^(-1) dt .
```

*Step 3.* On `[eps^2, 1]` substitute `t = v^2` (positive `C^1`):
`t^(-1/2) dt = 2 dv` exactly (POW-RAT), so

```text
int_(eps^2)^1 t^(-1/2)(1+t)^(-1) dt = 2 int_eps^1 (1+v^2)^(-1) dv ,
```

and the right side is a compact integral of a continuous integrand
whose limit is `2 F_I`. Therefore `B(1/2,1/2) = 4 F_I = p_I`.
*Step 4.* (MP) at `(1/2,1/2)` — reached from the compact region by
two descent steps `(3/2,3/2) -> (3/2,1/2) -> (1/2,1/2)` — and
`C(1) = 1` give `C(1/2)^2 = C(1) B(1/2,1/2) = p_I`. Positivity is
Q1. **QED Q6.** This claim is in the primary graph; it consumes Q3
and Q2 and nothing external. Note the acyclic order: (MP) does not
use any bridge, so `Q3 -> Q6` is a sound edge.

### Q7 — Public Machin bridge

**Claim (MACHIN).** `p_I = p_M`.

**Proof.** Define `A(x) := int_0^x dt/(1+t^2)` for **real**
`x` in `[0,2]` (compact integral of a continuous integrand, TCB
item 3); `F_I = A(1)`.

*Step 0 (the name `A_q` is well defined — proven here, so only the
name itself is consumed from WP3E).* The partial sums `S_(q,N)` with
an even number of terms increase, those with an odd number decrease,
and the gap of the consecutive pair is `a_(q,N) -> 0` (a strictly
decreasing null sequence, since `a_(q,n+1)/a_(q,n) < 1` as an exact
rational inequality). Monotone completeness (TCB item 2) gives a
common point of the nested hulls, and the shrinking gap makes it
unique; call it `A_q`.

*Step 1 (series name = integral name).* The finite geometric
identity `1/(1+t^2) = sum_(n=0)^N (-1)^n t^(2n) +
(-1)^(N+1) t^(2N+2)/(1+t^2)` and FTC give, for `x = 1/q` and in the
WP3E convention `S_(q,N) = sum_(n=0)^(N-1) (-1)^n a_(q,n)`:

```text
A(1/q) = S_(q,N+1) + (-1)^(N+1) rho_N,   0 <= rho_N <= a_(q,N+1),
```

where `rho_N = int_0^(1/q) t^(2N+2)/(1+t^2) dt <= a_(q,N+1)` by the
pointwise bound `t^(2N+2)/(1+t^2) <= t^(2N+2)` and FTC. The
remainder has sign `(-1)^(N+1)` and size `<= a_(q,N+1)`, hence
`A(1/q)` lies in `hull(S_(q,N), S_(q,N+1))` for every `N`: explicitly,
`A-S_(N+1)=(-1)^(N+1) rho_N` and
`A-S_N=(-1)^N(a_(q,N)-rho_N)`, whose signs are opposite because
`0 <= rho_N <= a_(q,N+1) < a_(q,N)`. By
Step 0's uniqueness, `A(1/q) = A_q`.

*Step 2 (addition law, by substitution — no chain rule).* For
rational `u, v` with `0 <= u, v <= 2`, `uv < 1` and
`g(u) := (u+v)/(1-uv) <= 2`:

```text
A(u) + A(v) = A(g(u)) .
```

Proof: on `[0, u]` the rational function `g(x) = (x+v)/(1-xv)` has
`1 - xv >= 1 - uv > 0`, and its derivative (TCB item 5a) is

```text
g'(x) = (1+v^2)/(1-xv)^2 > 0 ,
```

so `g` is an increasing `C^1` map of `[0,u]` onto `[v, g(u)]`, which
lies in `[0,2]` by the hypotheses. The exact polynomial identity

```text
(1-xv)^2 + (x+v)^2 = (1+x^2)(1+v^2)
```

gives pointwise `g'(x)/(1+g(x)^2) = 1/(1+x^2)`. The `C^1`
substitution `t = g(x)` (TCB item 5) then yields

```text
A(g(u)) - A(v) = int_v^(g(u)) dt/(1+t^2)
             = int_0^u g'(x)/(1+g(x)^2) dx
             = int_0^u dx/(1+x^2) = A(u) .
```

*Step 3 (compositions).* Three applications
with cancelling witnesses (exact cross-multiplications):

```text
2 A(1/5)  = A(5/12):     (2/5)/(24/25)   = 10/24  = 5/12,
                          10*12 = 24*5 = 120;    uv = 1/25 < 1
2 A(5/12) = A(120/119):  (5/6)/(119/144) = 720/714 = 120/119,
                          720*119 = 714*120 = 85680; uv = 25/144 < 1
A(1) + A(1/239) = A(120/119):
                          (240/239)/(238/239) = 240/238 = 120/119,
                          240*119 = 238*120 = 28560; uv = 1/239 < 1
```

with all composed values `<= 2`. Hence `4 A(1/5) - A(1/239) = A(1)
= F_I`, and multiplying by four, `16 A_5 - 4 A_239 = 4 F_I`, i.e.
`p_M = p_I`. **QED Q7.** After Q7 the WP3E bound `3 < p_M < 16/5`
and this probe's `p_I` concern the same constant; that is a
consistency remark, not a discriminating test, and no envelope
disjunction is tested anywhere.

### Q8 — Dressed slice and the s=1 anchor

**Claim (EOC-QPOS).** For all rational `s > 0`:
`Chat(s) = 2 int_0^inf e^(-2 p_M x) x^(s-1) dx` (quadratic-to-linear
pullback), and `Ehat(s) Ohat(s) = Chat(s)`; in particular
`Ehat(1) = 1` and `Ohat(1) = Chat(1) = 1/p_M`.

**Proof.** (a) `x = r^2` on cuts with the squared-cofinality lemma
gives the linear form of `Chat` (Jacobian `2r`,
`r^(2s-1) dr = (1/2) x^(s-1) dx`). (b) For every fixed positive real
constant `a` the scaled cut net `(a delta, a R)` is cofinal (TCB 8);
with `c := C(1/2)^(-1)` (positive by Q6) the substitution `x = c y`
and `c^2 p_I = 1` (Q6) plus `p_I = p_M` (Q7) give

```text
Ehat(s) = C(1/2)^(-s)   C(s/2),
Ohat(s) = C(1/2)^(-(s+1)) C((s+1)/2),
```

using E-PULL and JOIN (Q2) and the POW-RAT constant-power laws;
the linear substitution `w = 2 p_M x` gives
`Chat(s) = 2 (2 p_M)^(-s) C(s)`. (c) (DUP) at `p = s/2` and
`C(1/2)^(-2s) = p_M^(-s)` (iterated-power law with Q6+Q7) give

```text
Ehat(s) Ohat(s) = C(1/2)^(-(2s+1)) * 2^(1-s) C(1/2) C(s)
                = 2 (2 p_M)^(-s) C(s) = Chat(s) .
```

(d) At `s = 1`: `Ehat(1) = C(1/2)^(-1) C(1/2) = 1` and
`Ohat(1) = Chat(1) = 1/p_M`. **QED Q8.**

### Scale falsifier — three named residuals

Under `d mu_lambda = lambda dx`, `lambda` rational `> 0`, every
one-dimensional seed scales linearly. (MP) and (DUP) are homogeneous
of degree two and do not detect calibration. The three primitive
detectors are residuals against the original equations:

```text
R_1(lambda) = C_lambda(1) - 1                    = lambda - 1
R_2(lambda) = C_lambda(1/2)^2 - p_I              = (lambda^2 - 1) p_I
R_3(lambda; s) = Ehat_l(s) Ohat_l(s) - Chat_l(s) = lambda(lambda-1) Chat(s)
```

All three are nonzero for `lambda > 0`, `lambda != 1`. The frozen
fixture uses `lambda = 2` and requires rejection at all three
guards; scaled transformation laws must not be used as PASS
conditions of the mutated model. Tail moduli are tested separately.

## 5. Verifier surface (finite, exact, value-free stdout)

`verify.py` is a closed exact audit of a frozen bounded surface; the
theorem carrier is the written proof above. Obligations: zero
arguments; reads no file, archive, stdin, environment variable,
clock, or network; writes nothing but stdout; single import
`from fractions import Fraction as Fr`; no floating point anywhere (no
`** 0.5`, no `math.sqrt`, no float or complex literal); no `ast.Div`
(integer `//` and the `Fraction` constructor are the only quotients);
no random, subprocess, dynamic import, `eval` or `exec`; hard timeout
600 s; byte-identical stdout on x86_64 and aarch64 under Python 3.12.
`EXPECTED.txt` is the only stdout artifact; no transcript with a
forbidden suffix (`.log`, `.jsonl`, ...) will be produced or
requested, so the POLICY.md §7 transcript allowlist is never invoked.
Static audit recorded before pin (2026-08-26, repeated
2026-09-01; after pin, to be repeated on the read-back remote blob
before preflight): `py_compile` OK; AST scan: 0 `ast.Div` nodes,
0 float/complex literals, 1 import statement.

Preflight, run immediately before the single formal execution
(integrity check, not a scientific gate; after the immutable pin,
failure invokes the abandoned-pin disposition in §7):

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
required: exit 0; stdout exactly PYTHON_STARTUP_CLEAN plus LF; stderr empty
```

Replay ring: Laurent polynomials `Q[g, g^(-1)]` with the token
relation `p_hat := g^2` (the verifier never evaluates `g`
numerically). Frozen bounds:

```text
N_input  = 6      # input half-indices 1 <= k <= 6, arguments k/2
N_value  = 12     # dependency closure: DUP at p=k/2 needs half-index 2k <= 12
EOC_replay_domain = { 1, 2, 3 }   # integer s only
```

Gates (stdout lines are value-free; frozen block below). Gates 1–4
are the scientific phase. If any of them fires, `RESULT FIRED` is
emitted before gates 5–6; those two are PASS-candidate integrity
checks and cannot relabel a completed scientific negation:

1. `RING_LATTICE_REPLAY` — build `C(k/2)` for `k = 1..12` from
   `C(1/2) = g`, `C(1) = 1` by REC and build `B` from its three
   anchors by B-REC. Verify B symmetry, (MP), (DUP) for
   `p = k/2`, `k = 1..6`, B-HALF, the two-step diagonal descent
   `B(p+1,p+1) = p B(p,p)/(2(2p+1))`, and
   `B(1/2,1/2) = g^2` as exact ring equalities; verify (EOC) for
   `s` in `{1,2,3}` with
   `Ehat(s) = g^(-s) C(s/2)`, `Ohat(s) = g^(-(s+1)) C((s+1)/2)`,
   `Chat(s) = 2^(1-s) g^(-2s) C(s)`, and the `s = 1` anchor.
2. `MODULUS_CORE_SAMPLE` — for the frozen pairs
   `(s, b)` in `{(1/2,4), (3/2,4), (7/5,6), (1/7,6)}` verify the
   integer-exponent inequalities behind `D_b` and the bare-`C` tail
   schedule (`a m >= n(b+1+n)`; `n <= 2^n`;
   `(k+2)!/R_b = 2^(-(b+1))`), entirely in exact arithmetic. This
   finite gate does not audit the separate `E`, `O`, or two-ended `B`
   schedules of Q1; those universal algorithms remain carried by the
   written proof only.
3. `MACHIN_WITNESSES` — expand `(1-uv)^2 + (u+v)^2 - (1+u^2)(1+v^2)`
   as an exact polynomial in `u, v` and require the zero polynomial;
   verify the three composition equalities division-free
   (`(u+v) = target * (1-uv)`), the domain conditions (`uv < 1`,
   `u, v <= 2`, `(u+v) <= 2(1-uv)`), and the cross-multiplication
   witnesses; verify the Q7 Step-1 indexing at `q = 5` as exact
   rational identities: strict decrease `a_(5,n) > a_(5,n+1)` for
   `n = 0..4`, partial-sum gaps `S_(5,N+1) - S_(5,N) =
   (-1)^N a_(5,N)` for `N = 1..4`, and nesting of every later
   computed sum in the hull of each consecutive pair. (The
   remainder-envelope statement itself lives in the written proof
   Q7 Step 1, not in the finite audit.)
4. `FORM_IDENTITY_REPLAY` — verify, as identities of exponent
   vectors linear in symbolic `p, q, s` (coefficients in `Q`), the
   eight pullback forms: slope `y = xt`; `w = x(1+t)`;
   `u = t/(1+t)` (the `(1-u)`-exponent bookkeeping
   `-(q-1)+(p+q)-2 = p-1`); `v = w^(1/2)` (Jacobian exponent
   `-1/2`, factor `1/2`, the `(1-w)`-exponent carried unchanged);
   `y = x^2`; `x = r^2`; the Q6 half-power chain; and JOIN as the
   exponent equality `1 + (s-1) = s`.
5. `SCALE_RESIDUALS` — with `lambda = 2`: verify `R_1 = 1`,
   `R_2 = 3 p_hat`, and `R_3(s) = 2 Chat(s)` nonzero in the ring for
   `s` in `{1,2,3}`; require rejection of the mutated model at all
   three guards. This PASS-candidate phase is reached only after the
   gate-1 EOC premise has passed; if EOC itself fails, that failure
   already exits as scientific gate-1 `FIRED` and is not reclassified
   by the algebraically overlapping R3 check.
6. `PROOF_CONTROLS` — exactly 23 negative mutations, one per item of
   the mutation list below; each must be rejected at its named
   semantic guard, exercised through the same code path the PASS
   run consumes. A control that fails to reject is an integrity
   `STOP CONTROL_PASSED <name>`, never a `FIRED`; controls produce
   no stdout of their own beyond the counted summary line.

Frozen stdout (exact bytes fixed at pin; LF endings):

```text
P_JIPC_WP3D_QPOS_MELLIN_AUDIT 1
ARITHMETIC Q_EXACT_FRACTION PASS
RING_LATTICE_REPLAY N_INPUT=6 N_VALUE=12 EOC=1,2,3 PASS
MODULUS_CORE_SAMPLE C_PAIRS=4 PASS
MACHIN_WITNESSES POLY,CROSS3,DOMAINS,INDEXING PASS
FORM_IDENTITY_REPLAY FORMS=8 PASS
SCALE_RESIDUALS LAMBDA=2 GUARDS=3 PASS
PROOF_CONTROLS 23/23 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
```

Exit contract (WP3E register): a completed `RESULT PASS` or a
completed scientific `RESULT FIRED` (gates 1-4 negation lines
followed by `RESULT FIRED`) exits **zero** with empty stderr; any
integrity `STOP` exits nonzero. The scientific result is emitted
before the PASS-candidate gates 5–6. A gate-5 mismatch under its satisfied
gate-1 EOC premise is a verifier defect and therefore `STOP`, not
`FIRED`; a failed EOC premise retains its gate-1 `FIRED`
classification. The finite audit never
pronounces the scientific status: status selection belongs to
`RESULT.md`.

PASS-candidate mutation list (each with its named guard): (1) mutated REC
coefficient; (2) mutated DUP factor `2^(1-2p) -> 2^(-2p)`; (3)
displaced `C(1/2)` in DUP; (4) mutated B-REC coefficient; (5)
one-step diagonal-descent witness for B-HALF; (6) `B(1/2,1/2) ->
g^2 + 1`; (7) EOC replay outside the frozen domain (`s = 1/2`, rejected by the
domain guard before any half-power object is formed); (8) lattice
bounds, both halves: an input half-index beyond `N_input` rejected
by the input predicate AND a value beyond `N_value` absent from the
lattice; (9) mutated `D_b` ceiling (`b+1+c -> b+c`); (10) mutated
schedule factorial; (11) mutated Machin polynomial coefficient;
(12) mutated cross witness (`720*119 -> 720*118`); (13) violated
domain condition (`uv >= 1`); (14) mutated Q7 Step-1 sign; (15)
mutated slope Jacobian (missing `x`); (16) mutated `u = t/(1+t)`
bookkeeping (`p-1 -> p`); (17) mutated E-PULL factor (`1/2 -> 1`);
(18) mutated `v = w^(1/2)` factor/carry and `x = r^2` pullback
Jacobian (all parts rejected); (19) JOIN as definition — mutated provenance
   table rejected by the same provenance guard the PASS path consumes;
   (20) `lambda = 2` model under the mutated scaled-law guard: the two
   residual code paths must differ exactly by `lambda(lambda-1) Chat`,
   independently of the gate-1 EOC premise; (21) dressed weight renamed away
from `p_M` — rejected by the provenance guard (a name/graph test,
never a numeric envelope test); (22) nonpositive exponent rejected
at the modulus domain guard (irrational exponents are excluded by
the reduced-integer-pair input type itself); (23) claim label above
the slice (any of `MELLIN_SEEDS`, `MELLIN_PRODUCT_IDENTITY`,
`WP2_SCALAR_SEAM` asserted as PASS) — rejected by the label guard
the PASS path consumes.

## 6. Machine values (resolving the freeze blockers)

```text
FZ1_BRIDGE_SOURCE   = PUBLIC_SELF_CONTAINED (Q6; Q7 owns p_I = p_M)
FZ2_WRITTEN_PROOFS  = CARRIED IN THIS PREREG (Q1-Q8 above)
FZ3_ALLOWED_IMPORTS = exactly `from fractions import Fraction as Fr`;
                      hybrid or additional imports forbidden
FZ4_AST_POLICY      = no ast.Div (integer `//` allowed), no float
                      or complex literals, no imports beyond FZ3,
                      no exec/eval/getattr-dynamic, AST whitelist
                      audited before import
FZ5_RESOURCE_CAPS   = time 600 s (workflow-enforced); enforced by
                      guards inside the verifier: max rational
                      numerator/denominator 4096 bits on all lattice
                      values, max ring support 64 monomials;
                      structural (no runtime guard needed): exactly
                      23 fixtures, stdout exactly 10 lines on PASS,
                      no recursion anywhere in the code
FZ6_ARTIFACT_SET    = completed-run route: PREREG.md, verify.py,
                      EXPECTED.txt, RUN.md, RESULT.md; abandoned-pin
                      route: unchanged PREREG.md, unchanged verify.py,
                      RESULT.md only, with no EXPECTED.txt or RUN.md;
                      SHA-256 of verify.py frozen in the
                      claim-lock issue (verifier bytes are final before
                      the lock); SHA-256 of the pinned PREREG.md recorded
                      as a lock-issue comment at pin, after the locked
                      tuple and BASE_COMMIT are copied into PREREG.md
FZ7_STATIC_AUDIT    = py_compile OK; AST scan 0 ast.Div, 0 float or
                      complex literals, 1 import (pre-pin audit
                      2026-08-26, repeated 2026-09-01; after the pin,
                      repeated on the read-back remote blob before preflight)
FZ8_RUN_METADATA    = RUN.md carries neutral public metadata only
                      (OS, architecture, Python version); no machine
                      nickname, hostname, private address, fleet label
```

## 7. Falsifiers, FIRED, STOP, and abandoned pins

`FIRED` arises only from a completed exact mathematical negation:

- F1: any ring equality of gate 1 fails (B symmetry, MP, DUP,
  B-HALF, two-step diagonal descent, the bridge value, or EOC on the
  frozen lattice);
- F2: a Machin witness of gate 3 fails as exact arithmetic;
- F3: a form identity of gate 4 fails as exponent algebra;
- F4: a frozen `D_b` or bare-`C` schedule inequality of gate 2 fails
  as integer arithmetic.

`STOP` is integrity, not science. Before the pin, an authority,
collision, exactness, security, metadata, transcript or hash failure
halts the lane and creates no formal probe. After the pin, a negative
mutation that passes, a gate-5 residual mismatch, hash/readback or
preflight failure, nonzero exit, nonempty stderr, timeout, or other
failure before one completed formal gate invokes the abandoned-pin
route required by `POLICY.md`: the immutable `PREREG.md` and
`verify.py` remain unchanged, `RESULT.md` records `Status: ABANDONED`
and why the gate never completed, `EXPECTED.txt` and `RUN.md` are
absent, and the identifier is consumed forever. If the formal gate
completed and a later stdout-byte or architecture-integrity check
fails, the completed stdout and run record are preserved and
`RESULT.md` records integrity `STOP`; a completed gate is never
relabeled `ABANDONED`.

`CONFIRMED` is a status of `RESULT.md`, never of stdout: it may be
selected only after a completed `RESULT PASS` run, byte-identical on
both architectures, with the written proofs Q1-Q8 standing as the
theorem carrier. **Status ceiling:** candidate-T at L1; any public
`[T]` row is a separately claimed later Canon fold.

**Bounded fallback.** If the finite audit completes `RESULT PASS`
but the written universal proof is not accepted as theorem-grade in
review, the maximal salvageable status is `BOUNDED-AUDIT-C`: exactly
the frozen finite surface (the lattice, four-pair `D_b` plus bare-`C`
schedule sample, witness, form, and residual checks), with no
universal claim. The fallback is
selected in `RESULT.md`, never by the verifier.

## 8. Non-claims and untouched gates

This probe does not prove: effective holomorphic seeds (owned by
public WP3E), any identity beyond the rational slice, meromorphic
continuation, a functional equation, Fourier or Poisson theory, a
Gamma object, a circle constant, an archimedean place, any WP2
obligation, any L2-L6 lift; SAMPLING NOT PROVIDED. The gate names
`MELLIN_SEEDS`, `MELLIN_PRODUCT_IDENTITY`, `WP2_SCALAR_SEAM` and the
two pi-identification names belong to the private JIPC lineage:
Public Canon v74 carries no such gate or registry row, none is
created here, and any later Canon treatment is a separately claimed
fold.

## 9. Formal protocol locked by issue #777

1. Issue #777 froze the identifier, single branch, path, owner,
   layer, result-exposed mode, Public Canon v74 tuple, lock-time
   `BASE_COMMIT` and verifier SHA-256
   `238e587f1343e7fef07505e9bd6c8f75c9edf6a1efdeb98989f35ee5285151c0`.
2. Create only `probe/P-JIPC-WP3D-QPOS-MELLIN-1` and
   `probes/P-JIPC-WP3D-QPOS-MELLIN-1/` from that exact base. This
   complete `PREREG.md` and the never-executed `verify.py` are the
   only pin files.
3. Before any import or execution, commit and push both files as the
   immutable pin; record the full pin commit and pinned PREREG
   SHA-256 on issue #777. No second remote branch or attempt ref is
   created.
4. Read both remote blobs back; record exact commit, SHA-256, bytes,
   LF and final LF on issue #777; repeat the static audit (FZ7) on
   those read-back bytes.
5. Run the preflight (§5); only after public readback execute the
   pinned verifier formally exactly once in a deterministic
   environment.
6. If the gate completes, add only `EXPECTED.txt` (audited stdout),
   `RUN.md` (FZ8) and `RESULT.md`. If it never completes after the
   pin, add only the mandatory `RESULT.md` with
   `Status: ABANDONED`, no `EXPECTED.txt` and no `RUN.md`. In
   either route open one probe-only pull request; the completed route
   requires byte-identical x86_64 and aarch64 jobs plus aggregate
   `check` and manual security review.
7. Never amend, rebase, squash, force-push, rename, resume or reuse
   this probe after the pin; review and merge with provenance
   preserved.
