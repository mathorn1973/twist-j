# One golden cell: addition, frame information and the Dirac address map

Author: A. M. Thorn
Date: 2026-10-30
Candidate: C-GOLDEN-CELL-COMPOSITION-N
Owner: ChatGPT-golden-composition-20261030; issue #1842
Status: NON-CANONICAL / L1 / analytical candidate-T.
No public claim status, physical admission or dynamics is created here.

## 0. The exact question and its type

Keep the same arithmetic carrier O_+ used in the two-body note #1837:
O=Z[phi], phi^2=phi+1, with both real embeddings strictly positive.
Set epsilon=phi^2=1+phi and h=log(phi). For x=a+b phi write

    x'=(a+b)-b phi,
    tau(x)=2a+b,    N(x)=a^2+ab-b^2,
    E(x)=tau(x)/2,  P(x)=b sqrt(5)/2,
    eta(x)=log(x/x')/2.

O_+ is equivalently tau>0 and N>0. Its norm is signed before this
restriction. The existing unit group and arithmetic-rapidity statements
are inherited public inputs, not new claims of this note. Multiplication
by epsilon is an arithmetic positive norm-one boost; it is NOT asserted
to be a symmetry of the fixed Dirac walk.

The target address is the unchanged mass-two sine shell

    Ehat(k)=sqrt(4+sin(k)^2),  phat(k)=sin(k),
    cos(omega(k))=cos(k)/sqrt(5).

For a reduced r=a+b phi, the proposed state assignment is

    H(r)=(tau(r)/sqrt(N(r)), b sqrt(5)/sqrt(N(r))).       (1)

It has Ehat^2-phat^2=4. The principal momentum branch, when used, is
k in (-pi/2,pi/2] with sin(k)=phat. Other Fourier folds are explicitly
allowed in the negative theorem below. The sign of the step eigenphase
is a further mode label, not determined by H.

We distinguish: a raw arithmetic sum; the total of two constituents;
a single fixed-mass walker; and a normalized address. Requiring a
multiparticle total to remain on one single-particle mass shell is not
an ordinary physical conservation law. No new contact, species, scattering
coefficient, force or third kinematics is introduced.

## 1. The fundamental rapidity region IS closed under addition [candidate-T]

Choose the half-open region

    D={x in O_+ : -h < eta(x) <= h}.

Since tanh(h)=1/sqrt(5) and P/E=b sqrt(5)/tau,

    D={a+b phi : a+3b>0, a-2b>=0}.                     (2)

These inequalities already imply future positivity: putting L=a+3b>0
and R=a-2b>=0 gives tau=L+R>0 and 5b=L-R, hence
N=(tau^2-5b^2)/4>0. Conversely the same inequalities are precisely
-tau<5b<=tau on the positive sheet, proving (2).

Both inequalities are additive. Therefore

    D+D subset D.                                    (3)

This is an all-input proof, not an inference from 650 or any other finite
number of representatives. It corrects the statement that arithmetic
addition necessarily leaves the rapidity cell. What is not closed under
addition is the fixed mass-two hyperbola, or the normalized single-walker
address interpreted with ordinary vector addition.

For example 2+2phi^2=4+2phi lies ON the upper boundary of D: eta=h,
N=20, E=5, P=sqrt(5). It is not a single mass-two walker, but it is a
perfectly valid arithmetic total inside the rapidity region. One of its
constituents, 2phi^2, was outside that region before reduction.

The original sine band has both endpoints. A half-open fundamental
region chooses one arithmetic orbit representative; it does NOT identify
the walk's two physical edge modes by a proved dynamical symmetry.
The edge is massive (Ehat^2-phat^2=4), not a null light-cone vector.

## 2. Exact reduction and faithful coordinates [candidate-T]

For every x in O_+ there is a unique n in Z and r in D such that

    x=epsilon^n r.                                   (4)

Existence and uniqueness follow from eta(epsilon^n r)=2nh+eta(r)
and the disjoint half-open intervals ((2n-1)h,(2n+1)h]. This is a
standard fundamental-domain argument, not a new unit-group theorem.
It has a logarithm-free implementation:

    epsilon(a,b)    =(a+b,a+2b),
    epsilon^-1(a,b) =(2a-b,b-a).

Start at x with n=0. While a-2b<0, apply epsilon^-1 and increase n.
While a+3b<=0, apply epsilon and decrease n. The first loop, once used,
cannot cross the lower endpoint; the second cannot cross the upper one.
The rapidity argument proves termination without a heuristic cutoff.
The two integer matrices are mutual inverses and have determinant one.

Write enc(x)=(n(x),r(x)) and dec(n,r)=epsilon^n r. They are inverse
bijections: this is the original O_+ in new coordinates, not a physical
extension of the state space. Conjugation gives enc(x')=(-n,r') except
at the upper seam r=c(2+phi), where enc(x')=(-n-1,r).

For enc(x)=(n,r), enc(y)=(m,s), set

    v=r+epsilon^(m-n)s,
    enc(v)=(c,t).

Then the exact transported addition is

    (n,r) boxplus (m,s)=(n+c,t).                      (5)

It is commutative and associative because decoding turns it into the
original addition. No truncation of output states is allowed. If n=m,
then (3) gives c=0 and the result is simply (n,r+s).

The output index is between the two input indices. Indeed
(x+y)/(x'+y') is the weighted average of x/x' and y/y', with strictly
positive weights x'/(x'+y') and y'/(x'+y'). Applying log/2 proves
min(eta(x),eta(y))<=eta(x+y)<=max(eta(x),eta(y)). The index in the
ordered half-open strip partition has the same between property.

A common frame change epsilon^j multiplies x,y and x+y together.
Independent reductions of the two inputs generally change their relative
motion. Thus (5) needs the relative integer m-n. It does not justify a
physical boost of W or create an endogenous clock register.

## 3. Why deleting the frame is not a quotient of addition [candidate-T]

In the unit-orbit quotient [1]=[epsilon]. But

    N(1+1)=4,     N(1+epsilon)=N(2+phi)=5.             (6)

Unit multiplication preserves norm, so those totals cannot belong to the
same orbit. Hence [x+y] is not a well-defined function of [x],[y].

There is a stronger exact theorem. Let A be ANY abelian group, and let
f:O_+ -> A obey

    f(x+y)=f(x)+f(y),    f(epsilon x)=f(x).             (7)

Then f is identically zero. No continuity, boundedness or real-valued
assumption is needed. In particular A may be the momentum circle.

Proof. Every t in O is a difference u-v of two future-positive elements:
choose a sufficiently large positive rational integer v so that t+v has
positive embeddings. Define f_tilde(t)=f(u)-f(v). If u-v=u1-v1, then
u+v1=u1+v and additivity makes the definition independent of the choice.
This is an additive extension to O. Unit invariance extends as well, so
f_tilde((epsilon-1)t)=0 for every t. But epsilon-1=phi is a unit of O,
with inverse phi-1. Its image is all O, proving f_tilde=0. QED.

Therefore a nontrivial additive momentum cannot factor through independent
unit reduction alone, even modulo 2pi. This does not exclude a covariant
map retaining the frame, pair-level maps, or different input equivalences.

The amount of lost relative information is unbounded. The pairs
(1,epsilon^d), d>=0, have the same two reduced representatives and the
same individual norms one, yet

    N(1+epsilon^d)=2+phi^(2d)+phi^(-2d)=2+L_(2d).      (8)

These values are strictly increasing for d>=0. Thus a fixed finite label,
together with just those reduced representatives and individual norms,
cannot recover all pair totals. An unbounded relative integer suffices
in (5). No thermodynamic or native-memory cost is inferred.

## 4. What mass normalization erases, and the exact repair [candidate-T]

For r in D, (1) has phat in (-1,1], Ehat>0 and mass square four.
The inequalities follow exactly from tau>0, -tau<5b<=tau and
N=(tau^2-5b^2)/4. Positive integer scaling gives

    H(c r)=H(r),    N(c r)=c^2 N(r).                   (9)

So a spectral address forgets radial information. It cannot be additive
as a nonzero real two-vector: H(2r)=H(r) differs from 2H(r).
More generally a uniformly bounded real additive map on O_+ is zero,
by applying it to n x. This narrow theorem is not applied to total
energy on varying-particle-number sectors, whose range is not uniformly
bounded.

For x,y in ONE common reduced frame, z=x+y is still in D and

    sqrt(N(z)) H(z)
      =sqrt(N(x)) H(x)+sqrt(N(y)) H(y).                (10)

This is exact: each weighted vector is (tau,b sqrt(5)), which is
additive. The normalization factors are not probabilities and must not
be replaced by equal weights. A simple example is

    x=1, y=2+phi, z=3+phi,
    H(x)=(2,0), H(y)=(sqrt(5),1),
    H(z)=(7/sqrt(11),sqrt(5)/sqrt(11)).                (11)

Equation (10) retains all arithmetic scale when the norms are retained.
For the full unrestricted input, retain (n,N,H(r)). Reconstruction is

    b=phat sqrt(N)/sqrt(5),
    a=(Ehat sqrt(N)-b)/2,
    x=epsilon^n(a+b phi).                             (12)

On the image these are integers and (12) is an exact inverse. It is not a
claim that arbitrary real (N,Ehat,phat) is in the image. The raw
four-momentum is sqrt(N) H/2, and the total is generally not on the same
fixed mass shell as its constituents.

The usual bilinear composition identity remains

    N(x+y)=N(x)+N(y)+Tr(xy'),
    Tr(xy')=2ac+ad+bc-2bd,
    Tr(xy')^2-4N(x)N(y)=5(bc-ad)^2,                   (13)

for x=(a,b), y=(c,d). We cite it as inherited supporting algebra,
not another interaction or a new prime spectral law.

## 5. A branch-independent obstruction to the proposed W total [candidate-T]

For each r in D, allow ANY selection of k(r) modulo 2pi satisfying

    sin k(r)=b sqrt(5)/sqrt(N(r)).                    (14)

There is no function K:D->R/(2pi Z) such that

    K(x+y)=k(x)+k(y)                                 (15)

for every pair x,y in D. This statement is stronger than merely noting
that the principal arcsine is nonlinear. It permits arbitrary fold
choices, and K need not itself be the same chart as k.

Proof by two decompositions. All entries below belong to D:

    1+(4+phi)=2+(3+phi)=5+phi.                        (16)

The rest inputs 1,2 have k=0 or pi. Hence the first possible total has
sin^2(K)=5/19 for EVERY fold choice, while the second has sin^2(K)=5/11.
Those rational numbers differ. No common K exists. QED.

The failure is not limited to rational rest states. There is an all-prime
control in the same D:

    (3+phi)+(4+phi)=(2+phi)+(5+phi)=7+2phi,            (17)
    individual norms: (11,19) and (5,29),
    common total norm: 59.

In the first pair the two momentum sine squares are 5/11 and5/19.
For arbitrary cosine signs of the Fourier folds, the total sine square
belongs to the set

    {(100+20sqrt(21))/209, (100-20sqrt(21))/209}.       (18)

In the second pair the first sine is one and its cosine zero. The total
sine square is exactly

    1-5/29=24/29,                                    (19)

regardless of folds. Neither irrational number in (18) is (19). Thus
(15) also fails on these prime-norm addresses. At the edge the free
one-particle step is well defined; no singular scattering-basis limit
is being taken. No numerical approximation or branch fit enters this
counterexample. An eigenphase-band sign cannot repair an already
incompatible translation charge.

This rejects EXACTLY total factorization (15) for chart (14), not every
possible configuration-level correspondence. It does not assert that
pairs with different individual norms ought to be physically identical.
Rather, it shows that their original additive total alone cannot carry
this nominated target momentum. The constituent data matter.

## 6. Correct target composition, and what remains open

The existing free two-walker step is a tensor product. With one-particle
modes (k1,lambda1),(k2,lambda2), its joint translation momentum and step
phase are

    K_total=k1+k2 mod2pi,     lambda_total=lambda1 lambda2. (20)

This does not turn the tensor pair into one walker of mass two. The
coordinate identities in sections1-4 do not supply an isometry, a
preparation map, a native source, or an intertwiner with this tensor law
and its contact W. Equality of a sine-shell interval is not equality of
these dynamics. The known folding and eigenphase distinction of #1605,
#1839 and #1841 remain unchanged.

A stronger future assignment must state whether it retains constituent
norms, relative frames, Fourier folds and eigenphase labels, and then
verify the actual evolution and joint translation. Changing the target
composition or selecting a new momentum reading is a new comparison,
not a repair of the counterexample in (15). The arithmetic coordinate
repair (5),(10),(12) is complete at its own scope, but W compatibility
is NOT PROVIDED here. No second species is introduced to hide that gap.

The reported independent numerical review of #1841 is not elevated to
verified external acceptance: the named BUILD-MALY-VESMIR-2, review and
positive-sheet correction files were not retrieved. Their chat account
is result-exposed motivation. The current note has one authoring session.

The compact-state no-capture result for an unchanged unitary is a general
spectral conservation fact. It alone does not prove that one specific
third-body or recording mechanism is uniquely necessary; changed drives,
preparations and enlarged closed systems need their own contracts. This
note does not reopen that separate question.

## 7. Scope and evidence

Elementary fundamental-domain, group-completion and tensor-product
arguments are not claimed as globally new mathematics. The result is a
precise audit of the proposed TWIST-J state interface. The exact finite
checks in PREREG.md audit but do not replace these proofs.

No Canon, registry, frontier, gate, original U, W, contact law, SI claim,
Born occurrence rule, physical particle identity, formal P-probe or public
T status changes. Any promotion needs independent review and its own fold.
