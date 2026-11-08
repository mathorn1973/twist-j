# Integer domain of the fixed 322-contact word

NON-CANONICAL / L1. P-POLE-HEIGHT-INTEGER-DOMAIN-1.
Public reservation: #1911. Owner: A. M. Thorn, integer-domain session 2026-11-05.

## 1. Equation

In O=Z[j], Phi_5(j)=0, put p=j^2, u=1-j, B=1-j^2 and X=1+j-2j^3.
Classify the exact success set of the single fixed chronological word W:

    S_W = {t in Z : I_t.W = G_t},
    I_t = (tB,-tB,u,u,X,2),
    G_t = (u+tB,u-tB,0,0,X,2).

All six labelled slots enter equality, including both helpers. A contact
on slots x,y refuses unless x-y belongs to 2O; refusal is identity.
Admission sends (x,y) to ((x+y+p*(x-y))/2,(x+y-p*(x-y))/2).
The word does not inspect t or change its schedule. The symbolic verifier
classifies the parity branches of this supplied total contact law.

The first mandatory output is the full affine terminal map on each branch
containing t=-2,-1,0,1,2. The second is a deterministic, bounded attempt to
classify every integer t. Completeness is earned only if its frontier empties.

## 2. Code

The accepted standard-library verify.py propagates affine states A+nD in
the power basis 1,j,j^2,j^3 on dyadic cylinders t=r+2^k*n. The independent
checker.py uses the integral basis 1,u,u^2,u^3, generic polynomial reduction
modulo u^4-5u^3+10u^2-10u+5, and a trace Gram form for Q. It does not import
the primary arithmetic. At every contact/refinement both routes compare
complete coefficient states and admission decisions. Initial, terminal and
frontier checks compare the affine sum, quadratic total Q and six labelled
residue polynomials. Terminal equality is solved by integer divisibility
in one route and rational equation elimination in the other.

For each known t0, begin with t=t0+n. Whenever the next contact depends on
n parity, retain n even, double the stride and continue. This is precisely
the complete branch containing n=0, not a finite sample around t0. Emit
its terminal coefficients in t=t0+2^k*n, canonical cylinder label and equality
classification. The coefficients retain the anchored coordinate.
Audit n=-1,0,1 by point replay. Separately replay t=-5,...,5 and their full
literal inverses: reverse W and repeat each contact four times.

The complete attempt uses depth-first refinement, visiting even child before
odd child. A nonuniform contact splits into two children at the same program
position. One logical node-contact step is charged when an unfinished node
is processed, including a split and each later child visit. No search for a
new word, branch coalescence, heuristic pruning or random sampling is used.
Terminal leaves are solved exactly. Replay all reported singleton solutions.

Fixed limits, selected before execution:

- 1,048,576 logical node-contact steps;
- 65,536 completed terminal leaves;
- 4,096 nonempty solution records.

Stop before exceeding any limit and retain the current unclassified node
on the exact frontier. Output all nonempty classified domains, terminal
certificate hashes, counts, and the complete remaining frontier. Verify the
classified leaves plus frontier form a disjoint cover of Z, by reversing
residue bits into adjacent dyadic intervals, and by an exact Kraft sum.
The 600-second execution timeout is operational, not a scientific threshold.
No adaptive expansion or outcome-changing retry of this pin is allowed.

## 3. Carrier and fixed input

The carrier is O^6; labels are the fifteen unordered pairs of six addresses.
WORD.txt is copied verbatim from the immutable source pin of #1908:
6793d8a2a87c6d39f8b06c262caa251c1306732f, directory
probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/.
It is 966 ASCII bytes, 322 labels, single spaces and a final LF; SHA-256
6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7.
The macro bank and private source attachment are not runtime dependencies.

## 4. Systematics and prospective custody

This extends an exposed candidate, not a blind word discovery. #1908 already
reports success for the five inputs. Its subsequent public review reports
misses at |t|=3,4,5 and supplies another implementation in the u basis.
Those reports were read before this pin. Our independent code routes are
independently implemented representations within this working session;
they are not an independent human review or a new source of physical laws.

Freeze PREREG.md, PROOF.md, PROVENANCE.md, WORD.txt, verify.py and checker.py
in one source commit, push it, and read back every public file, comparing
bytes, SHA-256 and Git blobs, before the first execution or import. Static
inspection and AST parsing are permitted before pinning. Afterward append
only EXPECTED.txt, RUN.md and RESULT.md; scientific sources stay unchanged.

Use a clean source-pin checkout in a Linux-compatible environment, assertions
enabled, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. From the repository root run:

    python3 probes/P-POLE-HEIGHT-INTEGER-DOMAIN-1/verify.py

Record the pin and source hashes, command, neutral environment, exit code,
exact stdout and stderr hashes and byte counts. Existing CI must reproduce
this output on x86_64 and aarch64 against the same EXPECTED.txt.

## 5. Failure threshold and disposition

Any representation/admission disagreement, nonintegral admitted coefficient,
invariant violation, invalid partition cover, inconsistent affine/point
replay, incorrect inverse or disagreement of terminal classifications fires
the verification falsifier. A completed scientific F diagnostic is preserved
with exit zero. Missing a target for an otherwise valid t is a classification
result, not a verification failure. Failure to recover one of the five known
successes rejects the inherited five-input certificate in this implementation.

COMPLETE means every integer belongs to a fully classified terminal domain.
PARTIAL means only the emitted classified domains are decided; the explicit
frontier remains open. Reaching a resource cap is not a mathematical no-go.
A successful run of either extent must pass the same exact integrity audits.
Malformed input, unexpected exceptions and timeout are operational/integrity failures,
not evidence against existence. Preserve them and do not silently repair a
frozen pin. One architecture supports at most candidate-C; identical stdout
on x86_64 and aarch64 satisfies the computation gate only for the reported
scope. The proof describes the method; no automatic Canon promotion follows.

## 6. Action layer and limits

L1 only. This classifies one supplied word, not all possible loaders. It does
not search the 64-macro bank or claim minimality, autonomous control, physical
preparation, a clock, a funded work reservoir or a common Hamiltonian lift.
322 is a count of attempted contacts, not time or action. Alpha stays open.
The separate conditional construction in #1910 is not a premise of this probe.
