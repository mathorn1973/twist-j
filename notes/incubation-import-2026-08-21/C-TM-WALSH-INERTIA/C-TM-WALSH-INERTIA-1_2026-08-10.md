# C-TM-WALSH-INERTIA-1: the divisor-cube sign operator, its spectrum, and its inertia

STATUS: candidate. No authority. Incubation lane of the TWIST-J project.
DATE 2026-08-10 (UTC). One named session, this candidate only.
LAYER: L1. No lift claimed. No RH, no zeta, no J, no physical reading.

PINS

```
PREREG    claude/PREREG-C-TM-WALSH-INERTIA-1.md
          sha256 155b0a0ecf767278f67b3fb4fc5a75e22d1c9918b1bc49c262f7f9c67f57e667
          frozen before the verifier was written
verifier  claude/verify_tm_walsh_inertia_1.py
          sha256 0b56ebd126c876f2de98b737820b22890074ab88f248f47a90f1b74fa1efd646
stdout    sha256 e918be46b17cb03fce9ea21a66a4167ab87fcfaba571f52951cf4abd4bfac40a
          3257 bytes, exit 0, two runs byte-identical, runtime about 2 s
platform  Ubuntu 24.04, x86_64, Python 3.11.15, standard library only, exact
          integers only, no float anywhere. SINGLE PLATFORM: every computed
          row is capped at candidate-C until the two-architecture protocol.
result    47 gates PASS, 0 FAIL. No falsifier fired.

verifier v2 (current pin going forward)
          claude/verify_tm_walsh_inertia_2.py
          sha256 7a8e4e14aec22ac10f200cffabd98dc354f9e948f5cc32c3cd1862ab6bd10929
          stdout sha256 537af5c7da7140bfc6b2d58a05b48d043bc9755533d82abe670abd7e89b98971
          exit 0, two runs byte-identical, 47 gates PASS, gate list byte-equal
          to v1. Diff against v1 is presentation only, on owner directive of
          2026-08-10: an INERTIA_ORDER declaration block in the header and
          named POS NEG ZERO fields on the witness lines. No gate, range,
          threshold, or claim changed. v1 stays archived as the sealed first
          formal run.
```

TWO-PLATFORM PIN (2026-08-10/11): verifiers v1 and v2 reran on a second leg,
Debian 13 aarch64 Python 3.13.5, file hashes verified before execution,
stdout byte-identical to the x86_64 leg (v1: e918be46..., v2: 537af5c7...).
Full record: claude/RUN-TWO-PLATFORM-PIN_2026-08-10.md. The single-platform
cap note above is superseded by that record; labels unchanged.

INERTIA ORDER, cross-branch hazard. This lane prints (POS, NEG, ZERO). The
Linux x86_64 leg sigma=1 Hankel branch prints (NEG, ZERO, POS); its (257,0,255) means
257 negative, 0 zero, 255 positive. Never read one branch's tuple in the
other's order. On any future merge of the branches, unnamed tuples are to be
dropped entirely in favor of named fields (owner directive 2026-08-10).

Notation fence F1 of PREREG-C-TM-MOEBIUS-1 is in force: t(n) = (-1)^(s_2(n)),
t(1) = -1, c = mu * t as a Dirichlet convolution. tau is not used.

## 1. The object

For n odd squarefree with prime set P, k = omega(n), and x a subset of P, put
n_x = product of x, a_n(x) = -t(n_x), and let A_n be the 2^k by 2^k real
symmetric convolution operator A_n(x,y) = a_n(x XOR y) on the divisor cube.
The owner proposed on 2026-08-10 to stop reading the scalar c(n) alone and to
read this operator, its full Walsh spectrum, and its inertia. This document
closes the finite theory and records the first census.

## 2. Claims and outcomes

```
E1  candidate-T  PASS   characters diagonalize A_n; spectrum = unnormalized
                        Walsh spectrum of a_n. Standard; exposition.
E2  candidate-T  PASS   what(P) = (-1)^(k+1) c(n): the Moebius transform is
                        the top-character eigenvalue up to a parity sign.
                        Scalar content identical to A4 of C-TM-MOEBIUS-1 and
                        to public row MOBIUS-TM-PRIME2-BRIDGE; the operator
                        reading is the new part.
E3  candidate-T  PASS   tr A_n = 2^k and ||A_n||_F^2 = 4^k exactly, for every
                        n in scope, independent of the primes. The two moments
                        that are hard analytic input for a Weil-form
                        compression are definitional here.
E4  candidate-T  PASS   extremal rigidity: |c(n)| = 2^k iff A_n = 2^k Ptop
                        iff the A5(c) congruence; at equality the sign is
                        forced, c(n) = (-1)^(k+1) 2^k, because one eigenvalue
                        consumes the whole Frobenius norm and the positive
                        trace selects its sign. PRECISION FENCE: rank one
                        alone is strictly weaker. A_n = 2^k Pu happens for
                        u != P and forces c(n) = 0. Witnesses n = 7
                        (u empty) and n = 33 (u = {3}; the canon witness
                        c(33) = 0 of TM-MULTIPLICATION-CARRY-DEFECT).
                        General criterion: A_n = 2^k Pu iff t(n_x) =
                        -chi_u(x) for all x.
E5  candidate-T  PASS   even squarefree cubes: c(n) = 0 (A2) read spectrally:
                        the top character always lies in the kernel.
E6  candidate-T  PASS   two-bit gates: affine iff rank one (XOR spectrum
                        {4,0,0,0}); bent iff all |Walsh| = 2 with inertia
                        (3,1,0) or (1,3,0) by F(0,0). AND spectrum
                        {2,2,2,-2}, OR {-2,2,2,2}, (A_AND/2)^2 = I. Standard;
                        base case of the carry chain.
E7  candidate-T  PASS   character twist: chi_v multiplication translates
                        Walsh support and preserves inertia; global sign flip
                        swaps it; diagonal +-1 conjugation preserves the
                        spectrum (all 16 conjugations of AND exhausted by
                        exact characteristic polynomials). Carry models
                        (P AND Q) XOR K and (P OR Q) XOR K: spectrum
                        {4,4,4,-4,0,0,0,0}, active inertia (3,1). The XOR
                        carry bit moves Walsh support and cannot change the
                        AND/OR signature.
E8  candidate-C  PASS   census at N = 200000 and the witnesses below.
```

Proof sketches, complete at this scale. E2: expand mu(n/d) = (-1)^(k-|S|) on
the squarefree cube and compare with the top Walsh sum; the minus in a_n and
t(1) = -1 cancel to the stated parity sign. E3: a_n(empty) = +1 gives the
trace; Parseval gives the Frobenius norm since a_n is a sign vector. E4:
Parseval plus the trace as in the claim text; the equivalence with A5(c) is
the statement that a_n equals the top character as a vector. E7(b): characters
factor across a product of groups.

## 3. Census, exact integers (candidate-C, single platform)

Odd squarefree n <= 200000 by k, then extremal counts:

```
counts    k0:1  k1:17983  k2:35553  k3:22296  k4:4944  k5:277
extremal  k0:1  k1:8344   k2:4103   k3:157    k4:0     k5:0
first     k2: 69 87 115 145 213 265        k3: 4899 6095 7685 8165 9831 11615
```

k4 and k5 extremal sets exist but not below 200000; the A7 witnesses of
C-TM-MOEBIUS-1 were re-verified here by an independent implementation,
including full E4 rigidity at the witness:

```
n = 7461177     = 3.23.71.1523          c = -16  inertia (1,0,15)
n = 55888786221 = 3.23.503.857.1879     c = +32  inertia (1,0,31)
```

Rank-one census by (k, |u|), where u is the carrying character:

```
(0,0):1   (1,0):9639  (1,1):8344
(2,0):5439  (2,1):8926  (2,2):4103
(3,0):280   (3,1):874   (3,2):530   (3,3):157
(4,0):1     (4,1):9     (4,2):2
```

Rank one off the top character is common and is invisible to c: every such
cube has c(n) = 0. The scalar sees exactly one face of the rank-one family.

Inertia histograms (pos, neg, zero):

```
k1  (1,0,1):17983
k2  (1,0,3):18468   (3,1,0):17085
k3  (1,0,7):1841  (3,1,4):9534  (5,3,0):9688  (7,1,0):1233
k4  (1,0,15):12  (3,1,12):135  (5,3,8):298  (6,4,6):974  (6,10,0):52
    (7,1,8):52  (7,3,6):924  (9,7,0):1131  (10,6,0):1042  (11,5,0):257
    (13,3,0):64  (15,1,0):3
k5  32 patterns, dominated by full-rank mixed signatures; extremes include
    (14,18,0):1 and (22,10,0):5; full table in the pinned stdout
```

Large witnesses: n = 255255 (k = 6) has c = -2 and inertia (36,28,0);
n = 4849845 (k = 7) has c = 8 and inertia (64,48,16).

## 4. Post-freeze observations

P1  candidate-T (proved). At k = 1 the inertia is always (1,0,1): a = (1,a1)
    gives Walsh values {1+a1, 1-a1} = {2,0} or {0,2}. A negative eigenvalue
    requires k >= 2, that is, a genuine two-prime carry. The census confirms
    17983 of 17983.

P2  candidate-T (proved). Complete k = 2 dichotomy. For any semiprime cube
    the Walsh values are even, sum to 4, and their squares sum to 16, so
    either one value is 4 and the rest vanish (rank one; the trace forces
    +4), or all four are +-2 with exactly one -2. Hence

```
    inertia(A_pq) = (3,1,0)  iff  |c(pq)| = 2
    inertia(A_pq) = (1,0,3)  iff  c(pq) in {0, -4}
    c(pq) = +4 is impossible (the trace forces the extremal sign)
```

    matching the value set {-4,-2,0,2} of public row
    TM-MULTIPLICATION-CARRY-DEFECT and explaining its missing +4 as trace
    positivity. Census: 18468 + 17085 = 35553, no third pattern.

P3  candidate-C (data). Negative-majority cubes exist: 52 cubes at k = 4
    show inertia (6,10,0), and k = 5 shows (14,18,0). The trace fixes the
    eigenvalue SUM at 2^k, not the sign majority.

P4  candidate-C (data). The carry-slab pattern (3,1,4) of the E7 model is
    the single most common k = 3 inertia (9534 of 22296), and the rank-one
    pattern (1,0,2^k - 1) persists at every k observed.

## 5. Break attempts, recorded

```
B1  PASS  c recomputed on [1,20000] by forward inversion of t = 1 * c with
          no mu table at all; agrees everywhere; even annihilation holds on
          the window.
B2  PASS  mu by trial division against the sieve path; agrees on [1,20000].
B3  PASS  the loose reading "extremal iff rank one" is FALSE and is fenced:
          n = 7 and n = 33 are rank one with c = 0. The correct statement
          pins the top character (E4).
B4  PASS  polarization: negating the sign vector swaps (pos,neg); every
          claim is stated under t(1) = -1 and survives the sweep as fenced.
B5  PASS  adversarial census sweep for an extremal n violating the forced
          sign: zero violations in 12605 extremal cubes.
B6  PASS  popcount computed two ways on every call.
NO-GO 1   (frozen fence) t is not a Dirichlet character and not
          multiplicative (witnesses (3,11) and 105); t-weighting the
          coefficients of an explicit formula is not available to this lane.
NO-GO 2   (frozen fence) any diagonal +-1 regauging of a fixed basis
          preserves trace, Frobenius norm, and inertia (verified
          exhaustively on the AND operator); no sign gauge manufactures
          inertia.
```

## 6. Context, unpinned, cited as engineering readouts only

The Linux x86_64 leg sigma=1 program certifies spectral facts about the GLOBAL
bilinear operator H[m,n] = c(mn)/(mn) on ell2: ground states of the odd
compression at N = 511 with finite inertia (128,0,128), infinite-operator
bounds n_-(H) >= 128 and n_+(H) >= 128, the exact Schur rung to C_512 with
inertia (257,0,255) hence n_-(H) >= 257, n_+(H) >= 255, and the running
C_1024 extension (preflight 640 complete, production live at this writing).
The tail majorants there consume exactly the A5(a) bound |c(m)| <= 2^omega(m).
E4 of this candidate classifies the n where that bound is attained, so the
local rigidity theorem and the global inertia program are two readings of one
coefficient pair (t, c). A_n and H are different operators; nothing here
promotes either into the other.

External datapoint, assessed in claude/RECON-ZETA23-VERIFICATION-STANDARD:
the 2026-08-10 Anthropic zeta result replaces global positivity by counting
positive directions of a compressed Weil form, with trace and Frobenius norm
as the analytic inputs. In this candidate the analogous two moments are exact
and free (E3), and the whole arithmetic content sits in the sign distribution
(the census of section 3). The mechanism rhymes; no transfer is claimed.

## 7. Open lanes

```
O-TM-WALSH-INERTIA-LAW   determine inertia(A_n) as a function of n; the
                         census is the first data; first milestones: prove
                         the complete k = 3 pattern classification the way
                         P2 closes k = 2, and decide whether the negative
                         share admits a limit law. A frozen conjecture will
                         carry its own falsifier. Not a registry row.
O-TM-WEIL-COMPRESSION    does any admissible Weil test family admit a finite
                         compression carrying this divisor-cube Walsh
                         structure, or is there a proved no-go. Both answers
                         are first-class. Recon question only; nothing above
                         depends on it; no RH content is claimed.
```

OWNER RULING on the closure bar of O-TM-WALSH-INERTIA-LAW (2026-08-10, after
the freeze, recorded here without touching the frozen prereg): "derive the
inertia from the carry field" is near-tautological if the carry field means
all 2^k subset parities, since that data is essentially the whole cube. The
lane closes positively ONLY with a genuine compression: a finite state
independent of k, or a recursion under adding one prime, or a bounded set of
carry moments, or low-degree Walsh data, or O(poly k) invariants determining
the inertia. Absent such a compression the lane is to be recorded as
exposition to the Moebius paper, not as a program. The census E8 is a map of
the terrain, not the prey.

SUCCESSOR LANE. The owner opened the bridge question on 2026-08-10: the
divisor-restricted block of the global Hankel operator splits as an
XOR-diagonalizable base plus an intersection-square carry defect. Recon and
the proposed candidate id C-TM-HANKEL-XOR-DEFECT-1 live in
claude/RECON-C-TM-HANKEL-XOR-DEFECT-1_2026-08-10.md. The full-spectrum
tensor identity (the 2 by 2 integer operator whose k-th tensor power maps
the c-cube to the Walsh spectrum) is deliberately NOT added to this frozen
candidate and is part of that successor lane.

## 8. Promotion path

A fold consuming this candidate needs: the two-architecture byte-identical
protocol on verify_tm_walsh_inertia_1.py; a notes/ NON-CANONICAL landing in
mathorn1973/twist-j (no registry row proposed); and the E-list carried at
candidate-T for the proved rows and candidate-C for the census, never higher.
The natural publication surface is the same classical paper lane as
C-TM-MOEBIUS-1, as an operator section.
