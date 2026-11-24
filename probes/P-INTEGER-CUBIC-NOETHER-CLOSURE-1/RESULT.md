# Result: global Noether identity and scoped nonclosure

Status: PASS  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Probe: P-INTEGER-CUBIC-NOETHER-CLOSURE-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1653  
Pin: d978a878dd6044d7ba297d8402195a522e6fc8f8

## 1. Observed result and meaning of PASS

The first formal primary run completed with exit zero and empty stderr.
The separately authored dual-number breaker ran in its own isolated
subprocess and produced the same 767-byte, 22-line certificate. The
primary's final stdout is 807 bytes and 24 LF, with SHA-256
004569700d67d2c1d1614c056be97ce00eee3df732c887d30f8316e51dc5e98c.
EXPECTED.txt contains exactly that first stdout; RUN.md records custody,
the actual local environment and timing.

No preregistered falsifier fired. All six prospective files are unchanged
from the public pin. No definition, fixture, threshold, proof or program
was tuned after scientific execution.

PASS means that the frozen positive and negative mathematical predictions
were both verified: the complete action has the specified first-order
off-shell Noether cancellation, and the frozen truncated transformation
has a generally nonzero second-order remainder and a generator family
that does not close. PASS does not mean that this family is closed or
that an exact gravitational gauge symmetry has been established.

| Finite audit | Observed count or result |
| --- | ---: |
| Actual normative authority files | 5 hashes and byte sizes match |
| Complete off-shell configurations | 6 |
| Independent global coordinates per configuration | 133 |
| Global analytic/dual/coordinate derivative comparisons | 798 |
| Local continuity vertices | 120 |
| Constraint propagation residual vertices | 120 |
| Integer continuity vertices | 120 |
| Noether identities | 126 |
| Integer Noether identities | 126 |
| Exact mixed deformation checks | 504 |
| Field-redefinition identities including quadratic remainder | 504 |
| Exact integer tangent displacements | 504 |
| Full-array generator commutators | 1140 |
| Independently specified negative controls | 10 |
| Raw primary/breaker certificate | Identical |

The ordered global gradient payload has SHA-256
3dbc280e96a372f418c61e44d52893581cef4ac2a29202cc96cd0a82a1e1ce57.
The ordered Noether payload has SHA-256
9ec77ec050134a059ed501f9e27729cb42778fb3e5fc797cf46b00ef09633461.
Both were calculated independently from the derivative values by the
programs; neither was supplied as an expected input.

## 2. Complete global action and correct auxiliary variations

The model is the finite action S_epsilon=S_0+epsilon S_int declared in
PREREG.md, with h,chi on T+1 slices, fixed physical endpoints, and the
exact auxiliary spaces tau,lambda in e-perp and p in ker(B^T). For T=5
there are 133 independent coordinates, in complete bases of those spaces.

PROOF.md Section 3 derives the full gradient, including j_(n-1), j_n and
j_(n+1) when varying an interior field slice. The exact off-shell witness
with only N_1(e_0)=1 and h_1=(6,11,11,6,6)/40 gives the neighbor terms

    Delta grad_(h_2) = (29/10368,29/10368,0,0,0),
    Delta dS/dchi_2 = -17/51840.

A calculation that retains only the current centered on slice two misses
these contributions. Both new implementations include them.

The p equation is the restricted equation proj_(ker B^T) N=0, hence
N=B xi. The tau equation then gives
lambda_b=xi_b-xi_(b-1), with xi_0=xi_T=0. It does not imply N=0, and no
auxiliary equation forces the homogeneous lapse alpha to vanish.

The valid local propagation statement is retained with its full residual:

    H_(n+1)-H_n = B^T M_n-2 B^T p_n-Pi0 C_n,
    C_n = [q_h,n*R_h,n+sigma q_chi,n R_chi,n]/2.

The declared co-closed p, inherited field equations R=0 and M=0 propagate
H=0. These are the inherited field residuals, not automatically the
full multiplier-dependent Euler equations of S_epsilon. The difference
is explicit in the global variation and is not hidden by a gauge choice.

## 3. Exact first-order Noether completion

For arbitrary vertex parameters psi with psi_0=psi_T=0, including their
homogeneous spatial part, define

    delta_0 N_n = B psi_n,
    delta_0 lambda_b = Pi0(psi_b-psi_(b-1)),
    delta_0 alpha_b = mean(psi_b-psi_(b-1)),

    delta_1 h_n = psi_n*(h_(n+1)-h_(n-1))/2,
    delta_1 chi_n = <sigma,psi_n>(chi_(n+1)-chi_(n-1))/2.

All other changes under the respective transformations are zero. Finite
summation by parts and the exact continuity residual yield

    delta_0 S_0 = 0,
    delta_0 S_int + delta_1 S_0 = 0,
    (delta_0+epsilon delta_1)S_epsilon = epsilon^2 U_psi,
    U_psi = delta_1 S_int.

These are exact off-shell algebraic identities for every admitted
rational array and every finite T>=5, as proved in PROOF.md Section 5.
The six configurations and 126 parameter instances audit the proof;
the universal statements are not extrapolated from those finite counts.

The fixed witness h_3=e_0, alpha_3=1, psi_2=psi_3=e_0, with all other
fields, multipliers and parameters zero, gives

    delta_0 S_int=1/2,
    delta_1 S_0=-1/2,
    U_psi=115/324 != 0.

Thus the first-order cancellation holds while the finite action at
epsilon=1 is not invariant under this frozen truncated transformation.
Dropping the homogeneous delta_0 alpha contribution gives -1/10 instead
of zero. Dropping the interaction edge current in the separately frozen
witness gives -1/1296. Allowing p outside ker(B^T) gives delta_0 S_0=-2.

## 4. Exact derivatives and the field-redefinition remainder

Individual independent coordinates have polynomial degree at most two,
so their centered unit differences are exact derivatives. A simultaneous
field/multiplier direction can have degree three. In the preceding
witness the naive two-point derivative differs from the true derivative
by -1/8. The primary uses both the analytic global gradient and the exact
four-point cubic formula; the breaker uses independent dual arithmetic.

When multipliers have the pure auxiliary gauge values delta_0 psi,
their S_0 bilinear terms cancel. For u=delta_1 x the exact identity is

    S_epsilon|pure-gauge
      = A_auto(x-epsilon u)-(epsilon^2/2)A_auto''[u,u].

The same witness, with these pure auxiliary gauge multiplier values,
has the nonzero substitution defect

    S_1-A_auto(x-u) = -115/648.

The first-order coupling is equation-proportional on these multiplier
values. The quadratic remainder is retained. This does not assert an
exact physical equivalence, invertibility of the finite field change,
or an integrated finite gauge flow.

## 5. What the commutator proves

Let X_psi denote the physical field part delta_1. The convention is

    [X_psi,X_eta]x = (G_eta G_psi-G_psi G_eta)x,

where G denotes the corresponding linear map on the full time array
with zero endpoint tangent rows. PROOF.md Section 8 displays its exact
second-neighbor time terms. The 1140 full-array comparisons agree in
both implementations, including the horizon boundaries and scalar part.

For psi_2=ell, eta_3=ell and all other parameters zero, set h_n=e/5 at
every slice except h_4=e/5+ell, and chi=0. Every slice has spatial sum
one. Then

    [X_psi,X_eta]h_2 = -ell/4 = (-1/4,1/4,0,0,0),
    X_zeta h_2 = 0 for every zeta because h_3-h_1=0.

This is an explicit proof of nonclosure in the declared nearest-time
family, even if zeta is chosen as a function of this field state. The
same witness has sum_r(X_eta h_3)(r)=1: the family need not preserve the
earlier prepared fixed-mean sector.

The statement is not a no-go theorem for additional generators, wider
stencils, on-shell relations or higher-order auxiliary-dependent terms.
It identifies precisely the family that a subsequent construction must
enlarge or replace if closure is required.

## 6. Exact integer representation and remaining obligations

All fields and auxiliary coordinates on the finite horizon can be stored
as integer numerators over one positive D; psi=V/Qp. The executable
integer density and current share the scale 4mD^2 and obey

    E_(n+1)-E_n+B^T J_n
      = 2Qh_n*Ah_n+(2sigma)Qchi_n Achi_n.

Multiplying the first-order Noether identity by 4mD^2 Qp gives an exact
zero integer. The displacement x+(delta_0+epsilon delta_1)x for integer
epsilon is represented exactly at Dnew=20D Qp, with the explicit integer
increments in PREREG.md Section 6. Auxiliary subspaces are preserved.
No minimum-denominator, autonomous evolution, bank conservation or
finite gauge symmetry is claimed for this tangent displacement.

This probe establishes a complete global variational audit, an exact
first-order Noether identity, and a precise obstruction in the selected
generator family. An all-order action/generator completion, a closed
Hamiltonian constraint algebra, nonlinear Einstein equations, a 3D
spatial refinement and continuum limit remain open. Neither the formal
epsilon grading nor the word cubic supplies those missing results.
