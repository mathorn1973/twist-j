# One local L5 coupling with an exact energy account

PUBLIC / NON-CANONICAL. Action layer: L1. Authority: none.
Candidate C-FIELD-L5-ENERGY-FUNDED-COUPLING-N, issue #1305.
This proof uses the frozen PREREG at
f3993f87f537cfaa991bef3875ba5d74bfc82855. Universal algebraic statements
below are separate from the finite executable audit and its later outcomes.

## 1. Source account and statement

At public base b8ba1a07ad776cdd8d878fe0a407e07312c0e263, Canon v95
already proves INTEGER-F-JG-INVARIANTS, INTEGER-ENERGY-FUNDED-INVOLUTION,
FIELD-GAUSS-CONTACT-MEMORY and FIELD-EISENSTEIN-RESONANCE. Their respective
inputs here are the matter chart and quadratic family, the generic funded
involution, the pointwise Gauss bookkeeping, and the chosen R18/A20 channel.
Neither the generic funding construction nor the two matter energies is new.

The L5 field input is the public, reviewed NON-CANONICAL candidate
C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N at
dcfde46760bdfd4551686be1e99b5433fa6e9adf, whose PROOF.md has SHA-256
d9cde5b2182fbd8526865c1117730099b91d2fa1a0d78e059b3707abacffeb78.
It is not Canon authority. We restate the needed definitions and certificates;
no predecessor executable or private archive is a runtime dependency.

The result is a total involution G on a declared integer cell, preserving
its full energy and pointwise Gauss defect. The selected complete cell step
Ucell=F after G has inverse G after F^-1 and satisfies Ucell^10=I.
Its stated witness has exact period ten. This constructs a conditional law,
not a derivation of the architecture or a directed physical reaction.

## 2. Complete carrier, matter and raw field

The state is (m,b,z,r). The ordered triple m=(m0,m1,m2) consists of three
Z4 matter registers at vertex 0. The three Z4 spectators b=(b0,b1,b2)
are stored at their corresponding vertices. The raw field z=(E,M) is in
Z4 times Z2, in order (E0,E1,E2,E3,M0,M1). The neutral stored resource
r is in Z>=0. Thus there are 31 integer coordinates, with the last
nonnegative. Equality means equality of all these ordered coordinates.

The oriented multigraph has vertices 0,1,2 and edges
(e0,e1,e2,e3)=(0->1,0->1,0->2,2->1). The first two are distinct parallel
edges. Its face columns are e0-e1 and -e0+e2+e3. With +tail/-head,

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0.
Hraw(E,M)=E^t E+M^t M+E^t C M.
```

For matter in the canonical four-phase chart, set chi(v)=sum_i v_i and
Q(v)=v^t K v, where

```text
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Htotal=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
rho=(chi(b0)+sum_j chi(mj),chi(b1),chi(b2)), defect=DE-rho.
```

K has eigenvalues 9,1,7,7, by its constant, alternating and remaining
two-dimensional subspaces. It is the selected canonical (6,2,-1) form.
Also C^t C=[[2,-1],[-1,3]] has eigenvalues (5+-sqrt(5))/2 below four.
The identity 4Hraw=||2E+CM||^2+M^t(4I-C^t C)M proves positive
definiteness. Consequently Htotal is a nonnegative integer on the full
carrier. Spectator energy and resource energy are actual terms in this sum.
No measured charge or physical energy identification is made.

## 3. Integral split and field certificates

Define the embeddings, active action and bilinear matrix by

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]], H(x)=x^t B x/2.
```

For rational z the unique solution z=P(a,b,c,d)+S(u,v) is

```text
a=(2E0-3E1+E2+E3)/5, b=(-E0-E1+2E2+2E3)/5, c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

Substitution into E=(a-b+u,-a+u,b+v,b+u-v) proves both inverse
identities. Write g=2E0-3E1+E2+E3. Modulo five the four electric
numerators are respectively g,2g,g,3g. Thus all split coordinates are
integers iff g=0 mod5. The residue map is onto Z/5 because its E2
coefficient is one, so the split lattice has index five in Z6.
The lattice PZ4 is saturated: extraction (-E1,E2,M0,M1) is an integer
left inverse on its rational span. The static span has E0=E1=u,
E2=v,E3=u-v,M=0, so SZ2 is separately saturated as well.

Direct substitution gives DP_E=0, C^t S_E=0 and

```text
DE=(2u+v,-3u+v,u-2v),
Hraw(Py+Ss)=H(y)+Hstatic(s), Hstatic(u,v)=3u^2-2uv+2v^2,
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
```

The static cross terms vanish because C^t S_E=0 and P_E lies in
im C. Positivity of H follows from injectivity of P and positivity of
Hraw. In particular a nonzero integer active vector has H>=1.
For arbitrary raw z, g=2(DE)_0+(DE)_2 mod5. This identity involves the
actual field divergence, irrespective of whether matter satisfies Gauss.

The free field map and its inverse are

```text
T(E,M)=(E+CM,M-C^t(E+CM)),
T^-1(E',M')=((I-CC^t)E'-CM',C^t E'+M').
```

Their shear factorization proves integrality and mutual inversion.
Substitution gives Hraw(Tz)=Hraw(z), DT_Ez=DE, TP=PA and TS=S.
An exact certificate of the active order is

```text
Kcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]], det Kcyc=-1,
Z=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]], A Kcyc=Kcyc Z.
```

Here Z multiplies t in Z[t]/(1+t+t^2+t^3+t^4), so Phi5(A)=0 and
A^5=I. The rational split spans all six raw coordinates. Therefore
T^5=I on the entire raw space, including the four nonsplit residue classes.
Energy invariance restricted to P also gives A^t B A=B.

## 4. Exact L5 image and inverse

Use the integer matrices

```text
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

Multiplication gives L=(I-A)(I-A^2), N=A^2 L and AL=LA.
Reducing (1-t)^2(1-t^2)^2 modulo Phi5(t) gives 5t^3. Hence
L^2=5A^3 and LN=NL=5I. Both L and N commute with A.
For the B-adjoint, A^*=A^-1, so
L^*=(I-A^-2)(I-A^-1)=A^-3 L=A^2 L=N.
It follows that L^t B L=5B and H(Lx)=5H(x).

A complete integer image certificate, rather than shell recognition, is

```text
V_H=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]], det V_H=1,
L V_H=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
```

Thus det L=25 and its image is exactly the set of y=(a,b,c,d) for which
a-3b and c-3d are divisible by five. Equivalently,

```text
y in LZ4 iff a+2b=0 mod5 and c+2d=0 mod5.
```

The Hermite coefficient vector is ((a-3b)/5,b,(c-3d)/5,d).
On this image alone, x=Ny/5 is integral and uniquely satisfies Lx=y.
Indeed y=Lx implies Ny=5x, and divisibility of Ny conversely gives
L(Ny/5)=y. There is no rounding or omitted phase coordinate.
The image has 25 residue classes among the 625 classes modulo five.
Whole-shell surjectivity fails: H(0,0,1,-2)=5, but c+2d=-3 mod5.
That vector is not admitted, however large the stored resource is.

## 5. Matter endpoints and the total funded gate

Fix only phase i=0 and the literal ordered endpoints

```text
R=(e0-2e1+e2,0,0), A_matter=(e0,-e1,e2-e1).
```

Their sums are both e0-2e1+e2, and their additive Q energies are 18
and 20. For example Q(e2-e1)=6+6-4=8, giving 6+6+8=20.
Their node-0 total chi is zero. Individual register charges change:
R has (0,0,0), whereas A_matter has (1,-1,0). These two ordered
tuples are distinct and encode the reaction branch without an extra bit.

Before funding, pair each (R,b,PLx+Ss) with (A_matter,b,Px+Ss),
for all integer x,s and all spectators b, and fix every other state.
Unique splitting and injectivity of L make these disjoint two-element
pairs. This defines an unfunded involution even at x=0, since its matter
endpoints are different. Its non-resource energy changes by 2-4H(x)
on the R side and 4H(x)-2 on the A_matter side.

The funded gate G has these exact branches, with h=H(x):

```text
(R,b,PLx+Ss,r) -> (A_matter,b,Px+Ss,r+4h-2), if r+4h-2>=0;
(A_matter,b,Px+Ss,r) -> (R,b,PLx+Ss,r+2-4h), if r+2-4h>=0.
```

To recognize the first branch, test the raw split, then the two image
congruences, before forming x=Ny/5. To recognize the second, test the
raw split and take its active x directly. An off-endpoint tuple, failed
split, failed image test or failed resource test fixes the ENTIRE state.
No earlier partial write survives rejection. This is a total map of the
declared carrier and an instance of INTEGER-ENERGY-FUNDED-INVOLUTION.

For completeness, an accepted first branch has reverse resource
(r+4h-2)+2-4h=r>=0; the converse calculation is identical. The reverse
field reconstruction uses Lx and its exact inverse, and recovers s,b,m.
Every rejected state is unchanged and rejects again. Thus G^2=I on all
states, including offimage, nonsplit, off-endpoint and non-Gauss states.
For h=0, the R side requires r>=2 and the other side adds two. For h>=1,
the R side always has funding and deposits 4h-2; reversal needs that amount.
In particular h=1 leaves two stored units after paying the matter increase.
Zero-field reservoir-funded switching is part of this chosen law.

## 6. Complete energy and pointwise conservation

On a switched R state the input and output energies are respectively

```text
18+sum_j Q(bj)+5h+Hstatic(s)+r,
20+sum_j Q(bj)+h+Hstatic(s)+(r+4h-2).
```

They are equal. The opposite branch reverses this equality, and fixed
states preserve it trivially. Resource nonnegativity follows from the guard.
No static or spectator energy has been scaled, deleted or omitted.

Each switched field keeps exactly the same s, so its actual DE is
unchanged. The full matter vector sum at vertex 0 is unchanged; all
spectators are retained, hence every component of the actual rho is
unchanged too. Thus every component of DE-rho is preserved, even when
that vector is initially nonzero. In particular the Gauss subset DE=rho
is invariant. This is node-local charge conservation with zero transported
current, not conservation of the separate reacting-register charges.

## 7. Selected complete cell step and its exact recurrence

Define F(m,b,z,r)=(m,b,Tz,r) and Ucell=F after G. The preceding shear
identities give an integer inverse F^-1, preserve Htotal and each defect
component, and give F^5=I. Therefore Ucell^-1=G after F^-1 already
follows without a commutation assumption.

Here F and G also commute. On split states, F sends x to Ax and fixes s.
It preserves H(x), maps LZ4 onto itself, and commutes with both L and N.
Thus it preserves every image and resource decision and yields the same
updated field in either order. On nonsplit states, F preserves g modulo
five because it preserves DE, so both applications of G fix their inputs.
Off-endpoint matter remains off-endpoint under F. This covers every state,
including every rejected branch, without imposing Gauss.
Consequently Ucell^n=F^n G^n, Ucell^5=G and Ucell^10=I on the full
carrier. The only possible periods divide ten. These are complete-state
identities, not identities after discarding a branch, phase or resource.

Set w=(0,0,1,0), for which H(w)=1 and Lw=(-1,-2,1,2). With fixed
integer s and spectators, start at (R,b,PLw+Ss,0). At step k the state is

```text
even k: (R,b,PL A^k w+Ss,0);
odd  k: (A_matter,b,P A^k w+Ss,2).
```

This follows by induction from the gate and commutation identities.
The fifth step changes the matter endpoint, excluding periods one and
five. Also A^2w=(0,1,0,-2) differs from w. Injectivity of P and L makes
the second step different, excluding period two. The period is exactly ten.

## 8. Explicit accounts, rejection boundaries and finite audit

For s=0,b=0 the neutral gate example has total 18+5=20+1+2=23.
For s=(1,0), choose b=(2e0,-3e0,e0). Its spectator energy is 84.
The high and low raw fields are (2,2,-2,-1,1,2) and (1,1,0,1,1,0).
Both have actual divergence (2,-3,1), matching the stored matter charges.
Their field energies are 8 and 4, and the complete account is
18+8+84+0=20+4+84+2=110. The same exact period-ten formula retains
this nonzero-charge static field and all spectators at every step.

At the low w endpoint, r=0 or1 must reject reversal. Clipping its proposed
negative resource to zero would increase energy by two when r=0.
Dropping the forward surplus instead would lose two. Omitting spectator
energy undercounts the charged example by84; deleting S(1,0) destroys
its actual charges. Conflating the two matter patterns loses the branch
needed for the asserted inverse: at z=0,r=2 the R input gives resource0,
whereas the A_matter input gives resource4. After identifying their matter
patterns these identical projected inputs would have different outputs.
Clearing retained coordinates does not recover the literal input state.

The raw field (1,0,0,0,0,0), with spectators (e0,-e0,0), satisfies actual
Gauss but has g=2 mod5, so G fixes it even with R and r=100. Likewise
the H=5 offimage example is fixed. Adequate energy does not imply split
or image admission. Neither a permutation of the ordered matter tuple
nor another matter phase is silently identified with a switching endpoint.

For the frozen 625 representatives y in {0,1,2,3,4}^4 there are exactly
25 image members. Exactly one is zero; each other inverse has integer
H>=1. Thus on the R endpoint r=0 gives 24 switches and 601 fixed states,
whereas r=2 gives 25 switches and 600 fixed states. These counts concern
the literal representatives, not an energy shell or all lifts of residues.
The other finite fixtures and exactly ten witness steps are specified in
PREREG. Their execution can audit these identities but cannot replace the
universal proof or establish an unregistered architecture claim.

## 9. Interface, construction choices and limits

G accesses the four edge and two face registers of this fixed cell, the
ordered reacting triple, and its resource. F uses the same field cell.
Spectators are unchanged; their energies and charges remain part of the
full state. Both inverse operations have the same finite support. No
outside register is read or changed. This is finite-cell locality, not a
one-edge implementation, a global parallel schedule or an overlapping-cell
compatibility theorem.

The multigraph, orientations, matter chart and metric, fixed phase i=0,
selected endpoints, omitted other reactions, neutral resource, spectator
registers and order of the complete step are declared architecture choices.
The prior image theorem supplies admission and inversion; it does not
select this coupling. No preparation or reader is derived. The literal
integer tests preserve information on admission and fix the complement.

In particular Ucell is not the native canonical U. Its period-ten result
prevents describing its own repeated reaction as one-way decay, escaping
transport, a permanent record, a waiting-time law or irreversible emission.
It supplies no detector, particle identification, multicell coercivity or
physical L1--L6 bridge. QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and PHOTON-MASSLESS-PHASE remain open.
Any promotion and any later composition task require separate disposition.
