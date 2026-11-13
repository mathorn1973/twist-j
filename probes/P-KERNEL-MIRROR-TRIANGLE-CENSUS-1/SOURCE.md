# Source custody and corrections

PUBLIC-source; NON-CANONICAL; L1. This is a new public verification of known
results. It does not retroactively preregister the incubation experiment.

## Public basis

Public Canon v98 at main and dereferenced tag `canon-v98`:
`b9f7af5f1b58c76956e280e33bd345c90bd88d1f`.
Declared content commit: `e62613db629de237fe15715ae2a9235f4e207b2c`.
All five normative file hashes matched at intake on 2026-10-05.
The public letter definitions are in
[`kernel-connectivity`](../../reproduce/kernel-connectivity/verify.py)
and [`P-CENSUS-REPLAY-1`](../P-CENSUS-REPLAY-1/verify.py).
Registered affinity, linear order 200 and fired commutator results are
crosschecks, not inferred from the supplied archive.

## Supplied incubation package

The author supplied `platonska-telesa-a-census_2026-10-05.zip` (41947 bytes),
SHA-256 `a62e494e78732b5cbfdd4ed0ff01948c1bfe2e4ab5325d096ec5a5b37c3dec2d`.
All twelve entries in its `SHA256SUMS.txt` match their supplied files.
The original archive and extracted originals were retained unchanged.
The seven census files relevant to this probe have these identities:

| Original file | SHA-256 |
|---|---|
| PREREG-C-KERNEL-MIRROR-TRIANGLE-CENSUS-N.md | 807db25f76530ddb39df22f2d997f44b266f91f08cd091d37254bd8d11ca1b4c |
| PROMO-C-KERNEL-MIRROR-TRIANGLE-CENSUS-N.md | f9220d67b65a888ed9f17954b36ec79b481e9f5f4ec3bf6a35bec72f215c8b15 |
| RESULT-C-KERNEL-MIRROR-TRIANGLE-CENSUS-N.md | 87197d28c1b83ae4272149ca7db992b858c97cd07b5dc14f7c73295a0a5db035 |
| verify_c_kernel_mirror_triangle_census_n.py | 2afbbb515ab0b6409675f75fa100bbe0f9e81a731067a505d7974430efda0d48 |
| verify_c_kernel_mirror_triangle_census_n.stdout | 6c7f059bf6ee5f54a7ea2b3cbf350ebe40ed30db0965692a3a689de4285ecd9f |
| break_check_c_kernel_mirror_triangle_census_n.py | 295cfb9185c3e22e8a601aa3113ceca34cc1373912a2aefb3f05d7ce1bb2b100 |
| break_check_c_kernel_mirror_triangle_census_n.stdout | 7a48385c1ff951dde281e2bff937b44cbd89d254a27c2f6354d472681f7fd4f6 |

The supplied verifier transcript has 3862 bytes and reports 23/23 PASS.
The supplied crosscheck transcript has 2573 bytes and reports NO BREAK.
Its reported environment is Ubuntu 24.04, x86_64, CPython 3.13.16. These are
historical supplied records. Hash verification confirms byte identity; it
does not independently establish the original run environment or the
chronology of the original freeze. Fresh public execution is recorded only
in this probe's RUN.md and EXPECTED.txt.

The archive's separate Schlafli/golden-ratio scripts, their transcripts and
the accompanying general note are outside this probe. They are not run or
imported as public evidence here. Original RESULT observations P1--P5,
including exponent ten, are also excluded.

## Corrections without rewriting the original

1. Original PREREG Part B promised candidate-T on agreement with the breaker.
   One-architecture agreement alone does not satisfy the public computation
   gate. The historical table is candidate-C. Fresh architecture validation
   and independent analytic proof are distinct evidence routes; neither
   silently inserts a T into the Canon registry.
2. The new public freeze discloses every known pair and triple result. The
   order of bc was already publicly available before this public freeze;
   the original narrower knowledge declaration is not adopted as public
   priority evidence. This is verification, not a blind discovery.
3. The original surface description is made explicit in SURFACES.md using
   one triangle per element of the triple subgroup, not per original cell
   state. Reflection and orientation-preserving triangle groups are
   distinguished. Orientability now has a common analytic sign proof.
4. The public implementation is an adaptation, not a byte-identical rename.
   It freezes the known numerical targets, audits the explicit translation
   and orientation identities, and compares structured results from two
   independently implemented methods automatically. Original sources and
   transcripts are not edited to match the new run.
5. The independent crosscheck uses the affinity of the maps to compress a
   point stabilizer into images of six basis points. Its independence is
   implementation and group-order route independence, not freedom from
   that mathematical assumption. The bounded word search is omitted: it
   is unnecessary for the group-order theorem and its original order cap
   could report an unresolved order as a completed search.

Only the necessary current proof, verifier and provenance are published.
The archive is a supplied source package, not normative public authority.
