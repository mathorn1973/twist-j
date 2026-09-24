# Neutral-sum first execution and disposition, 24 September 2026

**PUBLIC, NON-CANONICAL.** Working item C-PHOTON-BCHI-DIRECT-BOUND-N,
issue #1143. Author: A. M. Thorn. Apache-2.0.

## Custody and first attempt

Prospective pin: `84b7ccfc1fafd8ab98eda21f31f175fdabe44cee`.
Public reservation: [issue comment 5814590651](https://github.com/mathorn1973/twist-j/issues/1143#issuecomment-5814590651).
Pre-execution pin and hashes: [issue comment 5814788453](https://github.com/mathorn1973/twist-j/issues/1143#issuecomment-5814788453).

The execution workspace fetched all five inputs directly from the immutable
public commit and matched their byte counts and SHA-256 before execution.
The capture wrapper checked those same bytes again immediately before
starting the verifier. No scientific code was executed before the pin.
There was one scientific attempt, no failure, correction or rerun.

| Pinned file | Bytes | SHA-256 |
|---|---:|---|
| NEUTRAL-SUM.md | 29910 | `11bee57086a8aa73e732675fb858537fec84a01c53b697ef1b337968acfa48f6` |
| NEUTRAL-PREREG-20260924.md | 6091 | `fe173e22e07e1f90e4135a781303974504309de35051f38e445ab6d10c1d1e77` |
| verify_neutral_sum.py | 24353 | `3d360b4f7923372be84cd595bde6e3afd25dbed481e18077e069f87ac3abf94c` |
| README.md | 25033 | `279ca914a7675905613d5b491c1704e6014cb0d689407b3ad10e7d2fde828692` |
| verify_connected_current.py, unchanged helper | 13159 | `ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403` |

## Execution

```text
command: python3 -B verify_neutral_sum.py
working directory: notes/C-PHOTON-BCHI-DIRECT-BOUND-N/
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
Python: 3.13.5
start UTC: 2026-09-24T13:12:54.616077+00:00
elapsed seconds: 11.302663898095489
exit code: 0
stdout bytes: 2088
stdout SHA256: 021f47496c3435cb9388e8a1c1743bb5b7d75bb267dd675a51beab601b466ff4
stderr bytes: 0
stderr SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The working directory above is the repository-relative replay location;
the first execution used a materialized directory containing the exact
pinned files. The wrapper captured raw stdout/stderr without transformation.
The code block below reproduces the entire scientific stdout, including its
final newline. Stderr was empty.

```text
Neutral sums and conditional variance; NON-CANONICAL exact finite audit
onecopy 5 states {-1: 389, 0: 577, 1: 389} fields 456 PASS
onecopy 7 states {-1: 1961, 0: 3363, 1: 1961} fields 2454 PASS
geometry-transfer 9 PASS
geometry-transfer 17 PASS
geometry-transfer 33 PASS
exact-onecopy-neutral-sum PASS; no full-covariance or P1 claim
GEOMETRY_COUNTS root=18 path=15 comb=2700 endpoint=120 root-placement=240
SUMMED_COMB ratio=3375/4096 prefactor=1/553728; generated events only
ALIGNED_COMB D=5 cubes=11 boundary=46 noncap=42
ALIGNED_COMB D=7 cubes=17 boundary=70 noncap=64
ALIGNED_COMB D=9 cubes=23 boundary=94 noncap=86
NEUTRAL_LOWER_FORM axes=(0, 1) slices={0: -5} norm={0: 25}
NEUTRAL_LOWER_FORM axes=(0, 2) slices={-1: -1, 0: -3, 1: -1} norm={-2: 1, -1: 6, 0: 11, 1: 6, 2: 1}
NEUTRAL_LOWER_PACK L=4 axes=(0, 1) k=4 faces=84 edges=144 vertices=80 c_L=1/140737488355328 deficit=7/1266637395197952
NEUTRAL_LOWER_PACK L=4 axes=(0, 2) k=4 faces=84 edges=144 vertices=80 c_L=1/140737488355328 deficit=7/1266637395197952
NEUTRAL_LOWER_PACK L=6 axes=(0, 1) k=36 faces=756 edges=1296 vertices=720 c_L=1/79164837199872 deficit=0
NEUTRAL_LOWER_PACK L=6 axes=(0, 2) k=36 faces=756 edges=1296 vertices=720 c_L=1/79164837199872 deficit=0
NEUTRAL_LOWER_PACK L=8 axes=(0, 1) k=64 faces=1344 edges=2304 vertices=1280 c_L=1/140737488355328 deficit=7/1266637395197952
NEUTRAL_LOWER_PACK L=8 axes=(0, 2) k=64 faces=1344 edges=2304 vertices=1280 c_L=1/140737488355328 deficit=7/1266637395197952
NEUTRAL_LOWER_PACK L=10 axes=(0, 1) k=225 faces=4725 edges=8100 vertices=4500 c_L=9/879609302220800 deficit=19/7916483719987200
NEUTRAL_LOWER_PACK L=10 axes=(0, 2) k=225 faces=4725 edges=8100 vertices=4500 c_L=9/879609302220800 deficit=19/7916483719987200
NEUTRAL_LOWER_PACK L=12 axes=(0, 1) k=576 faces=12096 edges=20736 vertices=11520 c_L=1/79164837199872 deficit=0
NEUTRAL_LOWER_PACK L=12 axes=(0, 2) k=576 faces=12096 edges=20736 vertices=11520 c_L=1/79164837199872 deficit=0
NEUTRAL_LOWER PASS; geometry and constants only, no positive P1 gap
RESULT PASS; complete P1 and Canon promotion remain unproved
```

## Result and scope

**PASS for the frozen finite audit.** No falsifier fired.

At D=5 and 7 the reduced sums include every state after the exhaustive
243-choice endpoint integrations. The verifier additionally reconstructed
456 and 2454 actual current-tagged lattice fields respectively. At D=9,17,33
it checked geometry, endpoint sums, local cap equations, transfer matrices
and bounds; it did not enumerate the complete reduced field space at those D.
The cube/comb counts and both finite-volume insertion packings passed the
separate inventories stated in the preregistration.

The written result is an evaluated full-measure bound for the declared
generated comb events, including their geometric union:
`(1/553728)(3375/4096)^R`. It is not a bound on the complement of that
class or the entire current covariance. The complete one-copy sum on the
aligned restriction and the exact deletion identity require no empty halo.

The full-measure variance proof improves the transverse floor to
`b>=25/(36*2^41)` for every admitted ordered profile. It also proves
`chi>=1/(36*2^41)`, so this particular floor cannot satisfy the strict
P1 comparison with any valid upper bound on chi. The unrestricted
macroscopic neutral contribution and the complement of the controlled
geometric class have not been bounded sufficiently.

Analytical arguments and static source were reviewed by separate agents
with shared sources; this is not blind external evidence. The written
derivations are candidate-T within their stated scope. This first exact
finite audit is candidate-C and uses one architecture. Ordinary repository
CI does not execute notes audits, so its two architecture jobs are not a
second-architecture reproduction of this scientific run.

**P1 remains OPEN.** P2, S7 and PHOTON-MASSLESS-PHASE are unchanged.
No complete positive P1 margin is claimed, and no Canon promotion is earned.
Public Canon v91, Registry, Frontier, gates, workflows, existing formal
probes and phase thresholds remain unchanged.
