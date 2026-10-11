# Fixed calcium-ion waveform: approximation audit over the whole pulse

PUBLIC NON-CANONICAL; conditional L1 model, theory and numerics only.

The predecessor's nominal pair gate closes its modeled motion at 500
microseconds. That endpoint alone does not test the linear optical-force
approximation or the omission of counterrotating terms. This probe holds
both previously constructed angle waveforms fixed and examines the entire
trajectory of all 25 active electronic states while five protected ions
have exactly zero electronic response.

The comparisons are: RWA harmonic force, its declared two-frequency linear
parent, and a Duhamel estimate for the full sinusoidal optical potential
along the latter's Gaussian trajectories. Seven-mode harmonic confinement,
ideal carriers and ideal protection remain assumptions. The optical parent
is explicitly selected, not uniquely reconstructed from the old model.

- PREREG.md freezes inputs, workload, thresholds and outcome semantics.
- DERIVATION.md states the conditional Hamiltonians and analytic bounds.
- EXACT-DESIGN.md defines the scope of the rational verifier.
- input.json contains the small immutable selection of predecessor data.
- verify.py is the independent exact audit used by repository CI.
- trajectory.cpp and numerical_run.py implement the floating campaign.

Before the first run these files and SOURCE_SHA256SUMS must have a public
immutable commit and byte-identical public readback. Static compilation is
permitted earlier; executing the verifier or numerical programs is not.

After pinning, from the repository root:

```sh
python3 probes/P-U-CA40-TRAJECTORY-VALIDITY-1/verify.py
```

Build the scanner outside the checkout with the preregistered GNU C++ flags,
then call `numerical_run.py --binary ABSOLUTE_BINARY --output NEW_DIRECTORY`.
The runner reads input.json beside its own source. The exact compile command,
pin and execution records are provided by RUN.md after completion.

The exact audit does not certify floating answers. Analytic intersample
inequalities evaluated in ordinary floating arithmetic remain numerical
estimates, without a rigorous roundoff enclosure. Large conservative bounds
can leave a question open; only the stated lower witnesses prove a threshold
violation in their declared comparison. An RMS Lamb-Dicke diagnostic does not
bound the support of a thermal state.

The dark protected electronic factor is an explicit Hamiltonian assumption
and remains independent of motion on the other coordinates. It preserves
protected source/reference states in this auxiliary block; it does not
restore an unknown coherent source after a full informative contact leaves
distinguishable receiver records. No physical experiment, microscopic optical
power calibration, total work account or Canon promotion is claimed.
