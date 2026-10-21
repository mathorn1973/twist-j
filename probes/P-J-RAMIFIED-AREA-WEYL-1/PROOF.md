# Proof: reciprocal J/phi area and ramified Weyl covariance

PUBLIC / NON-CANONICAL / L1. Evidence for P-J-RAMIFIED-AREA-WEYL-1, issue #1582.
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Basis: Public Canon v103, pin \`6b459a66d670656bd02a09c26da666bd16c077fb\`.

This is a self-contained algebraic derivation written by the probe owner. It
does not constitute independent review or a physical action derivation. Every
result below is conditional on the **marked choice of the pair carrier and
Weyl representation**. Previously registered J-PROJECTIONS,
J-GOLDEN-BRIDGE and FORCE-WEYL-HOLONOMY are credited as inherited inputs.

## A. The cyclotomic identity and the ramified ring

Let O=Z[j]=Z[X]/(Phi_5(X)), with
Phi_5(X)=X^4+X^3+X^2+X+1, and choose the symbol j for the residue of X.
Put J=1+j^2 and phi=-j^2-j^3. Then

    J phi = -(j^2+j^3+j^4+j^5)
          = -(1+j^2+j^3+j^4)
          = j.

The second equality uses j^5=1, the third uses
1+j+j^2+j^3+j^4=0. It follows that (J phi)^5=1; j is a
primitive fifth root. Both J and phi are units (the original J-unit
fact is part of the public Canon; phi is the familiar real quadratic
unit with phi^2=phi+1).

The quotient by the principal ideal (1-j) admits the exact presentation

    O/(1-j) = Z[X]/(Phi_5(X),1-X) = Z/(Phi_5(1)) = Z/5Z.

Its marked map rho sends a power-basis element sum a_k j^k to
sum a_k modulo 5, so

    rho(j)=1, rho(J)=2, rho(phi)=-2=3 (mod 5).

This is a **residue ring** equality, not an equality of complex phases:
rho(j)=1 is the precise reason that complex order-five rotation is
erased by reduction. Any new nontrivial mu_5 phase in a representation
must be read through a separately specified character, not inferred
by applying rho to the scalar j.

## B. The reciprocal pair is conformally alternating, not symplectic
##    at a single complex step

The marked O-module is O^2. Define the O-bilinear alternating pairing
omega((a,b),(c,d))=ad-bc and T=diag(J,phi). For all u,v,

    omega(Tu,Tv)
      = (J u_1)(phi v_2)-(phi u_2)(J v_1)
      = J phi (u_1 v_2-u_2 v_1)
      = j omega(u,v).

Here commutativity of O is essential. Iteration gives

    omega(T^n u,T^n v)=j^n omega(u,v).

Thus T^5 preserves omega exactly on **all** of O^2. The single-step
map does not preserve omega: on u=(1,0), v=(0,1), its value changes
from 1 to j, and j != 1. More accurately, T is a symplectic
similitude of multiplier j, of exact order five in the multiplier.
It would be incorrect to call this one-step conservation of a real
physical action.

The result uses a **chosen paired module** O^2. It neither constructs
the canonical native U nor proves a symplectic form on the original
four-dimensional M_J representation; no such deduction is asserted.

## C. Ramified symplectic reduction

Modulo (1-j), the pair map becomes

    A = diag(2,3) on F_5^2.

Its determinant is 2*3=6=1 (mod 5). In dimension two and over a
commutative field, omega(Au,Av)=det(A) omega(u,v). Therefore

    omega(Au,Av)=omega(u,v)

for every u,v in F_5^2. This is compatible with part B because the
multiplier j reduces to 1. The finite identity is a consequence of
a marked ramified reduction; no photon, time, physical area unit or
energy is derived.

## D. One explicitly selected finite Weyl realization

Take the abstract complex vector space V=C^5 with marked basis
|k>, k in F_5, and j=exp(2*pi*i/5). Define

    Z|k> = j^k |k>,
    X|k> = |k+1>,
    D|k> = |3k>.

These maps are invertible; D^-1|k>=|2k>. Calculation on each basis
vector gives ZX=j XZ. Hence

    D Z D^-1=Z^2,
    D X D^-1=X^3.

For u=(a,b), write W(u)=Z^a X^b. Conjugation yields

    D W(a,b) D^-1 = Z^(2a) X^(3b)=W(A(a,b)).

From X^b Z^c=j^(-bc) Z^c X^b,

    W(a,b) W(c,d) = j^(-bc) W(a+c,b+d),
    W(c,d) W(a,b) = j^(-da) W(a+c,b+d),

and therefore

    W(a,b) W(c,d)=j^(ad-bc) W(c,d) W(a,b).

Thus the Weyl commutator phase is exactly
j^(omega(u,v)) and is covariant under A. This proves a **conditional
algebraic compatibility**, not that the native U automatically
implements D, X or Z. It also does not identify the five basis states
with physical events or select a physical Hilbert metric.

Importantly, the phase map arises from the **chosen additive
character** chi_1:F_5 -> mu_5, chi_1(t)=j^t.
For each t in F_5^*, chi_t(a)=j^(ta) is another nontrivial additive
character. All four are distinct because chi_t(1)=j^t; they are
A-area-invariant because A preserves omega. The marked principal j
makes chi_1 one natural *choice*, but covariance alone does not
select one physical observation map.

## E. Exact nonselection of an energy quantum

Consider rational diagonal Hermitian costs

    H=diag(h_0,h_1,h_2,h_3,h_4), h_k in Q.

The condition D H D^-1=H is precisely h_(3k)=h_k.
Multiplication by 3 has two orbits in F_5:

    {0}, and {1,3,4,2}.

Therefore the full D-invariant diagonal class is **exactly**

    H=diag(h_0,h_1,h_1,h_1,h_1), h_0,h_1 in Q.

In particular, after fixing ground cost h_0=0 and nonnegative costs,
every rational gap Delta=h_1>=0 is admitted. The two explicitly
nonconstant costs with Delta=1 and Delta=2 both preserve the same D
and the same Weyl commutator phase. Hence the covariance and finite
phase data alone cannot select a unique positive energy unit.

Furthermore, a diagonal H commutes with X iff h_(k+1)=h_k for all k,
hence iff H is scalar. Since Z is diagonal, it adds no restriction to
that diagonal class. The stronger statement for **arbitrary complex
matrices** is also immediate: Z has five distinct eigenvalues,
so any H commuting with Z is diagonal; commuting with X then forces
the diagonal constant. Thus the only operators commuting with both
full Weyl generators are scalar.

This separates two possibilities clearly:

1. D-covariance admits nonconstant but freely scaled costs.
2. Full X/Z-invariance excludes any nonconstant local cost on V.

Neither possibility supplies physical energy from the phase alone.
A nontrivial energetic contact would require an additional coupled
carrier/interaction with a registered conservation and calibration
law. The existing energy-funded contacts have separate declared
architectures and do not become a native TWIST-J realization here.

## F. Status, falsifier and physical boundary

Claims A-E are exact conditional L1 algebra, presented as an authored
candidate-T proof. verify.py performs finite, exact, integer audits:
16 residue basis products, 64 alternating basis pairs, 625 F5 areas,
25 Weyl conjugations, 625 commutator pairs, four phase-character
invariance inventories, and 5^5 sampled rational diagonal costs.
The infinite O^2 and rational-energy results depend on the written
algebraic proofs, not on extrapolation from samples.

A counterexample to any identity or classification in its explicitly
marked carrier fires the relevant preregistered gate. A same-session
proof or a two-architecture rerun is not independent physical evidence.

**No physical action, SI hbar, chosen energy/readout, photon identity,
contact compiler, common physical carrier, force law, measurement
occurrence, or L1-to-L6 lift is established.** METRO-EDGE-SCALE [O],
QDD-INSTRUMENT-APPARATUS [O] and native contact admission remain
unresolved. The negative result is specifically the nonselection
within the declared diagonal-cost / Weyl-covariant class, not a
general no-go theorem for all physical decoders.
