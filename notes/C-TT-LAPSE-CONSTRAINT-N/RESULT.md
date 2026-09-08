# C-TT-LAPSE-CONSTRAINT-N: local result record

**NON-CANONICAL. No authority, no public verifier gate, no Canon promotion,
no O/H closure.** Conditional mathematics candidate-T; construction and its
declared choices candidate-D.

## Freeze and execution order

```text
PREREG.md frozen           2026-09-08T15:43:42Z
  sha256                   e0bb69848b442974ac6b69d32f1794547bdd982696bbb947e06077714e8f0af8
verify.py (first, frozen)  sha256 72664e56e677b38756705c7daeaef6afa674cda86449388a9c08f0f6a82b25d6
  run                      exit 1, 24 checks, 1 failed, stderr empty
  stdout retained          RUN-verify-first.txt
                           sha256 44c6ab2f1e65aff8f072ad0fe0eccc460f0623aca680a9b3c164fc0f7de25894
verify_fixture_corrected.py (successor, frozen before its run)
  sha256                   49ffc5142cee20bc3eb4ba16d97cc1a9f9530b1a81dfe6c52c610c875e647752
  run                      exit 0, 24 checks, 0 failed, stderr empty
  stdout                   EXPECTED.txt
                           sha256 741c8128fa777d5d7f5443aea2f9cdc13dfddec0c147a328b14860c7efe0bfa2
environment, leg 1         x86_64, Ubuntu 24.04, Python 3.11.15,
                           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
environment, leg 2         arm64, macOS 26.5, Python 3.13.13, same variables;
                           both verifiers rerun from the same frozen bytes:
                           exit codes 1 and 0, stderr empty, stdout byte-identical
                           to leg 1 (same two SHA-256 above)
```

Two architectures, byte-identical stdout, one author and one code path. This
is a local two-architecture reproduction record; it is not the public
GitHub x86_64 check at pull-request time and earns no public gate.

## Fixture disposition

The first frozen verifier failed exactly one check,
`K6 tau is a function of (u_0,u_1): 8 classes, ...`. The expected class
count was written as 8; the K1 joint law has nine `(u_0, u_1)` pairs, with
`0101` and `1010` sharing `(0, 0)`. The scientific content of that check
(that `tau` depends on the word only through `(u_0, u_1)`, and that the two
`(0,0)` words agree) is unaffected. The successor file differs from the
first in exactly two characters of that expected value (`diff` retained in
the pull request description) and was frozen before execution. The failed
run is not counted as a success and the first file is not modified.

## What the run establishes, at scope

- The planar sector decomposition of the discrete linearized ADM action:
  TT pair with the physical wave sign, transverse trace with the opposite
  gradient sign and a kinetic term only through the longitudinal coupling,
  longitudinal and vector directions without gradient energy, lapse
  multiplying only the transverse trace.
- The seven sector equations by exact variation of the explicit action, at
  two values of `lambda`; the lapse equation is algebraic (F2 no fire).
- The homogeneous limit gives `-(3/lambda)(Delta Phi)^2` per site, the sign
  and coefficient of `FRW-CANONICAL-FORM` (F1 no fire at linearized scope);
  the predecessor's pairing gives `+24` at the same place.
- The zero mode of the Hamiltonian constraint has no static flat solution for
  any K1 word in either reading; the homogeneous FRW sector is forced.
- Source reading: the conservation continuation is not K1-form in twenty of
  twenty cases (F6 fires there).
- Decoder reading: the constrained scalar `tau = L^+ (sigma - mean sigma)`
  is exact and rational for all ten words, `O(a^4)`, `lambda`-free; the two
  declared lattice transcriptions agree on the zero mode and differ on every
  nonzero-mode array (F6 no fire there; the fork is open).
- Flat-level spin structure: three distinct sector behaviours (F4 no fire at
  that level; the Regge-Wheeler coefficient is not reached).

## What it does not establish

No `P_S`, no `r_T(k)`, no cosmological identification of `tau`, no physical
amplitude, no discrete Bianchi identity at second order, no FRW-background
`k != 0` equations, no three-dimensional carrier, no RW coefficient. One
author, one code path, two local architectures: not an independent
confirmation and not the public two-architecture gate. No original O/H
closes.
