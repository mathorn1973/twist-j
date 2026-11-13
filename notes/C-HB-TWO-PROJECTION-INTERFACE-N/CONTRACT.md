# Frozen analytical contract

**NON-CANONICAL / L1 / no normative authority.**
A. M. Thorn, 2026-10-15. Original work Apache-2.0.
Candidate `C-HB-TWO-PROJECTION-INTERFACE-N`, issue #1509.

## 1. Exact inherited objects

All objects are mathematical premises from the pinned public sources in
SOURCES.json. Public authority is STATUS.md on main, not any candidate.
The combined R1 is c67b9af4f25f9ebb5904e3d654fd9fb3856c8c6f; its original
CONTRACT and explicit R1 erratum are read together. The source selection does
not grant acceptance to every source claim.

D3={x in Z^3: sum(x)=0 mod 2}. Shell squared lengths are 2,4,8,10,16,
with weights 6,1,15,1,1. Let Bst contain all vectors on those shells,
B0=Bst union {0}; y0=(0,0,0), y1=(1,1,0), y2=(1,0,1),
y3=(0,1,1), y4=(2,0,0), Y={y0,...,y4}, D=Y+B0+B0.
D is the fixed inherited Dirichlet domain, not a variable thermodynamic limit.
P:Q^4 -> Q^D inserts at y0,...,y3, in that order. Let L_D have diagonal
8/9 and off-diagonal -weight(|x-y|^2)/324 on admitted stencil displacements.
H=2I-L_D is symmetric. Set K=I-PP^T/2, J0=I-PP^T and T=KH.
For z in Q^4, S z=sum_(i=0)^3 (z_i-sum(z)/5) delta_yi
-sum(z) delta_y4/5. Define s0=S e0, s1=S e1, A=[s0 s1].
Thus A is a D-by-2 source matrix, distinct from either tape.

Let r=(q,r2) in F5^2. The balanced lift ell(0,1,2,3,4)=(0,1,2,-2,-1)
defines eta(r)=(ell(q)/2,(ell(r2)+1)/2,0,0). Write eta2(r) for its first
two entries and a(r)=A eta2(r)=S eta(r). All 25 r are in scope; the five
origin-zero prepared labels form only a subset.

Wave states are (u,v) in W=Q^D x Q^D. Four rational four-vector tape
slots and k in Z/2Z form the rest of X. The wave energy is
E_D(u,v)=(||u||^2+||v||^2-u^T H v)/2. E_full is E_D plus twice the
sum of the four squared tape norms, counting each slot once.
The supplied F replaces (u,v) by (v,w), where
w=K(Hv-J0u+4P a_in), b_out=a_in-P^T(w-u)/2,
and permutes slots ((A0,A1),(B0,B1)) to ((A1,B1),(b_out,B0)).
Here a_in=A0 is an incoming tape vector, not the contact source a(r).

Fix B in Q_(>=0), a store b in [0,B] cap Q, Wlog in Q and sigma in {+1,-1}.
For a fixed retained r define
Delta_sigma=E_D(u,v+sigma*a(r))-E_D(u,v).
The supplied H_B accepts iff 0<=b-Delta_sigma<=B and then maps
(v,Wlog,b,sigma) to (v+sigma*a(r),Wlog+Delta_sigma,b-Delta_sigma,-sigma).
It is the identity otherwise; u,r,tapes,k and other stated registers are fixed.
The global native U is not asserted to be invertible or to implement H_B.
All equality is literal rational coordinate equality, zero tolerance.

## 2. Questions, fixed before the new proof

Q1. Define R(u,v)=A^T(v-Hu/2)=(rho0,rho1). Does every Delta_sigma for
all 25 labels, both directions and every rational wave factor through R?
Give the exact formula, and identify the label-specific scalar versus a
single receiver-independent summary. Prove the reduced contact transition
on (r,R,Wlog,b,sigma) and its inverse/guard behavior, including both refusal
reasons and accepted zero. A factor map does not reconstruct the full wave.

Q2. Determine a fixed support sufficient for acquiring each rho_i on this
supplied lattice and derive the exact contact update of the summary.
No smallest spatial footprint or physical spatial dimension is claimed.

Q3. Compare every fixed rational LINEAR map L:W->Q^m, independent of r,
from whose value an arbitrary decoder f_(r,sigma) recovers every exact
Delta_sigma on W. Other fixed parameters may be supplied but not hidden
wave coordinates or a wave-dependent initialization. Classify L by kernel
inclusion and determine the sharp rank. Do not infer minimum nonlinear
encoding, number of bits, quantum dimension, or a minimum controller.
The class concerns exact work, not just one Boolean funding decision.

Q4. Does R also define an autonomous factor of the supplied F, even when
all four current tape slots, k, E_full and fixed contact/store/control
registers are given? Give the exact refresh formula R(F X).
Positive closure requires a total map of that summary with equality for
all X. Negative closure requires two exact occupied states with identical
input summaries and unequal next R. They need not be reachable from the
special two-use common-ready layer; no no-go on that narrower layer may
be inferred. Do not claim that any one-step enlarged summary closes all
later propagation or that the whole D wave is a minimal carrier.

Q5. Audit the origin of the operations required to acquire and update this
summary and actuate the contact: native label, eta, rational wave carrier,
local linear acquisition, arithmetic, exact order comparison, bounded
store update and retained direction. Distinguish CANON-ADMITTED,
EXPLICITLY-SUPPLIED-COMPARISON and UNSUPPLIED using exact source scopes.
No new primitive alphabet or compiler is authorized by this question;
A1's Q3 remains outside this candidate.

## 3. Pre-exposed expectations and falsifiers

Earlier chat exposed the expected G=A^T A=(1/5)[[4,-1],[-1,4]] and
Delta_sigma=(eta2^T G eta2)/2+sigma*eta2^T R, with accepted update
R'=R+sigma*G eta2. These are exposed targets to prove or refute, not
blind predictions. Earlier chat also warned that contact closure need not
imply F closure; no previously computed F collision is used as evidence.

Any failed displayed exact identity, invalid carrier, missing label/sign,
or counterexample to a universal clause refutes that clause. Do not move
a threshold or silently change the source S, F, eta, D or H_B.
Q3 accepts a proof of the complete frozen class, not a finite search.
Q4 distinguishes all-occupied from common-ready states explicitly.
Q5 cannot convert an algebraic formula or rational implementation into
native admission. Result statuses stay candidate-T/candidate-D/candidate-C
where justified, with physical status NOT_READY and NO Canon promotion.
