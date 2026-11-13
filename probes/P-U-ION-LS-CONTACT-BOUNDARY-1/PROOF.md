# Closed-loop ion contact: exact symmetry obstruction

**NON-CANONICAL mathematical candidate; conditional on the physical model
and encoding in [MODEL.md](MODEL.md).** This proof constructs no complete
two-contact physical history and assigns no new public Canon status. The
earlier contact and history data were already known before this candidate.

## 1. Fixed target and model boundary

Let the active source and receiver port spaces be copies of C^5 with the
SAME fixed physical level assignment, written |j> for j in F5. Let A denote
every remaining degree of freedom, including the other data registers,
motion, work sources, controller, and environment. The port interchange is

    P|j,k> = |k,j>,                 P_total = P tensor I_A.

At the actual second-contact entry the old mathematical contract has
kappa=0, r=4 and q=0. Its isolated contact is

    C4(s,q) = (q+4, s+1) mod 5.

For all five original histories with a2=4, the source is s=a2+1=0 and the
required active-port transition is therefore

    |0,0> -> |4,1>.                                      (1)

This is a necessary part of the required complete output. It is not a
replacement of that output by a new bit or by a source-preserving task.
There must be a real, isolated physical post-C endpoint at which this
condition is tested, before subsequent native evolution. The target data
are the already stored n=6 rows of
`probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary/CONTACTS.csv`.

The model class permits completed light-shift loops and common rotations
between loops, as specified below. It does not permit additional port-local
operations interleaved inside a loop, changes of the encoding, or uncounted
asymmetric drift. The theorem concerns this class, not every Hamiltonian
available in an ion experiment.

## 2. Closed-loop propagator from the Hamiltonian

Use a single harmonic mode with [a,a^dagger]=I. During one loop let

    D = diag(Delta_0,...,Delta_4),     Delta_j real,
    D_S = D tensor I,                 D_Q = I tensor D,
    A_phi = exp(i phi_S) D_S + exp(i phi_Q) D_Q,

and let eta, delta, phi_S, phi_Q and D be constant during that loop, with
delta>0. The declared interaction-picture Hamiltonian is

    H(t) = i hbar eta/2
           [A_phi a^dagger exp(-i delta t)
            - A_phi^dagger a exp(i delta t)].              (2)

Operators on ports and motion commute. Since D_S and D_Q commute and are
self-adjoint, A_phi is normal. Set L(t)=-iH(t)/hbar. Direct expansion gives

    [L(t1),L(t2)]
       = -i eta^2/2 A_phi A_phi^dagger sin(delta(t1-t2)).   (3)

This commutator commutes with every L(t). All higher nested commutators
therefore vanish. The first two Magnus terms are exactly

    Omega1(t) = beta(t) A_phi a^dagger
                - beta(t)^* A_phi^dagger a,
    beta(t)   = eta [1-exp(-i delta t)]/(2 i delta),
    Omega2(t) = -i K(t) A_phi A_phi^dagger,
    K(t)      = eta^2 [delta t-sin(delta t)]/(4 delta^2).

Consequently U(t)=exp(Omega1(t)+Omega2(t)). This identity needs no Fock
cutoff: resolving the finite-dimensional diagonal A_phi turns each block
into the usual scalar displacement operator with its scalar phase. Those
unitary blocks define the propagator on the full harmonic-oscillator
Hilbert space. The commutator calculation can equivalently be checked on
the common oscillator core and extended through these displacement
operators.

At tau=2 pi m/delta, for any positive integer m, beta(tau)=0. Thus

    U(tau) = exp[-i K(tau) A_phi A_phi^dagger]
             tensor I_motion,
    K(tau) = m pi eta^2/(2 delta^2).                       (4)

The loop closes as an operator identity in this ideal Hamiltonian, not
merely as equality of the final mean motional energy. It therefore also
closes on inherited motion correlated with any other included resource.
Equation (4) does not assert closure for unmodelled modes or errors in a
real device.

The remaining port operator is symmetric because

    A_phi A_phi^dagger
       = D_S^2 + D_Q^2
         + 2 cos(phi_S-phi_Q) D_S D_Q.                    (5)

Interchanging S and Q leaves (5) unchanged, hence [U_ports(tau),P]=0.
The instantaneous H(t) need NOT commute with P when phi_S differs from
phi_Q. The argument uses the completed-loop endpoint and does not replace
that fact by an unsupported symmetry of the raw Hamiltonian.

## 3. Symmetry survives every admitted complete sequence

Every common rotation R tensor R commutes with P. We may allow all unitary
R on C^5 as a favorable mathematical enlargement without asserting that
every such rotation is physically available. Operations I_ports tensor W_A
also commute with P_total. Equation (4) proves the same commutation for
each completed loop, including its identity action on motion. Finite
products of these operations therefore obey

    [V,P_total]=0.                                       (6)

Common free evolution has the same property. For diagonal bare energies,
the complete local Hamiltonian H_S tensor I + I tensor H_Q commutes with
P exactly when

    E_S(j)-E_Q(j) is independent of j.                    (7)

Indeed its |j,k> energy must equal its |k,j> energy, which is equivalent
to E_S(j)-E_Q(j)=E_S(k)-E_Q(k) for every j,k. Scalar port offsets are harmless.
Any differential drift outside (7) must be excluded, explicitly compensated
within the declared model, or counted as a departure in Section 5. It
cannot be silently omitted between completed pulses. During a loop, (2)
must be the actual declared interaction-picture generator, with any
remaining drift already treated in the model.

For the obstruction it is sufficient to work in the larger mathematical
class of all V satisfying (6), even if some of them are not generated by
the stated pulses. This enlargement can only make the impossibility
stronger within the admitted physical subclass. It assumes symmetry under
P_ports tensor I_A, not merely simultaneous interchange of the ports and
two corresponding auxiliary environments.

## 4. Inherited auxiliaries and the one-half bound

Fix any original history h=(a1,4). Exact rank-one physical encoding of its
active entry |0,0> implies that the full state there has the form

    rho_h = |0,0><0,0| tensor sigma_h.                    (8)

No common or fresh sigma_h is assumed. It may be mixed, depend on either
original input, and contain arbitrary correlations among all the other
data, modes, controllers and resources. The factorization with the active
ports follows because their reduced state is pure: positivity confines
the joint state's support to that one-dimensional port subspace. It is
not an extra cooling or reset operation. In particular

    P_total rho_h P_total = rho_h.

By (6) the output rho'_h=V rho_h V^dagger has the same symmetry. Define the
unconditional port-readout effects

    E41 = |4,1><4,1| tensor I_A,
    E14 = |1,4><1,4| tensor I_A = P_total E41 P_total.

Their probabilities are equal. Their supports are orthogonal, so

    p41 = p14,             p41+p14 <= 1,
    p41 <= 1/2.                                         (9)

Thus every one of the five histories with a2=4 has unconditional port
failure probability at least one half. A successful complete contact must
in particular pass this port test, so its success probability is no larger.
Taking the worst case over all 25 original histories gives

    epsilon_write^worst >= 1/2.                         (10)

Discarded trials, failed readouts and heralded failures count as failures;
postselection cannot turn a conditional success rate into p41. A readout
must faithfully resolve the fixed rank-one code states; a detector that
mislabels another state as |4,1> does not establish successful writing.

The proof also works for any jointly P_total-invariant input and any
P_total-covariant full channel. Reduced-port symmetry alone would not
justify this extension in the presence of arbitrary port-auxiliary
correlations. Equation (8) provides the required joint symmetry for the
actual exact entry. No upper bound on the duration or the number of
admitted complete pulses is used, and no attainability of equality in
(9) is claimed.

## 5. Robust operational version

For each actual history h, compare the actual normalized full output
rho_tilde_h with an ideal output rho'_h satisfying the hypotheses above,
using the same inherited input. Assume a declared uniform operational
bound

    (1/2) ||rho_tilde_h-rho'_h||_1 <= delta_out           (11)

on those complete output states. No numerical delta_out is supplied by
this proof. Such a bound must separately cover the model departures being
claimed, including unintended modes, leakage and asymmetric controls.
Both states must be embedded in one specified output space, with an
explicit failure outcome for states outside the code when necessary.

For every effect 0<=E<=I, its probability difference is at most the trace
distance in (11). Applying E41 and (9) gives

    epsilon_write^worst
       >= max(0, 1/2-delta_out).                        (12)

This is a bound on the actual total outputs; it needs no assumption that a
port-only channel remains defined independently of inherited correlations.
It also does not assert a diamond-norm bound or silently impose a finite
motional dimension.

If the entry is itself only close to an exact symmetric entry, an optional
separate statement is possible: let their full trace distance be at most
delta_in, and let delta_out bound the actual-versus-ideal dynamics on the
actual input. Contractivity under the ideal channel and the triangle
inequality then replace delta_out in (12) by delta_in+delta_out. A bound on
the reduced ports alone is not substituted for this full-state premise.

Consequently the portion of the frozen feasibility region requiring
epsilon_write<1/2 is empty for the ideal class; under (11), the portion
requiring epsilon_write<1/2-delta_out is empty when that threshold is
positive. This says nothing about feasibility above those thresholds.

## 6. Explicit routes outside the theorem

The equal port encoding is essential. For example take the different,
fixed dictionaries

    iota_S(s)=|s>,          iota_Q(q)=|q+4 mod 5>.

The physical input labels are then (s,q+4). Encoding the logical output
C4(s,q) produces (q+4,(s+1)+4)=(q+4,s), precisely physical SWAP of the input.
This is an exact algebraic control showing why the same-dictionary
restriction cannot be removed. It neither supplies an available physical
SWAP nor constructs the full history.

Likewise, the original contract permits a separately justified combined
physical step U6 after C when no physical post-C checkpoint exists. Such a
realization does not owe the intermediate test (1) and is outside this
isolated-endpoint theorem. Port-asymmetric couplings, intermediate
nonclosed loops with other data operations, asymmetric environments that
break (6), or additional physical interactions may also leave the class.
Failure here does not prohibit those alternatives or all ion encodings.

## 7. Secondary information and energy boundaries

The stored full boundary-9 logical states for histories
(a1,a2) in {0,1} times {0,1} coincide, including both receivers, both source
ports and the counter. For an exact reversible realization, assume a fixed
factorization into coded data and remainder, orthogonal initial encodings,
a common pure initial remainder, and the SAME pure coded final data vector
|omega_9^*> for those four histories. Unitarity then gives

    |input_h>|e0> -> |omega_9^*>|e_h>,
    0 = <input_h|input_k> = <e_h|e_k>       for h != k.

Therefore dim(H_remainder)>=4 is necessary. This is no sufficiency claim
for a physical implementation. If only a coarse reading is equal and its
physical data fiber has dimension d, the appropriate conclusion is merely

    d dim(H_remainder) >= 4.

Thus unspecified degeneracy or correlations cannot be silently excluded
from the information account. The analogous already merged pairs require
at least two distinguishable remainder states at boundary 6 under the same
pure-code convention. These observations do not construct any enlarged
history or assume fresh motion there.

Finally, independently specified disconnected port energies give the
isolated-contact difference

    w_s = E_S(4)+E_Q(s+1 mod 5)-E_S(s)-E_Q(0).

In particular w_4=0 for any such spectra; the equal-gap example gives
5 Delta for s=0,1,2,3. This difference is not the work of the whole
apparatus, a pathwise resource bound, or a measured quantity supplied here.
If a candidate instead uses a combined t6-to-t7 step with no real post-C
endpoint, this w_s refers only to a hypothetical intermediate state. Its
actual energy account must compare the complete physical endpoints,
including the changes of both receivers and every other participant.

The one-half obstruction is independent of this secondary energy account
and information lower bound. Neither supplies the missing full preparation,
first contact, native continuation, work-source history or archive-protection
certificate.
