# RUN - C-NATIVE-HODGE-METRIC-SEAM-N

Status: PUBLIC NON-CANONICAL candidate-C corroboration.
Owner: #1251.

## Public prospective pin

Commit:

    e0118a96f999e51ad623bb3cbc7954c38bd634a0

The three prospective files were publicly read back byte-for-byte before
scientific execution.

- PREREG.md SHA256:
  674fb16a3e6d9fd13558a363f1bd9291f2587535b3441b96609880bd76f99dbe
- metric.py SHA256:
  099b4084c0175e3e5e4d7558cc2535448c222e84a017a7dc2d2b08a20b6d441d
- verify.py SHA256:
  4841091a297c67ef12a1d2a9333795840711e46c0796179fe16088a83cecd298

All inherited source hashes were checked at runtime.

Command from repository root:

    python3 notes/C-NATIVE-HODGE-METRIC-SEAM-N/verify.py

## arm64

platform: Darwin
architecture: arm64
python: 3.13.13
exit_code: 0
stdout_bytes: 545
stdout_sha256:
5013c405ddca328076df12203ff65c0c69f4dbd2eb3866c29d1ebbcb4382b70f
stderr_bytes: 0

## x86_64

platform: Linux
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_bytes: 545
stdout_sha256:
5013c405ddca328076df12203ff65c0c69f4dbd2eb3866c29d1ebbcb4382b70f
stderr_bytes: 0

## Exact stdout

    PASS G1: zero-sum section, six unit directions and tagged diagonal increment
    PASS G2: permutation-invariant symmetric-form constraint rank=4; family dimension=2; tag checks=512
    PASS G3: normalized complete positive family Q_rho with one free rho>0
    PASS G4: Hodge member rho=45/4; Euclidean control rho=9/2 is distinct
    PASS G5: normalized Hodge spatial matrix = (3/2)I+(3/4)11^T
    PASS G6: normalized Lorentz time coefficient = (15+6sqrt5)/16; signature 3+1
    NON-CANONICAL: selected Hodge seam fixes rho only after independent Hodge-target adoption

These are same-code reproductions, not independent-agent confirmation.
Universal statements are supplied by PROOF.md.
