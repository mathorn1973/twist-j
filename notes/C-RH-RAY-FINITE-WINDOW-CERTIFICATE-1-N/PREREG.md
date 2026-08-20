# PREREG-C-RH-RAY-FINITE-WINDOW-CERTIFICATE-1-N

```text
STATUS:         NON-CANONICAL INCUBATION / ATTACK
AUTHORITY:      none
TARGET LINE:    PUBLIC context only
OWNER SESSION:  ray-finite-window-certificate-2026-08-20
ISSUE LOCK:     #466
BRANCH:         notes/c-rh-ray-finite-window-certificate-1-n
PATH:           notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-1-N/
BASIS:          Public Canon v56 ACTIVE
MAIN AT LOCK:   d525da0964e66800dd5276c2f22545f17910c13e
TAG:            canon-v56 at 6e521f077b57ea343e5b456adb666b50e6a17eb4
CONTENT COMMIT: b36c93ed8ce24a9cbd771168094db04f5a5ac06c
CANON SHA256:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
CANON BYTES:    288492
LAYER:          analytic and operator-theoretic only; no L1-L6 physical lift
FORMAL PROBE:   none
CANON WRITE:    forbidden
ZERO DATA:      forbidden in assertions
```

This file freezes one proof-first quantitative refinement of the Ray-Pick
incubation under issue #374. It does not claim a proof of RH, evidence for RH,
a public theorem, a public computation, or an Euler-side construction. The
result is conditional on a complete finite zero window and a certified tail
bound. Its purpose is to replace the qualitative statement "some finite
Ray-Pick matrix eventually becomes indefinite" by one explicit finite
certificate and one explicit derivative-order threshold.

No accepted verifier, breaker output, transcript, threshold output, synthetic
spectrum, or formal execution existed before this file was committed. The
candidate mechanism was exposed in issue #466 before this freeze and is
re-derived here. Static review and syntax checking are allowed after the
freeze. Scientific execution is forbidden until this file and `break.py` have
both been committed, pushed, and read back byte for byte.

## 0. Collision and predecessor boundary

The exact claim, branch, path, issue, probe, Registry, and nearby semantic names
were searched before issue #466. No collision was found.

The following are inherited and are not recounted as new:

1. Issue #374, `RAY-PICK-KERNEL`: the exact kernel
   `K_ray(a,b)=(M(a)+M(b))/(a+b)`, its Cauchy `ell^2` model, the equivalence
   between RH and positivity of every finite Ray-Pick matrix, the fixed
   accumulating ray, and the negative orbit direction.
2. Issue #374, `RAY-STIELTJES-MASTER`: the Stieltjes and Hausdorff
   reformulations and their honest Euler-side source bar.
3. Issue #363 and the public `LAMBDA-COCYCLE-*` rows. The independent lambda
   audit confirms that `(1/4) Z[1/5]` is the unique lambda-adic torsion angle
   set, while assigning that set to zeta ordinates is strictly extra and no
   finite enclosure decides membership. This attack is not a lambda-grid or
   finite-profile attack.
4. Every public RH status, theorem, falsification, and source boundary.

The fresh delta is only the finite-window certificate, its exact tail split,
and its explicit sufficient derivative order.

## 1. Falsifiers first

```text
RF1  the derivative formula in G1 has a wrong factorial, sign, conjugation, or
     inner-product convention;
RF2  distinct zero locations can give the same Cauchy coordinate t_beta, or
     the target interpolation is singular for a nontrivial tau orbit;
RF3  the polynomial P_r does not isolate the target vector exactly on a finite
     tau-invariant window;
RF4  tau invariance of the finite window does not remove every cross term in
     the J_ref form;
RF5  Tail_r < 2 m_O does not force a negative finite derivative form;
RF6  the constant in G5 depends exponentially on r, the claimed q_W is not
     below one, or the displayed exponential tail bound fails;
RF7  the ordinary Cauchy norm bound by M(c)/(c-1/2) is false under the frozen
     paired Hadamard convention;
RF8  a critical-line target, where tau alpha = alpha, is accepted as a
     nontrivial negative orbit;
RF9  an exact synthetic spectrum satisfying every frozen premise disagrees
     between the direct spectral form, the derivative matrix, and the
     polynomial certificate;
RF10 any result is described as Euler-side, zeta evidence, or RH progress
     without supplying the complete zero window and the required arithmetic
     tail certificate.
```

A fired falsifier is archived. No carrier, threshold, constant, window,
normalization, or decision route moves after this freeze.

## 2. Frozen analytic objects

Use the conventions of issue #374:

```text
X(z)       = xi(1/2+z), even and entire, X(0) != 0,
alpha      = rho-1/2,
tau alpha  = -conj(alpha),
M(a)       = X'(a)/X(a),
K_ray(a,b) = (M(a)+M(b))/(a+b),          a,b > 1/2.
```

The multiset of zero locations keeps multiplicities. Every nontrivial zero
satisfies `|Re alpha|<1/2`. On `ell^2` of distinct locations, with the standard
inner product linear in the first argument, define

```text
v_a(beta)       = sqrt(m_beta)/(a-conj(beta)),
(J_ref f)(beta) = f(tau beta).
```

Then `J_ref` is a self-adjoint unitary involution and

```text
K_ray(a,b) = <J_ref v_a,v_b>.
```

Fix one real `c>1/2`. For `k>=1`, put

```text
w_k(beta) = sqrt(m_beta)/(c-conj(beta))^k,
t_beta    = 1/(c-conj(beta)).
```

Let `W` be a finite tau-invariant set of distinct zero locations. Let

```text
O = {alpha,tau alpha} subset W
```

be one nontrivial tau orbit, so `tau alpha != alpha`, with common positive
integer multiplicity `m_O`.

Define

```text
H_W(t) = product_(beta in W minus O) (t-t_beta).
```

For integer `r>=1`, define the unique affine polynomial `L_r` by

```text
A_1(r) = t_alpha^r H_W(t_alpha),
A_2(r) = t_(tau alpha)^r H_W(t_(tau alpha)),
L_r(t_alpha)       =  1/A_1(r),
L_r(t_(tau alpha)) = -1/A_2(r),
P_r(t) = t^r H_W(t) L_r(t).
```

The explicit Lagrange form is frozen as

```text
L_r(t)
 = (1/A_1(r)) (t-t_(tau alpha))/(t_alpha-t_(tau alpha))
   + (-1/A_2(r)) (t-t_alpha)/(t_(tau alpha)-t_alpha).
```

## 3. G1, one-point derivative matrix

For integers `j,k>=1`, prove

```text
partial_a^(j-1) partial_b^(k-1) K_ray(a,b)|_(a=b=c)
 = (-1)^(j+k-2) (j-1)! (k-1)! <J_ref w_j,w_k>.
```

The proof must differentiate the two Cauchy vectors, not a conditionally split
zero sum. Define the scaled Hermitian derivative matrix

```text
G_N(j,k) = <J_ref w_j,w_k>,             1<=j,k<=N.
```

The raw mixed-derivative matrix is diagonally congruent to `G_N`, so both have
the same inertia. Every polynomial `P(t)=sum_(k=1)^N p_k t^k` gives

```text
f_P = sum_(k=1)^N p_k w_k,
<J_ref f_P,f_P> = p^* G_N p.
```

## 4. G2, exact finite-window interpolation

Prove the following points without numerical approximation:

1. `beta -> t_beta` is injective.
2. Since the target orbit is nontrivial, `t_alpha != t_(tau alpha)`.
3. `H_W(t_alpha)` and `H_W(t_(tau alpha))` are nonzero.
4. `L_r` therefore exists uniquely.
5. The polynomial `P_r` satisfies

```text
P_r(t_alpha)       = +1,
P_r(t_(tau alpha)) = -1,
P_r(t_beta)        = 0       for beta in W minus O.
```

6. `P_r` contains only powers `r,...,r+|W|-1`. Its degree is at most
   `N=r+|W|-1`.

## 5. G3, invariant split and sufficient negativity

Define

```text
f_r(beta) = sqrt(m_beta) P_r(t_beta),
u_O         = sqrt(m_O)(e_alpha-e_(tau alpha)),
e_r         = f_r restricted to W^c.
```

On `W`, exact interpolation gives `f_r|W=u_O`. Since both `W` and `W^c` are
`J_ref` invariant, prove the orthogonal split

```text
<J_ref f_r,f_r> = <J_ref u_O,u_O> + <J_ref e_r,e_r>
                 = -2m_O + E_r,
E_r             = <J_ref e_r,e_r>,
|E_r|           <= ||e_r||^2
                 = Tail_r,
Tail_r           = sum_(beta notin W) m_beta |P_r(t_beta)|^2.
```

Therefore

```text
Tail_r < 2m_O
```

is a sufficient finite negative certificate.

## 6. G4, finite Pick consequence

If the sufficient tail inequality holds, the coefficient vector of `P_r`
produces a negative quadratic value in `G_N` for

```text
N = r+|W|-1.
```

Hence `G_N` and the diagonally congruent raw derivative matrix are indefinite.
By Sylvester's criterion, at least one leading principal minor through order
`N` is nonpositive. This is an explicit upper bound on the order of a finite
Ray-Pick falsity witness, conditional on the frozen window and tail data.

No claim is made that the finite window or tail data are available from the
Euler side.

## 7. G5, uniform exponential tail bound

Freeze

```text
t_1      = t_alpha,
t_2      = t_(tau alpha),
tau_0    = min(|t_1|,|t_2|),
delta_t  = |t_1-t_2|,
h_*      = min(|H_W(t_1)|,|H_W(t_2)|),
q_W      = sup_(beta notin W) |t_beta|/tau_0.
```

Assume `q_W<1`. Define the finite constants

```text
B_W = (2 q_W tau_0 + |t_1| + |t_2|)/(delta_t h_*),
C_W = product_(gamma in W minus O) (q_W tau_0 + |t_gamma|).
```

The affine interpolation formula must yield, for every outside location,

```text
|L_r(t_beta)| <= B_W tau_0^(-r),
|H_W(t_beta)| <= C_W,
|P_r(t_beta)| <= B_W C_W (|t_beta|/tau_0)^r.
```

The ordinary Cauchy norm is

```text
C_2(c) = sum_beta m_beta |t_beta|^2.
```

Prove the unconditional comparison

```text
C_2(c) <= M(c)/(c-1/2).
```

The pointwise reason is

```text
1/|c-beta|^2
 = Re(1/(c-beta))/(c-Re beta)
 <= Re(1/(c-beta))/(c-1/2),
```

and the positive paired sum of the real parts is `M(c)`.

For any frozen integer `r_0>=1`, define

```text
A_W(c) = B_W^2 C_W^2 M(c)/((c-1/2) tau_0^2).
```

Then prove the uniform estimate, independent of `r`,

```text
Tail_r <= A_W(c) q_W^(2(r-r_0)),       r>=r_0.
```

The proof uses

```text
sum_(beta notin W) m_beta (|t_beta|/tau_0)^(2r_0)
 <= C_2(c)/tau_0^2
```

for `r_0>=1`, because every outside ratio is below one.

Freeze the sufficient derivative threshold as the least integer

```text
r_* = min {r>=r_0 : A_W(c) q_W^(2(r-r_0)) < 2m_O}.
```

It exists because `0<=q_W<1`. If `q_W=0`, take `r_*=r_0`. The certificate
order is

```text
N_* = r_* + |W| - 1.
```

This minimum definition, not a rounded logarithm, is the exact threshold used
by any verifier. An optional displayed logarithmic estimate is commentary only
and gates nothing.

## 8. G6, height-window corollary

Write the target location as

```text
alpha = x+iy.
```

Then

```text
tau_0 = 1/sqrt(y^2+(c+|x|)^2).
```

Suppose `W` contains every zero location with `|Im beta|<=T`. For each outside
location, `|t_beta|<1/T`, so

```text
q_W <= sqrt(y^2+(c+|x|)^2)/T.
```

Therefore the exact strict condition

```text
T > sqrt(y^2+(c+|x|)^2)
```

forces `q_W<1`.

An effective arithmetic certificate still needs all of the following:

1. proof that the finite list is complete with multiplicities through height
   `T` without assuming RH;
2. exact isolation of one nontrivial tau orbit inside that list;
3. certified upper bounds for `q_W`, `B_W`, `C_W`, and `M(c)` in the declared
   number system;
4. no zero-side input hidden inside a claimed Euler-side construction.

The theorem itself does not provide those inputs.

## 9. Code, carrier, and exact synthetic audit

After this file and `break.py` are remotely read back, one accepted verifier
may be written. It must use Python standard library only, exact integers,
`Fraction`, and a rational complex-pair implementation. No float may occur in
an assertion or threshold.

The synthetic carrier is a finite multiset of rational complex locations
closed under

```text
beta -> -beta,
beta -> conj(beta),
beta -> tau beta = -conj(beta),
```

with positive integer multiplicities. Synthetic points are theorem controls
only. They are not zeta zeros and not RH evidence.

The audit must include:

```text
S1  exact G1 derivative agreement against direct spectral differentiation;
S2  exact G2 interpolation and degree support;
S3  exact G3 split and tail inequality;
S4  direct Hermitian inertia against the polynomial negative certificate;
S5  one frozen case where a small r does not certify and a later r does;
S6  exact G5 exponential bound and exact r_* threshold;
S7  a non-tau-invariant-window negative control with a nonzero cross term;
S8  a target fixed by tau rejected as a trivial orbit;
S9  q_W>=1 rejected as outside the exponential-decay gate;
S10 deterministic output, no file writes, no external data, no random search.
```

## 10. Independent breaker order

`break.py` is written from this file before the accepted verifier is written or
read. It must be committed, pushed, and read back first. It attacks RF1-RF10
through a structurally different implementation. The breaker may use direct
spectral vectors and polynomial evaluation but must not import the accepted
verifier.

The breaker is frozen before any synthetic formal run. If the breaker finds a
counterexample, the finding is recorded and no threshold is repaired.

## 11. Decision and status ceiling

```text
CERTIFICATE
    G1-G6 have complete written proofs, the independent breaker is frozen
    first, and the exact synthetic audit agrees. Record candidate-T for the
    conditional finite-window certificate and candidate-C for the bounded
    synthetic audit.

PARTIAL
    G1-G4 survive, but G5 or G6 lacks a uniform bound or exact threshold.

F
    An exact counterexample fires RF1-RF9.

STOP
    Authority, collision, scope, convergence, preregistration order,
    breaker independence, source typing, or file integrity fails.
```

No outcome changes RH, issue #374, the lambda rows, the public Registry, or any
Canon file. Promotion, if ever justified, requires a fresh public claim under
the then-current authority and protocol.

## 12. Scope firewall

No actual zero ordinate. No zero table in an assertion. No RH proof or evidence.
No Euler-side positivity theorem. No Canon, Registry, Frontier, probe, release,
physical, decoder, Born, SI, or L1-L6 claim. No duplicate lambda-grid,
conductor-capacity, Suzuki local-capacity, or finite-profile lane. Negative
results are first-class.