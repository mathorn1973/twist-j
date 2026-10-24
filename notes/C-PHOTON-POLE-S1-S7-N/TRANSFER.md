# Finite transfer support and bounded electric insertion

**Item:** C-PHOTON-POLE-S1-S7-N, finite S2 component.  
**Parent:** [#744](https://github.com/mathorn1973/twist-j/issues/744).  
**Author:** A. M. Thorn.  
**Date:** 21 September 2026.  
**Status:** PUBLIC; NON-CANONICAL; candidate-T, conditional finite L4 operator algebra. Written proof, not independently reviewed. No phase, continuum, photon or native-U theorem.  
**Basis:** Public Canon v91, `11b66d4755a697031157f0e10dc1898a7d5b6379`.

The prospective scope is recorded in
[#744, comment 5753406017](https://github.com/mathorn1973/twist-j/issues/744#issuecomment-5753406017).
This note proves the finite part of the proposed S2 construction. It does
not assert that any S3-S7 pole predicate holds. No change to the fixed
weight, local score, physical candidate t=1 or primary diagonal-volume
prescription is made.

## 1. Fixed objects and conventions

Fix an integer N>=2. The spatial vertex set is V_N=(Z/NZ)^3. Its positive
oriented links are E_N={(x,i):x in V_N, i=1,2,3}. Even when N=2, links with
different labels are distinct; opposite traversals are signed uses of a
labelled link, not an identification of two positive links.

Let A_N=F_5^{E_N} and use the counting inner product on H_N=C^{A_N}.
All sums over A_N are unnormalized. Put v=|V_N|=N^3 and e=|E_N|=3N^3.
The symbol e in a character label below instead denotes an edge field;
its role is stated whenever needed.

Write j=exp(2*pi*i/5), phi=(1+sqrt(5))/2 and kappa=tan(pi/5)>0. Freeze

    W(f)=2+j^f+j^(-f)=(4,phi^2,phi^(-2),phi^(-2),phi^2)_f,
    G(f)=(0,1,2+sqrt(5),-(2+sqrt(5)),-1)_f.

Equivalently WG=2 sin(2*pi*f/5)/kappa. The Fourier convention is

    hat u(r)=sum_(f=0)^4 u(f) j^(-rf).

With the principal representative r in {0,1,2,-2,-1}, direct character
orthogonality gives

    hat W=(10,5,0,0,5),
    hat (WG)=(0,-5i/kappa,0,0,5i/kappa),
    hat (-i*kappa*WG)=(0,-5,0,0,5).                 (1)

These are exact character identities. In particular W is strictly positive
as a point function but its convolution is not positive definite.

For a vertex function lambda let

    (d lambda)(x,i)=lambda(x+e_i)-lambda(x).

For an integer representative edge field r define

    (partial r)(x)=sum_i [r(x-e_i,i)-r(x,i)].        (2)

Then <r,d lambda>=<partial r,lambda>. The sign in (2) is incoming minus
outgoing; modulo-five vanishing does not depend on this orientation choice.

The gauge projector and product convolution are

    (P_g u)(a)=5^(-v) sum_lambda u(a+d lambda),
    (K u)(a')=sum_a prod_l W(a'_l-a_l) u(a).

P_g includes the constant gauge transformations in its average. Their
redundancy does not spoil the projector normalization.

Let h_N(a) be the product of W(d_s a) over all positively oriented spatial
plaquettes. It is gauge invariant and strictly positive. Define

    (M u)(a)=sqrt(h_N(a)) u(a),   L=K P_g,
    mathbbT=M L M.                                  (3)

M is invertible, commutes with P_g, and need not commute with K.

## 2. Exact support of the transfer

Use the orthonormal characters

    chi_r(a)=5^(-e/2) j^(sum_l r_l a_l), r in F_5^{E_N}.

Gauge averaging is the finite character sum

    P_g chi_r = 1_{partial r=0 mod 5} chi_r.

The convolution eigenvalue is prod_l hat W(r_l). Hence the complete positive
label set is

    S_N={r in {0,+1,-1}^{E_N}:partial r=0 mod 5},
    S=span{chi_r:r in S_N},
    L chi_r = ell(r) chi_r,
    ell(r)=10^(number of zero links) 5^(number of nonzero links)>0
            for r in S_N, and zero otherwise.        (4)

Thus L is positive semidefinite, commutes with P_g, and ran L=S. The rank
is exactly |S_N|; no closed expression or asymptotic for this count is
asserted.

By (3), for every u,

    <u,mathbbT u>=||L^(1/2) M u||^2>=0.

Since M is invertible, this proves the exact identities

    ker mathbbT=M^(-1) S^perp,
    ran mathbbT=M S.                                 (5)

The second identity can also be read directly from M L M: M maps the full
space onto itself, L maps it onto S, and the final M maps S onto M S.
The physical-support candidate is therefore **M S, not S itself**. This
is a congruence statement, not a unitary Fourier identification.

Every matrix entry of mathbbT is strictly positive. Explicitly,

    mathbbT(a',a)=sqrt(h_N(a')h_N(a)) 5^(-v)
                 sum_lambda prod_l W(a'_l-a_l-(d lambda)_l).   (6)

Consequently its largest eigenvalue Lambda_N is strictly positive and
simple, with a strictly positive eigenvector. The elementary
Perron-Frobenius theorem is used only for this finite matrix. Gauge
invariance of the kernel puts this eigenvector in ran P_g.

Normalize T=mathbbT/Lambda_N and let Pi be the orthogonal projection onto
H_+=ran T=M S. Then 0<T|_(H_+)<=I and

    H=-log(T|_(H_+)),   V(t)=exp(-itH)                 (7)

are well-defined finite-dimensional operators, with H self-adjoint and
nonnegative. Inverses and logarithms below always act on H_+. This is not
an assignment of finite energy to ker T and is not a claim that H is a
finite-range or native Hamiltonian. No uniform-in-N spectral gap follows.

## 3. Rectangular partition normalization

Consider the same plaquette weight on a periodic N^3 by m four-dimensional
lattice, m>=2, summing every spatial and temporal link variable once.
Taking the trace of a product of (6) identifies the first and last spatial
slice. Each spatial h_N occurs exactly once because its two square roots
come from adjacent transfer factors. Each temporal link lambda is summed
once. Each transfer factor also contains precisely 5^(-v).

Therefore the exact finite identity is

    Z_(N,m)=5^(vm) tr(mathbbT^m)
           =(5^v Lambda_N)^m tr(T^m).                (8)

Tracing on H_N, on ran P_g, or on H_+ gives the same answer for m>=1:
all omitted directions are killed by the transfer. Equation (8) concerns
the partition function before gauge-volume division, with the full link
sum convention above.

**Notation correction to the local S1-S7 draft:** its rectangular identity
used T_N where the unnormalized mathbbT_N was intended. When normalized
T_N is used, Lambda_N^m must remain. This corrects an unfrozen draft
notation, not a canonical result or a fired scientific threshold.

The primary S1 limit is still the diagonal periodic sequence m=N. Formula
(8) does not exchange this with m->infinity first at fixed N, nor prove
that their local states or infrared limits agree.

## 4. Temporal electric insertion and its support

Fix a positive link l. In (6) replace the single factor W at that link
by WG and divide by the SAME Lambda_N. Call the resulting operator D_l.
Changing a and a', and changing lambda to -lambda in the sum, shows

    D_l^*=-D_l.

Define the Hermitian scaled insertion S_l=-i*kappa*D_l. Let Q_l on S be
the diagonal operator

    Q_l chi_r=-r_l chi_r, r in S_N.

Equation (1) shows, with exactly the same gauge average,

    S_l=Lambda_N^(-1) M L^(1/2) Q_l L^(1/2) M.        (9)

There is no contribution on a forbidden +/-2 character: both W and WG
have zero coefficient there. The middle multiplier on an allowed link is
-1, 0 or +1; hence -I_S<=Q_l<=I_S. Taking the congruence in (9) gives

    -T<=S_l<=T,                                     (10)
    -(1/kappa)T <= -iD_l <= (1/kappa)T.

Furthermore (9) and (5) give

    D_l=Pi D_l Pi.                                  (11)

Indeed u in ker T satisfies L^(1/2)M u=0, so D_l u=0; skew-adjointness
gives the other side. Support is not repaired by throwing away an
inconvenient extra insertion component. It is a property of the fixed WG.

The proposed Hermitian electric operator is therefore

    E_l=-i T_+^(-1/2) D_l T_+^(-1/2),
    X_l=kappa E_l=T_+^(-1/2) S_l T_+^(-1/2).         (12)

Its definition requires no small-eigenvalue cutoff or added regulator.
Equation (10) already proves ||E_l||<=1/kappa, independently of N.

## 5. A common unitary identifies all electric insertions

There is a stronger exact statement. Define

    Ucal=Lambda_N^(-1/2) L^(1/2) M T_+^(-1/2)
          : H_+ -> S.                               (13)

It is not the native U and not the time evolution V(t). Direct multiplication
using (3) gives Ucal^* Ucal=I_(H_+). Both spaces have dimension rank L,
so Ucal is onto and Ucal Ucal^*=I_S. Equations (9)-(13) imply

    X_l=Ucal^* Q_l Ucal  for EVERY link l.             (14)

The SAME unitary applies to every link. Thus

    X_l^*=X_l,   X_l^3=X_l,   [X_l,X_b]=0             (15)

for any l,b. For a fixed l, zero flux and the two orientations of a
coordinate winding loop through l belong to S_N. They realize r_l=0,+1,-1.
Consequently

    spec(X_l)={-1,0,1},   ||E_l||=1/kappa.            (16)

The equality is sharp for every N>=2 and every positive link. The joint
spectrum is precisely the set of signed fields -r with r in S_N, not the
unconstrained product of three labels on each edge. This statement makes
no photon-number or photon-polarization claim.

The common unitary depends on the complete finite transfer. Equations
(14)-(16) do not prove locality of Ucal, of H, or a finite causal speed.
They do not prove that arbitrary finite quantum controls are available.

### 5.1 The transfer itself on the constrained ternary carrier

The same polar unitary also gives a concrete transfer on S:

    Ucal T Ucal^*=Lambda_N^(-1) L^(1/2) M^2 L^(1/2)|_S.       (20)

To check this, insert (13), cancel T_+^(-1/2) T T_+^(-1/2)=Pi,
and use Pi M L^(1/2)=M L^(1/2), since its range is M S. Thus no
inverse square root needs to be numerically formed to specify the operator
in this representation.

Let P_s be the positively oriented spatial plaquettes and let partial_s
be their boundary with the same incidence convention as (2). The exact
character expansion of h_N is

    h_N(a)=sum_(n in {0,+1,-1}^{P_s})
             2^(|P_s|-|supp n|) j^(<partial_s n,a>).

Consequently its character-basis matrix elements are the nonnegative integers

    b(r'-r)=sum_(n:partial_s n=r'-r mod 5)
                2^(|P_s|-|supp n|),

and (20), for r,r' in S_N, has entries

    Ttilde(r',r)=sqrt(ell(r')ell(r)) b(r'-r)/Lambda_N.        (21)

This is a finite, fully specified transfer on constrained three-value edge
labels. The source of b is the SAME spatial W, not a new Hamiltonian fitted
to a desired spectrum. The operator is strictly positive definite on S
because h_N>0 and L|_S>0; its individual matrix entries need not all be
strictly positive. Its logarithm is unitarily equivalent to (7).

Equation (21) does not assert that this finite matrix can be explicitly
stored at large N, or that its logarithm is local. No many-link diagonalization
or new numerical result is used in this corollary.

## 6. The exact Gauss condition remains only modulo five

Define the integer-spectrum operator

    (partial X)(x)=sum_i [X_(x-e_i,i)-X_(x,i)].

By (14) its joint eigenvalues are -partial r(x), with r in S_N. Therefore

    exp(2*pi*i*(partial X)(x)/5)=I_(H_+).             (17)

One must NOT strengthen (17) to partial X=0 over R.

An explicit witness is available on every N>=3. Let A=(0,0,0), B=(1,0,0).
Take five directed paths from A to B with step lists

    (x), (y,x,-y), (-y,x,y), (z,x,-z), (-z,x,z).

Their labelled edges are pairwise disjoint. Sum their oriented unit flows.
The resulting r has 13 nonzero links, each +/-1. At intermediate vertices
incoming and outgoing flows cancel. With convention (2),

    partial r(A)=-5,  partial r(B)=+5,
    partial r(x)=0 elsewhere.                       (18)

It belongs to S_N but is not real-divergence-free. By (14), the corresponding
nonzero state Ucal^*chi_r has nonzero real divergence for the X operators.
This is a boundary witness inside the selected finite model, not a theorem
that continuum photons are impossible. Any emergent real Gauss law needs a
separate infrared statement; the finite condition alone does not supply it.

## 7. Magnetic insertions and correlation boundaries

For an oriented spatial plaquette p, let B_p be multiplication by G(d_s a)_p
followed by compression Pi on both sides. It is Hermitian and

    ||B_p||<=max_f |G(f)|=2+sqrt(5).                 (19)

This bound is uniform in N; no sharpness after compression is asserted.
Magnetic multiplication generally does not preserve H_+ before compression.
Consequently products of separately compressed operators need not equal
the compression of a same-slice product. Coincident insertions and contact
terms must use the original prescribed transfer insertion, not an inferred
product rule. No equal-time canonical commutation relation is proved here.

For temporal insertions, (11) makes the separated-slice prescription
support-compatible. The factor -i in (12) retains the odd Euclidean electric
reflection convention; it cannot be removed while keeping the same
Hermitian/Minkowski comparison.

Uniform bounds on finite operators are useful input to later construction,
but do not alone give convergence of states, insertions, generators or
joint energy-momentum measures. The selected diagonal-volume limit, its
reconstruction, the dimension-two scaling limit, a nonzero E=|q| atom,
its finite residue, actual rank-two EM tensor and error moduli all remain
open. Neither endpoint of #744 is declared matched by this note.

## 8. Evidence role and explicit nonclaims

The proof above is finite-dimensional for arbitrary N, not extrapolation
from a lattice enumeration. The optional exact audit verifies local
character identities, six-link Gauss alternatives, a concrete (18), and
algebra of the TARGET photon projector. It does not diagonalize the actual
many-link transfer, estimate its mass gap or measure a phase.

Candidate-T describes the present written argument only. Independent
review, formal public acceptance and Canon promotion are separate. No
claim of blind or two-agent confirmation is made.

S1-S7 remains a proposed attachment. PHOTON-MASSLESS-PHASE and
PHOTON-CONE-CONVERGENCE retain their scopes. No native time, SI scale,
charged-matter coupling, one-photon state, QDD input map, Born event or
physical detector is constructed. The three electric values in (16) are
not the two physical photon polarizations, and the two +/- frequency roots
of the scalar D3 equation are not those polarizations either.

## Sources and scope of inheritance

- [Current #744](https://github.com/mathorn1973/twist-j/issues/744): inherited
  seven-field contract and decision grammar, not this finite proof.
- [Fixed-action program](https://github.com/mathorn1973/twist-j/blob/11b66d4755a697031157f0e10dc1898a7d5b6379/notes/canon/PHOTON-PROGRAM-CLOSURE-V74.md):
  inherited W, G, t=1 and separation of phase from pole identification.
- [Canonical registry](https://github.com/mathorn1973/twist-j/blob/11b66d4755a697031157f0e10dc1898a7d5b6379/canon/REGISTRY.tsv):
  PHOTON-WINDOW-COORDINATES supplies its exact five-vector Fourier data;
  it does not select this transfer or prove a massless phase.
- S1-S7 local attachment, now included alongside this note: source of the
  proposed finite kernel and insertion convention. It is not authority.
- K. Osterwalder and E. Seiler, Gauge field theories on a lattice,
  Annals of Physics 110 (1978), 440-471,
  DOI 10.1016/0003-4916(78)90039-8: external context for positive transfer
  reconstruction. No massless result for this weight is imported. The
  finite specialization and its proof above are given explicitly.

Original new text and audit code: Apache-2.0. No third-party data or code
are redistributed.
