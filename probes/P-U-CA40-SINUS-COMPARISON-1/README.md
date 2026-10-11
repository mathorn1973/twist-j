# Direct seven-mode sine comparison

PUBLIC NON-CANONICAL, conditional L1 mathematics and floating engineering.
Original work Apache-2.0, A. M. Thorn, 2026-10-11.

This probe continues P-U-CA40-TRAJECTORY-VALIDITY-1 with the same two pulse
arrays. It directly propagates the declared sine-potential remainder in
the moving frame of the full two-frequency linear oscillator solution.
It is a numerical model comparison, with no ion experiment or apparatus
admission. The three-branch panel does not cover every active input.

Read PREREG.md for the fixed campaign and failure rules, DERIVATION.md for
the Hamiltonian, projection and observable formulas, and EXACT-DESIGN.md
for the deliberately narrower exact verifier. Numerical and exact outputs
are separate. The input.json bytes are copied unchanged from the public
predecessor pin 604bad993830222ab8c34cee6f31a7a36043e350, where their SHA-256
is ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53.
The original upstream waveform construction is identified inside input.json.
linear_model.py preserves the prior preparation, exact-frequency integral,
and topology helper implementations with no scientific change.

Neither the waveform nor its preparation is optimized here. Protection of
the other five ions is the inherited exact-darkness premise. The complete
unknown-source/informative-record obstruction remains unchanged. The fixed
classical optical drive supplies no finite quantum work reservoir or complete
experimental energy account.

The complete source and SOURCE_SHA256SUMS must be public at an immutable
commit and byte-read back before either verifier or numerical runner executes.
The first outcomes and any incomplete numerical campaign are retained.

Exact replay from the repository root:

```text
python3 probes/P-U-CA40-SINUS-COMPARISON-1/verify.py
```

For floating replay compile kernel.cpp with the flags in PREREG.md, then
call numerical_run.py with --binary and a new --output directory. It requires
the declared Linux CPU topology and uses exclusive output creation.
