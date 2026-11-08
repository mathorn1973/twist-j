# Exact finite closed-recoil audit

Status: prospective, NON-CANONICAL, NEW_DECLARED L1.
Probe: P-RELATIONAL-MASS-CLOSED-RECOIL-1. Ownership: #1694.
Base: `0f26395b17597af882014b99639d1fb6ee6d3d36`.

The standalone `verify.py` adapts the exact Fraction/matrix/automatic-
differentiation utilities of P-RELATIONAL-MASS-BOOST-COMPLETION-1. It imports
no old probe and has no runtime dependency on an old scientific result.
Formal Taylor arithmetic now retains coefficients through degree four.
Positive square roots have rational constant terms in every fixture. The
formal exponential is admitted only with constant term zero, which holds
at each interior contact fixture. No approximation to an exponential,
floating-point operation, orbit integration, external input, subprocess,
network, random choice or file write is used.

Command: `python3 probes/P-RELATIONAL-MASS-CLOSED-RECOIL-1/verify.py`.
Only static parsing is allowed before public pin/readback.

## Coordinates and exact derivatives

Each subsystem uses the fourteen coordinates
`(G11,G12,G22,Pi11,Pi12,Pi22,X1,X2,p1,p2,r1,r2,rho1,rho2)`
and one-form `tr(Pi dG)+p.dX+rho.dr`. The factor 1/2 in off-diagonal
metric Hamilton equations is retained. The joint carrier is the ordered
concatenation of A and B, with 28 independently differentiated coordinates.

Set kappa=3 and

```
h=tr(G Pi G Pi)/2+sqrt(rho^T G rho)+3 r^T G^-1r,
j=2 G Pi+r rho^T,   S=j12-j21,
epsilon=sqrt(h^2+c^2 p.p),   R p=(-p2,p1),
K=epsilon X/c^2-S Rp/(epsilon+h),
L=X wedge p+S,
Y=X+c^2 S Rp/[h(epsilon+h)].
```

All derivatives of h and S are taken from their actual internal canonical
variables, not from externally fixed parameters.

## 1. Thirty-six free covariant-center cases

The three internal states are:

- A: G=I, Pi=[[0,-1],[-1,0]], r=(1,0), rho=(0,6), h=10.
- B: G=I, Pi=[[0,-3],[-3,0]], r=(2,0), rho=(0,24), h=45.
- The congruence transform of A by M=[[1,1],[0,1]], transforming
  `(G,Pi,r,rho)` to `(MGM^T,M^-T Pi M^-1,Mr,M^-T rho)`.

For each state use c in `{1,2}`, t in `{0,1/4,1/2}`, and the two pairs
`d=(1,0), X=(1,-2)` and `d=(3/5,4/5), X=(-2,1)`.
Set `p=(h/c)2t/(1-t^2)d`. The two centers make all full-phase fixtures
distinct even at p=0. Rational energy is `epsilon=h(1+t^2)/(1-t^2)`.

Exact gradients and complete Poisson brackets must satisfy

```
{Y_j,K_i}=Y_i p_j/epsilon,
{Y_i,p_j}=delta_ij,
{Y1,Y2}=c^2 S/(h epsilon),
Ydot=c^2 p/epsilon,
K=epsilon Y/c^2-(S/h)Rp,
L=Y wedge p+(epsilon/h)S.
```

These are free-system identities. No interacting boost algebra is asserted.

## 2. Six fourth-derivative discriminators

At p=0, for each of the three states and c in `{1,2}`, vary p along e1.
Automatic degree-four expansion compares

```
F_R=sqrt(h^2+c^2 p.p),
F_N=h+c^2 p.p/(2h).
```

Both must have second derivative c^2/h, while the dimensionless expression
`h E''''/[3(E'')^2]` must equal -1 and 0 respectively. This is a comparison
of two declared laws with the same rest Hessian, not a native selection.

## 3. One new bound-state B witness

At B check h=45, j=[[0,42],[-6,0]], delta=252 and S=48.
The minimum parameters a=24, b=18, u=3/4 obey b^2=a^2-delta,
`(kappa/a)^(1/3)=1/2` and
`f'=2(kappa/a)^(1/3)+(a-b)(1-a/b)/2=0`.
Check Omega=[[0,-7/2],[1/2,0]], Omega^2=-7I/4 and compare the actual
Hamilton field of h at B against the infinitesimal congruence action of
Omega on every internal coordinate. This is one new pointwise orbit
certificate. Global minimum, all-time orbit and stability remain proof
claims; the old A orbit audit is not replayed.

## 4. Eight interior closed-contact cases

The new, separately declared common-time Hamiltonian is

```
Htot=epsilon_A+epsilon_B+V(X_A-X_B),
V(r)=22 exp[1/3-|r|^2/(1-|r|^2)] for |r|<1,
V(r)=0 for |r|>=1.
```

The centers in this potential are canonical X, not the free covariant Y.
This finite interaction is not asserted to be Lorentz covariant. In
particular free Ydot=c^2p/epsilon need not hold inside this contact.

Use A and B, c in `{1,2}`, d in `{(1,0),(3/5,4/5)}` and
`p_A=k d`, `p_B=-p_A`, with k in `{0,24/c}`. Set X_A=d/4,
X_B=-d/4, so separation is d/2. The potential exponent has zero constant
term, V=22, and automatic differentiation of all 28 coordinates must give

```
pdot_A=(352/9)d,   pdot_B=-(352/9)d,
Ptotdot=0,   Htotdot=0,
hdot_A=hdot_B=0,   jdot_A=jdot_B=0,
internal flow_i=(h_i/epsilon_i) X_(h_i),
Xdot_i=c^2 p_i/epsilon_i.
```

At the four k=0 cases also differentiate the actual canonical-center
velocities along the joint field. The accelerations are
`c^2(352/9)d/10` and `-c^2(352/9)d/45`, so their magnitude ratio is 9/2.
This instantaneous ratio concerns X, not the generally noncanonical Y
inside the contact. Initial total energy is 10+45+22=77.

## 5. Four outgoing free cases

Use c in `{1,2}` and the same two d. Set X_A=d, X_B=-d,
`p_A=(24/c)d`, `p_B=-p_A`. The separation is 2d and V vanishes with all
local derivatives. Differentiate the joint Hamiltonian and verify

```
epsilon_A=26, epsilon_B=51, Htot=77,
v_A=(12c/13)d, v_B=-(8c/17)d,
clock_A=5/13, clock_B=15/17,
|v_B| clock_A/(|v_A| clock_B)=2/9.
```

The raw speed ratio is instead 26/51. These are exact endpoint and local
flow identities. This program does not integrate a scattering orbit or
prove that the initial and outgoing fixtures share one trajectory; that
connection and any monotonicity/global continuation argument must be in
PROOF.md. In the outgoing free region X and Y have the same velocities.

## 6. Three complete-reference calibration comparisons

Use the original F_A=sqrt(h^2+c^2 q) and a different declared law

```
a(h)=1+(h-10)^3/12250,
F_B=sqrt(h^2+c^2 a(h)q),    q=p.p.
```

Analytically, for every h>0, a(h)>0 and a'(h)>=0, so F_B is positive
and F_B,h>0. Also a(10)=1, a'(10)=0 and a(45)=9/2. Consequently its
entire free Hamiltonian vector field agrees with F_A on the whole h=10
reference shell, including the internal clock, while its h=45 rest
Hessian is different. These universal statements require the proof.

The three exact finite comparisons are:

1. Rest preparation A, c=1, p varied along e1: both Hessians are 1/10.
2. Rest preparation B, c=1, p varied along e1: F_B Hessian is 1/10,
   whereas F_A Hessian is 1/45. For equal opposite weak force, their
   canonical-center acceleration ratios are therefore 1 and 9/2.
3. Preparation A at p=(15/2,0), c=1, X=0: both energies equal 25/2,
   and all fourteen actual automatic derivatives agree, including those
   determining the internal clock and center velocity.

The universal boost premise excludes this F_B, but the native arbitrary-
target counter-reading theorem does not select that premise. This audit
does not rerun native U or convert its existing classification into a
physical law.

## 7. Five negative controls and frozen outcome

1. At A with p=X=0, `{X2,K1}=3/10` while the covariant-center right side
   vanishes: the canonical X cannot be silently called covariant.
2. At the same state `{Y1,Y2}=3/50`: the covariant Y cannot be silently
   called canonical.
3. The outgoing raw speed ratio 26/51 differs from 2/9.
4. At A, p=(15/2,0), c=1, omitting the actual internal-clock factor 4/5
   changes the internal relative-position velocity.
5. At that same point F_N=205/16 and dF_N/dp1=3/4, whereas F_R=25/2
   and dF_R/dp1=3/5. Substituting F_N into the same displayed algebraic
   boost formula fails `{K1,F_N}=p1` under the actual canonical bracket.

All equalities are exact, with no tolerance or adaptive fixture. A named
failure prints `FALSIFIER=...`, `RESULT=FAIL` and exits 1. Unexpected
exceptions likewise produce a distinct failure code and exit 1. The first
result is retained; code is not repaired and rerun under the same pin.

Successful stdout contains ten lines: free covariant cases36; fourth
discriminators6; bound B witnesses1; contact cases8; rest acceleration
ratios4; outgoing cases4; reference calibration cases3; negative controls5;
`RECOIL_MASS_RATIO_A_OVER_B=2/9`; RESULT=PASS. The mass-ratio orientation
is A over B throughout this output. Actual stdout is captured only after the
public prospective pin/readback.

This finite audit covers only the enumerated algebraic identities. The
all-state results, source/target selection boundary, physical-unit freedom
and native/physical admission limitations are analytical obligations, not
claims established by these finite checks.
