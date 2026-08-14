# Local CAS inventory

Inventory date: 2026-08-14.  This is the current Codex scratch sandbox, not a
statement about NUC, JAS 2, MINI, PIJAM, or PIS.

```text
OS             Ubuntu 24.04.3 LTS, x86_64, Linux 6.18.35
Python         3.12.13
NumPy          2.3.5
SciPy          1.17.0
GMP runtime    libgmp.so.10
MPFR runtime   libmpfr.so.6

SageMath       absent
Singular       absent
Magma          absent
Macaulay2      absent
PARI/GP        absent
Julia/OSCAR    absent
GAP            absent
CoCoA          absent
Maxima/Reduce  absent
Mathematica    absent
Maple          absent
QEPCAD         absent
Z3             absent
SymPy          absent
python-flint   absent
cypari2        absent
```

The only local exact test path used here is Python's standard-library
`fractions.Fraction`.  NumPy and SciPy were not used for algebraic claims.

`selftest.py` SHA-256 after the passing run:

```text
ff928f0d566e29b40a26fd7637e2095c6e7b9b4e0ec40323385274cf2aa9b1c7
```
