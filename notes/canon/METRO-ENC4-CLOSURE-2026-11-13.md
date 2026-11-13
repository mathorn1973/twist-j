# Proposed ENC4 metrology closure

NON-CANONICAL. Proposed text and ledger changes for a separately
reviewed fold. Public Canon v111 remains authoritative. Public base
`f390a3ada72892afa5b73e6f07990dc4ab129dfb`. Public issue #1984.
The prospective finite audit is
[P-METRO-ENC4-CLOSURE-1](../../probes/P-METRO-ENC4-CLOSURE-1/PREREG.md).

## Scope of the proposed decision

Section 15 declares a fixed digit and padding convention for the
dimensional class and adopts ENC4 specifically for common blocking.
This proposal adopts the tagged aggregate formula for common ENC4.
It assigns the remaining encodings to METRO-ADMISSIBILITY-DIM and
keeps that row and its existing gate open. The full dimensional
class is the disjoint union of the two parts. R1 remains U_RF minus
that full union; R2 through R8 retain their present ownership.
No assumption identifies a general fixed padding convention with ENC4.

## Proposed section 15 text

### METRO-ENC4-TRANSLATED-BOX [T]

The source is a finite deterministic commuting digit-word tuple of
section 15 with q >= 2, a >= 2, r >= 1, nonempty allowed starts,
and a complete rational nonnegative readout W5. The convention is
one of the four common ENC4 conventions, used in all axes. Positive
integers have exactly their canonical base-q words, most or least
significant digit first, and zero has the empty word in E0 or the
single zero digit in Z0. Distinct coordinate digit maps commute.
The domain is N^a with its ordered input coordinates and a separate
ordered output basis.

For a translated box R and allowed start s put
M_R(s) = (1/|R|) sum_(n in R) W5(state(s,n)). The tagged aggregate
observable is A_R(s) = Normalize(M_R(s)). Its distance is the maximum
coordinate difference within the probability tag, zero between two
ZERO tags, and 1 between unlike tags. The terminal probability is
rational. The direct decision asks for a common limit over every
translation and allowed start as the minimum box side tends to
infinity, with an effective uniform modulus. RAW is the separate
arithmetic convergence question for M_R, with the same uniformity.
Positive scaling by |R| has no effect on A_R.

**Theorem.** A finite exact decision is available for both questions.
There is a finite set G of rational aligned-box limit vectors,
specified below. RAW accepts exactly when G is a singleton. Tagged
convergence accepts with ZERO if the entire stream is zero. For every
other stream it accepts exactly when zero is absent from G and the
vectors of G have one common normalized direction. Otherwise the
decision is INADMISSIBLE. The joint proof relation below is terminating,
sound, complete and decision-coherent, and each admitted reduction
preserves the decision and terminal value.

**Aligned limits.** Let P_i be the uniform digit-count transition
matrix on rational column functions. Its graph is finite. For each
closed irreducible class take the gcd of its positive return lengths.
Let h_i be the least common multiple of these periods. The recurrent
classes of P_i^h_i are aperiodic. On each such class a fixed power
is strictly positive: finite return lengths with gcd one generate
all sufficiently large lengths, and fixed connecting paths give
positivity at every pair of vertices. A uniform positive lower bound
for that power contracts the differences of probability rows. The
closed classes thus converge to their positive stationary rows. From
each transient vertex some path enters a closed class, so a uniform
finite-step positive entrance bound makes the transient tail decay
geometrically. Truncating the entry time and passing to the limit
shows that E_i = lim_m P_i^(h_i m) exists. It projects onto the
kernel of I-P_i^h_i along its image, since the limit fixes that kernel,
annihilates that image, and power boundedness excludes a Jordan chain
at 1. Rational elimination constructs E_i. Each E_i is stochastic.
The limit of P_i^k at residue b modulo h_i is P_i^b E_i.

Take a positive aligned interval [c q^k,(c+1)q^k), c >= 1.
Its variable digit block of length k keeps all zeros, and its fixed
word is enc_q(c). Write X for the pullback by that word. Its
average operator is X P_i^k for MSD and P_i^k X for LSD. Multiply
these operators in coordinate order on W5 and evaluate at an allowed
start. This product sums every digit choice on the Cartesian box
with uniform weights. Replace each variable factor by its residue
limit. The resulting values, over all allowed starts, positive
canonical fixed-word maps and residue vectors, form G. Positive
canonical word maps are finite transformation closures, starting
with a nonzero digit and adding digits on the right for MSD or
on the left for LSD. The complete stream is identically zero iff
all products of these maps enlarged by the correct zero map give
zero at every allowed start. This covers all coordinate faces.

**Zero-limit lemma.** If a member of G is zero, some aligned box
family at an allowed start has identically zero weight at every
length in its stated residue class. For each axis, a finite word
b_i sends the whole carrier into the union of closed classes.
To construct it, append a path sending one current transient image
into a closed class. Closed images remain closed and the number
of transient images strictly decreases. Appending further digits
preserves this property and adjusts the length to any prescribed
residue modulo h_i.

Choose positive fixed words v_i and residues kappa_i realizing a
zero limit. In LSD prepend b_i to v_i, with |b_i| divisible by
h_i, leaving the variable residue unchanged. In MSD append b_i
to v_i, with |b_i| congruent to kappa_i, and set the new variable
residue to zero. Both modified fixed words remain canonical positive
words. If a modified box has a point of positive weight, reinterpret
b_i as part of the variable word of the original box. The variable
segment now has the original residue and ends in a closed class.
Insert arbitrarily many period-multiple random letters at the end
of that segment and require a return to the same endpoint. The
probability of this return is bounded below for all sufficiently
large multiples, by the positive stationary diagonal entry of
the recurrent subclass of P_i^h_i. Fixed paths have positive
probability. The returns preserve each coordinate entry and exit
state, so the product event has positive probability bounded away
from zero while all side lengths grow. Nonnegative weights then
contradict the original zero limit. Hence every modified box is
zero. This applies even when the original zero-limit residue has
strictly positive mass at every finite length.

**Translated-box bound.** For each axis find a positive multiple
K_i of h_i with theta_i = ||P_i^K_i-E_i||_infinity < 1, where the
norm is the maximum absolute row sum. The search terminates by
convergence. Since P_i and E_i commute and P_i^h_i E_i=E_i,
(P_i^K_i-E_i)^m=P_i^(K_i m)-E_i for m>=1. Stochastic contractivity
bounds the factor error at exponent k>=K_i by
theta_i^floor(k/K_i). All word and residue factors are stochastic.
With W=max_(s,j) W5(s)_j, telescoping gives aligned box error at
most D(k)=W sum_i theta_i^floor(k/K_i) whenever all exponents are
at least k>=max K_i.

Decompose the positive part of each interval into maximal aligned
q-adic intervals. At a given level a maximal interval has a parent
crossing one of the two endpoints. Each parent contributes at most
q-1 wholly contained children. The point zero has relative weight
at most 1/N_i. Thus the total fraction of a product box with an axis
at zero or below level k is at most a(1+2 q^k)/M for min N_i>=M.
Replace each good product box by its aligned limit and each bad
product box by any member of G. The resulting convex combination
is within D(k)+W a(1+2 q^k)/M of M_R(s). Given rational eta>0,
choose k with D(k)<=eta/2 and M>=max(1,ceil(2 W a(1+2 q^k)/eta)).
This is an effective uniform bound over starts and translations.

Every aligned limit is realized by a subsequence with all sides
growing. Distinct raw limits preclude RAW convergence. If zero is
in G and the stream is nonzero, the zero-limit lemma gives
arbitrarily large ZERO boxes, while boxes enlarged around a
positive point stay PROBABILITY. If zero is absent, differing
directions preclude tagged convergence by continuity at positive
mass. If all directions coincide at p, each convex combination is
mu' p with mu'>=mu=min_(g in G) sum(g)>0. Raw error eta yields
normalized error at most (r+1)eta/(mu-r eta) if r eta<mu.
Choose eta=min(mu/(2r),epsilon mu/(2(r+1))) for tagged tolerance
epsilon. Use eta=epsilon for an accepted RAW claim and M=1 for
an identically zero stream. This proves the decision and modulus.

**Joint certificate.** A verifier recomputes the digit action and
all cross-coordinate commutators, transitions, finite boundary
maps, full-stream zero test, residue vectors and limit set. It
checks each E_i is stochastic, idempotent, commutes with P_i and
satisfies P_i^h_i E_i=E_i, and checks K_i is a positive multiple
of h_i with the exact stated contraction. Those checks imply the
unique residue limits by the power identity above, without trusting
a claimed spectral computation. The finite data give terminal
values, bound parameters, and a pair of aligned witnesses for a
raw or direction split. A tag split supplies one positive point
and a positive-prefix zero family. For each axis, evaluate the
fixed map at the correct end of the digit segment and compute the
union of all support sets for lengths kappa_i+h_i m, including
the transient preperiod and the repeated support cycle. Proceed
in coordinate order and verify that the final support has zero
weight. This independently checks the exact zero family, with
no dependence on the search used to construct it.

The rational digit-invariant submodule V is the span closure of
the output columns under every digit pullback. Iterate rational
elimination until the dimension is unchanged. The allowed-start
observable kernel consists of vectors in V vanishing on the set
reachable by digit words from the allowed starts. That set is
digit-closed, so the kernel is invariant. Choose a rational
complement and record the induced digit actions and outputs in
the quotient. Compute each coordinate average there, factor its
characteristic polynomial over Q and use Bezout idempotents for
coprime primary factors. Multiply commuting coordinate projectors
to obtain joint sectors. The nullities of powers of each primary
factor on each sector give Jordan counts by successive differences
divided by its irreducible degree. The peripheral factors divide
x^h_i-1 and are semisimple by bounded powers, inherited from the
stochastic carrier. These data are obtained by finite exact rational
linear algebra and polynomial factorization over Q. For a finite
algorithm for factorization, first clear denominators and take the
primitive integer polynomial. For each possible degree d, choose
d+1 integer inputs with nonzero polynomial values, enumerate their
finite signed divisors, interpolate candidate factors, and retain
only primitive integral exact divisors. Recurse on found proper
factors. The degree decreases and exhaustive interpolation certifies
irreducibility when no proper factor exists. A verifier recomputes
these data in a fixed rational basis and checks the record. It
also computes an arbitrary requested modulus from the checked
bound parameters. No computation of a direct limit is an oracle
in this relation. The construction produces a valid record for
every tuple. The decision and exact terminal are unique because
all valid records certify the same direct convergence criterion.

**Reductions.** Relabeling conjugates the digit maps and transports
starts by the bijection. Reachable restriction retains every
intermediate state of a digit word from an allowed start. The
congruence-checked Nerode quotient commutes with every word
action and retains the output at the image of each start.
Coordinate permutation carries starts as declared, permutes
coordinate actions and boxes together, and preserves cardinality
and the minimum side. Common same-carrier blocking under Pre_blk
and initialized MSD blocking preserve the full stream at each
integer index by METRO-COMMON-BLOCKING. These arrows use identity
output transport in the fixed ordered output basis. The set of
transported allowed-start streams is the same even when the
quotient identifies duplicate streams. Every box mean and its
tag are identical under transport, including zero, so the
decision and terminal value agree along every admitted arrow
and finite zig-zag. No completeness classification of all
stream-equivalent tuples is used here.

### METRO-ENC4-NORMALIZATION [D]

Adopt the preceding tagged aggregate L5-to-L6 contract for ENC4.
For each box Normalize returns an element of Y_r. For each source
tuple the admission algorithm returns ADMISSIBLE(L), with L in Y_r,
or INADMISSIBLE. ZERO is the value
of Normalize on a zero vector. At positive mass Normalize divides
by the sum once, after forming the box mean. The RAW condition
is a mathematical diagnostic and is not an additional admission
requirement. The separate arithmetic question can accept a zero
raw limit even when the tagged decision rejects, or reject
oscillating masses with one common tagged direction. The adopted
contract is a dimensionless normalization of a selected mathematical
stream. It imposes no physical unit or occurrence law.


## Proposed ledger and gate changes

- Register METRO-ENC4-TRANSLATED-BOX [T] as a mathematical theorem
  in section 15 with the displayed full common ENC4 domain,
  rational finite decision, rejection certificates, uniform modulus
  and admitted-reduction invariance. Use the inline proof as the
  proposed theorem evidence. The probe is an executable finite audit.
  An admitted exact counterexample to any of the aligned limits,
  zero-family lemma, certificate properties, modulus, or reduction
  invariance falsifies the corresponding clause.
- Register METRO-ENC4-NORMALIZATION [D] as the separately adopted
  typed L5-to-L6 dictionary in section 15. It depends on
  METRO-ENC4-TRANSLATED-BOX and the action layer definitions. Give
  it GATE-L5-L6-METRO-ENC4-NORMALIZATION, kind DICTIONARY_LIFT,
  with L5 source and L6 destination. The gate adopts the total
  per-box Normalize applied to the raw box mean and the uniform
  admission algorithm for that exact class. An exact discrepancy
  with the stated tag or terminal under the adopted formula fires
  the corresponding dictionary falsifier.
- Keep METRO-ADMISSIBILITY-DIM [O] and
  GATE-L5-L6-METRO-NORMALIZATION (OPEN_LIFT), and record that
  their remaining subject is the outside-ENC4 portion of the
  original dimensional class. Keep METRO-ADMISSIBILITY [O] with
  R1 defined as U_RF minus the full dimensional class, including
  the adopted ENC4 part. Retain the existing out-of-child R6
  boundary and the other residual obligations.
- The theorem uses the already admitted common ENC4 arrows,
  including METRO-COMMON-BLOCKING. It does not require a
  classification of every possible stream-equivalent tuple.
  Do not close METRO-REDUCTION-CALCULUS.
- The ledger owner adds the matching NORMATIVE, EVIDENCE,
  DEPENDENCIES, HISTORY and GATES records at the reviewed fold,
  preserving prior history. The registry drives regenerated
  frontier and status views. The fold regenerates normative
  checksums. This proposal assigns no release version and
  changes no active registry, gate, or published status.

A finite audit cannot by itself establish the all-input theorem.
The closure candidate requires independent proof review and
separate adoption of the ENC4 normalization contract. The broader
encoding class requires an effective contract and a new decision.
