# PREREG C-TM-WALSH-INERTIA-1

DATE 2026-08-10 (UTC). One named session, this candidate only.
CANDIDATE: C-TM-WALSH-INERTIA-1. No authority. Incubation lane of the TWIST-J
project.
TARGET ON PROMOTION: a `notes/` NON-CANONICAL note in mathorn1973/twist-j,
feeding the same classical-mathematics paper lane as C-TM-MOEBIUS-1. No
registry row is proposed by this document. No J-coupling, no physical reading.
LAYER: L1 (state; arithmetic and linear algebra of the finite divisor cube).
No lift to L2..L6 is claimed.

CURRENCY GATE (passed before this freeze): mathorn1973/twist-j main, STATUS
ACTIVE, Public Canon v41, tag canon-v41 = 278b5348c7ac, content commit
096e97b44727 ancestor of main, canon/SHA256SUMS 5 of 5 OK, CANON.md sha256
a15474c4204db637d7ce276ef6ea5dbe94b50af593e46389fd5e77aa16ca80e8, 198932
bytes. Registry dependencies read from the clone.

COLLISION SCAN. `claude/` of the project and the public repository scanned for
`walsh`: no existing candidate, probe, or registry row. Nearest lanes:
C-TM-MOEBIUS-1 (frozen 2026-08-10; the scalar theory of c whose A4, A5, A6,
A7 this candidate consumes), the Linux x86_64 leg sigma=1 Hankel program (the GLOBAL
bilinear operator H[m,n] = c(mn)/(mn); disjoint object, cross-referenced as
context only), public rows MOBIUS-TM-PRIME2-BRIDGE [T] and
TM-MULTIPLICATION-CARRY-DEFECT [T] (dependency edges). No collision.

PROVENANCE OF THE FREEZE. The operator reading was proposed by the owner in
conversation on 2026-08-10 (divisor-cube convolution operator, its Walsh
spectrum, trace and Frobenius moments, rank-one extremality, the two-bit gate
dichotomy, the carry twist). This document freezes the claim list, statuses,
falsifiers, and verifier gates BEFORE the pinned verifier is written and run.
Hand proofs precede the freeze; the census numbers of E8 are unknown at freeze
time and no census computation has been run.

## Notation fence (F1), inherited from PREREG-C-TM-MOEBIUS-1

`tau` is NOT used; it collides with the classical divisor function. Throughout:

```
t(n) = (-1)^(s_2(n)),  s_2 = binary digit sum,  t(1) = -1
c = mu * t (Dirichlet convolution), NOT the pointwise product mu(n) t(n)
evil: s_2 even.  odious: s_2 odd.
```

Fixed setup for every claim below: n odd squarefree, P its prime set,
k = omega(n) = |P|, G = powerset of P identified with F_2^k in the ascending
prime order, n_x = product of the primes in x for x in G, n_empty = 1.

```
sign vector    a_n(x) = -t(n_x), so a_n(empty) = -t(1) = +1
operator       A_n(x,y) = a_n(x XOR y), a real symmetric 2^k by 2^k matrix
characters     chi_u(x) = (-1)^(|u AND x|)
Walsh values   what(u) = sum over x of a_n(x) chi_u(x)   (unnormalized)
top character  u = P
inertia        (n_pos, n_neg, n_zero) of the eigenvalue multiset
```

## Field 1. EQUATION (frozen claims, with status label and falsifier)

```
E1  DIAGONALIZATION                                              candidate-T
    The 2^k characters chi_u form a complete orthogonal eigenbasis of A_n and
    A_n chi_u = what(u) chi_u for every u. The spectrum of A_n, with
    multiplicity, is the unnormalized Walsh spectrum of a_n.
    FALSIFIER: one (n, u) with A_n chi_u != what(u) chi_u.
    PRIORITY: standard finite abelian harmonic analysis. Exposition only.

E2  EIGENVALUE READING OF c                                      candidate-T
    what(P) = (-1)^(k+1) c(n). Equivalently, c(n) is, up to the parity sign
    (-1)^(k+1), the top-character eigenvalue of A_n. This is A4 of
    C-TM-MOEBIUS-1 (and the odd-squarefree Boolean formula of public row
    MOBIUS-TM-PRIME2-BRIDGE) read as a spectral statement; no new scalar
    identity is claimed.
    FALSIFIER: one n where what(P) != (-1)^(k+1) c(n).

E3  EXACT FIRST TWO MOMENTS                                      candidate-T
    tr A_n = 2^k and ||A_n||_F^2 = sum over u of what(u)^2 = 4^k, exactly,
    for every n in scope, independent of which primes divide n. (Parseval
    plus a_n(empty) = +1; the +1 is forced by t(1) = -1.)
    FALSIFIER: one n violating either identity.

E4  EXTREMAL RIGIDITY, RANK ONE ON THE TOP CHARACTER             candidate-T
    The following are equivalent:
      (i)   |c(n)| = 2^k  (the A5(a) bound of C-TM-MOEBIUS-1 is attained);
      (ii)  A_n = 2^k Ptop, Ptop the orthogonal projector onto chi_P;
      (iii) t(n_x) = (-1)^(|x|+1) for every x in G  (the A5(c) congruence).
    At equality the sign is forced: c(n) = (-1)^(k+1) 2^k. In particular one
    eigenvalue consumes the entire Frobenius norm and the trace forces it
    positive.
    PRECISION FENCE: rank one alone is strictly weaker than extremality.
    A_n = 2^k Pu for a character u != P occurs and forces c(n) = 0, not
    |c(n)| = 2^k. Named witnesses: n = 7 (u = empty; every divisor odious)
    and n = 33 (u = {3}; the canon witness c(33) = 0 of row
    TM-MULTIPLICATION-CARRY-DEFECT). General criterion:
    A_n = 2^k Pu iff t(n_x) = -chi_u(x) for every x.
    FALSIFIER: an n satisfying one of (i)..(iii) and violating another; an
    extremal n with c(n) != (-1)^(k+1) 2^k; a rank-one A_n violating the
    character criterion.

E5  EVEN DEGENERACY, SPECTRAL FORM OF A2                         candidate-T
    For n even squarefree the same definitions give what(P) = 0, because
    c(n) = 0 (A2 of C-TM-MOEBIUS-1, public row even-annihilation clause).
    The top character is always in the kernel of the even cube. No novelty;
    this is A2 read through E2.
    FALSIFIER: one even squarefree n with what(P) != 0.

E6  TWO-BIT GATE DICHOTOMY                                       candidate-T
    For F(x,y) = a0 XOR a1 x XOR a2 y XOR a12 xy on F_2^2 with sign vector
    (-1)^F and operator built as above:
      a12 = 0 (affine, 8 gates): exactly one nonzero Walsh value, equal to
      +-4; the operator has rank one. XOR spectrum {4,0,0,0} up to order.
      a12 = 1 (bent, 8 gates): all four Walsh values have absolute value 2;
      inertia (3,1,0) if F(0,0) = 0 and (1,3,0) if F(0,0) = 1. AND spectrum
      {2,2,2,-2}, OR spectrum {-2,2,2,2}, and (A_AND/2)^2 = I.
    PRIORITY: standard Boolean harmonic analysis (bent functions). Exposition
    only; claimed as the base case of the carry chain, not as new.
    FALSIFIER: any of the 16 spectra or inertias differing.

E7  CHARACTER TWIST AND THE CARRY MODELS                         candidate-T
    (a) Multiplying a sign vector by a character chi_v translates the Walsh
    support by v and preserves the inertia multiset; a global sign flip swaps
    (n_pos, n_neg). Diagonal +-1 conjugation D A D preserves the spectrum.
    (b) Tensor slab: on F_2^(k1+k2), if s(x, w) = s1(x) chi_w0(w) then
    shat(u, w) = s1hat(u) 2^(k2) [w = w0].
    (c) Consequently the two carry models of public row
    TM-MULTIPLICATION-CARRY-DEFECT, (P AND Q) XOR K and (P OR Q) XOR K on
    F_2^3, both have spectrum {4,4,4,-4,0,0,0,0} and active inertia (3,1):
    the XOR carry bit is a character twist that moves Walsh support and
    cannot change the (3,1) signature of the AND/OR nonlinearity.
    FALSIFIER: a computed spectrum or inertia differing; a diagonal
    conjugation changing the char-poly of the AND operator.

E8  CENSUS AT N = 200000 AND WITNESSES                           candidate-C
    Recorded at the pinned range, odd squarefree n <= 200000 (k <= 5), all
    exact integers: counts by k; extremal counts by k and the equivalence
    E4(i) iff E4(iii) iff single top support checked both directions on every
    n; forced-sign check on every extremal n; rank-one census classified by
    (k, |u|); the full inertia histogram of A_n by k. Direct witnesses beyond
    the sieve, by subset enumeration only: k = 6 at n = 255255 and k = 7 at
    n = 4849845 (E2, E3, bound); the A7 extremal witnesses of C-TM-MOEBIUS-1
    at k = 4 (n = 7461177) and k = 5 (n = 55888786221) re-verified by an
    independent implementation, including E4 at those n.
    FALSIFIER: independent recomputation disagreeing on any recorded count.
```

## Field 2. CODE

```
verifier   verify_tm_walsh_inertia_1.py, written AFTER this freeze
rules      Python standard library only; integer arithmetic only; no float
           anywhere; under 120 s; run with
           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC;
           deterministic stdout; no wall clock, no hostname, no machine
           identifier in stdout; run twice, byte-identical stdout required.
```

Verifier gates, all exact: V1 = E6 with complete matrix-action eigencheck of
all 16 gates; V2 = E7(a) by exhausting all 16 diagonal conjugations of the AND
operator with Newton-identity characteristic polynomials; V3 = E7(b)(c) with
matrix-action eigencheck and the slab comparison against twice the AND
spectrum; V4 = E1, E3 by direct matrix trace, Frobenius, and action on all
characters, for every odd squarefree n <= 105 plus n = 1155 and n = 15015;
V5 = E2, E3, E4, E8 census over all odd squarefree n <= 200000 by fast Walsh
transform; V6 = E8 witnesses at k = 6, 7 and the A7 cross-checks at k = 4, 5;
V7 = E5 on every even squarefree n <= 20000; V8 = the F1 fences numerically
(c is not mu(n) t(n) pointwise; t is not multiplicative, witnesses (3, 11)
and 105).

Breaker gates, independent code paths: B1 = c recomputed by forward Moebius
inversion from t = 1 * c with no mu table, compared on [1, 20000]; B2 = mu by
trial-division factorization on the same range; B3 = the rank-one non-extremal
witnesses n = 7 and n = 33 verified and classified; B4 = polarization sweep,
the opposite sign vector swaps inertia on a named witness; B5 = adversarial
search of the whole census for an extremal n violating the forced sign;
B6 = popcount computed two ways on every call.

## Field 3. CARRIER AND DATA

No experimental data, no external file, no network, no randomness. The carrier
is the divisor cube of odd squarefree integers together with the binary digit
word. Independent of every TWIST-J structure: no F_5^6, no J, no selector, no
decoder. Nothing is imported from the internal line.

## Field 4. SYSTEMATICS

```
S1  polarization: t(1) = -1 fixed; the opposite convention negates a_n,
    swaps inertia components, and negates what(P); fenced by B4.
S2  normalization: Walsh values here are UNNORMALIZED (sum, not average).
    A4 of C-TM-MOEBIUS-1 states the NORMALIZED top coefficient; the exact
    bridge is what(P) = (-1)^(k+1) c(n) versus
    c(n) = (-1)^k 2^k that-normalized-coefficient. Both are checked.
S3  ordering: the cube is indexed in ascending prime order; all statements
    are basis-free (spectra, inertia), so the order is presentation only.
S4  single platform: this session runs one architecture (x86_64). All
    computation-grade rows stay candidate-C. Promotion needs the standard
    two-platform byte-identical protocol.
S5  arithmetic: Python integers, exact and unbounded; no float anywhere.
```

## Field 5. FAILURE THRESHOLD

Zero tolerance. Any single counterexample to E1..E7 fires that row to F. Any
disagreement in an E8 recorded number fires E8. No threshold moves after the
fact. A fired falsifier is archived, not deleted. A defect demonstrated to be
in the verifier implementation rather than in a claim is an integrity STOP,
recorded with both file hashes, and is not a scientific falsification; the
corrected verifier is archived alongside, never silently substituted.

## Field 6. ACTION LAYER AND WHAT IS EXPLICITLY NOT CLAIMED

Layer L1 throughout. No lift is claimed.

```
NOT CLAIMED  any statement about zeta zeros, RH, Weil positivity, explicit
             formulae, or any analytic-number-theory bound
NOT CLAIMED  any connection to the sigma=1 Hankel operator H[m,n]=c(mn)/(mn)
             beyond shared coefficients; H is a different operator and its
             certificates are cited as context only
NOT CLAIMED  novelty for E1, E6, or the bent-function facts (standard); for
             E2 as a scalar identity (it is A4 restated); for E5 (it is A2)
NOT CLAIMED  any density, growth, or infinitude statement about extremal n
             (that is O-TM-EXTREMAL-ALL-K of C-TM-MOEBIUS-1, untouched here)
OPEN         O-TM-WALSH-INERTIA-LAW: determine the inertia of A_n as a
             function of n (equivalently the sign distribution of the 2^k
             Walsh values); the census of E8 is the first data. Closes
             positively with a theorem deriving inertia(A_n) from the carry
             field of n; a frozen conjectured law acquires its own falsifier
             when frozen. Not a registry row proposal.
OPEN         O-TM-WEIL-COMPRESSION: whether any admissible test family for a
             Weil-type finite compression admits a basis in which the
             compressed form carries the divisor-cube Walsh structure above,
             or a proved no-go. Recon question only; no row, no claim, and
             nothing in E1..E8 depends on its answer.
```

FROZEN 2026-08-10 (UTC), before the verifier was written. The two known
no-go facts recorded at freeze time, to be treated as fences and not as
results: replacing Lambda(n)/sqrt(n) by t-weighted coefficients in an
explicit formula is not available to this lane (t is not a Dirichlet
character and not multiplicative, V8); resigning a fixed orthonormal basis
by any diagonal +-1 gauge cannot change trace, Frobenius norm, or inertia
(E7(a), V2).
