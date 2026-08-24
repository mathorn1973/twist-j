# RUN RECORD: B2 arm (a) executed, the certified entry layer of the Weil Gram engine

```
Status     NON-CANONICAL run record. Procedural class per the owner
           ruling of 2026-08-12: certified reconnaissance of
           computational class C, NOT candidate-C. No prereg was frozen
           when these runs executed; only a run performed after an
           explicit owner ANO over the frozen prereg may carry the
           candidate-C label. Gates nothing, promotes nothing.
Mirror     the byte authority of this record is
           weil-tower-2026-08-12/RUN-CERT-WEIL-GRAM-B2A.md on the
           handoff branch (committed 88718e8); this project copy is the
           reading surface.
Date       2026-08-12
Artifact   twistj-handoff, branch handoff/weil-tower-recon-20260812:
           70ad550 module + DH/zeta battery logs; 40bcd3e tower battery
           logs; 88718e8 draft prereg aligned with the executed state
           (B2 closed as arm (a), certified ENGINE section with version
           pins, branch-resolved guard doctrine, E3 rephrased, run
           record and C5 cross-check pinned on the branch, manifest
           regenerated, 31 pinned files). Draft after alignment:
           sha256 6ec12fdb...ec2da2, 13959 bytes.
Module     weil_gram_certified.py, sha256
           857582788e6e9ac4134725490c8d0e21b34dbedd0065d0698b5c7b6f322a1a39
           byte-identical on the development sandbox, nuc, gx10 (Linux aarch64 leg)
           and in the handoff repo.
Deps       python-flint 0.9.0 (FLINT/Arb), Python 3.12.3, both platforms.
Logs       cert_battery_nuc_x86_64.log    sha256 5a563761...0987765
           cert_battery_jas2_aarch64.log  sha256 a8954e57...aa9c96
           tower_battery_nuc_x86_64.log   sha256 ce6eeea2...a049ec
           tower_battery_jas2_aarch64.log sha256 f7b02a3c...1a3330
           crosscheck_theta_nuc_x86_64.log  8617542a...e84b98
           crosscheck_theta_jas2_aarch64.log 2af145b0...9e5323
```

## 1. What was built

The certified entry layer required by B2 arm (a) of
DRAFT-PREREG-C-WEIL-GRAM-TOWER-1, as a standalone module alongside the
float engine, same carrier, same normalization, same coefficient tables.
The certification chain starts at the matrix entries:

```
prime side    exact finite sums evaluated in Arb ball arithmetic
              (Lambda(n); chi5; xi_k ideal census with eta_p from the
              exact Z[phi] generator; DH -f'/f divisor recursion with
              algebraic tau in balls)
polar side    closed forms in balls
archimedean   rigorous integration (acb_calc_integrate) on the analytic
              pieces of the K(x) B(x) integrand, a second-order certified
              enclosure on [0, delta] at the removable singularity
              (B(0) = 0 used as an asserted exact identity; delta = 2^-20;
              enclosure width O(delta^2)), exact closed-form tail
inertia       certified triples (certainly negative, undecided, certainly
              positive) valid for every Hermitian matrix within the entry
              balls: full-spectrum Arb eigenvalue enclosures when
              isolable; otherwise sound LOWER bounds by certified
              ball-LDL definiteness of compressions onto exact dyadic
              subspaces (min-max), remainder reported undecided
DARK witness  an exact dyadic-rational vector w (scale 2^-16) with Q(w)
              re-verified in balls and certified negative
dependency    certified means modulo Arb / python-flint correctness and
              the module itself; no float enters any assertion
```

Structural detail that mattered: ball comparisons at lattice tie points
are undecidable at any finite precision, so cells carry integer indices
(m, kappa) and every branch decision at x = 0, at kink points and in the
modulation difference d = w_j - w_i is made in the integers.

## 2. Selftest (both platforms ALL OK)

```
C1  exprel series with certified remainder; k(x) = 1/exprel(2x) in (0,1]
C2  rho closed forms
C3  the pinned V1 case in certified balls: c_2..c_7 of DH minus
    consistent with closed forms; G[0,0] in [3.0150510837 +/- 6.2e-11],
    G[0,1] in [8.03856170934 +/- 1.3e-12], both inside the pinned
    tolerances of the float engine's V1; Q_-(1,-1) in
    [-10.0470212512 +/- 4.5e-11], CERTIFIED negative
C4  Galois additivity G[xi_0] = G[zeta] + G[chi5] certified entrywise
    (difference balls contain 0; worst upper 4.9e-11) at N=2, K=1
C5  certified eta/theta census against the float engine's theta_split
    on all 29 split primes below 322, zero mismatches; pinned as
    crosscheck_theta.py with per-platform logs on the branch
```

## 3. The DH and zeta battery, certified, identical on x86_64 and aarch64

Two platforms: nuc (x86_64, 8 cores) and gx10 = Linux aarch64 leg (aarch64, 20
cores). Every certified inertia triple and every witness ball printed
IDENTICALLY on both platforms; the diff of the readout lines is empty.
(Full logs differ only in hostnames and timings; a public probe would
route timings to stderr to get byte-identical stdout.)

```
block     N  K   dim  max entry rad  CERTIFIED (neg, und, pos)
zeta      6  3    48  4.6e-11        (0, 0, 48)   certified PD
chi5      6  3    48  4.6e-11        (0, 0, 48)   certified PD
dh_minus  6  3    48  4.5e-11        (16, 0, 32)  witness Q(w) in
                                     [-7948.377445 +/- 4.62e-7] < 0
dh_plus   6  3    48  4.5e-11        (0, 0, 48)   certified PD:
                                     below-height control, per the
                                     branch-resolved guard
dh_minus  6  8   108  3.0e-10        (28, 13, 67) witness
                                     [-8875.494193 +/- 4.75e-7] < 0
zeta      6  8   108  3.0e-10        (0, 33, 75)  zero certainly-negative
dh_plus   6 14   180  9.2e-10        (2, 50, 128) witness
                                     [-2.85387454 +/- 4.43e-9] < 0
```

## 4. The certified tower (owner directive "Jdi na věž")

xi_0 through xi_6 at N=6 for both K=3 (draft grid) and K=6 (the night
engine's grid), plus zeta and chi5 at K=6 for the direct float
comparison. Identical readout lines on both platforms (commit 40bcd3e).

```
block   K=3 (dim 48)      K=6 (dim 84)     night float at K=6 (eps 1e-8)
xi_0    (0, 0, 48) PD     (0, 0, 84) PD    (0, 4, 80)
xi_1    (0, 0, 48) PD     (0, 0, 84) PD    (0, 3, 81)
xi_2    (0, 0, 48) PD     (0, 0, 84) PD    (0, 3, 81)
xi_3    (0, 0, 48) PD     (0, 0, 84) PD    (0, 2, 82)
xi_4-6  (0, 0, 48) PD     (0, 0, 84) PD    (0, 0, 84)
zeta    (0, 0, 48) PD     (0, 19, 65)      (0, 22, 62)
chi5    (0, 0, 48) PD     (0,  5, 79)      (0,  9, 75)
```

Readings, labeled (all class C, certified, two-platform):

```
[C] The ENTIRE Hecke tower xi_0..xi_6 is certified positive definite at
    both grids, with ZERO undecided directions in every xi block.
    Together with section 3 this is the certified version of the
    night's headline: one carrier family in which every tower block is
    certainly nonnegative at these sections while both DH branches
    carry certified negative directions with exact dyadic witnesses,
    each branch on a section covering its zero height.
[C] The certified layer strictly sharpens the float readouts: the
    eps-floor "zero" directions of the night run are resolved as
    certainly positive wherever the true eigenvalue clears the entry
    radii (xi blocks entirely; zeta 22 -> 19 undecided; chi5 9 -> 5).
[C] The undecided mass sits exactly where the rank diagnosis puts the
    near-kernel: und(zeta) > und(chi5) > und(xi_k) = 0, machine-checked.
[note] PSD of tower sections remains a GRH-consistency readout, not
    evidence; the value added is certificate grade, the strict
    sharpening over float, and the two-platform identity.
```

## 5. State of the freeze decision

Owner ruling of 2026-08-12: ANO-7 not yet; the computational part is
complete and no further run is needed before the freeze. The draft was
aligned to the executed state in commit 88718e8: B2 closed as arm (a)
with the certified path and version pins in ENGINE; the guard doctrine
carries the owner's BRANCH-RESOLVED text (with the zero heights named
T0- and T0+, since tau- and tau+ already name the DH mixing constants);
E3 rephrased so that below-height positivity is not a firing; the run
record and the C5 cross-check are pinned on the branch; the manifest
was regenerated (31 files). The draft now awaits the owner's explicit
ANO-7; the public-probe question (stdlib-only verify versus internal
verifier with the pinned Arb dependency) stays deferred until after it.

## 6. Provenance

Basis: Public Canon v45 gate rerun this session (fresh clone, 5 of 5
SHA256SUMS OK). Draft prereg lineage: 5139f2e (G0 pass) -> 88718e8
(alignment). Float engine weil_gram_tower.py consumed read-only as the
reference for carrier, normalization, pinned V1 numbers and the night
tower inertia (run_tower.log); nothing in it was edited. Machines:
macOS arm64 leg (repo work), nuc x86_64 and gx10/Linux aarch64 leg aarch64 (runs), cloud
sandbox (development and third informal x86 replication). Log transfer
NUC/Linux aarch64 leg to macOS arm64 leg by direct LAN netcat with end-to-end SHA-256
verification.
