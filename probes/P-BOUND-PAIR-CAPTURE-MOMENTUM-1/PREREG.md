# P-BOUND-PAIR-CAPTURE-MOMENTUM-1

**NON-CANONICAL / L1 / prospective exact-arithmetic audit.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: [#1812](https://github.com/mathorn1973/twist-j/issues/1812).

## 1. Question and equation

Certify finite rational enclosures for the normalized asymptotic joint
capture-and-record probability of the single fixed homogeneous model under
the source family defined in
`notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/PROOF_CAPTURE_PROFILE.md`.
The analytical theorem, not the finite computation, supplies the complete
source semantics, evenness, strict decline and all-input ratio enclosure.
This is result-exposed mathematical development, not a blind empirical fit.

For the unchanged object walk use `mu=2`, `g=2*pi/5`; retain the token/pulse
carrier, capture rotation `(3/5,4/5)`, `beta=4*pi/5`, receiver `z=100`, all
26 labels, and the full inherited `F1,F2` resolvents. The incident pair
center-momentum window is `[p-delta,p+delta]`, `delta=1/1000`. Its total
energy density remains flat on `[8*pi/5-h,8*pi/5+h]`, `h=1/1000`.
The incoming state is the contact-selected relative-ac source, normalized
with its own displayed density. It has no incoming relative-bound component.
The initial token is still localized at `y=0`, label 1. The success event
is exactly the original `Q_win`, including its bound-branch factor, outgoing
right pulse and receiver write. A memory click alone is not success.

Write `omega*=4*pi/5`, `e=delta^2=1/10^6`, and

```text
t_p = cos(p)-5*cos(omega)
f(p,omega) = sqrt(t_p^2-16)/(t_p+4*cos(omega-g))
r(p,omega) = f(p,omega)/f(0,omega)

[(1-e)/(1+e)] r(p,omega*-h)
 <= P_win(p)/P_win(0)
 <= [(1+e)/(1-e)] r(p,omega*+h).
```

The reference `P_win(0)>2/10^28` is inherited, not evaluated anew. The
absolute scattering denominator is retained in the theorem's positive
weight; this audit does not evaluate it or claim an absolute rate.

## 2. Frozen code and carrier

The complete executable is the adjacent `verify.py`. It is self-contained
Python 3 using only `fractions.Fraction` and `math.factorial/isqrt`, with
no floating-point operations, randomization, file input or network access.
All results and thresholds are computed from exact integers and ratios.

The analytical source base is public main/tag `canon-v106` at
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`; content
`9242db4f040d67d9417eacd06612230b74248cff`. The Canon digest is
`52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7`,
1370107 bytes. The source files and their byte hashes are listed in the
analytical note's `SOURCES.md`.

The continuous theorem domain is `|p|<=999/1000`, hence all incident
momenta obey `|P|<=1`. The entire finite audit grid is fixed now:

```text
p = j/10 for j=0,1,...,9; and p=999/1000.
```

Negative centers are used only for the stated evenness consistency check.
No grid point, source width, energy window, branch, event, contact or
parameter may be changed after the public pin to repair a failed result.

## 3. Systematics and rigorous error account

Every arithmetic operation gives an outward-rounded closed interval on
the `10^-36` rational grid. Square roots are enclosed by integer square
root and checked by squaring their endpoints. Pi uses Machin's identity
`16*atan(1/5)-4*atan(1/239)`, with exactly 40 alternating-series terms and
the first omitted term bounding each remainder.

Sine and cosine use exactly 32 terms. On the frozen argument domain
`|x|<=4`, the Lagrange remainders are bounded by `|x|^65/65!` and
`|x|^64/64!`, respectively. Intermediate roundoff is outward, never a
nearest-number substitution. The final printed bounds round outwards to
the `10^-6` grid.

The nonzero width of the momentum source is already included analytically
through `e=10^-6`; the energy width is included through the two energy
endpoint formulas. No midpoint equality is substituted for the packet.

Thirty-three finite consistency checks compare the simplified density
against the separately implemented inherited Schur/Mobius formula, at
all eleven centers and the lower, central and upper energies. Intersecting
intervals with width below `10^-24` are required. These are consistency
checks, not a substitute for the symbolic identity proof.

## 4. Fixed failure criteria

Fail with a nonzero exit and preserve the first result if any condition
below fails. Do not change thresholds after the pin.

1. Any interval operation is undefined, any square-root enclosure is wrong,
   or a Taylor argument leaves `[-4,4]`.
2. Pi does not lie strictly between `3` and `22/7`, with interval width
   below `10^-30`; the golden coefficient or central-energy cosine fails
   its independent interval identity check.
3. The certified quadrant and scalar-box inequalities needed by the
   analytical envelope proof fail.
4. An inherited/simplified density comparison is disjoint or either
   interval has width at least `10^-24`.
5. At any positive center, the printed ratio interval is not a subset of
   `(0,1)`, has width greater than `1/200`, or overlaps the previous
   center's printed interval. The value at `p=0` is exactly `1` by identity.
6. A signed-center evenness consistency check fails.
7. The fixed whole-program limit of 60 seconds is exceeded, stdout is
   nondeterministic, or stderr is nonempty on a successful run.

The program prints all eleven intervals and its exact check count.
It does not require any selected target probability, measured value,
electron property or photon property to match.

## 5. Action layer and conclusion limits

Action layer: **L1 only**. The proof concerns a supplied unitary model and
its declared normalized source and readout. A finite certificate is at
most a bounded computational result pending the repository's applicable
acceptance gates. No L1-to-physical-occurrence lift is asserted.

No physical photon/electron identity, charge, spin, statistics,
polarization, SI calibration, finite-time detector or native preparation
is claimed. The extra token/pulse channel is present throughout.

## 6. Prospective custody and execution

No scientific executable was run in this task before this preregistration.
Only analytical derivation, read-only source checks, static code review
and compilation are allowed before the pin. The complete verifier and
preregistration must be committed and pushed, and their exact public
readback confirmed, before the first execution. Record that immutable
commit, both file SHA-256 values, the exact command, neutral environment,
first-run stdout, stderr byte count and exit code in `RUN.md`.

The first execution is:

```text
python3 probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/verify.py
```

from the repository root under a 60-second outer timeout. Preserve its
stdout as `EXPECTED.txt` only with its actual disposition. Later required
architecture runs replay the same pinned code and exact output. Any
incomplete first pin follows the repository's abandoned-pin rules; no
silent retry or threshold adjustment is authorized.
