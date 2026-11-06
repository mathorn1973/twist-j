# Correction Audit R1–R2 for the Record-Retention Package

**PUBLIC, NON-CANONICAL. Design-exposed exact audit; not a registered probe.**

License: Apache-2.0.

Audit of the corrected identities of
`notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROOF.md` (Theorem 1 items 5–6,
Remark 1.3, Theorem 4 item 3) under the contract
`notes/C-HOMOGENEOUS-RECORD-RETENTION-N/CORRECTION_PROTOCOL.md`, following
review items R1 and R2 recorded in
`notes/C-HOMOGENEOUS-RECORD-RETENTION-N/CORRECTIONS.md`.

## Run

From the repository root, with Python 3.10 or later:

```text
python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/verify.py
```

The verifier imports the local law from the unchanged original verifier
`reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py` after checking that file's
byte count and SHA-256 and those of the original `EXPECTED.txt`. It reads no
other file, uses only the standard library and exact arithmetic, and disables
bytecode writing. `tools/check_reproduce.py` compares its stdout byte for byte
with `EXPECTED.txt`.

## Groups

| Group | Content |
|---|---|
| 0 `CUSTODY` | original verifier and stdout unchanged |
| 1 `WRONG_MEMORY_BALANCE` | $p_n = (1-q)\Lambda_n^2$, carrier-left balance and weighted wrong-memory balance for $q = 0, 1, 5/9$; unweighted form holds only for $q = 0$ |
| 2 `INPUT_CLASS` | correlated label-1 input follows Remark 1.3; the product formula fails |
| 3 `COMMUTATOR_CONTROL` | the free pulse step does not commute with $\mathbf 1_{x<z}$ |
