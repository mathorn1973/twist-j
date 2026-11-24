# Exact P=0 scattering result

Candidate: C-W-P0-SCATTERING-N. Issue: #1840. Date: 2026-10-30.
Status: NON-CANONICAL / L1 / analytical candidate-T plus candidate-C audit.
No Canon, registry, gate, native-U or physical-status change.

## Positive result in the unchanged walk

The complete two-open-channel S matrix (PROOF.md,13), including phases
and equal-flux normalization, is derived from the existing four-channel
contact-after-streaming W at P=0. Its direct substitution passes all
2560 frozen original-operator equations. The exact reflected/transmitted
fractions obey R+T=1 and have the closed scalar form (16).

On lambda=exp(i theta), cos theta=(cos q-4)/5, there is exactly one
transparent point in the open propagating band:

    lambda_*=exp(4pi i/5)=j^2=J-1,
    cos(q_*)=4-5phi/2,
    R(q_*)=0, t(q_*)=exp(2iq_*).

The equality to J-1 is only the declared axiom J=1+j^2; it introduces no
new dynamics. Mechanism: lambda_*^2=gamma, so the contact transfer equals
the inverse free transfer. The point has nontrivial transmission phase.
The opposite eigenphase band has no transparent point at the same g.

## Certified stationary reflection intervals

Every interval below has width exactly1/10^9. The two columns are the
SAME contact with different eigenphase branches, not different couplings.
The q variable is relative momentum; at P=0, single-particle k=q/2.

| q | R on lambda=exp(i theta) | R on lambda=exp(-i theta) |
|---|---|---|
| pi/6 | [540043260,540043261]/10^9 | [999422264,999422265]/10^9 |
| pi/3 | [165495405,165495406]/10^9 | [997123437,997123438]/10^9 |
| pi/2 | [1416558,1416559]/10^9 | [990968106,990968107]/10^9 |
| 5pi/6 | [585936209,585936210]/10^9 | [936052225,936052226]/10^9 |

The first column explains the shape of the reported approximate packet
values. It does not reproduce the unseen packet code or certify its
finite-time, width, band purity, flat component or detector errors.
One cannot use a scalar sine-shell point without its phase/mode preparation
to predict the scattering. The second column is an exact countercheck.

## Bound-state and arithmetic boundaries

The known compact state delta_0 A remains a reducing eigenstate with
lambda=gamma. Its population is exactly conserved. None of the two
incident propagating modes can fill it from zero at P=0. This is NOT a
refutation of the bound-state branch, its curvature or the extra-carrier
capture apparatus. Bare stationary scattering and capture are different.

Equal norms always make the arithmetic elastic alternative a swap, so the
same-species result supplies no test of the unequal-norm prime obstruction.
The cited prime spectral addresses involve absolute Galois embeddings
and prime-dependent mass normalization; they are not the unchanged
additive O_+ chart. The literal chart obstruction of #1839 is untouched.
The group-speed bound1/sqrt5 is not the strict finite-step support cone.

No second species or new contact was introduced. No many-body completion,
physical occurrence, Born sampling derivation, apparatus, clock, empirical
prediction or native-U realization is supplied. An unequal-species test
would still need an explicitly selected coupling and a compatible state
map, rather than only a second numerical mass parameter.

## Executions and disposition

All six frozen audit groups passed on first execution on both x86_64 and
aarch64; respective stdout is byte-identical. Source pin and run metadata
are in RUN.md, output in EXPECTED.txt. Proof and finite audit are separate.
This is reproducibility, not independent review or public T status.
All frozen source bytes remain unchanged. No falsifier fired.
