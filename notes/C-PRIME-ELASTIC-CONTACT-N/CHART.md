# Direct Dirac chart: exact range and arithmetic-carrier obstruction

Author: A. M. Thorn
Date: 2026-10-30
Reservation: #1838, C-PRIME-ELASTIC-CONTACT-N
Status: NON-CANONICAL / L1 / analytical candidate-T.
The proposed FULL_DIRECT_CHART is rejected below in its frozen class.
This is not a registered F row or a no-go for other momentum readings.

## 1. Frozen question and inherited sources

The public source is Canon v106, main
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`, specifically
DIRAC-STEP-THEOREMS and LADDER-LIGHTCONE, with exact witness
`reproduce/dirac-ladder/verify.py`, checks INVARIANTS and MASS-SHELL.
DIRAC-STEP and DIRAC-LADDER are D dictionaries; they are not promoted here.
The arithmetic-contact comparison is the same O_+ of PROOF.md and the
noncanonical predecessor #1837, head
`54631cb5128ff0b978a732b1367a8207c434e4f2`.

The existing #1603 / #1605, pinned here at
`da39ea38df90bbf594e90a00f0532964e4e1f041`, CONTACT-KINEMATICS.md sections
1-2 and 4-5, already supplies the sine-shell reader, its fold, the position
commutator and the distinction from phase energy. Those are attributed
inputs and elementary rederivations, not new claims of this note.

Freeze the existing single walk, with mu=2, real Fourier variable k modulo
2pi, zeta=exp(ik), and the Pauli matrix X:

    D_mu(k)=diag(zeta,zeta^-1)(I+i mu X),
    U_mu(k)=D_mu(k)/sqrt(1+mu^2).

No auxiliary sheet, mass change, rescaling, complex k, new position/time
map or different momentum reader is part of FULL_DIRECT_CHART. Choose the
positive sine-energy band, not a positive logarithmic-energy postulate.
The proposed equality is in LIGHT-CONE coordinates:

    Ehat(k)+phat(k)=2 phi^n,
    Ehat(k)-phat(k)=2 phi^-n,        for every n in Z.  (1)

Equating Ehat or phat individually with a light-cone leg would instead be
a coordinate error. The ladder index is not identified with the native U
counter, the contact position q, or physical elapsed time.

## 2. Exact image of the physical Dirac band [candidate-T]

The raw characteristic equation is

    lambda^2-2 cos(k)lambda+(1+mu^2)=0.

Write its positive sine-band eigenvalue as
lambda=sqrt(1+mu^2) exp(-i omega), with 0<omega<pi. Then

    cos(omega)=cos(k)/sqrt(1+mu^2),
    phat=sin(k),
    Ehat=sqrt(1+mu^2) sin(omega)=sqrt(mu^2+sin(k)^2).   (2)

For mu=2 the exact image is therefore

    {(E,p): E>0, E^2-p^2=4, -1<=p<=1}.                (3)

Every p in [-1,1] is attained. In rapidity coordinates E=2 cosh(eta),
p=2 sinh(eta), (3) is exactly

    -log(phi)<=eta<=log(phi).                         (4)

Indeed asinh(1/2)=log((1+sqrt(5))/2)=log(phi). The branch
-pi/2<=k<=pi/2 maps bijectively to this interval; its inverse derivative
is singular at the endpoints. The complete k circle covers each interior
point twice, through k and pi-k modulo 2pi, and each endpoint once.
Their phase angles are omega and pi-omega. Thus the pair (Ehat,phat)
forgets phase-branch data even where it has the right shell value.

## 3. Complete golden-rung intersection [candidate-T]

For the positive inverse ladder define

    E_n=phi^n+phi^-n,
    p_n=phi^n-phi^-n.

Then E_n^2-p_n^2=4. By (4), or by strict monotonicity of
r-r^-1 for r>0, equation (1) is possible exactly for

    n=-1,0,1.                                        (5)

The complete table, with k understood modulo 2pi, is

| n | E_n | p_n | k |
|---|---|---|---|
| -1 | sqrt(5) | -1 | -pi/2 |
| 0 | 2 | 0 | 0 or pi |
| 1 | sqrt(5) | 1 | pi/2 |

At n=2 the target is E_2=3, p_2=sqrt(5); it would require sin(k)=sqrt(5),
which no real k satisfies. At n=-2 the sign of p reverses. Since |p_n|
increases with |n|, these witnesses and monotonicity exclude every
|n|>=2, not just a finite audit window.

Disposition: FULL_DIRECT_CHART is false. The local two-rung-wide rapidity
window (4) survives exactly. No continuum approximation was used.

## 4. A stronger obstruction for the actual contact carrier [candidate-T]

The positive inverse pair (2phi^n,2phi^-n) is not always the pair of Galois
embeddings of the single field element 2phi^n. In F=Q(sqrt(5)),

    conjugate(2phi^n)=(-1)^n 2phi^-n,
    N(2phi^n)=4(-1)^n.                                (6)

For odd n its embeddings have opposite signs, so it is outside the contact
carrier O_+ and has norm -4. Replacing that conjugate by its absolute value
changes the reading; it is not a norm-preserving identification of carriers.
The two endpoint matches in (5) consequently do not provide two massive
arithmetic inputs for the elastic-contact theorem.

More generally, for x=a+b phi in O_+, the unchanged Galois reading is

    E_O=(2a+b)/2,   P_O=b sqrt(5)/2,
    E_O^2-P_O^2=N(x).

Suppose N(x)=4 and (E_O,P_O) lies in (3). Then

    5b^2<=4,

so b=0. Norm four and positivity force a=2. Therefore

    {x in O_+: N(x)=4 and |P_O(x)|<=1}={2}.            (7)

This all-input proof needs no enumeration. Under this direct comparison
the only common massive state is rest; there is no nontrivial pair of
mass-two arithmetic movers on which to transfer #1837's scattering rule.

The full integral norm-four shell also has a simple classification.
Modulo two, a^2+ab-b^2 vanishes only at (a,b)=(0,0). Thus every x of
norm four is 2u with N(u)=1. The inherited unit group +-phi^Z and total
positivity give exactly

    x=2phi^(2j), j in Z.                              (8)

This fixed shell contains only the unit orbit of 2. Introducing other
prime-ideal content does not fill its gaps while preserving norm four.
The norm-four inert-prime factor cannot silently become a collection of
new fixed-mass momenta. Changing mass, carrier or normalization is outside
this statement.

## 5. Phase, position and arithmetic closure must remain typed

The following limitations are inherited from #1605, not newly discovered:

    omega'(k)=sin(k)/Ehat(k),
    [i partial_k, phat]=i cos(k),
    dEhat/dk=cos(k) omega'(k).

Thus equality of a drift with p/E does not make phat canonical for the
unchanged lattice position, nor make Ehat the logarithmic generator of
U_mu. The distinct W theorem nominates H=i Log_alpha(W). It does not
identify that interacting energy with the free additive sine energy.
The separate onsite-contact counterexample and its full-space account
already delimit that identification in #1605 and the v106 contact rows.
This PR does not repeat those experiments or claim their ownership.

The proposed blanket statement "every observable is in Q(sqrt(5))" also
fails literally for these existing models. At k=pi/6, equation (2) gives
Ehat=sqrt(17)/2. If sqrt(17)=a+b sqrt(5) with a,b rational, comparing
coefficients gives ab=0 and either a^2=17 or b^2=17/5; neither is a
rational square. This is an exact band-value counterexample.

Even the registered constant kappa=sqrt(16phi+7)/20 of
CONTACT-W-BOUND-PAIR-RESPONSE need not lie in that field:

    N(16phi+7)=7^2+7*16-16^2=-95.

A square in F has norm equal to the square of a rational number, hence
nonnegative. Therefore sqrt(16phi+7), and kappa, are outside F. This
changes no spectral theorem and computes no new bound-pair spectrum.

Algebraic numbers can still be represented exactly by integer polynomial
data with a specified root. Finite configuration amplitudes of W already
have the registered localized cyclotomic module Z[zeta_20,1/5], not just
Z[phi]. Coefficient-ring closure is different from all eigenvalue or
expectation-value fields, and arbitrary Hilbert states are a further
completion. No failure of integer arithmetic follows from these distinctions.

## 6. Decision on the proposed sequence

The direct chart is REJECTED at exactly (1), with (5) its surviving finite
rung intersection and (7) the stricter Galois-carrier intersection.
The following stages of the proposed SAME-chart chain are NOT REACHED:

- transferring the arithmetic elastic-admission test to W's incoming modes;
- matching a W bound-pair spectrum to the norm/rest classification.

No W scattering probability was calculated by this note. Its existing
bound-state and contact theorems remain intact. A matching finite list of
shell values would not by itself prove an intertwiner preserving update,
composition, energy, position, source, clocks and records. Those are part
of a complete model, not consequences of a scalar dispersion identity.

An alternative multichart or nonlinear reading is not excluded, but must
be separately typed and tested. It may not be presented as a passing
instance of the frozen question (1). No new such reading is proposed here.
As external context only, nonlinear reference-frame symmetries of discrete
walks are studied by Apadula, Bisio, D'Ariano and Perinotti,
"Symmetries of the Dirac quantum walk and emergence of the de Sitter
group", arXiv:1806.03940. No theorem from that paper is imported.

The previously constructed contact remains a declared reversible machine,
not a bound-state model or a finished universe. Its old source and exact
local evidence are preserved byte-for-byte. In particular, its unbounded
2beta stream, at-most-one encounter and unselected reflection law remain
explicit limitations. No registered T, D, H or O owner changes status.
