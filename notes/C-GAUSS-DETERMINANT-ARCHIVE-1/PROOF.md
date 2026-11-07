<!-- SPDX-License-Identifier: Apache-2.0 -->

# Gauss boundaries and a prepared determinant record

**NON-CANONICAL / L1. Conditional analytical candidate-T only.**
Candidate C-GAUSS-DETERMINANT-ARCHIVE-1; reservation #1951.
These are written proofs in the models frozen in PREREG.md. Independent
public acceptance and the separate finite audit are not asserted here.
The desired coupled root-pair writer remains an open construction.
Use of the quoted P27/P35 trace data is conditional on those supplied
witnesses; their finite audit remains distinct from the general proofs.

## 1. Public premises and conventions

Use O=Z[j], j^4+j^3+j^2+j+1=0, rho=j^2, phi=-j^2-j^3,
h(a)=a*conj(a), and Q(a)=Tr_(K/Q)(h(a))/2. The ordinary contact is
identity outside x-y in 2O and otherwise sends

    s=(x+y)/2, t=(x-y)/2, (x,y) -> (s+rho*t,s-rho*t).

Its admitted linear branch is unitary for sum h, preserves the coordinate
sum, and has determinant rho. The refused branch is identity. The total
contact satisfies C^5=I, including the refused complement. Each slot's
residue modulo 1-j is preserved. An admitted diagonal has determinant rho
even though its actual state and current do not change.
In particular (0,0) is admitted with determinant rho, while (0,1) is
refused with determinant 1; both actual currents are zero. Thus current
alone cannot determine the branch determinant on the unrestricted domain.

The pinned premises are:

- [CONTACT.md, sections Setup and Explicit witnesses](https://github.com/mathorn1973/twist-j/blob/d4d363722f052141a4ce65e9da39f11a74b43b95/notes/C-COMMON-COUNTER-PATH-PHASE-N/CONTACT.md).
- [PROOF.md, sections 1-2](https://github.com/mathorn1973/twist-j/blob/f975ee0056d85583623bfc27cb41a18dda18907f/notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/PROOF.md).
- [RECEIVER-CONTACT.md, sections 1-2](https://github.com/mathorn1973/twist-j/blob/f975ee0056d85583623bfc27cb41a18dda18907f/notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/RECEIVER-CONTACT.md).

The first source distinguishes conserved state account sum Q(z_i) from
the path sum H=sum h(t). Its full-orbit census is candidate-C; these
proofs neither promote that census nor use its completeness.

## 2. G0: the fixed-field boundary

Assume exactly one variable charged coordinate x at vertex v_x and one y
at a distinct vertex v_y. All other contributions to the charges at those
vertices are fixed. The field A,E is fixed throughout the writer. The
writer is a fixed word of ordinary contacts. All uncharged auxiliary,
archive and reference coordinates have the same initial values across
the compared inputs. Fields may differ between inputs but cannot change
during a writer run. Require Gauss at every elementary cut.

**Theorem G0.** No such writer acquires a nonconstant record of x,y in
the initially common uncharged coordinates.

**Proof.** Write the charge vector as

    q = x*e_(v_x) + y*e_(v_y) + q_fixed,    D E = q.

Fixed E and Gauss before and after each primitive give q'=q. Distinct
vertices and fixed other contributions imply x'=x and y'=y separately.
An ordinary contact between x and any auxiliary a preserves x+a; hence
x'=x forces a'=a. The same holds for y. A contact between x,y also acts
as identity on the current state. Refused and diagonal contacts do not
provide an exception. Thus every contact incident to a charged coordinate
is statewise identity on every admissible run. Delete these fixed word
positions. The remaining auxiliary-only word acts on the same initial
auxiliary state for every input, so its final archive is the same. QED.

This is a scoped obstruction, not a universal impossibility theorem.
Input-dependent uncharged e or references may already contain input
information. Extra active charged coordinates at one vertex permit
charge-preserving local exchange. Field updates, supplied admission
controls, changing charge assignments and multi-contact observation cuts
are outside G0. In particular, a branch flag is not an extra physical
register supplied by an ordinary statewise-identity contact.

The declared loaded account is

    Q(x)+Q(y)+Q(e)+Q(y-e)+H_field.

Even an uncharged contact involving e need not preserve this account:
preserving the contacted slots' Q-sum does not preserve Q(y-e). Energy
accounting cannot repair a Gauss violation at an earlier elementary cut.

## 3. G1: continuity preserves Gauss but not complete return

Use the supplied complete graph on six source vertices from PREREG.md.
Orient each distinct edge ab from a to b, so D delta_ab=-e_a+e_b.
Let S=sum z_i at the initial source. The fixed background is b=-S e_1;
initial E_1k=z_k for k>1 and zero elsewhere gives D E=z+b.

For one ordinary source contact set i=(1-rho)*(z_a-z_b)/2 on admission
and i=0 on refusal. The continuity-only extension is

    z'=z+i*D delta_ab,    E'=E+i*delta_ab.

Consequently D E'-z'-b=D E-z-b at every primitive cut. Each edge and
source coordinate keeps its residue modulo 1-j. The source account is
preserved, but no conservation of Q_source+sum_edges Q(E) follows.
This extension is not claimed to implement the loaded contact or the
27-site field. Its field-return test is independent of those claims.

**Proposition G1.** The declared P27 returns z but not E; P35 returns both.

**Proof.** P27 uses edge 35 exactly once. Its first four contacts use only
12, so immediately before 35 one has z_3=u=1-j and z_5=X=1+j-2j^3.
Directly in O,

    t_35=(u-X)/2=j^3-j,
    i_35=(1-j^2)*(j^3-j)=-1-j+2j^3=-X != 0.

No later step changes E_35. Thus Delta E_35=-X. Source closure implies
D Delta E=0, which does not imply Delta E=0. Eight refused C13 attempts
leave this residual unchanged. For P35, the initial C12^5 returns its
source pair and edge. In each C35 C36^5 C35^4 block, C36^5 returns its
pair and its edge before the remaining four C35. The five C35 then have
zero net current as well. Every source and edge coordinate returns. QED.

Q(-X)=15 is a current norm, not the total field-energy increment: the
latter also contains the initial-field cross terms. Extra restoring
currents or shared routing would change G1's declared implementation.

A useful one-edge fact does hold in the loaded model. Its equations are

    d=(2y-x-e+F)/4, i=(rho-1)*d,
    x'=x-i, y'=y+i, F'=F+i, e'=e.

On F=e-x, one has d=(y-x)/2, so its guard and its source update exactly
match the ordinary contact. Also F'+x'=F+x=e, preserving that subspace.
This supplies one edge only. Other contacts can change a shared source
coordinate without changing that edge's F, so no jointly invariant
multi-edge realization follows from this observation.

## 4. M: a finite-horizon record in seven prepared banks

Let L=35, T=2^L, and x0=(B,-B,u,u,X,2), where B=1-j^2. Prepare
z^(0)_0=x0 and z^(k)_0=x0+T*e_k for k=1,...,6. At each of L times,
apply the same attempted pair in the fixed order of all seven banks.
This is a supplied preparation and calendar; x0 is known, not copied
from an unknown state. There are 42 slots and 7L=245 primitive attempts.

**Lemma M1 (matching guards).** All seven banks make the same admission
decision at each of the L synchronized steps.

**Proof.** Initially each difference z^(k)-z^(0) belongs to 2^L O^6.
After m common branch matrices it belongs to 2^(L-m) O^6: an admitted
matrix divides coefficients by at most two; a refused matrix is identity.
For m<L these differences are in 2O^6, so the next pair differences have
the same class modulo 2O and the guards agree. Applying the common branch
continues the induction. Every bank stays integral. No agreement beyond
the stated horizon is asserted. Admitted state-changing counts can differ
between banks; admission, rather than state change, is the shared datum.
QED.

Let M_m be the product of these common admitted matrices, using identity
for a refused attempt. At synchronized cuts, linearity gives

    D_m=[z^(1)_m-z^(0)_m ... z^(6)_m-z^(0)_m]=T*M_m.

Therefore det D_m=T^6*rho^(A_m), where A_m is the admitted count in the
base bank. At the final cut this is T^6*j^4 for padded P27 and T^6 for
P35. These are determinants of actual current difference columns.
Computing that determinant and dividing by T^6 are external mathematical
readings, not an implemented root-pair writer.

Every individual ordinary primitive, including between synchronized
cuts, preserves the complete Q, coordinate sum and each slot residue.
For the known source Q(B)=Q(u)=5, Q(X)=15, Q(2)=8, hence Q(x0)=43.
Since sum x0=5-j-2j^3 and Tr_(K/Q)(sum x0)=23, polarization gives

    Q_initial=7*43+6*(2*T^2)+T*23=12*T^2+23*T+301.

The initial coordinate sum is 7*sum x0+6T. Reversing all 245 primitives
and replacing each C by C^4 gives the literal 980-attempt inverse on the
occupied apparatus. It restores every bank and erases the record. It
does not require extending the matching-guard induction beyond L.

## 5. The larger path account and the remaining boundary

Let H_base be the sum h(t) over base admissions and A their number.
At a synchronized pre-contact cut, put v=(e_a^*-e_b^*)M_m. The common
matrix fixes the all-ones vector and is unitary. Thus

    sum_k v_k=0,    sum_k h(v_k)=2.

The shifted banks' half-differences are t_k=t_0+(T/2)*v_k. Summing their
six Hermitian norms cancels the cross terms. Adding the base bank gives
7h(t_0)+T^2/2 on each admission. On a refusal all banks are identity.
Consequently the complete extended path sum is exactly

    H_extended=7*H_base+(T^2/2)*A.

For the declared pair H_base=55+20phi, but A is 27 versus 35. Therefore
H_extended(P35)-H_extended(P27)=4T^2. M is not an equal-total-area
determinant discriminator. Its conserved initial budget is equal for the
two runs, while their complete path sums differ; neither fact selects a
physical action law.

The separate receiver control uses supplied roots and account 36. Its
response (32,17,2,7,27) establishes no operation that converts D into an
actual phase pair. M also supplies no field coupling or transfer from an
unknown charged input. G0, G1 and M therefore leave the common coupled
root-pair target open. There is no claim here of a physical phase, action
unit, alpha, native-U implementation or universal obstruction to a writer.
