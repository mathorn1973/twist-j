# Photon and electron witness

This witness checks the exact layer beneath the photon window, the
center split, the electron ratio, and the electron sign:

- the window coordinates: `w(0) = 4`, `2 w(1) = 3 + sqrt5`,
  `2 w(2) = 3 - sqrt5`, the tilt `w(1) - w(2) = sqrt5`, and the
  Kramers-Wannier dual pair `what = 5 (2, 1, 0, 0, 1)`, `chat = w`,
  with `w` not self dual;
- the universal one-bit quantum `what(1)/what(0) = 1/2` and the exact
  closure of every class `|k| >= 2` on the centers `p = 3, 5, 7`;
- quadratic reciprocity of the tilt channel (swap for `p = 3 mod 4`,
  preserve for `p = 1 mod 4`) with the Gauss sums `g^2 = -3, +5, -7`;
- monopole charge quantization in fifths on the 4D lattice, and the
  elementary monopole cost bracket `[17, 21]`;
- the incidence bounds: straight runs cost 5 bits per segment, the
  `1 x K` ladder bound is exactly `9K + 8`, and a nine shape library
  realizes the exact table with minimum rate `31/8` and the integer
  margin `2^31 > 7^8`;
- the sixteen identity block behind `g = 2` and the double cover
  closure pair `(5, 10)` with `R^5 = -I`;
- the seven public electron sign laws on the kernel: the count parity
  as initial datum, the forced tick 0 event slot and phase lock, the
  annihilation census `{+1: 3125, -1: 3125, +-2: 0}` decided by tick
  3, the eps ledger `(+6250, -6250, 9375 event free)` with one Z_2
  governing the five readouts, the 20 state pair cycles, the equal
  `+2/+3` supports, and the transient shift and Galois images.

All checks use the Python standard library and exact arithmetic:
integers, `Fraction`, `Z[zeta_p]`, `Z[zeta_10]`, and `Q(sqrt5)`
pairs.  Angles are integer multiples of `pi/10`; no float appears in
any assertion.

The scope boundaries are essential.  The center split SELECTION
sentence (`p = 5` is the first prime passing both doors) rests on one
declared external import, the four dimensional `Z_N` self duality
threshold `N <= 4`; the witness verifies the arithmetic on both
doors, and the selection is carried by the registered dictionary
reading `CENTER-SPLIT-SELECTION [D]`, not promoted here.  The window
proof itself (the kappa lemma and the electric face roughening) is
the open frontier row `PHOTON-WINDOW-PROOF [O]`; this witness corners
the adversary in integers and closes nothing.  The internal gyron
window count law is not claimed here: the parity gate derives the
count structurally (999 plus the initial datum) and asserts only the
parity identity.  The eps totality on event free survivors is not
claimed publicly.

Evidence for `PHOTON-WINDOW-COORDINATES [T]`, `PHOTON-UNIVERSAL-BIT
[T]`, `CENTER-SPLIT-RECIPROCITY [T]`, `CENTER-SPLIT-CLOSURE [T]`,
`MONOPOLE-FIFTHS [T]`, `MONOPOLE-COST [C]`, `KAPPA-BOUNDS [T]`,
`KAPPA-SHAPES [C]`, `ELECTRON-G-RATIO [T]`, `ELECTRON-G-DOUBLE-COVER
[T]`, and `ELECTRON-SIGN-LAWS [T]`, and exact support for the D
dictionary rows `CENTER-SPLIT-SELECTION`, `ELECTRON-G-TREE`, and
`ELECTRON-SIGN`.

Run from the repository root:

```text
python3 reproduce/photon-electron/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 20/20 ALL
PASS`, exit 0, and empty stderr.
