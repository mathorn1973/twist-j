# C-LI2-PENTAGON-BALANCE-1

```text
STATUS      candidate-T. NON-CANONICAL. No authority. Promotes nothing.
LANE        incubation, this project. Target line on promotion: PUBLIC,
            mathorn1973/twist-j, registry section 16 "p = 5 and the wall".
DATE        2026-08-01
BASIS       Public Canon v30, tag canon-v30.
            CONTENT_COMMIT 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
            CANON_SHA256   2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
            CANON_BYTES    157167, canon/SHA256SUMS 5 of 5 OK, tag and content
            commit both ancestors of main (head b8d4d58).
LAYER       none. This is an archimedean special-value statement. It declares
            no layer because it makes no L1-L6 reading. Any lift needs its own
            named gate.
SCOPE       archimedean special values in the standard embedding, principal
            logarithm and principal dilogarithm. No physical lift, no field
            trace, no imaginary-part claim, no substrate coupling, no anchor.
LANE MERGE  RESOLVED 2026-08-01. C-LI2-MODULUS-POINTS-1, proposed but never
            opened by claude/RECON-TWIST6D-LEGACY-DECODER_2026-07-31.md
            section 5.2, is RETIRED INTO this candidate. Its content (the
            Landen partition of the modulus points) is T5 here, obtained as a
            corollary of the collapse rather than imported. One lane, not two.
            Do not open C-LI2-MODULUS-POINTS-1.
REPO       landed as branch notes/C-LI2-PENTAGON-BALANCE-1, commit
            80bd13295142ff122c959bf15a902691f6190751, base b8d4d58, author
            A. M. Thorn <thorn@twistj.com>, 6 files under
            notes/C-LI2-PENTAGON-BALANCE-1/. All repo gates green locally.
            NOT PUSHED: this session had no push credential. Handover in
            claude/HANDOVER-C-LI2-PENTAGON-BALANCE-1_2026-08-01.md.
```

## Dependencies

```text
WALL-LI2-RUNG      [T]  supplies the four wall values and the orbit sum pi^2/5
WALL-CIRCLE-LEMMA  [T]  supplies W_N = pi^2 (N-1)(N-2)/(12N) for all N >= 3
J-PROJECTIONS      [T]  supplies |J| = phi^-1
external           classical Abel five-term relation for the Rogers
                   dilogarithm, and L(x) + L(1-x) = zeta(2)
```

Nothing here is stronger than WALL-LI2-RUNG. The wall values are quoted, not
re-derived.

## Statement

Write r = |J| = phi^-1, and L for the Rogers dilogarithm
L(x) = Li_2(x) + (1/2) log x log(1-x) on 0 < x < 1.

### T1, the golden complement

```text
1 - |J| = |J|^2 = J conj(J) = phi^-2
```

exact in Q(sqrt5), with the two right-hand members the registered modulus
chord.

### T2, the collapse, and that it forces the golden point

Putting x = y = r in Abel's five-term relation makes both right-hand arguments
equal to x/(1+x). Setting x/(1+x) = x^2 is, as an integer polynomial identity,

```text
x - x^2(1+x) = -x(x^2 + x - 1)
```

so the collapse holds if and only if x^2 + x - 1 = 0. The five-term relation
therefore degenerates to

```text
2 L(r) = 3 L(r^2)
```

at the golden point and at no other positive point.

### T3, the term-count lemma

With the complement relation L(r) + L(r^2) = zeta(2) as first row and a
collapse p L(r) = q L(r^2) as second row, the system is [[1,1],[p,-q]] and

```text
det = -(p + q)
```

For Abel's relation (p,q) = (2,3) and det = -5. The 5 in the defect is the term
count of the functional equation. It is not an independent derivation of p = 5
from the axiom, and this candidate does not claim it is.

### T4, the solved system

```text
L(r)   = (3/5) zeta(2) = pi^2/10
L(r^2) = (2/5) zeta(2) = pi^2/15
L(r) - L(r^2) = (1/5) zeta(2) = pi^2/30
```

### T5, the Rogers correction cancels, and the Landen values follow

With l = log phi, both Rogers corrections equal l^2, hence

```text
L(r) - L(r^2) = Li_2(r) - Li_2(r^2) = pi^2/30
Li_2(phi^-1)  = pi^2/10 - log^2 phi
Li_2(phi^-2)  = pi^2/15 - log^2 phi
Li_2(phi^-1) + Li_2(phi^-2) + 2 log^2 phi = zeta(2)
```

The last three are Landen's classical values; they are consequences here, not
inputs. This subsumes the C-LI2-MODULUS-POINTS-1 proposal.

### T6, the balance

```text
sum_(a=1)^4 Re Li_2(sigma_a(J)) = 2 L(|J|) = 3 L(J conj(J)) = (6/5) zeta(2)
```

equivalently, subtracting Basel from each side,

```text
W(J) - zeta(2) = L(|J|) - L(J conj(J)) = (1/5) zeta(2) = pi^2/30
```

### T7, balance selection

For integer N >= 3, N != 4, let r_N be the minimal nonzero modulus among
1 + zeta_N^a, that is 2 sin(pi/2N) for odd N and 2 sin(pi/N) for even N, and
let W_N be the wall sum of WALL-CIRCLE-LEMMA. Then

```text
W_N = 2 L(r_N)     <=>   N = 5
W_N = 3 L(r_N^2)   <=>   N = 5
```

Proof. W_N/zeta(2) = (N - 3 + 2/N)/2 is strictly increasing for N >= 3. r_N is
strictly decreasing within each parity class. L is strictly increasing on (0,1)
because L'(x) = -log(1-x)/(2x) - log(x)/(2(1-x)) has both terms positive. So
the gap is strictly increasing within each class and has at most one zero per
class. N = 5 is a zero, both sides being pi^2/5. The even class has no integer
zero, the gap being negative at N = 6 and positive at N = 8. N = 4 is excluded
because r_4 = sqrt2 > 1. QED.

## Explicit non-claims

```text
1  The balance is an equality of two RATIONAL multiples of zeta(2). Both legs
   lie a priori in the one-dimensional Q-vector space zeta(2)Q, because
   W_N/zeta(2) is rational for every N by WALL-CIRCLE-LEMMA. Numerical
   agreement is therefore not evidence and is not offered as evidence.
2  No morphism between the two derivations is claimed. The wall leg is Euler
   reflection plus the Bernoulli boundary value Re Li_2(e^(i theta)) =
   pi^2 B_2(theta/2 pi). The modulus leg is complement plus five-term collapse.
   They are different arguments that produce the same rational.
3  The coefficients 2 and 3 are the left and right term counts of Abel's
   relation. They take these values at every point where the collapse occurs
   and carry no dependence on J. They are NOT two forces and NOT three spatial
   dimensions. Any such reading is an unnamed lift and is refused here.
4  No field-trace claim. No imaginary-part claim. Im Li_2(J) is not zero.
5  No anchor. Every value here is dimensionless. H-ANCHOR-FORCED is untouched.
6  T7 selects an ORDER, not a field. Q(zeta_10) = Q(zeta_5).
```

## Falsifier

```text
F1  the identity x - x^2(1+x) = -x(x^2+x-1) fails
F2  2 L(phi^-1) != 3 L(phi^-2), or either differs from 3 zeta(2)/5, 2 zeta(2)/5
F3  the orbit sum differs from (6/5) zeta(2), i.e. WALL-LI2-RUNG is wrong
F4  det [[1,1],[p,-q]] != -(p+q) for some p, q
F5  some integer N >= 3, N != 4, other than 5 satisfies W_N = 2 L(r_N) or
    W_N = 3 L(r_N^2)
F6  monotonicity (i), (ii) or (iii) in the T7 proof fails
F7  r_N is not the minimal nonzero modulus at the stated parity formula
```

Any of F1 to F7 fires the candidate. None of them is a threshold that can be
moved; all are exact.

## Evidence

```text
verify_li2_pentagon_balance_1.py  sha256 6f9e449ee0d8e3aa8a7f208f8757689eae77c1e617494d8e79183d6396e97e05
  stdout                          sha256 ea439c3831af84f42bd2c2837e80505c1b778b5c5151619764bf0e864585085e
  67 checks, 0 failures
break_li2_pentagon_balance_1.py   sha256 0164a199301c10be836709d2d0a2efa43ca78b50227508f53bf95a1c2b264305
  stdout                          sha256 755d8d614733e131e057978531d68c6c9dcb6152a30467d40d67627d3a61dd49
  29 checks, 0 failures, 2 hits, both against material NOT carried here
platform  Ubuntu 24.04.4, x86_64, Python 3.11.15. ONE architecture only.
grade     audit. The verifier was written after the source material was read.
          A public probe requires a fresh preregistration, a pin before first
          execution, and a second architecture with byte-identical stdout.
```

## Break record

The breaker attacked five things and landed two hits, both on material that has
been removed from this candidate as a result:

```text
attacked  the printed "wall uniqueness" Delta_N = zeta(2)/N
result    HIT. Its normal form is N(N-5) = 0. Shaped tautology. REMOVED.
attacked  the printed modulus uniqueness over the root-circle family
result    HIT. N = 10 also satisfies 1 - r_N = r_N^2, since
          r_10 = 2 sin(pi/10) = phi^-1. The odd-N restriction was unjustified.
          REMOVED and REPLACED by T7, which kills N = 10 correctly:
          W_10 = (18/5) zeta(2) while 2 L(r_10) = (6/5) zeta(2).
attacked  the collapse and the balance, by independent quadrature
          (Simpson on -log(1-t)/t, not the verifier's Bernoulli series)
result    survived, agreement below 1e-9
attacked  T7, by exhaustive sweep N = 3..1001 in both parities
result    survived, N = 5 the unique integer solution of either equation
attacked  the evidential weight
result    HIT, recorded above as non-claim 1 rather than removed
```

A candidate that has not survived one honest attempt to break it is not ready.
This one was attacked, lost two sections, and is stated here without them.
