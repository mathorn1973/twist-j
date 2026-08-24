# P-ARITH-RAPIDITY-1 preregistration

Date: 2026-08-11

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the verifier are both
present at the immutable pin, that pin is pushed, and both files are read
back from the public remote.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v43
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v43
CONTENT_COMMIT: 320324f0def8ac9af89d0f128dbd7ab6548df55b
CANON_SHA256:   a52d0c266024dd492b56f6ad3a1121e3bccd0a0563b86176cab0118bc8e4991c
CANON_BYTES:    207795
BASE_COMMIT:    981aa1b9c8bc7ecd084346e099f014f3fc78847c
```

The governing authority is `mathorn1973/twist-j` on `main`; the canon
SHA256SUMS verified 5 of 5 OK on a fresh clone at preregistration time. This
probe is L1 only. It opens no inter-layer gate.

## Source, claim lock, and disclosure

```text
SOURCE:  incubation candidate C-ARITH-RAPIDITY-4, accepted in the
         incubation lane with verifier sha256
         5d176fd3818600ef993284af2edf4a734520c30535fc31adda3911cd3dcd196b
         and stdout sha256
         11ea81bce2ff6333f1e529c805cb4cb6318913eab90f48daa55207d371e37a1f,
         26 of 26 checks PASS, byte-identical on x86_64 and aarch64.
         Three predecessor ids died by integrity STOP under their own
         frozen rules: a gate name exceeding its test, assertions outside
         the frozen specification, and a self-audit off-by-one. None died
         for a mathematical reason and the frozen specification was never
         amended. A five-part breaker against the accepted candidate
         survived with broken=0, byte-identical on x86_64 and aarch64
         (breaker sha256
         441845e379b6c798405e381115e058ea9c35d8fc277ade2b82aac483be413724,
         stdout sha256
         7bc924abb5c3943bd4410347f72d0d09b3cc71b883e55fbc29b1fc5772046a77).
ISSUE:   public claim lock: issue 342, opened before this pin.
OWNER:   one session; no other session claims this probe. probes/, the
         public branch list, open issues, and the registry were checked
         for collisions at claim time; no ARITH or RAPIDITY probe,
         branch, or registry claim exists.
STATUS CEILING: this probe certifies computation-grade evidence (C) for
         the gated finite-scope clauses of Field 1. The universal
         statements are carried by the written proofs embedded in this
         file, which the verifier AUDITS at finite scope; the verifier
         carries no universal quantifier. NO registry, frontier, or
         canon file is edited by this probe's pull request.
```

Lineage: the public basis rows consumed are `BOOST-READING-SPLIT` [T],
`BOOST-COUNT-LADDER` [D], and `LADDER-ALTERNATOR-BASIS` [T]. This probe is
disjoint from every existing probe: `P-BOOST-COHERENCE-1` selects
alternator coins on the composed-velocity cover, and no existing probe
touches the number-field rapidity class structure of Q(sqrt5). The
verifier is the accepted incubation verifier with only its header comment
and first stdout line renamed; the gate set, the arithmetic, and every
check name are unchanged.

Notation. F = Q(sqrt5) with real embeddings sigma+ and sigma-, conj the
nontrivial automorphism, N(x) = x conj(x) the field norm WITH SIGN,
phi = (1 + sqrt5)/2, L_n and F_n the Lucas and Fibonacci numbers. A pair
(u, v) denotes u + v sqrt5 with u, v rational; O_F = Z[phi]. The
multiplicative rapidity avatar is rho(x) = x / conj(x); the additive
rapidity eta(x) = (1/2) log |sigma+(rho(x))| appears only in prose and
proofs, never in the verifier, which is logarithm-free throughout.

## The claims, with their proofs

### A. ARITHMETIC-RAPIDITY-DECOMPOSITION, audited by G1, G2, G7

For x in F*, rho(x) = x/conj(x) and eta, lam as

```text
rho(x) = sigma+(x)/sigma-(x)   as a real number under sigma+
eta(x) = (1/2) log |sigma+(rho(x))|
lam(x) = (1/2) log |N(x)|
```

PROOF. Conjugation is a field automorphism, so rho(xy) = rho(x) rho(y)
identically; taking (1/2) log |sigma+| of both sides gives eta(xy) =
eta(x) + eta(y). N is multiplicative, so lam is additive. From
|sigma+-(x)| = exp(lam +- eta) the two embedding absolute values are
reconstructed. In signed Galois coordinates x = a + b sqrt5 put t = a =
(sigma+ + sigma-)/2 and s = b sqrt5 = (sigma+ - sigma-)/2; then
t^2 - s^2 = a^2 - 5 b^2 = N(x) WITH SIGN, so N is the Minkowski invariant
of the pair, N > 0 timelike and N < 0 spacelike. QED

NULL SCOPE, stated exactly: a^2 - 5 b^2 = 0 with a, b rational forces
a = b = 0, because sqrt5 is irrational; the arithmetic F-locus contains
NO nonzero null vector. The real completion has the usual nonempty
Lorentz null cone t = +- s. The two statements are not in tension and
neither may be quoted without the other.

GROUP SCOPE, three separate statements, none of which implies another:
the norm-one positive part of the real completion is isomorphic to
SO+(1,1); the F-points form its rational subgroup, which is DENSE, not
discrete, by the rational parametrization
t -> ((1 + 5 t^2)/(1 - 5 t^2), 2 t/(1 - 5 t^2)) of the norm-one conic;
the discrete rapidity lattice is supplied only by the units,
O_F*/{+-1} = <phi> with eta(phi^n) = n log phi. The wording "F* is a
countable arithmetic subgroup" is wrong, since an arithmetic subgroup is
discrete and this one is not; it is not used here.

UNITS. rho(phi) = -phi^2, hence eta(phi) = log phi. phi^n =
(L_n + F_n sqrt5)/2 exactly for every n, so in signed Galois coordinates
Lucas is ALWAYS the time reading and sqrt5 Fibonacci ALWAYS the space
reading, with L_n^2 - 5 F_n^2 = 4 (-1)^n: the alternator N(phi) = -1
exchanges the timelike and spacelike unit sheets. The public
BOOST-READING-SPLIT [T] uses the positive-inverse coordinates
C_n = phi^n + phi^-n and S_n = phi^n - phi^-n, where the L and sqrt5 F
readings swap by parity on one timelike hyperbola. Both are exact; they
differ by POSITIVE-INVERSE CONVENTION VERSUS SIGNED GALOIS CONJUGATION,
the bridge being sigma-(phi^n) = (-1)^n phi^-n. No conflict is claimed
or implied.

### B. ONE ARCHIMEDEAN RAPIDITY AXIS, consumed as standard theory

K = Q(zeta5) has r1 = 0 and r2 = 2, so the Dirichlet unit rank is
r1 + r2 - 1 = 1: exactly one independent archimedean rapidity axis, read
as half the difference of log moduli at the two archimedean places,
equivalently in K+ = F. J = zeta5 phi^-1 has place moduli (1/phi, phi),
N(J) = 1, rapidity -log phi, phase 2 pi/5, and J^5 = phi^-5 closes the
phase while the rapidity persists. Unit rank counts rapidity axes and
NOTHING else; no space-dimension conclusion is drawn here or anywhere in
this probe.

### C. SPLIT-PRIME-RAPIDITY-CLASS, audited by G3, G4, G5, G6

TWO DISTINCT OBJECTS, and the distinction is the content of the claim.
For an ORIENTED prime ideal p of F above a split rational prime, with
p = (pi) by class number one,

```text
r(p) = [eta(pi)]  in  R/(log phi)Z
```

is well defined: another generator is pi' = +- phi^n pi and eta(pi') =
eta(pi) + n log phi. Conjugation gives r(pbar) = -r(p). For the RATIONAL
split prime p the canonical object is therefore only the unordered pair

```text
R(p) = { r(p), -r(p) }  in  ( R/(log phi)Z ) / {+-1}
```

and nothing finer without an extra choice. Anchors: for p inert
(p = +-2 mod 5), (p) is prime and rho(p) = 1, so r = 0 exactly; for the
ramified prime, p5 = (sqrt5) and rho(sqrt5) = -1, so r(p5) = 0 in
R/(log phi)Z, with sqrt5 the privileged generator whose eta is exactly 0
rather than 0 modulo the lattice.

EXACT AVATAR OF THE CLASS, so that no gate needs a logarithm:
[eta(x)] = [eta(y)] in R/(log phi)Z if and only if rho(x)/rho(y) =
+- phi^(2n) for some integer n. PROOF. The difference is n log phi iff
|sigma+(rho(x)/rho(y))| = phi^(2n); the element w = rho(x)/rho(y) has
N(w) = 1 by construction, and a norm-one element of F with |sigma+(w)| =
phi^(2n) equals +- phi^(2n) because sigma+ is injective on F. QED
Membership in +- phi^(2Z) is decided exactly: for w in O_F with
N(w) = 1 the trace satisfies |Tr(w)| = L_(2m), which is strictly
increasing in |m|, so m is identified by an integer search bounded by
the trace and w is then compared against +- phi^(+-2m) exactly.

### D. ARITHMETIC-FRAME-READING, decoder scope, NOT gated

Measurement as choice or quotient of the unit frame, reading the
invariant, the relative rapidity, and the sheet parity. Public decoder
totality, uniqueness and completeness remain open; nothing here moves
them, and no gate below touches this reading.

### E. PRIME-RAPIDITY-WEIL-BRIDGE, interface only, NOT gated

Frozen interface, asserted of nothing: for k in Z,

```text
chi_k(p) = exp( 2 pi i k r(p) / log phi ),  chi_k(pbar) = conj chi_k(p),
chi_k(p^m) + chi_k(pbar^m) = 2 cos(m theta_p),
theta_p = 2 pi k r(p) / log phi
```

is well defined precisely because the unit ambiguity contributes
exp(2 pi i k n) = 1. Weights, recorded so a later bridge cannot fudge
them: the explicit-formula weight of a prime ideal is log N(p), so a
degree-one split prime contributes log p with paired term
2 (log p) p^(-m/2) cos(m theta_p), while an INERT prime has N(p) = p^2
and therefore weight 2 log p on the sparser norm grid p^(2m). No claim
whatever is made that this interface reproduces the explicit formula or
touches RH; a later frontier row built on this interface closes
negatively if no admissible pairing reproduces the log N(p) weights and
the archimedean term exactly.

## Field 1. EQUATION (the gated clauses; each check name states exactly its test)

```
G1  identities on the exact grid a, b in [-8, 8] minus the origin: rho
    and N multiplicative on the declared pair list; t^2 - s^2 = N with
    sign on the whole grid; x conj(x) = (N, 0) on the whole grid; rest
    locus class zero exactly iff ab = 0; no nonzero F-rational null
    vector on the grid.
G2  units: N(phi^k) = (-1)^k for 1 <= k <= 12; rho(phi) = -phi^2;
    phi^n = (L_n + F_n sqrt5)/2 and L_n^2 - 5 F_n^2 = 4 (-1)^n for
    1 <= n <= 30; sheet sign matches parity.
G3  exact class machinery: the +- phi^(2Z) membership test agrees with
    direct comparison against phi^(2m) and its negative for |m| <= 12;
    it returns 0 on rho(sqrt5) and on rho(q) for the rationals
    q = 1, 2, 3, 7, 11, 13; the class shift of phi^n against 1 is
    exactly n for |n| <= 8.
G4  TWO GENUINE CONSTRUCTIONS, both returning a generator of norm +p in
    O_F, for every split p < 2000: (i) Pell sweep on a^2 - 5 b^2 =
    +-4 p with norm normalized to +p; (ii) Euclidean gcd of p and
    sqrt5 - r in Z[phi] at the canonical root 0 < r < p/2 with
    r^2 = 5 mod p, Q(sqrt5) being norm-Euclidean, with every division
    step asserted norm-decreasing rather than assumed. GATE: the
    canonical unordered classes agree, R1(p) = R2(p), decided by the
    exact avatar of claim C, that is rho1/rho2 or rho1 rho2 lies in
    +- phi^(2Z). The oriented split (how many pairs agree oriented, how
    many only after conjugation) is REPORTED AS DATA and gates nothing,
    since construction (i) fixes no orientation.
G5  well-definedness of r: for every split p < 500 and every generator
    variant pi, -pi, phi pi, phi^2 pi, -phi^3 pi, the class is
    unchanged; and the conjugate class is the negative, tested as
    rho(pi) rho(conj pi) = 1 exactly.
G6  anchors: class zero exactly for every inert p < 2000; the ramified
    generator sqrt5 at class zero with rho(sqrt5) = -1 exactly and
    sqrt5 sqrt5 = 5.
G7  frame change by phi^k for k = 1, 2, 3 on the grid: |N| scale
    preserved, the class shifts by exactly k, rapidity differences
    invariant.
G8  rationals are dense, units are not: at least 400 distinct norm-one
    F-points from the Pell parametrization with numerator and
    denominator under 40 land in pairwise distinct classes, exhibited
    exactly. No density theorem is gated; the exhibit is a finite
    witness against discreteness of the rational norm-one subgroup.
G9  interface consistency, no claim: rho(conj pi) = rho(pi)^-1 exactly
    for every split p < 2000, which is the algebraic content of
    chi_k(pbar) = conj chi_k(p); and the weights recorded as integers,
    N(p) = p for split and p^2 for inert on the same range.
G10 self-audit: the verifier prints its runtime inventory of executed
    check names, one line per assertion, and the inventory length
    equals the number of checks executed.
```

Q(sqrt5) being norm-Euclidean is consumed as standard theory, and the
verifier asserts the norm-decreasing property at every division step
rather than assuming it.

## Field 2. CODE

`verify.py` in this directory, pinned together with this file BEFORE the
first formal execution. Python standard library only; exact integer and
Fraction arithmetic only; no float anywhere; deterministic stdout; no wall
clock, no hostname, no machine identifier; under 120 seconds; run from the
repository root as

```text
env -i PATH="$PATH" HOME="$HOME" LC_ALL=C LANG=C \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ARITH-RAPIDITY-1/verify.py
```

Two legs: a local formal run on a neutral platform (Debian 13, aarch64)
recorded in `RUN.md` with `EXPECTED.txt` holding the exact stdout bytes,
and the repository x86_64 and aarch64 checks at pull-request time. Byte
identity across architectures is required.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. The carrier is exact
arithmetic in Q(sqrt5) represented as rational pairs. Nothing outside
this repository and the standard library is read.

## Field 4. SYSTEMATICS

```
S1  universal statements live in the written proofs of claims A and C
    and in the standard theory consumed by claim B; the verifier audits
    them at the stated finite scope and nowhere claims a universal
    quantifier.
S2  every gate name states exactly what its code tests, and G10 makes
    the executed inventory auditable from the stdout alone. This is the
    direct lesson of the dead predecessor ids.
S3  the two constructions of G4 are structurally independent, a
    Diophantine sweep versus a Euclidean gcd; neither reads the other's
    output. A third construction, a direct norm sweep in the (1, phi)
    basis, was run against the accepted candidate in the incubation
    breaker and agreed on the unordered class for all 146 split
    p < 2000; its systematic orientation flip against the Pell
    construction, 0 oriented to 146 conjugate, where Pell against
    Euclid gives 70 to 76, is the expected signature that orientation
    is construction convention and only R(p) is canonical.
S4  the class comparison is exact and logarithm-free; no floating point
    appears in the file at all.
S5  convention: signed Galois coordinates throughout; the bridge to the
    positive-inverse convention of BOOST-READING-SPLIT is stated in
    claim A and is not itself gated.
```

## Field 5. FAILURE THRESHOLD

Zero tolerance: any FAIL line in the verifier stdout fires the probe and
the result is recorded as fired, not hidden. A defect demonstrated to be
in the verifier implementation rather than in a gated claim is an
integrity STOP, archived with both file hashes; the probe is then dead
and any successor uses a new name. No threshold moves after the pin. The
pinned branch is never amended, rebased, squashed, or force-pushed.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Not claimed: any decoder movement; any physical
reading beyond the existing [D] rows; any space-dimension conclusion
from unit rank; any RH, zeta-zero, Weil-positivity, or explicit-formula
result; any Hecke bridge (claim E is a frozen interface asserted of
nothing); any canonical real value of the split-prime rapidity beyond
the unordered class; any registry, frontier, or canon movement. The
probe's outcome feeds a later, separate fold decision by the owner.
