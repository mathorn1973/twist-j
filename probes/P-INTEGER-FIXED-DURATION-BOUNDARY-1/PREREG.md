# Fixed-total-lapse boundary problem

Status: PROSPECTIVE
Scope: NON-CANONICAL NEW_DECLARED L1, scalar normal form, force a=0
Owner: A. M. Thorn, session integer-fixed-duration-boundary-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1668

## 1. Question and custody

The predecessor #1666 proves the exact scalar action and classifies zero
energy when every lapse is varied independently. This probe distinguishes
fixing their sum before variation, classifies the complete stationary phase
equivalence, and determines the residual endpoint/energy ambiguity. The
identifier's word duration denotes a declared total lapse, not an admitted
physical clock. No gravitational interaction or physical preparation is
introduced. Negative lapses and the uniform spatial mode are admitted.

Public Canon v103 is ACTIVE. Authority, final base, predecessor commits,
normative byte hashes and implementation independence are in SOURCE.md.
Publish and read back six files before any scientific execution, import or
fixture evaluation: this contract, PROOF.md, SOURCE.md, verify.py,
breaker.py, FROZEN.sha256. Before that only analytical work, source review,
AST parsing and byte checks are allowed. No post-pin scientific repair.

## 2. Exact definitions and theorem domains

Use six configuration coordinates x=(h_0,...,h_4,chi), with no mean-zero
restriction. On five cyclic vertices, spatial edges r->r+1 have weight
29/324 and r->r+2 have weight65/324, one of each per r. With head-minus-tail
incidence Bsp, let Lsp=Bsp^T W Bsp, ell=(1,-1,0,0,0), g=1/324, and

    V=[[Lsp,-g ell],[-g ell^T,1]], C=I-V/2, D=I-C^2,
    K=[[0,I],[-D,0]], M0=[[C,I],[-D,C]],
    R(s)=exp(sK), M(s)=M0 R(s)=[[U(s),B(s)],[-DB(s),U(s)]],
    v=(1,1,1,1,1,0), H(q,p)=(p.p+q^T Dq)/2.

The predecessor proves D>=0 with ker D=span(v), C,D symmetric commuting,
and M0,R symplectic and H preserving. Here both programs independently
rebuild the matrices from these definitions. For det B(s)!=0 define

    E(s)=B(s)^-1, A(s)=E(s)U(s),
    F_s(q,Q)=(q^T A(s)q+Q^T A(s)Q)/2-q^T E(s)Q.

The action is S=sum_(b=1)^T F_(s_b)(x_(b-1),x_b)+Ebdry, with fixed
configuration endpoints and Ebdry=(x0^T Vx0+xT^T VxT)/4. Interior momenta
are pL_n=A(s_n)x_n-E(s_n)x_(n-1) and
pR_n=E(s_(n+1))x_(n+1)-A(s_(n+1))x_n. Field stationarity is pL=pR.
The exact bond parameter derivative is -H of its endpoint phase.

Universal results concern real phase states, arbitrary real lapses, T>=3,
and the union of regular configuration representations. Formal identities
are over Q and finite arithmetic fixtures are rational. No finite nonzero
exponential is evaluated numerically. Complex energy shells are excluded.

## 3. Two variational problems and complete phase equivalence

Problem A varies all lapses independently: field stationarity plus lapse
stationarity gives H=0, hence static uniform real histories. Adding the
explicit term Efixed sum s_b instead gives H=Efixed.

Problem B restricts sum s_b=L before variation. Its lapse variations have
sum delta s_b=0. Their equations require only equality of bond energies,
already implied by matched momenta. They impose no fixed numerical energy.
Adding Efixed sum s_b is then constant and cannot impose H=Efixed. A later
chosen energy shell is a separate classification condition. With regular
fixed endpoint data and L, the resulting energy may be determined by those
data; fixed L alone does not select it.

Write a_n=sum_(b<=n)s_b, a0=0. Every stationary phase history is

    z_n=M0^n R(a_n)z0.

Declare finite phase equivalence, with lapse arrays part of the history:

    s'_b=s_b+theta_b-theta_(b-1),
    z'_n=R(theta_n)z_n, theta0=thetaT=0.

This is equivalence inherited from the global phase action, requiring
regular start and end configuration representations when those are used.
It does NOT require a connecting path to stay inside one regular chart
component. For the narrower continuous regular-path relation, retain also
the ordered interval components of R minus {s:det B(s)=0} for all bonds;
these labels together with (z0,L) are complete on each nonempty fixed-sum
domain. No finite total count of those chart sectors is asserted.
For the declared finite phase equivalence the complete invariant is
(z0,L). The dressed phases R(-a_n)z_n=M0^n z0
are invariant. Every real L has a regular representative (choose two
parameters avoiding the discrete zero set of det B). Thus the phase
classification is not silently restricted to the zero-centered chart.

## 4. Complete boundary and energy classification

Put M_T(L)=M0^T R(L)=[[U_T,B_T],[-DB_T,U_T]], where T denotes integer
power. With fixed configuration endpoints q,Q, solve

    B_T p0=d, d=Q-U_T q.

There is no orbit if d is not in im B_T. Otherwise let pstar be the
unique minimum-Euclidean-norm solution, k=dim ker B_T. Each orbit is
uniquely represented by p0=pstar+w, w in ker B_T. On the additional
chosen energy shell H=Efixed,

    ||w||^2=rho^2=2Efixed-q^T Dq-||pstar||^2.

For k=0 there is one orbit exactly when rho^2=0, otherwise none. For
k>0: rho^2<0 gives none, rho^2=0 gives one, rho^2>0 gives the sphere
S^(k-1) of radius rho. In particular k=1 gives two orbits at positive
radius. These are real classifications, not rational point counts.

On det B_T!=0 the reduced bond action is

    Ftot_L(q,Q)=(q^T B_T^-1 U_T q+Q^T B_T^-1 U_T Q)/2
                         -q^T B_T^-1 Q.

It equals the stationary sum of F_s, and partial_L Ftot_L=-H(q,p0).
The full S includes the unchanged Ebdry. The parameter derivative holds
at fixed q,Q. Neither this formula nor the quadratic form is asserted
positive definite.

For T=3,L=0,

    U3=C^3-3CD, B3=4C^2-I=(I-V)(3I-V).

B3 is invertible with inertia (five positive, one negative). The spatial
eigenvalues are 0 and (235 +/- 18 sqrt(5))/324, each nonzero value twice.
Thus I-Lsp>0. The Schur complement of I-Lsp in I-V is
-g^2 ell^T(I-Lsp)^-1 ell<0; also 3I-V>0. These prove the assertion.

## 5. Exact two-orbit caustic

At T=3,L=-3, q=Q=0, Efixed=5/2, the complete phase classification has
exactly two orbits, p0=+v and p0=-v. On a nonuniform C-eigenmode write
c=cos(phi), omega=sin(phi), 0<phi<pi/2. Then

    B_3(-3)=sin(3(phi-sin(phi)))/sin(phi)>0,

while the uniform eigenvalue is 3+L=0. Consequently ker B_3(-3)=span(v).
The three lapse arrays (-3,0,0),(0,-3,0),(0,0,-3) are regular: B(0)=I,
the uniform B(-3)=-2, and nonuniform
B(-3)=sin(phi-3sin(phi))/sin(phi)<0. This is not the principal chart.

For each sign and each of the three arrays, define

    p_n=sign*v, q_n=(n+a_n)*sign*v, n=0,...,3.

These are exact rational stationary histories with the same configuration
endpoints, total lapse and energy. The three distributions for one sign
are phase equivalent. Opposite signs are not, because z0 is invariant.
The finite audit uses only the exact uniform shear, not an evaluated
nonuniform exponential. The full two-orbit completeness rests on the proof.

## 6. Frozen finite exact audit

Use degree N=4, including coefficients0..4. Both programs independently
derive every matrix, coefficient, gradient and recorded scalar. One uses
matrix-power rational series and direct derivatives, the other independent
recurrences and a distinct action/derivative implementation. No imports or
source reads of companion or predecessor scientific programs.

1. Check five normative files against SOURCE. Build Lsp from edges; compare
   its circulant diag188, nearest -29, next -65, divided by324. Check Dv=0,
   C^2+D=I, symmetry, M0^T G M0=G for G=diag(D,I), [M0,K]=0. Compute five
   positive LDL pivots of I-Lsp and six positive pivots of 3I-V, and the
   strictly negative Schur scalar above. Compute U3,B3 from actual M0^3,
   compare displayed polynomials, invert B3 and check both inverse products.
   LDL is unpivoted in declared coordinate order (h0,...,h4, then chi
   where present), with unit lower-triangular factor and diagonal pivots.
2. Derive R_j=K^j/j!, M_j=M0 R_j, U_j,B_j, then formal E=B^-1,A=EU
   through degree4. Verify (j+1)R_(j+1)=K R_j, j=0..3, and all 15 ordered
   pairs i+j<=4 in R_i R_j=binomial(i+j,i)R_(i+j).
3. Six seeds r=1,...,6 in ascending order. Initial phase coordinates are

       z0[j]=(((r+1)(j+2)+j^2) mod19-9)/(r+2), j=0,...,11.

   Form z_n=M0^n z0, n=0..3. Require positive H=energy, equal at all four
   phases. At the three zero-lapse bonds compute actual F0, momenta and
   partial_s F0 from A'_0=-I,E'_0=-C. Check matching interior momenta,
   both endpoint momenta, and all three parameter derivatives equal -H.
   Directions delta s are (1,-1,0),(0,1,-1),(1,-2,1), in that order.
   Compute their actual parameter work and require zero (18 regular cases;
   CONSTRAINED_VARIATIONS counts these, excluding the caustic checks).
   The free direction (1,0,0) has actual work -H!=0 (six cases).
   Add Efixed=H+1 to every bond parameter derivative: the three constrained
   works remain zero, although H-Efixed=-1. This is an explicit distinction.
4. For each seed recover p0=B3^-1(Q-U3 q) and compare with the input.
   Let E3=B3^-1,A3=E3 U3. Evaluate Ftot0 from the displayed formula and
   compare with the actual sum of three F0 (excluding Ebdry on both sides).
   Differentiate the composite blocks at zero, U3'=-D B3,B3'=U3,
   E3'=-E3 B3' E3,A3'=E3' U3+E3 U3'. Evaluate the actual derivative of
   the quadratic boundary expression at fixed q,Q and require -H.
   Recover its incoming and outgoing momenta and compare z0,z3. The
   unique momentum makes Efixed=H+1 incompatible with the same endpoints.
5. For each seed set theta=(0,(r-3)/(r+1),(2r-5)/(r+2),0),
   eta=(0,(r+2)/(r+3),-(r+1)/(r+4),0), alpha_b=theta_b-theta_(b-1).
   Compute the actual transformed phase series
   Z_n(epsilon)=R(epsilon theta_n)z_n, n=0..3. Require unchanged endpoints,
   zero total alpha, coefficientwise bond transfer
   M0 R(epsilon alpha_b) Z_(b-1)=Z_b, dressed phase
   R(-epsilon theta_n)Z_n=z_n, constant H(Z_n), and composition
   R(epsilon eta_n)Z_n=R(epsilon(theta_n+eta_n))z_n through degree4.
   Substitute the transformed q-series and s_b=epsilon alpha_b into the
   actual generating matrices A(s),E(s), compute all incoming/outgoing
   momentum series and require the transformed p-series. Require the
   actual sum of quadratic bond action series constant and equal to its
   zero-lapse value. Counts: 24 phase series, 18 bond series and six action
   series, each with five coefficients. No predicted zero substituted for
   any of these actual series operations.
6. For sign=(-1,+1), and distinguished -3 bond k=0,1,2, ascending,
   construct all six uniform caustic histories from Section5. For each
   bond use exact restriction F_s=||Q-q||^2/[2(1+s)], its field gradients
   and its fixed-q,Q parameter derivative. Check endpoint-zero fields,
   matching momenta, H=5/2, total lapse -3, action zero, and all three
   constrained works zero. Check phase-gauge equivalence of each k=1,2
   history to k=0 using theta=a_new-a_old and the exact uniform shear.
   Opposite signs have distinct initial phases, so the observed orbit
   count is two (the proof supplies completeness). A transformation with
   theta3=1 changes total lapse by1 and final q by sign*v and is excluded.

## 7. Eight controls, payload and outcomes

Use the six regular seeds and the caustic cases already frozen above;
no added fixtures after the pin. Controls must actually observe:

NC01: positive regular H contradicts inferring H=0 from constrained works.
NC02: adding Efixed sum s at fixed sum leaves stationarity with H-Efixed=-1.
NC03: omit the phase change under the first seed's changed lapses; at least
      one degree-one bond-transfer residual is nonzero.
NC04: use the wrong positive sign in dressing; at least one first-seed
      degree-one dressed residual is nonzero.
NC05: collapse the two caustic signs to one orbit; their initial p differ.
NC06: impose Efixed=H+1 at regular fixed endpoints; unique recovered p has
      the original H, so the energy constraint residual is -1.
NC07: allow thetaT=1 as endpoint-fixed; total lapse and final q change.
NC08: reverse the sign of the boundary parameter derivative; actual -H
      differs from the false +H for every positive-energy regular seed.

Completed scientific failure emits a declared F_* and RESULT=FAIL, exit0.
F_AUTHORITY: normative bytes; F_GEOMETRY: matrices, inertia certificates or
inverse; F_SERIES: coefficient recurrences/composition; F_VARIATION: bond
momenta, constrained/free lapse work or added constant; F_BOUNDARY: recovery,
action or derivative; F_GAUGE: actual transformed series; F_CAUSTIC: frozen
uniform histories, equivalence or endpoint violation; F_CONTROL: missed
deliberate defect; F_COUNTS: counts; F_BYTES: breaker failure/unequal bytes.
Unexpected runtime failure uses POLICY's abandoned-pin route. No frozen
file is repaired, and no completed failure is relabelled abandoned.

Canonical payload: ASCII, LF after each record, Fraction.__str__, comma
separated fractions, row-major matrices, phase q then p. Records in order:

    P|<five LDL pivots of I-Lsp>|<six pivots of 3I-V>|<Schur scalar>
    B|<flatten U3>|<flatten B3>|<flatten inverse B3>
    R|j|<flatten R_j>                    j=0..4

For each regular seed r ascending:

    Z|r|n|<twelve phase coordinates>     n=0..3
    H|r|energy
    W|r|<three actual constrained works>|<free work>|<three added-term works>
    A|r|<sum F0>|<Ftot0>|<actual boundary parameter derivative>
    G|r|n|j|<twelve transformed phase coefficients> n=0..3 then j=0..4
    S|r|<five actual transformed sum-of-bond-F coefficients, excluding Ebdry>

For each caustic sign then distinguished bond in Section6 order:

    C|sign|k|<phases n=0..3 flattened>|<energy>|<action>|<three constrained works>

Finally N|NC01|DETECTED through NC08 ascending. PAYLOAD_SHA256 is the hash
of these concatenated records, without normalization. The certificate is:

    CERTIFICATE=P-INTEGER-FIXED-DURATION-BOUNDARY-1
    AUTHORITY_FILES=5
    SERIES_ORDER=4
    COMPOSITION_PAIRS=15
    REGULAR_BOUNDARY_CASES=6
    CONSTRAINED_VARIATIONS=18
    FREE_LAPSE_WITNESSES=6
    GAUGE_PHASE_SERIES=24
    GAUGE_BOND_SERIES=18
    GAUGE_ACTION_SERIES=6
    CAUSTIC_HISTORIES=6
    CAUSTIC_ORBITS=2
    CAUSTIC_ENERGY=5/2
    PAYLOAD_SHA256=<computed lowercase digest>
    NEGATIVE_CONTROLS=8
    CERTIFICATE_RESULT=PASS

Primary invokes the frozen breaker with the same interpreter and -I,
timeout540 seconds. Require exit0, empty stderr and raw identical
certificate bytes; append BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS,
each LF. Enclosing run limit600 seconds. Neither program reads companion
source or EXPECTED.txt. The primary only launches that fixed subprocess.

## 8. Publication and limits

FROZEN.sha256 lists the other five prospective files. After public readback
and first execution add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md, README.md.
Required x86_64 and aarch64 checks use unchanged sources and output.

Proof supplies universal classification; finite exact cases audit its
implementation. The caustic witness uses negative lapses and the uniform
mode and makes no claim for a positive-lapse or mean-zero restriction.
The fixed-sum variational problem changes an explicitly named boundary
condition. It does not refute the predecessor's free-lapse H=0 result.
No new nonlinear bulk interaction, physical clock, metric selection,
native-U realization, continuum limit or cross-layer lift is supplied.
