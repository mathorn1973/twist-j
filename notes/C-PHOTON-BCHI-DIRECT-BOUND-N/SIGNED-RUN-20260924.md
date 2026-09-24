# Signed-slice and insertion audit: first run

PUBLIC, NON-CANONICAL; candidate-C finite audit, candidate-T written proof.
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.

## Disposition

**PASS at the frozen finite scope; P1 remains OPEN.** The first execution
passed without a failed attempt, source correction or changed target.
No scientific execution preceded the public pin and four-file readback.

The audit confirms the aligned bridge's signed slice vector, ell=2 despite
growing raw face area, neutral constant-slice removal, and the local
geometry used in the insertion proof. It does not estimate Xi_L in the
full measure. The actual b floor and the matching chi floor follow from
the written analytical partition comparison, not a full-measure census.
Their equality still prevents this floor from certifying a positive gap.

## Frozen inputs

Public pin: `777d7c9d7c8bf009dd0c980f3dfb7c212c1da497`.
Branch: `notes/photon-signed-slices-20260924`.
Parent public main: `6f181bb96b9b0692c03195dbc12233b14ed2b476`.
Public Canon v91 unchanged: 772678 bytes, SHA-256
`6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1`.
The content commit and activation tag are ancestors of the public base;
its x86_64, aarch64 and aggregate checks were successful at intake.

| Input | Bytes | SHA-256 |
|---|---:|---|
| SIGNED-SLICES.md | 13484 | `2b592a32912b4e02320b3a98946ba4ba02f50df221a85f3a40b49c907ca700f2` |
| SIGNED-PREREG-20260924.md | 4506 | `5d9b001eefd3cf925b709e6d48faa6a1680d80f107f6469df3162420c7e712c6` |
| verify_signed_slices.py | 10815 | `cbb8e92d34dc1ca54ca595100631c1f01e697c1bc6b2100738eae36e61c37bf5` |
| verify_connected_current.py, unchanged helper | 13159 | `ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403` |

All four files were fetched from the exact public commit and matched these
hashes before execution. They matched again after execution. The imported
helper's previous audit does not execute on import.

## Command and environment

From this note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_signed_slices.py
```

- Platform: Debian GNU/Linux 13 (trixie).
- Architecture: x86_64.
- Python: 3.13.5; standard library only.
- Budget: 60 seconds; process timeout 55 seconds inside the wrapper.
- Elapsed: 0.110019 seconds.
- Exit code: 0.
- Stderr: empty, 0 bytes; SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Stdout: 1468 bytes; SHA-256
  `8e0eafecd18f239021da2c49a770defb91dc83e4e70af456a05c1ae9041689f6`.

Exact stdout, including its final newline:

```
Signed axial slices: NON-CANONICAL exact finite audit
D=3 L=10: faces=52, m01=16, charged_edges=8, signings=2, current_components=2, signed_l1=10, signed_l2_squared=50, I1=2, bound=4
D=4 L=12: faces=56, m01=18, charged_edges=8, signings=2, current_components=2, signed_l1=10, signed_l2_squared=50, I1=2, bound=4
D=8 L=20: faces=72, m01=26, charged_edges=8, signings=2, current_components=2, signed_l1=10, signed_l2_squared=50, I1=2, bound=4
D=16 L=36: faces=104, m01=42, charged_edges=8, signings=2, current_components=2, signed_l1=10, signed_l2_squared=50, I1=2, bound=4
D=32 L=68: faces=168, m01=74, charged_edges=8, signings=2, current_components=2, signed_l1=10, signed_l2_squared=50, I1=2, bound=4
Closed cube: slice=0; winding plane: constant slice=8; quotient=0
Integer residue, cyclic primitive, median quotient: PASS
Insertion L=8 orientation=01: faces=21, degrees=4x5+32x2, neighborhood=137<=153, one component, exact slice coefficients: PASS
Insertion L=8 orientation=02: faces=21, degrees=4x5+32x2, neighborhood=137<=153, one component, exact slice coefficients: PASS
Insertion L=12 orientation=01: faces=21, degrees=4x5+32x2, neighborhood=137<=153, one component, exact slice coefficients: PASS
Insertion L=12 orientation=02: faces=21, degrees=4x5+32x2, neighborhood=137<=153, one component, exact slice coefficients: PASS
Exact floors: rho=2^-173; b_floor=25*rho; chi_floor=rho; difference=0
RESULT PASS; no uniform upper-chi estimate or positive P1 gap
```

The observed neighborhood size 137 is a finite audit result. The written
all-volume theorem retains its prospectively proved bound 153 and constant
rho=2^-173; no threshold or constant was optimized after this observation.

## Review and remaining scope

Two separate analytical agents derived the signed quotient independently.
A separate lower-bound derivation and review checked the positive primal
comparison, insertion bijection, no-overcount translation sum, L>=4 geometry
and exact infrared floor. Pre-pin review required an explicit finite-lift
qualification for the neutral-chain argument and a nonempty-profile
qualification for the comparison. Both are included in the frozen proof.
A separate static code/interface review found no blocker.

These reviews used shared sources and were not blind external acceptance.
This is one scientific architecture; ordinary repository CI does not run
this notes audit. No theorem grade, formal two-architecture scientific
gate, phase determination or Canon promotion is claimed from this run.
The signed ensemble upper estimate, a stronger transverse lower contribution
and the original strictly positive P1 comparison remain unresolved.
