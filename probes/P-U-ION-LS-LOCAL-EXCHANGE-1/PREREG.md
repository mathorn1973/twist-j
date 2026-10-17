# P-U-ION-LS-LOCAL-EXCHANGE-1 preregistration

**NON-CANONICAL. L1 exact audit of a construction in an externally adopted
effective ion model.** Reservation [#1364](https://github.com/mathorn1973/twist-j/issues/1364).
No public status, physical error certificate or full-history realization is
earned by adopting this model. Canon v97 and the physical HOLD in #1359 are
unchanged. This new probe does not amend #1361 or #1363.

## 1. Equation and frozen target

Freeze the physical level dictionary and port roles of #1363 at
`8847b657c648b5c2b231eca13d9adfbef451cc60`. For the first and second local
contacts, respectively, the actual pair inputs are `|s,1>` and `|s,4>`,
with every s in F5. The corresponding required outputs are `|1,s>` and
`|4,s>`. All 25 original histories remain in scope as input provenance:
the first local requirement is repeated over a2, and the second over a1.
Their preparation, other data, and native continuation are not implemented
by this local study.

The mandatory basis-label target allows a fixed, declared phase for each
s and each program c=1 or 4, with no input-dependent program choice. A full
coherent SWAP on all 25 arbitrary two-ion inputs is **not required**.
The present candidate supplies a stronger sufficient result: in the fixed
interaction frame specified by MODEL.md, each five-dimensional actual
input subspace transfers coherently up to one source-independent phase.
The permitted laboratory-frame phases are the known free phases of that
frame, not retrospectively selected corrections. The exact effective
endpoint must factor from the included motion and remainder with the
source-independent action specified in MODEL.md.

Only the two predetermined programs indexed by c=1 and c=4 are admitted
as this constructive witness. Either may be used on its corresponding
addressed pair. Their selection uses the contact number, not a1 or a2.
The claim is their finite reachability within the frozen control model;
failure of a witness is not a no-go for every other word in that model.

## 2. Code and exact construction

Accepted primary: `verify.py`. Independently authored check:
`verify_independent.py`, executed as a separate isolated Python process.
No code imports the old ion writer or any sealed scientific verifier.
No floating-point tolerance, numerical pulse optimizer, stochastic search,
matrix logarithm, uncontrolled product limit, or abstract universal-gate
assumption is admitted.

The primary uses exact rational coefficients in Q[z]/(z^4+1), z=exp(i*pi/4).
The independent code uses a separate Q(i,sqrt(2)) representation. Symbolic
quadratic coefficients verify the LS profile identity for every real
fixed profile, not a chosen integer approximation to measured shifts.

Freeze this chronological word construction:

1. Use affine permutations p(j)=a*j+b mod5 in lexicographic (a,b) order,
   a=1,2,3,4 and b=0,...,4. Compile each p by disjoint cycles, visiting
   the smallest unvisited index first. A cycle (0,a1,...,ak) is the star
   sequence a1,...,ak; a nonzero cycle (a1,...,ak), k>=2, is the star
   sequence a1,...,ak,a1. Singleton cycles do nothing. Each star is the
   documented collective R^(0,j)(pi,0); its monomial phases are retained.
2. One echo consists of twenty blocks: apply that compiled p, one fixed
   closed LS loop, then the exact inverse carrier word. All twenty LS
   loops have the same profile, amplitude and duration. Inverse carrier
   pulses use positive durations and laser phase shifted by pi.
3. By the symbolic identity and parameter condition in MODEL.md, an echo
   acts as G with diagonal entries 1 on |jj> and -i on |jk>, j!=k, apart
   from one common phase from any included stationary diagonal terms.
   G is a proved composite, never an assumed physical primitive.
4. For c in {1,4}, process j=0,...,4 except c in ascending order. Each
   pair block is: G; Vx^dagger,G,Vx; Vy^dagger,G,Vy, in time order,
   with Vx=R^(c,j)(pi/2,pi/2), Vy=R^(c,j)(pi/2,0).
   Compile these rotations into star pulses as in PROOF.md. No direct
   D-D transition is added to the library.
5. Append R^(0,j)(2pi,0) for j=1,...,4 except c in ascending order.
   These implement D_c, with +1 on c and -1 on the other four levels.

The proof gives 240 completed LS loops and at most 2923 star carrier
pulses per contact, with total carrier angle at most 2918*pi. Exact
counts from the deterministic compiler will be reported, not fitted.
No minimality, optimal runtime or optimal physical fidelity is claimed.

The independent checker deliberately uses a separate greedy output-label
compiler for the affine frames. It verifies the same diagonal conjugations
including cancellation of its monomial phases, and the same external
contact-word chronology. Its frame pulse counts describe that alternate
implementation, not a reproduction of the primary cycle-compiler counts.
The stated resource bounds are audited against the primary frozen compiler.

## 3. Carrier, sources and control admission

Authority and preparation baseline: public main
`2973a432303e046aacb2cee3cea97254ea3ab8eb`, Canon v97 as declared by STATUS.
The local physical class is defined in MODEL.md and independently sourced
in SOURCES.md. PROOF.md supplies the continuous-model closure and finite
word derivation. All are frozen with this preregistration before execution.

The allowed elementary controls are only collective resonant 729 nm
0<->j carrier pulses, and completed light-shift loops in one harmonic COM
mode. The geometric phase difference is fixed at pi, the detuning delta_*
is fixed before profile calibration, and Delta_j=lambda*d_j uses one
common intensity scale and one fixed nonscalar profile d. The amplitude
lambda_* required by the proof must lie inside an independently specified
admissible range. It is not five independent level-shift controls.

Motion at local input may be mixed and correlated with the included
remainder. The chosen physical comparison domain has support in number
levels 0,...,10; this does not assert actual preparation or cooling of the
time-six apparatus into that domain. The ideal factorization is proved
operatorially and uses no new common auxiliary state between loops or
contacts. The selected model, including the leading carrier approximation,
has exact zero local mathematical error. No calibrated real-device error
is inferred from this statement.

Finite duration and incident drive-energy expressions are included in
MODEL.md. They are conditional on the fixed calibrated amplitudes, Rabi
rates and powers being admissible. They are not a closed finite quantum
laser/controller dilation or a total apparatus work balance.

## 4. Systematics, inheritance and prior knowledge

The mathematical construction was derived and discussed analytically before
this pin. In particular the expected positive result, the twenty-member
twirl, embedded exchange, phase correction and conservative counts are
already exposed in issue #1364. The formal run is an exact audit of that
disclosed candidate, not a blind prediction. No candidate or predecessor
scientific code was executed during preparation. Syntax/AST checks and
repository/source reads are permitted before pinning.

The primitive physical ingredients come from Hrmo et al.; the fixed-profile
intensity law is supported by the underlying optical Stark-shift theory.
The twenty-permutation construction is derived here and is not attributed
as an experimental result of either source. The source's simplified
equal-D-shift echo is not imported. All five fixed shifts are retained.

The single-mode, leading Lamb-Dicke/resonant-carrier model excludes several
real effects. Off-resonant and number-dependent carrier response, additional
modes, scattering, metastable decay, profile variation, ramps and cross-talk
remain physical errors without a numerical aggregate bound. The analytical
closure of one ideal mode is not an all-mode hardware certificate. The
archive and full n=0,...,9 resource history stay outside the local model.
The earlier four-state information lower bound is unaffected.

## 5. Failure thresholds and outputs

Exact arithmetic, zero tolerance. The primary must verify:

- elementary carrier unitarity and positive-time inverse phases;
- all 20 compiled permutation label actions, their inverse phases and
  six-star-pulse upper bound;
- all 25 symbolic quadratic echo identities and local diagonal-phase
  cancellation, using ordered-pair transitivity;
- exact D-D rotation compilation from the allowed star edges;
- all 200 pair-block basis columns (eight pair blocks times 25), including
  their spectator phases;
- all ten actual coherent contact columns, stronger than the mandatory
  population requirement;
- the specified LS count, carrier count and total-angle bounds;
- an omitted-LS, same-wait control with exactly one successful basis input
  per contact; and a witness that the candidate is not a full SWAP on
  arbitrary pair inputs, which is not a failure of the local target;
- independent checker exit zero, empty stderr and its explicit PASS.

Any wrong identity, forbidden primitive, resource-bound violation,
unaccounted required phase, malformed manifest, dependency change, timeout
or nonzero/error output is a STOP for this candidate at its actual cause.
No postselection, decoder adaptation or silent repair is permitted. A
candidate failure does not establish emptiness of the complete control
class. A computation error before a completed formal gate is disposed of
under the repository's abandoned-pin policy, never repaired under the same
frozen identifier.

Run from the repository root on Linux:

```text
python3 probes/P-U-ION-LS-LOCAL-EXCHANGE-1/verify.py
```

The independent subprocess timeout is 300 seconds. The whole formal audit
has a 600-second limit. Record actual stdout, stderr, exit, environment,
elapsed time, pin and hashes in RUN.md; exact successful stdout becomes
EXPECTED.txt only after the first recorded execution. Record the outcome
and its scope in RESULT.md. Required CI architectures must replay the same
accepted primary and stdout on the same PR head. No scientific claim is
inferred from the infrastructure checks alone.

## 6. Action layer and custody

Action layer L1: exact finite operator-word audit within an externally
adopted effective model. No L1-to-physical or probabilistic occurrence gate
is closed, and no result is derived from J. The positive decision is
**conditional ideal-model local reachability**, not an experimental claim.

INPUTS.json binds the byte lengths and SHA-256 values of the scientific
support documents and independent code. The primary embeds the manifest
hash; the public immutable Git pin binds the primary and manifest together.
This avoids a circular self-hash. Commit, push and read back every pinned
file before execution. The preregistration, accepted code and support
inputs are immutable after that pin. Results and neutral validation records
are added separately. Only this new probe directory is changed.
