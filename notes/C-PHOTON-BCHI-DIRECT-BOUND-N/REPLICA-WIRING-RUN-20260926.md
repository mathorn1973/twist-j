# First exact audit: full-replica pair/five wiring

**PUBLIC, NON-CANONICAL; candidate-C finite audit.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, owner #1143.
Author: A. M. Thorn. Date: 26 September 2026. Apache-2.0.

## Provenance and frozen inputs

The analytical derivation and prospective protocol are in
[REPLICA-WIRING.md](REPLICA-WIRING.md); the complete executable is
[verify_replica_wiring.py](verify_replica_wiring.py).

- Public basis: Canon v92, main `8b1132d828d94f83e653dab34d686a7e68394939`.
- Branch: `notes/photon-replica-wiring-20260926`.
- Complete prospective pin: `04da0efb2cff30f072ebbbe07d718b5ee924ee0f`.
- Proof commit: `83a1663b46f21ed35238f432eda8e877f11aa95a`.
- Public pre-execution scope notice: PR #1160, comment 5845415644.

Before execution, the GitHub file-read API at the exact pin returned the full
file Git blob identifiers below; both matched hashes computed from the complete
local bytes. The API excerpts were partial, but their blob identifiers address
the complete files. This was content-address verification, not a claim that a
second complete download was performed. Both local SHA-256 hashes were checked
before and after execution and remained unchanged.

| Input | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| REPLICA-WIRING.md | 15858 | d96b2736c1cbe6a951d99c33f76d28c827a12ded20618dc6b7933b8ff4839aae | fb2d91a277f32dd0e62fa5c55b6eb738b8994aaf |
| verify_replica_wiring.py | 12898 | 592fdfdf1f61dd1ff4429c2d83c0e8d1407ced4f96900b4c4776cb565f048afa | 338e2e7a182ec4601bf938bba6c7e98b306829a1 |

Only analytical work, static source inspection and compilation preceded the
public pin. This was the first scientific execution of this verifier. No rerun,
post-pin input correction or threshold change occurred. The same agent wrote
and checked the proof and source; this is not independent or blind review.

## Execution

```text
command: PYTHONHASHSEED=0 PYTHONUNBUFFERED=1 python3 verify_replica_wiring.py
working directory: directory containing the two frozen inputs
platform: Linux
architecture: x86_64
Python: 3.13.5
start UTC: 2026-09-26T10:21:04.861605+00:00
budget seconds: 45
elapsed seconds: 3.100341409
exit code: 0
timeout: false
stderr bytes: 0
stdout bytes: 542
stdout SHA-256: 760d85a6a34ff4128f4db427c09ecd4ed90b403f9631c56d40829f71baecf352
input hashes unchanged: true
```

Complete scientific stdout, including a final newline:

```text
face_table: 9 ordered pairs, exact inverse and weights PASS
local_projectors: m=0..12; partitions=27237; sign_masks=8191; admissible=1719 PASS
neutral_edge_mixtures: m10 two_fives=1/126; m12 two_fives=2/77 PASS
tied_face_graphs: 9 one-edge fixtures and 1 two-edge fixture; all covariance entries PASS
double_current_fixture: 5 doubled faces; signs=2; consistent wirings=126 PASS
four_cup: 21 faces; 53 standalone states; 2809 replica pairs; 441 covariance entries PASS
RESULT PASS (finite exact audit only; uniform moments and P1 not tested)
```

## Scope and publication boundary

All finite equalities and declared censuses passed. The graph fixtures preserve
one shared sign per face, including its repeated tokens. The four-cup check
compares the independent-replica covariance factor on the complete standalone
53-state family; it does not enumerate all wirings on a full periodic lattice.
The global partition and covariance identities rest on the written composition
proof, not a finite-volume extrapolation from these fixtures.

The result is one-architecture finite evidence. No ARM64 scientific replay or
independent proof review has occurred in this continuation. Ordinary repository
CI does not itself execute this notes verifier. No complete local repository
policy/Canon/gate replay is claimed: the execution environment did not contain a
full repository checkout. PR checks and mathematical review must be assessed
separately on the actual head before any merge.

The new positive representation sums all replica sums and current backgrounds,
but supplies no evaluated uniform constant for either Xi_L or Xi_L^(2), no
long-distance decay and no positive b_lower-25 chi_upper margin. P1 remains
open. Canon v92 and all original frozen inputs are unchanged. Only this neutral
run record is added after the prospective pin. The PR is for review, not an
acceptance or release claim.
