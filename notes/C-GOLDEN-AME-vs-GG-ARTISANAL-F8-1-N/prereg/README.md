# Artisan F8 preregistration package

This directory is the pre-computation package for
`C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N`.

Its purpose is to freeze the experiment before any target invariant is
evaluated.  The normative specification is `PREREG.md`; exact external byte
pins are in `SOURCE_PINS.json`.

The two computational files are standard-library Python:

- `diagram_classifier.py` exhausts only abstract permutation diagrams.  It
  has no tensor or source-file interface.
- `construction_skeleton.py` freezes the direct Gross–Goedicke construction,
  field representation, locator, edge labels and contraction path.  Its CLI
  executes arithmetic/label self-tests only.  Its post-lock target
  contraction entry point intentionally raises `NotImplementedError`.

Run the complete preregistration-only replay with:

```sh
python3 run_prereg_checks.py
```

Expected scientific audit lines include:

```text
COLLISION_FREE_LABELED=24
COPY_CLASSES=4
ORBIT_SIZES=6,6,6,6
PARTY_IMAGE_ORDER=6
PARTY_KERNEL_ORDER=4
PARTY_ACTION=D0_FIXED_D1_D2_D3_FULL_S3
ORDER_F241_OF_3=120
CONJUGATE_XI_MAPS_TO_161
GOLDEN_A_DENOMINATOR_MOD241=207
TARGET_INVARIANT=NOT_COMPUTED
```

No file in this package contains a target invariant value.  Do not add the
pinned source files or post-lock result artifacts to this directory before
publishing its commit/hash.
