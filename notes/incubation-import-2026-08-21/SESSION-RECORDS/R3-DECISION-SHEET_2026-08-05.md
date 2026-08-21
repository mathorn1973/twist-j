# R3 DECISION SHEET: the photon transfer data, with computed verdicts

```text
STATUS   NON-CANONICAL decision sheet for the owner ruling R3. No
         authority, no claim, no probe. Prepared so that R3 is one
         strike, not an essay. Basis: owner ruling R1-B (2026-08-05),
         lane A recon (RECON-PHOTON-TRANSFER-DATA_2026-08-05), and the
         step-2 moment recon below.
PINS     recon_alphabet_moments.py
         sha256 e477599af8fa56cf7aed7d798db2bdc5690d6d811c81c976fdd5e067dbdae6c1
         stdout sha256 7178f7612f724032a29b7ed703f6b09f164e795222ff0bfdfb5c8e076071807f
         12 of 12 checks PASS, exit 0, stderr empty. Exact arithmetic.
```

## New computed facts (step-2 moment recon, all [computed, recon])

```text
N1  UNIQUE LIFTS. Every one of the 20 deposited classes has exactly ONE
    minimal-norm integer lift. The minimal-lift convention involves no
    choice at all; the alphabet lifts to exactly 20 vectors.
N2  PLANARITY. All 20 lifted vectors are COPLANAR: they span a rank-2
    sublattice (in the ruled coordinates, second coordinate 0
    throughout; coplanarity is invariant under the point-group
    ambiguity retained by R1-B). Mod 5 the classes spread through the
    kernel; over Z the minimal lifts flatten into one plane. Reading
    OPEN, not claimed; the span question (mod 5 versus over Z) is a
    named follow-up.
N3  UNIFORM-ON-ALPHABET IS EXCLUDED for isotropy: anisotropic already
    at SECOND order, M2 = diag(60, 0, 100). Same for per-class weights
    (identical by N1). Exact witness, first exclusion in the R3 space.
N4  THE SYMMETRIC COMPLETION IS FIVE COMPLETE SHELLS. The 48-closure of
    the lifted alphabet is exactly the full shells of norms
    {2, 4, 8, 10, 16} with sizes {12, 6, 12, 24, 6} (each shell is one
    group orbit; 60 vectors). Second order isotropic (M2 = 160 I).
N5  UNIFORM-ON-COMPLETION IS EXCLUDED at fourth order: deficit exactly
    +916 per coordinate. Second exclusion, exact witness.
N6  THE LIVE ISOTROPY CONSTRAINT on the machine's own shell family:
    with the frozen deficit functional, shells (2, 4, 8, 10, 16) carry
    a = (-4, +32, -64, +440, +512), and fourth-order isotropy of a
    shell-weight system (w2, w4, w8, w10, w16) is the ONE equation
        -4 w2 + 32 w4 - 64 w8 + 440 w10 + 512 w16 = 0,
    equivalently w2 = 8 w4 - 16 w8 + 110 w10 + 128 w16.
    Cross-check: uniform weights give -4+32-64+440+512 = 916, matching
    N5 independently.
N7  the seed class lifts to the single vector (1, 0, -3) (norm 10).
```

## The R3 choice space, one line per option

**Object W, the weight system.**

```text
W1  uniform per vector on the alphabet lifts      EXCLUDED (N3)
W2  uniform per class                             EXCLUDED (N1 = W1)
W3  uniform on the symmetric completion           EXCLUDED at 4th
                                                  order (N5, 916)
W4  shell weights on the deposited family {2,4,8,10,16} constrained by
    N6 (a one-parameter-family choice after normalization; the
    isotropy-restoring family of the machine's own shells).
    Falsifier: the derived characteristic under the chosen W4 point
    fails octahedral invariance, or a later derivation forces a
    different point.
W5  a DERIVED weight system: weights produced by a named mechanism
    (path counts of the coupled dynamics, Born amplitudes of the
    quadratic leg, or a measure-theorem). No such derivation is
    registered today (lane A verdict EMPTY); choosing W5 means
    commissioning that derivation first.
W6  owner-declared other (displayed, with its own falsifier).
```

**Object F, the flux.**

```text
F0  flat (zero flux). The phase-free results apply verbatim.
    Falsifier: any registered transport of the cell-level fiber
    commutators to the carrier that is nonflat.
F1  uniform flux f in Z_5 on the single triangle orbit (one number,
    four nonzero choices). Opens the magnetic (Weyl pair) sector;
    the scalar-symbol framework no longer applies and the
    characteristic must be posed on the magnetic cover.
F2  cell-inherited flux: transport the registered fired fiber
    commutator table through the ruled lift. Requires one additional
    displayed map (fiber to triangle classes); that map is itself a
    freeze with a falsifier.
```

## Recommended strike (one line each, owner's to accept or replace)

```text
R3-W: adopt W4 with the MINIMAL positive point of the N6 family as the
      working point, displayed at freeze time, labeled an owner choice
      in the moduli ledger; commission W5 (the derivation) as the lane
      that can later supersede it. 
R3-F: adopt F0 (flat) for the FIRST characteristic run, with F2 named
      as the successor once the fiber-to-triangle map is displayed.
      Flat first is not physics; it is the control leg the phased run
      is compared against.
```

## What runs immediately after R3

```text
1  P-FCC-TRANSFER-SYMBOL-1 (draft identity, UNFROZEN until R3): one
   ambient Z^3, the five shells and W displayed in the prereg, the
   operator symbol and its exact fourth-order expansion, octahedral
   invariance as the symmetry referee gate. Pre-pin blind review by
   the other model family per the STOP discipline.
2  P-FCC-TIME-CHARACTERISTIC-1 (draft identity, UNFROZEN): adds the
   time transfer and the joint null characteristic det C(omega,k) = 0;
   the owner's recorded offer applies (clock readout declared n -> n
   makes the temporal output map trivial and puts the whole content in
   the characteristic).
3  the cone convergence test of the ONE-CONE-TWO-ROUTES formulation,
   once route 2's label allows.
```

## Falsifier of this sheet

Any computed fact N1 to N7 failing exact recomputation; a registered
derivation appearing that selects weights (then W5 supersedes and the
sheet is rewritten, recorded); a demonstration that the deficit
functional is the wrong invariant for the phased (F1/F2) sector, where
it is NOT claimed to apply.
