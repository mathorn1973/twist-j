# Source Manifest for P-INTEGER-RETAINED-PAIR-SOURCE-1

```text
probe_id:               P-INTEGER-RETAINED-PAIR-SOURCE-1
status:                 NON-CANONICAL
claim_level:            L1
external_datasets:      NONE
raw_transcripts:        NONE
canonical_authority:    mathorn1973/twist-j main (Public Canon v103, tag canon-v103)
base_commit:            b8bb9ed3ca1403df71c5192959e64cc9a9fb5018
content_commit:         01fb76f6b3b14a6a5ec05d0017ea922390ab6f66
canon_sha256:           d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b
canon_bytes:            1052518
predecessor_note:       C-JM-RETAINED-PAIR-SOURCE-N
predecessor_pr:         https://github.com/mathorn1973/twist-j/pull/1681
predecessor_pin_commit: 760157f57495fb87059b3a8a8e7943be7d0793c1
predecessor_head:       08836040d7117c9315c0b24be33eb8829f068898
predecessor_issue:      https://github.com/mathorn1973/twist-j/issues/1680
chain_scope_issue:      https://github.com/mathorn1973/twist-j/issues/1696
chain_scope_pr:         https://github.com/mathorn1973/twist-j/pull/1697
```

## Normative and Predecessor Inputs Referenced

1. `canon/CANON.md` (`Public Canon v103`, SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`, `1052518` bytes) and `POLICY.md` (Reading-family discipline and formal probe protocol).
2. `notes/C-JM-RESULTANT-SEAM-41-N/REPORT.md` (merged `PR #1671`, `issue #1670`):
   - minimal polynomials `f(x) = x^4 - 3x^3 + 4x^2 - 2x + 1` of `J = 1 + j^2` and
     `g(x) = x^4 - 4x^3 + 8x^2 - 4x + 1` of `M = 1 + m + m^2`,
   - resultant `Res(f, g) = 41`, common mod-41 root `x = 19`, and index-3 subring
     `Z[M] subset Z[m]`.
3. `notes/C-JM-PREPARATION-MEMORY-N/PROOF.md` (`PR #1679`, pin `87485fc66140a436bd6a337dd2ff452093ab607f`, `issue #1677`) and `notes/C-JM-RETAINED-PAIR-SOURCE-N/PROOF.md` (`PR #1681`, pin `760157f57495fb87059b3a8a8e7943be7d0793c1`, `issue #1680`):
   - rational pair Householder reflection `U_z = I_81 - (v_z r_z^T)/d_z`,
   - occupied-port swap continuation and `HOLD` block law,
   - opposite-seam collision `sigma_41 = lambda sigma_40 + (1 - lambda) sigma_42`
     with `lambda = 354161/735212` and 181-output one-sided seam test at `Q = 14112`.
4. `notes/C-JM-DECODER-CHAIN-PUBLICATION-N/SCOPE.md` (`PR #1697`, `issue #1696`):
   - explicit non-unique-decoder existence scope.
5. All computational checks in `verify.py` and `breaker.py` are self-contained
   using only the Python standard library (`fractions`, `functools`, `hashlib`,
   `itertools`, `math`, `pathlib`, `subprocess`, `sys`). No external files outside
   `probes/P-INTEGER-RETAINED-PAIR-SOURCE-1/` are read at runtime.
