# Exact integer joint field-source variation

NON-CANONICAL, L1. Ownership issue:
https://github.com/mathorn1973/twist-j/issues/1645.

This probe builds a selected discrete linear TT metric and scalar source
whose continuing reciprocal equations follow from one quadratic action:

    (Delta_c^2+L) h_n = chi_n ell / 324^n,
    (Delta_c^2+1) chi_n = a - <ell,h_n>/324^n,
    ell=(1,-1,0,0,0), a in {-1,0,+1}.

The common scale D_n=2*324^(n(n-1)/2) stores both h_n and chi_n exactly
as integer numerators. The unrestricted 21-coordinate core has an exact
six-congruence inverse. A transported Hermitian register over Z[j] realizes
the source numerator on ready states through its c1 coordinate.
Adding bank and direction gives a total reversible 23-coordinate funded
map with conserved positive arithmetic account E+b and finite shells.

The full metric/lapse/shift/source first variation is proved analytically.
The primary and separate breaker check 720 exact reduced TT-plus-source
derivatives on solutions and 36 derivatives off solutions, together with
390 history records, image guards, source holonomy, negative controls,
sharp budgets and complete least-period paths.

The first formal run passed with a 589-byte, 21-line stdout. Its raw
19-line certificate matched the independently authored breaker exactly.
The finite output is in EXPECTED.txt; the all-counter results are proved
in PROOF.md, including

    |chi_n-chi_n(free)| < 2/323,
    ||h_n-h_n(free)||_inf < 1630/209304 < 1/125,
    -299/500 < h_n(r) < 499/500.

For word 0011 and a=0, an initially zero source becomes chi_2=1/648.
It changes the metric at counter three by ell/68024448. Continuing
backreaction changes chi_3 by a further 71/68024448 relative to the
first-impulse-only control. The sharp bank for the first step is 89368.

## Read and reproduce

- PREREG.md freezes the equations, carrier, fixtures, falsifiers and
  certificate grammar before execution.
- PROOF.md gives the full action, inverse, account, holonomy, causal
  bounds, exact witnesses and period arguments.
- SOURCE.md identifies the actual authority bytes and every declared
  modeling choice and companion input.
- verify.py uses scaled integer evolution, polynomial quotient and
  2x2 Hermitian matrix arithmetic, and a direct quadratic action.
- breaker.py independently uses rational evolution, direct Hermitian
  coordinates and an independently arranged action.
- FROZEN.sha256 commits the five prospective source files.
- RUN.md, RESULT.md and EXPECTED.txt record the first execution and its
  exact earned scope; REVIEW.md describes the internal review roles.

From the repository root, using Python 3.12 and the standard library:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 probes/P-INTEGER-JOINT-VARIATION-1/verify.py

The complete stdout must match EXPECTED.txt byte for byte and ends with:

    CERTIFICATE_RESULT=PASS
    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The unchanged repository PR workflow replays the verifier and breaker
on both x86_64 and aarch64. Actual workflow receipts belong in the draft
PR after the jobs finish; RUN.md records the first local execution.

## Exact scope

The source kinetic sign is negative relative to the TT field sector.
This is a selected joint-action model, not a result that integer arithmetic
requires that sign. Physical matter admissibility, a positive physical
Hamiltonian and quantum stability are not established.

The common denominator is sufficient but not claimed primitive or
optimal. The Hermitian register is an invertible amplitude realization
and monitor; the source law itself is newly declared. The account is
an arithmetic admission cost, and k is a counter. The model does not
derive native TWIST-J U, full nonlinear general relativity, a continuum
manifold or a physical clock. These remain separate research obligations.
