# A minimal common-ready archive and its conditional phase location

NON-CANONICAL. Reservation #1416. Conditional candidate-T. This proof
answers the synchronization distinction test at a specified mathematical
scope. It adds an explicit integer archive/write rule; it does not find
that rule inside unchanged native U or derive physical coherence.

## 1. Native state and the exact lost distinction

The complete registered native state is (n,x) in N0 x X, X=F5^6,
x=(p1,p4,p1p,p4p,q,r). For n>=0 let theta_n=popcount(n) mod 2,
z(x)=sum(x) mod 5 and

    d_n(x)=g_(z(x)+2theta_n mod 5)(x),
    U(n,x)=(n+1,d_n(x)), E_0=id, E_(n+1)=d_n E_n.

All following coordinate operations are in F5. Native involutions are

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r),
    (g_0,...,g_4)=(a,b,c,d,e).

Their sheet maps under selection are

    tau_0=(0,4,0,4,4), tau_1=(2,1,1,3,1).            (1)

Each initial sheet X_s={x:z(x)=s} has 3125 heads, and each restricted
selected step is an affine bijection onto its target sheet. Actual first
controls are 011; the three-step restrictions are bijections from all
five initial sheets onto X_1. E3 therefore has 3125 fibers, with five
heads per fiber and exactly one from each initial phase s. The registered
first collision is

    x=(4,1,0,0,0,0), x'=(2,1,1,2,1,0),
    E1 x=E1 x'=(1,4,0,0,0,0).                       (2)

At any fixed later clock, merged current states remain identical forever.
There is no additional archive coordinate in (n,x) to retain which head
occurred. A pointed full orbit containing its original head retains that
head as an input by definition; this is different from a material register
written by U. The canonical decoder may read that orbit, but its existence
does not supply such a register or a physical phase effect.

## 2. A global dirty-state permutation from one common ready

Define the native phase calendar on five initial values:

    h_0(s)=s, h_(n+1)(s)=tau_(theta_n)(h_n(s)),
    i_n(s)=h_n(s)+2theta_n mod 5.                     (3)

The first values are h_1(s)=0 for s=0,2 and 4 otherwise;
h_2(s)=2 for s=0,2 and 1 otherwise. For n>=3,

    h_n(s)=4-3theta_(n-1), independently of s.         (4)

The last identity follows from first synchronization h_3=1 and (1) on
sheets 1,4. It is the existing synchronization formula, not a newly
selected calendar.

Add an archive m in F5, starting in the SAME ready value zero for every
head. The extended carrier is A=X x F5. Define

    P0(x,m)=(g_(m+z(x)) x,m+z(x)),                   (5)
    Pn(x,m)=(g_(i_n(m)) x,m), n>=1.                  (6)

The first map is the shear B(x,m)=(x,m+z(x)) followed by the
archive-controlled native involution C(x,mu)=(g_mu x,mu). B has inverse
B^-1(x,mu)=(x,mu-z(x)); C is an involution. Consequently

    P0^-1(y,mu)=(g_mu y,mu-z(g_mu y)).                (7)

Every tail Pn is an involution since its index depends on the unchanged
archive and n, and each g is an involution. Equations (7) and Pn^-1=Pn
hold on ALL dirty archive states, not only the initialized submanifold.
The calendar is a function of the existing integer counter; no external
sequence is supplied during the run.

For a ready input, induction gives

    P_(n-1)...P0(x,0)=(E_n x,z(x)), n>=1.             (8)

At the first step mu=z(x), and theta_0=0, so the checkpoint update is
the literal d_0. If (8) holds at n, its checkpoint phase is h_n(z(x));
the selected index in (6) equals the native index in d_n, proving the
next step. Thus every origin head follows its exact native checkpoint
trajectory, and its initially blank archive is filled during P0.

For a compact inverse of a whole dirty prefix, put

    Q_n(s)=g_(i_(n-1)(s)) ... g_(i_0(s)), i_0(s)=s.

Then for n>=1,

    (x,m0) -> (Q_n(mu)x,mu), mu=m0+z(x),
    x=Q_n(mu)^-1 y, m0=mu-z(x).                      (9)

Each Q_n(s) is a permutation, so (9) also proves full dirty-prefix
bijectivity. For the clean family, reverse the finite Q_n(z(x)) word
to recover every original head. No accumulating log is needed for this
one fixed-origin trajectory; independently writable new inputs would be
a different contract, and erasing/resetting the archive is not supplied.

The shear, added archive and archive-controlled selection are EXPLICIT
new comparison operations. The original generators act on six coordinates,
not on this seventh one. Their native compilation, physical storage,
coupling and preparation are not derived. The construction improves on a
preloaded tag by writing it from common zero, while still admitting this
additional writer rather than concealing it in a loader.

## 3. The attained five-state bound and unavoidable off-ready change

At n=3, five original heads must have the same native checkpoint and
clock. Exact full-head preservation requires five distinct auxiliary
outputs there. Hence any fixed-clock initialized completion preserving
all 15625 heads through E3 needs an archive alphabet of size at least
five. Construction (8) attains it, and thereafter retains full distinction
for all n. This is an inherited full-head lower bound with a new explicit
common-ready/permutation realization. A one-step initialized injection can
use three states because d_0 has maximum fiber three; that does not meet
the all-head three-step requirement. QDD-only recovery has a different,
weaker three-state target.

A finite bijective extension cannot project to d_n(x) on EVERY dirty
state whenever d_n has a collision. For a fiber d_n^-1(y) of size k>1
and an archive alphabet M, all k|M| inputs over that fiber would have
output checkpoint y, whose output slice has only |M| states. Injectivity
is impossible. Thus the native agreement of (8) must be restricted to
the specified initialized reachable family; arbitrary dirty inputs follow
the explicit completion, which can have a different checkpoint projection.
Full dirty inverses are still essential and have been provided.

## 4. Hilbert representation and what it actually preserves

Introduce H_X=ell2(X) and H_M=ell2(F5) solely as mathematical
representations. Per-tick permutations Pn determine unitary maps between
the time slices H_A. They add neither physical preparations nor occurrence
probabilities. If an arbitrary coherent source is SUPPLIED, the ready
isometry induced by (8) is

    T_n: sum_x a_x|x>|0> -> sum_x a_x|E_nx>|z(x)>.    (10)

E_n is injective on each initial sheet. Therefore

    <E_nx,z(x)|E_nx',z(x')>=delta_(x,x'),
    T_n^* T_n=I                                      (11)

for every n>=1, preserving every cross-inner-product, not just individual
basis norms. At n>=3, x -> (E_nx,z(x)) is a bijection X -> X_n x F5;
the ready source Hilbert space identifies with the entire reachable joint
space. This is genuine mathematical retention of all supplied coherences.
It does not say the actual integer system can prepare each vector in H_X.

For n>=1, let Pi_s project onto the initial phase sheet, and define

    K_(n,s)|x>=|E_nx> if z(x)=s, and zero otherwise.

After discarding the archive the reduced operator is exactly

    Phi_n(rho)=sum_s K_(n,s) rho K_(n,s)^*,
    sum_s K_(n,s)^* K_(n,s)=I.                       (12)

For this completion, terms Pi_s rho Pi_t with s!=t disappear. Coherence
within one sheet survives its bijective transport; phase erasure is not
erasure of all coherence between distinct retained E3 labels. The archive
choice in (5)-(6) accounts for this particular whole block decomposition.
A different dilation can have different off-fiber overlaps, so (12) is
not asserted as the unique possible reduced channel. At n=0 the archive
is still common zero and the reduced map is identity, preserving the
initial cross-phase coherences.

## 5. The hard j/j^-1 test at a merger

Take the two heads in (2), with initial phases s=0 and s'=2. They have
the same checkpoint y_n for every n>=1. With j=zeta5, supply the two
normalized comparison vectors

    psi_+=(|x>+j|x'>)/sqrt(2),
    psi_-=(|x>+j^-1|x'>)/sqrt(2).                     (13)

Equation (10) gives

    T_n psi_+ = |y_n> (|0>+j|2>)/sqrt(2),
    T_n psi_- = |y_n> (|0>+j^-1|2>)/sqrt(2).          (14)

The whole density operators differ; their squared Hilbert-Schmidt
distance is 2 sin^2(2pi/5)=(phi+2)/2>0. Their checkpoint reductions are
both |y_n><y_n|. Hence every checkpoint-only observable has the same
mean in these two preparations, while suitable archive/joint observables
can distinguish them. The loss of LOCAL access is not a loss of the
global supplied coherent state.

This local invisibility at a merger is general for a configuration-faithful
isometric dilation. If T|x>=|F(x)>|e_x> and F(x)=F(x') with x!=x',
isometry requires <e_x,e_x'>=0. In a superposition of those two inputs,
tracing the auxiliary factor removes the cross term. Thus preserving
complete distinction does not automatically turn merger amplitudes into
locally accessible interference. It instead forces a record to distinguish
the merging alternatives in this basis-faithful class.

For contrast, two different heads on the same initial phase sheet have
the same archive label but distinct outputs. Their two relative phases
remain as off-diagonal entries of the reduced checkpoint density. This
proves that the completion does not prohibit all native-label coherence
readings. Its physical preparation and coupling still need their own
derivation. None of these density calculations is a new Born occurrence
postulate or a physical work law.

The free map |x>->|E_nx> with coherent summation over mergers is a
different operator. On a five-head fiber, coefficients all equal have
source norm squared five and image norm squared twenty-five; a pair of
opposite coefficients maps to zero. It is not the reduced quantum channel
(12) and not a unitary on the full source. The canonical Galois code has
a special isometric restriction with supplied correlations; this remains
a distinct code class and is not refuted by the present argument.

## 6. The forward clock is a separate unitary obstruction

On the complete forward carrier N0 x A, the extension

    V(n,a)=(n+1,Pn a)

is injective but not onto: it has no output with clock zero. Its basis lift
has Vhat^* Vhat=I and Vhat Vhat^*=I-Pi_(clock=0). Bijective time-slice
propagators do not make this clock-including lift a unitary group.

One optional mathematical completion adjoins the two-sided clock Z and
sets Pn=I for n<0. Then

    V_Z(n,a)=(n+1,Pn a),
    V_Z^-1(n,a)=(n-1,P_(n-1)^-1 a)                    (15)

is a permutation and has a unitary basis lift. This is a new clock domain
and a chosen negative-time rule. It does not extend the Thue-Morse parity
to all Z2, select a physical time unit, or derive a local continuous
Hamiltonian. Alternatively, indexed unitary slice evolution can use n as
an external mathematical index, with its clock interpretation declared.

## 7. What the test decides about the proposed physical bridge

For unchanged current-state U on all origin heads, an initial phase
distinguishing the five E3 antecedents is genuinely unrecoverable. A
head-retaining abstract orbit supplies different input, and a restricted
preparation sheet avoids those mergers but changes the admitted domain.

An exact minimal integer archive can preserve full distinction, including
any separately supplied coherent amplitudes. It does not generate
off-diagonal coherence from a basis state or a diagonal classical ensemble
in this fixed configuration basis:
permutations merely move basis states and diagonal density operators.
The same integer law is consistent with a physical domain containing only
such configurations, or with a separately admitted coherent domain. Thus
distinction preservation alone does not force that latter domain. A
different, non-basis-preserving code or Fourier reading can expose other
coherences; its preparations and observable dictionary must be specified
independently and are outside this basis argument.

For the merger test (13), the phase survives in the added archive, where
the field/charge checkpoint alone cannot read it. To reproduce #1413's
phase-sensitive current/work one must independently establish the physical
phase-bearing preparation, its observable coupling to charge/field, and
actual generator or controlled limit. Transporting a chosen work matrix
by T_n would tautologically preserve its means; it would not derive a
Hamiltonian, energy exchange or measured current from these permutations.

The result therefore resolves this hard test, not the entire first route:
original current U loses the distinction; a five-state COMMON-ready
completion retains it through explicit added gates; conditional coherence
is global and can be locally hidden. No native writer has been found in
unchanged U, and no impossibility theorem for all integer models follows.
Continuum limits of difference laws remain separate mathematical routes
and do not require a physical Hilbert interpretation. No such limit,
unbounded U(1) carrier, photon phase or Born rule is proved here.

## 8. Source and disposition

Authoritative inputs at main 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc:
canon/CANON.md, KERNEL-Z6-SYNCHRONIZATION and
U-NATIVE-CHART-AND-QDD-READBACK;
probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md (five-state preloaded full-head
recovery, explicitly conditional);
probes/P-U-GALOIS-FIBER-CODE-1/PROOF.md (special correlated coherent code).
The endpoint j/j^-1 work witness is in draft #1415, source
7b219ed86f3c61afdd811527d24d855678770948. It is not a physical input
selected by this archive construction.

The present common-ready gate formula, dirty inverse and phase-location
comparison are original Apache-2.0. Finite auditing checks the frozen
fixtures; general all-time and Hilbert statements rest on these proofs.
Internal static review is not independent public peer acceptance. No Canon,
Registry, Frontier, GATES, old notes, probes, tools or workflows change.
