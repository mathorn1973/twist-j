# TT native emission: owner review and the remaining normalization task

**Status: NON-CANONICAL analytic review and Canon proposal.**

Reviewer: Codex-TT-closure-review-20260911, for A. M. Thorn.
Review lock: #946. Existing candidate ownership: #931.

Public basis: Canon v83, main
`3e8518e7e3420a4618328bd11e6b0b696ed5c28c`.
Content commit: `528e868abaa368403ac3c7e81ebd326a3d81b588`.
Canon SHA-256:
`aaaa9773390b3283f6ea72df1ef47fb5d29f80db2197b2b6419e32b65757bca6`,
601172 bytes.

Reviewed candidate: PR #932 at
`8b0cd3b0b15ac11c73c8800e77571538af9c2019`.
Immutable preregistration/verifier pin:
`a8e35e95d8adb891a28233779f2547a2441d70f1`.

## 1. Verdict and evidence ceiling

The written mathematical construction is accepted at its frozen L1 scope,
with the input-versus-conclusion distinctions below. The reviewer derived
the coefficient class and the variational and work identities directly from
PREREG.md and the public action, without reading or reusing verify.py.
PROOF.md was also read. This is an analytic review, not blind two-agent
confirmation, a new formal probe, or an independently implemented verifier.

The original public computation gate is independently observable: workflow
34450033441 on the reviewed head passed both required architectures and
the aggregate check. This fact does not turn the review into an independent
computational confirmation. Frozen files and thresholds are unchanged.

Proposed owner decision: adopt one isolated-packet emission dictionary at D,
provided its exact scope, source-work convention, output equality and
remaining physical boundaries are included in the Canon. There is no basis
for an unconditional physical-emission T claim. Until that separate reviewed
fold, TT-SOURCE remains O.

## 2. The original owner condition

The v83 registry scope is:

> the emission map from an explicitly defined public source object

Its decision condition is:

> closes positively by deriving the typed emission map and its source dependency; closes negatively if no map satisfies the registered TT propagation and conservation constraints

The positive branch is an existence problem. It does not require global
uniqueness, a numerical tensor-to-scalar ratio, or a complete nonlinear
source theory. The negative branch is universal and is not being invoked.
Acceptance must nevertheless provide a complete typed map and its source,
and cannot replace conservation with an unaccounted impulse.

The construction supplies the requested mathematical existence at one
declared reading. Its physical interpretation is a dictionary choice. A
positive D adoption must retain that distinction rather than claim that
the complete emitter dynamics or the physical occurrence of an impulse
has been derived.

## 3. Re-derived quadratic class and normalization

Use complex coordinates x,y for the real spin-one doublets. Rotation weight
two admits precisely

    Q(x,y)=A*x^2+B*x*y+C*y^2.

All quadratic monomials involving one conjugate have weight zero; those
with two conjugates have weight minus two. Reflection covariance makes
A,B,C real. Q(y,x)=-Q(x,y) implies B=0 and C=-A. Thus the complete declared
local homogeneous quadratic class is

    Q_kappa(x,y)=kappa*(y^2-x^2), kappa real.

This is a classification of the frozen class, not of every possible source
map. Locality, degree, representation type and slice antisymmetry remain
premises.

For Phi=H1-H0, the emitted zero-start energy is kappa^2*Phi^2/2. The
preregistered complete-transfer convention A5 equates this with the K1
kinetic channel Phi^2/2. Since active packets exist, |kappa|=1 follows.
The displayed plus sign is then a frozen relative orientation convention.
Energy and antisymmetry alone do not distinguish +Phi from -Phi.

Consequently no adjustable magnitude remains *within this convention*,
but A5 itself is not derived from J, energy conservation alone, or the
quadratic classification. Both this convention and the sign must appear
in any adopted definition. The frozen preregistration already states them;
the present review changes no condition and fires no new falsifier.

## 4. Native source, totality and context

The even/odd child-window decomposition of 0->01, 1->10 gives exactly the
ten K1 words. The pair-frequency equations have the unique solution
f00=f11=1/6, f01=f10=1/3; the triple and four-letter decompositions give
the printed masses, including 1/6 for 0110 and 1001 and 1/12 otherwise.
Existence of these frequencies need not be assumed: normalized finite
prefix counts obey the same affine pair recursion with an O(1/N) boundary
error and a linear part of norm at most 1/2 in the max norm. Iteration down
the dyadic scales gives convergence. Triple and four-letter counts then
inherit convergence from their finite even/odd decompositions.

The exact source object is Src(w)=(w,u0,u1,b0,b1,H0,H1), with the existing
K1 definitions. u0=w2-w0 and u1=w3-w1 are L1 reads of the native bits;
comparison with the L5 omega formula adds no reverse layer dependency.
Stationary word masses are arithmetic frequencies, not an event law or
an L6 probability adoption.

The output context must include labelled sites, the selected plus frame,
the marked local onset, zero initial outgoing field, the unchanged L,
the isolated impulse, and literal equality of every marked field slice.
The equation

    h_(m+1)=(2I-L)h_m-h_(m-1)+delta_(m,1)*Phi

uniquely defines every finite prefix and all prefixes restrict consistently.
h2=Phi; the mean remains zero. Four packets are static and six emit.
This is not a rule for overlapping windows along a whole native orbit.

## 5. Source factors from the full constrained action

Take the public quadratic lapse/shift action A2, with all its independent
metric variables retained, and add the declared symmetric stress coupling:

    A_lin=A2/(2*lambda)+(1/2)*sum_(n,r,i,j) S_ij(n,r)*H_ij(n,r),
    lambda=216*pi.

At H11=h_plus, H22=-h_plus, H12=H21=h_cross, the TT variation of the
first term is -(R_L h_plus*delta h_plus+R_L h_cross*delta h_cross)/(2*lambda).
The stress term is S11*h_plus+S12*h_cross when S22=-S11. Therefore

    R_L h_plus=2*lambda*S11=-2*lambda*S22,
    R_L h_cross=2*lambda*S12.

The factors in #932 are correct. Setting rho=J_i=S_i3=0 satisfies the
linear planar Noether source laws identically. It removes no failing
longitudinal component: the transverse stress is an explicitly chosen
source in the unconstrained transverse sector.

This check does not identify the zero linear rho with the nonzero quadratic
source-work contribution. Those have different perturbative orders.

## 6. Work transfer and auxiliary constraint

Put a=h_(n-1)(x), b=h_n(x), c=h_(n+1)(x). The kinetic difference is

    ((c-b)^2-(b-a)^2)/2=(c-a)*(c-2*b+a)/2.

For an oriented edge x->y, set d=h_(n-1)(y), e=h_n(y), f=h_(n+1)(y).
At x the assigned spatial-energy difference is
w*(e-b)*((f-c)-(d-a))/4. The current is
w*(e-b)*((c-a)+(f-d))/4. Their difference equals
w*(c-a)*(b-e)/2. The y endpoint gives the corresponding opposite-sign
identity. Summing incident edges proves

    Delta e+B^T j=(h_(n+1)-h_(n-1))*R_L h_n/2.

At h0=h1=0, h2=Phi, the field receives Phi^2/2 at onset. The frozen
source channel decreases by precisely that amount, and after onset the
force is zero. Total local work therefore balances on every isolated
history, not merely on the verifier's finite horizon.

The complete source object's microscopic energy has not been identified
with that channel. Its stipulated depletion is part of the isolated
transfer contract, not an additional derived source equation.

Finally 2L*tau=Pi0(e+e_src), mean(tau)=0 has a unique solution since the
weighted graph is connected. The conservation identity gives

    B^T p=-B^T j/2-L*Delta tau=0.

The mean is accounted for by conservation, not silently removed from a
failed equation. This algebraic compatibility does not produce a joint
nonlinear action for the complete emitter and geometry.

## 7. What an adoption can and cannot close

At the selected scope the map, source dependency, unchanged planar
propagator and linear/quadratic conservation checks are all supplied.
That permits the proposed positive D adoption under the original
existential clause. It does not require or justify a universal claim
about all sources, propagation on curved backgrounds, or a unique reading.

The word 'emission' in that D must mean the exact isolated source-to-field
dictionary just reviewed. It must not be expanded into a claim of a
microscopic emission clock, irreversible flux, complete source depletion,
outgoing vector dynamics, detector response or a physical occurrence law.
None of those is falsified or proved impossible here.

The same square on the source descriptor and a square-root dynamics for
the outgoing field are different constructions. #932 does not use the
singular action pullback h=v^2 rejected in #930. It consequently avoids
that specific silent/emitting-branch failure without repairing the
rejected pullback itself.

## 8. Exact next task under the existing normalization owner

TT-VECTOR-STATE-NORMALIZATION retains its full O scope. The next definition
must freeze one complete joint input, evolution and readout tuple:

    (source state, outgoing vector carrier, state law or occurrence rule,
     evolution, vector-to-tensor relation, two-point data, pseudo-covariance,
     fourth moments or complete state, action normalization,
     scalar carrier and readout, tensor/scalar units, comparison equality).

The immediate decision is whether the selected isolated construction can
be extended to this complete tuple without an additional free
dimensionless input, while retaining the K1 input and the registered
TT relations. It must distinguish b_src from any outgoing vector and
must state whether the emitted h is the registered square of that vector.
The emission theorem itself supplies neither the vector nor its law.

No scalar denominator may be manufactured from the trace of the selected
TT representative, which is zero, or from det(I+H)=1-|h|^2 without a
separate physical scalar dictionary. If P_S vanishes or is undefined,
no finite r_T, including zero, follows. Low-order covariance agreement
and Gaussian/Wick replacement cannot bypass the registered fourth-moment
boundary.

This is a definition task under the existing O, not a new O, a probe pin,
a predicted spectrum, or a request for more general foundation classes.

## 9. Older-lane reconciliation

#910 records useful linear lapse/shift structure and a restricted
same-carrier derivative obstruction. The later public K1 construction
already fixes an algebraic D with -D^2=L; the typed incidence factorization
L=B^T W B does not require a rational same-carrier square root.

#911's predefinition is now present on main. Its historical FRW-INHOM O
label is not the current owner status. v83 closes the explicitly selected
hybrid existence clause, not every stronger full-ADM or GR demand listed
in that historical issue. Its remaining wider demands do not automatically
become extra conditions of TT-SOURCE, and are not erased by adopting an
isolated emission map.

No archived note, source, failed construction or unmerged branch is
deleted by this reconciliation. Hodge-Tate and RH notes supply no premise
of this proposed owner closure.
