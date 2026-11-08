# Evidence pins and independent review obligations

**NON-CANONICAL, L1. Independent acceptance pending.**
Author: A. M. Thorn. Apache-2.0.

## Authority and source custody

Current public main and canon-v105 were freshly fetched and agree at
892a0b11089d34e241e1eb76d2c03247022d18e6. The declared content commit is
b8cdfd6ea58ae798545bc6000c817147fa0f0dcc, an ancestor of main. The Canon
has 1295029 bytes and SHA-256
73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31.
STATUS, POLICY, AGENTS, CORE, FRONTIER, current issue reservations,
coordination ownership and live remote heads were checked. The new lane
does not modify the separate #1775 source or any frozen predecessor.

The principal mathematical input is the public text at
[#1775 comment6399173427](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399173427):
ACTIVE_EQUAL_SPECTRUM.md, 23985 bytes, SHA-256
c6c5e76e48014ba8f670ff9ae8ea44557867b9dc92de38cef94a5e527bad7e5f.
The original ten source-content hashes and their published manifest
were verified during the preceding analytical triage. The original
reported commit is 17147b63f12765e6888be60600dd8c0b280516e7, parent
3abf054e435e31c51e6e50528b09fe3cf7cffe13. This source is cited by its
verified public text hash; no assertion is made here that its reported
commit was independently imported or published as a remote ref.

Other exact sources:

- Canon v105, Section 2: original Omega, selector, generators and chart.
- Canon v105, HOMOGENEOUS-CAPTURE-CURRENT-RECORD: active space, original
  occupation codes, receiver and phase-zero intertwiner I_0, especially
  [lines27986 onward](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27986).
- [SOURCE-PHASE-NATIVE proposal](https://github.com/mathorn1973/twist-j/blob/5ce14091995dfdc0e57fe7b256b72aed6f16ac3e/notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md),
  pin5ce14091995dfdc0e57fe7b256b72aed6f16ac3e: added coefficient field and
  the direction of its residue semiconjugacy.
- [PR1772](https://github.com/mathorn1973/twist-j/pull/1772),
  3abf054e435e31c51e6e50528b09fe3cf7cffe13: exact amplitude scale and
  selected-log locality boundary, not a native source loader.
- [PR1774](https://github.com/mathorn1973/twist-j/pull/1774),
  3de02b0eb898f1756e3626ee2881d596c72d0094: finite-prefix simulation and
  a differently encoded funded archive, not preparation of this source.

The working branch for this successor starts from the last pin above.
All pre-existing tracked files remain unchanged. This directory contains
only new English analytical notes.

## Review obligations

1. Recheck the exact #1775 source identities and distinguish their pending
   status from Canon facts and new conditional deductions.
2. Verify that U_rec^(+/-2) on the whole seed-memory subspace stays left
   of the receiver and has the same fixed source factor for every memory.
3. Verify the complete Householder R, SELECT signs, controlled scalar
   phase, inverse calls and exact good block (I+U^2-U^-2)/3.
4. Check Z>9/4, the real attenuation coefficients, and that the new
   calibrated rotation is counted rather than derived from U_rec.
5. Prove P_in A* P_good A P_in=P_in/4 and the single exact amplification
   identity on the entire unknown-memory subspace, not a single vector.
6. Verify full raw complements, no postselection, all helper return,
   coherent setting phase, and the 29/31 named-operation counts.
7. Check the six-coordinate-radius preparation cone and period-15
   completion, without converting admitted-input equality to global
   equality of finite and infinite dynamics or their spectral measures.
8. Check the actual occupation gauge I_0, the injective 29-site encoding,
   ternary active values, the transient integer h=2 level of charge8,
   2204 occupation bits, n=2208, and charge10 code.
9. Verify Givens elimination, Gray paths, AND scratch restoration and
   routing bounds 8n^2 4^n and 128n^3 4^n on complete finite spaces.
10. Check that local energy support includes every occupation partner,
    every finite ladder boundary fiber has a unitary definition, and
    all actual histories remain in complete energy fibers.
11. Check Q_max=8816, b_0=17632, B=26468, the 4414 ladder sites, their
    coherent routing/return, and the bound 512n^4 4^n.
12. Verify fixed-strength local logarithms, runtime and free-frame
    treatment, and that driven control is not called autonomous.
13. Keep epsilon H_N separate from Q=E0 f(U_rec), and verify the stationary
    target distance and covariant-input asymmetry bounds.
14. Check the complete three-qubit thermal permutation, reference-uniform
    reset channel, donor counts, temperatures, energy/entropy flow and
    absence of hidden donor replacement within one reset proof. Check
    the concrete 2209-helper, 220900-donor and 10934550-operation option.
15. Verify the distinction between linear reduced-reference error and
    the generic square-root full-donor decoupling bound.
16. Verify every joint preparation/evolution/readout error coefficient;
    no material tolerance, physical detector or outcome occurrence is
    inferred from the mathematical probability bound.
17. Check nonzero source overlap, retained coherent setting phase, the
    exact 2^N garbage bound and limits of the no-perfect-catalysis proof.
18. Preserve the K25 old-memory scope, full26 preparation scope, and the
    explicitly additional qubit required by the optional full26 flag code.
19. Check the first-step native collision, synchronized chart, residue
    no-inverse counterexample, true zero-sum SWAP/eigenphase and its
    checkpoint-diagonal readiness lower bound.
20. Check the native dictionary typing and all unresolved admission,
    seed, phase, precision, controller, reset and physical-energy inputs.

An exact failure in any stated operator identity, dimension, support or
error estimate falsifies the corresponding claim. A construction outside
a no-go hypothesis is not a counterexample to that scoped theorem.

## Validation method and operational scope

The proofs were developed and cross-read within one authoring session.
The native-boundary and source-circuit roles cross-checked each other;
the source and native roles also checked the coordinating author's
generic local synthesis and reservoir construction. The resource role
separately derived its complete thermal channel and reset bounds.
This is not independent mathematical acceptance.

No new scientific executable, simulation, expanded gate enumeration,
formal probe or empirical measurement was run. Existing repository
integrity checks and document custody checks are recorded after actual
execution below. They do not prove the new mathematics. New CI, a remote
ref, a public PR or an independent review must not be inferred from this
local analytical package.

Actual existing local checks passed:

| Check | Observed result |
| --- | --- |
| check_policy.py | POLICY PASS |
| check_canon.py | CANON PASS v105 claims=577 |
| check_ledger.py | LEDGER PASS claims=577 items=641 dependencies=1160 evidence=577 history=1124 gates=26 programs=7 |
| check_gate_contract.py | GATE CONTRACT PASS gates=26 |
| Tracked predecessor comparison | No changes against base3de02b0eb898f1756e3626ee2881d596c72d0094 |
| New text checks | Valid UTF-8/LF; no trailing whitespace or private environment markers |

The full 210-test suite and new CI were not run for these new analytical
notes. No remote publication, independent acceptance or scientific
promotion is reported by this validation record.

Two material draft issues were corrected during same-session review:
the occupation realization now retains the exact I_0 gauge, and the
fourth two-bit level is the real integer h=2 with charge8. Consequently
the reservoir figures are Q_max=8816, b_0=17632 and B=26468. This avoids
introducing a second zero-energy h=0 level. Free-frame equality, dirty
scratch complements and driven control remain explicit qualifications.
