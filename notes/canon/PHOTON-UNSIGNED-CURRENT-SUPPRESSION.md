# Photon unsigned-current suppression

Status: NON-CANONICAL / CONDITIONAL MODEL / RESULT-EXPOSED.

This note proves uniform signed and unsigned marked-current bounds for one
explicit finite-product model. It consumes an exact finite classification
at proposed computation status C, subject to required exact-head reproduction,
without promoting that classification or selecting
the model as the complete TWIST-J action. Neither photon successor root nor
GATE-L4-L6-PHOTON-MASSLESS-PHASE is closed. Public Canon v72 remains unchanged.

## 1. Inputs and the conditional layer gate

The finite input is
[P-PHOTON-Z5-STAR-QUADRATURE-1](../../probes/P-PHOTON-Z5-STAR-QUADRATURE-1/PREREG.md),
whose immutable preregistration/verifier pin is
`66bcc0714cac5789292954bea300e398689ffd0a`. Its
[result](../../probes/P-PHOTON-Z5-STAR-QUADRATURE-1/RESULT.md) and
[exact output](../../probes/P-PHOTON-Z5-STAR-QUADRATURE-1/EXPECTED.txt)
classify only 462 finite L4 factor polynomials. The accepted verifier SHA256
is `87fcc66932750cd325c8ab4f7c28e6832780e7ebd8b3bd19352b255391ce2044`;
the scientific output SHA256 is
`8f883ec07afeb4db2c1d366e8d94d29305568643e07a97847aeef93ffd2c9015`.

The probability application is separately named here:

```text
NOTE-GATE-L4-L6-PHOTON-UNSIGNED-CURRENT-IDENTITY
from: L4 finite oriented cubical incidence and the specified factor Q
to:   L6 normalized finite current law nu_K, on its full power-set sigma-algebra
map:  normalized positive character expansion, followed by j=partial n/5
equality: exact finite partition, mixed-Haar and cylinder identities below
scope: only the selected free-box model of section2
```

This is a notes-only conditional gate name, not a registered or Canon-adopted
gate, not a new formal probe, and not an enlargement of the pinned L4
preregistration. Its mathematical identities are proved below; physical
selection and occurrence are not. There is no claimed pointwise bijection
or positive joint coupling between primal angles and character currents.

The model is the same provisional one used in the
[Born-current observable note](PHOTON-BORN-CURRENT-OBSERVABLE-LEMMA.md).
The required infrared target remains the separate
[defect-screening criterion](PHOTON-DEFECT-SCREENING-CRITERION.md).
No external massless-phase theorem is imported here.

## 2. Selected finite model and exact character law

Let K be a finite free rectangular cubical box in Z^4, with one positive
orientation per edge and face. Write E,P for its edges and plaquettes,
d for the integer cellular coboundary and partial for its transpose.
All edge variables, including boundary edges, are summed. There is no
periodic identification or fixed boundary-angle condition.

Put A_e in (2pi/5)Z modulo2pi and choose the full-support primal weight

```text
W(theta)=2+2cos(theta),
W on Z5 = (4,phi^2,phi^-2,phi^-2,phi^2), phi=(1+sqrt(5))/2.
```

Gauge transformations A->A+d lambda leave the plaquette factors unchanged.
Removing the constant two per face gives Q(theta)=1+cos(theta). With
normalized five-point Haar averages the partition function is

```text
Z_K = E_(A in Z5^E) product_(p in P) Q((dA)_p)
    = sum_(n in {-1,0,1}^P, partial n=0 mod5) 2^(-|supp n|).
```

Proof: Q(theta)=1+(exp(i theta)+exp(-i theta))/2. Expand the finite
product and average each edge character. Orthogonality enforces
partial n=0 modulo5, with the displayed positive coefficient. In particular
Z_K>=1. Define nu_K as this sum divided by Z_K and j=partial n/5.
An edge belongs to at most six plaquettes, so j_e in{-1,0,1}; also
partial j=0. At degree less than five, j_e=0 identically.

These definitions fix the complete finite law used here, not a law forced
by Canon. The ternary n is a character-expansion face field, not the
principal lift of the primal plaquette angle.

## 3. Closed-background sector identity and a sharp local bound

For an integer edge field j let

```text
Q_(K,j)=sum_(n ternary, partial n=5j) 2^(-|supp n|).
```

Use the auxiliary continuous extension Q(theta)=1+cos(theta) on U(1).
Its product, normalized against U(1)^E Haar measure, defines mu_U with
partition function Q_(K,0). Character orthogonality gives exactly

```text
Q_(K,j)/Q_(K,0) = E_mu_U exp(-i5<j,A>) in[0,1].
```

The denominator sums every integer-closed background, not just n=0.
Nonnegativity of the Fourier coefficient follows from the character sum.
This identity does not identify the continuous and Z5 phases. The
continuous Q has zeros; no logarithm or division by Q at a zero is used.

Condition on every angle but one edge. Absorb orientation signs into
the offsets using cosine's evenness. Its factor is

```text
q(theta)=product_(h=1)^r (1+cos(theta+b_h))
        =2^-r |P(exp(i theta))|^2, r<=6,
P(z)=product_h(1+exp(i b_h)z)=sum_(a=0)^r p_a z^a.
```

Pad p_a=0 outside0..r and use unscaled Laurent coefficients of |P|^2:

```text
C0=sum_(a=0)^6 |p_a|^2>0,
c5=p5 conjugate(p0)+p6 conjugate(p1).
```

The pairs(0,5) and(1,6) are disjoint. Thus

```text
2|c5| <= |p0|^2+|p5|^2+|p1|^2+|p6|^2 <= C0.
```

For r=5 only the first pair remains; for r<5 c5=0. The conditional
fifth-harmonic expectation therefore has modulus at most1/2. The common
factor2^-r cancels. This polynomial proof retains continuous zeros.

The constant is locally sharp even with Z5 offsets. Choose phases
{0,0,1,2,3,4} times2pi/5. Then P=(1+z)(1+z^5), C0=4,c5=2.
The six opposite parallel edges of an interior edge's incident plaquettes
are distinct and can realize all six offsets independently. All angles
can lie in Z5, where every factor Q is strictly positive. Local sharpness
does not mean a full-volume sector probability simultaneously saturates.

## 4. Plaquette-independent sets and eight-color geometry

Call S plaquette-independent when no plaquette contains two edges of S.
Conditioned integrations over S then factorize. Taking S inside supp j
and applying section3 gives

```text
Q_(K,j)/Q_(K,0) <= 2^(-|S|).
```

Color the positive edge (x,i) by

```text
(i, sum_(k!=i)x_k modulo2).
```

There are eight colors. Different directions receive different colors,
and the two parallel edges of a plaquette have opposite transverse
parity. Every color class is plaquette-independent. Consequently, for
L=|supp j|,

```text
Q_(K,j)/Q_(K,0) <= 2^(-ceil(L/8)).
```

If a requested sector is empty, the same bound holds with numerator zero.
A sector bound alone does not control the number of sectors.

## 5. Signed marked currents with every outside sector summed

For independent S and u in{-1,0,1}^S, define N_S(u) by the positive
character sum with partial n_e=5u_e on S and only partial n_e=0 modulo5
outside S. Then N_S(u)>=0 and sum_u N_S(u)=Z_K.

Integrate A_e in U(1) on S with insertion exp(-i5u_e A_e); average A_e
in Z5 outside S. Finite character expansion proves this mixed integral
equals N_S(u). Fix the complementary Z5 environment. Plaquettes not
meeting S contribute H>=0; the remaining factors separate into one q_e
per selected edge. Triangle inequality and the local harmonic bound give,
when every u_e is+1 or-1,

```text
0 <= N_S(u) <= 2^(-|S|) N_S(0),
P_nu_K(j_S=u) <= 2^(-|S|) P_nu_K(j_S=0) <= 2^(-|S|).
```

No outside current is fixed: all unmarked sectors, including nonzero ones,
are summed. For arbitrary marked edges T and prescribed nonzero signs,
select an independent subset of size ceil(|T|/8) and discard the other
constraints to obtain

```text
P_nu_K(j_e=u_e for every e in T) <= 2^(-ceil(|T|/8)).
```

Summing the2^|S| sign choices cancels this exponential factor. An unsigned
exponential bound therefore needs another argument, given next.

## 6. Exact discrete star constant and independent witness

For the mixed integral the offsets belong to Z5. With
zeta=exp(2pi i/5), the class of star polynomials is

```text
P_k(z)=product_(b=0)^4(1+zeta^b z)^k_b,
k_b>=0, sum_b k_b<=6.
F=c5+conjugate(c5),
D=(1/5)sum_(t=0)^4 |P_k(zeta^t)|^2=C0+F,
theta(k)=|F|/D.
```

The equality is exact quadrature: only Laurent modes0,+5,-5 survive.
Every summand in D is positive, because -1 is not a fifth root of unity.
F is real but can be negative. In particular |F| means the modulus of
the signed alias sum, not2|c5|. The actual Q factors multiply C0,F,D by
the same2^(-r), leaving the ratio unchanged.

The finite probe enumerates all C(11,5)=462 phase-count vectors without
symmetry removal. Its exact classified maximum is

```text
theta_*=(82+50sqrt(5))/361,
1/2 < theta_* < 1.
```

There are five maximizing count vectors:
(0,2,0,2,2),(0,2,2,0,2),(2,0,2,0,2),(2,0,2,2,0),(2,2,0,2,0).
HALF failed at exactly these five vectors; STRICT_UNIT passed. These are
the original simultaneous thresholds, not a post-run replacement.

An independent written check of the witness(2,0,2,0,2) is short. Write
s=sqrt(5) and square

```text
(1+z)(1+zeta^2 z)(1+zeta^4 z)
 =1+(-zeta-zeta^3)z+(-1-zeta^3)z^2+zeta z^3.
```

The resulting coefficients p0,...,p6 are

```text
1;
-2zeta-2zeta^3;
-4-zeta-zeta^2-4zeta^3;
-2+4zeta-2zeta^2;
3+3zeta+4zeta^3;
2+2zeta^2+2zeta^3;
zeta^2.
```

Coefficient reversal p_(6-a)=zeta^2 conjugate(p_a) pairs the norms.
Using zeta+zeta^4=(s-1)/2 and zeta^2+zeta^3=-(s+1)/2 gives

```text
|p0|^2=|p6|^2=1,
|p1|^2=|p5|^2=6-2s,
|p2|^2=|p4|^2=(35-15s)/2,
|p3|^2=30-10s.
```

For example p2=3zeta+3zeta^2+4zeta^4 has norm square
34+9(zeta+zeta^4)+24(zeta^2+zeta^3), and p3=-2(1-zeta)^2.
It follows that

```text
C0=79-29s,
c5=-4(zeta+zeta^4)=2-2s,
F=4-4s,
D=83-33s,
|F|/D=(82+50s)/361.
```

D>0 follows from83^2>5*33^2. At this negative-F witness HALF would
require C0+3F>=0, but91-41s<0 since8281<8405. Also
1-theta_*=(279-50s)/361>0. The witness alone refutes HALF; the global
upper bound and complete extremizer set depend on the finite C input,
not on this one calculation. This note does not promote that input to T.

## 7. Unsigned cylinder theorem

For independent S, sum N_S(u) over u in{+1,-1}^S. At fixed complementary
Z5 angles the selected integrals contribute F_e, whereas summing all
three values0,+1,-1 contributes D_e. Absorb the factors2^(-r_e) into H,
writing H_tilde>=0. The following identities are exact:

```text
sum_(u in{+1,-1}^S)N_S(u)
  = E_(Z5 outside S) H_tilde product_(e in S) F_e,
Z_K
  = E_(Z5 outside S) H_tilde product_(e in S) D_e.
```

The first integrand can have either sign, but its integral is nonnegative
by the original character sum. The classified pointwise inequality
|F_e|<=theta_* D_e, followed by triangle inequality, proves

```text
P_nu_K(j_e!=0 for every e in S) <= theta_*^|S|.          (UNSIGNED)
```

For arbitrary finite markers T, choose an independent subset of exactly
ceil(|T|/8) edges using section4. Event inclusion then gives

```text
P_nu_K(j_e!=0 for every e in T)
  <= theta_*^ceil(|T|/8).                              (COLORED)
```

These are actual unsigned event bounds under the complete selected law,
not ratios to a globally defect-free sector. No signs have been frozen
and no outside current sectors have been discarded. Their new content
is volume-uniform suppression of multiple unsigned markers. A sharp
pointwise star constant need not be a sharp global probability constant.

Conditioning on complementary angles in the proof is not conditioning on
complementary currents. Arbitrary outside-current insertions may destroy
the nonnegative angle weight H. Neither conditional Bernoulli domination
nor an arbitrary-current conditional version of(UNSIGNED) is asserted.

## 8. Limit transfer and the remaining infrared gap

For increasing boxes, extend n by zero outside each box. The infinite
face alphabet is finite on every coordinate; diagonal subsequences of
the finite-dimensional distributions therefore exist. For any fixed
finite edge set, the current j=partial n/5 depends on only finitely many
faces and agrees with its full-lattice definition once those faces are
inside the box. Cylinder probabilities converge along such subsequences.
The uniform bounds above pass to every resulting local limit. They also
survive convex averages and translated or signed-coordinate averaged
limits formed from the same laws. No uniqueness, translation invariance
of an arbitrary limit, or Gibbs-state identification is claimed.

The estimate controls marker count, not pair separation. In particular,
for two widely separated fixed markers its upper bound need not decrease
with their distance. It does not establish connected-covariance decay,
weighted second-moment summability, or the strict spectral screening gap
in PHOTON-DEFECT-SCREENING-CRITERION. The full score defect rho=dX and its
branch-correction and cross-covariance terms remain uncontrolled here.

Even the crude seven-choices-per-step loop count with the eight-color
exponent would require7 theta_*^(1/8)<1. That sufficient condition fails
already because theta_*>1/2. This is failure of that crude estimate, not
a divergence theorem or a no-go theorem for refined geometric methods.

The local finite classification, the conditional measure identity, and
the infrared claim must remain separate. This note establishes the first
application bounds using the classified finite input. It supplies no
massless phase, continuum propagator, polarization, physical photon,
apparatus reading, or Canon adoption, and leaves both photon roots open.
