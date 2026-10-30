# Prime obstructions to exact two-body channels in Z[phi]

Author: A. M. Thorn
Date: 2026-10-30
Candidate: C-PRIME-TWO-BODY-CHANNELS-N
Owner: ChatGPT-prime-two-body-20261030, issue #1836
Status: NON-CANONICAL / L1 / analytical candidate-T.
Finite audits are supplementary candidate-C, not public theorem promotion.

## 0. Premises, attribution and boundaries

Let F=Q(sqrt(5)), O=Z[phi], phi=(1+sqrt(5))/2. A prime denotes Galois
conjugation, not differentiation. Write x=a+b phi as the coefficient pair
(a,b), so

    x'=(a+b)-b phi,
    Tr(x)=2a+b,    N(x)=a^2+ab-b^2.

Define O_+ by BOTH real embeddings being strictly positive. Equivalently,
Tr(x)>0 and N(x)>0. All incoming and outgoing states here belong to O_+.
The selected comparison reads E=Tr(x)/2 and P=b sqrt(5)/2, hence
E^2-P^2=N(x). Addition of elements is the DECLARED conserved two-body total;
the individual norms are the DECLARED squared-mass labels. These are a
kinematic comparison contract, not a derivation of physical particles,
original U, a contact interaction, a source, a clock or SI calibration.
Zero and massless states are outside this carrier.

ARITHMETIC-RAPIDITY-DECOMPOSITION, SPLIT-PRIME-RAPIDITY-CLASS and
SPLIT-PRIME-RAPIDITY-INDEPENDENCE in Public Canon v106 are inherited
arithmetic context. The unit group is +-phi^Z. The usual two-body triangle
polynomial below is the standard Kallen polynomial, not a new kinematic
invariant (PDG, Review of Particle Physics, 2025, Kinematics, 49.4.2).
All proofs specific to this arithmetic admission problem are supplied here;
no claim of priority over the mathematical literature is made.

Important sheet guard: multiplication by phi has norm -1 and does NOT
preserve O_+. The positive norm-one unit boosts in this carrier are
phi^(2Z). We do not replace signed Galois coordinates by absolute values
mid-proof. An arithmetic class modulo log(phi) is not automatically a
physically admitted rest-frame operation on this positive sheet.

No result here computes the CONTACT-W dispersion, its bound state, its
curvature 19, or any interaction rate. Admission is not occurrence.

## 1. Complete exact channel criterion [candidate-T]

Fix z=A+B phi in O_+, let T=N(z)>0, and let r,s be positive integers.
We seek ALL ordered pairs (x,y) in O_+^2 satisfying

    x+y=z,    N(x)=r,    N(y)=s.                         (1)

Put

    D=T+r-s,
    Delta=D^2-4Tr
         =T^2+r^2+s^2-2Tr-2Ts-2rs.                    (2)

Then (1) has a solution if and only if:

(a) 0<D<2T;
(b) Delta=5 b^2 for an integer b>=0, and b=D modulo 2;
(c) for at least one sign epsilon, the algebraic integer

    w_epsilon=(D+epsilon b sqrt(5))/2                   (3)

is divisible by z' in O.

The complete output list is

    x_epsilon=w_epsilon/z',    y_epsilon=z-x_epsilon,   (4)

retaining exactly the signs satisfying (c) and counting b=0 only once.
There are at most two ordered solutions. These are necessary AND sufficient
conditions, not merely obstructions.

Proof. For a solution put w=xz'. Then N(w)=rT and
Tr(w)=xz'+x'z=T+r-s=D, by expansion of N(z-x). Every element of O has
Tr(w)^2-4N(w)=5 b^2, with b its phi coefficient, and the trace and b have
the same parity. Also w and T-w=yz' have positive embeddings, so (a)
holds. This proves necessity, including divisibility.

Conversely, (2)-(3) give N(w)=rT>0 and Tr(w)=D>0, so both embeddings of w
are positive. Also N(T-w)=sT>0 and Tr(T-w)=2T-D>0, so T-w is positive.
Division by the positive element z' gives positive x,y satisfying (1).
Condition (c) places x in O; y=z-x is then in O. The quadratic equation
w^2-Dw+rT=0 proves completeness. QED.

For direct integer implementation, a sign can be represented by signed b.
The output coefficients are

    a=[A D+(2B-A)b]/(2T),
    c=[B D+(2A+B)b]/(2T).                              (5)

Condition (c) says precisely that both displayed numerators are divisible
by 2T. Thus the criterion is fully decidable using integers, without
logarithms, decimal tolerances, or prime factorization.

Every admitted solution has 1<=r,s<T: each embedding of x and y is strictly
between zero and the corresponding embedding of z. The usual real
threshold is T>=(sqrt(r)+sqrt(s))^2. Condition (a) together with Delta>=0
selects that threshold branch, rather than the pseudothreshold.
The additional square-class and divisibility conditions are what the
chosen integer carrier adds. Nonnegative Delta alone is not sufficient.

## 2. Complete elastic response in the field [candidate-T]

Given x,y in O_+, put z=x+y and retain the same ordered norms r=N(x),s=N(y).
The two possible field-level solutions are

    (x,y),
    (R_z(x),R_z(y)),    R_z(u)=(z/z')u'.                (6)

They coincide exactly when x/z is rational, equivalently the two incoming
rapidities agree. Otherwise they are distinct labelled outputs.

Proof. One root of the quadratic in section 1 is w=xz'; the other is its
conjugate x'z. Divide both by z'. The map R_z fixes z, preserves N, maps
positive embeddings to positive embeddings, and satisfies R_z^2=identity.
All statements follow directly from conjugation. QED.

Thus the second output is admitted by O exactly when

    z' divides z x' in O.                              (7)

Checking y separately is unnecessary because R_z(x)+R_z(y)=z in O.
For eta(u)=log(sigma+(u)/sigma-(u))/2 on O_+,

    eta(R_z(x))=2 eta(z)-eta(x).                        (8)

Equation (8) is the exact reflected rapidity IF this output is chosen;
conservation alone does not choose it instead of the first output.
No continuous impulse or external force has been postulated here.

## 3. Exact prime-ideal obstruction [candidate-T]

For a fractional element q, its denominator ideal is

    den(q)={a in O : aq in O}.

Unique factorization of fractional ideals applied to (6) gives

    den(R_z(x))=(z') / ((z')+(zx')).                    (9)

Here + is ideal sum, the ideal gcd; the quotient is an integral ideal.
For every prime ideal P its exponent is exactly

    max(0, v_P(z')-v_P(z)-v_P(x')).                    (10)

At an inert or ramified rational prime the prime ideal is fixed by
conjugation, so v_P(z')=v_P(z) and (10) vanishes. Consequently all
rational primes in a denominator are SPLIT primes. In F these are exactly
p=1 or 4 modulo 5. Neither 5 nor an inert prime can be such an obstruction.
A least positive integer denominator always divides T=N(z), since
R_z(x)=z^2 x'/T.

Now suppose the incoming pair is primitive in the IDEAL sense:

    (x)+(y)=O.                                       (11)

Then (z')+(x')=O, so (7) is equivalent to z' dividing z. The ideals (z)
and (z') have the same positive absolute ideal norm, so divisibility is
equality. Thus

    R_z(x) in O  iff  (z)=(z')                        (12)
                   iff z/z'=phi^(2k) for some k in Z
                   iff eta(z)=k log(phi).

The middle equivalence uses the inherited unit group and positivity; no
canonical orientation of split primes is selected. The last equivalence
is algebraic evaluation in the positive real embedding.

Let e_P,e_P' be the exponents of the two primes over each split p in (z).
Under (11), the least rational clearing denominator of the second output is

    d_z=product_(p split) p^|e_P-e_P'|.                (13)

Indeed at each split pair, (9) has the positive part of the exponent
difference, on only one of its two ideals. A rational p contributes one
valuation to both ideals, so exactly |e_P-e_P'| copies are necessary and
sufficient. Inert and ramified factors cancel. No prime-factor count of
N(z) alone replaces the two oriented exponents.

This makes the role of prime content precise: it determines exact lattice
admission of the reflected recoil. It does not determine its occurrence.

The rapidity condition in (12) is NOT the assertion that every such z can
be brought to a rational rest element by the positive-sheet boosts
phi^(2Z). For example z=2+phi=phi sqrt(5) has eta(z)=log(phi) and N(z)=5;
its reflection is integral, while a real positive rest scalar sqrt(5)
is not a two-positive-embedding element of this same field carrier.
The signed and absolute-value readings must remain separate.

## 4. An all-c family predicted before the audit [candidate-T]

Take the primitive pair

    x=1,   y=c phi^2,   c a positive integer.

Then

    z=(c+1)+c phi,             T=c^2+3c+1,
    R_z(1)=[(2c^2+2c+1)+(3c^2+2c)phi]/T.              (14)

The greatest common divisor of T and its two numerators is gcd(T,5).
To see this, reduce the numerators modulo T to -4c-1 and -7c-3;
7(4c+1)-4(7c+3)=-5. If 5 divides T then c=1 mod 5, and both numerators
are divisible by 5. Moreover writing c=1+5k gives
T=5(1+5k+5k^2), so T has exactly one factor 5. Hence

    least integer denominator = T/gcd(T,5).            (15)

This is one exactly when c=1. For every c>=2 the nontrivial labelled
elastic reflection leaves O. The original outgoing pair remains allowed.

The first fixtures are

    c=1:  z=2+phi,   T=5,   R_z(1)=phi^2;
    c=2:  z=3+2phi,  T=11,  R_z(1)=(13+16phi)/11;
    c=3:  z=4+3phi,  T=19,  R_z(1)=(25+33phi)/19.

The last two rational norms of R_z(1) are still one. The obstruction is
integrality, not failed energy/momentum conservation in the field. A
localization admitting the relevant denominator would repair this
particular obstruction but is a DIFFERENT carrier, not a consequence of
native U or of the original contract. The 19 here is not equated with
an unrelated contact-dispersion coefficient.

## 5. Divisibility is indispensable, even after the square test [candidate-T]

Set

    z=(3+2phi)(4+3phi)=18+23phi,    T=209=11*19,
    r=1, s=181,    D=29, Delta=5.

The field-level channel satisfies the real threshold and the exact
square-class condition. Its only first outgoing states are

    (13+16phi)/11,    (25+33phi)/19.                    (16)

Neither lies in O. There is therefore NO channel (1,181) on the specified
integer carrier for this specified total z, despite admissibility in F.
This is an exact arithmetic selection rule obtained before any observed
scattering data, not a fitted spectral-prime label.

There is a stronger control. The different total z0=15-phi also has norm
209, but the same ordered norms ARE allowed there:

    z0=1+(14-phi),    N(14-phi)=181.                    (17)

Thus total invariant norm and outgoing norms alone do not decide integer
channel admission. They give exactly the same T,r,s,Delta in (16)-(17).
The oriented prime-ideal content of the total is additional data.
This is a discrete-carrier comparison, NOT a claim of Lorentz-invariant
physical prohibition under arbitrary real boosts. The two totals can be
related by a field norm-one multiplier, which need not preserve O.

## 6. What arithmetic does not select [candidate-T]

On the COMPLETE declared carrier O_+^2 define

    I(x,y)=(x,y),
    C(x,y)=(R_z(x),R_z(y)) if R_z(x) is integral,
           (x,y) otherwise, where z=x+y.               (18)

Both maps are total involutions and preserve the ordered norms and total.
For an admitted reflected state the same total and reverse reflection
show admission of its inverse, proving involutivity of C.
They are distinct even for unequal norm labels: take x=phi^2=1+phi and
y=4-phi^2=3-phi. Then z=4, the norms are 1 and 5, and C conjugates both
states nontrivially whereas I does nothing.

Consequently the stated arithmetic laws do not uniquely determine a
collision update. This is a precise nonuniqueness in THIS declared class,
not a no-go over an unspecified complete physical apparatus class.
Neither (18) supplies a spatial contact, a duration, a binding potential,
a bound-state spectrum, a probability or a native-U realization.
The existence of admissible outputs is necessary, not sufficient, for a
physical transition governed by additional dynamics.

## 7. Complete finite enumeration and exact audit methods

Every x=a+b phi in O_+ has a>0: in embedding coordinates,
a=(phi sigma-(x)-phi' sigma+(x))/sqrt(5), with both coefficients positive.
If 0<x<z in both embeddings, the same positive linear functional gives
0<a<A. Also N(x)>0 puts -a/phi<b<a phi, hence |b|<2a.
Thus the finite box

    a=1,...,A-1,  b=-2a+1,...,2a-1                     (19)

contains every possible outgoing x; testing future positivity of x and
z-x then gives the complete list. Comparing that list with (2)-(5)
tests both positive channels and all absences, not merely some examples.

The separate check uses doubled trace t=2a+b. For a fixed total (t_z,B),
all outgoing states satisfy 1<=t<t_z and |b|<t, with t=b mod 2. It tests
(t^2-5b^2)>0 and the corresponding remainder condition. Solving the two
linear equations for the second formulation gives

    t=[t_z D+5B u]/(2T),
    b=[B D+t_z u]/(2T),    Delta=5u^2.                 (20)

Require both to be integers of equal parity. This implementation does
not import the coefficient implementation. Both are same-session work,
not independent-agent confirmation.

For the ideal-primitivity audit one may use norm-Euclidean division in O.
Round the two rational coefficients of x/y to nearest integers. The
remainder factor delta has coefficients of absolute value at most 1/2,
so |N(delta)|<=3/4<1. The nonzero integer norms therefore decrease, giving
a terminating gcd. For split-prime exponents the verifier independently
lifts the two roots of t^2-t-1 modulo p by exact Hensel lifting, and tests
A+B root modulo p^k. No floating point is used.

The universal claims are the written proofs above, not the finite audit.
Public promotion, a formal probe and independent review are separate.
