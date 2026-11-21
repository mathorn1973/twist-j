# Prospective full-Schreier common-loader construction

NON-CANONICAL / L1. Identifier P-POLE-HEIGHT-FULL-SCHREIER-1.
Public reservation #1905. All scientific source and input files must be
committed, pushed and publicly read back before the first execution.

## Equation, carrier and full endpoint

O=Z[j], Phi_5(j)=0; p=j^2, u=1-j, B=1-p, X=1+j-2j^3.
The integral contact on labelled slots refuses when x-y is not in 2O;
otherwise C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2). Other slots do not move.
All15 unordered edges of six labelled slots are allowed. The exact target is

    I_t=(tB,-tB,u,u,X,2) -> G_t=(u+tB,u-tB,0,0,X,2)
    for every t in {-2,-1,0,1,2}, under one chronological word.

The admission branch belongs to this fixed law and may differ between
inputs; no input label selects a program. Helpers X and2 return exactly.
One inverse contact is C^4, four forward elementary contacts. Refused
contacts also count. Q(z)=Tr(z*zbar)/2 is positive definite, and total
Q=10t^2+33. Invariants are the whole sum, summed Hermitian account, summed
Q and each labelled residue modulo(1-j). Exact integer arithmetic only.

## Fixed input and exposed predecessor

BANK.json is unchanged from the predecessor:7943bytes, SHA-256
d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07.
It contains64directed macros and the expected odd targets/even residuals
and targets. W38 is replayed on all five original preparations; every
macro/inverse is audited on both odd endpoints before use.

PR1904 completed with a1556-state zero orbit,99584edges,65-contact bridge,
selected95undirected loops, and an inconclusive minus walk. These counts
are exposed inputs to design, not blind predictions. The sampled765/805
states do not establish full selected-subgroup orbits. No attribution of
the miss to one particular cutoff is assumed. PROVENANCE.md and SOURCES.tsv
bind the old source, output and exact reused arithmetic. The new program
copies declared scalar routines but imports or executes no predecessor.

## Accepted code and exact construction

verify.py is the accepted standard-library verifier; BANK.json is its
only scientific read fixture. Word expressions use a shared directed
acyclic graph of elementary macro leaves, concatenations and inverses.
Nodes are actual chronological words, not equivalence classes inferred
from sampled states. Their exact expanded forward-contact lengths define
logical work, independently of caching. The final witness is expanded
and independently replayed contact by contact.

First reproduce the complete zero orbit under all64bank generators,
with at most4096vertices. Use a weighted rooted tree at G_0 to construct
a bridge a from the post-W38 zero residual, with a 4096-contact bridge
cap. Complete graph closure may
exclude this zero bridge; any capped graph is inconclusive. Rooted paths
U_x and every generator edge x.m=y give

    F_(x,m)=U_x m U_y^(-1).

Retain the COMPLETE descriptor family, including self-loops and every
nonempty kernel word. No shortest4096 pool,256-contact cutoff or endpoint
diversity filter is applied. Structural word identities may be used only
when justified by actual concatenation/inversion or C^5 identities.

After applying a to the two remaining residuals, stream the full family
on the minus source s and target h. Both image maps start with the empty
word at their root. A common image s.F=h.G yields b=F G^(-1). Retain at
most eight bridges with distinct resulting plus sources r_plus.a.b.
The first representative R_y of each target image y is kept fixed.
Every further target word U with the same image contributes U R_y^(-1).
Keep every nonidentity structural collision loop and its inverse; matching
images are not a reason to discard kernel words. These star loops generate
all pairwise collisions among the processed target words (PROOF.md).

For each collision loop L, evaluate its image of G_2 and every current
plus source q. Image equality q.L=G_2.M supplies c=L M^(-1), and hence
W38 a b c. When a new minus bridge arrives, backfill ALL earlier collision
loops on its plus source so timing loses no processed candidate. The first
complete witness stops the search and enters the reserved final audit.
A successful prefix need not finish the remaining descriptor stream.

If the direct descriptor pass completes with no minus bridge, run fixed
bidirectional root-restarted walks on ALL full-family generators for at
most32768steps per side, restart depth8, feeding each encountered root
path into the same image/collision mechanism. Stop this fallback phase
once a minus bridge exists. If there is still no complete witness, run
at most32768steps per side, restart depth8, on ALL retained collision
loops and inverses for the plus inputs, cycling source restart blocks
across the at-most-eight bridge roots. The target side has one fixed root.
No short-word selection or endpoint fingerprint reduction occurs.

Deterministic ordering is part of the accepted algorithm. The weighted
zero tree uses (distance, canonical 24-byte state key) heap order and the
fixture's macro order; equal-distance predecessors keep the first arrival.
Descriptors are ordered by canonical zero-state key and fixture macro ID.
The identity is already in both root maps. Identical structural DAG IDs
skip repeated direct root applications, but equal endpoint images do not.
All image representatives remain the first encountered word. Keep the
first eight bridges with distinct plus-root states. Collision directions
are appended as L then L^(-1), evaluated on the plus target first and then
source roots by index. A new root's identity image is considered before
backfilling every earlier collision direction.

Fallback banks preserve the first structural-ID encounter, considering
program then inverse. Source and target steps alternate. The plus-source
restart root is (step//8) modulo the current root count. The xorshift64*
shifts are 12,25,27 and multiplier 2685821657736338717; seeds are
0xD1B54A32D192ED03 (minus) and 0x94D049BB133111EB (plus), with 64-bit
masking. If the selected program is the immediately previous inverse,
advance its index once modulo the bank size. No other stochastic input
or adaptive change is allowed.

The global search allowance is300000000logical forward elementary
contacts. Cost is charged before each whole word application, including
cache hits. Exhaustion is INCONCLUSIVE. The final expanded word cap is
100000 contacts. The sum of the four piece lengths W38,a,b,c must fit
before final cross-boundary DAG reductions; this conservative check can
skip a reducible overlong candidate and is not a shortest-word test.
Mandatory fixture audits, the explicit W38.a dual-arithmetic and literal
inverse replay for t=-1,0,+1, and final five-input forward/inverse audits
are reserved outside the exploratory work allowance. The program
must report which direct/fallback phases actually completed.

## Systematics, falsifiers and dispositions

Two exact scalar representations audit parity admission, p rotation,
sums, Hermitian accounts, Q, marked residues and C^5. Reused primary
arithmetic is not represented as a new independent implementation.
Cache and DAG optimizations may not alter word meaning or cost accounting.
Fixture hashes, macro inverse identities and all promised return states
must match. A found word must reach every complete G_t and recover every
I_t under its literal inverse. Any arithmetic, invariant, fixture, closure
or promised-return mismatch is a fired verification failure. Preserve it;
never retune or repair the frozen source.

A complete family of stabilizer generators does not mean that the image
of a root under one generator is its full orbit. Even processing every
star loop once does not classify arbitrary products of those loops.
Only an actually complete zero-orbit exclusion may yield a K0 no-go here.
Every other empty image intersection, exhausted fallback, bridge limit or
work/word/state cap is INCONCLUSIVE. No minimum length is claimed. The
bridge limit8 can change the outcome of the incomplete final search; the
coset theorem for a FULL subsequent stabilizer is not used to hide this.

The process timeout is600seconds, matching the existing repository gate.
It is operational, not a scientific negative threshold. The first run uses
a clean public source-pin checkout on Linux-compatible execution with
assertions enabled, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and no
bytecode writes. No source import or scientific run occurred before pin.

## Custody and scope

Record the full source pin and all source/fixture hashes, then verify
immutable public contents before execution. Append only EXPECTED.txt,
RUN.md and RESULT.md after the run; preserve exact stdout/stderr, exit code
and neutral environment metadata. Existing x86_64 and aarch64 CI must
reproduce the same exact stdout. No source, seed or bound changes after pin.

The prior seven-stock audit remains separate and unchanged. No complete
171-stock census or minimum38 reproduction is included. The optional
orbit-size lemma is explicitly conditional on the supplied external even
orbit count; it is not a premise used to accept a positive construction.
No Canon promotion, native source bridge, funded schedule, autonomous
controller, physical time, Planck action or alpha identification follows.
