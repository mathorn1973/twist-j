# Run record

## Custody precondition

The frozen files were committed together at
[`aa44cfe32bf461c217d6046ff3c835d3bd12eca7`](https://github.com/mathorn1973/twist-j/commit/aa44cfe32bf461c217d6046ff3c835d3bd12eca7),
read back from GitHub with matching Git blob SHAs, and recorded with SHA-256
hashes in [issue comment `5490491218`](https://github.com/mathorn1973/twist-j/issues/750#issuecomment-5490491218)
before either program was executed.

```text
4db1a4fd2988a843e1c752610a80cdb898457692b1342bcc1e47986bad6a50f4  PREREG.md
56c5f8d0dd306e2b90b393c6b1e947bea394c1b2487def7e972f813cd22214ad  verify.py
16e9e0ea135366fa456f15733134d0fa676a0d691c4a22b463f2875fd5a06f3f  break.py
```

Post-run hashing returned the same three values. The frozen surface did not
change during execution.

## Environment

```text
Python 3.12.13
Linux 6.18.35 x86_64
```

Both programs use only the Python standard library, exact integer/rational or
finite-field arithmetic, and deterministic bounded scans. They perform no
network, subprocess, filesystem-write, random, or environment-dependent
operation.

## Commands and exits

Run from `notes/C-C40-RECIPROCAL-RAMIFIED-SEAM-N/`:

```sh
python3 verify.py
python3 break.py
```

Both commands exited `0`. Their exact stdout is preserved respectively in
`EXPECTED.txt` and `BREAKER_EXPECTED.txt`.

The principal verifier audited all `17,984` rational primes at most `200,000`
(`17,982` unramified). The blind breaker separately factored one prime from
each of the sixteen unit classes and audited all `168` primes at most `1,000`
(`166` unramified). These scans are explicitly not the proof of the universal
claim; the complete unit group and ramified identities are.

