# Complete occupied-tape inverse and energy proof

**NON-CANONICAL / conditional candidate-T / L1 mathematical design.**
Original work Apache-2.0, A. M. Thorn, 2026-10-13.
Reservation: [#1484](https://github.com/mathorn1973/twist-j/issues/1484).
Lane R follows the complete contract pinned at
`4302c31f07823b2a843e3702ca14620c1917b853`, with immutable
[CONTRACT.md](CONTRACT.md), README and SOURCES. The authority basis is Public
Canon v101 at `5f54015ed8361e3a64cb10894397020ddfadd104`.

This is an analytical proof on the specified rational carrier. No scientific
code, verifier, propagator, hardware operation or data acquisition is used.
Physical realization, independent source admission and qualification remain
the separate obligations of the contract. No Canon status is changed.

## 1. Fixed types and the finite Dirichlet energy

Use the contract's finite set

    D = Y+B_zero+B_zero,  B_zero=B union {0},

with its literal coordinates, zero extension and marked insertion
`P:Q^4 -> Q^D`. Distinct marked sites give `P^T P=I_4`. Put

    G=diag(g_0,...,g_3)=2I_4,
    C=PGP^T,  D_g=I+C/2,  J=I-C/2,  H=2I-L_D,  K=D_g^-1.

Here D_g is diagonal, with value 2 on R and 1 elsewhere. Thus K is a
rational total operator, without any nonzero-state or clean-memory premise.
All vector inner products below are ordinary real inner products, restricted
to the rational carrier. In particular, no quotient by sign is taken.

The full stencil is symmetric and has strictly positive coefficients. Its
shell multiplicities at squared lengths `(2,4,8,10,16)` are `(12,6,12,24,6)`;
their weighted sum is `288/324=8/9`. For the zero extension f_tilde,

    f^T L_D f
      = (1/2) sum_(x in D3) sum_(d in B)
          c_d [f_tilde(x)-f_tilde(x+d)]^2.                       (1)

This includes edges crossing the boundary of D. The right side is
nonnegative. If it vanishes, f_tilde is constant along every stencil edge.
In particular it is constant along the infinite chain `x+n(1,1,0)` for each
x. Finite support makes that constant zero. Hence L_D is positive definite.
Using `(a-b)^2<=2a^2+2b^2` in (1) also gives

    0 < L_D <= (16/9) I                                        (2)

as quadratic forms on nonzero vectors. Boundary diagonal entries remain
8/9: replacing this operator by an induced-subgraph Laplacian would not
prove the same assertion.

For m=(u+v)/2 and d=(v-u)/2, symmetry of L_D yields

    E_D(u,v) = (||v-u||^2+u^T L_D v)/2
             = (m^T L_D m + d^T(4I-L_D)d)/2.                 (3)

Both forms on the right are positive definite by (2). Therefore E_D is
positive definite on the complete wave pair: it vanishes exactly at u=v=0.
This proof does not require the operational initial source or the causal
horizon. The finite mathematical wave law and its energy are defined for
arbitrary rational wave pairs and for every iterate.

Write `q_g(a)=a^T G a=2 sum_(j=0)^3 a_j^2`. Every sum includes all four
ports, including zero-valued or sign-reversed ports.

## 2. Complete coupling and its two-sided inverse

The full coupling is

    w=K[Hv-Ju+2PGa],
    p=P^T(w-u)/2,
    b=a-p,
    Couple((u,v),a)=((v,w),b).                                (4)

Take any output `((v,w),b)` in `Q^D x Q^D x Q^4`, not merely an output of a
prepared trajectory. Define

    u=K[Hv-Jw+2PGb],
    a=b+P^T(w-u)/2.                                          (5)

These expressions are total and rational. To verify them, substitute
`a=b+P^T(w-u)/2` into the forward equation in (4). Since C=PGP^T,

    D_g w = Hv-Ju+2PGb+C(w-u)

is equivalent, after collecting terms, to

    D_g u = Hv-Jw+2PGb.                                      (6)

Equation (6) is precisely (5). The equivalence is reversible, and D_g is
invertible. Thus applying (5) after (4) recovers the original u and a, and
applying (4) after (5) recovers the arbitrary output v,w,b. The complete
coupling is a bijection on the entire product, with no reset, discarded
output, normalization or ancillary ready state.

## 3. Exact per-cut energy identity

Symmetry of L_D gives the algebraic identity

    E_D(v,w)-E_D(u,v)
      = (1/2)(w-u)^T [w+u-Hv].                               (7)

From (4),

    w+u-Hv = 2PGa-(C/2)(w-u) = PG(a+b).

Using `P^T(w-u)/2=p=a-b` in (7) therefore gives

    E_D(v,w)-E_D(u,v)
      = (a-b)^T G(a+b) = q_g(a)-q_g(b),

or, equivalently,

    E_D(v,w)+q_g(b)=E_D(u,v)+q_g(a).                         (8)

This is an exact identity for arbitrary signed a,b and arbitrary wave pairs.
It includes incoming work at every port. Under the cold condition a=0, the
wave-energy decrease is q_g(b)>=0. Its square does not replace the stored
signed vector b.

## 4. Total occupied two-tape transition

The complete carrier is

    X=(Q^D x Q^D) x (Q^4)^2 x (Q^4)^2 x (Z/2Z).

Every tape slot may already be occupied. For
`X=((u,v),(A0,A1),(B0,B1),k)`, apply (4) with a=A0 and define

    F(X)=((v,w),(A1,B1),(b,B0),k+1 mod2).                    (9)

The slot labels B0,B1 here mean the outgoing tape, not the geometric stencil
`B_zero`. The pointer advances independently of amplitude values.

For an arbitrary post-state

    X_plus=((v,w),(alpha0,alpha1),(beta0,beta1),k_plus),

first apply (5) to `((v,w),beta0)` to obtain u and a. Then set

    F^-1(X_plus)
      = ((u,v),(a,alpha0),(beta1,alpha1),k_plus-1 mod2).        (10)

Indeed, the forward coupling consumes exactly this a and returns exactly
beta0. Its slot permutation returns `(alpha0,alpha1)` and `(beta0,beta1)`.
Conversely, starting from (9), (10) recovers A0 from the complete coupling,
A1 from A'_0, B0 from B'_1 and B1 from A'_1, as well as the original pointer.
Both composition identities hold on all of X. F is globally one-to-one and
onto, including zero or occupied tape entries and either pointer value.

Define

    E_full(X)=E_D(u,v)+q_g(A0)+q_g(A1)+q_g(B0)+q_g(B1).        (11)

The tapes after (9) contain A1,B1,b,B0, so (8) immediately yields

    E_full(F(X))=E_full(X)                                   (12)

on the full carrier. This is not a ready-prefix-only identity. By (3) and
g_j=2>0, E_full is positive definite in all amplitude coordinates and
nonnegative on X. It vanishes exactly when the wave and all tape amplitudes
vanish; either value of k is still allowed. The mathematical pointer has
zero assigned bookkeeping energy. No physical zero-cost pointer is proved.

Induction applies (10) and (12) to arbitrary occupied continuation:
`F^n` is a bijection with inverse `(F^-1)^n`, and E_full is invariant for
every integer n>=0. No fresh zero slot or extra bit is introduced at any step.

## 5. Exact two-cut composition and prepared post-state

For any initial tapes, let

    Couple((u,v),A0)=((v,w0),b0),
    Couple((v,w0),A1)=((w0,w1),b1).

Direct substitution into (9) gives the complete two-step formula

    F^2((u,v),(A0,A1),(B0,B1),k)
      = ((w0,w1),(B1,B0),(b1,b0),k).                         (13)

In particular the first two incoming values are A0,A1, independently of both
initial B slots. This statement includes arbitrary occupied initial B and
does not assume that it is energetically empty.

For the declared source z, set s=sum_i z_i and

    S=S(z)=sum_(i=0)^3 (z_i-s/5)delta_yi -(s/5)delta_y4.

For arbitrary c0,c1 in Q^4 define the cold-prefix preparation

    X0(z;c0,c1)=((0,S),(0,0),(c0,c1),0).                     (14)

The exact wave and signed outputs are

    w0=K H S,
    w1=K[H K H S-J S],
    b0=-P^T w0/2,
    b1=-P^T(w1-S)/2.                                        (15)

The actual intermediate and final full states are

    X1=((S,w0),(0,c1),(b0,c0),1),
    X2=((w0,w1),(c1,c0),(b1,b0),0).                         (16)

Thus both cuts are cold for every c0,c1. The chronological delivered record
is `Y_2=(b0,b1)`. The final B tape stores `(b1,b0)`; the chronological reader
must return `((B_tape_final)_1,(B_tape_final)_0)`, in that order. Neither a tape
slot-order convention nor an energy deposit may silently change this signed
chronological equality. The remaining wave and both tapes are retained.

Because the five marked sites are distinct,

    ||S(z)||^2=||z||^2-s^2/5,
    E_D(0,S)=z^T(I_4-11^T/5)z/2.                            (17)

The source Gram matrix has eigenvalues 1 on the sum-zero subspace and 1/5
on the constant line. It is positive definite. Applying (8) twice yields

    E_D(w0,w1)+q_g(b0)+q_g(b1)=E_D(0,S),                    (18)

and the full occupied-state account is

    E_full(X2)
      = E_D(w0,w1)+q_g(b1)+q_g(b0)+q_g(c1)+q_g(c0)
      = E_D(0,S)+q_g(c0)+q_g(c1)=E_full(X0).                 (19)

The old occupied B energy moves into A; it is not discarded or assumed zero.
For z in Z_op, (17) gives E_D(0,S)<=||z||^2/2<=2, so the sum of the two
cold outgoing deposits is at most 2. This is a mathematical normalized
bound, not a measured SI energy or an apparatus calibration.

## 6. Why the causal claim stops at H_run=2

On the infinite lattice use `H_infty=2I-L` and the same port-diagonal K,J
extended by their off-port identity values. Multiplication by H_infty expands
support by at most `B_zero`; diagonal K and J do not expand support. Starting
with support Y, the infinite counterparts of (15) therefore have

    supp(w0) subset Y+B_zero,
    supp(w1) subset Y+B_zero+B_zero=D.

The previous fields in the two cuts have the same respective support bounds.
Every infinite field needed to evaluate those two updates vanishes outside D.
The principal Dirichlet restrictions consequently equal the infinite updates,
including all four port values, through the declared two-cut horizon. The
initial occupied B never enters those two updates, by (13). This proves the
prepared causal-prefix equality on the stated domain, without a trajectory
census or a boundary-energy deletion.

F remains a well-defined energy-preserving finite-domain law after H_run, but
the support may then reach outside D in the infinite model. No equality with
that infinite continuation is claimed. A larger causal horizon requires a
newly declared carrier/contract, not reinterpretation of this proof.

## 7. Pointer, cold capacity and history recirculation

The pointer is parity: k_n=k_0+n mod2. It is not consulted in the wave or
tape equations. In particular k_2=k_0 does not indicate that the trial ended,
that its state returned, that its record was exported or that a reservoir was
renewed. The contract separately supplies the external stop at H_run=2.

For the preparation (14), steps 3 and 4 receive a2=c1 and a3=c0. If these
entries are occupied, the continuation is warm and can return tape energy
to the wave. With full operational readiness c0=c1=0 there are four initially
prepared zero entries across the two tapes: the next two inputs are also
zero. They are pre-existing resources, not fresh clean entries. After four
steps the tapes are `(b0,b1)` and `(b3,b2)`, so the fifth input is b0. These
facts concern finite-domain continuation only and extend neither the H_run
causal guarantee nor the physical operational test.

Old output signs are not erased by (9); they first shift, then return as
inputs and interact with the wave under a bijective coupling. They need not
remain separately visible as literal output slots. Given the final complete
state and a known finite n, repeated (10) reconstructs the complete past
trajectory, including every signed b at each cut. This is a backward-read
statement with the full wave, all occupied tapes and known horizon. The
current B tape or parity pointer alone is not a separate ever-growing
chronological archive, and no arbitrary new independent input stream is
supplied during repetition of this fixed autonomous map.

The pair energy is even under simultaneous amplitude sign reversal, whereas
F's amplitude part is linear and reverses every output sign. Thus energy
records cannot substitute for the signed full-state reader or its inverse.
Likewise summing q_g(b) over arbitrarily many recirculating steps and calling
it permanently extracted energy would count returned energy repeatedly. The
correct per-cut net transfer always remains q_g(a)-q_g(b).

## 8. Comparison with T3 and the T2 archive domain

The scoped T3 proof at
`145266fd4bc0961f9294a5f3eb6e95613b36d43d` shows: if pi is onto, L is onto
and `pi L=h pi` on the whole declared carrier, then h must be onto. It excludes
complete reversible lifts preserving its specified nonsurjective native
context update on every helper state, regardless of helper capacity.

This construction changes that off-ready projection law. Projection of F to
the wave is not the cold wave map independently of A0: the term `2PG A0`
in (4) is present on the complete carrier. For example at wave pair (0,0),
the incoming value A0=e_j gives w=2Pe_j, while A0=0 gives w=0. The required
two-cut cold projection is reproduced on the prepared prefix; it is not an
identity on every occupied helper state. This is precisely a different
completion permitted by T3's stated scope. It is neither a counterexample
to T3 nor an onto reversible
lift of the same lossy cold/native update on a whole independent product.

The T2 proof at `fd96e5eb3318620f75056efeec3c2439ace08e84` concerns its
different integer field/contact carrier and two unbounded nonnegative integer
registers encoding ternary words. Its fixed finite-alphabet history bound
uses positive definite integer energies, finite old shells and independently
chosen contact words. None identifies those stocks/gains or ternary digits
with the present rational amplitudes or tape slots.

Here a finite number of slots is not a finite alphabet: the carrier is Q,
with no denominator, precision or distinguishability bound. Even a fixed
positive mathematical energy shell need not be finite. For example take
wave zero, all slots zero except

    A0=((1-t^2)/(1+t^2), 2t/(1+t^2), 0, 0),  t in Q,

and fix k. These infinitely many rational states have q_g(A0)=2 and hence
E_full=2. A finite-bit pigeonhole bound cannot be applied merely by counting
these slots or by invoking their bounded energy. Conversely this exact
rational model supplies no physically readable infinite precision or free
archive capacity. A finite-bit, finite-resolution or finite-energy physical
capacity claim needs its own encoding, distinguishability and resource
contract. No minimum register count is proved here.

## 9. Physical boundary and reset qualification

With the selected positive calibration parameters, the dimensional map gives

    tau_step sum_j F_j V_j
      = E_star [q_g(a)-q_g(b)] = E_star Delta E_wave.          (20)

Equation (20) is the mapped algebraic per-cut identity. It does not by itself
equal an independently measured continuous work integral without the frozen
bin/transfer rule and uncertainty. When wave and both tapes are inside the
physical instance boundary, their energy changes cancel by (12): the outgoing
tape energy is internal storage, not an additional external flux to add again.
If records or sensors are separately copied/loaded, those physical systems
also belong in the declared ledger rather than being silently omitted.

The measured boundary must include source preparation, both tapes, control/
clock, sensing/loading, retained records, loss ports and reset, with the
contract's external work/heat sign convention. The inverse is not a preparation
or renewal procedure. Mapping arbitrary occupied unknown states to a single
ready state while discarding their distinctions would not be this bijection.
A new trial must specify the actual source preparation, ready-tape operation,
old-record disposition, all work/heat exchanges and independent qualification.
No reset cost, Shannon distribution, entropy or Landauer value is derived.

Stage S/I/V qualification, calibrated units, physical source/contact admission,
native-to-wave encoding, common timing, occurrence/sampling and L2-L6 bridges
remain open. The candidate proof establishes the exact complete inverse,
positive amplitude energy invariant and two-cut prepared signed record at
their frozen rational mathematical scope.
