# P-REGISTRATION-PAIR-RECOVERY-1 preregistration

FROZEN EXACT TARGET. NON-CANONICAL. No external measurement payload admitted.

```
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/899
branch: probe/P-REGISTRATION-PAIR-RECOVERY-1
base: 9d820faabc34224027b67d7cabd18355d396428f
authority: ACTIVE Public Canon v80
action layer: L1 exact rational coefficients and finite weighted event trees
physical lift: NONE
formal executions before public pin: 0
```

## 1. Equation, claims and intended counterexamples

For rational hazards h_1..h_N in [0,1], freeze

```
S_0=1; w_n=h_n S_(n-1); S_n=S_(n-1)(1-h_n);
u_0=1; u_n=sum_(j=1)^n w_j u_(n-j).
```

PROOF.md gives the independent coefficient/tree interpretation and proofs.
Targets, all confined to the stated mathematical class:

- Exact forward renewal transform and finite-prefix inverse
  `w_n=u_n-sum_(j<n)w_j u_(n-j)`; admissibility iff w>=0 and sum w<=1.
- Unique reachable-age hazards w_n/S_(n-1), with UNREACHABLE at zero survival;
  finite-prefix extensions and their distinct eventual intensities.
- A hard-dead-time example refutes universal direct replacement of normalized
  hazard by normalized all-pairs density, even with a known stationary rate.
- For h=a eta, the finite dilute bound
  `|u_k-h_k|<=a(1-S_(k-1))<=a[1-(1-a)^(k-1)]<=a^2(k-1)`.
- In the stipulated product model, feasible positive opportunity rates are
  exactly a in [max h,1] intersected with (0,1], with eta=h/a; zero cases
  remain explicit.
- Equal full pair laws and intensity for the periodic sets
  {0,1,4,6} and {0,1,3,7} modulo12, despite different first-gap laws.
  This makes the renewal premise indispensable for the inverse.

An intended counterexample surviving is a positive audit result for this
probe. No experimental paper, actual device, Born law or native physical
model is declared falsified. The probe is not a new L6 probability law for U.

## 2. Accepted code and public pin

The only executable scientific source is verify.py, Python standard library
with fractions.Fraction and exact integer operations, compatible with Python
3.10 or later. No randomness, numerical fit, plotting, external process,
external scientific package, network request or file data is used by it.
The immutable accepted source set is PREREG.md, PROOF.md and verify.py.
Commit, push and read back all three byte for byte at a full source pin before
execution or import. Static AST inspection is allowed and is not a run.

The scientific entry point is

```
python3 probes/P-REGISTRATION-PAIR-RECOVERY-1/verify.py
```

A completed audit writes one deterministic JSON line. Fractional witnesses are
serialized exactly as rational strings. EXPECTED.txt preserves the raw first
stdout. RUN.md records source pin/hashes, environment, command, exit status,
stderr and stdout bytes/hashes. No source repair, rebase, squash, amend or
force push is permitted after the pin. A precompletion failure consumes the
pin under POLICY.md; it cannot be silently fixed and rerun.

## 3. Carrier and finite census

The carrier is immutable rational tuples. Empty prefixes are admitted.
Malformed types and out-of-range hazards are rejected. No floating-point
coefficient is accepted as an exact rational input.

Freeze these finite families before execution:

1. Every hazard word of lengths 1..6 over {0,1/2,1}, and lengths 1..4 over
   {1/4,3/4}: 1,122 nonempty prefixes. Independently enumerate all 56,326
   associated binary event words. Compare total weight, first-gap and
   all-pairs occupancy with the recurrence and reachable inverse.
2. Every proposed u word of lengths 1..5 over {0,1/2,1}: 363 prefixes.
   Validate the reconstructed gap inequalities and round-trip every admitted
   case via a hazard representative, explicitly tagging unreachable ages.
3. For every hazard prefix in family 1 with positive final survival, compare
   proper residual extensions at N+1 and N+7: equal observed prefix and
   unequal mean gaps. Include the empty and all-zero boundary explicitly.
4. Hard-dead-time d=0..4, a in {1/4,1/2,3/4,1}, through lag24. Compare the
   recurrence with the gap and shifted-negative-binomial closed forms in
   PROOF.md. Include the d=1,a=1/2 counterexample, memoryless d=0, deterministic
   a=1 and the separately handled a=0 boundary.
5. For a in {1/4,1/2,3/4,1} and eta words of lengths1..5 over {0,1/2,1}, test
   every term of the dilute bound and the k=2 sharpness witness eta=(1,0).
6. Product ambiguity for h=(0,1/4,1/2,1/4) at a=1/2,3/4,1, with infeasible
   smaller a and zero-prefix controls. Memoryless normalized shapes also
   demonstrate the lost absolute scale.
7. The two period12 patterns: all12 overlap residues, intensity, first-gap
   vectors through12 and repeated-lag check0..48. Also compare first/second
   moments, triple111 and first-gap3 for fair three-bit words and even-parity
   words, with a registration anchored at zero.

Each assertion belongs to a named output category. Exact implementation
details and failure labels are frozen by the accepted verify.py bytes.
The finite census is an audit; general statements rest on PROOF.md.

## 4. Systematics, model assumptions and exposure

- The age-only independent restart rule is stipulated. Neither pair data nor
  a successful inverse proves that a physical source/detector is renewal.
- Hazard, first-gap weight, anchored pair density, stationary intensity and
  normalized pair shape are separate objects. Missing lags are not zero.
- UNREACHABLE is not zero efficiency. Silent finite prefixes do not determine
  an infinite silent future; a=0 cannot be normalized by a or its intensity.
- Stationary intensity does not imply pointwise convergence of pair density,
  particularly for deterministic periodic gaps. No finite reference bin is
  treated as an intensity calibration.
- The dilute bound is in units of the admitted Bernoulli opportunity rate,
  at a finite horizon. Physical binning and missed-arrival state changes are
  not silently absorbed into its assumptions.
- In the source-product interpretation missed opportunities do not change
  detector state. Additional memory, correlated light or electronics may
  change that model and require a separate gate.
- Primary Mark et al. arXiv:2407.20682v1 and its published conclusions,
  recovery table/figures and Zenodo12773197 metadata have been seen, as have
  metadata for a 2026 source candidate (Zenodo18662495). Their measurement
  payloads were not acquired or opened. This is not a blind study, data fit,
  independent experimental replication or a statistical significance test.
- No empirical count-bin independence, complete acquisition, photon
  attribution, detector-efficiency calibration or physical storage claim is
  made. No new data source is accepted in this probe.

## 5. Failure threshold and disposition

Threshold: exactly zero failed checks, exact rational equality or the stated
exact inequalities, exit0, empty stderr, one valid JSON line. A completed
mathematical failure remains visible in the output and is not repaired.
PASS means PROOF_AUDIT_PASS for the frozen mathematical targets, including
the intended counterexamples. A failed exact identity or boundary assertion
means FALSIFIED for the affected mathematical target, not an external device.

Required PR CI must run the unchanged verifier on x86_64 and aarch64 with
Python3.12 and reproduce EXPECTED.txt byte for byte; aggregate check must pass.
Canon, existing probes, owner schemas and workflows remain unchanged.

## 6. Action layer and physical decision

All formal executions occur in L1 rational coefficient/tree calculus.
The external registration interpretation is conditional and supplies no
L1-to-L5 or L1-to-L6 gate, probability law for U, physical detector
realization, empirical falsification, or canonical status promotion.

The successor decision is precise: direct all-pairs normalization requires
additional justification; exact inversion is available within its full
renewal input contract; outside it even full pair data can be nonidentifying.
The native physical source/record/occurrence obligations remain OPEN and
STOP-DEFINITION where their required physical inputs are absent.
