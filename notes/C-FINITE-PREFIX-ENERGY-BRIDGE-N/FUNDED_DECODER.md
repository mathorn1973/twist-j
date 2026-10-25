# A counted sharp-sector decoder and its preparation boundary

**NON-CANONICAL, L1; analytical candidate, independent acceptance pending.**

## 1. The receiver is not automatically a factor of the code

Write the original space H=H_G tensor M, dim M=26, with all original
nonreceiver factors included in H_G. Q=E0 f(U_rec) generally acts on M
too. A receiver observable that changes under U_rec cannot commute with
Q, since commutation with Q would imply commutation with exp(-iQ/E0).
Consequently the sharp-source trace identity from #1768 cannot simply
be applied to M after replacing its source-only energy by this Q.

For an orthonormal basis e_i of the D-dimensional code X, define

    G=span{(I tensor <m|)J e_i: 1<=i<=D, 1<=m<=26},
    g=dim G<=26D,       L=G tensor M,       dim L=26g. (D1)

Let i_G:G->H_G be inclusion. There is an exact isometry

    D_in:X->L,       (i_G tensor I_M)D_in=J.          (D2)

This same D_in is used for every prefix. The finite output channel is
Tr_G(D_in sigma D_in*) and retains arbitrary reference correlations.
It does not identify a 26-state tensor factor inside X.

## 2. Complete load, selection and decoding unitaries

Let a_-=min spec(q_d/d), b_+=max spec(q_d/d), v=b_+-a_-.
Choose a common eigenvector e_* of q_d,r at height b_+, with residual
r_* in [0,d]. Put E=X. Select fixed basis-ready states 0_I and 0_L.
The following isometries between equal-dimensional subspaces extend to
complete unitaries on their stated finite spaces:

    P_load: |e_*>_E |phi>_I -> alpha|phi>_E |0>_I,
    D_dec:  |psi>_E |0>_L -> |e_*>_E D_in|psi>_L.    (D3)

For P_load the prescribed subspaces have dimension a, and D>=a.
For D_dec both have dimension D. Choose ordered orthonormal bases of
the two orthogonal complements and map them to one another. This fixes
the full unitary; no discarded domain or postselected isometry is used.

The selector C has N+1 admitted values. Define

    V_sel=sum_(n=0)^N |n><n|_C tensor V^n,
    W=D_dec V_sel P_load.                            (D4)

All unmentioned factors carry identities. These definitions first act on
the admitted finite spaces. With c=ceil(log2(N+1)) physical selector
qubits, extend the ENTIRE word W by identity on the orthogonal complement
of the valid semantic code, including unused selector labels. Merely
extending V_sel would leave D_dec P_load acting there and would be a
different raw extension. The flag flip in the thermal target uses this
same valid-code block. The input contract promises valid selectors;
no physical time or completion guarantee is assigned to invalid labels.

At every admitted n,

    W(|e_*>|phi>_I|n>_C|0>_L)
       =|e_*>|0>_I|n>_C D_in V^n alpha|phi>_L.      (D5)

The word has one common endpoint. It must not leave an additional discarded
auxiliary record of n beyond the prescribed dilation (D9). A fixed coherent
controlled word and complete compiler cleanup meet that condition; G itself
may of course carry the correlations required by the target channel.

## 3. Sharp battery and the whole-word identity

Use B=max(1,v) gap-d qubits, with unary vectors u_k=|1^k0^(B-k)> and
H_B=d sum n_i. There is no supplied coherent battery. For every
b_+<=z<=B+a_- define

    F_z psi=sum_(r=a_-)^(b_+) P_r psi tensor u_(z-r),
    P_good=sum_z F_z F_z*,
    Gamma(Y)=sum_z F_z Y F_z*+(I-P_good).             (D6)

P_r here are the spectral projectors of q_d, tensored with identities
on I,C,L and other zero-energy factors. The F_z are orthogonal isometries
of the entire semantic source/information space. Thus

    Gamma(Y2)Gamma(Y1)=Gamma(Y2 Y1),
    [Gamma(Y),q_d+H_B]=0,       Gamma(Y)*Gamma(Y)=I. (D7)

Every nonunary configuration and incomplete fiber is in the retained
identity complement. Later binary/one-hot padding is identity-extended
as described in the thermal note; it is not omitted from raw dimensions.

Because e_* tensor u_0=F_(b_+)e_*, equations (D5)-(D7) give exactly

    Gamma(W)(|e_*>|phi>_I|n>_C|0>_L|u_0>)
      =|e_*>|0>_I|n>_C D_in V^n alpha|phi>_L|u_0>.   (D8)

The same identity holds coherently over n and all inputs. The battery
returns to vacuum and decouples on this specified completed family.
There is no accumulation of a battery-coherence approximation over N.
Intermediate source/battery states need not be products.

Append a complete SWAP between M in L and a separate occupied archive A
of dimension 26. Both helper M and A have zero bare energy in this
simulator. The archive receives the exact original memory channel, and
its old contents move to helper M. All correlations with I,C,A and R
are preserved in the complete joint identity; nothing is erased.

The input-register reset in (D8) is also not erasure. Its quantum
information is in L, C and their correlations. The ready helper bank
has been consumed. Restoring E and the battery is not a reset of L or
regeneration of the thermal apparatus.

## 4. Coherent selected output

Define T_n=D_in V^n alpha. The common isometry

    T_sel=sum_n |n><n|_C tensor T_n                  (D9)

followed by SWAP_(M,A) is the ideal completed dilation, including the
arbitrary old archive. Tracing G and the helper holding old A gives
the promised joint channel to C,A,R. This formula, rather than separate
comparisons of marginals, defines the output when A is initially
correlated with the other input registers.

For the simpler input without the old-archive factor, writing its
C-blocks as rho_nm makes the coherence explicit:

    rho_(C,M,R),out
      =sum_(n,m) |n><m| tensor
         Tr_G[(T_n tensor I_R)rho_nm(T_m* tensor I_R)]. (D10)

If C is discarded, only the diagonal sum remains. C is an active
control, not a passive reference, and must be retained physically when
(D10) is claimed. This is one selected snapshot per run, not simultaneous
copies of all N+1 quantum states.

## 5. A preparation obstruction that remains after decoding

Suppose a complete preparation input commutes with Q_S+H_rest and its
unitary conserves that sum. The reduced output sigma_SR then commutes
with Q_S tensor I_R, by invariance under total time translations and
partial trace. Sharp batteries and independent Gibbs ancillas, including
different temperatures, meet the stationarity premise. Arbitrary
reference correlations in zero-energy input factors do not change it.

For a target pure state Psi_SR and a finite spectral partition {P_j}
of Q_S, write p_j=||(P_j tensor I_R)Psi||^2. A stationary sigma is block
diagonal, whence

    <Psi|sigma|Psi> <= max_j p_j,
    D_tr(sigma,|Psi><Psi|)>=1-max_j p_j.              (D11)

Indeed each normalized block of sigma has overlap at most p_j, and its
block weights sum to one. Measuring the target rank-one projector gives
the trace-distance lower bound. A covariant outcome instrument preserves
this obstruction; an asymmetric control or measurement is another resource.

For the actual thermal construction the conserved bare operator is the
ROUNDED sum. Apply (D11) to q_d. The residual interaction correction
permits intrabin changes; it does not create interbin q_d coherence.

Equation (D8) places the simulated spatial state in a zero-energy helper
dictionary, not on the original Q-bearing spatial degrees. Assigning Q
to those helpers after the proof would change the physical Hamiltonian
and invalidate its energy accounting. The archive channel is real in the
declared device; the original spatial-state preparation remains open.

## 6. Resource bounds and falsifiers

The new ready helper uses ceil(log2 g)+5 zero-energy qubits; its raw
dimension is 2^(ceil(log2 g)+5), not 26g. Input I, selector and occupied
archive use respectively ceil(log2 a), c and five admitted qubits.
The full five-qubit memory/archive SWAP specifies the invalid-code
extension too. Two additional ready bits are a completion flag and pointer.
All compiler scratch and routing bits are counted in the next note.

The exact matrices P_load,D_dec,V_sel and their elementary rotations
are supplied coupling specifications. Their computability, finite
manufacturing precision and perturbation tolerance are not derived.
No large matrix or expanded circuit has been calculated here.

Falsifiers include a missing Schmidt component in G, a nonunitary
completion, a failure of (D8) for correlated inputs, losing old archive
contents, leaking a selector record outside (D9), or treating the
degenerate decoder dictionary as physical preparation of the original Q.
