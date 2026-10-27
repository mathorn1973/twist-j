# Complete binary classification: result

**NON-CANONICAL, L1. Analytical candidate-T over an exact finite audit; the
audit is candidate-C until byte identical on a second architecture.**

All three frozen programs passed on their first execution. No falsifier of
PREREG section 6 fired.

## The classification

A binary reader on R_n(u)=O/(u^n-1) exists exactly when:

```text
u = J        n not in {1, 5}
u = phi^-1   n not in {1, 2, 3, 4, 5, 7}
```

Every horizon up to 30 was decided by the rule predicted in PREREG section 2:

```text
u = J        L0 at 1; E1 at 2,3; CERT at 4; L1 at 5; CERT at 6; E1 at 7..30
u = phi^-1   L0 at 1,2; L1 at 3; L2 at 4; L1 at 5; CERT at 6; L1 at 7;
             CERT at 8; E1 at 9..30
```

For n>=31, PROOF.md Lemma 5 applies to every unit of modulus exponent one.

## Status and evidence

| Claim | Proposed status | Basis |
|---|---|---|
| Lemmas 1 to 5 | candidate-T | PROOF.md; the Lemma 5 integer premises are checked by verify.py |
| Classification for all n | candidate-T | Proof plus the exact audit for n<=30 |
| Exact finite audit n<=30, counts to 150 | candidate-C | Three programs, one session, one architecture (x86_64) |
| Physical sampling, Born occurrence, native U | not supplied | PREREG section 5 |

## What the audit established

**Counts.**

- F_n for n=1,...,150 and both units agree across three exact paths: the
  relative norm in Z[phi], the Bareiss determinant, and traces with Newton
  identities.
- All 300 COUNT rows are identical between verify.py and break.py.
- Every cycle count C_n is integral.

**Quotients.**

- Every R_n(u) for n<=12 and both units was enumerated through an audited
  Hermite lattice: 24 quotients, 332,848 states in total, the largest
  104,005.
- The fixed-point identity #Fix(T^d)=F_d held at every d|n.

**Exhaustive search for n<=8, using no lemma.** It found no reader at
exactly the excluded horizons. The minimal multiplicities at the positive
horizons were:

```text
u = J        c = 2, 3, 2, 2, 7, 2   at n = 2, 3, 4, 6, 7, 8
u = phi^-1   c = 3, 4               at n = 6, 8
```

**Realization on the actual quotient.** At every positive n<=12, a reader
was built from real orbits and every n-word was computed by iterating the
tick. All 2^n words appeared exactly c times. The largest support had
49,152 states.

**Certificates and tail.**

- The four frozen certificates passed every check and their abstract
  realization.
- The Lemma 5 inequalities hold at n=31; (B) fails at n=30, as frozen.
- P_n>=n*2^n holds for every 31<=n<=150 for both units. That is an audit,
  not a replacement for the proof.

**Agreement.** All 60 CLASS rows are identical between verify.py and
break.py.

## Exposure and independence, restated

The finite facts were seen before the contract (PREREG section 0). The
contract freezes them inside a complete all-n proof, with newly written
programs executed only after the pin.

Code distinctness is real: the two programs share no function, count by
different algebra, and decide by different methods (lemmas against
exhaustive search). Author independence and architecture independence are
absent. An aarch64 run of the same pin, or a review by another session,
would supply them.

## Reading, without a status

J=zeta*phi^-1 and phi^-1 have the same modulus, growth rate 2 log phi and
tail. Their finite exceptions differ: {1,5} against {1,2,3,4,5,7}. The
phase is invisible to the exponent and visible to finite arithmetic. It
changes the small-n counts, for example F_2=11 for J against F_2=1 for
phi^-1. As a result J has a binary reader at 2, 3, 4 and at every n>=6,
while phi^-1 has one only at 6 and at every n>=8.

## Boundaries

- No Canon, registry, frontier, probe, workflow or release changes.
- No physical selection of S or f, no sampler, no Born occurrence, no
  native-U bridge and no L1-to-L5/L6 gate.
- Other units of modulus exponent one are covered by the tail but not
  classified at finite n.
