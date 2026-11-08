# Complete integer domain of the 322-contact word

Status: NON-CANONICAL / L1. COMPLETE exact classification; local candidate-C.
The two-architecture computation gate is satisfied only when the existing
x86_64 and aarch64 jobs reproduce this identical output. No Canon promotion.

For the fixed W in WORD.txt, the full six-slot contract holds exactly when

    I_t.W = G_t  if and only if  t in {-2,-1,0,1,2}.

This classifies all integers, not merely a finite tested interval. W is
therefore a common five-input loader and is not a loader for arbitrary
integer t. The result says nothing against a different word or construction.

## Complete symbolic partition

The deterministic traversal finished after 9,823 logical node-contact steps,
54 splits and 55 terminal leaves. Its maximum exponent is 14 and maximum
pending stack is 10. All resource caps remained untouched. The exact
reverse-bit interval audit and independent Kraft sum establish a disjoint
cover of Z with classified-domain measure 1 and remaining measure 0.
The unresolved frontier is empty.

Exactly five leaves have a single successful integer. No leaf succeeds on
its whole congruence class. The other 50 leaves are empty: 24 have a nonzero
constant equation, 24 have inconsistent affine roots, and two have a common
nonintegral root. All 24 coefficient equations include both helpers.

Terminal certificate SHA-256:
54aec1c9ab5976bd37c84fc17cb6f3f8f21d478982fee863c5d4a0eab8a68878.
Partition certificate SHA-256:
586997912ae0c06a5ec88ff3ae5a2b83e823763271db33e5efe85c5126786754.
The public verifier reconstructs every affine leaf and hashes its full
terminal record; the five nonempty records are emitted explicitly.

## Five compulsory branches

The branch containing each known t0 has the following exact domain and
success set. The trace is shared throughout that congruence class; the
endpoint remains affine and is generally different.

| t0 | Complete admission-trace cylinder | Successful t in that cylinder |
| ---: | --- | --- |
| -2 | t = -2 mod 512 | -2 only |
| -1 | t = -1 mod 512 | -1 only |
| 0 | t = 0 mod 512 | 0 only |
| 1 | t = 1 mod 512 | 1 only |
| 2 | t = 2 mod 1024 | 2 only |

Each emitted anchored map has the form G_t0+n*D in the coordinate
t=t0+2^k*n. Its error is n*(D-2^k*V), with nonzero slope, so n=0 is its only
solution. EXPECTED.txt contains every coefficient, split position and trace
hash. Canonical residue r labels the cylinder; the coefficients retain the
explicitly printed anchored coordinate.

## Exact audits

87,030 checks passed with zero fired verification falsifiers. The primary
power-basis arithmetic and independent u-basis polynomial arithmetic agree
at every transition. They also agree on invariant polynomials and terminal
classifications, using integer divisibility and rational elimination.
The 21 distinct scalar audits include t=-5,...,5 and the two adjacent points
on each anchored cylinder. All 11 point cases in -5,...,5 pass the complete
1,288-contact inverse, including those that miss the forward target.
The previously exposed misses at |t|=3,4,5 are confirmed.

The scalar audits supplement the symbolic proof and complete partition;
they are not the reason the result extends over Z. The first clean local
run exited zero with empty stderr; stdout is 8,944 bytes and 29 LF lines,
SHA-256 092b93a5ae235c631dd72b8adb51b02d7b1e91cf78a86f53ce307672a5eac84d.
Sources and input were publicly frozen before execution; see RUN.md.

## Limits

The word is unchanged and no new word was searched. This result does not
establish shortest length, macro-bank reachability for other t, or a no-go
for an arbitrary-integer loader. It neither supplies physical preparation
nor compiles a clock, work reservoir or Hamiltonian controller. A count of
322 attempted contacts is not a time or action normalization. Alpha remains
open. The conditional construction in #1910 has a separate scope.
