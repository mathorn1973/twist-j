# Reviewed exact scalar decoder and observed-orbit capacity

Status: PASS at the frozen local scope; required two-architecture replay is
a separate acceptance gate. PUBLIC, L1, NON-CANONICAL until a separate fold.
Proof evidence: candidate-T with independent-agent mathematical review.
Finite evidence: candidate-C from the completed local x86_64 run; the required
workflow determines completion of the two-architecture computation gate.
No frozen mathematical falsifier fired. No source or threshold changed.

Owner: A. M. Thorn. Lock: #1283. Predecessor notes PR: #1282.
Immutable pin: 9b0f7cec517eb5cd722af98aa87b21af7ccad6a6.

## 1. Reviewed infinite-domain result [candidate-T]

On every nonzero alpha in Z[zeta_5] with N(alpha)<=941, the exact reading
D_25(alpha)=(S(alpha),S(J alpha),alpha mod25O) has the direct integer inverse
in decoder.py. It returns the original four coefficients, the unique oriented
strip representative and the integral J exponent. It rejects every reading
outside the exact image. The general sufficient criterion is m^4>16X.

The proof addresses termination even before scalar representability is known,
the strict/inclusive strip endpoints and the complete coefficient box [-8,8]^4.
The two traces are unbounded integers and refer to a pure J step. More pure-J
traces supply no new information because S_(n+2)=3*S_(n+1)-S_n.

## 2. Preserved review finding and corrected capacity [candidate-T]

The independent mathematical reviewer found a scope defect in a literal
native-label reading of the predecessor's phrase "maximum exactly K_m".
The arithmetic key capacity is K_m(X)=|D_m(B_X)|. The native retained alphabet
has only 3125 labels, so its usable capacity is min(3125,K_m(X)). The formal
proof and preregistration correct this before their public pin. The frozen
historical note is retained unchanged; the finding is not concealed.

The correction does not alter the decoder, the norm budget, the mod5 deficit
or the sufficiency of mod25. The inherited native chart is bijective onto all
3125 labels in every sheet n>=3. This establishes the premise needed to align
arbitrarily shifted codewords at sufficiently late sheets.

The observation is D_m alone, with no separately supplied sheet index n.
Injectivity is global across sheets. Supplying (n,D_m) changes the class:
distinct J offsets can then encode the finite labels already at norm one.
This is an essential observation boundary, not a physical no-go.

## 3. Complete finite evidence [candidate-C pending required replay]

| Quantity | Exact result |
| --- | ---: |
| B_940 | 3110 |
| B_941 | 3150 |
| Two-trace classes | 145 |
| Two-trace plus full mod5 keys | 2603 |
| Two-trace plus full mod25 keys | 3150 |
| Usable native labels with mod5 | 2603 |
| Usable native labels with mod25 | 3125 |
| Native-label shortfall with mod5 | 522 |
| Mod5 collision classes | 493 |
| Largest collision class | 10 |
| First collision norm | 55 |

The complete sorted strip digest agrees between the two implementations:
6a08d7de33b4cadb615f942b37202540dd6dea0f59f2412ffb822389c7c1cdab.
Their complete census JSON agrees byte for byte.

The exact witness is alpha=(0,1,1,-2), beta=(0,1,1,3), with
alpha*bar(alpha)=beta*bar(beta)=7+phi, traces (15,20), norm 55, and
beta-alpha=5*zeta^3. The identity is candidate-T; minimality consumes the
complete census. Equal readings normalize with the same J exponent, so
absence of smaller strip collisions also excludes smaller collisions anywhere
in the infinite norm-bounded domain.

Thus the first sufficient full 5^r-residue depth for 3125 labels is r=2 in
the frozen class. No minimality among other moduli, partial refinements,
extra time information, other observables or different norm budgets is claimed.

## 4. Execution and separation

The primary code was preserved byte for byte from the predecessor. It scanned
83521 coefficient vectors, performed 103950 ordinary and 40 large-exponent
round trips, and retained its invalid-input, endpoint and corruption controls.

The newly commissioned breaker was authored by a fresh-context agent from the
frozen preregistration only, before reading any implementation. It scanned
130321 vectors, performed 15750 round trips at exponents -37,-2,0,3,41, and
checked all 645 unordered collision-pair differences. It does not import the
decoder or primary audit. Its complete code was frozen and publicly stored
before comparison. Target answers were disclosed, so result blinding is not
claimed. The separate mathematical reviewer had implementation excerpts in
the inherited conversation and is not described as blinded.

The first combined run used Python 3.12.14 on Ubuntu 24.04.3 LTS, x86_64,
returned exit zero with empty stderr, and produced 1616 stdout bytes in
14 lines, SHA-256 d17ff82883dca610813187679221cb315b7636c79f9013062de691b5988d744d.
The inherited primary stdout retains its historical candidate/pending-review
wording; current proof-review disposition is in REVIEW.md and this result.
RUN.md records the exact pin, commands, custody and evidence limits.

## 5. Promotion boundary

Candidate statements for a later reviewed fold are the two-trace reconstruction,
the general norm/residue injectivity criterion, total exact image recognition,
and the corrected observed-orbit capacity theorem with its exact census.
The required Python 3.12 two-architecture replay must pass before that evidence
is considered complete. Passing it does not itself edit or activate a Canon.

No physical apparatus, preparation, occurrence law, persistence/reset, native
source completeness, SI scale, photon/P1, RH or higher-layer result is supplied.
All current Canon claims and all 25 H/O owners remain unchanged.
