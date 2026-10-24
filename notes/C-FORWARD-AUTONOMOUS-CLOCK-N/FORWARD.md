# Complete forward filter and its error contract

**NON-CANONICAL, L1, candidate-T.** This is a same-session analytical
continuation under [claim #1747](https://github.com/mathorn1973/twist-j/issues/1747),
not independent acceptance of the preceding capture construction.

The authority baseline is public main
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The explicit source and ideal
filter input is [PR #1746, PROOF.md at 01acc42b](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
Only the elementary filter and comparison statements below are rederived
here. Numerical capture bounds remain conditional on that candidate's source,
spectral and finite-front proofs.

## 1. Forward controlled steps suffice for the ideal filter

Let V be any unitary on the object Hilbert space, omega=zeta_5, and
F_(a,b)=omega^(ab)/sqrt(5), with a,b in {0,1,2,3,4}. Define

    B(V) = (F* tensor I) diag(I,I,I,I,V) (F tensor I).

This is a full unitary on the object and a five-state register, including
register inputs other than zero. Its actual object operation is controlled V;
F* is an operation on the register. No controlled V* occurs in this word.
For the initialized register, the geometric sum gives

    B(V)(|0> tensor psi) = sum_a |a> tensor K_a(V) psi,
    K_0(V) = (4I+V)/5,
    K_a(V) = omega^(-4a)(V-I)/5,  a=1,2,3,4.

Consequently

    sum_a K_a* K_a = I,
    H(V) := K_0* K_0 = (17I+4V+4V*)/25,
    I-H(V) = (4/25)(I-V)*(I-V),
    9I/25 <= H(V) <= I.

The adjoints in these effect identities describe norms, not additional
executed object instructions. Each fine-history operator is a polynomial in
V involving only nonnegative powers. All such operators and their adjoints
commute because V is unitary.

Run m elementary blocks with fresh registers. For a word w of length m let
A_w=K_(w_m)...K_(w_1). The all-zero word has effect H^m; the sum of the
effects of every other word is I-H^m. Now run n complete words, retaining
all mn registers, and reversibly write f(h)=1 iff at least one word is all
zero. The complete initialized map is

    S_f psi = sum_h |h> tensor |f(h)> tensor A_h psi.

The map writing f is a reversible XOR into a fresh bit, defined on both bit
inputs. Since the history kets are orthogonal, the effects are sums of
A_h* A_h, with no cross terms. Commutation permits grouping the n rejected
word sums. Thus

    S_f* Pi_(flag=0) S_f = (I-H^m)^n,
    S_f* Pi_(flag=1) S_f = G_(m,n)(V) := I-(I-H^m)^n.

This is a complete coherent circuit identity, not an assumption of
independent realized trials. The accepted vector is Pi_(flag=1) S_f psi,
not G psi or sqrt(G) psi. Erasing or coherently recombining the histories
would require a new argument and is not part of this construction.

For commuting unitaries V_R=T_R and V_W=z_g^(-1)W, the two register banks
likewise commute at the level of all object branch operators. Accepting iff
both program flags succeed gives precisely

    G = G_(32768,8)(T_R) G_(8192,8)(z_g^(-1)W).

There are D_R=262144 forward controlled T_R calls and D_W=65536 forward
controlled z_g^(-1)W calls, D=D_R+D_W=327680 fresh five-state registers,
and 2D auxiliary Fourier operations. The source loader and Boolean logic
are additional declared operations. The forward-only statement concerns
object evolution inside this filter; it is not a claim that every source
preparation gate is a power of W, nor a derivation from the original law.

## 2. Conditional composition with the finite source

Use the predecessor's fixed source, T native steps and final front test J_T.
Its claimed exact front identity has the form

    J_T U_rec^T psi_s = c_T W^T chi_s tensor |s+T,2>
                       tensor SWAP_(L,D) Xi,
    |c_T|^2 = q_T = (64/625)(16/25)^(T-1),

for every logical/reference vector Xi in L tensor D tensor R. The object
state chi_s is fixed independently of Xi. The filter and front test commute,
and the filter acts trivially on these logical registers. Hence the full
accepted vector is exactly

    c_T sum_(h accepted) |h>|1> tensor A_h W^T chi_s
                         tensor |s+T,2> tensor SWAP_(L,D) Xi.

Its squared norm is q_T <chi_s,G chi_s>. This equation retains every
accepted fine history and all old-memory/reference correlations. Rejected
source marks, fronts and filter histories remain in the complementary flag.
The marked basis loader multiplies this accepted vector by sqrt(2/5),
while its other source branches remain retained. The predecessor's spectral
estimates then imply, conditionally,

    p_basis > p_* := 1/20000,
    delta_ideal < delta_* := 50000/(99*2^29) < 1/10^6.

Here delta is the conditional object weight outside the nominated wider
bound-band projector. This document does not independently accept the
source's parity, spectral-gap or finite-front premises. These are L1 norms,
not empirical event frequencies.

## 3. An explicit energy demand, not a free register

Choose the auxiliary energy E_A=epsilon(I-|0><0|), epsilon>0. It has a
nondegenerate ground state and a four-dimensional excited eigenspace, not
five distinct energy levels. The exact final mean increase of one fresh
register is

    Delta E_A = epsilon <psi,(I-H(V))psi>
              = (4 epsilon/25)<psi,(2I-V-V*)psi>.

It lies between zero and 16 epsilon/25. If the object's selected energy H_S
commutes with V, the block leaves H_S unchanged. Unless V psi=psi, the
register increase therefore needs another account under the additive ledger
H_S+E_A. A declaration of unitarity alone supplies no such account.

There is also an intermediate demand: immediately after F on |0>, the mean
register energy is 4 epsilon/5. Controlled V preserves E_A, and the final
F* changes it to the expression above. Even B(I)=I does not make these
separately implemented intermediate Fourier gates energetically free.

For a nonselective elementary block, the adjoint channel fixes every
operator commuting with all K_a. In particular it fixes every bounded
function of the commuting V_R,V_W. Thus the final mean energy of all D
filter registers, before Boolean flag computation, is exactly

    epsilon <D_R(I-H(V_R)) + D_W(I-H(V_W))>,

evaluated in the pre-filter object state. The identity also holds for mixed
states and reference correlations. It is not a postselected energy account.
Loader, work-bit, clock and predicate energies are additional. The chosen
epsilon is a declared energy gap, not a derived physical calibration.

A useful restricted obstruction follows. Assume an energy-conserving unitary
with additive H_S+E_A+H_B, bounded H_S, [H_S,V]=0, and a fixed pure battery of finite mean
energy, and exact implementation of the pure full-history initialized map
B(V)(|0> tensor psi) for every object input psi after tracing the battery.
Purity and linearity force the final battery state to be independent of psi:
otherwise superpositions of inputs would lose the required coherence.
Energy conservation then forces

    epsilon(I-H(V)) = c I,

where c is the battery's fixed mean-energy loss. Hence a non-scalar V+V*
excludes this exact universal implementation under these assumptions.
This is not a no-go for the single fixed object source of Section 2, for
approximation, or for a different declared energy model. On a restricted
input subspace the same argument requires a non-scalar compressed energy
demand; varying spectator logical labels alone need not provide one.

## 4. Reference-uniform approximation and conditioning

At a common read boundary suppose the full normalized ideal and actual
vectors obey ||Phi_tilde-Phi||<=eta, uniformly including arbitrary reference
systems and all retained registers. An ideal spectator battery may be
included in Phi. Let Pi be the common acceptance projection, x=Pi Phi,
y=Pi Phi_tilde, p=||x||^2 and p_tilde=||y||^2. Contractivity gives

    |sqrt(p_tilde)-sqrt(p)| <= eta,
    p_tilde >= (sqrt(p)-eta)^2,  provided eta < sqrt(p).

Let Q be the unwanted object projection, commuting with Pi, and suppose
||Qx||^2<=delta p. Then ||Qy||<=sqrt(delta p)+eta and therefore

    delta_tilde <= ((sqrt(delta)+eta/sqrt(p))/(1-eta/sqrt(p)))^2.

The trace distance (one half of the trace norm difference) between
normalized accepted pure states is at most
eta/sqrt(p): project x-y orthogonally to the direction of y and divide by
||x||. Partial trace cannot increase this distance. All these conclusions
therefore retain the reference-uniform and reduced-state meanings.

For the conditional input bounds in Section 2 it suffices to have
eta<=1/6000000 to retain delta_tilde<1/10^6. The arithmetic is exact:

    50000*1030^2 = 53045000000 < 99*2^29 = 53150220288,
    sqrt(delta_*) < 1/1030,
    sqrt(20000) < 150,
    alpha := eta/sqrt(p_*) < 1/40000,
    (1/1030+1/40000)/(1-1/40000) < 1/1000.

The last inequality is equivalent to 41030000<41198970. The accepted weight
has the corrected bound

    p_tilde > (1/sqrt(20000)-1/6000000)^2 > 1/20002.

For the last comparison, use (1-1/40000)^2>19999/20000 and
19999*20002=400019998>400000000. The original strict 1/20000 threshold is
not automatically preserved by a nonzero approximation error. This generic
bound is not sharp for ENERGY.md's specified E-eigenstate source: its exact
diagonal-observable lemma preserves p_tilde>1/20000 for that source.

In particular, the separately proved one-battery estimate
eta<=sqrt(8Q/L), with positive integer energy bound Q and L=Q*5^22,
meets this contract without a numerical fit:

    sqrt(8Q/L) = sqrt(8/5^22) < 3/5^11 < 1/6000000,
    3*6000000 = 18000000 < 5^11 = 48828125.

This implication uses the stated joint-vector estimate; a bound only on
one marginal, one successful word or an unnormalized effect cannot be
substituted for it. The battery construction and its physical admission
must be assessed separately from this exact error transfer.
