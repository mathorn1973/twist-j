# RUN

**PUBLIC, NON-CANONICAL.**
Owner: #1170
Author: A. M. Thorn
Date: 26 September 2026

Frozen pin: `3812d058619ffe07984bd71dd18585b80a901ce3`.

GitHub readback before execution:

- `PREREG.md`: blob `d4a9a7a69289039511451bc7f9f3a17a0cade3bf`,
  SHA-256 `da99f47fbd7befb8edd9e0f9d3b4525aa3e387d5114258e0214b47bbfaad319e`.
- `verify.py`: blob `78991c5f8ae28715a4c551538edec0eb394d3caf`,
  SHA-256 `4b96d46c8b1079a1256f32215b4815d3bf8a25cdb1e29244d198cb163e6c43a8`.

Environment:

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

Result:

```text
exit_code: 0
stdout_bytes: 349
stderr_bytes: 0
stdout_sha256: bf5ec3c2332db4901f11bdeeb50952862581dff77d4bdc76771e091ad3aad75f
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout:

```text
CONTEXTS PASS per_entry=1442 by_type=15,148,462,572,245 unique_filtered_graphs=1830
B0 1,15,74,154,143,49
B1 1,15,74,154,143,49
B2 1,14,65,129,115,38
B3 1,13,57,110,97,32
B4 1,12,50,94,82,27
ROOT5 1,11,44,82,72,24 contexts=474
P6 1,18,111,308,429,294,79
UNCLE_MEMORY_CERTIFICATE NONE
AUDIT PASS; uncle_memory_ansatz=NO_CERTIFICATE; Xi=OPEN; P1=OPEN
```

Stderr is empty. One architecture only.
