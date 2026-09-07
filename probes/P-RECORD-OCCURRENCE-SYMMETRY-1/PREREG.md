# P-RECORD-OCCURRENCE-SYMMETRY-1 preregistration

**FORMAL / PROOF-FIRST / RESULT-EXPOSED.**
Author: A. M. Thorn. Date: 2026-09-07.
Public lock: [#887](https://github.com/mathorn1973/twist-j/issues/887).
Branch: `probe/P-RECORD-OCCURRENCE-SYMMETRY-1`.

## Authority, prior evidence and execution custody

ACTIVE Public Canon v80; public main at claim time
`fc327267b0d445246d6efa419c40c38f550448c8`; tag target
`4577448dba85c492b27773a64e5fd557abc02b30`; content
`b00171ef21ecb0d905593224f66f5e8a0f6c28e5`; Canon SHA-256
`8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. Tag/content ancestry and hash were checked; the v80 publication
checks and current main check succeeded. Remote heads, open issues/PRs and
scientific namespaces were checked before issue #887 claimed this fresh name.

This follows the merged relational-reading note #884 and pair-selection
probe #886. The v80 occurrence proof already classifies chronological onset
laws and permutation scans. The native memory/history and entropy probes do
not supply a complete finite autonomous occurrence criterion. The new scope
is a general L1 selector/cycle/resource theorem, not another execution of
those probes or the physical definition lane #539. See PROOF.md section 5.

All candidate proofs and displayed witnesses are known before the pin. This
is result-exposed mathematical review, not a blind empirical prediction.
Commit and push PREREG.md, PROOF.md and accepted verify.py together, then
read back all three public files at that exact commit and match their hashes
before the first formal run. Only static parsing is allowed before the pin.
After it, no amendment, rebase, squash, force push, reuse or verifier repair.

## Field 1: exact claims and falsifiers

PROOF.md freezes the definitions and universal proofs. The targets are:

1. For finite G-sets R,E with E nonempty, equivariant selectors are classified
   by one fixed outcome of the ready stabilizer per ready orbit. Their count
   is the product of these fixed-set sizes. A fully symmetric ready state
   cannot select one element of a nontrivial transitive outcome set.
   Equivariant deterministic updates cannot shrink a stabilizer, and
   equivariant bijections preserve it exactly.
2. Invariant laws on a finite G-set are arbitrary mixtures of uniform orbit
   laws. Equivariant pushforward preserves invariance, and a transitive fine
   outcome action then gives uniform output and coarse cardinality ratios.
   An invariant initial ensemble is a separate sufficient premise.
3. For any finite nonempty Omega, permutation T and event map including
   SILENT, every-start accepted frequencies equal q iff every cycle has
   d_C>0 and m_(C,j)=q_j d_C. Silent cycles have NO_EVENT. Accepted-prefix
   discrepancy is strictly less than d_C; tick discrepancy less than l_C.
4. Stationary laws are exactly mu(x)=gamma_C/l_C on cycles. Their conditioned
   single-tick event laws have the stated gamma_C d_C/l_C mixture formula;
   every mixture of active cycle profiles is realized by some stationary law.
   Uniform stationary mass need not give every-start counting frequencies.
5. A deterministic closed finite model giving independent Bernoulli(p)
   k-blocks, 0<p<1, needs at least 2^k supported initial states. If its law is
   uniform on N states and p=a/b in lowest terms, b^k divides N. A reversible
   single-cycle b^k-state construction attains this bound, also gives the
   every-start a/b frequency, and fails independence through k+1 under the
   same uniform law. No finite closed autonomous model supplies all horizons.

An exact counterexample inside a frozen class falsifies its target. The
identity-dynamics and 0011 witnesses instead falsify the proposed stronger
implications from reversible symmetry/stationarity to path balance, and from
correct low-order frequencies/laws to full independence. These negative
implications are explicitly predicted, not reasons to exclude the witnesses.

## Field 2: accepted code and frozen finite audit

Command from the repository root:

```text
python3 probes/P-RECORD-OCCURRENCE-SYMMETRY-1/verify.py
```

The accepted code is the verify.py in this public pin. It uses Python's
standard library, integer comparisons and Fraction; no floats, randomness,
input files, repository reads, network or clocks. Its four finite audits are:

- Symmetric and cyclic permutation actions on d=1..4 labels, ready carriers
  E^k for k=0..3: all orbits/stabilizers, all representative outcome choices
  and their extension well-definedness, orbit-stabilizer sizes, orbit law and
  positive rank-weighted orbit-mixture pushforwards for k>=1. Exhaust all
  maps E^k->E for d<=3,k<=2 for the full symmetric action, using adjacent
  transpositions as generating covariance tests. Audit tuple reversal and
  two-tuple diagonal collapse stabilizers. Include the empty ready set.
- Every permutation on n=1..5 states and every ternary event assignment
  SILENT=-1, LOW=0, HIGH=1. Check each start by independent tick simulation
  over the common cycle-length lcm; compare its accepted profile and the
  all-cycle criterion against the global active counting target. Audit
  accepted horizons 1,d_C,2d_C+1 and tick horizons 0,n,2n+1. Test stationary
  mixtures with cycle weights l_C and 1,2,..., and the converse active-profile
  mixture with weights proportional to cycle indices plus one. No truncation
  is interpreted as proof of an infinite limit.
- Identity dynamics for d=2..6 under all label permutations and all initial
  states; constant three-output words and equality correlation. Exact cyclic
  one-, two- and three-block counts for 0011; 16^20=2^80.
- All maps from N=1..4 seeds to binary k-words for k=1..2, checking support
  and uniform-law necessary bounds for all reduced a/b with b=2..4. Check
  all-LOW reduced denominators for b=2..12, every coprime 0<a<b, k=1..6,
  and N=1..64. Construct word-graph Euler cycles for b=2..5,k=1..4; independently
  enumerate every cyclic k-letter window, verify the phase permutation is one
  reversible cycle, and check all binary windows of lengths 1..k for every
  coprime 0<a<b. Check frequency balance and the all-LOW failure at k+1.

All-domain conclusions rest on the written proofs, not finite extrapolation.

## Field 3: carriers and data

Finite group actions and literal finite functions, nonnegative real
probability vectors as conditional mathematical parameters, finite
permutations/cycles with declared event labels, rational Bernoulli parameters,
and finite word graphs. There is no external or experimental dataset.
The source (1,0,0,0) and its adopted QDD A=1,B=15 are a comparison instance
from v80; no amplitude or source effect is derived here. The construction
parameters a,b,k and the selected word order are explicit inputs.

## Field 4: systematics and controls

Execute in Linux or Linux-compatible WSL with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1. Standard-library Python >=3.10;
CI uses 3.12. Record the actual interpreter, platform and architecture.
Use a 600-second ceiling, require exit 0, empty stderr and exact UTF-8 stdout.

Controls distinguish empty ready from empty outcomes, one-label degeneracy,
fine-label action from coarse partition, initial-law invariance from map
covariance, stationary tick conditioning from first accepted hit, silent
cycles from zero-frequency branches, and every-start frequency from a
uniform-ensemble marginal. Uniform versus arbitrary seed laws have distinct
bounds. The closed finite autonomous state must include all memory and finite
clocks. Native U's unbounded counter, fresh inputs and unbounded record
carriers are outside that finite-state premise.

## Field 5: threshold and disposition

Zero exact mismatches. Preserve admitted mathematical counterexamples.
Timeout, source or pin defect, nonzero exit or uncompleted output is integrity
STOP, not physical falsification. Never repair accepted code under this name.
After a completed first run, append its exact EXPECTED.txt, RUN.md and
RESULT.md. The required x86_64 and aarch64 CI jobs must replay the pinned
verifier with byte-identical stdout, exit 0 and empty stderr. Proof review
and the finite audit are different evidence; passing code creates no
canonical status. Report negative implications at their exact declared scope.

## Field 6: action layer and nonclaims

Action layer: **L1 exact mathematics and symbolic models only**. No physical
L4 support, L5 record realization or L6 measure is adopted. No cross-layer
gate is executed. Independence is examined as an explicit hypothetical law,
not imposed on the QDD physical owner. The results neither derive nor falsify
Born's empirical rule and neither realize nor exclude a native-U apparatus.

Physical preparation, record ownership, symmetry action, apparatus class,
reset, occurrence and any environmental resources still need an independent
typed specification. Missing definitions remain STOP. Canon/Registry,
frontier, dependency, gate and release identities stay unchanged. A results
summary may update the motivating NON-CANONICAL note after execution.
