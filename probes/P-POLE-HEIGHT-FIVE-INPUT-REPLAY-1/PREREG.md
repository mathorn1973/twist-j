# Fixed common five-input loader replay

NON-CANONICAL / L1. P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1.
Public reservation: #1907. Owner: A. M. Thorn, replay session 2026-11-05.

## 1. Equation

For O=Z[j], Phi_5(j)=0, put p=j^2, u=1-j, B=1-j^2 and
X=1+j-2j^3. On six labelled slots, test the same fixed chronological word
W on all t in {-2,-1,0,1,2}:

    I_t=(tB,-tB,u,u,X,2)
    I_t.W = G_t=(u+tB,u-tB,0,0,X,2)
    G_t.W^(-1) = I_t.

Both helpers must return at their original addresses. The literal inverse
reverses the 322 labels and repeats each contact four times, giving 1288
contacts. Also test sigma(W), obtained by exchanging labels 1 and 2 and
sorting each pair. Its full contract is identical, with t exchanged with -t.

The total contact refuses, acting as identity, unless x-y belongs to 2O.
On admission it sends (x,y) to (s+p*d,s-p*d), where s=(x+y)/2 and
d=(x-y)/2. All other slots remain fixed. This parity decision is the only
state-dependent branch of the supplied contact law. The program never
selects a label or a word from t.

## 2. Code

The accepted verify.py uses only the Python standard library. One route
uses four integer coefficients modulo Phi_5 and multiplication by j^2;
the other uses five cyclic coefficients modulo the all-ones vector, in a
minimum-zero gauge with the common-parity admission test.
At every forward and inverse contact it compares the complete states and
admission decisions, and checks the ring sum, summed positive half-trace
Q and each labelled residue modulo u in both representations.

Q(a)=(5*sum(a_i^2)-(sum(a_i))^2)/2, with the fifth coefficient zero
in the power-basis representation. Each initial total is 10*t^2+33.
Accepted diagonal contacts count as admitted but not state-changing.
The verifier emits exact endpoints, admission/refusal/change counts and
hashes of the chronological traces. These counts are observations, not
adjustable success thresholds. There is no search, optimization, orbit
construction, floating point, random seed, network access or predecessor
code import.

## 3. Carrier and fixed input

The carrier is O^6, with the fifteen labels 12,13,14,15,16,23,24,25,26,
34,35,36,45,46,56. Each label denotes one attempted contact, read left to
right, including refusals. WORD.txt is the supplied candidate verbatim:
966 ASCII bytes, 322 labels, single spaces and one final LF, SHA-256
6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7.
The hash without the final LF is
d45bc66672eb16bee7c3a1bc9ec907f78ca5f6ed7250a3de9331d4e15ad653c0.

No macro bank is needed at runtime. The predecessor bank has 64 directed
macros; its byte identity is documented in PROVENANCE.md. Membership,
construction history and shortest macro decomposition are not hypotheses
of this primitive-word replay.

## 4. Systematics and prospective custody

This is a confirmation of an exposed candidate. The supplied round-five
review reports five-input success, inverse recovery and forward admission
counts 137,177,112,177,123 in increasing t order. It also exposes longer
words, searches and claimed lower bounds. These reports are not new blind
predictions and do not substitute for the new run.

The two code routes, complete six-slot equality, per-step invariants and
literal inverse address scalar, indexing, admission and helper-accounting
errors. Sigma is tested by an exact label transformation, not a supplied
second search. The transformations share the mathematical contact law;
agreement is not claimed to establish its physical realization.

Before the first formal run, commit and push PREREG.md, PROOF.md,
PROVENANCE.md, WORD.txt and verify.py, then read back every public file at
that immutable commit and compare Git blobs, SHA-256 and bytes. Static
inspection and syntax compilation are permitted before pinning; replay is
not. Record the source pin and all hashes in RUN.md. No scientific source
or input changes after the pin. Append only EXPECTED.txt, RUN.md and
RESULT.md. A changed scientific question needs a fresh identifier.

Use a clean source-pin checkout, Linux-compatible execution, assertions
enabled, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. The command from the repository root is:

    python3 probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/verify.py

The finite audit has two words, five inputs per word, 322 forward and
1288 inverse contacts per input, hence 16100 paired-representation steps.
The existing gate's 600-second timeout is operational only. There is no
adaptive resource expansion or retry to change a scientific outcome.

## 5. Failure threshold and disposition

Any coefficient mismatch at an endpoint, helper return, intermediate
representation comparison or inverse recovery, any admission disagreement,
any invariant failure, or failure of the sigma correspondence fires the
verification falsifier. The verifier prints a deterministic F diagnostic
and exits zero for a completed scientific falsification. Preserve its exact
stdout as EXPECTED.txt and explain the failed clause in RESULT.md. F here
rejects this certificate, not the existence of every possible common word.

Malformed or hash-mismatched input, exceptions and an operational timeout
are integrity/execution failures, not a mathematical no-go result. Preserve
the failure evidence and do not silently repair or rerun a frozen pin.

PASS means this fixed W and its sigma image meet the complete stated
finite contract. One architecture is at most candidate-C. Existing CI must
run the identical verifier on x86_64 and aarch64, exit zero with empty
stderr and byte-identical stdout against the one committed EXPECTED.txt.
Passing both satisfies the computation gate for the stated existence
witness. It does not itself update the Canon or any registry row.

## 6. Action layer and limits

Layer L1 only. The preparation, six addresses, contact law and finite
external schedule are supplied. Program length is a count of attempted
contacts, not physical time or action. There is no autonomous controller,
native-U compilation, physical preparation or Planck/alpha identification.
No shortest-word, 38-contact lower bound, 21-macro lower bound, orbit-size,
stabilizer-transitivity or stock-census conclusion is tested here.
The sealed predecessors and their inconclusive searches stay unchanged.
