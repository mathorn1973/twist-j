# Independent written-proof and physical-scope review

PUBLIC; pre-pin review of P-QDD-ION-SIDEBAND-WRITER-1, lock
[#1091](https://github.com/mathorn1973/twist-j/issues/1091).
Date: 2026-09-20. Reviewer: separate ion_independent_review agent.

**Disposition: no blocking gap found in the stated ideal-model theorem.**
This disposition does not certify laboratory feasibility, apparatus execution,
physical native U, or the Canon's L1-to-L5 obligations. Hardware status remains
**NOT_RUN**.

## 1. Independence and material reviewed

I read PREREG.md, PULSE-PROOF.md, CHART-AND-CYCLE.md, APPARATUS.md and
PULSES.tsv. I independently followed the written Hamiltonian and pulse
identities before reading any verifier. I did not read verify.py and did
not run a scientific computation, pulse simulation, or hardware experiment.
This is a written-proof review by a separate agent, not a claim of blind
discovery or a second experimental measurement.

I also checked the relevant physical precedents directly in the primary
papers linked below. Those experiments supply precedent for the interaction
family and controller. They are not measurements of this proposed sequence.

## 2. Pulse signs and the coherent conditional shift

The Hamiltonians in PULSE-PROOF equations (1)-(2) are Hermitian with the
stated convention. Exponentiating an addressed two-state block gives the
two conjugate phase factors in equations (3)-(4). Replacing a negative pulse
area by a positive area and optical phase shifted by pi gives the inverse
operation; no negative duration is needed.

For the chronological carrier sequence R_v(-pi), R_u(pi), R_v(pi), I obtain

    |u> -> -|v>,   |v> -> |u>,   |g> -> |g>.

The auxiliary phase is therefore fixed, rather than discarded. The blue
version has the same action on the relevant one-phonon logical states.
In the ordered chain (0,1,2,3,4), input 0 accumulates four minus signs,
whereas each other input uses the positive direction of one exchange.
Every output of the resulting X^(-1) has phase +1. Repeating the same
argument in the order (0,3,1,4,2) gives the local X^2 with phase +1.

On the selected source level, V=B(pi)R(pi) supplies a minus sign and one
phonon. The target inverse cycle leaves that phonon available for V^dagger,
whose second minus sign cancels the first. Other source levels remain in
the common vacuum and all target blue pulses are dark. Thus G supplies
exactly X^(-1) on the selected sector, the identity on its complement, and
one common final motional state and phase. Reversing the pulse order and
phases gives its inverse; changing the addressed source level gives G_c.

This establishes the operator identity on all logical pair basis vectors
with their phases. Linearity then establishes the same isometry on arbitrary
superpositions, correlated port inputs, and states entangled with the archive
or another reference. It is not an inference from populations alone.

I checked the chronological PULSES.tsv against the signed sequence in the
proof: twelve carrier pulses for X^2, then two source carrier and fourteen
blue pulses for G. Its stated writer count is 28 pulses, evenly divided
between carrier and blue pulses.

## 3. The oscillator has not been silently truncated

The proof tracks occupied invariant subspaces throughout each continuous
pulse, not merely at pulse boundaries. The selected source is transferred
from logical D with motion zero to g with motion zero and then to logical
D with motion one. During target blue pulses the only coupled occupied
pair is |g,0> and the currently addressed |j,1>. Other occupied logical
levels are dark. At the end of each target triple, its auxiliary population
is empty and the initial motion for that triple is restored.

The source remains in D during those target pulses; it is not simultaneously
driven. The final inverse source pulses return the mode to vacuum. Hence
no addressed pulse encounters |g,1> or |j,2>, including midway through a
pulse and for coherent superpositions. This justifies the vacuum-doublet
calculation under the declared Hamiltonian. It does not remove the higher
oscillator sectors from the physical Hilbert space, prove a hot-mode gate,
or suppress omitted off-resonant and heating effects.

Each G block ends with the same vacuum, so its reuse in the archive compiler
is justified. Local carrier blocks do not excite motion. The proposed model
rejection for a nonvacuum initial mode is a scope check, not a theorem that
all possible hot-mode implementations fail.

## 4. Negation, native chart and the archive cycle

The two initial 2pi carrier pulses in NEG give a minus sign to logical
levels 1 and 2, respectively, and net phase +1 to g. The signed exchanges
Q_(1,4) and Q_(2,3) then produce the phase-free logical negation. Omitting
those two corrections would preserve the population permutation while
giving the wrong coherent operation. Each 2pi pulse also has its full
physical area and duration; counting it as one pulse is not counting it
as a pi-duration operation.

The native comparison uses twenty distinct states T_e Y_h(n). Source
invertibility on the common stable branch separates h, and the port value
separates e. Consequently E_n is an isometry onto a 20-dimensional subspace,
with hardware label h-1 in {0,1,2,3}. Adding an arbitrary five-level archive
gives dimension 100, faithfully contained in the 125 logical dimensions.
The extra hardware source label 4 has the explicitly declared response 2;
it does not assert an extension to native h=0.

The inherited transport U_n T_e=T_(-e) U_n gives a single logical NEG per
step in this moving chart. The chart absorbs the free source trajectory and
reference port; it does not make the physical ion source evolve by native U.
The all-waiting-time statement follows by induction from that transport
identity, rather than from a finite run of the actual controlling sequence.

The chronological arithmetic y+=x; x-=y; y+=x; x=-x is exactly SWAP.
Each SUM uses six controlled cycles by the balanced representatives
1,2,-2,-1. Therefore SWAP has 252 blue and 44 carrier pulses. Adding
the writer, one NEG for each executed waiting step, and the two output
NEG operations for odd waiting gives exactly

    blue:    266,
    carrier: 58 + 8 k + 16 (k mod 2).

With epsilon=(-1)^k, the full map is

    (s,e,m) -> (s, epsilon*m, e+f_hw(s)).

Only e=m=0 gives a restored ready port and the unpolluted record f_hw(s).
For general inputs, the old archive content returns to the port and the
initial port error remains in the archive. Thus the construction neither
erases information nor hides the preparation conditions. The ideal pulse
counts exclude real compensation, preparation, readout and reset operations.

## 5. Physical provenance and limitations

[Meth et al., version 2, Appendices A and G](https://arxiv.org/html/2310.12110v2)
support calcium multilevel storage, the auxiliary-ground-state sideband
interaction, removal of the shared motional excitation, and the need for
buffer ions and phase/cross-talk management. Their reported device does
not establish performance of this proposed writer or its much longer
archive compilation.

[Schindler et al., Sections 1.2 and 2.2-2.4](https://arxiv.org/pdf/1308.3096)
support the controller chain, laser manipulation, cooling and fluorescence
readout. The proposed apparatus must still supply its own compatible
calibrations, addressing geometry, timing, detector qualification and raw
records. Parameters from different experiments cannot be assembled into
a purported measured device.

The logical writer is exact only in the stated effective interaction picture.
Free Zeeman phases and spectator light shifts require independent calibration
and compensation. Pulse timing and phases come from external electronics and
laser references, with external energy supplied to the ions. Treating those
fields classically does not prove a clean finite quantum controller or defeat
the earlier clean-energy obstruction.

The separate engineering fields explicitly mark an intervention comparison
and checkpoint modification. They do not claim feeds_U=false, submit an
accepted canonical decoder profile, or derive an oscillator and pulse program
from J. Returning the final checkpoint to its free endpoint does not make
the intermediate actuation a passive readout.

Archive detection must distinguish valid outcomes from dark leakage and
failed acquisition. The subsequent macroscopic record, persistence, and
source-preserving reset require material evidence. Retaining HIGH coherence
does not retain an uncorrelated LOW/HIGH source after measurement, and repeated
readings of one source are not independent preparations.

The profile correctly leaves full-sequence coherence and heating budgets,
hardware access, numerical experimental tolerances and actual operation
unresolved. A future hardware preregistration must freeze those quantities
before acquisition. The present exact theorem and proposed test sequence
do not establish the physical occurrence law, laboratory readiness, apparatus
family completeness, or a native physical realization of U.

## 6. Disposition

The written derivation, fixed pulse list and physical scope are mutually
consistent under their explicit premises. No mathematical correction was
required by this review. Exact verifier execution and both public architecture
replays remain separate gates, and cannot substitute for the future physical
experiment.
