# P-TM-HANKEL-K3-TRANSFER-1 preregistration

Date: 2026-08-11

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable pin, that pin is pushed, and both files are read
back from the public remote.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v41
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v41
CONTENT_COMMIT: 096e97b44727830102846746f0c723af1c59a2cf
CANON_SHA256:   a15474c4204db637d7ce276ef6ea5dbe94b50af593e46389fd5e77aa16ca80e8
CANON_BYTES:    198932
BASE_COMMIT:    278b5348c7ace52737700f05f7ab230ffd201fc6
```

The governing authority is `mathorn1973/twist-j` on `main`; the canon
SHA256SUMS verified 5 of 5 OK on a fresh clone at preregistration time. This
probe is L1 only. It opens no inter-layer gate.

## Source, claim lock, and disclosure

```text
SOURCE:  incubation candidate C-TM-HANKEL-XOR-DEFECT-1; companion
         non-canonical note notes/C-TM-HANKEL-XOR-DEFECT-1.md at commit
         51634cfcdeef85a5bdbaa2c1fa0c404e391afa17, branch
         notes/c-tm-hankel-k3-transfer, pull request pending review at
         preregistration time
ISSUE:   the executing environment holds no API credential to open the
         claim issue; the owner directed this probe directly and may attach
         an issue number at pull-request time. Recorded as a stated
         deviation, not hidden.
OWNER:   one session; no other session claims this probe. probes/ and the
         public branch list were checked for collisions at preregistration
         time; no P-TM-HANKEL probe exists.
STATUS CEILING: this probe certifies computation-grade evidence (C) for the
         gated claims below; written proofs remain in the companion note;
         NO registry, frontier, or canon file is edited by this probe's
         pull request.
```

Lineage: the public basis rows consumed are `MOBIUS-TM-PRIME2-BRIDGE` [T]
and `TM-MULTIPLICATION-CARRY-DEFECT` [T]. This probe is disjoint from the
carry-layer probes (`P-CARRY-*`), from `P-MOBIUS-TM-PRIME2-1`, and from the
`P-TM-SYM2-*` family: its object is the divisor-block Hankel compression
`K_P` and its XOR/defect splitting, which no existing probe touches.

Notation as in the companion note: `t(n) = (-1)^(s_2(n))`, `t(1) = -1`,
`c = mu * t`; the symbol tau is not used. For an odd squarefree prime set
`P` with `k = |P|`: `K_P(S,T) = c(n_S n_T)`, `Kxor_P(S,T) = c(n_(S XOR T))`,
`R_P = K_P - Kxor_P`; `P` is extremal when `t(n_Z) = (-1)^(|Z|+1)` for all
`Z`. `W(S,T) = 2^(|T|-|S|)` for `S` a subset of `T`, else 0. Inertia is
printed with named fields `NEG ZERO POS`.

## Field 1. EQUATION (the gated claims; each maps to a note section)

```
G1  (note sections 1 and 2) On pools of prime sets, extremal and not
    (all 120 pairs from the odd primes 3..59, all 120 triples from
    3..31, six named sets up to k = 5): R has zero empty row and column;
    the nonempty block of R is I modulo 2 with odd determinant; the
    intersection-layer operators are I modulo 2 with odd determinants;
    the layer inversion K(S,T) = sum over V subset (S AND T) of
    d_V(S XOR T) holds entrywise.
G2  (note section 3) The local identity u^T m u = diag(1,-3) and, on
    every extremal pair with p < q <= 1000, the four known extremal
    triples, and the two known chains at k = 4, 5: the exact congruence
    W^T Kxor W = diag((-1)^(|S|+1) 3^(|S|)) and the parity of W^T R W.
G3  (note section 4) On every extremal pair with p < q <= 1000: the
    W-basis pencil equals the displayed 4 by 4 matrix with the five unit
    letters, and |3D + 3E + F| <= 7. On the first 128 extremal pairs in
    lexicographic order: the pencil determinant has zero roots in the
    open interval (0,1) by exact isolation, and the inertia is
    NEG 2 ZERO 0 POS 2 at s = 0, 1/2, 1. The isolation scope is bounded
    by the 120 second budget; the all-pairs statement is carried at
    theorem grade by the written proof of note section 4, whose Schur
    bound is itself gated abstractly in G5.
G4  (note section 5) The three witnesses {5,101,293}, {83,89,263},
    {149,269,293} are extremal; their K inertia is NEG 5 ZERO 0 POS 3 by
    two independent exact paths; determinants -3840, -768, -9856; the
    pencil constant term is 3^12; exactly one pencil root in (0,1) each;
    among all extremal triples with n <= 200000 (count 157) exactly one
    is nonbalanced; among the 99 triples with p < q < r <= 300 exactly
    three fail.
G5  (note section 6) Abstract ternary tables, extremal binary face, 19
    free signs: the 32 and 16 local bound cases of the rigidity lemmas;
    all 2 by 2 pair-Schur principal minors nonnegative on the whole
    2^15 substrate; the unique all-minors-zero configuration with
    inertia NEG 2 ZERO 0 POS 1; the determinant trichotomy of G_6 with
    census 32398 / 110 / 260; the exact 16x lift to the 2^19 strata
    518368 / 1760 / 4160; classes 522462 / 51 / 1775 by sign of det K;
    every table in the det K > 0 class has K inertia NEG 4 ZERO 0 POS 4,
    every table in the det K = 0 class NEG 4 ZERO 1 POS 3, and every
    table in the det K < 0 class NEG 5 ZERO 0 POS 3; the two-scalar law
    FAIL iff det G_6 < 0 and det K <= 0; the nonsingular and singular
    non-rigid strata all balanced.
G6  (note section 7) The six linear orbit sums give 3584 buckets with
    exactly 58 mixed; the canonical 28 quadratic invariants give 88352
    buckets with zero mixed; Burnside orbit count 89472 by formula and
    by direct enumeration; the quotient gap 89472 - 88352 = 1120.
G7  (consistency) All eight named real triples certify extremal. The
    three witnesses satisfy det G_6 < 0 through the abstract linear
    form, with det K equal to the G4 values -3840, -768, -9856 (a
    second path against the direct integer build of G4); the five known
    non-rigid real triples, including {3,23,71} with n = 4899, satisfy
    det G_6 >= 0 and det K > 0.
```

## Field 2. CODE

`verify.py` in this directory, pinned together with this file BEFORE the
first formal execution. Python standard library only; exact integer and
Fraction arithmetic only; no float anywhere; deterministic stdout; no wall
clock, no hostname, no machine identifier; under 120 seconds; run from the
repository root as

```text
env -i PATH="$PATH" HOME="$HOME" LC_ALL=C LANG=C \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-TM-HANKEL-K3-TRANSFER-1/verify.py
```

Two legs: a local formal run on a neutral platform (Debian 13, aarch64)
recorded in `RUN.md` with `EXPECTED.txt` holding the exact stdout bytes,
and the repository x86_64 and aarch64 checks at pull-request time. Byte
identity across architectures is required.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. The carrier is the divisor
lattice of odd squarefree integers, the binary digit word, and the finite
abstract ternary tables. Nothing outside this repository and the standard
library is read.

## Field 4. SYSTEMATICS

```
S1  polarization: t(1) = -1 fixed; the opposite convention negates every
    sign table and swaps inertia components; all claims are stated under
    the fixed convention.
S2  normalization: Walsh values are unnormalized sums; the W congruence
    is over the integers, not the reals.
S3  independence: the 15-bit trichotomy census has two independent
    implementations agreeing before this probe; the 2^19 sweep uses a
    fraction-free leading-minor fast path with a characteristic
    polynomial fallback on any zero pivot; witnesses are verified by two
    distinct exact inertia paths and the witness determinants by two
    distinct constructions (direct integer build and abstract linear
    form).
S4  scope: every universally quantified claim gated here is quantified
    over a finite, fully enumerated domain stated in Field 1; nothing is
    sampled. The G3 root-isolation subscope is deterministic
    (lexicographic prefix), fixed here before the pin.
```

## Field 5. FAILURE THRESHOLD

Zero tolerance: any FAIL line in the verifier stdout fires the probe and
the result is recorded as fired, not hidden. A defect demonstrated to be in
the verifier implementation rather than in a gated claim is an integrity
STOP, archived with both file hashes; the probe is then dead and any
successor uses a new name. No threshold moves after the pin. The pinned
branch is never amended, rebased, squashed, or force-pushed.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Not claimed: anything about zeta zeros, the Riemann
hypothesis, Weil positivity, explicit formulae; anything about the infinite
operator beyond the finite compressions; any J-coupling, physical reading,
or L2-L6 lift; any registry, frontier, or canon movement. The probe's
outcome feeds a later, separate fold decision by the owner.
