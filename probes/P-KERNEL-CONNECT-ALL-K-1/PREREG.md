# PREREG. P-KERNEL-CONNECT-ALL-K-1

```
LAYER:  L1 (state). No lift to any other layer is claimed.
TARGET: KERNEL-CONNECT-ALL-K [H] (canon section 3 and section 18).
```

## The five frozen fields

```
EQUATION     U := the smallest subspace of F_5^6 containing the letter
             translations {v_c, v_d, v_e} with M_g U = U for every
             g in {a, c, d, e}, letters the verbatim census generators of
             reproduce/kernel-connectivity, v_g = g(0):
             v_c = (2,1,2,1,1,0), v_d = (2,1,3,4,1,1), v_e = (2,1,3,4,2,1).
             Decision: dim U = 6 proves, by the confinement, extraction,
             and transport lemmas of the candidate record, that the
             diagonal letters {a, c, d, e} with the two way CSUM ring
             transvections connect (F_5^6)^k into one component for every
             k >= 2, uniformly in k; dim U < 6 would prove more than one
             component for every k >= 1 and close the row negatively.
CODE         verify.py = verify_kernel_connect_all_k.py of this package,
             sha256 b6fd3cb513987aae9b9c6d5a5c31e26c2c9a34b4610582e8c8072ffaa33cccbc
             (19840 bytes). Python standard library only, exact arithmetic,
             no floats in any assertion, deterministic, under 120 s, run
             from repo root with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC.
CARRIER      the frozen coupled ring model: cells Z_k, cell space F_5^6,
             moves the diagonal letters D_g (g in {a, c, d, e}, applied at
             every cell, the diagonal action of the registered wedge
             cluster) and R_i: x_{i+1} += x_i, L_i: x_i += x_{i+1} for
             every ring index i mod k. At k = 2 this is the registered
             pair transvection model. The per-cell letter variant contains
             the diagonal letters as products, so the positive result
             covers it a fortiori.
SYSTEMATICS  (1) the sealed internal k = 2 and k = 3 witnesses are not
             public and are not used; the owner confirms at the fold that
             the frozen reading matches their scope. (2) incubation
             history: the identical verifier already ran in the project
             incubation lane on x86_64 (stdout sha256 15685afb...9709,
             RESULT 8/8); the public runs are the formal legs. (3)
             verifier implementation defects are amended openly with the
             pin history retained and are not fired falsifiers.
THRESHOLD    FIRE if gate 02 reports dim U < 6 (closes the row negatively
             for every k). FAIL-KILL if any lemma-instance gate (03, 04,
             05, 06, 08) fails: kills the candidate proof, not the row.
             Gates 01 or 07 failing void the import of the public census
             and the probe aborts.
```

Falsifier for the closed row: an exact recomputation of the module closure
giving a dimension other than 6, or an exhibited pair of states at any
k >= 2 provably in different components of the frozen model.

Expected stdout: byte identical to EXPECTED.txt recorded at the formal
aarch64 run; the incubation stdout sha256 is
15685afbb9a96ca4ba2cb3787b4ddd74b57cd9d89436350ca7b4ee9542ac9709 and the
output is platform neutral, so the formal legs must reproduce it byte for
byte.
