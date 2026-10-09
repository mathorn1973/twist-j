# A common endpoint/field Hamiltonian and the boundary of its integer meaning

NON-CANONICAL. Conditional candidate-T; no independent review.
Reservation #1412. This is a quantum comparison, not the requested native
integer-physics closure. In particular, integer configuration labels and
integer-ring operator entries are not a deterministic integer dynamics.

## 1. Inputs and the precise change of theory

Use the labelled D3 incidence complex of the noncanonical #1403 and #1411:
b0=0, b1=(1,1,0), b2=(1,0,1), b3=(0,1,1); all translated edges b_j-b_i,
i<j, and the eight translated oriented triangles +/-(b_i,b_j,b_k).
On a finite primitive periodic quotient with each period at least two,
G is head-minus-tail incidence, C is face circulation, CG=0, P=C^T C.
Edge and face labels survive identifications of their endpoints.
Put R=Z[phi], phi^2=phi+1, s=2-phi, with its positive marked real value.

The source of the moving-endpoint comparison is #1411 at
62487b6e249fad97a6405b862c7fb52a648d4c1f, proof Git blob
261536ba95c0f050369e6965e098d4bbde9ea63a. Its five-value carrier, energy,
matching schedule and all-time translating solutions are NOT retained here.
The field source #1405 is at 393354eaa6ff8afc84d624c06995c3c087f679cd.
Only its supplied spatial complex is used, not its discrete-time law.
Public Canon v100 main is 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc.

Define the countable configuration set

    X={f in Z^Edges : n(f)=G^T f in {-1,0,1}^Vertices}.

Flux is unbounded and is NOT reduced modulo five. There is no separate
particle-position register. Now introduce the additional Hilbert space
H=l2(X), its standard orthonormal basis |f>, complex superposition and
continuous Hamiltonian time. These are NEW, UNADOPTED physical premises.
They do not follow from R, J, the original U, or the selected QDD dictionary.
The restriction on endpoint values is not a derivation of a charge unit or
Pauli exclusion. Charge-zero on a finite closed graph implies equal total
numbers of positive and negative endpoints.

L1 exact configuration/operator arithmetic, a proposed L4 Hilbert support,
and proposed L5 histories are separated by NOTE-ENDPOINT-HILBERT-EXTENSION
and NOTE-HAMILTONIAN-TIME-READING. These names are unadopted comparisons,
not registered gates. No physical reading or Canon status is accepted here.

## 2. Local operators with complete domains

E_e|f>=f_e|f>, N_z|f>=n_z(f)|f>. For a face p let c_p be its integer
boundary row, as an edge column, and define

    W_p|f>=|f+c_p>.

G^T c_p=0, so W_p is a unitary permutation on all X and W_p^dagger=W_p^-1.
All W_p commute. No artificial truncation of their images is allowed.

For e:a->b and sigma in {+1,-1}, define a directed partial hop

    T_e,sigma |f>=|f+sigma e> if (n_a,n_b)=(sigma,0),
                     =0 otherwise.

Its adjoint maps (0,sigma) back by -sigma e. These two domains are disjoint.
Let S_e swap every such matched pair, and fix all other basis states.
Then S_e^2=I, S_e=S_e^dagger. Put K_e=I-S_e. On each active pair K_e is
[[1,-1],[-1,1]], and it is zero on inactive configurations. Therefore

    K_e>=0, ||K_e||<=2,
    K_e=(I-S_e)^dagger(I-S_e)/2.                       (1)

No energy-resonance test or prior five-state cutoff enters the hop.
The decision uses only the fluxes incident to the two endpoints. W_p is
supported on one face. These are spatially local operators; this statement
does NOT make their finite-time exponential a strictly finite-range map.

Closed face shifts leave every n unchanged and commute with elementary
flux addition. Hence on every configuration, including inactive hops,

    [W_p,T_e,sigma]=[W_p,T_e,sigma^dagger]=[W_p,S_e]=0.   (2)

Both signs of endpoint number are conserved by S_e and W_p. Pair creation
and annihilation are deliberately absent. The all-neutral sector is an
invariant subspace, but it is no longer pointwise frozen.

For an explicit gauge account, adjoin temporary site labels q_z in
{-1,0,1}, and impose G^T E-q=0. The isometry

    V|f>=|f> tensor |G^T f>

identifies H with this constrained space. Each W_p changes no q. Each
T_e,sigma changes f_e by sigma AND q_a,q_b by -sigma,+sigma.
It preserves every Gauss constraint, and commutes with the corresponding
local gauge phases. The site labels are redundant in this reduced space;
we have not renamed a violated Gauss constraint as a physical particle.

## 3. One positive energy and one complete quantum evolution

Choose the following ONE comparison tuple, with no fitting:

    H_F = (1/2)sum_e E_e^2
          +(s/2)sum_p (2I-W_p-W_p^dagger),
    H_M = sum_z N_z^2 + sum_e K_e,
    H = H_F+H_M.                                         (3)

The coefficients, endpoint restriction, Hilbert norm and time convention
are selected inputs. Replacing these coefficients by other positive values
preserves the construction's structure; no uniqueness or physical selection
is claimed. The nonzero matrix entries of 2H belong to R. In particular,
finite operator-word calculations on finitely supported vectors are exact
integer coefficient arithmetic (with rational normalization of means).

Every term of (3) is nonnegative. The magnetic term is
(s/2)(I-W_p)^dagger(I-W_p), and (1) treats the hopping term.
The diagonal electric operator A0=(1/2)sum E_e^2 is self-adjoint on

    Dom A0={psi : sum_f (sum_e f_e^2)^2 |psi_f|^2<infinity}.

All other terms form a bounded symmetric operator B: N_z^2<=I,
||K_e||<=2 and ||2I-W_p-W_p^dagger||<=4. Thus H=A0+B is self-adjoint
on Dom A0 and essentially self-adjoint on finite-support vectors.
For completeness, for |Im z|>||B|| the resolvent equation factors through
I+B(A0-z)^-1, invertible by its norm-convergent Neumann series. The closed
symmetric operator has both nonreal resolvent half-planes and is self-adjoint.
The bounded perturbation also preserves the finite-support core.

The spectral theorem therefore defines the exact group

    U(t)=exp(-itH), U(t)^-1=U(-t), U(t)^dagger H U(t)=H.     (4)

No external current, battery, reset or trajectory is prescribed. Conservation
is of this SINGLE operator and its energy distribution/expectation, not a
claim that its diagonal value is conserved at each putative classical jump.
The continuous t and the convention hbar=1 are comparison structure, not
an identification with the native integer counter or an SI action unit.

On a finite graph, A0 has compact resolvent: only finitely many integer
flux vectors have sum f_e^2<=K. The resolvent identity gives compact
resolvent for H too. Every nonempty invariant endpoint-number sector
therefore has an attained bottom spectral eigenvalue. This does not compute
that value or an electron mass. In particular, the bare term sum N_z^2
is not the physical rest-energy difference from the neutral ground state.
It is not the old unattained classical R-valued Poisson infimum in a new name.
No infinite-volume spectral or charged-particle existence theorem is used.

## 4. Exact continuity, source and field work

Set the real skew-adjoint operator and the Hermitian current

    B_e=sum_sigma sigma(T_e,sigma-T_e,sigma^dagger),
    J_e=-i B_e.

The basis definitions imply [E_e,T_e,sigma]=sigma T_e,sigma,
[N_a,T_e,sigma]=-sigma T_e,sigma and
[N_b,T_e,sigma]=sigma T_e,sigma. Consequently,

    dN_z/dt=i[H,N_z]=-sum_e G_ez J_e,                      (5)
    dE_e/dt=(is/2)sum_p C_pe(W_p-W_p^dagger)-J_e.          (6)

Thus the same actual hop supplies the charge current and electric response.
Multiplying (6) by G^T cancels its face term and reproduces (5).
There is no independent source that can be moved while leaving its field
unchanged. The total signed charge, and in this comparison both endpoint
numbers separately, remain constant.

By (2), the magnetic part commutes with H_M. The total endpoint cost also
commutes with every hop. On the common finite-support core we obtain

    W=dH_F/dt=i[H_M,H_F]
       =-(1/2)sum_e {E_e,J_e},
    dH_M/dt=-W.                                           (7)

Here {A,B}=AB+BA. The anticommutator is required by noncommutativity; a
one-sided classical product is generally not the same operator. Formula
(7) is a real exchange between field energy and the hopping energy, not
an auxiliary variable assigned the discrepancy. The derivatives are core
identities and expectation identities where the stated moments/domains
exist; no unbounded-operator domain statement is silently extended to all
normal states. Exact total energy conservation (4) has its spectral meaning.

The sum over edges in (7) is local, so each W_e identifies the work at the
corresponding charged hop. A global decomposition is not substituted for
a full local spatial Poynting theorem, which is not claimed here.

## 5. A phase-sensitive work witness and actual coherent mobility

Take a=0, b=b1, p=b2. Let f have flux -1 on the stored edge a->p and zero
elsewhere. It has n_a=+1,n_p=-1 and f_e=0 on e:a->b. Let g=f+e.
Then n_b=+1 replaces n_a=+1 and g_e=1. Both belong to X.

On the pair f,g the off-diagonal Hamiltonian entry is exactly -1. No face
shift connects different charge profiles and no other labelled edge makes
the same flux change. Its electric diagonal difference is 1/2. Put

    psi_plus=(|f>+i|g>)/sqrt(2),
    psi_minus=(|f>-i|g>)/sqrt(2).

The configuration probabilities, every diagonal observable's mean and the
total mean H agree for these two states. H has real symmetric entries, so
their imaginary coherence contributes no difference to <H>. But directly
from (5)-(7),

    <W>_plus=+1/2, <W>_minus=-1/2,
    <dN_b/dt>_plus=+1, <dN_b/dt>_minus=-1.                 (8)

For the negative endpoint the signed charge-current means reverse, while
the corresponding field-work statement keeps its sign convention.
The compensating material-work means are the negatives of (8).
The values are in the comparison's units, not watts, e, or hbar.

The derivative of <g|U(t)|f> at zero is i, and therefore

    <g|U(t)|f>=it+O(t^2).                                 (9)

The kernel genuinely moves charge amplitude. Successive directed hops along
an initially empty route give the literal shifted link configuration and
carry the endpoint; they do not merely update a position label. Such words
show allowed transitions, not a prescribed or proved ballistic trajectory
of U(t). For a two-link path to h with H_hf=0, its ordered hops contribute
+1 to (H^2)_hf; all two-off-diagonal contributions have the same positive
sign. A nonzero second-order transfer is therefore not a cancellation artifact.

The field also affects subsequent motion: on an active pair [H_F,K_e]
is nonzero, with entries set by the changed electric energy. Thus the two
parts of (3) do not evolve independently. Deleting off-diagonal hopping
freezes all N_z; simply matching the diagonal configuration probabilities
loses (8). These are direct controls against fictitious coupling.

## 6. Neutral field content: exact restriction versus harmonic comparison

On the subspace n=0, H_M=0 exactly, since every S_e is the identity there.
H reduces to the compact U(1) pure-gauge rotor Hamiltonian H_F. The vector
|0> is not fixed by H_F: every oriented face supplies a nonzero coefficient
of |+c_p> and |-c_p>. All these outputs still have n=0. This is neutral
quantum field dynamics, not yet a proof of a photon quasiparticle.

Under the Fourier duality of integer flux and angle, W_p is multiplication
by exp(i(Ca)_p) and E=-i partial_a. The neutral subspace is gauge invariant
under a->a+Gchi. The magnetic energy is s sum_p[1-cos((Ca)_p)].
Its small-angle Hessian, as an explicitly separate quadratic comparator, is

    H_F^(2)=(1/2)|E|^2+(s/2)|Ca|^2,
    a_dot=E, E_dot=-sPa, a_ddot=-sPa.                     (10)

The supplied D3 cochain calculation gives

    spec P(k)={0,8,4-|S|,4-|S|,4+|S|,4+|S|},
    S=1+exp(ik.b1)+exp(ik.b2)+exp(ik.b3).

For nonzero k near zero there are two transverse low modes, with
omega^2=s(4-|S|)=s|k|^2/2+O(|k|^4). Gauge/zero modes, the three extra
gapped modes and crossings remain. This is not two branches at every k
without qualification. Counting two transverse modes is cochain geometry,
not a unique prediction of D3.

The exact compact Hamiltonian is NOT (10). No small-fluctuation control
at the selected coefficients, thermodynamic massless phase, positive photon
pole residue or deconfined charged excitation is established here.
In particular, (10) is not the old finite-tick relation
4sin^2(omega/2)=s lambda. Continuous-time sampling is a new operation.

A definite unit-flux string of length L still has electric mean L/2.
Adding loop transition operators does not prove that the dressed charged
energy is independent of separation. That question concerns the spectrum
above the neutral ground state in an appropriate volume limit, not only
a matrix element between bare strings. No earlier failed gluing is reopened.

## 7. The integer/physical admission boundary

2H has exact R entries, and finite-support algebra is computable with
integer pairs. However, (9) sends a basis configuration to a superposition,
not to another basis configuration. A distribution of classical configs is
also insufficient, as (8) uses two states with the same probabilities.
Therefore this comparison is NOT a deterministic integer automaton in
another notation. It adds a full complex Hilbert state and Hamiltonian time.

Local Hamiltonian terms likewise do not by themselves give the strict
finite dependency radius of a native discrete tick. Arbitrarily long
allowed hopping words appear at successively higher time derivatives.
No equivalence at a specially chosen sampled time, finite-depth circuit,
or native U realization is supplied.

The construction provides one mathematically consistent positive energy,
autonomous reversible quantum evolution, moving endpoint amplitude and
nonzero reciprocal work. It does not provide the user's stronger accepted
closure from integer microscopic states to actual particles and photons.
Its useful output is the explicit missing hopping/coherence energy and an
exact interface to be met by a possible integer derivation, not a license
to import quantum dynamics without proof. Existing ETH-QDD choices do not
adopt this infinite field Hilbert space or its Hamiltonian automatically.

No spin, fermionic exchange sign, relativistic particle mass shell,
electron/proton/neutron identity, particle creation, physical charge unit,
Born occurrence, SI scale or native action/energy selection follows.
All canonical physical owners remain open at their registered scopes.

## 8. Sources and disposition

The common lattice gauge-Hamiltonian mechanism is established prior work:
- J. Kogut and L. Susskind, Physical Review D 11, 395 (1975),
  DOI 10.1103/PhysRevD.11.395.
- E. Zohar and M. Burrello, Physical Review D 91, 054506 (2015),
  arXiv:1409.3085, DOI 10.1103/PhysRevD.91.054506.
They are methodological context, not a claim that their full theory equals
this restricted scalar endpoint model. The algebra above is self-contained.
No external simulation, source code or published numerical result is copied.
Original text and code Apache-2.0. Conditional candidate-T only; unreviewed.
