# Connected-current result and exact run record

PUBLIC, NON-CANONICAL; candidate-C finite audit. Working item
C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026.
Original text/code: Apache-2.0.

## Scientific result

**Finite audit: PASS. Full distance-decay target: still OPEN.**

The separately written candidate-T derivation establishes:

- an exact neutral-edge pairing augmentation of the original measure and
  the decomposition `Cov(j)=E_aug sum_K J_K outer J_K`;
- finite-volume susceptibility upper bounds through charged connection
  probabilities or the root oriented-face moment M_L;
- an explicit family, for every D>=3, showing that disconnected charged
  loops cannot generally be sign-switched independently while their
  occupied face support is fixed;
- the integrated source constant `c=3281*5^20/3^44<1/3000`, specializing
  the pre-existing complex-source method, and the resulting stronger local
  circulation bounds.

The actual uniform bound on M_L or on the charged connection moment is not
proved. The tube's conditional far-edge product is -1, but its probability
is not a volume-uniform covariance lower bound and its axis current form
factor is zero. This is not a failure of unconditional decay or of P1.
The local constants contain no distance parameter. No numerical value for
the required chi upper bound or positive b-25chi gap is claimed.

## Frozen inputs and custody

Pin: `049aca14c3fd8291bd55817046b16a23c928cbe0`.

All three files were publicly read back against their complete source
before any scientific execution. A separate exact-pin download on the run
host passed the hashes at 2026-09-24T09:33:41.690434+00:00.
The same input bytes and hashes were checked again after execution.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| CONNECTED-CURRENT.md | 13894 | `7ce7bdf7501e0e4b56de806a59b47ea53efc333cb141753c9d253576c211f0fe` |
| CONNECTED-PREREG-20260924.md | 4601 | `942c1361dae4108b909e6acd00e35bc41ee4c8fa746f5c10929851fd61951349` |
| verify_connected_current.py | 13159 | `ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403` |

This was the first scientific execution. Only analytical work, source
inspection and syntax parsing preceded the pin. There was no failed
attempt, repaired input or shifted target.

## Execution

- Platform: Debian GNU/Linux 13 (trixie).
- Architecture: x86_64.
- Python: 3.13.5; standard-library integers and Fraction.
- UTC start: 2026-09-24T09:34:13.937446+00:00.
- Elapsed: 0.118864 seconds; frozen limit: 60 seconds.
- Exit code: 0; timeout: no; stderr: 0 bytes.
- Stdout: 1286 bytes; SHA-256 `937dd805c701254c7d607efa681fa46f3ca96c80a1dc0b5ec5530fbd79a5a7cf`.
- Empty stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Working directory contains the unchanged pin files. Command:

```sh
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_connected_current.py
```

Exact UTF-8 stdout, LF line endings and final newline:

```text
C-PHOTON-BCHI-DIRECT-BOUND-N connected-current audit (NON-CANONICAL)
Local incidence census: 153 admissible patterns, neutral=141, charged=12; pairing weights: PASS
Touching cubes: faces=12, signings=4, pairing probabilities=1/2,1/4,1/4; all face covariances: PASS
D=3 L=10: faces=52, neutral_edges=84, charged_edges=8, pairing_components=1, signings=2, current_components=2, conditional_product=-1, axis_form_factor=0: PASS
D=4 L=12: faces=56, neutral_edges=92, charged_edges=8, pairing_components=1, signings=2, current_components=2, conditional_product=-1, axis_form_factor=0: PASS
D=8 L=20: faces=72, neutral_edges=124, charged_edges=8, pairing_components=1, signings=2, current_components=2, conditional_product=-1, axis_form_factor=0: PASS
D=16 L=36: faces=104, neutral_edges=188, charged_edges=8, pairing_components=1, signings=2, current_components=2, conditional_product=-1, axis_form_factor=0: PASS
D=32 L=68: faces=168, neutral_edges=316, charged_edges=8, pairing_components=1, signings=2, current_components=2, conditional_product=-1, axis_form_factor=0: PASS
Integrated block constant c=312900543212890625/984770902183611232881<1/3000: PASS
Circulation bounds: one<1/1501, pair<1/2250001, absolute covariance<1/4500001: PASS
RESULT PASS; no distance-decay or P1 conclusion
```

## Review and limits

Two analytical agents developed complementary parts. A third agent
separately reviewed the pairing law, all-D geometry, normalization and
source bound, then statically reviewed the final proof and complete audit.
All had access to shared source material: this is not blind external
review or formal independent acceptance.

The review required keeping the connectivity bounds finite-volume:
local convergence alone does not identify connections whose paths can
escape. The final proof does so, and makes no unproved infinite-volume
connection identification. Before the pin it also corrected formula
rendering and clarified that the touching-cube fixture proves strict graph
refinement and face-covariance cancellation, not a strict numerical
improvement for a nonzero current covariance.

The audit verifies all 153 allowed local incidence patterns, the exact
touching-cube augmented law and every face covariance, five prescribed
neutral-tube instances, and rational source/normalization constants.
The universal claims depend on the written proofs, not extrapolation from
those five distances.

No new formal P-probe, physical reading, cross-layer lift or Canon
promotion was made. This is one x86_64 scientific execution. Ordinary
repository CI does not automatically execute the notes audit and must not
be described as its two-architecture verification. Public Canon v91 and
the original ordered-limit obligations retain their scope.
