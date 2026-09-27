# RUN - C-HEXAGON-HODGE-PHOTON-SEAM-N

**Status:** candidate-C corroboration only. Not a formal public probe.  
**Owner:** issue #1219.

## Public custody before execution

- branch execution basis: `2a8b368ece347a6b291d727415211de41cb51c4c`
- `PREREG.md` blob: `75967843fb2893259008e7fed7c727d4b6cb121c`
- `verify.py` blob: `841383125bacd68f39939be75d6831c4111f7dc8`
- `break.py` blob: `ed5aea5cb6c8035929fd064e8b9be70885587a6f`
- `PREREG.md` SHA-256: `e367566c4fe27332567e7536a2daba9b00dbcaa7f8081b20110a64ec7ffcc98f`
- `verify.py` SHA-256: `c6dc3677381182e29bd01da087003d53860e8b24b054e263294ad485e4db199a`
- `break.py` SHA-256: `9c9410f046f851a75928b7d4ebd12db227e0e6026b06ef2dc6840957d4d799ba`

All three files were publicly read back through the GitHub connector before
execution. The local executable copies had Git blob hashes byte-identical to
the public `verify.py` and `break.py` blobs.

## Exact local execution

```text
platform: Linux
architecture: x86_64
python: Python 3.13.5
verify_exit_code: 0
verify_stdout_bytes: 668
verify_stderr_bytes: 0
verify_stdout_sha256: d6471afff9cf4d986ab159e6e7d6d157488d9207c0c0e431b7d97fcccc1a8227
break_exit_code: 0
break_stdout_bytes: 486
break_stderr_bytes: 0
break_stdout_sha256: 5de009330663c665730cf188b82ffcdc44534e3dcac331520a4756de04714773
```

Exact verifier stdout:

```text
PASS G1: planar-hexagon coordinate matrix has |det|=48; antipodal odd triple is reducible under the cycle.
PASS G2: marked exterior J-step charpoly is (x^2-3x+1)(x^4-x^3+x^2-x+1).
PASS G3: wedge^2 of the fixed-J Lorentz-chart step has the frozen exact charpoly and gcd(pW,pB)=1.
PASS G4: same-step intertwiner class S L = B S is zero by coprime characteristic polynomials.
PASS G5: for all m,n>=1, dim Hom(L^m,B^n)=0 if 10 does not divide m, 8 if 10|m and m!=n, 12 if 10|m=n; never invertible.
PASS G6: axial recurrence preserves y^2-3yz+z^2; this is an algebraic (1,1) form, not a photon propagation law.
ALL PASS: C-HEXAGON-HODGE-PHOTON-SEAM-N exact audit complete.
```

Exact breaker stdout:

```text
PASS BREAK-1: same-step source and target spectra are disjoint.
PASS BREAK-2: separate label census matches the all-positive-integer blocked Hom formula on the frozen audit grid.
PASS BREAK-3: source and target eigenvalue multiplicities never match, so blocking never yields an invertible semisimple intertwiner.
PASS BREAK-4: target time reversal has the same spectral multiset and does not repair the obstruction.
ALL PASS: breaker found no counterexample in its frozen exact census.
```

The universal blocking theorem rests on `PROOF.md`; the finite loops in both
scripts are audits, not the theorem.
