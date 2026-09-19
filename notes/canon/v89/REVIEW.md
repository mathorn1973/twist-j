# Result-exposed independent statement review

**NON-CANONICAL. PREPARATION REVIEW ONLY.** No formal scientific verifier,
blind breaker, architecture gate or public promotion was executed here.
This note is not an accepted proof record or an execution receipt.

## Exposure and method

The reviewer read the user-supplied v89 intake proposal, STATUS, POLICY,
AGENTS, the relevant Canon/CORE/FRONTIER and Registry/Evidence/dependency/gate
rows, and the inherited public native-quotient and Galois-code proofs.
The reviewer also received short statement-only clarifications from the
intake builders. The reviewer did not read either new author verifier,
either incubation audit.py, or the new source/intake proof implementations.
Prior target results were already exposed in the proposal. Accordingly
this is a preregistration-statement review with independent mathematical
reasoning, not a result-blind test or a sealed prereg-only breaker.

No scientific code was run. Local checks concern document bookkeeping:
the fold lists exactly all 28 current H/O rows, with matching statuses;
no normative Canon diff is present at review time. Ordinary file hashes
identify reviewed draft bytes and do not make them a public pin.

## Channel statement review

Reviewed `galois-channel/PREREG-DRAFT.md`, final local preparation SHA-256
`0f3d76b2709e73ea4172d0298585838c95fc5673afaeaaab252080e766d5d2c1`.
This is a mutable local draft; any amended byte identity must be recorded
and reviewed before this assessment is used for a formal pin.

No mathematical counterexample was found at its stated full complex CPTP
scope. The following independently reconstructed checks explain the
assessment and the limits of a future finite audit.

1. **Full code, one environment vector.** For a Stinespring isometry,
   exact preservation of every code density and its coherent superpositions
   forces one environment vector for the entire code. Since F is onto the
   complete four-dimensional output, isometry orthogonality puts every
   complement image in the environment subspace orthogonal to that vector.
   This removes all code/complement partial-trace cross terms. Preservation
   only of four separately tested basis densities would not suffice.
2. **Universal mean bound.** Let q_ka=Qe_ka. The four q vectors at fixed k
   are orthogonal with squared norm 3/4. Their outer-product sum is 3/4
   times a rank-four projection. For positive complement effects A_k with
   sum Q, total complement agreement is at most (3/4)Tr(Q)=9; the code
   contribution is one over all sixteen points. Mean agreement is thus at
   most 10/16=5/8, and minimum agreement is at most the mean. The stated
   effects attain equality at every point.
3. **Every equality slack matters.** Equality makes each A_k supported in
   span{q_ka:a=0,...,3}. Write its coefficients in that four-vector basis.
   At fixed a, signed diagonal conjugation reduces the vectors to
   q_k=e_k-(1/4)1. The four outer products |q_k><q_k| are linearly
   independent: their diagonal-value matrix is (1/2)I+(1/16)J, with
   eigenvalues 1/2 and 3/4. This independence holds for complex
   coefficients. Each a,b block of sum A_k=Q consequently fixes its
   coefficient to delta_ab, including the off-block coefficients. Thus
   A_k=sum_a|q_ka><q_ka| is forced, without restricting channels to real or
   rational matrices. Merely verifying ranks of selected examples does
   not prove this equality classification.
4. **Purified auxiliary lower bound.** The code environment direction is
   separate. Each output-coordinate complement effect is V_perp* (|k><k|
   tensor I) V_perp and therefore has rank at most the remaining environment
   dimension. Its rank four gives at least 1+4=5 total directions. A mixed
   ready state must count its purification. The four-state nonoptimal
   control makes clear that exact-code transfer alone has no five-state
   bound.
5. **Positive and negative controls differ.** Point-exact compatibility
   means the endpoint coordinate has probability one. Its uniform coded
   coordinate law cannot match all F rho F*. The rank-four point-exact
   control in the prereg need not output I/4 for every code input; I/4 is
   the stated fixed-alpha control. Phi5 and Phi17 agree on coordinate
   effects but differ on full raw output densities, so their channels
   must not be identified.
6. **Construction versus physics.** U20 is a complete orthogonal matrix
   certificate, with all residual outputs included. The fixed code output
   has the same auxiliary state for every alpha. It is not an outcome
   record and does not provide an occurrence law or reset.

The loader wording refinement was incorporated and reviewed: the prohibition
now covers post-freeze or source-state-dependent alteration of the declared
code/loader to repair target agreement. It does not prohibit the explicitly
constructed matched loader L. The construction makes no independent
physical target-independence claim. This resolved a scope-clarity issue,
not a discovered counterexample.

## Native point-port statement review

Reviewed `point-port/PREREG-DRAFT.md`, SHA-256
`8dcb21668f42f0420ec4a9f53f9c365fa6ca0bdfdee7d9b100f25cd025cd90e0`,
plus the builder's statement-only target weights and block endpoints.
No source proof, new PROOF-DRAFT.md, audit.py or verify.py was read.

No conceptual counterexample was found at the fixed-encoder,
source-independent-seed, unchanged-U port scope. The following are
independent deductions from the preregistered mathematical contract:

1. Freeze the common seed xi. Equal encoded sums give equal initial
   quotients, hence equal histories under every subsequent native step,
   and equal deterministic processor responses. Integration over the same
   source-independent seed law gives at most five transcript laws.
   Conditioning on the same processor completion event preserves this
   factor wherever its probability is positive. The prereg requires it
   positive at every supported source. Source-conditioned seed laws,
   seed-dependent f, native interventions or extra source-sensitive
   acceptance would change these premises.
2. The six displayed original target values are distinct, so no five-law
   response realizes all six. The zero source remains undefined rather
   than providing a sixth numeric target or a zero weight.
3. Arbitrary deterministic f realizes every five-label assignment k by
   choosing f(p)=(k(p),0,0,0). The ready (0,1) first-observation separation
   supplied by the inherited quotient makes the stated upper comparison
   operational within this mathematical port. The uniform random response
   is an external input, not occurrence derived from native U.
4. The six sharp free-class weights 0,9/64,2/7,5/8,49/64,1 have adjacent
   gaps at least 9/64. Six points cannot fit into five radius-e intervals
   if e<9/128. The five supplied target-cover intervals
   [0,1/46], [1/26,1/6], [2/7,3/8], [5/8,49/64], [1,1] each have width
   at most 9/64. Their midpoint responses attain 9/128 provided that
   the complete target census lies in that union and every claimed target
   witness exists. Those finite premises still require exact independent
   audit; their assertion alone is not a proof of exhaustive coverage.
5. In a permutation all encoded-sum fibres have 125 original labels.
   Exactly one has 124 supported labels and the null; the other four
   each have 125 supported labels. The fibre containing a beta=1 source
   therefore has at least 124 supported sources. Conditional on the
   frozen exact count of only 120 sources with beta>5/32, that fibre
   contains a beta<=5/32 source, forcing response error at least
   (1-5/32)/2=27/64. The supplied sorted-block extremes and the explicit
   full 625-label bijection attain the bound; testing only an injection
   on the supported labels would be a different problem.
6. Independently of numeric minimax error, the null's sum fibre contains
   124 supported sources with the same full response law. Thus its
   support tag cannot be distinguished in the stated permutation class.

The statement-only amendment was incorporated and reviewed. The final
prereg now embeds the complete 22-value table, six packing witnesses,
both five-block certificates, full permutation assignment, ready
observations and external-randomness construction. It explicitly defines
z_n as the sum of all six native checkpoint coordinates, distinct from
the encoded initial four-piston sum. The listed multiplicities sum to 624;
the entries strictly above 5/32 sum to 120, and their cumulative counts
agree with the five displayed faithful block endpoints. The first-ready
observations also agree directly with the inherited quotient formulas.
These are internal statement consistency checks. This review does not
claim an independent enumeration of all 624 sources or execution of the
full attaining bijections; those proof/audit obligations remain.

## Readiness and promotion boundary

The editorial fold and physical template are ready for local review.
Formal pin readiness additionally requires finalized independent proof
review, approved exact verifier content, collision-cleared ownership and
source custody, and the repository's current public pin procedure. No
local preparation note, static compilation or future successful audit by
itself gives a public theorem or a physical dictionary.

The three proposed claims remain L1 mathematics with external CPTP
premises explicit where used. Evidence rows must reference actual sealed
RESULT.md paths and tool-computed bundle digests. Existing reader/Born
projection gates do not supply a new physical bridge. The 28 H/O rows,
especially apparatus, terminal semantics and class completeness, remain
unchanged. The physical template deliberately leaves actual carrier,
clock, material outcome record, ordered occurrence and reset unresolved.