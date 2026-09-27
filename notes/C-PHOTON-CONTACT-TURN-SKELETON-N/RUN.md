# First exact audit: contact-turn skeleton

**PUBLIC, NON-CANONICAL. candidate-C finite audit only.**
Owner: #1192. Author: A. M. Thorn. Date: 27 September 2026.
License: Apache-2.0.

## Public pin and custody

The complete scientific input was published together at
`a5c5fc5045eeb0bf30c0de1821e8d03366324231` before the first scientific execution.
The three files are byte-identical to the previously prepared, unexecuted
builder inputs. The public commit, not the local builder commit, is the pin.

The author explicitly approved the connector identity
`A. M. Thorn <221838986+mathorn1973@users.noreply.github.com>` for this one
candidate package. The scoped authorization is recorded on issue #1192 before
publication. It does not change the repository's default author identity.

| Input | Git blob | Bytes | SHA-256 |
|---|---|---:|---|
| PREREG.md | ca3e195cb61ac1a19b6f232cc64fa6a1040770a6 | 8274 | 3beae785369ed0a597a430a86c6d95472c9c6cb77dfe678087d2283df0a1b222 |
| PROOF.md | df7e676bc43e3d3a1c06cc58b0e9df6cc763810d | 12696 | fc3dc556524cd9e9a125e209168f0531ee15dbe8a540e4cb8b7e5b19ed582dc7 |
| verify.py | 8253d2024b93f426eef313cb6009c105ce1b2989 | 10478 | 3de96d5fc4f7eb2f422d33924ff8f6e8e6b2f1140dd27cc37cae59f900fe7dbc |

Public Git readback verified all three blobs, byte counts and SHA-256 hashes
before execution. The worktree was clean at the exact pin. Static compilation
was performed; no scientific execution preceded this recorded run.

## Command and deterministic environment

Run from the repository root:

```text
python3 notes/C-PHOTON-CONTACT-TURN-SKELETON-N/verify.py
```

```text
platform: Linux
architecture: x86_64
python: 3.13.5
PYTHONHASHSEED: 0
PYTHONDONTWRITEBYTECODE: 1
OMP_NUM_THREADS: 1
OPENBLAS_NUM_THREADS: 1
MKL_NUM_THREADS: 1
NUMEXPR_NUM_THREADS: 1
PYTHONOPTIMIZE: unset
```

The command was run once by a subprocess with an actual 45-second timeout.
The outer tool budget was larger, so a tool timeout was not used as the
scientific process limit. No retry, source edit or parameter change occurred.

## First-run result

```text
exit_code: 0
timed_out: false
timeout_seconds: 45
elapsed_ns: 472705846
stdout_bytes: 803
stdout_lines: 9
stdout_sha256: d119e399860ba707533efaeb6be5f3dfd4b0493b7329a2b99ef680772ed609f8
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact scientific stdout:

```text
SOURCE_TILT PASS sign_patterns=31 quarter_turn_pairs=2145 direction_transfer_lengths=1..10
CONSTANTS PASS B=4913/16384 A=4913/4096 q=741863/819200 integer_gap=77337
GEOMETRY PASS cycles=93 periodic_embeddings=186 observed_axis_pairs=2232
L_STRIP PASS n=2..20; all_n_ge_5_quarter_turn_and_outside_SC_by_base_and_ratio; ribbons=n,n
PERIODIZATION PASS synthetic_profiles=9 support_spans_multiple_periods
SERIES PASS coefficients=0..32 exact_tail_identities_R=1..24
BOUND PASS C_quarter=9150228420549984384365501350041678899650851393161127836665153245438373507373930082095902829272075280785251379/7664558694084152605828561045241161572356418550769204257024868598916896967675084800000000000000000000000000
INTEGER_CEILING C_quarter<1194
AUDIT PASS; quarter_turn_single_cycle_Xi=UNIFORM; full_Xi=OPEN; P1=OPEN
```

Stderr is empty.

## Scope of the audit

The complete frozen finite audit passed on one x86_64 architecture. This is
candidate-C. The same author wrote PROOF.md and verify.py; no independent or
blind proof confirmation is claimed. Ordinary repository CI does not turn
this notes verifier into a two-architecture scientific gate. The all-volume
statements rely on the written candidate-T argument, pending separate review.

The integer ceiling 1194 was descriptive output of the frozen exact formula,
not a fitted acceptance threshold. It bounds only the declared quarter-turn
single-cycle contribution, not full Xi_L, Xi_L^(2), chi_L or P1.
