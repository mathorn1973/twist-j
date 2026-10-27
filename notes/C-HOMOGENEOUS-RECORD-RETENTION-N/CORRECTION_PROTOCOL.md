# Correction Audit Contract: R1–R2 of `C-HOMOGENEOUS-RECORD-RETENTION-N`

**PUBLIC, NON-CANONICAL. Prospective contract for the correction audit,
committed, pushed and read back before its first execution.**

License: Apache-2.0.

## 1. Regime

Under the disposition in `CORRECTIONS.md` R4, this is a **design-exposed
NON-CANONICAL exact audit**. It is not a registered public probe and not a
formal gate under `POLICY.md` §3. It checks exact identities that are already
proved analytically in `PROOF.md` after the R1 and R2 corrections: Theorem 1
items 5 and 6, Remark 1.3, and the corrected proof of Theorem 4 item 3. It
introduces no new parameter, threshold or quantitative result. It does not
re-evaluate the Theorem 6 bound, and it does not change the first run or its
verdict. Its result can only confirm or refute the stated identities at the
stated finite instances.

## 2. Code and inputs

- Code: `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/verify.py`,
  SHA-256 `b6730c48e9fc3bb7a4c3f08094263a80de5ff209aaef83db68749d112df36fd7`,
  8596 bytes. Python standard library only; exact integers and fractions; no
  floating point, network or randomness.
- Law implementation: imported from the unchanged original verifier
  `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py` only after its byte
  count 33053 and SHA-256
  `a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7` are
  checked. The original `EXPECTED.txt` (1162 bytes, SHA-256
  `dccec8381f051efede09b61cea2b15c6735a883a4286e2d13c131bc2ea0164d3`) is also
  checked. These two files are the only files read. Bytecode writing is
  disabled during the import.
- Instances: receiver $z = 100$, $4$ macrosteps of the complete local law.

## 3. Checks and failure conditions

| Group | Content | Fails if |
|---|---|---|
| 0 `CUSTODY` | bytes and SHA-256 of the original verifier and stdout | any mismatch |
| 1 `WRONG_MEMORY_BALANCE` | memory inputs $q = 0$ (entangled on $d_0,d_2$), $q = 1$ (old memory exactly $d_1$), $q = 5/9$ (entangled intermediate), each with the original mixed spatial state and with a free crossing pulse ($x = z-1$, bank 1, object 20 sites away). At every step: $p_n = (1-q)\Lambda_n^2$; carrier-left balance (2); weighted wrong-memory balance (2') evaluated on the wrong-memory weight itself; $p_n\equiv0$ for $q = 1$. The unweighted form must hold at every nonzero-current step for $q = 0$ and fail at every such step for $q = 1$ and $q = 5/9$; nonzero current must occur | any exact equality fails, no nonzero current, or the unweighted pattern differs |
| 2 `INPUT_CLASS` | correlated label-1 input $\chi_A\otimes e_1\otimes d_0\otimes r_0 + \chi_B\otimes e_1\otimes d_1\otimes r_1$: Remark 1.3 holds at every step, and the product formula with the marginal $q = 1/2$ fails at least once | Remark 1.3 fails or the product formula never fails |
| 3 `COMMUTATOR_CONTROL` | a bank-1 pulse at $z-1$ reaches bank 2 at $z$ in one free step, so $[V,\mathbf 1_{x<z}]\ne0$ | no crossing amplitude |

A failed assertion aborts the run with a nonzero exit code. It would refute the
corrected identity, or the audit code, at that instance, and would be recorded,
not hidden.

## 4. Pre-pin disclosure

The audit functions were exercised before this pin only on non-frozen toy
instances (receiver $z = 7$, $2$ macrosteps). That exercise included the
custody check of the original files. No check at the frozen instance
($z = 100$, $4$ macrosteps) has been executed. The identities are analytical
consequences of Theorem 1, so the audit is design-exposed and not a blind test.

## 5. Execution and custody

From a clean checkout of the pin commit, run
`python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/verify.py` from the
repository root under the `tools/check_reproduce.py` environment
(`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, at most
120 seconds, exit 0, empty standard error). Save the exact stdout as that
directory's `EXPECTED.txt` and record neutral fields in its `RUN.md`. A changed
verifier or contract after this pin requires a new pin; a recorded run is never
overwritten.
