# P-RECORD-QUOTIENT-CALCULUS-1 preregistration

Date: 2026-08-22

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific
result is earned by this file. The accepted verify.py may be parsed, compiled
and inspected statically, but it is not imported or executed before this file
and verify.py are committed together, pushed, and read back byte for byte from
the public remote.

Public claim lock: issue 524, opened before this file was committed.

## Authority

~~~text
STATE:          ACTIVE
CANON:          Public Canon v60
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v60
CONTENT_COMMIT: 18b21bdaf2c2236c9444b120900277ccfb63e050
CANON_SHA256:   9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0
CANON_BYTES:    329876
BASE_COMMIT:    9b73d772ce9b8c9479d80e3b10f673b1f5af78f1
LAYER:          L1 exact arithmetic only
~~~

The authority gate used a clean clone of public main, not an attachment or a
rendered page. canon/SHA256SUMS is five of five OK. The recomputed SHA-256 and
byte count of canon/CANON.md equal the declared fields. Both canon-v60 and the
content commit are ancestors of main. BASE_COMMIT is the head of main at lock
time and is the parent of the pin commit.

This probe changes exactly probes/P-RECORD-QUOTIENT-CALCULUS-1/. Canon,
registry, frontier, evidence, release, workflow and policy files are excluded.

## Collision search

Before drafting, the public open and closed issues and pull requests, remote
branches, probes/ and canon/REGISTRY.tsv were searched for both
P-RECORD-QUOTIENT-CALCULUS-1 and RECORD-QUOTIENT-CALCULUS. No issue, branch,
probe path or registry claim with either exact name existed at lock time.

Adjacent objects are recorded here so the boundary cannot be lost.

1. PR 521, notes/record-crt-idempotent-and-v60-manifest-draft, is open,
   unmerged and non-canonical. Its owner ruling names this probe as a later,
   separate formal step. Its rev2 derivation, runs and mutation-harness report
   exposed the result and informed the design, but they are discovery context
   only. They create no claim lock, no probe, no status and no formal evidence.
   Repository CI does not inspect the scientific content of notes/.
2. CARRY-PENTAD [T], J-BINARY-NORM-DESCENT [T] and
   CARRY-QUADRATIC-SYMMETRY [T] are adjacent public L1 rows. Their cyclotomic
   carrier context and guards are imported, not re-derived or moved. No prime,
   cycle, exponent or physical reading is selected here.
3. The existing QDD record probes concern observable quotient covariance,
   conditioning, ports or higher-layer event records. This probe concerns only
   ideal arithmetic of finite R-algebras and performs no layer lift.
4. Issue 503 is the open Canon cleanup lock over carry and J-binary material.
   It blocks overlapping Canon writes, not this one-directory probe. A later
   registry or Canon fold is separate and must be locked and sequenced through
   issue 503, not around it.

## Result exposure and dead-run disclosure

RESULT-EXPOSED, not blind.

The claims R1-R6 were derived and exercised in the non-canonical PR 521 lane.
The first published incubation verifier was defective: it contained a literal
True, two construction-true conditions, a wrong gate count and stale byte
metadata, and it mixed an L1 claim with apparatus language. A successor draft
repeated the same defect class and was discarded. The published rev2 then
narrowed the scope to R1-R6 and reported 31 passing gates plus a mutation audit.

None of those runs is evidence for this probe. The accepted verify.py here is
byte-new and adapted into formal repository output form from the exposed rev2
implementation. The mathematical routes and most implementation logic are
therefore inherited, not independent. Its exact accepted bytes have never been
imported or executed at the moment of this pin. Static reading, parsing and
syntax compilation are allowed before the pin. The formal protection is the
public exact-byte pin and readback before one execution, not a claim of blind
discovery or novel implementation.

The mutation harness remains outside this probe. Its report helped expose
shared-route defects, but a pre-pin static review also found that its
timeout/exception and non-unique-snippet accounting do not by themselves
enforce its advertised contract. It is neither one of the five formal evidence
files nor support for theorem status. The theorem ceiling below rests on the
written proof; the verifier is a finite audit of that proof.

## Field 1: equation and written proof

Let R = Z[zeta_5], a Dedekind domain, lambda = 1 - zeta_5, and let I be a
nonzero proper ideal. Unique factorization of nonzero ideals gives

~~~text
I = product over P in Supp(I) of P^(e_P),  with every e_P >= 1.
~~~

Write rad(I) for the ideal radical and

~~~text
n_I = rad(I)/I inside R/I,    n_I^0 = R/I.
~~~

The convention n_I^0 = R/I is load-bearing: Loewy layer k is
n_I^k/n_I^(k+1) for k >= 0, so layer zero is R/rad(I).

### R1: canonical Booleanization

Distinct prime powers in the factorization of I are pairwise comaximal, hence
CRT gives a canonical product of R-algebras

~~~text
R/I  =  product over P in Supp(I) of R/P^(e_P).
~~~

Every factor is local. If e is an idempotent in a commutative local ring, then
e(1-e)=0 and one of e or 1-e is a unit; multiplying by that inverse gives
e=0 or e=1. Thus each local component contributes exactly a zero-or-one choice.

The map

~~~text
e  |->  {P in Supp(I) : the P-component of e is 1}
~~~

is therefore a canonical Boolean-algebra isomorphism

~~~text
Idem(R/I)  =  P(Supp(I)).
~~~

Meet, join and complement are carried by ef, e+f-ef and 1-e. The atoms are
labelled by the prime ideals themselves. No enumeration or order of the primes
is part of the statement.

### R2: radical invariance

Reduction in each component,

~~~text
R/P^(e_P)  ->  R/P,
~~~

maps the only two idempotents 0 and 1 bijectively to the only two idempotents
of the residue field. Taking products shows that

~~~text
Idem(R/I)  ->  Idem(R/rad(I))
~~~

is a bijection and a Boolean-algebra isomorphism. Exponents are invisible to
the idempotent layer.

### R3: exact Loewy profile

In the P-component A_P = R/P^(e_P), the nilradical is P/P^(e_P). For k < e_P,

~~~text
(P/P^(e_P))^k / (P/P^(e_P))^(k+1)
       = P^k/P^(k+1),
~~~

and that additive quotient has order N(P). For k >= e_P the component is zero.
Products over the CRT factors therefore give, for every k >= 0,

~~~text
|n_I^k/n_I^(k+1)| = product {N(P) : e_P > k}.
~~~

The last nonzero layer has k = max_P(e_P)-1, so

~~~text
L(R/I) = min {L : n_I^L = 0} = max_P e_P.
~~~

Only orders are claimed. No module decomposition is inferred from a
cardinality comparison.

### R4: reductions are forced

A unital R-algebra map f:R/I -> R/J must commute with the structural maps from
R. Consequently

~~~text
f(r+I) = r+J
~~~

for every r in R. This formula is well-defined exactly when every element of I
vanishes modulo J, namely exactly when I is contained in J. It is then the
canonical projection and is unique. Hence

~~~text
Hom_(R-alg)(R/I,R/J)
  = {canonical projection}  if I is contained in J,
  = empty                   otherwise.
~~~

The category is thin. Unitality is load-bearing. As a control, an R-linear map
is determined by t=f(1); it is well-defined when I*t is contained in J and is
multiplicative exactly when t is idempotent. Requiring t=1 leaves precisely the
unital map classified above.

### R5: irreversibility

If I is strictly contained in J, the projection R/I -> R/J exists. A unital
R-algebra section R/J -> R/I would, by R4, require J to be contained in I.
Together the two inclusions would force I=J, a contradiction. Thus a strict
quotient has no unital R-algebra section.

### R6: fixed Boolean support, unbounded depth

The ideal (lambda) is the unique prime over 5, with residue field F_5, and (2)
is inert in R, with residue field F_16. They are coprime. For every L >= 1 set

~~~text
I_L = (lambda)^L (2).
~~~

Then Supp(I_L) = {(lambda),(2)} and rad(I_L) = (lambda)(2), independently of
L. CRT gives

~~~text
R/rad(I_L) = F_5 x F_16.
~~~

R1 gives four idempotents for every L. R3 gives

~~~text
L(R/I_L) = max(L,1) = L.
~~~

The support, radical, reduced record and Boolean algebra are constant while
the filtration length is unbounded. Therefore the Boolean skeleton and the
reduced record cannot determine filtration depth.

### Frozen maximum statement

The six clauses above are one theorem packet:

~~~text
RECORD-QUOTIENT-CALCULUS  [T]  L1, exactly R1-R6.
~~~

This is a maximum later row, not a status created by the probe directory. The
T ceiling rests on the written universal proof. Any conclusion supported only
by the finite carrier below must remain C with that carrier attached.

## Field 2: code

Accepted file:

~~~text
probes/P-RECORD-QUOTIENT-CALCULUS-1/verify.py
~~~

Exact integers and integer tuples only. Python standard library only, with one
itertools import. No float, complex number, approximation, randomness, network,
subprocess, external data, filesystem read or write, or read of canon/. Zero
arguments. Deterministic stdout contains no environment, platform, path or
timing field. Empty stderr on a clean pass. Exit zero only if every gate passes.

Ideals are represented directly as Hermite-normal-form sublattices of Z^4 in
the basis 1,z,z^2,z^3 of Z[X]/(1+X+X^2+X^3+X^4). Quotients are enumerated over
their HNF boxes. The verifier therefore carries non-rational ideals such as
(lambda)^L(2) directly.

The 31 gates are grouped as follows:

~~~text
W1-W4       ring and ideal-lattice machinery
F1-F5       prime factorization and residue reduction controls
R1a-R1e     canonical Booleanization
R2a-R2c     radical invariance
L1-L5       exact Loewy orders and the n^0 convention
H1-H3,H5,H6 unital R-algebra maps, thinness, no section and the independent
             CRT valuation count
N1-N4       fixed-support depth no-go
~~~

The formal command is exactly:

~~~text
python3 probes/P-RECORD-QUOTIENT-CALCULUS-1/verify.py
~~~

## Field 3: carrier

~~~text
ring:             R = Z[X]/(1+X+X^2+X^3+X^4)
basis:            1,z,z^2,z^3
support catalog:  primes above 2, 3, 5 and 11

named ideal       norm
(lambda)          5
(2)               16
(3)               81
(4)               256
(5)               625
(6)               1296
(lambda)(2)       80
(lambda)^2(2)     400
(10)              10000
(11)              14641
(20)              160000
~~~

Idempotents and Loewy layers are fully enumerated for those eleven finite
quotients. The Hom audit uses the eight listed ideals of norm at most 2000 and
all 64 ordered pairs. The R6 audit uses I_L=(lambda)^L(2) for L=1,2,3,4,5, of
norms 80, 400, 2000, 10000 and 50000.

This finite family audits the formulas and controls; it does not carry the
universal quantifiers or the word unbounded. Those belong to the proof in
Field 1. No external data is used.

## Field 4: systematics

There is no numerical tolerance. Every scientific assertion is an exact
equality, inequality, ideal containment, finite enumeration or tuple identity.

Known hazards and frozen controls:

~~~text
wrong Loewy origin
  n^0=R/I is written into the statement. L4 exhibits the different table
  obtained by dropping the first layer.

support counted by rational primes
  (11) splits into four prime ideals; R1e requires sixteen idempotents there,
  while (6) has two prime ideals and four idempotents.

cardinality mistaken for structure
  R1a requires a bijection onto actual subsets and R1c checks Boolean
  operations. R3 claims layer orders only, not module decompositions.

unitality built into its own control
  multiplicative R-linear maps are enumerated first from idempotent images of
  one; the unital filter is applied afterwards. H6 compares that enumeration
  with a separate count of selectable CRT components from prime valuations.

shared radical route
  L5 compares the lattice-chain index with a product of residue-field sizes
  over support and does not form the radical on its second route.

finite audit mistaken for proof
  every finite range is stated in Field 3. The universal claims stand on the
  explicit proof in Field 1.

ring-map machinery trusted wholesale
  F5 checks reduction as a ring map on a deterministic bounded subset for the
  selected residue primes. This is a machinery control, not a sampling claim
  for R1-R6 and not a proof of the universal theorem.
~~~

The quotient and idempotent enumerations over the frozen finite carrier are
exhaustive. The F5 machinery check alone uses a deterministic stride through a
bounded set, exactly as disclosed above. No statistical sampling,
uncertainties or error bars exist. SAMPLING NOT PROVIDED.

The formal run limit is 120 seconds. Before pinning, a float in a scientific
assertion, a syntax failure, stale authority, a collision, or any extra probe
file is STOP. After pinning, any mutation of PREREG.md or verify.py, threshold
movement, amend, rebase, squash or force-push is STOP.

## Field 5: failure threshold and decision

Thresholds never move after this pin. Any one failed gate fires the probe.

~~~text
RECORD-QUOTIENT-CALCULUS-CONFIRMED
  the written proof remains valid and all 31 exact gates pass.

RECORD-QUOTIENT-CALCULUS-FIRED
  any gate fails or a frozen proof step is invalid. The run and fired
  falsifier are preserved; no threshold is adjusted and no T is earned.
~~~

Candidate falsifiers, one line each:

~~~text
an idempotent of R/I whose local residues are not zero or one, or a failure of
the canonical Boolean map for some nonzero proper ideal I;

a failure of Idem(R/I) -> Idem(R/rad(I)) to be bijective;

a layer order different from product {N(P):e_P>k}, or Loewy length different
from max_P e_P;

a unital R-algebra map R/I -> R/J when I is not contained in J, two distinct
such maps, or failure of the canonical projection when I is contained in J;

a unital R-algebra section of a strict quotient;

an L>=1 for which I_L=(lambda)^L(2) changes support, radical, reduced record or
idempotent count, or for which L(R/I_L) is not L;

a failed ring, HNF, factorization, residue or independent-route machinery gate.
~~~

No threshold depends on the exposed incubation output. A fired result is a
first-class result and is merged as fired.

## Field 6: action layer and firewall

L1 state only. No L2 manifold, L3 boundary, L4 support, L5 stream or L6 measure
claim is made and no lift is named.

R1 describes the space of Boolean idempotents, not which atom occurs. R4
classifies possible unital quotient maps, not which ideal is physically
realized. R6 is a negative theorem and supplies no completion law.

Nothing here selects I or creates an apparatus, instrument, event-completion
law, orientation, read convention, decoder, atom selection, measure, Born
weight, coarse-graining, RG flow, continuum statement, write/read/scale
dictionary, neighbouring-ring census, cyclotomic unit-rank minimum or
M=(I,tau,mu) signature.

~~~text
SAMPLING NOT PROVIDED.
~~~

## Formal order

PREREG.md and verify.py are committed together and pushed. Both are read back
byte for byte from the public remote in a separate clean checkout. The
accepted verifier is then run exactly once from that checkout's repository
root. EXPECTED.txt, RUN.md and RESULT.md are added without changing either
pinned file. One probe-only pull request must pass byte-identical stdout on
x86_64 and aarch64 and the aggregate check. Merge is by merge commit only.
Registry, frontier and Canon treatment is a separate later fold.
