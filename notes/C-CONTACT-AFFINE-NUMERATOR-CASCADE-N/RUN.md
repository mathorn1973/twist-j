# Exact execution record

NON-CANONICAL / L1. One architecture, x86_64.

Both sources and the frozen contract were publicly committed and read back
byte for byte before either scientific execution. Shared source pin:
`0fde5621d9954ce86526eb1657e9afa1f1120fc6`.

- PREREG.md SHA-256: `fc85714e88ad9940ff31cdc6165fa541104543f0841c83f5b2ce1a7491574419`.
- verify.py SHA-256: `a0d55f34a913063e443f035affae4e99da5796f290e29077b317fe599f3ab679`.
- blindbreak.py SHA-256: `afee2a28b67f357c03ab9f23e38484d6fe52de6d59ed97a81c5f57e8d1b612e7`.
- BREAK-SCOPE.md SHA-256: `0181746faa4ffae392dcbf5a7c173bbe999ef84b123da7b59c49fc20fe5e1a65`.

The formulas were derived symbolically before pinning. The audit tests these
known formulas; no blind discovery of the affine law or gain is claimed.
The independent breaker was written without opening the author code/output,
then frozen before its execution and comparison.

## Author execution

Task-workspace command (the verifier reads no local data):

```sh
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -u contact_numerator/verify.py
```

Started UTC: `2026-11-02T22:36:31.807219+00:00`.
Platform: Linux-6.18.57-x86_64-with-glibc2.39; architecture: x86_64; Python: 3.12.14.
Exit code: 0. Stderr: 0 bytes.
Actual stdout: 747 bytes, SHA-256 `6512d4a20ad6883de75378580b8404e0a66a82e209876fb783522ef76ef2047a`.

EXPECTED.txt retains the actual stdout. It records 2850 full forward and
native-inverse cases, including one expected out-of-contract depth-limit
witness. The witness is not counted as a positive arithmetic readout.
Every test uses actual primitive contacts, not abstract arithmetic-table
semantics. Cached pairs are exact primitive transformations with invariant
checks; complete word replay and state comparison are retained.

## Repository replay

```sh
python3 notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/verify.py
python3 notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/blindbreak.py
```

The independent execution and comparison details are recorded in REVIEW.md
and BREAK-EXPECTED.txt. Both lanes are x86_64. They do not satisfy a public
two-architecture scientific gate. Ordinary required repository CI does not
scientifically execute notes/ verifiers. No Canon or apparatus-owner closure
is claimed by these executions.
