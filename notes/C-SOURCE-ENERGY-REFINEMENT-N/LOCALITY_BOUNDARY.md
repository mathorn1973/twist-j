# Exact geometric range, prepared-source action, and ancillary boundaries

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
The prospective [CONTRACT.md](CONTRACT.md) is public at
`d69ff34274ffce191055df7fd44e092366e20819`.
Independent scientific acceptance is not asserted.

An exact decomposition into terms of fixed interaction order does not
give a fixed microscopic spatial range. This note proves a geometric
obstruction for the entire finite-code polynomial generator, states a
separate necessary energy-action condition on the actual prepared
family, and explains why accurate ancillary time simulation alone does
not settle that condition. None of these results excludes every local
approximation on the prepared family or every dressed encoding.

## 1. Physical support and a fixed ancillary ready state

Use the original occupation code and its retained diagonal phase gauge.
Physical sites are the original integer lattice sites. Additional
ancillary factors, when present, have declared physical locations.
Let a normalized ancillary ready vector a be fixed independently of
the data, and write

    V psi = I psi tensor a,                          (G1)

with identity on any passive references. The ready vector may be
entangled across its ancillary sites; a product over those sites is not
required. A fixed mixed ready state can be purified with a passive
reference. The factorization in (G1) between the data and its supplied
ancilla is the condition used here. A data-dependent dressed encoding
is a different class.

Consider a self-adjoint physical Hamiltonian

    H_tilde = sum_X H_X,       diam(X)<=rho,          (G2)

where each H_X acts as identity outside its physical support X. Finite
sums suffice for the finite apparatus question. The same matrix-element
arguments apply to infinite sums when their partial sums define the
stated matrix elements and the compressed operator
K=V*H_tilde V is bounded. Individual terms need not be positive or
separately conserve occupation charge. Their strengths and number are
not restricted by the following necessary support condition.

Compression against the fixed ancilla leaves each term supported on
the data factors in X: it takes the expectation against the reduced
ancillary state on X and leaves the data outside X unchanged. Therefore
a matrix element between two original occupation basis states is zero
unless every physical site at which their active occupation patterns
differ belongs to X. Entanglement within the supplied ready ancilla
does not change this statement. The code's diagonal phases multiply
matrix elements by phases and do not change their zeros.

## 2. An extremal matrix element fixes an exact range lower bound

Let U_L be the complete finite cyclic coordinate step of
[PR1781 PHYSICAL_BLOCK.md](https://github.com/mathorn1973/twist-j/blob/5f7301e4d891596628cb25c6e735a7e4cd9004a8/notes/C-FINITE-OCCUPATION-ENERGY-N/PHYSICAL_BLOCK.md),
on R,c in 97+[-L,L] and r in [-L,L]. Keep the unchanged factor order

    U_L=P_beta Gamma S_R S_r E_rec,L Q_p M2 C,
    beta=4pi/5,       g=2pi/5.                       (G3)

The object coin e1 streams R by -1 under a forward step. At r=0,
Gamma supplies phase exp(-ig). The diagonal e1 matrix element of M2
is 1/5. In pulse bank 2, the maximal right-moving matrix element of
E Q_p is -4/5, and its final bank is again 2.

Fix any integer N>=1 and L>=2N+1. For a Laurent polynomial

    q(z)=sum_(k=-N)^N a_k z^k,       a_N != 0,        (G4)

choose the following two normalized coordinate-code basis vectors:

    b: R=97,   r=0, o=e1, pulse bank 2,
       c=97-2N, carrier label 0, receiver label 1;
    a: R=97-N, r=0, o=e1, pulse bank 2,
       c=97-N,  carrier label 0, receiver label 1.   (G5)

Both lie in the admitted finite code. Receiver label 1 is an ordinary
occupied input label, not a blank memory or a source-dependent oracle.
These are test vectors for an equality on the ENTIRE finite code; they
are not the active phase-prepared source pair.

**Lemma G1.** The matrix element is exactly

    <a|q(U_L)|b>
      = a_N exp[-iN(beta+g)] (-4/25)^N.             (G6)

**Proof.** Every forward or inverse complete step changes R by at most
one. Since R starts at the center and |k|<=N<L, no R wrap can occur.
Thus |k|<N cannot connect the two R coordinates in (G5).

For the inverse N-step term, the first inverse object streaming acts
on the initial e1 before the inverse object coin or inverse contact.
It moves R by +1. The remaining N-1 steps can move R left by at most
N-1, so their total displacement cannot be -N. Thus
<a|U_L^-N|b>=0.

For the forward N-step term, reaching R=97-N requires the leftmost
object shift at every step, hence coin e1 at every streaming stage.
Reaching c=97-N from c=97-2N requires the rightmost pulse shift at
every step, hence pulse bank 2 after each step. There is no other path
with these simultaneous extremal displacements. The coordinate period
2L+1 is larger than 2N, so a wrapped pulse path cannot give the same
endpoint in N steps.

Before forward step j+1, 0<=j<N, the object center and pulse position
are respectively 97-j and 97-2N+j. Their separation is 2(N-j)>0.
The contact is therefore identity throughout this extremal path.
The receiver cut is never crossed: all its carrier positions are below
100, so its label calibration acts as identity. The object relative
coordinate remains zero. Each step has amplitude
exp[-i(beta+g)](1/5)(-4/5). Multiplying the N amplitudes proves (G6).
QED.

In the original physical encoding, b has its two object constituents
at site 97 and its pulse at 97-2N. In a, both object constituents and
the pulse are at 97-N. The object and carrier occupy disjoint subbanks;
their changes cannot cancel at a site. The memory at 100 is unchanged.
Consequently the active occupation patterns differ at all three sites

    97-2N,       97-N,       97.                     (G7)

Their physical diameter is 2N. The diagonal gauge preserves the nonzero
magnitude in (G6).

**Theorem G2.** No sum (G2) with rho<2N has compression equal to
E0 q(U_L) on the entire finite original code, under the fixed ancillary
embedding (G1). In particular it cannot exactly intertwine that
generator on the entire code.

**Proof.** Every compressed term has zero matrix element between the
two physical states (G5), because its support cannot contain both
extreme sites of (G7). Their sum has zero matrix element. Equation
(G6) is nonzero, a contradiction. Exact intertwining would imply that
same compressed equality. QED.

This theorem permits arbitrarily strong terms, arbitrarily many ready
ancillas, and entanglement within their common fixed ready state. Those
resources do not enlarge a single term's physical data support after
compression. In a finite exact decomposition, at least one term
contributing to (G6) must have diameter at least 2N.

For the present Fejer polynomial of exact degree

    D=2^35-1,       L=47D+3,
    q_D(z)=pi-i sum_(k=1)^D
                   [1-k/(D+1)](z^k-z^-k)/k,        (G8)

the highest coefficient is -i/[D(D+1)]. Its witness magnitude is

    |<a|q_D(U_L)|b>|=(4/25)^D/[D(D+1)]>0.           (G9)

Thus exact realization of this entire finite-code generator with a
fixed data-independent ancillary ready state requires a term of
physical diameter at least 2D. An exact bounded-order decomposition
may meet this requirement through a small number of widely separated
sites. It does not become a microscopic short-range decomposition.

The value (G9) is extremely small. This proof does not supply a useful
lower bound at the allowed approximation tolerance, and its test input
is not the actual prepared source. It therefore does NOT exclude a
different short-range Hamiltonian that approximates only the requested
source family and finite time interval. Nor does it exclude an
explicitly dressed encoding or a different admitted physical class.

## 3. A necessary action bound on the actual prepared family

The actual sources psi_± use only original U powers between -2 and 2
on chi at (R,r,c)=(97,0,97). Their coordinate support therefore obeys
|R-97|<=2, |r|<=2, |c-97|<=2. The object positions R+r and R-r,
the carrier, and the receiver at 100 all fit in the conservative
physical interval

    Lambda_0={93,...,101}.                           (G10)

Every active source basis ket has occupation charge 10. Unknown memory
and references change neither this active support nor its charge.
For rho>=0, let Lambda_0^[rho] be the physical rho-neighborhood of
Lambda_0, and let P_out,rho be the projection in the original active
charge-10 code onto basis states having at least one active occupied
site outside that neighborhood. It acts as identity on passive
references.

**Lemma G3.** For the compressed operator K in Section 1 and any actual
prepared-family input psi,

    P_out,rho K psi=0,
    ||H_tilde V psi - V Q psi||
      >= ||P_out,rho Q psi||.                       (G11)

**Proof.** Consider a source basis ket beta supported in Lambda_0 and
a target charge-10 basis ket alpha with a nonzero active occupation
at y outside Lambda_0^[rho]. A nonzero matrix element of a term H_X
would require y in X and equality of all active data outside X.
Since diam(X)<=rho, X is disjoint from Lambda_0. All charge 10 of beta
therefore lies outside X and is retained by alpha. Its additional
positive active charge at y would then give alpha total charge greater
than 10, a contradiction. The compressed term has zero matrix element.
Linearity, convergence of admitted partial sums and the passive
reference identity prove the first statement. Applying the contractions
V* and P_out,rho to the full action error proves the second. QED.

No separate termwise charge-conservation assumption was used: the
source and target active code charges already suffice for the support
argument. Ancillary transitions and leakage outside the original code
cannot remove the projected lower bound.

A finite polynomial certificate supplies a possible future lower-bound
test. If ||[q(U)-f(U)]psi||<=delta, then

    ||H_tilde V psi - V Q psi||
      >= E0 ( ||P_out,rho q(U)psi|| - delta ).       (G12)

A negative right side is only the trivial bound. The vector q(U)psi
has finite support, but no projected tail in (G12) was enumerated or
bounded from below in this note. In particular no nonzero lower value
for the actual requested tolerance is asserted. The finite-source
boundary is a necessary test, not an impossibility theorem for its
whole physical realization class.

## 4. Accurate time simulation need not approximate energy action

For any real Delta>0 consider the positive two-dimensional Hamiltonian
and bare ready state

    H_Delta = [[1,sqrt(Delta)],[sqrt(Delta),Delta]],
    e0=(1,0)^T.                                     (G13)

Put v=(1,sqrt(Delta))^T/sqrt(Delta+1). Then
H_Delta=(Delta+1)|v><v| and |<v,e0>|^2=1/(Delta+1). Comparing with
the zero target generator gives, for every real dimensionless time t,

    ||[exp(-it H_Delta)-I]e0||
      = |exp[-it(Delta+1)]-1|/sqrt(Delta+1)
      <= 2/sqrt(Delta+1).                            (G14)

This tends to zero uniformly for all times. Nevertheless

    ||H_Delta e0||=sqrt(Delta+1),                    (G15)

which diverges. A common positive scalar energy may be added to both
target and simulator without changing these comparisons. No numerical
example or limit exchange is needed for (G13)-(G15).

Thus a high-energy mediator can have a vanishingly small excited
amplitude and excellent state evolution while carrying a large energy
action on the bare input. A construction based on such mediators must
supply its own energy-action bound or an explicit dressed initial
encoding, with its preparation and original-port comparison. A history
clock or a low-energy effective Hamiltonian does not satisfy that
additional contract merely by reproducing an endpoint or a time window.
This example is a warning about an inference, not a no-go theorem for
all properly accounted ancillary constructions.

## 5. Separate review obligations

1. Check the geometric support definition and the fixed ancillary
   compression, including ready states entangled across ancillary sites.
2. Check the finite U_L factor order, inverse first-streaming step,
   extremal path, calibration predicates and exact coefficient in (G6).
3. Check the original object and pulse subbanks and the physical
   changed-site union (G7), including the retained diagonal gauge.
4. Check the exact whole-code range theorem and its specialization to
   the Fejer coefficient, without promoting the tiny witness to a
   source-family approximation lower bound.
5. Check the conservative source support, charge argument, arbitrary
   memory/reference extension and the two contractions in (G11).
6. Check the polynomial comparison in (G12) and preserve its unexecuted,
   unevaluated lower-tail status.
7. Check the positive two-dimensional example and the distinction
   between uniform time accuracy, bare energy action and dressed codes.

These are same-session analytical results under the frozen model and
source assumptions. No scientific executable, matrix enumeration,
simulation or numerical spectral search was run.
