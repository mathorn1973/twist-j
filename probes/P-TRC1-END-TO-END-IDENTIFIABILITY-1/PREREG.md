# P-TRC1-END-TO-END-IDENTIFIABILITY-1 preregistration

FROZEN EXACT TARGET. NON-CANONICAL. PUBLIC PIN MUST PRECEDE EXECUTION.
No external measurement payload is admitted.

```text
owner: A. M. Thorn
public issue: https://github.com/mathorn1973/twist-j/issues/901
branch: probe/P-TRC1-END-TO-END-IDENTIFIABILITY-1
base: 876726287c96d6c25a64029a339a99039bcfdd67
authority: ACTIVE Public Canon v80
action layer: L1 exact conditional transducer and finite probability simplex
physical lift: NONE
formal executions before public pin: 0
```

## 1. Equations and targets

Implement the MODEL-side composition specified in
`notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md`, with the direct five-field
cyclotomic write and the inherited signed five-site source and reservoir
equations. For a fixed valid head h and context c=(Gamma,q,N), freeze:

```text
z = balanced first four coordinates of h; P_0=(0,Sz),
checkpoint_t=U^t(h),
P_(t+1),b_t = cold_couple(P_t,Gamma),
H_(t+1,x)=H_(t,x)+Gamma_x*b_(t,x)^2,
C_(t,x)=floor(H_(t,x)/q),
tape_(t+1)=tape_t concatenated with signed b_t.
```

The source is prepared once. The original head supplies the quadratic read;
the moving checkpoint supplies the separate linear Tr4 and binary theta.
Every step emits one complete transition record, including a zero-crossing
step. Ordinals are exactly C_old+1 through C_new at each site. Compatibility
checks the deterministic transition itself, both pair and apparatus
snapshots, source/context/checkpoints, signed tape and all derived accounts.
Rereading is passive; reset is disabled; END retains the completed state
and emits no additional accounting record. Context equality includes N.

For distinct ordered heads h_i with positive rational weights p_i summing
to one, sample the head once at preparation and define

```text
P(visible prefix y)=sum_i p_i 1[predicted_prefix(h_i,c)=y].
```

The audit targets exact normalization, consistent prefix marginals,
conditioning by source-survivor weights, impossible-prefix handling and a
counterexample to replacing the joint law by a product of time marginals.
The product control samples labels of precomputed trajectories separately at
each cut; it is not a physical replacement of a source coupled to retained
memory. Prefix queries retain the same context, including its original horizon.

For rational calibration and prediction matrices A and B on a fixed finite
source family, with C=[1;A], prove and audit

```text
Bp is determined by Ap for every preparation mixture p
iff ker(C) is contained in ker(B)
iff rank([C;B])=rank(C).
```

The actual-chain negative fixture uses sources e0 and e1, whose scalar QDD
weights agree but whose origin threshold counts differ at Gamma_0=1,
q=1/16,N=1. The full QDD densities are not part of that calibration.
Interior mixtures with respective a/b weights (1/3,2/3) and (2/3,1/3)
retain identical calibration and predict crossing probabilities 1/3 and 2/3.
A positive algebraic control includes an explicit source-indicator calibration
row; it does not claim that this row is physically available.

Carry two additional analytic controls: visible histories are invariant
under z -> -z and ignore counter/final-coordinate provenance, admitting at
most 313 antipodal signed-head classes for each fixed context; and the
existing complete positive energy-partition obstruction excludes sharp
QDD LOW/HIGH redistribution when the origin is active and N>=1. This is
not a new physical no-go theorem. PROOF.md states exact domains and proofs.

## 2. Accepted code and public pin

The new executable scientific source set is chain.py and verify.py. Python
3.10 or later and its standard library suffice. All scientific arithmetic
is integer or fractions.Fraction. The implementation has no randomness,
fit, external payload, network access, external process, or physical
certificate issuer. It uses hash-bound public engines:

| Repository path | SHA-256 |
| --- | --- |
| probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/kernel.py | 8fe60efb5f1c8888ac455332ec8305bc531687836f5c604aedd2e483ed534ba9 |
| probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py | 983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60 |
| probes/P-DECODER-RESERVOIR-COUPLING-1/coupling.py | 54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403 |

The specification bytes at the declared base are:

```text
notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md
a5b79aa738c911b1373fe660b5d0055864f76287b1cf879bd212913ff000d03d
notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.json
6ed7dbf03cb70bdff9be74277e8aed21578c1321a0b0cfcd883495e06f4c3b30
```

The immutable accepted source set is this PREREG.md, PROOF.md, chain.py
and verify.py. The fresh public ID is claimed in issue #901. Before any
import or scientific execution, commit, push and compare all source bytes
with GitHub at the full pin. Also verify the three inherited engines against
their declared hashes. Static AST parsing and source review are allowed.

The sole scientific entry point is

```text
python3 probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/verify.py
```

A completed audit emits deterministic exact JSON. Failed audit assertions
and caught section exceptions are retained as PROOF_AUDIT_FAIL with a count
and a capped diagnostic list; the ordinary audit still completes with exit 0.
This does not authorize claiming success or repairing a failed pinned source.
An import/integrity or other precompletion failure remains distinct.
Preserve the first raw
stdout as EXPECTED.txt, and record the pin, source hashes, command, environment,
exit code, byte counts and stdout/stderr hashes in RUN.md. No source repair,
amendment, rebase, squash or force-push follows the pin. A precompletion
failure consumes the ID and requires the POLICY.md abandoned-pin disposition.
No execution record or computational result exists at the initial source pin.

## 3. Carrier and finite census

All source, context and record values are typed immutable finite data.
Malformed values are distinct from valid zero-source accounting and from
missing physical certificates. Freeze the following finite families:

1. All 625 signed vectors in {-2,-1,0,1,2}^4 at n0=0 and final pentits (0,0).
   Audit direct QDD, five-site preparation, the norm identity, and the 313
   antipodal classes. No long-wave propagation of this whole census is used.
2. All 15,625 six-pentit checkpoints at counters 0,1,32: 46,875 native U
   transitions compared with an explicit independent generator/clock oracle.
3. Propagated sources: zero, e0, -e0, 2e0, e1, (1,-1,0,0), (1,1,1,1),
   all with n0=0 and final pentits (0,0), together with e0 at final pentits
   (1,2) and e0 at n0=7. The latter aliases remain distinct full heads.
4. For each of those nine heads, use these five contexts:
   empty Gamma,q=1,N=0; empty Gamma,q=1,N=2;
   origin Gamma=1,q=1/16,N=2; origin Gamma=1,q=1/8,N=2;
   Gamma_0=1,Gamma_(1,1,0)=2,q=1/16,N=1.
   Verify complete transitions, reversal to cold input, energy/tape accounting,
   zero/subthreshold/multiple branches, ordinal ownership and all prefixes.
5. Deliberate malformed inputs and record mutations: invalid heads/contexts,
   forged pair snapshots, sign-changed outgoing amplitudes with unchanged
   squared energy, cross-source/context records, altered crossings, duplicate
   or skipped records and changed checkpoint provenance. They must fail the
   declared compatibility or validation relation. Missing physical evidence
   must not become a model success or zero-source result.
6. The fixed fair ensemble on heads zero and 2e0 at origin Gamma=1,q=1/16,N=2,
   grouped at the complete event-history and visible levels; exact prefix
   marginalization, survivor conditioning, impossible prefixes, preserved
   END payload and a concrete failure of multiplying separate time marginals.
   The extra interior mixtures in item 7 are also fixed rational inputs.
   None estimates physical occurrence frequencies. At prefix zero, the law
   of event tuples is a unit mass at the empty tuple, while complete prepared
   states separately retain the source and pair.
7. Extra one-step actual-chain fixtures: e0/e1 at origin Gamma=1,q=1/16;
   e0/2e0 at origin Gamma=1,q=1/8. Verify exact first-port deposits and
   threshold counts (1,0) and (0,2) respectively. Audit calibration/prediction
   matrix ranks, equal-calibration interior mixtures, the positive
   source-indicator control and the two opposite QDD-null witnesses.

Detailed assertions and output categories are frozen by verify.py at the
public pin. The finite census audits the independent general proofs; it
does not replace them with an extrapolation from bounded runs.

## 4. Systematics and declared choices

- The five-site source is designed with knowledge of the QDD norm. Neither
  norm agreement nor successful composition makes it an independent native
  physical preparation law.
- One wave update per U checkpoint is a selected label correspondence.
  U is not altered by context, observations, posterior weights or target data.
- Cold fresh incoming modes, a retained signed tape and exact rational
  thresholds are premises of this mathematical apparatus. Energy, heat,
  counts and remainders must not be counted as independent energy stores.
- Full retained records and their lossy visible projection have different
  equalities. Equal signs-squared or visible counts do not equate sources,
  complete records, native states or physical events.
- The once-selected ensemble is an imported probability premise. Exact
  finite probabilities do not prove a temporal frequency limit, an iid
  source, all-order Bernoulli behavior or a unique Born law.
- Calibration in the negative fixture means the explicitly named scalar
  QDD columns, not full tomography, physical calibration or a density matrix.
  The global linear criterion does not assert that every particular
  nonnegative calibration fiber is nonidentifying.
- Positive complete energy redistribution is a specific processing class;
  its obstruction does not exclude different couplings or coherent amplitude
  processing. Threshold records are not automatically sharp QDD outcomes.
- Only MODEL-side mathematical operations are implemented. FOREIGN_NIST
  envelopes, actual acquisition loss, source/readout calibration, physical
  certificate admission and #539 reset conformance are outside this probe.
  No physical payload is opened. #900's distinction among all-pairs counts,
  first gaps and hazards remains necessary for a later empirical comparison.

## 5. Failure threshold and disposition

The tolerance is exactly zero. Any failed exact identity, unexpected accepted
forgery, lost record, duplicate ordinal, incorrect posterior, altered
dependency, incorrect expected counterexample or type conflation defeats
that audit assertion. No parameter, source family, threshold, outcome
projection or failure rule is changed in response to execution.

Survival of the intended counterexamples is a positive audit result for
their stated negative claims. A failed new implementation is not a physical
falsification. Missing physical definitions remain STOP_PHYSICAL; they are
not converted to a negative physical theorem. Completed failures are
preserved under ordinary probe policy; uncompleted pins are abandoned.

## 6. Action layer and limit of closure

The work is L1: exact rational finite-support dynamics, records, matrices
and a conditional finite probability simplex. TRC1 names prospective
L4/L5 source/instrument/record interpretations and a separately supplied
L6 occurrence law. No such physical bridge is earned here.

The strongest intended outcome is a complete executable MODEL chain plus
an exact condition for when its selected calibration determines predictions,
with an explicit actual-chain nonidentifiability witness. Public Canon,
registry, ledger and physical owner issues #539/#830/#832/#834 remain
unchanged. A later Canon release is a separate authorized fold.
