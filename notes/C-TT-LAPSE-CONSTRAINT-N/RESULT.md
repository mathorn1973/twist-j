# C-TT-LAPSE-CONSTRAINT-N: local result record

**NON-CANONICAL. No authority, no public verifier gate, no Canon promotion,
no O/H closure.** Exact identities and arrays candidate-T; construction and
its declared choices candidate-D. Conclusions rescoped after the owner review
of 2026-09-08; the frozen preregistration and the first two verifiers are
unchanged.

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
verify_review_addendum.py (frozen 2026-09-08T16:20:38Z, after the review, before its run)
  sha256                   1ac036812809675ff0560d2eb424a71da3fd659968165b2ac6c8c73cec3c62f2
  run                      exit 0, 10 checks, 0 failed, stderr empty
  stdout                   EXPECTED-addendum.txt
                           sha256 ba7a54b61c9aae0fd3b4943a16b95cb64cdb722c6881b1b58ac03cc548a3bda6
environment, leg 1         x86_64, Ubuntu 24.04, Python 3.11.15,
                           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
environment, leg 2         arm64, macOS 26.5, Python 3.13.13, same variables;
                           all three verifiers rerun from the same frozen bytes:
                           exit codes 1, 0, 0, stderr empty, stdout byte-identical
                           to leg 1 (same three SHA-256 above)
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

## Kinds of check, stated plainly

In `verify_fixture_corrected.py`: the sector decompositions (K1) are exact
polynomial identities; the constraint arrays (K6) are exact finite-array
equations with assertions inside `solve_tau`; the variation check (K3)
audits random exact configurations at two values of `lambda`, which is not a
universal certificate; the K7/F5 line is `check(..., True)`, a declaration;
the F4 line counts distinct strings in a hand-written sector table. The
review addendum replaces the declarative and sampled items by certificates:
A4 symbolic Euler-Lagrange identities in all 105 field, 15 source and the
`1/lambda` variables; A5 lapse linear and its equation lapse-free; A6
computed coefficient census (370 monomials, coefficients rational multiples
of `lambda^0` or `lambda^(-1)`). The F4 statement remains descriptive.

## What the runs establish, at scope

- The planar sector decomposition of the discrete linearized ADM action
  (polynomial identities).
- The seven sector equations as polynomial identities in all variables; the
  lapse equation algebraic and lapse-free (F2 record).
- Homogeneous quadratic coefficient `-(3/lambda)(Delta Phi)^2` per site,
  the `FRW-CANONICAL-FORM` sign and coefficient; the predecessor's pairing
  gives `+24` at the same place (F1 record at quadratic scope).
- Zero mode: the complete constraint `L tau = sigma` has no solution on the
  static flat compact carrier for any K1 word in either reading; the
  projected arrays satisfy `L tau - sigma = -mean(sigma) 1 != 0` (A3).
- Source reading: the conservation continuation is not K1-form in twenty of
  twenty cases (F6 fires at that scope).
- Decoder reading: projected `tau = L^+ (sigma - mean sigma)` exact and
  rational for all ten words; the two declared transcriptions differ by
  exactly `(1/2) L(h^2)` in the source and `(1/2) Pi(h^2)` in `tau`, from the
  polynomial identity `L(h^2) = 2 h L h - 2 g(h)` (A1, A2); `+3/40` at
  occupied and `-1/20` at empty sites at cut 0.
- The vector witness `h_13 = n f(r)` satisfies every displayed equation
  (A7): the system, having no shift, has no momentum constraints.
- `Z_n = sum sigma_i` is not conserved by the free TT equation,
  `Z_1 - Z_0 = (1/4)||L f||^2`; the staggered cross-slice form is (A8).

## What they do not establish

No complete constrained gravitational model; no momentum constraints; no
solution of the full Hamiltonian constraint (only of its projection); no
FRW background or its nonzero-mode equations; no common cubic action for the
second-order source and no derived time placement; no `P_S`, no `r_T(k)`, no
cosmological identification of `tau`, no physical amplitude; no
three-dimensional carrier; no Regge-Wheeler coefficient. No owner condition
C1 to C5 is claimed complete. One author, one code path, two local
architectures: not an independent confirmation and not the public
two-architecture gate. No original O/H closes.
