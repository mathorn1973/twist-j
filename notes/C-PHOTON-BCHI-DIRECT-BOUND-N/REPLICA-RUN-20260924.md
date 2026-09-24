# First replica-cap and zero-sector audit, 24 September 2026

**PUBLIC, NON-CANONICAL; candidate-C finite audit.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Apache-2.0. Public Canon v91.

## Frozen provenance

Base main: `65195ab6ff6da1dcd3df17666238e16801b21838`, after #1157.

Prospective public pin: [`0ada73a7ce17ee2b03830184094315b4c04a7b2d`](https://github.com/mathorn1973/twist-j/commit/0ada73a7ce17ee2b03830184094315b4c04a7b2d).
The proof, preregistration, complete source and sole imported helper were
read back from this public commit on Linux x86_64 and hash-checked before the
first scientific execution. The public pre-execution record is
[issue #1143, comment 5813563575](https://github.com/mathorn1973/twist-j/issues/1143#issuecomment-5813563575).

No scientific execution preceded that pin. Separate agents statically
reviewed the written derivations and source with shared sources, not as
blind external reviewers. The first execution below passed without
correction or rerun.

| Input | Bytes | SHA-256 before and after execution |
| --- | ---: | --- |
| `REPLICA-CAPS.md` | 13284 | `99e73b4d3d3dac2bc6928f2dd8ba3746d77a9c39d5a6b35a92c1330bdc2bbd22` |
| `REPLICA-PREREG-20260924.md` | 4984 | `abf77fe9c8878deb63ff1edc1b14f6cce1217d999913213b91908a62f0bbf969` |
| `verify_replica_caps.py` | 12861 | `c14706224baf6e4f6309503e3db98ae94f1dc7c6debbccceaa9e0004783858a6` |
| `verify_connected_current.py` | 13159 | `ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403` |

All four inputs remained byte-for-byte unchanged after the run.

## Execution and exact output

Command, from the note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_replica_caps.py
```

- Architecture: x86_64; Debian GNU/Linux 13.5 (trixie).
- Platform: `Linux-6.12.90+deb13-amd64-x86_64-with-glibc2.41`.
- Python: 3.13.5, standard library only.
- Started: `2026-09-24T11:54:45.698995+00:00`.
- Elapsed: 3.675559292 seconds; 60-second preregistered budget,
  subprocess timeout 55 seconds; no timeout.
- Exit code: 0.
- Stdout: 973 bytes, SHA-256
  `9affd3d8e614807d341fdb1439b8fff53013a84f8245d551319d5035cf4dd3c0`.
- Stderr: 0 bytes, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The following block contains exact stdout, including the final newline:

```text
Replica cap audit: NON-CANONICAL conditional fiber only
D=3: complete fiber=32, interfaces=4, difference-current correlation=81/625: PASS
D=4: complete fiber=64, interfaces=5, difference-current correlation=243/3125: PASS
D=8: complete fiber=1024, interfaces=9, difference-current correlation=19683/1953125: PASS
D=16: geometry=18 segments, exact transfer: PASS
D=32: geometry=34 segments, exact transfer: PASS
Single-replica conditional covariance is one quarter of the difference moment
L=4: disjoint four-cups=1, injective finite images=9, 2^-41 binomial factor: PASS
L=6: disjoint four-cups=1, injective finite images=9, 2^-41 binomial factor: PASS
L=8: disjoint four-cups=16, injective finite images=243, 2^-41 binomial factor: PASS
L=10: disjoint four-cups=16, injective finite images=243, 2^-41 binomial factor: PASS
L=12: disjoint four-cups=81, injective finite images=243, 2^-41 binomial factor: PASS
RESULT PASS; no full-measure distance bound or positive P1 gap
```

## Interpretation

The finite checks cover the complete restricted pair fibers for D=3,4,8,
the derived geometry and exact transfer matrix for D=16,32, and the
disjoint insertion packings and selected-background injections for
L=4,6,8,10,12. All arithmetic is integral or rational. The written
[proof](REPLICA-CAPS.md) supplies the all-D classification, zero-halo
exterior factorization, arbitrary closed-background injection, and
arbitrary-face-source Hessian bound. Those statements are not inferred
from finite sampling.

The exact conditional difference-current moment is `(3/5)^(D+1)`.
Its single-copy conditional covariance is one quarter of that moment;
the unconditional two-copy covariance identity cannot be applied after
conditioning as if the two copies remained independent.

The full-measure global zero-current-sector probability and its normalized
Fourier second-moment contribution are at most
`(1+2^-41)^(-floor(L/4)^4)`. This does not bound neutral components inside
configurations carrying current.

**No full-measure distance-decay bound, uniform numerical chi upper bound,
or positive P1 gap was obtained.** Ordinary repository CI is separate and
does not constitute a second-architecture execution of this notes audit.
The canonical phase and P1 remain OPEN.
