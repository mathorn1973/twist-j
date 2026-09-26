# RUN: first exact polymer-tree audit

**PUBLIC, NON-CANONICAL.**
Owner issue: #1168
Author: A. M. Thorn
Date: 26 September 2026

## Frozen input

Candidate pin:

`ea6d059ed3f7bf64b9cb05e1606583235df69856`

GitHub readback before execution:

- `PREREG.md`
  - Git blob: `360584dff5fad3557e5025a6d59a9b0543a25541`
  - SHA-256: `d468043a049d8afd444c1ffc30696354112f83a557250dc074bc7277091593ae`
- `verify.py`
  - Git blob: `11886675f5b28ae5b5353345320cd35ab1549931`
  - SHA-256: `9a38377e85bc3f6f195b749c981520c9f7e726de61773363d5df7822f5fc8d50`

## Environment

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

One architecture only. No two-architecture scientific gate is claimed.

## Command

```text
python3 verify.py
```

## Result

```text
exit_code: 0
stdout_bytes: 405
stderr_bytes: 0
stdout_sha256: 34c1fdf9ab073f7d2b2fa12f89c6b852132d37458eaf8d45398e3e518e364847
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout:

```text
LOCAL_CELLS PASS root_faces=6 incident_per_face=4 root_children=18 planted_children=15
CONFLICTS root_edges=42 planted_edges=31
P6 1,18,111,308,429,294,79
P5 1,15,74,154,143,49
SERIES PASS degree=12
H_COEFF 1,18,381,9020,229104,6104058,168340282,4765055808,137652453735,4041954733588,120286041826002,3619888728570540
LOCAL_TREE_CERTIFICATE NONE
AUDIT PASS; local_majorant=NO_CERTIFICATE; Xi=OPEN; P1=OPEN
```

Stderr is empty.

The frozen result is the preregistered negative branch of the local criterion:
all local cubical checks passed, but none of the frozen `y>1` candidates had a
dyadic `q` certificate.

The written result strengthens this finite search analytically: the exact
derived polynomial satisfies `P5(u)>16u` for every `u>=0`, so the local
recursive majorant diverges already at `y=1`. That theorem is not an
additional computation.
