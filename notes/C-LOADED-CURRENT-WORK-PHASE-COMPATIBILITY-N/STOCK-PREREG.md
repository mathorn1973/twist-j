# Fixed-word stock census preregistration

Status: **NON-CANONICAL / L1**. This is a prospective author-side exact
candidate-C audit. The user has already exposed an informal report of
121374 assertions and the stock counts below. That report and its original
checker are not reproduced by this new source. Exposure to its reported
answers is recorded explicitly; this audit is not independent acceptance
or a blinded prediction.

The earlier receiver, reduced-source, and full-field sources and run records
remain unchanged. The new standalone verify_stock_census.py imports none of
them and performs no full-field replay.

## 1. Pin, resources, and failure rule

Before the first scientific execution, publicly pin this file,
verify_stock_census.py, the accompanying analytical stock note, and a
SHA-256 manifest. Record the immutable commit and verifier hash.
Only source reading, AST syntax parsing, and hashing are allowed before pin.

After pin, run python3 verify_stock_census.py in this note directory,
using the Python standard library, exact integers, no network, and no
floating point. Each architecture has a fixed limit of 300 seconds wall
time and 1 GiB memory. Run the identical pinned bytes on x86_64 and aarch64.
Success requires exit zero, empty stderr, and byte-identical scientific
stdout. The first run supplies the exact output artifact.

An assertion failure, exception, resource limit, or architecture mismatch
fails this gate. Preserve and report the failure. Do not repair the source,
raise limits, alter the searched class, or change the expected counts under
the same pin. In particular a disagreement with an exposed external count
is a result to report, not permission to revise that count silently.

## 2. Exact stock class and complete bound

Use O=Z[j], Phi_5(j)=0, rho=j^2, four integer coefficients, and

\[
 Q(c)=\frac{5\sum_{i=0}^3c_i^2-(\sum_{i=0}^3c_i)^2}{2}.
\]

For a pair (p,q), the ordinary total contact C is identity if p-q is not
in 2O. Otherwise write p=s+t, q=s-t and send it to
(s+rho*t,s-rho*t). The fixed word is

\[
 W=[C(p,S),C(p,q)]^5,
\]

with the displayed order repeated five times. The five input states are
(j^b,-j^b,S), b=0,...,4. A stock is successful exactly when the five
terminal values Q(S_out) are pairwise distinct. This fixes the carrier,
input family, contact word, marked stock slot, and readout. There is no
restriction to a chosen parity class or normalized stock frame.

The first census includes every S in O with Q(S)<=32. Its exhaustive
coefficient box is [-5,5]^4. Indeed

\[
 G=(5I-\mathbf1\mathbf1^T)/2,\qquad
 G^{-1}=(2/5)(I+\mathbf1\mathbf1^T),
\]
\[
 c_i^2\le (G^{-1})_{ii}Q(c)=4Q(c)/5.
\]

For Q<=32, c_i^2<=128/5<36, hence every integer coefficient lies between
-5 and 5. Test all 14641 box members and filter only by Q<=32.

The separate second census tests all 625 stocks in [-2,2]^4, with no
quadratic-account cutoff. It must not be substituted for the first search.

A successful census with no stock below Q=22 and an explicit Q=22 witness
establishes the stock minimum only for this particular fixed-word,
five-input, terminal-Q-readout family. It is not a universal receiver cost,
slot-count bound, passive-detection bound, physical frame selection, or
coupling prediction.

## 3. Exposed expected findings and fixed witnesses

The externally reported hypotheses to check are:

- Among all stocks Q<=32, exactly 40 successes at each of Q=22,28,32,
  and no successes at other levels: 120 in total.
- In the full unrestricted coefficient box [-2,2]^4, exactly 32 successes.

The following witnesses were derived by hand before this audit executes:

| Stock coefficients | Q | Terminal Q for b=0,1,2,3,4 |
|---|---:|---|
| R=(3,4,2,0) | 32 | (32,17,2,7,27) |
| S=(2,-2,1,0) | 22 | (12,7,22,2,17) |
| T=(1,2,0,-2) | 22 | (22,12,2,7,17) |

T=1+2j-2j^3 is the normalized main example. Both Q=22 stocks remain
active supplied receiver stocks. The high pair plus stock costs 26;
adding an untouched -stock companion costs 48 and makes the sum zero.
The old two-pair encoded pointer plus stock costs 30, or 52 with that
neutralizing companion. These preparations retain pointer backreaction
and do not include a permanent archive or a physical calorimeter.

The program also selects the lexicographically smallest coefficient tuple
among all minimum-Q successful stocks. Its tuple and five readings are
not supplied in advance; the first pinned run computes and prints them.

## 4. Frozen finite inventory

1. Check the fifth-root relation, ten-contact word and forty-contact
   inverse, the three preparation accounts, and all three exposed response
   tables. For each Q=22 witness and every high digit check account 26,
   stock energy not exceeding 22, exact pointer backreaction, and literal
   inverse. Check the optional neutral companion is unchanged, has total
   account 48 and sum zero, and is included in the inverse. For each
   Q=22 witness and all 25 two-pair labels check account 30, unchanged low
   pair, complete inverse, and the neutral account 52 with its inverse.
2. Enumerate all 14641 stocks in [-5,5]^4, require nonnegative Q, retain
   Q<=32, and apply the literal receiver to all five prepared inputs.
   Every audited operation checks full Q and ring-sum conservation;
   every refused contact checks literal identity. Record every successful
   stock and its readings, and check its full inverse on all five inputs.
   Check the exposed count dictionary {22:40,28:40,32:40}, total 120,
   minimum Q=22, and inclusion of both explicit Q=22 witnesses.
3. Separately enumerate all 625 stocks in [-2,2]^4 without a Q cut.
   Check success by the identical literal word and readout, and compare
   the successful count with the exposed value 32. Compute its distribution
   by Q as an output, without an additional unexposed target distribution.
4. For each of the three frozen stocks and five high digits, check complete
   state covariance and invariant terminal Q under simultaneous multiplication
   of all three slots by each of the ten units +j^s and -j^s, s=0,...,4;
   check the inverse of every rotated prepared input.
   Separately rotate only the stock by j^s and check the relative-phase
   identity reading_(j^s stock)(b)=reading_stock(b-s).
   A negative stock alone is not called the same frame experiment.
5. Use all 125 raw occupied triples from (0,1,j,J,R), with J=1+j^2 and
   R the Q=32 stock. Check their complete inverses and, for every one
   of the ten units, complete-state covariance and inverse. The explicit
   all-refused input (1,j,0) must stay fixed.
6. Independently implement the existing native clock as whole-pair swaps
   (3,4),(2,3),(1,2),(0,1), followed by ordinary contact power
   3(m+1) mod5 on pair zero and 3m mod5 on each other pair.
   Start from the same delta neutral clock preparation, of total Q=4.
   For each of the three stocks, m=0,...,4, and actual tick counts n=1,13,
   check that the occupied known pair site n mod5 has amplitude
   j^(mn+floor(n/5)).
7. For every such actual clock endpoint and each stock-only phase frame
   j^s stock, s=0,...,4, attach the same receiver word at the known site.
   Check the relative-phase reading at exponent mn+floor(n/5)-s,
   complete account 4+Q(stock), literal receiver inverse, and the entire
   clock reversal with stock retained.
   For each of the ten simultaneous units, rotate the complete initial
   clock and stock, execute the actual ticks and receiver, and check
   complete-state covariance and identical final stock Q.
   The Q=22 one-tick tables must be those above. The thirteen-tick tables
   at unrotated stock are (22,12,2,7,17) for S and (2,22,7,12,17) for T.

These are prescribed discrete clock experiments. They do not compile the
earlier field-driven Gamma controller or identify physical duration.

## 5. Canonical result encoding and limits

Sort each success list by the pair (Q, coefficient tuple). Each record has
keys Q, stock, readings; stock and readings are integer arrays. Encode the
entire list using Python json.dumps with sort_keys=True and
separators=(",",":"); append one LF; hash its ASCII bytes with SHA-256.
Print the count and this digest for the complete bounded census and the
separate box census. This commits to every successful stock and every
readout without printing 120 records.

Also print the lexicographic minimum-Q record, both explicit Q=22 witnesses,
the preparation accounts, every stock-level count distribution, and the
actual relative-frame tables. A table has rows s=0,...,4 and columns
m=0,...,4; names distinguish Q32, Q22_S, Q22_T and ticks 1 or 13.
Scientific stdout additionally gives the exact assertion count and PASS,
with no timings, random data, machine names, paths, or floating values.

All ten simultaneous frame changes preserve Q because their multipliers
have u*ubar=1. This is a covariance result for a complete marked apparatus,
not a selection of one absolute root. The stock-only comparison deliberately
changes the reference relative to the source. The explicit stock savings
therefore refine a mathematical receiver construction; they do not supply
a natural stock, a physical phase law, a passive detector, or alpha.