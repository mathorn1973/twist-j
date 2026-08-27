# C-GRH-QSQRT5-SPLIT-ORIENTATION-1. GRH(zeta_Q(sqrt5)) read on the pure split-orientation channel O_5

```text
CANDIDATE ID:   C-GRH-QSQRT5-SPLIT-ORIENTATION-1
DATE:           2026-08-27
SESSION:        agent lane claude/grh-zeta-split-orientation-lq2sh8
TARGET ROW:     none opened. Reads J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]
                forward across its own continuation fence, with the analytic
                inputs imported as labeled classical facts.
                TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] is untouched; see
                section 8 for why this note cannot feed it.
PARENTS:        probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1 (the frozen C_0,
                O_5 Euler products and 1/zeta = C_0 O_5);
                notes/C-J-DEDEKIND-WEIL-ROAD-N.md (GRH factor taxonomy, there
                for the quartic field Q(zeta_5));
                notes/incubation-import-2026-08-21/C-PRIME-BOOLE
                (Mertens-form RH equivalences as literature imports);
                notes/incubation-import-2026-08-21/C-PRIME-ORDER-READING
                (zeta_F = zeta L(chi_5) for F = Q(sqrt5); square-root
                fairness vocabulary).
LAYER:          L1 exact Euler-factor algebra, plus classical analytic
                continuation facts imported as [T-lit]. No decoder, measure,
                physical, SI, or L2-L6 lift is claimed.
AUTHORITY:      none. NON-CANONICAL candidate document per POLICY.md.
                No public T/D/C/H/O/F status is created here.
                RH remains [O]. GRH(zeta_F) is not claimed, not evidenced,
                and not assumed anywhere in this note.
```

## 0. What this candidate delivers

```text
1  The Dirichlet coefficients o(n) of the Canon's orientation-independent
   split-prime product O_5(s): supported exactly on the pure
   split-orientation integers (every prime factor split, every exponent
   odd), with |o(n)| = 2^omega(n), the size of the orientation fiber
   above n, and an explicit sign law.                     [candidate-T]
2  A Dedekind regrouping: O_5(s) zeta_F(s) L(2s,chi_5)
   = zeta(4s)(1 + 5^-s + 25^-s + 125^-s) for F = Q(sqrt5), prime-locally
   and coefficientwise, with every left factor a genuine Dirichlet
   series (no Mobius inversion needed).                   [candidate-T]
3  A half-plane divisor dictionary: on Re(s) > 1/2 the meromorphic
   continuation of O_5 is G/zeta_F with G holomorphic and nonvanishing;
   its poles are exactly the zeros of zeta_F there, with multiplicity,
   and its only zero is a simple one at s = 1.
                                  [candidate-T on [T-lit] continuation]
4  The reading itself: GRH(zeta_F) holds if and only if the pure
   split-orientation channel is pole-free on Re(s) > 1/2, if and only
   if the signed orientation count T_5(N) = sum_{n<=N} o(n) obeys
   square-root cancellation.  The upward direction (channel bound
   implies GRH) is elementary given 3; the downward direction is the
   classical Perron/growth mechanism, imported, not re-proved.
                        [candidate-T up / candidate-T-lit down]
5  An unconditional floor: sigma_c(O_5) >= 1/2, so T_5(N) is not
   O(N^theta) for any theta < 1/2.  Square root is the floor
   unconditionally and the exact ceiling precisely under GRH(zeta_F).
                                  [candidate-T on Hardy [T-lit]]
6  The channel split of GRH data: C_0 is unconditionally holomorphic on
   Re(s) > 1/2 and sees only the L(s,chi_5) zeros (as zeros); O_5 sees
   the full zeta_F = zeta L(chi_5) zero set (as poles).  The
   orientation channel alone carries the whole field GRH. [candidate-T]
7  A verifier for the L1 algebra only: 7/7 exact integer gates, three
   breakers firing at frozen witnesses 5, 4, 16, stdout pinned.
```

Everything analytic below Re(s) = 1 rests on classical continuation
facts about zeta, L(s,chi_5) and zeta_F, imported as [T-lit] and named
where used. Nothing in this note produces cancellation, locates a zero,
or moves any registered row.

## 1. Notation hygiene

Two collisions are flagged before they propagate.

- `O_5(s)` in this note is exclusively the Canon's orientation-independent
  scalar split-prime Euler product of
  J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]. Elsewhere in the Canon
  the symbol `O_5` names the ring Z[zeta_5] (ramified-profile and residue
  sections). The ring never appears in this note.
- `F = Q(sqrt5)` and `zeta_F` here are the real quadratic field and its
  Dedekind zeta. The road note C-J-DEDEKIND-WEIL-ROAD-N writes `zeta_K`
  for the quartic field K = Q(zeta_5); restricting its taxonomy to the
  quadratic subfield gives `zeta_F(s) = zeta(s) L(s,chi_5)`, the form
  used throughout this note (recorded in-repo in C-PRIME-ORDER-READING). GRH(zeta_F) means: every nontrivial zero of
  zeta_F has real part 1/2, equivalently RH for zeta and GRH for
  L(s,chi_5) jointly.
- `chi_5` is the quadratic character mod 5; split means chi_5(p) = 1.
- `T = p^-s` inside local factors; `omega(n)` counts distinct prime
  factors; `sigma_c` is the abscissa of convergence of a Dirichlet
  series.

## 2. Frozen Canon inputs

From J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T] (evidence
probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1), all at formal Euler-factor
scope and absolutely convergent for Re(s) > 1:

```text
C_0(s) = sum c_0(n) n^-s
       = L(s,chi_5) L(2s,chi_5) / zeta(4s) * (1-5^-s)/(1-5^-4s),
O_5(s) = prod_(chi_5(p)=1) (1-p^-s)^2 / (1+p^-2s),
1/zeta(s) = C_0(s) O_5(s),
O_5(s) = zeta(4s)/(zeta(s) L(s,chi_5) L(2s,chi_5)) * (1-5^-4s)/(1-5^-s).
```

The row's fence, quoting the registry scope: "no continuation, zero
location, cancellation, RH, physical or L2-L6 claim" (the CANON.md
prose sentence reads "They assert no continuation, zero location,
cancellation, RH, or physical reading"). This note crosses the
continuation fence
deliberately, in a NON-CANONICAL document, with the crossing built only
from labeled classical imports; the [T] row itself is quoted, never
extended in place.

Also used: J-IDEAL-COUNT-QUADRATIC-CHARACTER [T], which gives the ideal
count of F as a_F = 1 * chi_5 (Dirichlet convolution), the coefficient
sequence of zeta_F.

## 3. QS5-CHANNEL-COEFFICIENTS [candidate-T]

The split-prime local factor of O_5 expands exactly:

```text
(1-T)^2/(1+T^2) = (1 - 2T + T^2) * sum_(j>=0) (-1)^j T^(2j)
                = 1 - 2T + 2T^3 - 2T^5 + 2T^7 - ...
                = 1 + sum_(j>=0) (-1)^(j+1) 2 T^(2j+1).
```

Every even exponent >= 2 cancels; every odd exponent survives with
coefficient +-2. Hence the Dirichlet coefficients o(n) of O_5 are
multiplicative with

```text
o(p^k) = 0                        if chi_5(p) != 1  (any k >= 1),
o(p^(2j)) = 0                     if chi_5(p) = 1, j >= 1,
o(p^(2j+1)) = (-1)^(j+1) 2        if chi_5(p) = 1, j >= 0.
```

Call n a pure split-orientation integer when every prime factor of n is
split and every exponent in n is odd; n = 1 qualifies by the
empty-product convention. Then, with a = omega(n) and J(n) = sum of
(e_i - 1)/2 over the exponents e_i of n:

```text
o(n) = 0 unless n is pure split-orientation, and there
o(n) = (-1)^(a + J(n)) 2^a,   |o(n)| = 2^omega(n).
```

The magnitude 2^omega(n) is exactly the number of orientation choices
above n: one of the two conjugate prime ideals of O_F above each split
prime dividing n. The scalar product O_5 is orientation-independent by
the [T] row; its coefficients nevertheless count the orientation fiber.
That is the sense in which the channel is pure split-orientation, and it
is the entire content of the name (QS5-ORIENTATION-READING
[candidate-D]; a reading, not a new object).

Coefficientwise, 1/zeta = C_0 O_5 is mu = c_0 * o, re-audited by gate
V03 to n <= 100000 on an implementation independent of the probe's.

## 4. QS5-DEDEKIND-REGROUP [candidate-T]

With zeta_F(s) = zeta(s) L(s,chi_5) [T-lit; in-repo restriction of the
road note's quartic factorization], regroup the closed form of O_5 by
the field rather than by the character:

```text
O_5(s) = zeta(4s) / ( zeta_F(s) L(2s,chi_5) ) * (1-5^-4s)/(1-5^-s).
```

Since (1-T^4)/(1-T) = 1 + T + T^2 + T^3 at T = 5^-s, the ramified
correction on this side of the factorization is FINITE, and the identity
takes the inverse-free form

```text
O_5(s) zeta_F(s) L(2s,chi_5) = zeta(4s) (1 + 5^-s + 25^-s + 125^-s).
```

(The infinite one-prime expansion recorded in the [T] row belongs to the
reciprocal correction on the C_0 side; the two statements are
consistent.)

Prime-local proof, term by term:

```text
split p:    (1-T)^2/(1+T^2) * 1/(1-T)^2 * 1/(1-T^2) = 1/(1-T^4),
inert p:    1 * 1/(1-T^2) * 1/(1+T^2)               = 1/(1-T^4),
p = 5:      1 * 1/(1-T) * 1                          = (1+T+T^2+T^3)/(1-T^4).
```

Each line is the local factor of the right side. Coefficientwise the
identity reads o * a_F * e_2 = r, where a_F = 1 * chi_5 is the ideal
count [T], e_2 is chi_5(m) placed at n = m^2 (the coefficients of
L(2s,chi_5)), and r(n) = 1 exactly when the prime-to-5 part of n is a
perfect fourth power, else 0. Gate V04 verifies this to n <= 100000;
every factor on the left is a genuine Dirichlet series, so the gate uses
no Mobius inversion. Gate V07 confirms the identity is tight: dropping
the 5-block, the L(2s,chi_5) factor, or the zeta(4s) factor breaks it at
first differences 5, 4, 16 respectively.

## 5. QS5-HALFPLANE-DIVISOR [candidate-T on [T-lit] continuation]

Classical imports, used from here on and nowhere above: zeta continues
meromorphically to C with a single simple pole at s = 1; L(s,chi_5) is
entire; hence zeta_F is meromorphic with a single simple pole at s = 1;
the completed zeta_F satisfies a functional equation symmetric about
Re(s) = 1/2 and its nontrivial zeros lie in 0 < Re(s) < 1; chi_5 is
real and primitive, so the completed L(s,chi_5) satisfies its own
functional equation symmetric about Re(s) = 1/2 and the nontrivial
zeros of L(s,chi_5) also lie in 0 < Re(s) < 1 (used only for the
channel split in section 6). All [T-lit].

Define the continuation of O_5 by the closed form of section 4; it is
meromorphic on C and agrees with the Euler product on Re(s) > 1. Write

```text
O_5(s) = G(s) / zeta_F(s),
G(s) = zeta(4s) (1-5^-4s) / ( L(2s,chi_5) (1-5^-s) ).
```

On Re(s) > 1/2 every constituent of G is holomorphic and nonvanishing:

```text
zeta(4s):      Re(4s) > 2, absolutely convergent Euler product;
1 - 5^-4s:     zeros only on Re(s) = 0;
L(2s,chi_5):   Re(2s) > 1, absolutely convergent Euler product,
               so 1/L(2s,chi_5) is holomorphic and nonvanishing;
1 - 5^-s:      zeros only on Re(s) = 0.
```

Therefore, on the open half-plane Re(s) > 1/2:

```text
poles of O_5  =  zeros of zeta_F, with equal multiplicity;
zeros of O_5  =  { s = 1 }, simple (the pole of zeta_F).
```

## 6. QS5-GRH-DICTIONARY and QS5-CHANNEL-SPLIT [candidate-T]

By the functional-equation symmetry of the nontrivial zeros of zeta_F
about Re(s) = 1/2 [T-lit], GRH(zeta_F) is equivalent to the absence of
zeros of zeta_F in Re(s) > 1/2. With section 5:

```text
GRH(zeta_F)  <=>  O_5 is holomorphic (pole-free) on Re(s) > 1/2.
```

That is the title of this note in one line: GRH for the Dedekind zeta of
Q(sqrt5), read on the pure split-orientation channel, is exactly the
statement that the channel continues past the Euler half-plane without
poles, all the way to the critical line.

The same bookkeeping splits 1/zeta = C_0 O_5 by channel. On Re(s) > 1/2,

```text
C_0(s) = L(s,chi_5) H(s),
H(s) = L(2s,chi_5)(1-5^-s) / ( zeta(4s)(1-5^-4s) ),
```

and H is holomorphic and nonvanishing there (zeta(4s) is zero-free and
pole-free on the open half-plane Re(s) > 1/4; its only pole, at
s = 1/4, sits on that boundary, well outside Re(s) > 1/2). Hence
unconditionally C_0 is holomorphic on Re(s) > 1/2, its zeros there are
exactly the zeros of L(s,chi_5), and, by the functional-equation
symmetry of the L(s,chi_5) zeros [T-lit, section 5],

```text
GRH(L(.,chi_5))  <=>  C_0 has no zeros on Re(s) > 1/2.
```

So the two channels of the [T] factorization carry the GRH data
asymmetrically: the zero-rapidity channel C_0 sees only the character
factor, as zeros, and can never acquire a pole; the orientation channel
O_5 sees the whole field zeta_F = zeta L(chi_5), as poles. The divisors
add back correctly to 1/zeta on Re(s) > 1/2, an internal consistency
check. In particular, a channel-Mertens statement for O_5 is pinned to
the FIELD hypothesis GRH(zeta_F), formally finer bookkeeping than the
Mertens statement for mu, which is pinned to RH for zeta alone [T-lit,
recorded as literature imports in C-PRIME-BOOLE]: the tracked pole set
zeros(zeta_F) contains zeros(zeta) strictly, as a set, while the
relative logical strength of the two hypotheses is of course open.

## 7. Summatory form: floor and bridge

Write T_5(N) = sum_(n<=N) o(n), the signed orientation count over the
pure split-orientation integers up to N.

### QS5-SUMMATORY-FLOOR [candidate-T on Hardy [T-lit]]

Unconditionally sigma_c(O_5) >= 1/2. Proof: by Hardy [T-lit] zeta has
infinitely many zeros on Re(s) = 1/2; each is a zero of zeta_F. At such
a point rho, G(rho) != 0: the only factor of G needing care on the
closed line is 1/L(2s,chi_5) at Re(2s) = 1, where the classical
nonvanishing L(1+it,chi_5) != 0 [T-lit] applies; hence rho is a genuine
pole of the continuation. A Dirichlet series is holomorphic on
Re(s) > sigma_c, and on that half-plane it agrees with the continuation;
sigma_c < 1/2 would make the continuation holomorphic at rho.
Contradiction.

Consequently T_5(N) is not O(N^theta) for any theta < 1/2: the channel
cannot cancel better than square root, with no hypothesis.

### QS5-SUMMATORY-BRIDGE-UP [candidate-T]

If for every eps > 0, T_5(N) = O_eps(N^(1/2+eps)), then by partial
summation the series sum o(n) n^-s converges on Re(s) > 1/2, is
holomorphic there, and agrees with the continuation; so O_5 is pole-free
on Re(s) > 1/2, and by sections 5 and 6, GRH(zeta_F) holds. Elementary
given the dictionary.

### QS5-SUMMATORY-BRIDGE-DOWN [candidate-T-lit]

Conversely, under GRH(zeta_F) the classical mechanism gives, for every
eps > 0, T_5(N) = O_eps(N^(1/2+eps)). Mechanism, not re-proved here:
under GRH, 1/zeta_F(sigma+it) = O_(delta,eps)((|t|+2)^eps) uniformly on
sigma >= 1/2 + delta [T-lit: Borel-Caratheodory and Hadamard product
bounds, as for 1/zeta in Titchmarsh ch. 14, extended to Dirichlet
L-functions, e.g. Montgomery-Vaughan ch. 13]; G is bounded on such
strips by absolute convergence; |o(n)| <= d(n), so the truncated Perron
formula applies with the standard error; shifting the contour from
Re(s) = 1 + 1/log N to Re(s) = 1/2 + delta crosses no pole under GRH,
and the delta -> 0 collection gives the bound. This is Titchmarsh's
proof that RH gives M(x) = O(x^(1/2+eps)), transported verbatim along
the dictionary. VERDICT: mechanism classical; import audit against
Titchmarsh sec. 14.25 and Montgomery-Vaughan before this direction is
called more than candidate-T-lit.

Together:

```text
GRH(zeta_F)  <=>  for every eps > 0:  |T_5(N)| = O_eps(N^(1/2+eps)),
```

with the upward arrow elementary (given the dictionary) and the downward
arrow classical. Square-root cancellation of the signed orientation
count is the whole of the field's GRH, and by the floor it would be
exactly sharp: square-root fairness of orientations, in the vocabulary
of C-PRIME-ORDER-READING.

### QS5-TRIANGLE-BOUNDARY [candidate-T]

The termwise triangle route is closed for this channel too, in the same
spirit as J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO [T] (which concerns the
l1 norm of the integral lift, a different sum; no overlap of scope).
The l1 series of the channel is

```text
sum |o(n)| n^-s = prod_(chi_5(p)=1) ( 1 + 2 T/(1-T^2) ),
```

and log of the right side at real s -> 1+ is 2 sum_(split) p^-s + O(1)
= log(1/(s-1)) + O(1), by the split-prime density coming from
L(1,chi_5) != 0 [T-lit; in-repo: C-SPLIT-UNIT records
ln phi = (sqrt5/2) L(1,chi_5) as literature]. Since the coefficients
|o(n)| are nonnegative, divergence along the real axis as s -> 1+ pins
the abscissa from below at 1 (Landau), while |o(n)| <= d(n) pins it
from above at 1; so the l1 series has abscissa exactly 1, and
sum_(n<=N) |o(n)| is not O(N^(1-delta)) for any delta > 0. A square-root bound on T_5 can never come from termwise
absolute values; cancellation across signs is essential.

## 8. Non-claims and the bridge-row fence

```text
1  No RH, GRH, zero-location, zero-free-region, or cancellation claim
   is made. RH remains [O]. GRH(zeta_F) and GRH(L(.,chi_5)) are targets
   of the dictionary, not assertions.
2  This note manufactures no cancellation mechanism. Every arrow into a
   summatory bound either assumes GRH (bridge-down) or assumes the
   bound (bridge-up). The content is a dictionary between half-plane
   statements and channel statements, plus one unconditional floor.
3  TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O] requires deriving
   M(N) = O_eps(N^(1/2+eps)) from the refined shell WITHOUT assuming an
   equivalent Mertens estimate, a zeta-zero statement, or the target
   bound. Every conditional statement in this note is on the forbidden
   side of that fence: feeding QS5-SUMMATORY-BRIDGE into that row would
   be circular by the row's own wording. This note therefore adds
   vocabulary and a boundary to that row, and zero progress. The row
   stays [O], untouched. Note also the mismatch of targets: the bridge
   row's target is M(N) (RH strength for zeta); the channel bound here
   is pinned to GRH(zeta_F), a formally finer target.
4  No Hecke, automorphic, adelic, or spectral identification is made or
   used; chi_5 enters only as the quadratic character mod 5.
5  No zero data, no numerical zero, and no floating-point quantity
   enters anywhere. The verifier is exact-integer only; its T_5
   readouts are readouts, not estimates, and gate nothing analytic.
6  No orientation is selected anywhere: O_5 is the Canon's
   orientation-independent scalar, and the 2^omega(n) fiber count is a
   cardinality, not a choice. SPLIT-PRIME-RAPIDITY-CLASS [T] keeps only
   the unordered pair; nothing here refines it.
7  No canon file is edited; no probe is opened; no registry row is
   proposed, changed, or implied. Promotion, if ever, follows section
   11.
```

## 9. Verifier and pins

Exact-integer, stdlib-only, no floats, no analytic input; gates V01-V07
as listed in the file header. The analytic sections 5-7 are prose with
[T-lit] imports and are deliberately not gated.

```text
verifier:  C-GRH-QSQRT5-SPLIT-ORIENTATION-1_verifier.py
sha256:    5fda458115d4b26b5432bbbf937b59e480e1aa7b5d280cc726c7b71659d17d4e
bytes:     9308
stdout:    stdout_grh_qsqrt5_split_orientation_1.txt
sha256:    4b66eab905ec980db9ba7b37840eeb7d32bea1dabd4a1bd93726e737638ca9c3
bytes:     651
run:       LC_ALL=C PYTHONHASHSEED=0 TZ=UTC python3 <verifier>
platform:  Linux x86_64, CPython 3.11.15, exit 0, stderr empty
result:    VERIFY RESULT 7/7 ALL PASS
```

Exact readouts (from the pinned stdout; gated as integers by V06,
analytically a readout only, no claim):

```text
N        T_5(N)    isqrt(N)
10       1         3
100      -19       10
1000     -103      31
10000    -377      100
100000   -947      316
500000   -1869     707
```

## 10. Break attempts

```text
BR1  Drop a factor from the regrouped identity: the three breakers of
     gate V07 (drop the finite 5-block; drop L(2s,chi_5); drop
     zeta(4s)) each fire, at first differences 5, 4, 16. The identity
     has no slack.
BR2  Read the dictionary as progress on the bridge row: blocked; the
     row's own non-circularity fence excludes every conditional arrow
     of section 7 (see non-claim 3).
BR3  Weaken the target to RH for zeta alone: fails; the poles of O_5 on
     Re(s) > 1/2 include the zeros of L(s,chi_5), so pole-freeness of
     the channel is the FIELD hypothesis, not RH(zeta). The channel
     split of section 6 localizes exactly where each factor's zeros
     land.
BR4  Get square-root from the triangle inequality: closed by
     QS5-TRIANGLE-BOUNDARY; the l1 mass of the channel has abscissa 1.
BR5  Cancel a zeta_F zero against a G zero in the half-plane: G is
     nonvanishing on Re(s) > 1/2 (section 5), and on the closed line
     the only delicate factor is 1/L(2s,chi_5), covered by the
     classical L(1+it,chi_5) != 0. No cancellation is available.
```

## 11. Live falsifiers and promotion posture

```text
F-a  Any exact integer disagreement in gates V01-V05, or a breaker not
     firing at its frozen witness, fires against
     QS5-CHANNEL-COEFFICIENTS or QS5-DEDEKIND-REGROUP: the fired gate
     is archived, not moved.
F-b  An import audit showing the [T-lit] continuation or growth facts
     misquoted (functional-equation symmetry, Hardy, L(1+it) != 0, the
     GRH growth bound for 1/zeta_F) demotes the affected assertion to
     candidate-H until repaired; QS5-SUMMATORY-BRIDGE-DOWN in particular stands
     or falls with Titchmarsh sec. 14.25 transported.
F-c  A proof that zeta_F has a zero off the critical line would close
     the dictionary's GRH side negatively; the dictionary itself
     survives and reports it as a pole of O_5 off the line. Only a
     bookkeeping error in sections 5-6 falsifies the dictionary.
F-d  If the O_5-vs-Z[zeta_5] notation collision of section 1 causes a
     misquote anywhere downstream, the wording, not the mathematics,
     is repaired, and the repair is recorded.
```

Promotion posture: the L1 content (sections 3-4 and the verifier) could
be formalized as a probe under the two-architecture gate, at most
candidate-T going in. The analytic dictionary (sections 5-7) enters, if
ever, only through the release procedure with its [T-lit] imports named
in the preregistration; the bridge-down direction stays a literature
import unless independently proved. Nothing is requested now.
