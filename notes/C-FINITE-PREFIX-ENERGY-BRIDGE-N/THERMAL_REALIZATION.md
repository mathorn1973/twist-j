# Local thermal realization of the selected archive channel

**NON-CANONICAL, L1; conditional analytical construction, not independently
accepted.** This instantiates the compiler and controller at frozen
`811daddc3b2f085ee5bc6f50261ac95a4c11fe44`; it changes no source proof.

## 1. Exact finite targets and input inventory

Simultaneously diagonalize q_d and r=q_phys-q_d on E. Original label i
has rounded charge j_i and residual r_i in [0,d]. Use descending charge
order, put the chosen e_* first among maximum-charge labels, and insert
helper labels at missing intermediate heights, with residual zero. Then

    ell<=D+v,       v=b_+-a_-<=m-1,
    B=max(1,v),    c=ceil(log2(N+1)),
    f=ceil(log2 a)+ceil(log2 g)+5+5+c+2,
    b_size=ell+B+f,       n=16 b_size,
    u=ceil(log2 a)+5+c,   A_ready=n-u.                (T1)

The two five-bit factors in f are helper memory and occupied archive.
The last two bits are a ready flag and pointer. Only u bits are admitted
information: I, occupied A, and selector C, jointly arbitrary with R and
restricted to their valid codes. Their preparation is not attributed to
Gibbs cooling. Every other Z bit, including helper G,M and all compiler
workspace, must be prepared. Future Z rows remain genuine I/2 Gibbs
inputs and are transported as in the source controller.

There are three interleaved qubit tracks E_i,X_i,Z_i. All E sites have
gap d. X sites have physical gap d(1+j_i)+r_i; pad them by the nearest
endpoint height and residual zero. All Z sites have zero gap. Reserve
the first five Z sites for the archive, place the active label/battery
segments starting at cell 6, and reserve the final two Z sites for flag
and pointer. The common one-label offset is mu=d and is counted.

The main word has two targets and a final pointer instruction:

1. Gamma(W), with the admitted flag flipped to one after the decoder,
   identity on invalid semantic codes. Every primitive and routing path
   excludes the protected archive prefix and the final pointer site.
2. The flag-controlled full five-bit helper-memory/archive SWAP.
3. The final CNOT from flag to pointer, after scratch cleanup.

The flip is a unitary X on the ready flag, not a reset. On dirty inputs
all gates retain their full unitary action. The flag marks completion of
the selected simulation, NOT successful capture or an individual event.
The ideal admitted completion probability is p0=1.

The sharp lift is identity off complete fibers and semantic codes.
Its nontrivial label action is within one-excitation sectors. The frozen
conserving compiler therefore applies: every elementary gate preserves
rounded data energy and label number on the entire raw space, with at
most four data sites. On the prepared-workspace input its selective
controls and scratch are restored. Dirty workspace retains a complete
conserving unitary but need not implement the intended semantic target.
The two targets, pointer gate and parity padding fit conservatively in

    J<=20000000 b_size^4 4^b_size,                    (T2)

using the source's three-target allowance. No expanded circuit is claimed.

## 2. Thermal reset, one launch and exact size

Fix an integer accuracy parameter k>=8. Set

    r_reset=2(k+ceil(log2 A_ready)+1),
    xi=A_ready (2/3)^r_reset < 2^(-k-1).             (T3)

There are A_ready fresh hot/cold gap-d donor pairs in each reset round.
The full three-qubit reset exchanges |1,0,1> and |0,1,0>, leaving the
other six states fixed. Used donors remain present. On the cold-ground
comparison input, its reference-uniform error is xi, from the complete
replacement-channel proof in the frozen source.

Put s=r_reset+J, inserting an identity before the last CNOT so s is odd.
Use data positions (4c',2t), c'=1,...,3n, t=0,...,s; reset donors lie
at (4c'-1,2t),(4c'+1,2t). Let W_row=3n and

    b_path=s(4W_row+6)-1,
    q=4(3*6-1)=68,
    L_c=q+4+b_path+2p_pad >=512,
    K=2L_c,                                         (T4)

where p_pad is the least nonnegative integer satisfying the inequality.
These are the source controller's exterior lead, alternating rails,
guarded completion and equal-length completed tail. The right guard is
4W_row+4, beyond all donors. The seed at active cell 6 is distinct from
fuel, sink and initial cursor. Ordinary transfers have identical spectra;
all original active factors arrive in the final row. In particular C
and A are fixed physical final-row registers throughout the completed
tail; they are not merely labels that move to an unspecified bank.

Every term has at most seven sites, Manhattan radius at most 16 and
incidence at most 64, as in the source proof. Replacing fifteen admitted
bits by u only changes the nominated reset columns and their count;
none of those geometric bounds depends on which Z columns are reset.
All physical site dimensions remain two.

The exact total and cold-site counts are

    S=3n(s+1)+2 A_ready r_reset+K+3,
    C_c=2n(s+1)+A_ready r_reset+K+2,
    N_hot=A_ready r_reset+1,
    N_zero=n(s+1),          dim H_raw=2^S.           (T5)

The final three sites are fuel, sink and latch. The u admitted information
bits replace u of the row-zero Z Gibbs factors; all remaining zero-gap
sites have I/2. Battery and label padding, all future rows and every
physical cursor are included, once each.

## 3. Actual temperatures and full Hamiltonian

Let G_fuel=(b_++4)d. The fuel physical gap is G_fuel+r_*.
Choose

    beta_h(G_fuel+r_*)=ln 2,
    beta_c d=(k+1+ceil(log2 C_c))ln 2.               (T6)

Every noninformation input is an independent Gibbs state for its stated
physical onsite spectrum, at beta_h for fuel and hot donors and beta_c
for every charged cold site. These are two-temperature resources, not
a Gibbs state of the full interacting Hamiltonian. The fuel excitation
has probability 1/3. Hot gap-d donor excitation p>=1/3. Cold defects obey

    eta=1-product_(cold i)(1+exp(-beta_c e_i))^(-1)
         <=C_c exp(-beta_c d)<=2^(-k-1).             (T7)

The count is fixed before beta_c, so no circular temperature/site choice
is used. Zero-gap qubits remain I/2 until reset; low temperature alone
does not prepare them.

For clarity the complete law is restated. H_D is the rounded energy of
all E/X data rows and all reset donors. With fuel h, sink c0, latch L,
and physical cursor qubits C_j, put

    H0=H_D+G_fuel n_h+d n_c0+d n_L
        +2d sum_(j=1)^(L_c-1)n_Cj+d sum_(j=L_c)^K n_Cj.

The launch partial isometry is

    X0=s_h^- s_c0^+ s_X*^+ s_C1^+,
    Pin=X0*X0,    Pout=X0 X0*,    D0=Pin+Pout.

It exchanges |1,0,0,0> and |0,1,1,1> at the four launch sites. Their
actual physical energies both equal G_fuel+r_*.
At each other edge j use Xj=s_C(j+1)^+ s_Cj^- G_j and
Dj=n_Cj+n_C(j+1), where G_j is the full raw instruction. At the
completion edge j=L_c-1 insert s_L^+ in Xj and retain this same Dj.
Define V0=Pin, Vj=n_Cj for j>=1 and, with fixed g0>0,

    a_j=g0 sqrt((j+1)(K-j))/(K+1),
    v_j=g0-a_(j-1)-a_j>=0,       a_(-1)=a_K=0,
    Hprop=sum_(j=0)^(K-1) a_j(Dj-Xj-Xj*)+sum_(j=0)^K v_j Vj,
    H=H0+Hprop.                                      (T8)

Every term is positive: ordinary single-cursor blocks are positive
unitary off-diagonal 2-by-2 blocks, double-cursor sectors have the stated
positive diagonal, the launch block is a positive exchange block, and
completion uses a contraction s_L^+. Thus positivity includes all
multiple-cursor, dirty-workspace and invalid-code sectors.

All terms commute with H0 and C_charge=N_X+n_h, where N_X counts every
label excitation in every row. With

    R_all=sum_(all rows,i) r_i n_Xi+r_* n_h,
    E_phys=H0+R_all,       H_int=Hprop-R_all,           (T9)

one has 0<=R_all<=d C_charge. Hence the complete unconditioned drift is

    -d C_charge<=U_H(t)* E_phys U_H(t)-E_phys<=d C_charge.
                                                            (T10)

The negative residual term is part of the declared interaction and may
not be dropped. This is an inclusive device account; it is not energy
conservation of an independently prepared original spatial source.

Every onsite gap is less than Delta+5d and every propagation summand
has norm at most g0. The conservative individual-term bound
J_loc=Delta+5d+g0 is independent of N and the number of sites.

## 4. One completed joint channel and finite window

On the all-cold-ground component the fuel-ground branch is dormant.
The excited branch starts exactly one history and cannot relaunch at a
later node. The full raw unitary word, including reset donors, determines
its orthogonal histories. Its clock restriction is

    Hprop=g0 I-[2g0/(K+1)]J_x,         spin J=K/2.

Thus its node probabilities are Bin(K,sin(theta)^2), with
theta=g0 t/[hbar(K+1)]. Choose the physical latency from the fixed g0:

    T_h=pi hbar(K+1)/(3g0).                           (T11)

Throughout [T_h,2T_h] the completed weight obeys

    w(t)>=1-(3/4)^L_c>1-2^-128.                      (T12)

At every completed node the C,A,R joint output is the same completed
channel. All branches of V_sel share the same history and H0 energy;
the clock does not record the chosen n. Its superposition is therefore
not silently replaced by a classical mixture.

The physical read predicate is Pi_read=n_L n_P. It rejects the dormant
branch even when its unprepared pointer is one. Let rho_ideal be the
joint C,A,R output of (D9) and occupied SWAP. The comparison component
and the retained thermal defects give

    p_read(t)>=(1/3)w(t)(1-xi)-eta,
    D_tr(rho_read(t),rho_ideal)
       <=xi+eta/[(1/3)w(t)(1-xi)].                    (T13)

These are the complete-instrument mixture bounds with p0=1, not a
capture success estimate. For k>=8, (T3),(T7),(T12) imply the simple
conservative consequences

    p_read(t)>1/4,
    D_tr(rho_read(t),rho_ideal)<5*2^(-k-1).           (T14)

For example w>511/512 and 1-xi>511/512 make the denominator exceed
1/4; subtracting eta<=1/512 still leaves p_read>1/4. The sharper
expressions (T13) remain the authoritative parameter-dependent bounds.

Every cold-defect branch evolves and may cause a false output; eta covers
it without postselecting a favorable preparation. No tail error is added
to the conditional clean output, since the latch excludes incomplete
histories. Increasing N changes the target, site count, temperature and
latency; it does not increase g0 to hide that cost.

At 3T_h the cold-ground comparison density returns exactly to its
initial state, including reset failures, because K is even and the
complete initial comparison commutes with H0. Therefore

    p_read(3T_h)<=eta.                                (T15)

This is unmeasured autonomous recurrence. External measurement changes
the evolution and needs a separately counted instrument and storage.

## 5. Energy, entropy, capacity and remaining resources

For all initial Gibbs factors their actual energy and entropy are those
of the declared gaps and temperatures. Put gamma_i=(1+exp(beta_c
[d(1+j_i)+r_i]))^(-1). Then exactly

    <C_charge>=1/3+(s+1)sum_(i=1)^n gamma_i.          (T16)

The unconditional mean drift in (T10) is bounded by d times (T16), not
by an accepted-ensemble energy. Rounded bare capacity and residual
capacity are

    E0max=(s+1)[nd+sum_(i=1)^n d(1+j_i)]
             +2 A_ready r_reset d+G_fuel+d(3L_c+1),
    Rmax=(s+1)sum_(i=1)^n r_i+r_*,
    Ephys,max=E0max+Rmax,
    0<=H<=[E0max+(2K+1)g0]I.                         (T17)

For an explicit interacting moment account, set

    Aprop=g0 sum_(j=1)^K n_Cj+g0 Pin+a_0(Pout-n_C1),
    M0=H0+Aprop.

The product thermal input is diagonal on every charged factor; admitted
information may be arbitrary in zero-energy factors. Distinct hopping
edges do not return the charged cursor/fuel/latch configuration, while
G_j*G_j=I. Consequently the source proof gives exactly

    <H>=<M0>,
    Var(H)=Var(M0)+sum_j a_j^2 <Xj*Xj+Xj Xj*>.       (T18)

These are finite local thermal expectations, not omitted interaction
energy. Only the four launch factors couple in Aprop; all other diagonal
thermal contributions are independent Bernoulli sums. The formulas count
the changed donors and every copy. Globally unitary evolution preserves
entropy and moves the old archive and reset information to retained
helper/donor states; those systems are never discarded physically.

Two temperatures, exact spectra and couplings, geometry, the input
product-state boundary and admitted information are specified resources.
No work cost for preparing that boundary from one equilibrium bath has
been proved. No finite precision, manufacturing or robustness claim is
made. Spectral basis vectors and original spatial geometry are represented
by a dictionary and exact couplings, not produced as original lattice
states. The source and battery reset of (D8) does not replenish helper
purity, spent donors or the clock, and (T15) prevents indefinite closed
storage. Those limits remain part of the result.
