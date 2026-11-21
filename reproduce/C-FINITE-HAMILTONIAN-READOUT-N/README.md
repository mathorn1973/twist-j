# Exact audit of C-FINITE-HAMILTONIAN-READOUT-N

NON-CANONICAL L1, conditional candidate-T; design exposed, not independent
confirmation. Read the matching notes/ directory, especially PROOF.md and
PREREG.md. The program audits finite exact instances of the stated general
analytical lemmas, not a full spatial device or a Born occurrence mechanism.

From the repository root, after the public prospective pin is read back:

```sh
python3 reproduce/C-FINITE-HAMILTONIAN-READOUT-N/verify.py
```

Use the repository-provided `tools/check_reproduce.py --base FULL_BASE_SHA`
for later deterministic byte comparisons. Exact stdout, the prospective pin
and neutral environment/run metadata will be recorded in EXPECTED.txt and
RUN.md after the first run. The verifier uses only the Python standard library.
