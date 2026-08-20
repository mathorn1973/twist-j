# PREREG-C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N

```text
STATUS:          NON-CANONICAL INCUBATION / RESULT-EXPOSED RE-DERIVATION
AUTHORITY:       none
TARGET LINE:     PUBLIC context only
OWNER SESSION:   ray-finite-window-certificate-v57-2026-08-20
ISSUE LOCK:      #468
BRANCH:          notes/c-rh-ray-finite-window-certificate-2-n
PATH:            notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N/
BASIS:           Public Canon v57 ACTIVE
MAIN AND TAG:    4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT COMMIT:  8e8b04abe4d3359942449533854ef1d142be70df
CANON SHA256:    c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON BYTES:     295013
LAYER:           analytic and operator-theoretic only; no L1-L6 physical lift
FORMAL PROBE:    none
CANON WRITE:     forbidden
ACTUAL ZEROS:    forbidden in assertions
```

This is a fresh v57 object. It does not resume, rebase, amend, or promote the
closed v56 lane #466. It freezes one conditional theorem and one exact
synthetic audit. No result here has public authority.

## 0. Authority and exposure

Public Canon v57 is current. The tag is identical to main. The declared content
commit is an ancestor. The five normative hashes agree with
`canon/SHA256SUMS`. The release PR records green policy, Canon, ledger,
x86_64, aarch64, aggregate, activation, and unit gates.

The v57 fold adds arithmetic statements about `2 log phi`, one toral finite
census, and one metrology finite witness. It does not change the public RH or
`LAMBDA-COCYCLE-*` rows. This content check does not import any v56 note into
v57 authority.

The complete v56 result is known before this freeze. Closed issue #466 exposed

```text
q_W = 3/5,
direct tail transition r = 14,
N = 17,
inertia = (4,2,11),
first nonpositive leading minor = 5,
uniform-bound transition r = 19,
breaker findings 0/10,
verifier 10/10 PASS.
```

Therefore this lane is not blind discovery and cannot be called independent
confirmation. It is a fresh-basis re-derivation, theorem audit, and exact
reproduction. That ceiling is frozen now.

## 1. Predecessor boundary

Inherited, not new:

1. Issue #374: the Ray-Pick kernel

   ```text
   K_ray(a,b)=(M(a)+M(b))/(a+b)
   ```

   and its Cauchy model, RH positivity equivalence, fixed accumulating ray,
   negative orbit direction, negative-index reading, Stieltjes form, and
   Hausdorff form.
2. Issue #363 and the public lambda rows: the exact lambda-adic torsion grid
   and the finite-profile boundary.
3. Closed issue #466: the v56 stale-basis discovery and synthetic control.
4. Every current public RH status and source bar.

Fresh delta: one v57-pinned written proof, one v57-pinned independent breaker,
one separately implemented v57-pinned verifier, and exact run records.

## 2. Falsifiers first

```text
F1   wrong sign, factorial, conjugation, or inner-product convention in the
     mixed derivative identity;
F2   noninjective beta -> t_beta, singular target interpolation, or hidden
     zero collision;
F3   failure of P_r to isolate exactly one nontrivial tau orbit on W;
F4   nonzero cross term despite tau invariance of W;
F5   Tail_r < 2m_O without a negative finite derivative form;
F6   an r-dependent constant presented as uniform, or failure of the
     exponential tail estimate;
F7   failure of sum m_beta|t_beta|^2 <= M(c)/(c-1/2);
F8   failure of the complete-height q_W bound;
F9   disagreement among direct spectral form, coefficient form, derivative
     matrix, exact inertia, and leading-minor checks;
F10  acceptance of a tau-fixed critical-line point as a nontrivial orbit;
F11  acceptance of q_W >= 1 into the exponential-decay gate;
F12  any Euler-side, zeta-evidence, or RH-progress wording unsupported by a
     complete zero window and arithmetic tail certificate.
```

Any fired F is archived. Thresholds, constants, carrier, and routes never move.
Authority, collision, pin, ordering, hash, license, or scope failure is STOP,
not F.

## 3. Frozen analytic objects

Use

```text
X(z)       = xi(1/2+z), even entire, X(0) != 0,
alpha      = rho-1/2,
tau alpha  = -conj(alpha),
M(a)       = X'(a)/X(a),
K_ray(a,b) = (M(a)+M(b))/(a+b),          a,b>1/2.
```

On `ell^2` of distinct zero locations, with multiplicity `m_beta`, use the
inner product linear in the first argument and

```text
v_a(beta)       = sqrt(m_beta)/(a-conj(beta)),
(J_ref f)(beta) = f(tau beta),
K_ray(a,b)      = <J_ref v_a,v_b>.
```

Fix real `c>1/2` and define

```text
t_beta    = 1/(c-conj(beta)),
w_k(beta) = sqrt(m_beta)t_beta^k,       k>=1.
```

Let `W` be finite and tau invariant. Let

```text
O={alpha,tau alpha} subset W
```

be nontrivial, with common positive integer multiplicity `m_O`. Define

```text
H_W(t)=product_(beta in W minus O)(t-t_beta).
```

For integer `r>=1`, define the unique affine `L_r` by

```text
t_alpha^r H_W(t_alpha)L_r(t_alpha)=+1,
t_(tau alpha)^r H_W(t_(tau alpha))L_r(t_(tau alpha))=-1,
P_r(t)=t^rH_W(t)L_r(t).
```

The exact Lagrange formula is part of the frozen proof surface.

## 4. Gate V1, mixed derivatives

Prove for `j,k>=1`

```text
partial_a^(j-1)partial_b^(k-1)K_ray(a,b)|_(c,c)
 = (-1)^(j+k-2)(j-1)!(k-1)!<J_ref w_j,w_k>.
```

Define

```text
G_N(j,k)=<J_ref w_j,w_k>,        1<=j,k<=N.
```

The raw derivative matrix is diagonally congruent to `G_N`. For
`P(t)=sum_(k=1)^N p_k t^k`,

```text
p^*G_Np=<J_ref f_P,f_P>,
f_P(beta)=sqrt(m_beta)P(t_beta).
```

No conditional zero summation is permitted in this step.

## 5. Gate V2, interpolation

Prove:

```text
P_r(t_alpha)=+1,
P_r(t_(tau alpha))=-1,
P_r(t_beta)=0 for beta in W minus O,
powers(P_r) subset {r,...,r+|W|-1}.
```

The proof must explicitly establish injectivity of `beta -> t_beta`, target
nontriviality, nonvanishing of the two `H_W` values, uniqueness of `L_r`, and
the degree bound.

## 6. Gate V3, invariant split

Set

```text
f_r(beta)=sqrt(m_beta)P_r(t_beta),
u_O=sqrt(m_O)(e_alpha-e_(tau alpha)),
e_r=f_r restricted to W^c.
```

Prove

```text
<J_ref f_r,f_r>=-2m_O+E_r,
E_r=<J_ref e_r,e_r>,
|E_r|<=Tail_r,
Tail_r=sum_(beta notin W)m_beta|P_r(t_beta)|^2.
```

The cross term vanishes because `W` and `W^c` reduce `J_ref`. Therefore

```text
Tail_r<2m_O
```

is a sufficient finite negative certificate.

## 7. Gate V4, finite matrix consequence

Since `deg P_r<=N=r+|W|-1` and `P_r(0)=0`, the coefficient vector belongs to
`G_N`. The sufficient tail inequality must imply that `G_N` is indefinite.
By Sylvester's criterion, at least one leading principal minor through order
`N` is nonpositive.

## 8. Gate V5, uniform exponential bound

Freeze

```text
t_1=t_alpha,
t_2=t_(tau alpha),
tau_0=min(|t_1|,|t_2|),
delta_t=|t_1-t_2|,
h_*=min(|H_W(t_1)|,|H_W(t_2)|),
q_W=sup_(beta notin W)|t_beta|/tau_0.
```

Assume `q_W<1`. Define

```text
B_W=(2q_Wtau_0+|t_1|+|t_2|)/(delta_t h_*),
C_W=product_(gamma in W minus O)(q_Wtau_0+|t_gamma|).
```

Prove

```text
|L_r(t_beta)|<=B_Wtau_0^-r,
|H_W(t_beta)|<=C_W,
|P_r(t_beta)|<=B_WC_W(|t_beta|/tau_0)^r.
```

For frozen `r_0>=1`, define

```text
A_W(c)=B_W^2C_W^2M(c)/((c-1/2)tau_0^2).
```

Prove the uniform estimate

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)),      r>=r_0.
```

The constant must not depend on `r`.

Freeze the exact threshold

```text
r_*=min{r>=r_0:A_W(c)q_W^(2(r-r_0))<2m_O},
N_*=r_*+|W|-1.
```

No rounded logarithm gates anything.

## 9. Gate V6, ordinary Cauchy norm

Prove unconditionally on the frozen zero multiset convention

```text
sum_beta m_beta|t_beta|^2<=M(c)/(c-1/2).
```

Use

```text
1/|c-beta|^2
 = Re(1/(c-beta))/(c-Re beta)
 <= Re(1/(c-beta))/(c-1/2),
```

and the positive paired Hadamard sum for `M(c)`.

## 10. Gate V7, complete height window

For `alpha=x+iy`, prove

```text
tau_0=1/sqrt(y^2+(c+|x|)^2).
```

If `W` contains all zero locations with `|Im beta|<=T`, prove

```text
q_W<=sqrt(y^2+(c+|x|)^2)/T.
```

Thus the strict height condition

```text
T>sqrt(y^2+(c+|x|)^2)
```

forces `q_W<1`.

## 11. Frozen synthetic carrier

The result-exposed replay carrier is exactly

```text
c=7/5,
alpha=2/5+12i/5,
tau alpha=-2/5+12i/5,
W={alpha,tau alpha,conj(alpha),conj(tau alpha)},
outside={24i/5,-24i/5},
multiplicity 1 on W,
multiplicity 10^6 outside,
r_0=1.
```

It is closed under negation, conjugation, and tau. It is theorem control only.
It is not a zero set, not an approximation to a zero set, and not evidence.

The verifier must audit exact direct transition, exact coefficient form,
exact symmetric inertia, all leading minors through the certificate order, the
uniform majorant, the complete-height control, a noninvariant-window cross-term
control, a tau-fixed target rejection, and a `q_W>=1` rejection.

## 12. Breaker-first order

A fresh `break.py` is written from this preregistration before the new accepted
verifier exists. It must use a direct finite spectral representation and a
polynomial implementation structurally different from the verifier. It may
know the v56 exposed result. It must not import or read the new verifier.

`PREREG.md` and then `break.py` are committed, pushed, and remotely read back
before the first v57 execution. The breaker runs once. Its finding is preserved.
Only afterwards are `PROOF.md` and `verify.py` written and pinned. The accepted
verifier runs once. No file is amended after execution.

## 13. Expected decision routes

```text
CERTIFICATE  complete written proof, breaker no surviving break, verifier PASS;
             candidate-T conditional theorem, candidate-C synthetic replay
PARTIAL      V1-V4 survive, but V5-V7 do not close exactly
F            one mathematical falsifier F1-F11 fires
STOP         integrity, authority, collision, ordering, or scope failure
```

## 14. Firewall

No actual zeta ordinate. No zero table in an assertion. No RH proof or evidence.
No Euler-side positivity theorem. No Canon, Registry, Frontier, public probe,
release, physical, decoder, Born, SI, or L1-L6 claim. The theorem says only
that a complete zero-side window containing an off-critical orbit would force
one explicit finite Ray-Pick derivative failure. It does not supply the orbit,
the window, or the arithmetic certificates.