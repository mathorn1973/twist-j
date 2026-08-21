# PREREG C-RG-FIXEDPOINT-1, 2026-07-31

Status: FROZEN before first execution. Candidate lane of the TWIST-J project.
No authority. This preregistration follows the six-field discipline of the
public POLICY.md. The SHA-256 of this file and of the verifier are recorded
in the run record before the first formal execution.

## Identity

```text
candidate:     C-RG-FIXEDPOINT-1
target line:   public, on promotion only (ENTROPY program, canon section 3)
owner:         one named session, Cowork session of 2026-07-31
action layer:  L5 finite kernel structure; no L6 measure lift; no lift named
currency:      Public Canon v28, tag canon-v28, content commit 86a04600,
               CANON sha256 4b720846..., SHA256SUMS 5 of 5 OK, clone head
               3161cbc7, verified in this session on 2026-07-31
```

## Prior art, cited and re-audited, not assumed

```text
CENSUS-313 [C]            core 6250, components 313 = 312 x 20 + 1 x 10
ENTROPY-BLOCK-HALVING [C] block maps two-to-one on the core, k = 0..10
ENTROPY-LIVING-SET [C]    halves 3125 + 3125, four restrictions bijective
ENTROPY-UNIQUE-PAST [C]   fibers exactly two, depths 1..12
ENTROPY-MIRROR-LAW [C]    own-half involutions, cycle type {1:1, 2:1562},
                          unique fixed state per letter in the singlet;
                          cross restrictions mutually inverse:
                          F_1 o F_0 = id on H_1, F_0 o F_1 = id on H_0
KERNEL-Z6-SYNCHRONIZATION [T], CORE.md engine block: the update
                          U(n,psi) = (n+1, g_(z_6(psi) + 2 theta_n mod 5)(psi))
probes/P-ENTROPY-BRIDGE-2/verify.py   the pinned kernel constants, census
                          protocol, and substitution word, copied verbatim
probes/P-ENTROPY-MIRROR-1/PREREG.md   the block-map recursion and the
                          right-to-left composition convention
```

## Pre-freeze hand derivations, disclosed

Derived on paper from the public row statements before any candidate
computation; frozen here as audit gates, not as discoveries.

```text
D1  image containment: Fix(Phi^(k)_eps) subset H_(eps xor (k mod 2)),
    because the image of the level-k block lies in the half of its last
    letter, and the last letter of subst^k(eps) is eps xor (k mod 2)
    (tm(2^k - 1) = k mod 2).
D2  k = 1 tower floor: by ENTROPY-MIRROR-LAW clause M03,
    Phi^(1)_0 = F_1 o F_0 = id on H_1 and Phi^(1)_1 = F_0 o F_1 = id on H_0,
    so Fix(Phi^(1)_eps) = H_(1-eps), cardinality 3125, exactly.
D3  k = 0 multipliers: the unique fixed state of F_1 is expected to be
    3 C_D = (1,3,4,2,3,3) (the unique fixed point of generator d, with
    z_6 = 1 selecting d at letter 1), and the unique fixed state of F_0 is
    expected to be 3(C_D + V_E) = (1,3,4,2,1,3) (the unique fixed point of
    generator e, with z_6 = 4 selecting e at letter 0). Both generators are
    affine reflections with linear part -I, so both k = 0 multipliers are
    expected to be exactly -I. This is a hand derivation; its gate H0 may
    fire without invalidating anything public.
The open content of this candidate therefore begins at k = 2.
```

## Definitions, frozen

```text
State space   F_5^6, states (p1, p4, p1', p4', q, r), encoding base 5 as in
              the public probe verifier.
Generators    a, b, c, d, e with the public constants
              S_VEC = (2,1,2,1), U_VEC = (0,1,0,-1), C_D = (2,1,3,4,1,1),
              V_E = (0,0,0,0,1,0), all involutive affine maps mod 5.
Selector      z_6(psi) = sum of coordinates mod 5; letter t in {0,1} applies
              generator index (z_6 + 2t) mod 5 in the order (a,b,c,d,e).
Branch maps   F_t(psi) = g_((z_6(psi) + 2t) mod 5)(psi).
Census        Thue-Morse driver theta_n = s_2(n) mod 2 from n = 0; warmup
              400 ticks, window 300 ticks; distinct window sets are the
              components; their union is the recurrent core R.
Halves        H_eps = Im(F_eps | R).
Block maps    Phi^(0)_eps = F_eps; Phi^(k+1)_eps = Phi^(k)_(1-eps) o
              Phi^(k)_eps, composition right to left (Phi^(k)_eps first).
              Equivalently the composition along the substitution word
              subst^k(eps), first letter applied first.
Multiplier    every generator is affine with linear part L_g independent of
              the state; along the 2^k substeps of Phi^(k)_eps from x, the
              multiplier is the ordered matrix product
              M_k^eps(x) = L_(g_m) ... L_(g_2) L_(g_1)  (g_1 first substep),
              equivalently the chain rule
              M_(k+1)^eps(x) = M_k^(1-eps)(Phi^(k)_eps(x)) . M_k^eps(x).
Spectrum      the characteristic polynomial det(xI - M) over F_5, monic,
              degree 6, reported as the coefficient tuple c0..c6.
Range         k = 0..12, both letters, fixed points counted on R.
              Full-space fixed points outside R are a diagnostic count only.
```

## Six frozen fields

### 1. Equation

Audit gates (fail = STOP, they re-derive public [C] rows or pinned
conventions; a STOP is a currency problem, not a result):

```text
G01 census: |R| = 6250, 313 components, sizes {20: 312, 10: 1}, disjoint
G02 halves: H_0, H_1 disjoint, 3125 each, union R; F_t(R) subset R
G03 every generator is affine: g(x) = L_g x + g(0) exactly on a
    deterministic state sample
G04 every L_g is an involution with determinant 1
G05 the doubling recursion equals the literal word composition on the full
    space for k = 0..6, both letters
G06 the multiplier recursion equals the literal ordered product along the
    substep walk for k = 0..8, first min(10, |Fix|) fixed states per (k,eps)
G07 characteristic polynomial self-tests: companion matrix of a fixed monic
    sextic reproduces its coefficients; charpoly(I) = (x-1)^6 expanded
    independently
G08 halving re-audit: |Phi^(k)_eps(R)| = 3125 for k = 0..10, both letters
G09 k = 0: exactly one fixed state per letter, both in the singlet, the two
    states distinct, and no common fixed state on the full space
G10 k = 1: Fix(Phi^(1)_eps) equals H_(1-eps) exactly (set equality, 3125)
G11 half law D1: Fix(Phi^(k)_eps) subset H_(eps xor (k mod 2)), k = 0..12
```

Hypotheses (fired = first-class result, recorded, threshold never moved):

```text
H0  k = 0 multipliers: both equal -I exactly (hand derivation D3)
H1  existence: Fix(Phi^(k)_eps) is nonempty on R for every k = 0..12 and
    both letters
H2  mirror spectrum: at every fixed point of every Phi^(k)_eps in range,
    the multiplier M satisfies (M^2 - I)^6 = 0, equivalently every
    eigenvalue over the algebraic closure of F_5 lies in {1, -1};
    the test is independent of the charpoly implementation
H3  halving extension: |Phi^(k)_eps(R)| = 3125 also at k = 11, 12
```

Measurements (recorded exactly whatever they are, candidate-C on PASS of the
audit gates):

```text
M1  the tower |Fix(Phi^(k)_eps)| for k = 0..12, both letters, plus the
    off-core full-space fixed count as a diagnostic
M2  the multiset of characteristic polynomials of the fixed-point
    multipliers per (k, eps), with counts, plus the number of distinct
    multiplier matrices
M3  the component split of the fixed points (singlet count, size-20 count,
    number of distinct components touched)
M4  the count of fixed points whose multiplier is an involution (M^2 = I)
O1  recorded, ungated: the minimal eventual period p in {1, 2, 4} of the
    count tower within range, with its onset k0, or NONE
```

### 2. Code

```text
verify_rg_fixedpoint_1.py, Python 3 standard library only, exact integer
arithmetic, no float anywhere, single process, no filesystem writes,
deterministic output, target runtime under 120 s. Kernel constants copied
verbatim from probes/P-ENTROPY-BRIDGE-2/verify.py of the clone at head
3161cbc7. Compilation and static checks are allowed before the freeze;
formal execution is not.
```

### 3. Carrier and data

```text
The finite kernel F_5^6 with the public constants; the Thue-Morse prefix;
the warmup-400/window-300 census; scales k = 0..12. No external data, no
files read, everything rebuilt inside the verifier.
```

### 4. Systematics

```text
1  single architecture and single session: every grade below candidate-T
   carries that caveat; nothing here is a two-platform pin.
2  composition convention frozen: word order, first letter applied first;
   the multiplier order is the matching chain rule. The breaker runs the
   opposite convention as a second reading; a convention-dependent count
   is reported as such, never silently.
3  fixed points are counted on R only; the off-core diagnostic is not a
   claim.
4  the H2 test (M^2 - I)^6 = 0 is computed directly by matrix products,
   independent of the Hessenberg charpoly code that produces M2.
5  matrix memoization affects speed only; every reported object is exact.
6  k = 0 and k = 1 rows are audits of public rows and of disclosed hand
   derivations (D2, D3); the new content of the candidate begins at k = 2.
```

### 5. Failure threshold

```text
Any G-gate FAIL: STOP, record, do not proceed to hypotheses; the candidate
is not evaluable against a basis that fails its own audit.
H1 fires on any (k, eps) in range with an empty fixed set: recorded F for
the existence hypothesis; the strong reading (a state-level RG fixed point
floor for the binary leg) is dead in the tested range.
H2 fires on any fixed multiplier with an eigenvalue outside {1, -1}:
recorded F for the mirror-spectrum hypothesis; the recorded spectra become
the primary data of the lane.
H0, H3 fire: recorded, first-class, no STOP.
No tolerance anywhere. Every comparison is exact. No threshold moves after
this freeze. A crashed verifier is an engineering defect, repaired with the
crash recorded and a revision bump before any rerun; it earns nothing.
```

### 6. Action layer

```text
L5 finite kernel structure. No lift is named. Explicitly out of scope: any
continuum or scaling limit, any critical exponent, any C(mu) or positivity
object, any measure or L6 statement, any physics reading, any all-scale
law, any periodic-point census beyond fixed points, any registry, frontier,
Canon, or site edit on either line.
```

## Falsifier map, restated in one block

```text
G01..G11 FAIL        -> STOP, currency or implementation problem, recorded
H1 empty fixed set   -> F for existence in range, first-class, archived
H2 foreign eigenvalue-> F for the pm1 spectrum hypothesis, spectra become
                        the result
H0, H3 fail          -> recorded, hand derivation or extension wrong,
                        no STOP
```

## Environment

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_rg_fixedpoint_1.py
```

The stdout SHA-256 and the exit code are recorded in the result document
together with neutral platform fields. Promotion, if any, is a later public
probe under POLICY.md; this document authorizes none.
