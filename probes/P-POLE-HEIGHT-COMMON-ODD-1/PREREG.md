# P-POLE-HEIGHT-COMMON-ODD-1

NON-CANONICAL / L1. Owner: A. M. Thorn, common-odd-loader-20261104.
Reservation: https://github.com/mathorn1973/twist-j/issues/1901.
Base: ACTIVE Canonv109, main650029c20408f1dd665983d72225d0d195fd030e.

## 1. Equation, carrier and supplied witness

In O=Z[j], Phi_5(j)=0, let p=j^2, u=1-j, B=1-p, X=1+j-2j^3.
The only elementary operation is the integral contact on one of fifteen
unordered pairs of six labeled slots:

    C(x,y)=(x,y) if x-y is not in 2O;
    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2) otherwise.

It satisfies C^5=I and C^-1=C^4. It preserves complete slot sum, full
Hermitian account sum H, trace account sum Q and each labeled residue
modulo u. H(x)=x conjugate(x), Q=Tr(H)/2, with exact power-basis formula
Q(x)=(5sum x_i^2-(sum x_i)^2)/2. All tolerances are zero.

For t in {-2,-1,0,1,2}, define

    I_t=(tB,-tB,u,u,X,2),
    G_t=(u+tB,u-tB,0,0,X,2).

Freeze the following supplied chronological word, in one-based labels:

    12 12 12 12 35 36 13 13 13 13 16 26 26 26 16 16 23 23 23 23
    26 26 26 16 13 13 13 13 36 34 45 45 45 45 46 46 12 12

Call it W38. Replay every input with independent four-coordinate and
five-coordinate quotient arithmetic. Audit every forward contact, all
invariants and the complete literal reversed C^4 inverse. Print actual
endpoints, admission histories and first-four/helper-return outcomes.
Assert the disclosed exact catalytic endpoints for t=-1,+1 only. Other
inputs are reported, not assumed to fail. Neither this replay nor the
bounded extension below proves the reported minimum38.

## 2. Finite audit of analytical stock exclusions

The neutral Q<=20 ball has a unique zero-sum integer five-coordinate
representation with Q=(5/2)sum a_i^2. Enumerate [-2,2]^5 with zero sum
and sum squares<=8; the account bound proves this box complete.

Let N={0} union {j^a-j^b:a!=b} and define

    T=N union ((u+N) minus {u+(j^2-j^4),u-(j^2-j^4)}).

PROOF.md proves unrestricted-helper failure for either odd input with
stock in T. A second criterion declares S isolated if its residue modulo
2O is outside

    {0,u,p^k B : k=0,...,4} modulo 2O.

Then S cannot contact the other five cells: the only nontrivial source
motion is the five-cycle in the first two cells. Audit all five C12 states
for each isolated stock and both odd signs, and every one of their fifteen
outgoing contact edges, including exact closure and absence of the target.
This tiny closure audit is not a reachability census of residual stocks.

Check exact sets, parity classes, exceptions, intersections and shell
counts. The exposed analytical expectations are |T|=32, |isolated|=102,
intersection14, union120, residual51. The excluded shell counts at
Q=0,5,10,15,20 are1,20,30,28,41. These expectations are proof audits,
not termination counts for a search. Preserve any contradiction.
The resulting minimum Qstock=15 is restricted to the declared six-slot
preparation, fixed helper2 and an odd input; the previous X witness
supplies attainment. No global helper-energy minimum is asserted.
The reported9 successful stocks and42 residual failures are not re-censused.

Before pinning, a further analytical isolation was derived for the four
stocks S=+/-2(j-j^3), +/-2(j^2-j^3). For each stock and both odd signs,
generate the product of five C12 phases and five C56 phases, audit all25
states and all15 outgoing edges, and require no first-four target. These
four stocks lie outside the preceding120 exclusions. The3000 exact edge
checks audit a new proof that only those two disjoint changing contacts
are possible. Report this additional set separately, union124 and
residual47; do not rewrite the preceding120 classification. The proof
and this extra audit were added before the prospective source pin and
before any scientific execution, not after inspecting search outcomes.

## 3. Returning-loop construction

After W38, the odd pair is g=(G_-1,G_+1). Build a deterministic breadth-first
excursion tree from g using all fifteen elementary contacts in fixed
lexicographic order, depth at most4 and at most2000 stored pair states.
Do not add a2001st state; report truncation if this bound prevents growth.
A finite tree is only a construction resource, never the complete odd orbit.

After building the tree, inspect every retained node and all fifteen edges,
including depth-four nodes and self-loops. For an edge a.C_e=b whose target
is also retained, form L=U_a C_e U_b^-1 using the stored root paths.
Use its compact inverse U_b C_e^4 U_a^-1. Adjacent equal contact powers
may be reduced modulo5, a global identity including refusal branches.
Discard only globally empty reduced words and formal word duplicates.
Do not identify words by their action on the odd orbit or the current
three even states. Such a kernel can carry the needed control.

Audit the exact return of both odd states for every candidate macro.
Paths have length<=4, so the displayed forward/inverse representations
have length<=21/24 before valid reductions. Reserve the twelve primitive
edges fixing g and their inverses. Select at most twenty additional
undirected loop representatives by the frozen two-sided exact Q-error
ranking, then word length and lexicographic tie rules in verify.py.
The total bank has at most32 undirected loops and64 directions.
Target-based ranking is a declared search heuristic, not completeness.
Specifically choose the lexicographically smaller reduced word/inverse as
an undirected representative L. Let eF be the exact error from r.L to h,
and eR the exact error from h.L^-1 to r. Rank the nonreserved candidates
by (min(eF,eR),eF+eR,len(L)+len(L^-1),L). Keep up to twenty. Each chosen
representative and inverse is a separate directed move.

## 4. Bounded search on the remaining three inputs

The starting even triple is r=(I_-2.W38,I_0.W38,I_2.W38), and its target is
h=(G_-2,G_0,G_2). Search from r and from h with the same inverse-closed
directed move bank, in the same macro-ID order. The backward side stores
its actual goal-to-meeting path; reverse its order and invert each macro
when joining it to the forward path. This traverses all reversed edges
without a separate inverse-ID iteration order. Use a deterministic beam of
width128, at most20 alternating rounds per side, with at most20000 retained
history states per side in FIFO order. Only retained beam candidates
enter that visited history; candidate-state deduplication chooses minimum
(native elementary length, macro-ID path). Rank retained candidates by
(exact Q error, native length, canonical state bytes, macro-ID path).
Check opposite-side meetings before own-side visited pruning. Store full
macro paths so a meeting before retention remains reconstructable.
Per-layer candidate pools are bounded by the
current beam width times the number of macro directions.

The exact heuristic error is the sum of Q of slot differences between
the current triple and the relevant opposite endpoint. It is nonnegative
and vanishes only at equality. It is not assumed monotone or an admissible
shortest-path lower bound. Selection and ties follow the frozen source;
no scientific decision depends on elapsed time or random sampling.

Count logical elementary even-case contacts, including cache hits: applying
a macro of length L to three cases costs3L. The search budget is20000000;
stop before applying an unaffordable complete macro. Tree construction,
finite theorem audits and bounded candidate scoring are separately limited
by their declared finite domains. Fixed caches are engineering aids and
cannot alter scientific counts, outputs or decisions.

Retain actual frontier/depth, pool/history, word and budget counts. A
found meeting yields one fixed expanded program W38 followed by the
reconstructed loop word. Audit it on all five original inputs using both
arithmetic routes, complete invariants and literal inverse recovery.
Require exact G_t endpoints for all five inputs. Also audit exact odd
restoration at every macro boundary; intermediate odd motion is allowed.
Print the actual elementary program and its length. No shortest-length
claim is made for this heuristic construction.

A state/work/depth/beam non-finding is BOUNDED_NOT_FOUND or LIMIT, never a
no-go. Even exhaustion of the generated subgroup would not establish that
it equals the full stabilizer. STABILIZER.md gives the exact full-group
criterion and explains the missing completeness implications.

## 5. Falsifiers, execution and immutable records

Freeze PREREG.md, README.md, PROVENANCE.md, PROOF.md, STABILIZER.md,
SOURCES.tsv and verify.py before scientific execution. The source contains
the complete accepted implementation and deterministic serialization.
Static syntax/security review is allowed before pinning; import or
scientific execution is not. Commit and push every source, record exact
SHA-256/byte counts, and read back immutable public contents and Git blobs.

Run once from a clean Linux-compatible checkout at repository root:

    python3 probes/P-POLE-HEIGHT-COMMON-ODD-1/verify.py

The external process timeout is600seconds. Capture actual stdout/stderr
outside the checkout and preserve every failure or interruption. Assertion
failure, arithmetic mismatch, broken closure, wrong witness endpoint,
invalid invariant or false returned-loop certificate exits nonzero.
A search limit with all completed audits passing is a valid incomplete
scientific result, printed deterministically and exiting zero. A timeout
without completed stdout is an incomplete execution, not a result to retry
silently. Do not change any source, cap, threshold or target after pinning.

Append only EXPECTED.txt, RUN.md and RESULT.md. RUN.md must contain the
repository-required flat pin/verifier/command/environment/exit/hash/byte
fields from the actual run. Required local checks and x86_64/aarch64 CI
reproduce the same frozen verifier and exact output. Source and result
custody are distinct from scientific status.

Analytical results are candidate-T / L1. A verified common word proves
only the specified finite construction. The review's census/minimum claims
remain attributed unless audited here. Same-session subagent reviews and
two arithmetic routes are not independent-session acceptance; architecture
agreement alone does not promote the Canon. No predecessor, normative
Canon, workflow, merge, release or physical action/alpha claim changes.
