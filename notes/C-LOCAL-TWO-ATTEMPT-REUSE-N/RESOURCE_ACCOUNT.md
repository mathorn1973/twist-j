# Two attempts: locality, preparation, retention and consumed stock

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1769. The frozen source is PR #1768 at
`811daddc3b2f085ee5bc6f50261ac95a4c11fe44`.

The three companion proofs compose into one finite static local law.
It exports two quantum records, replaces the working core after each
attempt, and returns that core to its original physical sites. The
first saved output remains available through the first replacement
and the second attempt. The statement includes failures and arbitrary
correlations of the three admitted inputs with a passive reference.
It is a conditional existence result with a very large resource count.

## 1. What the single Hamiltonian implements

Use the definitions and explicit coordinates in LOCAL_CONTROLLER.md.
Its full raw generator is the positive operator

    H_local=Q+H_hist.

It is time independent. Its outer launch, transport, program gates,
exports, replacements, return transport and holding tail all belong
to that same generator. The old H_D occurs through local gate matrices
approximating its endpoint unitary; it is not also left running as a
second uncontrolled interaction on the core. The new law does not
claim the old intermediate continuous trajectory.

Every site is a qubit at a distinct integer point in three dimensions.
The prospective bounds in the unchanged CONTRACT.md are met by the
listed terms:

| Quantity | Bound or fixed choice |
| --- | --- |
| Sites in one interaction | At most 9 |
| Manhattan interaction radius | At most 256 |
| Terms incident on one site | At most 64 |
| Norm of one listed term | At most J_* |
| Frozen energy cap | J_*=E_*+g_D+d |
| Outer propagation scale | g_out=J_*/4 |

E_* is the largest physical onsite gap of the frozen core, including
its fuel. These scales are fixed before increasing the product depth,
number of copies or cursor length. Exact local matrices, spectra and
couplings remain supplied data. The strength cap does not imply a
robust or economical manufacturing prescription.

LOCAL_COMPILATION.md supplies the primary full-raw instruction word:

    M=2^121(K_D+1)^4,
    P_0=2M(2K_D+1)+14+4S,
    P_0<=P<=P_0+3,       P even.

The padding arranges odd latch-export stages and the correct return
orientation. It does not alter the frozen error goals. Each run has
operator error below 2^-120; both runs together have error below
2^-119 on any joint input and reference. Sitewise transport, export
and replacement are exact full-space SWAPs. The old onsite-Q phases
are included in the primary word, so this is a literal raw operator
comparison, not only an equality on thermal marginals.

## 2. Counted geometry and latency

Let X,Y be the coordinate spans of the complete old S-qubit core,
including its old clock, donors, launch lead and tail. Define

    P_x=8X+4,               P_y=8Y+2,
    F_num=(P_x+9)(P_y+9),   R_num=(P_x+5)(P_y+5),
    B_0=P(F_num+R_num+14)-1,
    B=max{512,B_0},        L_c=5B,        K_out=10B.

The proof specifies every cursor vertex, not only this upper bound.
The first export is followed by a detour adding exactly 4B edges;
the completed return is followed by a 5B-edge tail. There is one
thermal outer fuel, one sink and one completion latch. Virtual node
zero is not a further physical cursor. The exact total is

    S_new=(3S+14)(P+1)+K_out+3,
    dim H_raw=2^S_new.

Three full core banks and two seven-site output channels have copies
in all P+1 layers. This includes unused output copies, dirty future
copies and all displaced contents. Returning the three core banks
restores the future core-copy contents to their original order; no
such restoration is claimed for all unused output-copy junk.

The physical window scale follows from this size at fixed g_out:

    T_hold=pi hbar(K_out+1)/(3g_out)
          =4pi hbar(10B+1)/(3J_*).

The source parameter tau specifies a target gate matrix and is not
the duration of the larger apparatus. Adding sites and instructions
increases T_hold. No interaction is strengthened to hide that cost.

## 3. Complete initial state and two temperatures

Write S=C_c+H_h+Z for the old cold positive-gap, hot and zero-gap
site counts. Layer zero contains the active core and two full fresh
cartridges, each with its actual thermal hardware. Their fifteen-site
information inputs I_0,I_1,I_2 have an arbitrary joint admitted state
rho_(I_0,I_1,I_2,R). The hardware is initially independent of that
state. I_2 is the counted next input; it can be correlated with both
earlier inputs and the reference. It is not called a Gibbs resource.

All positive-gap core copies in later layers are cold. Their spectra
are the same as those of their corresponding core sites, including
copies of old hot donors and old fuel. Every new zero-gap factor is
the genuine Gibbs state I/2. In particular, the output archive and
pointer destinations are mixed and need not be blank. The exact counts
are

    H_new=3H_h+1,
    C_new=3C_c+3P(C_c+H_h)+2(P+1)+K_out+2,
    Z_new=(P+1)(3Z+12),
    H_new+C_new+Z_new=S_new.

The forty-five information sites are already included in Z_new. All
other counted factors are independently prepared Gibbs states at the
two declared temperatures. Retain the old beta_h. After fixing every
dimension, choose the common beta_c to satisfy

    beta_c d>=[120+ceil(log_2 C_new)]ln 2.

The old source bounds hold at this colder permitted choice too. No
instruction or dimension depends on beta_c, so the choice is not
circular. The probability of any cold excitation is below 2^-120.
Those excitations remain in the actual state and in the Hamiltonian's
raw domain; the proof bounds their effect rather than removing them.

For comparison with the two ACTUAL thermal core channels, leave the
three original packages and all future core copies actual. Only the
outer sink/cursors/completion and all output-copy latches need a zero
comparison. Their total error obeys

    eta_ctrl<=[K_out+2+2(P+1)]exp(-beta_c d)<2^-120.

This includes a fixed output latch before its transported contents
arrive. Omitting such a site would allow an uncounted false read.
An exact permutation transports arbitrary future-copy contents, so
no extra pure routing bank is being hidden in this error definition.

Preparation is a specified two-temperature product boundary condition,
not equilibrium of the full interacting H_local. Its nonstationarity,
all thermal entropy, bare energy, full interacting mean and variance,
and finite capacities are explicit in LOCAL_CONTROLLER.md. If S_info
is the entropy of the joint information state, the apparatus entropy is

    S_initial=S_info+(Z_new-45)ln 2
                       +sum_(positive-gap u)h_2(p_u).

For a state including R, use the actual information/reference entropy.
There is no free purification or fresh bath between instructions.

## 4. Joint output, first-record lifetime and one launch

Let E be the complete actual thermal single-core output channel,
including accepted, rejected, dormant and defective branches. Let
Omega_T be its fresh hardware state. The exact abstract endpoint,
after discarding only the displayed reduction's spent systems, is

    Xi=Omega_(T_D) tensor
       (E tensor E tensor id_(I_2,R))(rho).

The saved O_1,O_2 are fixed physical blocks. D and its I_2 input are
back at their original physical sites. Fresh hardware T_D factors
from the records and reference; I_2 need not factor. Complete reset
has this structure even for the approximate local run gates. The
discarded systems remain present as physical spent stock and junk.

The one outer fuel has gap 3d and activation probability

    p_out=1/(1+exp(3beta_h d))>=1/3.

It controls the entire word once. Both E channels already contain
their inner thermal launches. The full joint acceptance probability
is not the product of two separately quoted apparatus successes.

At t=T_hold/2, conditional on outer activation, the first export is
complete and reset one has not started with probability greater than
1-2^-128. Every later forward instruction leaves the fixed first
output untouched. Its completed-export weight stays at least this
large from T_hold/2 through 2T_hold, including the reset and second
run. This is a history-weight bound; an accepted first record also
requires that inner attempt's accepted event. It is not a near-unit
unconditional detection probability.

For every t in [T_hold,2T_hold], the physical outer completion latch
F selects the completed tail with ideal weight p_out w(t), where
w(t)>1-2^-128. TWO_USE_CHANNEL.md proves

    p_comp,actual>=p_out w-eta_ctrl,
    D(rho_comp,actual,Xi)<2^-96.

The comparison is one joint state of both outputs, restored original
hardware, I_2 and R. Merely seeing two outputs does not certify that
the subsequent reset and return are already finished; F supplies that
condition without measuring a hidden clock index.

For the stronger event that F and both output acceptances are true,
the same proof compares with the joint ideal-ready instrument and gives

    p_both,actual>1/12000000000,
    D(rho_both,actual,Omega_T tensor rho_both,ideal)<2^-67<2^-60.

The denominator comes from a uniform single-use lower bound applied
conditionally to the correlated second input, and one shared outer
activation. It does not assume independent information inputs. No
single-use unwanted-band bound is imported under this stronger joint
selection without a separate proof.

At 3T_hold the clean outer history returns, undoing exports and
replacements too. Each saved read probability is then at most
eta_ctrl. Permanent closed retention is excluded by the predecessor's
general result. This construction supplies a finite lifetime under
the exact law; perturbation tolerance is not established here.

## 5. What is reset and what is consumed

Both complete S-site replacements run even when a source attempt is
rejected or dormant. They consume two fresh hardware/input packages
in addition to the initially active package. The next input in the
second cartridge is retained in D; it is not generated by the reset.
The spent cartridges retain previous hardware states, unused old
output contents and their correlations. The two saved quantum outputs
occupy separate seven-site blocks. No unknown quantum archive is
copied or erased to produce a nominally blank core.

After final replacement the working hardware is usable in the
specified state. That does not make the ENTIRE apparatus a renewed
cyclic resource. Its outer controller is on its holding history;
its two output records, spent cartridges and other junk differ from
their initial states. The exact later outer return removes the records
rather than supplying a fresh successful cycle with retained outputs.

A further pair of retained attempts needs another accounted schedule
and enough fresh cartridges, output capacity and control resources, or
a separately justified regeneration process. The present theorem
does not implement that process. Repreparing a spent product of Gibbs
hardware while retaining records must also handle its correlations.
If initial disjoint resource blocks B_a are Gibbs at beta_a, global
unitarity gives the exact entropy identity

    sum_a beta_a Delta E_a
      =S(X)_initial-S(X)_final
         +I(X:B_1:...:B_m)_final
         +sum_a D(rho_Ba,final || gamma_Ba),

when X and those blocks initially factor, and the block energies are
the specified bare onsite energies. Here I is total correlation and
logarithms are natural. This follows by expanding each Gibbs relative
entropy and conserving total entropy. It includes whatever systems,
including the reference when appropriate, are assigned to X. It is
an account of a proposed regeneration process, not proof that the
present local law performs one, nor a universal heat-per-bit claim.
Interaction and switching energy would need their own account if
that new process changes the law.

For the present unmeasured static evolution, rounded Q and the complete
occupation budget C_all are conserved. Every copied source/fuel
residual is kept:

    E_phys=Q+R_payload,     H_int=H_hist-R_payload,
    0<=R_payload<=d C_all,
    -d C_all<=U_t^*E_phys U_t-E_phys<=d C_all,
    <C_all>_initial<1+2^-120.

The bound holds once for the full unconditioned state at all times.
It is neither accumulated once per local gate nor automatically valid
after selecting two accepted records. Removing the counterterms
would change the generator and invalidate the stated construction.

## 6. Evidence boundary

The new result composes analytical local compilation, an explicit
finite geometry, a counted thermal launch and a joint two-use channel.
The inherited locality, thermal and reuse layers remain unaccepted
conditional inputs until their separate independent review. The
new successor likewise requires independent mathematical review.
Same-session cross-reading and repository CI do not supply it.

No new scientific executable, expanded circuit, matrix simulation or
numerical experiment was run. Canon, registry, predecessor files and
workflows are unchanged. This existence proof does not establish
economical resources, material robustness, native derivation, an
individual-outcome selection law or unlimited replenished operation.
