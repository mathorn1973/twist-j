# P-POLE-HEIGHT-CHARGED-LOADER-1

NON-CANONICAL / L1 / exposed analytical constraints and a prospective
bounded exact construction search.
Owner: A. M. Thorn, pole-height-charged-loader-20261104.
Reservation: https://github.com/mathorn1973/twist-j/issues/1895.
Base: ACTIVE Public Canon v109, main
650029c20408f1dd665983d72225d0d195fd030e.

## 1. Question and immutable source boundary

Find, if the frozen bounded search succeeds, one common finite contact
word that loads the five unknown inputs below. The input label t may
select neither a word nor an externally supplied branch. The contact's
own parity gate may act differently on different inputs.

The mathematical obstructions, helper classification and known-reference
controls were derived before execution. No unknown-input loading word is
supplied. This search is a deterministic heuristic, not an exhaustive
reachability or shortest-word proof. NOT_FOUND is a legitimate bounded
search outcome, not an impossibility theorem or a falsification of every
possible construction.

Before any scientific execution commit and push all six source files:
PREREG.md, README.md, PROVENANCE.md, SOURCES.tsv, PROOF.md and verify.py.
Read back their exact public bytes and record their hashes at the pin.
Only static inspection, syntax parsing and metadata operations precede
that pin. After a genuine completed run append only EXPECTED.txt, RUN.md
and RESULT.md. Source bytes, search limits and acceptance criteria are
immutable after pinning. Preserve a failed or abandoned pin under policy;
do not repair, rename or reuse this identifier.

## 2. Carrier and fixed inputs

Use O=Z[j], Phi_5(j)=0, p=j^2, u=1-j, B=1-p and

    Q(x)=[5 sum x_i^2-(sum x_i)^2]/2,
    H(x)=x conjugate(x),

in the ordered power basis (1,j,j^2,j^3). The only primitive operation is

    C(x,y)=(x,y) if x-y not in 2O;
    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2) otherwise.

Its inverse is C^4. Every division on admission must be exact.
For t=-2,-1,0,1,2 in that order, the complete six-slot initial state is

    (tB,-tB,u,u,0,2).

The first four target slots are (u+tB,u-tB,0,0). The complete necessary
helper list is (1-p^k,1+p^k), k=0,...,4, as proved in PROOF.md. A found
word may give different k for different t; every endpoint must be printed.
Only k=0 is exact helper restoration. No final auxiliary state is discarded.

The five complete input states are evolved together as one joint search
state. There are 5^5=3125 allowed joint goal states. The alphabet contains
C_ij^r for the fifteen fixed-label pairs 1<=i<j<=6 and r=1,2,3,4, ordered
lexicographically. There are no primitive swaps, resets, negative copies
created at runtime or state-conditioned external instructions. The supplied
negative copy and reference cells are explicit preparation inputs.

## 3. Frozen bounded search

The accepted code fixes a bidirectional deterministic beam search. The
forward root is the joint input; reverse roots are all 3125 allowed joint
goals in lexicographic phase order. Search alternates forward and reverse
layers through twenty layers in each direction. Retain at most 2000 states
per beam; retain at most 20000 visited joint states per direction using
the code's deterministic FIFO policy. A matched path has at most forty
macros. The finite visited capacity and beam pruning discard possibilities.

Forward priority measures exact summed Q error in the first four target
slots, with helper restoration as a secondary preference. Reverse priority
measures exact Q error to the complete joint input. The accepted code
specifies the exact score tuple, deterministic ties, beam admission,
visited-record timing and first-meeting selection. These implementation
choices are part of this frozen algorithm, not adjusted after a result.

Skip joint-identity moves and immediately repeated edges, whose adjacent
powers can be combined modulo five. These skips do not make the remaining
beam exhaustive. Candidate states are checked for a direct endpoint or
opposite-direction meeting as specified in the code before beam pruning.
A found common word stops the search. Otherwise report the bounded
non-finding after the frozen rounds. No random seed, empirical target,
wall-clock stopping heuristic or floating-point score is used.

All search arithmetic is exact. Pair-transform caching is bounded and may
change performance only; it cannot alter scientific state or search order.
The total candidate-expansion budget is below 4.8 million: one reverse
initial layer can examine at most 3125*60 moves, and the other thirty-nine
layers at most 2000*56 moves each. The first forward layer is smaller.
A counter in the code audits the implemented bounds. Its attempts count
budgets all four exponent choices for an edge before examining them; a
first meeting can therefore leave up to three budgeted choices unevaluated.

## 4. Mandatory construction audit

Before searching, check the declared cyclotomic arithmetic, input/goal
budgets, five helper phases and the known-reference catalytic word
(0,u,2)->(u,0,2) using C_13^3 followed by C_23^2. These are exposed controls,
not the requested unknown-input construction.

For a found word, expand every macro into elementary forward contacts.
Replay every complete six-slot B-family input using an elementary contact
implementation separate from the search macro transform. Check agreement
with the selected endpoint, full sum and H and Q at every contact, every
slot's residue modulo u, and complete inverse recovery. Audit fifth power
and inverse behavior on the actual encountered pairs. Report both macro
length and elementary forward length; an inverse costs four forward C
letters in this convention.

Check the complete helper endpoint against its unique phase k. For each
odd input check the necessary admitted charged-contact residues and length
bounds from PROOF.md: at least 10+k elementary forward contacts if k!=0,
and at least 15 if k=0. Verify that some input admission histories differ,
as required by the uniform-branch obstruction.

Also audit the A_t=t(j-j^3)=jB_t wrapper: prepend C_12^2, run the same found
word, append C_12^3. Require first four outputs (u+A_t,u-A_t,0,0), the same
helper phase, full conservation and inverse recovery for all five t.
This is a second fixed schedule for a known source family, not a claim
that one unchanged word loads all ten A/B preparations.

## 5. Preparation cost and reader interface

A Q-conserving loader can change the interaction account. For the complete
six-slot state v define

    I(v)=Q(v_2-v_3),       E(v)=sum_i Q(v_i)+I(v).

For the B-loader and its complete elementary trajectories define the common
initial loader stock by the frozen rule

    B_load=max(0, I(v_prefix)-I(v_initial))

over all prefixes and all five t. This is a derived property of the found
word, not a fitted acceptance threshold. During loading use
b_L=B_load+I(initial)-I(current), which must remain nonnegative. This bank
accounts for every interaction-energy excursion, in addition to the
preserved site account. It is separate from a reader bank initially 10.

At the loaded boundary, apply the actual C_12 once and debit only the
reader bank by the change of E. It must accept for all five inputs and
leave b_R=10-5t. The loaded bank itself ends loading at B_load+10t,
because I(initial)=5+5t^2+5t and I(loaded)=5+5t^2-5t. Thus B_load>=20 is
necessary. Positivity and Q conservation also give B_load<=101 for this
family, as proved in PROOF.md. All helper states remain part of E's site account.

Require conservation of E+b_L+b_R throughout loading and reading. Reverse
the funded reader step and then the complete loader, using the algebraic
inverse of each funded step and paying its endpoint change from the
original bank. These backward steps retrace the original affordable
boundaries. They do not claim affordability of four separately funded
forward C steps implementing each inverse on data alone. The four-letter
convention above prices forward contact words and the separate data
inverse audit. Require exact restoration of the six input slots and both
initial bank values. The A wrapper's state audit
is mandatory; no common B_load for an untested A funding schedule is implied.

The schedule choosing the paying bank is supplied. This does not construct
an autonomous switch, a new Hamiltonian, a persistent copied record or
free resetting of a bank. It is a fully stated discrete account extension.

## 6. Failure criteria and interpretation

All equalities have tolerance zero. A wrong ring operation, gate, sum/H/Q,
marked residue, helper classification, final target, macro/elementary
agreement, inverse, branch-diversity check, charged-contact bound, stock,
reader mark or full-bank recovery rejects the respective construction.
Preserve every discrepancy and actual process failure. Never call a
partial or unaffordable trajectory a successful loader.

A completed NOT_FOUND reports only this deterministic bounded search.
No success, optimality, charged-reference minimality, physical electric
charge, native-U implementation, action quantum or alpha value follows
from it. A successful word proves the declared finite preparation only.
The centered native piston chart, the O-slot encoding and any physical
carrier still need an explicit interface.

## 7. Execution and records

Run from a clean Linux checkout of the public pin:

    python3 probes/P-POLE-HEIGHT-CHARGED-LOADER-1/verify.py

Use the unchanged 600-second limit, assertions enabled, LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. Remove inherited
PYTHONOPTIMIZE, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR.
Save raw stdout/stderr without newline conversion.

Record the actual full pin, verifier hash, exact command, neutral platform,
architecture, Python, exit status, bytes, lines and SHA-256 values in RUN.md.
EXPECTED.txt is actual completed stdout, not a prewritten transcript.
RESULT.md separates any found finite construction, bounded non-finding,
analytical candidates and remaining physical obligations. Open one draft PR
changing only this probe directory. Required x86_64 and aarch64 checks
replay the same bytes. Same-session review is not independent acceptance.
