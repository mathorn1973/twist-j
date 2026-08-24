# OWNER RULING R3: the photon transfer data (adopted per the decision sheet)

```text
DATE     2026-08-05
BASIS    the R3 decision sheet of 2026-08-05, owner directive "jdi
         podle doporuceni" adopting the recommended strike; owner
         ruling R1-B (the canonical lift); lane A recon
         (RECON-PHOTON-TRANSFER-DATA_2026-08-05); the step-2 moment
         recon (recon_alphabet_moments.py, 12 of 12 PASS).
```

## The ruling

```text
R3-W  W4 ADOPTED. The weight system of the photon transfer symbol is
      the shell-weight system on the machine's own completed shell
      family {2, 4, 8, 10, 16}, at the MINIMAL POSITIVE POINT of the
      N6 isotropy family, computed under the frozen criterion below:

          W* = (w2, w4, w8, w10, w16) = (6, 1, 15, 1, 1)

      CRITERION (frozen with the ruling): admissible points are
      integer weight vectors with every entry >= 1 (every deposited
      shell participates) satisfying the N6 cone
          -4 w2 + 32 w4 - 64 w8 + 440 w10 + 512 w16 = 0.
      Selected is the admissible point of minimal total sum(w); ties
      broken lexicographically in the order (w2, w4, w8, w10, w16).
      Computed: the minimizer is unique (total 24); the tie-break is
      displayed and unused. Proof by exhaustive enumeration of all
      positive 5-tuples with total <= 24, cross-checked by an
      independent elimination scan; both in the pinned verifier.

R3-F  F0 ADOPTED for the FIRST characteristic run: flat flux, zero
      holonomy on every triangle, the phase-free results apply
      verbatim. F2 (cell-inherited flux transported through the ruled
      lift) is the NAMED SUCCESSOR; it waits on one displayed map,
      fiber commutator classes to carrier triangle classes, which is
      itself a freeze with a falsifier. Flat first is the control leg
      the phased run is compared against, not a physics claim.

W5    COMMISSIONED. The derivation lane (weights produced by a named
      mechanism: path counts of the coupled dynamics, Born amplitudes
      of the quadratic leg, or a measure theorem) is commissioned as
      the lane that SUPERSEDES W* on arrival. Its arrival rewrites
      the decision sheet and is recorded, never silent.
```

## Witnesses at W* [computed, exact, two-platform]

```text
mass      sum w_n |S_n| = 288
M2        sum w <k,v>^2 = 648 |k|^2 exactly (M2 = 648 I)
M4        sum w <k,v>^4 = 3168 |k|^4 exactly (pure 3168 = 3 x 1056)
symbol    S(k) = sum w (cos<k,v> - 1) = -324 |k|^2 + 132 |k|^4 + R6
          exact Taylor coefficients 648/2 and 3168/24; the symbol is
          isotropic through FOURTH order
6th order ANISOTROPIC with exact display: k^6-type 21888, k^4k^2-type
          63360 (isotropy would need 65664), triple product absent
          (isotropy would need 131328). Every vector of the family
          has a zero coordinate, the planarity echo: the triple
          moment vanishes identically at every weight choice.
W*        primitive (gcd 1). The overall scale of W is a cone
          direction not fixed by isotropy; W* fixes it by integrality
          and minimality. The PHYSICAL pairing of that scale with the
          time leg is K3 material, named here and not ruled.
```

## Correction to the decision sheet, recorded

The sheet's W4 line called the N6 family "a one-parameter-family
choice after normalization". Wrong count: one linear condition on
five weights is a FOUR-dimensional integer cone, three parameters
after scale normalization. The correction changes nothing downstream,
the ruling selects one point either way; recorded because the sheet
is quoted. The sheet itself stays as written, corrections are
recorded, not silently edited.

## Scope

A lane dictionary ruling at note grade, like R1-B and the
EFFECT_SHADOW_MINIMAL freeze: no canon change, no registry row, no
status move. It binds this lane's candidates and recon; a public row
adopting it would be a separate fold.

## Moduli ledger

The photon lane now carries THREE owner choices, each with a named
supersession path:

```text
R1-B  the canonical lift            superseded by a derived-lift theorem
R3-W  the weight point W*           superseded by the W5 derivation
R3-F  flat flux first leg           superseded by the F2 displayed map
```

## Effect

```text
1  P-FCC-TRANSFER-SYMBOL-1 unblocks. The draft prereg is prepared
   (UNFROZEN, for cross-model blind review per the STOP discipline);
   no pin and no execution before that review and the owner process.
2  P-FCC-TIME-CHARACTERISTIC-1 has no remaining owner unknown: R1 and
   R3 are ruled and the standing clock-readout offer (n -> n, the
   temporal output map trivial, all content in the characteristic)
   covers its normalization. It queues behind the symbol probe.
3  The cone convergence test of ONE-CONE-TWO-ROUTES becomes reachable
   once the symbol row exists.
```

## Non-claims

W* is not derived from J; it is the minimal isotropy-restoring choice
on the machine's own shells, counted as a choice. F0 is not a physics
claim. Nothing here touches the sealed probe, the frozen candidate
records, or the public canon.

## Falsifier of the ruling's usefulness

A registered derivation selecting different weights (W5 supersedes,
recorded); the derived characteristic under W* failing its own
referee gates; a demonstration that the fourth-order deficit
functional is the wrong invariant for the flat sector. For the phased
(F1/F2) sector the functional is NOT claimed to apply.

## Pins

```text
verify_r3_w4_minimal_point.py
  sha256 116e04152ea95ba8ba861c9d01722f9aede7f950e1dac09b7fc5186513357400
  9706 bytes
stdout
  sha256 177ea11e06d82ee97fca49a7810506da7886ae5fced19411f89deb8540272840
  2060 bytes, 16 of 16 checks PASS, exit 0, stderr empty
runs   byte-identical on two architectures: x86_64 (Python 3.11.15)
       and aarch64 (Ubuntu 24.04, Python 3.12.3), both under
       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
       TZ=UTC
```
