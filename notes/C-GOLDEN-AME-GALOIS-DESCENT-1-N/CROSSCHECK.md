# Independent cross-check

`crosscheck.py` is a second standard-library implementation. It shares only
the frozen source and preregistration, and imports no code from
`verify_galois_descent.py`.

It independently confirms:

```text
labeled G_mod = {1,21}
fixed field   = Q(zeta_20), degree 8
party (2 3)   = no additional transporter
```

For every one of the 16 Galois automorphisms it enumerates 73,728 raw local
permutation tuples. The eight automorphisms exchanging `a` and `b` have no
colored-support candidate. In the label-preserving class, only `k=1,21` have
a phase lift over both `Z/5` and `Z/8`. The JSON includes every phase audit,
all-entry substitution checks, and left-null certificates.

Run:

```sh
python3 crosscheck.py AME46_ORIGINAL.m --output CROSSCHECK.json \
  > EXPECTED_CROSSCHECK.txt
```

The committed transcript and JSON are deterministic under changed
`PYTHONHASHSEED`.

## Detailed conclusions

The exact amplitude table is:

| `k` | `sigma_k(a)` | `sigma_k(b)` | `sigma_k(c)` |
|---:|---:|---:|---:|
| 1 | `a` | `b` | `c` |
| 3 | `-b` | `a` | `-c` |
| 7 | `-b` | `a` | `c` |
| 9 | `-a` | `-b` | `c` |
| 11 | `a` | `b` | `-c` |
| 13 | `b` | `-a` | `-c` |
| 17 | `b` | `-a` | `c` |
| 19 | `-a` | `-b` | `-c` |
| 21 | `-a` | `-b` | `-c` |
| 23 | `b` | `-a` | `c` |
| 27 | `b` | `-a` | `-c` |
| 29 | `a` | `b` | `-c` |
| 31 | `-a` | `-b` | `c` |
| 33 | `-b` | `a` | `c` |
| 37 | `-b` | `a` | `-c` |
| 39 | `a` | `b` | `c` |

There are exactly two support-preserving labeled tuples,
`(id,id,id,id)` and `(id,id,t,t)` for `t=(0 1)(2 3)(4 5)`. The second has no
phase lift even for `k=1`. The detailed solvability signatures modulo
`(5,8)` for these two tuples are:

```text
k=1:  (yes,yes), (no,no)
k=9:  (no,no),   (no,yes)
k=11: (yes,no),  (no,no)
k=19: (no,no),   (no,no)
k=21: (yes,yes), (no,no)
k=29: (no,no),   (no,yes)
k=31: (yes,no),  (no,no)
k=39: (no,no),   (no,no).
```

Each rejected colored candidate in `CROSSCHECK.json` carries an explicit
sparse dual vector. The certificates satisfy either

```text
y^T A = 0 mod 5,  y^T b = 1 mod 5,
```

or

```text
y^T A = 0 mod 8,  y^T b = 4 mod 8.
```

The only normalized lifts are `k=1,h=0` and `k=21,h=20`, with all 24 local
exponents zero, checked by substitution into all 112 equations. The latter is
coherent because `21*20=20 mod 40` and its order-two cocycle exponent is
`20+20=0 mod 40`.
