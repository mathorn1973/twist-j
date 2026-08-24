# DRAFT PREREG: P-FCC-TRANSFER-SYMBOL-1 (UNFROZEN, NOT FOR PIN)

```text
STATUS   DRAFT, UNFROZEN, NON-CANONICAL. This is the review copy for
         the pre-pin blind review by the other model family, per the
         STOP discipline of P-A3-FCC-POINT-GROUP-1. It becomes a
         preregistration only when frozen by the owner process with
         its SHA-256 recorded, on this fresh identity, after review.
         Nothing here may be cited as a probe or as a result.
IDENTITY P-FCC-TRANSFER-SYMBOL-1, fresh, no reuse of any sealed name.
TARGET   public line, mathorn1973/twist-j, as a probe under POLICY.md
         and AGENTS.md, which govern over this draft if they differ.
LAYER    L6 (measure: a weight system on translation steps). The
         carrier facts consumed are registered L2 rows; no layer lift
         is claimed by this probe.
PROCESS  prepared in the incubation lane. The preparing seat cannot
         open issues or pull requests; the claim issue, the pin and
         the execution follow the owner process after review.
REVIEW   the blind reviewer's question, from the STOP record: can a
         reader derive every gate's pass or fail from this document
         alone? If not, the draft is not ready to freeze.
```

## Field 1, equation

One ambient: Z^3. No other coordinate system, lattice model, or
finite-field object appears anywhere in this identity.

Displayed objects:

```text
SHELLS   S_n = the full norm shell of Z^3 at norm n, for
         n in {2, 4, 8, 10, 16}. Box bound: coordinates in -4..4,
         provably sufficient (any |v_i| >= 5 forces norm >= 25 > 16).
         Representatives and sizes (each shell = all signed
         permutations of its representative):
           S_2  (1,1,0)  12      S_4  (2,0,0)   6
           S_8  (2,2,0)  12      S_10 (3,1,0)  24
           S_16 (4,0,0)   6      total 60 vectors
GROUP    the 48 signed permutation matrices of Z^3 (the carrier point
         group of the frozen point-group record).
WEIGHTS  W* = (w2, w4, w8, w10, w16) = (6, 1, 15, 1, 1), the frozen
         working point of OWNER RULING R3 (2026-08-05). Its criterion
         is displayed in field 3 and re-verified in-probe (G5).
FLUX     flat (F0, ruling R3): the symbol is scalar, no phases.
SYMBOL   S(k) = sum_n w_n sum_{v in S_n} (cos<k,v> - 1).
```

The claims, all EXACT finite identities (polynomial coefficient
identities over Z, no analysis, no truncation language needed):

```text
T2   sum_n w_n sum_v <k,v>^2  =  648 |k|^2
T4   sum_n w_n sum_v <k,v>^4  =  3168 |k|^4
T6   sum_n w_n sum_v <k,v>^6  =  21888 sum k_i^6
                                 + 63360 sum_{i != j} k_i^4 k_j^2
                                 + 0 (k_x k_y k_z)^2 terms,
     and this is NOT proportional to |k|^6: the exact anisotropy
     witness (isotropy would need 65664 and 131328 in the last two
     places).
TG   the weighted family {(v, w(v))} is invariant as a multiset under
     every one of the 48 matrices; hence S(Mk) = S(k) term by term
     (the octahedral referee gate at the level of the full symbol).
```

Derived display, not a separate claim: the Taylor form
S(k) = -324 |k|^2 + 132 |k|^4 + R6, coefficients 648/2 and 3168/24,
isotropic through fourth order, anisotropic at sixth.

Proposed status on success: T for T2, T4, T6, TG as finite exact
identities, in the sense the public taxonomy applied to the
point-group record. Every physical reading (dispersion, speed,
restoration of isotropy as physics) stays OUTSIDE this probe.

## Field 2, code

verify.py, Python standard library only, exact integer arithmetic
(Fraction only for the two displayed Taylor coefficients), no float
anywhere, no randomness, no clock, deterministic iteration order
(sorted shells, sorted dict displays), ASCII-only output, well under
120 seconds, run from repository root under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## Field 3, carrier and data

No external data. Everything consumed is displayed IN THIS DOCUMENT:
the shell definitions with box bound, representatives and sizes; the
group as the signed permutation matrices; the weight point W* with
its frozen criterion, quoted in full:

```text
admissible: integer w = (w2, w4, w8, w10, w16), every entry >= 1,
            with -4 w2 + 32 w4 - 64 w8 + 440 w10 + 512 w16 = 0
selected:   minimal total sum(w); ties broken lexicographically in
            the order (w2, w4, w8, w10, w16)
computed:   unique minimizer W* = (6, 1, 15, 1, 1), total 24,
            tie-break unused (re-verified in-probe, G5)
```

plus the monomial conventions (exponent triples (i, j, l) with
multinomial coefficients C(m; i, j, l)) and the cosine convention
(cos<k,v> - 1, the symbol vanishes at k = 0). Nothing else is
consumed. Verified properties are not inputs: even coordinate sum
(FCC membership) is gated (G2), not assumed.

## Field 4, systematics

Two-platform byte-identical stdout: the GitHub x86_64 required check
and a local leg with neutral public environment fields (for example
platform Ubuntu 24.04, architecture aarch64; never a machine
nickname). EXPECTED.txt, RUN.md, RESULT.md per POLICY. Deterministic
output ordering as in field 2.

## Field 5, failure threshold

Any gate FAIL on the pinned run is the probe result F for the
identity block as stated. A fired falsifier is merged, archived,
never amended; no threshold moves after the pin. If the two platform
legs differ byte for byte, the run is void and the probe reports the
discrepancy, not a result.

## Field 6, action layer

L6.

## Gates (GATE DESIGN RULE: every gate names its constructed failing input)

```text
G1  shell sizes = (12, 6, 12, 24, 6)
    failing input: add norm 6 to the family; its size 24 breaks the
    displayed size vector
G2  all 60 vectors have even coordinate sum
    failing input: (1, 0, 0)
G3  each shell is one 48-orbit with the displayed representative
    failing input: the norm-9 shell of Z^3, which splits into orbits
    of sizes 6 and 24 (constructed in-script)
G4  W* is admissible: entries >= 1 and cone value exactly 0
    failing input: uniform (1,1,1,1,1), cone value 916
G5  W* is the unique minimal admissible point (exhaustive over all
    positive 5-tuples with total <= 24, plus the independent
    elimination scan)
    failing input: (230, 1, 1, 1, 1), admissible with total 234
G6  T2 as a coefficient dict equality with 648 |k|^2
    failing input: w2 -> 7 gives 656 on the (2,0,0) monomial
G7  T4 as a coefficient dict equality with 3168 |k|^4
    failing input: uniform weights; the 916 deficit breaks
    proportionality to |k|^4
G8  TG multiset invariance under each of the 48 matrices
    failing input: the 59-vector family with one vector of S_2
    removed (constructed in-script)
G9  T6 exact display AND inequality with 21888 |k|^6
    failing input: any altered display value; the isotropy
    sub-assertion would pass only if the k^4k^2 coefficient were
    65664 and the triple-product coefficient 131328
```

## What this probe does NOT do

No time leg, no characteristic, no dispersion claim, no physics
reading, no canon edit beyond its own probe directory and the earned
registry row. The time leg is P-FCC-TIME-CHARACTERISTIC-1, queued
behind this probe's review. The phased sector (F1/F2) is out of
scope; the fourth-order deficit functional is not claimed to apply
there.

## Open review questions for the blind reviewer

```text
1  Layer declaration L6 with named L2 dependencies: correct, or does
   the symbol identity need a joint declaration?
2  Proposed label T for finite exact polynomial identities:
   consistent with the taxonomy as applied to the point-group record?
3  Is the box-bound display sufficient self-containment for G1, or
   should the frozen prereg display all 60 vectors literally?
4  Is the polynomial-identity form (no truncation language at all)
   the cleaner claim, or does the R6 remainder need an explicit
   O(k^8) statement anywhere?
5  Does G8's failing input (drop one vector) satisfy the GATE DESIGN
   RULE better than citing the deposited 20-class alphabet (recon F6,
   not displayed here to keep one ambient)?
```

## Falsifier

Any of G1 to G9 failing on the pinned two-platform run. Supersession
path: the W5 derivation replacing W* re-runs the identity block at
the derived point as a NEW probe with a fresh identity; this one
stays sealed either way.

## Draft pins (of the ruling support computation, not of this draft)

```text
verify_r3_w4_minimal_point.py
  sha256 116e04152ea95ba8ba861c9d01722f9aede7f950e1dac09b7fc5186513357400
stdout
  sha256 177ea11e06d82ee97fca49a7810506da7886ae5fced19411f89deb8540272840
  16 of 16 checks PASS, byte-identical x86_64 / aarch64
```
