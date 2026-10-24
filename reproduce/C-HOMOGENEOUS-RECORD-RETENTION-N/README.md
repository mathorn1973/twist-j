# Record Retention on the v105 Homogeneous Law: Standard-Library Verification

**PUBLIC, NON-CANONICAL.**

License: Apache-2.0.

Exact audit of `notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROOF.md` under the
preregistration `notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROTOCOL.md`.

## Run

From the repository root, with Python 3.10 or later:

```text
python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py
```

The verifier uses only the Python standard library (`fractions.Fraction`,
`int`, `math.comb`, `math.factorial`, `math.isqrt`). It performs no
floating-point arithmetic, reads no files, makes no network calls and uses no
randomness. `tools/check_reproduce.py` runs it with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, a
120-second limit, exit code 0 and empty standard error, and compares standard
output byte for byte with `EXPECTED.txt`.

## Groups

| Group | Content |
|---|---|
| 1 `LABEL_ALGEBRA` | exchange on all 26 labels; wrong-memory, full-record and old-information identities |
| 2 `PHYSICAL_CONJUGACY` | exact local law in $\mathbb Z[i][\zeta_5]$ versus the calibrated evolution; wrong-memory identity; unitarity; record change equals a quarter of the carrier bond current; negative controls |
| 3 `RECROSSING_AND_NO_PARKING` | polynomial identities behind the Hardy no-parking theorem; light-cone recrossing witness |
| 4 `SYMMETRY_AND_DARK_RECORD` | reflection symmetry making $\Omega$ even; dark-state parity; eternal parked record |
| 5 `SUCCESS_SECTOR` | membership of the declared family in the v105 event and analytic preconditions |
| 6 `RETENTION_CERTIFICATE` | rational bounds $\bar\delta(T)$, $\bar\eta(T)$, the modulus table and the frozen verdict |

Structural failures abort with an assertion. The quantitative verdict is
printed as `ACHIEVED` or `NOT ACHIEVED` against the frozen tolerance.
