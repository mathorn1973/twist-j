# P-POLE-HEIGHT-ODD-ORBIT-1

NON-CANONICAL / L1 analytical candidate and result-exposed prospective audit.
Owner: A. M. Thorn, pole-height-odd-orbit-20261104.
Reservation: https://github.com/mathorn1973/twist-j/issues/1897.
Base: ACTIVE Public Canon v109, main 650029c20408f1dd665983d72225d0d195fd030e.

## 1. Equation, question and exposed information

In O=Z[j], Phi_5(j)=0, put p=j^2,u=1-j,B=1-p. The only elementary move is

    C(x,y)=(x,y),                         x-y not in 2O;
    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2), otherwise.

C^5=I and C^-1=C^4. Division is exact on admission. For x in the power
basis (1,j,j^2,j^3),

    Q(x)=[5sum_i x_i^2-(sum_i x_i)^2]/2,
    H(x)=x conjugate(x).

Every move preserves the complete slot sum, sum H, sum Q and each slot's
residue modulo u. The focused question is exact reachability of the first
four target slots, with the auxiliary endpoint unrestricted:

    input(t)=(tB,-tB,u,u,0,2),
    target_first_four(t)=(u+tB,u-tB,0,0).

Audit t=-1,+1, then t=0. Reported review counts 1480, radius 25, no odd targets,
and 110, radius 14, distances 10+k for t=0 are exposed in PROVENANCE.md. They
are comparisons after completion, never enumeration stop counts. The
analytic N/R closure proof was also derived before this pin. This is a
prospective execution of a result-exposed verification, not a blind search.

## 2. Carrier, finiteness and analytical claim

Six ordered O slots and all fifteen pairs i<j are the complete finite
problem. A contact word may depend on the known input; ruling it out even
then rules out a common unknown-input word. No external permutation is
an extra edge in the census. The analytical alphabet theorem also allows
permutations and extra N-valued neutral helpers as specified in PROOF.md.

C^5=I alone does not establish finite global orbits. Here positive Q does:
Q(x)>=sum_i x_i^2/2 and the total is 28 for odd inputs, 18 for t=0. Every
power-basis coefficient is therefore in [-7,7]. This finite box is an audit
bound, not a replacement for exhaustive reachability traversal.

The two alphabets are

    N={0} union {j^a-j^b:a!=b},     |N|=21;
    R={j^a+j^b:a,b mod5},          |R|=15.

Check all ordered N*N, N*R and R*N pairs: 441+315+315=1071 pairs. Audit
closure, exact agreement of both arithmetic implementations, conservation,
residues and fifth-power/inverse identities. This finite local audit backs
the independently written analytical case proof; it is not an empirical
argument that arbitrary observed orbits have the same alphabet.

## 3. Accepted source and exhaustive traversal

Freeze exactly PREREG.md, README.md, PROVENANCE.md, SOURCES.tsv, PROOF.md and
verify.py before scientific execution. The accepted code specifies exact
iteration order, representation conversion and output serialization.

The primary route uses integer power-basis arithmetic and breadth-first
search of every elementary edge. It records shortest forward-contact
distances and predecessor certificates. The secondary route uses its own
five-coefficient quotient arithmetic and depth-first traversal of the four
nontrivial powers of each contact. It does not consult the first route's
reachable set while generating its own. Compare complete converted sets,
not only sizes or hashes.

For each completed orbit, audit every elementary edge for closure and
inverse behavior, invariants and distance inequalities. Every nonroot
state must have a predecessor one level lower. These predecessor paths
and all-edge inequalities certify the shortest distances. Report the full
sorted-state digest, distance histogram, radius, target count and target
phase distances. Report each neutral slot's set of Q values and the count
of states where reference slots 3 and 4 are simultaneously zero.

The necessary helper endpoints at a target are (1-p^k,1+p^k),k=0,...,4.
Check them explicitly rather than assuming the helper endpoint is reset.
For t=0 print and replay a shortest elementary word to each actual target;
verify full inverse recovery. Only k=0 restores helpers exactly.

Both traversals permit at most 100000 stored states per input. Discovering
a new 100001st state emits LIMIT and exits with status 2; it is not added.
That limit outcome or the process timeout is an incomplete audit, never a
completed orbit or a nonreachability claim. The code must preserve/report the limit outcome;
limits, arithmetic, inputs and source may not be changed after pinning.
No randomized tie, floating-point scientific condition or wall-clock
heuristic is used. No t=+/-2 or enlarged-helper census is included.

## 4. Systematics and falsifiers

Tolerances are zero. Reject a ring/parity discrepancy, malformed quotient
conversion, unequal complete route sets, missing edge, invalid inverse,
conservation/residue failure, invalid shortest-path certificate or false
claimed endpoint. A target in a completed odd orbit falsifies the proposed
no-go. Failure of the N/R local closure falsifies its analytical mechanism.
A completed count or radius differing from the supplied review is reported
as a mismatch with that review, not hidden by changing a threshold.

Separate source/run success, comparison with the supplied counts and the
scientific conclusion. No incomplete search is labelled exhaustive. A
passing finite audit does not claim minimum resources among all helpers,
a common seven-slot word, a physical charge or an automatic Canon status.
The broad N-valued-helper no-go rests on PROOF.md, not extrapolation from
three six-slot computations. Arbitrary neutral preparations are excluded.

## 5. Execution and immutable records

After a committed/pushed source pin and exact public byte readback, run
from a clean Linux checkout:

    python3 probes/P-POLE-HEIGHT-ODD-ORBIT-1/verify.py

Assertions enabled; LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. Remove inherited PYTHONOPTIMIZE, PYTHONIOENCODING,
PYTHONUNBUFFERED, TWISTJ_EVIDENCE_DIR. The process limit is 600 seconds.
Save raw stdout/stderr, exact exit status and neutral environment metadata.

For a genuine completed audit append only EXPECTED.txt, RUN.md, RESULT.md.
Do not invent a transcript before execution. Preserve a failed/abandoned
pin under POLICY.md, rather than repairing its sources in place. Open one
draft PR changing only this new probe. Required x86_64 and aarch64 jobs
must reproduce the same exact source/output bytes. Same-session review and
two arithmetic routes are not independent scientific acceptance.
