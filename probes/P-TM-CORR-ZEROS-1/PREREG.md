# P-TM-CORR-ZEROS-1 preregistration

Date: 2026-08-30

Author of record: A. M. Thorn

```text
PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST /
NO PRIORITY CLAIM / ZERO FORMAL RUNS /
REMOTE PIN AND READBACK REQUIRED BEFORE EXECUTION
```

This file freezes one exact theorem-first public probe. It earns no scientific,
registry, Canon, dependency, gate, evidence, or release status. No formal
execution or import of `verify.py` is allowed until this file and the accepted
verifier have been committed together, pushed, hash-pinned on the public lock,
and read back byte for byte from the public remote. Syntax parsing and static
source review are allowed before the pin; executing any verifier statement is
not.

Public object lock: issue
[#694](https://github.com/mathorn1973/twist-j/issues/694), opened before this
prospective pin, accepted verifier, or formal execution.

## 0. Public identity, authority, and chronology

```text
probe:               P-TM-CORR-ZEROS-1
branch:              probe/P-TM-CORR-ZEROS-1
path:                probes/P-TM-CORR-ZEROS-1/
owner:               A. M. Thorn
candidate claim:     TM-CORR-ZEROS
proposed status:     T by the complete written proof; verifier is an audit
action layer:        L5 abstract drive-word stream only

STATE:               ACTIVE
CANON:               Public Canon v71
AUTHORITY:           mathorn1973/twist-j main
TAG:                 canon-v71
ACTIVATION_COMMIT:   39e61fbfe794b0d3d3ab2a28ba9f960c13f4fe7f
CONTENT_COMMIT:      a77d720433c19976f9ab663d023ec9364eac34eb
CANON_SHA256:        0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
CANON_BYTES:         369836
LOCK_BASE_COMMIT:    7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
```

The governing authority is public `main`. The theorem below defines its
sequence directly and consumes no existing scientific claim as a premise.
References to the public Thue--Morse drive are contextual cross-references,
not dependency edges and not a lift from another protocol layer.

The initial public pin contains exactly:

```text
PREREG.md
verify.py
```

It contains no `EXPECTED.txt`, `RUN.md`, or `RESULT.md`. Their absence records
zero formal runs rather than an incomplete result bundle.

## 1. Mandatory result-exposure and prior-art disclosure

The result and many finite checks were exposed before this public
preregistration. The declared non-canonical lineage is:

```text
notes/C-TM-CORR-ZEROS-1/
notes/canon/PROMO-C-TM-CORR-ZEROS-1.md
```

That lineage contains an earlier candidate preregistration, verifier, breaker,
single-architecture transcripts, hashes, ranges, and a positive proposed
result. Every one of those items is historical corroboration only. None is a
public pin, formal execution of this probe, blind prediction, two-architecture
gate, or evidence for the proposed row. The accepted `verify.py` here is a new
merged implementation with a new gate layout and no imported transcript.

The recursion and the complete family `5*2^a` are known in prior literature.
Coons, Mazáč, Pincus-Kazmar and Stout, *On the absolute value of the
autocorrelations of the Thue-Morse sequence*, arXiv:2511.06386, states the same
recursion and the zero family `5*2^a`. Baake and Coons, *Correlations of the
Thue-Morse sequence*, Indagationes Mathematicae 35 (2024), surveys the
recursion and its earlier lineage, including Mahler. Baake and Grimm,
*Aperiodic Order*, Vol. 1, Ch. 10.1, and Mauduit, Periodica Mathematica
Hungarica 43 (2001), remain unread in the declared review lineage. The
`7*2^a` family, exhaustiveness, and the parity proof have therefore not
received full human literature clearance against every identified source.
This probe makes **no novelty or priority claim for any clause or proof
step**. Its proposed status rests only on the self-contained proof below.
Unread literature does not enter a gate and cannot be turned into priority
wording after the pin.

The explicit general discrepancy bound in the candidate lineage is excluded.
The old magnitude, scaling, and single-`N` breaker outputs are also excluded.

## 2. Six frozen preregistration fields

### 2.1 Field 1: equation and theorem

For an integer `n >= 0`, let `s_2(n)` be its binary digit sum and define

```text
u_n = (-1)^s_2(n) in {-1,+1}.
```

For integers `k,N >= 0`, define the exact half-open finite sum

```text
S_k(N) = sum_(0 <= n < N) u_n u_(n+k).
```

The subscript `k` is the literal additive lag in `u_(n+k)`. It is not an
ordinal label and does not mean `k-1`. Define

```text
c(k) = lim_(N -> infinity) S_k(N)/N
```

only after existence has been proved below. The frozen theorem has exactly
four clauses.

#### T1. Exact dyadic finite-sum identities

For every `m,N >= 0`,

```text
S_(2m)(2N)   = 2 S_m(N),
S_(2m+1)(2N) = -(S_m(N) + S_(m+1)(N)).
```

These are exact identities at finite `N`, not asymptotic statements.

#### T2. Existence, uniqueness, recurrence, and coefficient ring

Every limit `c(k)` exists. The resulting sequence is the unique solution of

```text
c(0) = 1,
c(2m) = c(m),
c(2m+1) = -(c(m) + c(m+1))/2,
```

and for every `k >= 0`,

```text
3 c(k) is in Z[1/2] = {a/2^r : a in Z, r >= 0}.
```

#### T3. Complete zero classification

For every integer `k >= 1`,

```text
c(k) = 0  iff  oddpart(k) in {5,7}.
```

Equivalently, the positive zero set is exactly

```text
{5*2^a : a >= 0} union {7*2^a : a >= 0}.
```

The value `oddpart(0)` is not used; `c(0)=1`.

#### T4. Unique neighbouring coincidence

For every integer `m >= 1`,

```text
c(m) = c(m+1)  iff  m = 1.
```

#### Frozen universal parity lemma

Let `L(m)=m.bit_length()` for `m>=1`. For `m>=4`, define

```text
A_m = 3 * 2^(L(m)-3) * c(m),
B_m = 3 * 2^(L(m)-3) * c(m+1).
```

Then `A_m` and `B_m` are integers and `A_m+B_m` and `A_m-B_m` are odd.
They are scaled integer representatives, not necessarily reduced numerators.

No general bound on `|S_k(N)-c(k)N|` is part of T1--T4 or the parity lemma.

### 2.2 Field 2: accepted code

The accepted verifier is exactly `verify.py` in this directory. It is one new
file merging only the relevant obligations of the exposed candidate verifier
and breaker. It uses the Python 3.12 standard library, `int`, and
`fractions.Fraction`; it uses no floating point.

The verifier:

- reads no file, Canon artifact, transcript, environment value, clock, host
  property, or network resource;
- uses no subprocess, dynamic execution, third-party package, random module,
  fitted parameter, or mutable external input;
- writes deterministic stdout and no intentional stderr;
- has exit code `0` for `PROOF-SURVIVES`, `1` for integrity `STOP`, and `2`
  for a complete exact scientific falsifier;
- gives integrity `STOP` precedence over scientific falsification.

The accepted source has zero formal executions at this prospective pin. AST
parsing and source hashing are not executions. Import, `runpy`, helper calls,
or any invocation of its `main()` are executions and are forbidden pre-pin.

### 2.3 Field 3: carrier and audit data

The theorem carrier is the one-sided abstract sequence

```text
(u_n)_(n>=0) in {-1,+1}^N_0
```

defined directly by binary digit sum. All theorem variables range over
nonnegative integers, with the explicit positive restrictions in T3 and T4.
There is no experimental data, fixture, network input, measured constant, or
external file.

Finite audit ranges are frozen before execution:

```text
G1  0 <= m,N <= 300
G2  0 <= N <= 2^18 for the k=1 exact limit-base recurrences
G3  0 <= k <= 2^18+2; stated range checks through k=200000
G4  4 <= m <= 2^18
G5  1 <= k,m <= 200000
G6  matrix/recurrence overlap 0 <= k <= 20000;
    every odd q <= 4001 with every 0 <= a <= 64;
    fixed deep cases and 256 deterministic 512-bit cases
G7  complement: 0<=k<=64, 0<=n<1024;
    translated reversal: 0<=k<=64, 0<=N<=512;
    lag relabelling: 1<=label<=20000;
    {0,1} finite identity: 0<=k<=64, 1<=N<=512;
    weighted-limit nonvanishing: 1<=k<=200000
```

The deterministic deep-case seed is

```text
P-TM-CORR-ZEROS-1/G6/sha512/v1
```

It is a reproducibility seed, not randomness and not a source of evidence for
the universal quantifier.

### 2.4 Field 4: systematics and exclusions

1. **Half-open range.** `0 <= n < N` is load-bearing. A closed endpoint is a
   different finite identity.
2. **Lag index.** `k` is the actual offset in `u_(n+k)`. Relabelling the offset
   as `k-1` produces zero labels
   `{1+5*2^a,1+7*2^a : a>=0}` and is outside scope.
3. **Direction is not the issue.** A genuinely reversed product with its
   half-open window translated consistently is the same sum after a change of
   variable. With an unshifted truncation it differs only by finitely many
   boundary terms and has the same limit. No contrary "shift-direction"
   claim is made.
4. **Balanced alphabet.** The theorem uses `u_n in {-1,+1}`. For
   `t_n=(1-u_n)/2`, the `{0,1}`-weighted correlation is instead
   `d(k)=(1+c(k))/4` and has no positive zero.
5. **Normalization.** The mean is over positions `n` with denominator `N`.
   It is not a mean over lags, a Fourier-density claim, or a spectral measure.
6. **Fixed point.** Complementing every `u_n` leaves every product unchanged.
   Other shifts or labelled fixed points are not silently substituted.
7. **Existence is proved.** It is not inferred by assuming the recurrence for
   an already existing limit.
8. **No general discrepancy theorem.** The elementary `k=1` estimate used to
   prove existence is a proof lemma only. The old all-`k` logarithmic bound,
   its finite scan, and every proposed optimality statement are excluded.
9. **No finite threshold classification.** Values away from zero are not
   uniformly separated in `k`; zero-family finite sums need not vanish or be
   monotone; no single-`N` magnitude or scaling threshold is admitted.
10. **Prior exposure.** Earlier positive outputs do not make this blind work
    and are not copied into the pin or expected transcript.
11. **No priority.** The theorem is registered, if at all, on proof alone and
    carries no novelty statement.
12. **No TWIST-J lift.** The numerals `5` and `7` arise from base-two word
    arithmetic. Nothing uses or selects `J`, `zeta_5`, `F_5^6`, the physical
    prime, a decoder, an apparatus, an observable, or a measure.

For completeness, the `{0,1}` fence follows exactly from

```text
t_n t_(n+k)
 = (1-u_n-u_(n+k)+u_n u_(n+k))/4.
```

The prefix mean of `u` tends to zero because its even prefixes cancel and an
odd prefix has one residual sign. The shifted prefix has the same limit. The
recurrence gives `|c(k)|<=1/3` for `k>=1` by strong induction, hence
`1/6<=d(k)<=1/3`.

### 2.5 Field 5: failure threshold and decision semantics

There is no numerical tolerance. The scientific theorem package is
`FALSIFIED` by any complete exact witness to one of the following:

```text
F1  either T1 finite-sum identity fails at some exact (m,N);
F2  some c(k) fails to exist, the displayed recurrence or uniqueness fails,
    or 3c(k) is not in Z[1/2];
F3  some k>=1 has c(k)=0 with oddpart(k) not in {5,7}, or has c(k)!=0 with
    oddpart(k) in {5,7};
F4  for some m>=4, A_m or B_m is not integral, or A_m+B_m or A_m-B_m is even;
F5  c(m)=c(m+1) for some m!=1, or c(1)!=c(2).
```

The following are integrity `STOP`, not scientific falsification:

```text
I1  authority, public lock, pin commit, source hash, or public readback differs;
I2  a proof certificate, type, carrier, audit route, or source review is
    incomplete or malformed without a complete exact mathematical witness;
I3  two exact implementations disagree but no independently validated witness
    decides which implementation is wrong;
I4  execution raises, times out, reads undeclared input, writes stderr, or
    violates the deterministic exact-arithmetic contract;
I5  aarch64 and x86_64 stdout, verifier hash, or committed EXPECTED bytes differ.
```

Decision precedence is fixed:

```text
if any I1--I5 occurs:              STOP-INTEGRITY
else if any F1--F5 is exhibited:   FALSIFIED
else if all proof/audit gates pass: PROOF-SURVIVES
```

A changed convention, carrier, layer, or theorem is outside scope rather than
a falsifier. A fired falsifier is preserved and never repaired by moving a
threshold.

### 2.6 Field 6: action layer

```text
declared layer:  L5, abstract drive-word stream mathematics only
cross-layer:     none
gate row:        none opened by this probe
physical lift:   none
```

The probe neither constructs a stream from an L1 state nor maps a stream to an
L6 measure. It begins and ends with the explicitly defined abstract sequence.
The public Thue--Morse drive is a contextual identification only. Any physical
ownership, realization, decoder, spectral, or measure statement requires its
own separately named object and gate.

## 3. Complete written proof

### 3.1 Exact dyadic identities

Binary digit parity gives

```text
u_(2n)=u_n,                 u_(2n+1)=-u_n.
```

For the even lag, split the half-open sum at length `2N` into indices `2j`
and `2j+1`:

```text
u_(2j)u_(2j+2m)       = u_j u_(j+m),
u_(2j+1)u_(2j+1+2m)   = u_j u_(j+m).
```

Adding over `0<=j<N` gives `S_(2m)(2N)=2S_m(N)`.

For the odd lag,

```text
u_(2j)u_(2j+2m+1)       = -u_j u_(j+m),
u_(2j+1)u_(2j+2m+2)     = -u_j u_(j+m+1).
```

Adding gives
`S_(2m+1)(2N)=-(S_m(N)+S_(m+1)(N))`. This proves T1 for all
`m,N>=0`, including `N=0`.

### 3.2 Existence at lag one

Since `S_0(N)=N`, the `m=0` odd identity gives

```text
S_1(2N)=-N-S_1(N).
```

The one additional product at an odd length is

```text
u_(2N)u_(2N+1)=u_N(-u_N)=-1,
```

so

```text
S_1(2N+1)=-N-S_1(N)-1.
```

Put

```text
E(N)=S_1(N)+N/3.
```

Then exactly

```text
E(2N)=-E(N),
E(2N+1)=-E(N)-2/3.
```

Also `E(1)=-2/3`. If `L(N)` is the binary length of `N>=1`, induction along
the binary expansion gives

```text
|E(N)| <= (2/3)L(N).
```

Indeed an even child does not increase the absolute bound, while an odd child
increases it by at most `2/3`, exactly the increment from `L(N)` to
`L(2N+1)=L(N)+1`. Therefore `E(N)/N -> 0` and

```text
c(1)=-1/3.
```

This elementary estimate is only the base-limit lemma. It is not the excluded
general discrepancy claim.

### 3.3 Existence for every lag and the recurrence

Proceed by strong induction on `k`. The cases `k=0` and `k=1` are settled.

If `k=2m>=2`, then `m<k` and T1 gives

```text
S_k(2N)/(2N)=S_m(N)/N -> c(m).
```

If `k=2m+1>=3`, then `m,m+1<k` and T1 gives

```text
S_k(2N)/(2N)
 = -(S_m(N)/N + S_(m+1)(N)/N)/2
 -> -(c(m)+c(m+1))/2.
```

Appending one term changes `S_k(2N)` to `S_k(2N+1)` by one sign. Since every
normalized finite sum has absolute value at most one, the difference between
the odd-length and preceding even-length normalized means is at most
`2/(2N+1)`, which tends to zero. Thus the full sequence of normalized sums
converges and has the displayed recurrence. This proves existence without
assuming it.

### 3.4 Uniqueness and `3c(k) in Z[1/2]`

At `m=0`, the odd recurrence is self-referential:

```text
c(1)=-(c(0)+c(1))/2.
```

Its coefficient is nonzero and it forces

```text
3c(1)=-1.
```

For every `k>=2`, the right-hand indices in the appropriate recurrence are
strictly smaller than `k`; strong induction therefore gives uniqueness.

The same induction proves the coefficient-ring assertion. It holds at
`k=0,1`. An even step preserves `3c`, while an odd step replaces two elements
of `Z[1/2]` by minus one half of their sum. Hence
`3c(k) in Z[1/2]` for all `k>=0`.

### 3.5 Universal parity proof and the zero set

Direct recurrence evaluation gives

```text
c(1)=-1/3, c(2)=-1/3, c(3)=1/3, c(4)=-1/3,
c(5)=0,    c(6)=1/3,  c(7)=0,   c(8)=-1/3.
```

For `m>=4`, define `A_m,B_m` as in the parity lemma. They are integers at the
four base indices and

```text
(A_4,B_4)=(-1,0),
(A_5,B_5)=(0,1),
(A_6,B_6)=(1,0),
(A_7,B_7)=(0,-1).
```

Because `L(2m)=L(2m+1)=L(m)+1`, the recurrence gives the two exact integer
transfers

```text
(A_(2m),   B_(2m))   = (2A_m,       -(A_m+B_m)),
(A_(2m+1), B_(2m+1)) = (-(A_m+B_m), 2B_m).
```

The child coordinate sums are respectively `A_m-B_m` and `B_m-A_m`.
Modulo two both equal `A_m+B_m`. Every base sum is odd, and every `r>=8` has
the unique parent `floor(r/2)>=4`. Induction down this binary tree proves that
`A_m+B_m` is odd for every `m>=4`. Since `A_m-B_m` has the same parity, it is
odd as well. The transfers simultaneously prove integrality at every child.

For an odd lag `2m+1` with `m>=4`,

```text
A_(2m+1)=-(A_m+B_m)
```

is a nonzero scaled integer representative of `c(2m+1)`. It need not be the
reduced numerator. Direct inspection of `m=0,1,2,3` shows that the only odd
zeros are `2m+1=5,7`. Repeated use of `c(2m)=c(m)` reduces every positive lag
to its odd part. The remaining odd part `1` is nonzero because
`c(1)=-1/3`. This proves T3.

### 3.6 Unique neighbouring coincidence

For `m>=4`, the two coordinates `c(m)` and `c(m+1)` have the same nonzero
scale in `A_m,B_m`. Equality would force `A_m-B_m=0`, impossible because that
difference is odd. The direct small cases are

```text
c(1)=c(2)=-1/3,
c(2)=-1/3 != 1/3=c(3),
c(3)=1/3  != -1/3=c(4).
```

Thus `c(m)=c(m+1)` holds exactly at `m=1`, proving T4.

### 3.7 Scaled-representative wording

No proof step calls `A_m` or `B_m` a literal reduced numerator. For example,

```text
c(33)=1/8,
3*2^(L(33)-3)c(33)=3.
```

The needed implication is only that the nonzero scale makes the representative
zero exactly when the corresponding rational correlation is zero.

## 4. Frozen verifier gates

The verifier emits exactly seven pass/fail gate lines after a fixed header.
The universal theorem rests on section 3; finite ranges are audits.

### G1 `DYADIC-FINITE`

Construct the word directly and audit both T1 identities for every
`0<=m,N<=300`, including zero.

### G2 `LIMIT-BASE-CERTIFICATE`

Construct `S_1(N)` directly through `N=2^18`, audit both exact `E` recurrences,
the base value, and the coefficient identity used by the binary-length bound.
This gate contains no all-`k` discrepancy bound or extremum search.

### G3 `RECURRENCE-RING`

Build the exact rational recurrence through the required shared range. Audit
the two recurrences, `3c(k) in Z[1/2]`, and the exact `|c(k)|<=1/3` alphabet
fence for positive `k`.

### G4 `PARITY-CERTIFICATE`

Audit the four base pairs, both integer transfer matrices, exhaustive closure
of the two odd-sum parity states modulo two, and the scaled pairs through
`m=2^18`. The finite parity-state closure plus the written parent descent is
the universal proof certificate; the large range is redundant audit support.

### G5 `ZERO-NEIGHBOR`

Audit exact set equality for the zero classification on `1<=k<=200000` and
that the neighbouring coincidences on `1<=m<=200000` are exactly `[1]`.

### G6 `INDEPENDENT-MATRIX-DEEP`

Use the independently implemented pair vector

```text
v_m=(c(m),c(m+1))^T
```

and matrices

```text
M_0 = [[1,0],[-1/2,-1/2]],
M_1 = [[-1/2,-1/2],[0,1]].
```

Compare with the recurrence on `0<=k<=20000`; check fixed deep cases; check
every odd `q<=4001` at every dyadic shift `0<=a<=64`; and check 256
SHA-512-derived 512-bit cases under the frozen new seed. A route disagreement
without an independently validated witness is integrity STOP.

### G7 `CONVENTION-FIREWALL`

Audit exact complement invariance for `0<=k<=64`, `0<=n<1024`; exact
translated reversal for `0<=k<=64`, `0<=N<=512`; literal-lag versus `k-1`
zero labels for `1<=label<=20000`; the finite `{0,1}` product identity for
`0<=k<=64`, `1<=N<=512`; and nonvanishing of `(1+c(k))/4` for
`1<=k<=200000`.

The old candidate gates are disposed as follows:

```text
old V1                 -> G5
old V2                 -> G1
old V3                 -> excluded
old V4 valuation       -> replaced by G4 parity certificate
old V5, B2, B3, B3b    -> G5 and G6
old B4, B5             -> corrected G7
old B1, B1b            -> excluded: no finite magnitude/scaling threshold
old B6                 -> pre-pin static source audit
```

The pass transcript ends with

```text
SCIENTIFIC DECISION PROOF-SURVIVES
SUMMARY 7/7 PASS
```

It contains no timing, hostname, environment-dependent ordering, observed
minimum, stale hash, old output, or discrepancy statistic.

## 5. Corrected D1--D15 defect ledger

All fifteen defects are fixed by this pin; none is silently dropped.

```text
D1   The k=1 recurrence is self-referential. The proof explicitly solves
     3c(1)=-1 before strong induction.
D2   L(0) was undefined. Binary length is used only for positive integers,
     and scaled A_m,B_m only for m>=4.
D3   The old general bound used real log_2(N), incompatible with an exact
     rational gate. The entire general discrepancy claim and old V3 are
     excluded.
D4   Mere rationality hid the actual ring. T2 states and proves
     3c(k) in Z[1/2], without the false claim that every reduced denominator
     has odd part three.
D5   The half-open range was unfenced. It is now part of the equation and
     theorem scope.
D6   The earlier text misnamed a lag-index change as shift direction. The
     actual load-bearing convention is literal lag k versus labelled lag k-1;
     genuine translated reversal is equivalent.
D7   The balanced alphabet was unfenced. The {0,1} identity and its empty
     zero set are proved and audited as a distinct function.
D8   The valuation proof wrote equality where the ultrametric inequality alone
     was insufficient. The valuation route is removed entirely.
D9   The old root sat next to an induction it could not seed. The new parity
     induction begins exactly at m=4,5,6,7 and uses parent descent.
D10  Dyadic extension silently needed c(1)!=0. The proof explicitly uses
     c(1)=-1/3 to dispose of odd part one.
D11  The old all-k discrepancy bound lacked a valid proof route; the natural
     sup-norm induction yields only a sublinear power estimate. The bound is
     outside theorem and gate scope.
D12  "Literally the numerator" was false after rational reduction. A_m and
     B_m are called scaled integer representatives; c(33)=1/8 but A_33=3.
D13  Nonzero correlations are not uniformly bounded away from zero as k
     varies. No range-free separation or observed minimum is emitted.
D14  On a zero family, finite S_k(N) need not vanish or be monotone. No such
     finite signature is used as a theorem premise or threshold.
D15  Single-N magnitude thresholding cannot classify the zero set. Old B1 and
     B1b are not ported; the independent route uses exact recurrence/matrix
     equality and the universal proof.
```

## 6. Zero-run pin and post-pin procedure

Before the pin, only the following are allowed:

```text
git diff/check-style whitespace review
file inventory, byte count, and SHA-256
AST or syntax parsing without import or execution
static import/call/float/source audit
public collision, authority, branch, and issue readback
```

Forbidden before the pin:

```text
python verify.py
import verify
runpy or any helper invocation
tools/check_verifier.py
generation of EXPECTED.txt, RUN.md, RESULT.md, or scientific stdout
copying any earlier transcript into the public probe
```

The owner must commit and push `PREREG.md` and `verify.py` together, record the
full pin commit plus both file SHA-256 values and byte counts on issue #694,
then read both files back byte for byte from the public remote. Any difference
is STOP and requires a new identifier if the immutable pin has already been
spent.

Only after successful readback may the exact pinned verifier run. The first
completed formal run supplies one exact `EXPECTED.txt` and a neutral `RUN.md`.
The single-probe pull request then changes only
`probes/P-TM-CORR-ZEROS-1/`; required GitHub x86_64 and aarch64 jobs must replay
the same verifier with byte-identical stdout. A later Canon fold is separate,
may register only T1--T4 at L5, cites prior art without priority language, and
adds no discrepancy, `J`, `F_5^6`, decoder, physical, or measure claim.

No `P-TM-AUTOCORRELATION-SIGN-AUDIT-1` object may be opened in parallel.
