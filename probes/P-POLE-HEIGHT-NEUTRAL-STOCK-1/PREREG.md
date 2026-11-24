# P-POLE-HEIGHT-NEUTRAL-STOCK-1

NON-CANONICAL / L1. Owner: A. M. Thorn, neutral-stock-witness-20261104.
Reservation: https://github.com/mathorn1973/twist-j/issues/1899.
Base: ACTIVE Canon v109, main650029c20408f1dd665983d72225d0d195fd030e.

## 1. Equation and exposed question

In O=Z[j], Phi_5(j)=0, let p=j^2, u=1-j, B=1-p, A=j-j^3,
J=1+p, D=1-j^3, X=1+j-2j^3. The only elementary move is

    C(x,y)=(x,y) if x-y is not in 2O;
    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2) otherwise.

C^5=I, C^-1=C^4. H(x)=x conjugate(x), Q(x)=Tr(H(x))/2.
In the four-coordinate power basis Q(x)=(5sum(x_i^2)-(sum x_i)^2)/2.
Complete slot sum, sum H, sum Q and each labeled residue modulo u are
invariants. The two literal chronological words, with one-based labels,
were supplied before authoring:

    W17: 57 27 27 23 23 23 47 47 47 67 67 67 17 17 37 37 37
    W20: 57 57 57 37 37 37 67 67 67 17 17 26 26 26 67 67 46 46 57 57

For each t in (-2,-1,0,1,2), run both on

    (tB,-tB,u,u,0,2,-2).

The desired first four outputs are (u+tB,u-tB,0,0). The exposed claims
are W17 success for t=+1 with helpers (-B,1+p,-2p), and W20 success for
t=+1 with helpers (0,2,-2). Assert precisely those claims. Print actual
endpoints, admission histories, first-four success and helper restoration
for every t. No other t is assumed to succeed. No shortest17/20 claim is
made by replaying these words.

A supplied review also reports a 27-contact catalytic X word but did not
supply it. Search only the known t=+1 six-slot source and full endpoint:

    source=(B,-B,u,u,X,2),
    target=(u+B,u-B,0,0,X,2).

The reported27 is exposed comparison data, not a success threshold. A
found word is replayed across all five t, without assuming universality.
The review's142 preparations, Q10 non-finding, 2u orbit11080 and rotated
stock34-contact construction are not repeated as censuses here.

## 2. Carrier, finite local audit and analytical statements

All values are integral cyclotomic tuples, with exact arithmetic. All
21 unordered slot pairs are admitted choices in seven slots, and all15
in six slots. Refusal is the identity and still counts as a requested
contact in replay; a shortest path never needs an identity edge.

Define N={0} union {j^a-j^b:a!=b}, R={j^a+j^b}. Audit all1071 ordered
N*N, N*R, R*N pairs and the same pairs shifted uniformly by u, each
through five powers. Check arithmetic agreement, closure, inverses,
translation covariance and all pair invariants. Separately examine all225
R*R pairs after one contact and report the actual count escaping
(N union R)^2; reported20 is comparison only.

Audit the analytical translated-target obstruction for both odd signs
and all five allowable helper phases, the21-stock account distribution,
Q2 unit classification, the exact C^3(2u,2) account15 counterexample,
JA=-u and C(u,X)=(2D,0). Enumerate the finite neutral Q<=20 ball by
integer five-vectors of zero sum in [-2,2]^5. Q=(5/2)sum a_i^2 and the
account bound proves this box complete. Classify Q=2 in the power basis
[-2,2]^4; Q>=sum x_i^2/2 proves that box complete too. All finite
counts back separately stated exact proofs, not larger orbit claims.

The broader no-go in PROOF.md is for exact restoration of every helper
whose translated value is in the indicated alphabet. The special2u
six-slot no-go additionally permits arbitrary helper endpoints by its
independent conservation classification. No arbitrary additional stock,
no global helper minimum and no physical-energy interpretation is added.

## 3. Accepted code and bounded search

Freeze exactly PREREG.md, README.md, PROVENANCE.md, PROOF.md, SOURCES.tsv
and verify.py. The accepted code fixes iteration order, canonical tuple
representations, predecessor choices and deterministic serialization.
The primary arithmetic reduces four-coordinate integer polynomials by
Phi_5. The second route uses five-coordinate quotient representatives
and cyclic rotation. It evaluates contacts independently of the primary
contact formula. Every witness contact and inverse is checked in both.
Search uses the primary representation with independently audited cached
pair transitions; it is not described as two independent searches.

The X search alternates complete forward and backward breadth-first
layers, at most20 on each side. Forward edges cost one C; reverse edges
are C^-1=C^4 and cost one reversed forward edge. Use all15 pairs in the
fixed order. Search states have total Q=43, so Q>=sum x_i^2/2
bounds every power-basis coordinate by9 in absolute value; the state
digest uses an injective fixed-width integer encoding within that bound.
Each side may store at most100000 distinct states, including
its root. Stop before adding a100001st state. No randomized tie or
wall-clock-dependent scientific decision is allowed.

After a complete layer first intersects the opposite stored ball, choose
by shortest distance sum and then deterministic state/word ordering as
implemented. Complete alternating balls and the absence of any earlier
intersection certify minimum forward-elementary length. A partial layer
stopped by a cap does not confer this certificate: any already-discovered
meeting witness is retained and replayed, but shortest is explicitly
unproved and the search remains LIMIT. Without a meeting, cap or depth
exhaustion yields LIMIT. Only a genuinely empty frontier without meeting
can establish disconnection of this fixed pair. Do not substitute an
exposed length, visited count or presumed orbit size for completion.

Print source/target, result classification, actual side sizes/depths,
edge counts, any recovered elementary word and its shortest-certificate
flag. Independently replay any recovered word, its complete inverse and
all five input instances. The positive-instance exact catalytic endpoint
is mandatory for a found witness; the other four outcomes are reported.
No search of a simultaneous five-input orbit occurs in this probe.

## 4. Systematics, failure threshold and status

All scientific tolerances are zero. Reject malformed conversions,
nonintegral admitted outputs, arithmetic disagreement, incorrect
invariants or residues, failed C^5/inverse identities, false witness
endpoints, invalid local closure or a false search certificate. A
verified target contradicting the stated translated-alphabet theorem
would falsify that theorem; do not discard it.

Reported counts and lengths are comparison fields only. A mismatch is
reported without moving a threshold. Assertion failure exits nonzero.
A bounded-search LIMIT is a scientifically valid incomplete outcome
printed in deterministic stdout and exits zero if every completed audit
passed. It is neither a no-go nor an abandoned runtime. An external
600-second timeout or interruption without completed stdout is preserved
as an incomplete execution, with no retry or silent source repair under
this identifier.

Analytical results are candidate-T / L1. A finite witness proves exactly
its displayed transition; computational search outcomes retain their
stated scope. Same-session authoring reviews are not independent
acceptance. Two-architecture agreement does not automatically promote
Canon status. Mathematical charge, stocked Q and chosen control words
are not an empirical particle or electromagnetic identification.

## 5. Prospective execution and immutable records

Before scientific execution, commit/push all six source files, record
the commit and each SHA-256/byte count, and read back the immutable public
bytes. Static syntax/security review may occur before pinning; no import,
search or scientific verifier execution may occur then. Execute once from
a clean Linux-compatible checkout of that pin at repository root:

    python3 probes/P-POLE-HEIGHT-NEUTRAL-STOCK-1/verify.py

Capture exact stdout/stderr outside the checkout, neutral environment
fields, exit code, bytes and hashes. After completion append only
EXPECTED.txt, RUN.md and RESULT.md, preserving all source bytes. The
required repository checker and x86_64/aarch64 CI replay the same frozen
source and compare exact scientific stdout. No architecture, path or
wall-clock value appears in scientific stdout.

No source modification, parameter retuning, repeat-until-success or
resumption of a sealed probe is allowed. A changed scientific question
requires a new identifier. No predecessor, Canon, registry, workflow,
policy or release edits are part of this probe.
