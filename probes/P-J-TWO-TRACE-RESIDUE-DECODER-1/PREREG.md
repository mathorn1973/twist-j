# P-J-TWO-TRACE-RESIDUE-DECODER-1

PUBLIC formal probe. L1 only. Candidate-T proofs and candidate-C finite
audit until review and the required evidence gates; no Canon authority.
Owner: A. M. Thorn / thorn-jtrace-formal-20260929. Lock: issue #1283.
Date: 29 September 2026. Original work under Apache-2.0.

## 1. Basis, exposure and immutable inputs

Public Canon v93 is ACTIVE. Main basis:
789399eebba3ea17a2e59af237bb3280173fbff2.
Tag canon-v93: d708d887f3dbf92ae02115d92ecf12d581db72b5.
Content: 138eb9af93ca94d5f95531e46301ed23718fc07d.
Canon SHA-256: 9002c1c0f299f0226fa5ebc05747b0f0be1a11465279f35ee6e43a79f6ccaa21.
Canon bytes: 807444. Status, policy, agent manual, normative hashes,
ancestry, current ledger and required main workflow were checked.

This is a fresh formal successor to merged notes PR #1282 and its frozen
candidate pin 821090bc4daa55bb9974e3ec5a8e6af4d391a07a. The earlier results
and proofs are exposed. This is prospective reproduction and adversarial
audit, not blind discovery. Neither the note nor any sealed probe is resumed.

Dependencies: J-PROJECTIONS, J-STEP, J-UNIT-STRIP-NORMAL-FORM,
J-SCALAR-CODE-CAPACITY-3125 and U-COUNTER-REACHABLE-AMPLITUDE-CLASS,
at their registered L1 scopes. In particular, the conserved label map is
a bijection X_n -> F5^5 for every n>=3, not merely onto over all times.
No numerical embedding, external data or external Python package is used.

Freeze this preregistration before commissioning the independent breaker.
Then freeze PREREG.md, PROOF.md, REVIEW.md, decoder.py, primary.py,
break.py and verify.py together in one public Git pin before execution.
verify.py binds the other six input files by their SHA-256 hashes. Its own
hash and pin are checked by the repository runner. Compilation and static
review only may precede the pin. Read back all seven files before any run.

## 2. Carrier, equation and equality

O=Z[zeta], zeta^4+zeta^3+zeta^2+zeta+1=0; J=1+zeta^2;
phi=-zeta^2-zeta^3. Scalars are four integers in the ordered basis
(1,zeta,zeta^2,zeta^3); equality means coefficient equality.
For nonzero alpha define

    alpha*bar(alpha)=u+v*phi,
    A=|sigma_1(alpha)|^2, B=|sigma_2(alpha)|^2,
    N(alpha)=A*B=u^2+u*v-v^2,
    S0=S(alpha)=Tr(alpha*bar(alpha))/2=A+B,
    S1=S(J*alpha),
    D_m(alpha)=(S0,S1,alpha mod mO).

Primary domain: all nonzero alpha in O with N(alpha)<=941, including every
integer power of J. Residues are four canonical integers from 0 to m-1.
The two traces are exact, unbounded integers at a stipulated PURE J step.
An affine step J*alpha+d, approximate traces, or a physical detector changes
the contract.

## 3. Frozen mathematical claims

A. Reconstruct u=(S0+S1)/5 and v=(3*S0-2*S1)/5. The trace-pair lattice
is S0+S1=0 mod5; membership alone is not scalar realizability. Prove
N=(3*S0*S1-S0^2-S1^2)/5 and S_(n+2)=3*S_(n+1)-S_n for all integer n.

B. For all integers X,m>=1, D_m is injective on 0<N<=X whenever
m^4>16X. This is sufficient, not minimal among arbitrary moduli.

C. The oriented J strip 1<=A/B<phi^4 is exactly 0<=v<u, equivalently
2*S0<3*S1 and 2*S1<=3*S0. Each J orbit has one strip representative.
The decoder must terminate on every syntactically admitted input, either
returning exactly alpha, its strip representative beta and integer k with
alpha=J^k*beta, or rejecting the input as outside the exact D_25 image.
The normalized coefficient box [-8,8]^4 is proved, never tuned to an audit.

D. Let B_X be the COMPLETE oriented strip with 0<N<=X. In the reader
class R(n,x)=J^n*G(ell_n(x)), G is nonzero integral and every conserved label
is available at every n>=3. The sole observed datum is D_m(R(n,x)); the
observer is NOT separately supplied n. Require injectivity across the union
of sheets n>=3, not merely at fixed n. The arithmetic codebook capacity
is K_m(X)=|D_m(B_X)|, including arbitrary J shifts of the codebook.
The maximum usable subset of the native 3125-label alphabet has size
min(3125,K_m(X)); all native labels are possible exactly when K_m(X)>=3125.
Supplying (n,D_m), restricting observation times or changing the reader is
outside this capacity assertion.

E. At X=941, verify the exposed exact values |B_940|=3110, |B_941|=3150,
145 trace-pair classes, K_5=2603 and K_25=3150. The first D_5 collision
norm is 55. The explicit pair (0,1,1,-2), (0,1,1,3) has u=7,v=1,
(S0,S1)=(15,20), and difference 5*zeta^3. The minimum full 5^r-residue
depth for 3125 labels is r=2 in D's class only; no partial-refinement or
other-observable minimality is asserted. The complete trace stream adds
no information to its first two entries.

## 4. Accepted code and complete finite audit

decoder.py and primary.py preserve the note's integer inverse and primary
audit code; primary.py is the note's verify.py under an explicit new name.
The new wrapper verify.py runs that audit and the newly authored break.py,
checks their complete strip digests and census data, and asserts the frozen
exposed counts. It imports only local pinned modules and the standard library.

Primary: scan all 83521 vectors in [-8,8]^4; test 103950 round trips for
all 3150 strip representatives at k=-16,...,16; 40 stress cases for the first
ten lexicographically sorted representatives and k=-1024,-257,257,1024;
the twelve existing invalid-data inputs, both half-open strip endpoints,
the affine-step negative control and valid-to-valid corruption control.
The latter explicitly forbids a general error-correction claim.

Independent-agent break.py is authored from THIS preregistration only,
without reading decoder.py, primary.py, verify.py, the old break.py or their
outputs. Its source is frozen before comparison. Known target counts above
are disclosed, so result blinding is not claimed. It uses its own exact ring
arithmetic and tests:

1. Complete larger box [-9,9]^4 (130321 vectors), finding the entire strip.
2. Trace/norm identities by cyclotomic multiplication and Galois actions;
   all J/J^-1 basis identities and both strip boundaries.
3. Its own inverse/normalization for every strip representative at exponents
   -37,-2,0,3,41; exactly 15750 round trips, with full coefficient equality.
4. Every colliding unordered D_5 pair in that strip; check divisibility of
   its difference by 5, and 5^4<=N(difference)<=16*N(alpha).
5. The complete census below, not a sample. No code outside this pin executes.

The independent routine run_audit() returns a JSON-serializable dictionary
with keys summary, scanned, roundtrips and collision_differences. summary has:
bound, strip_count, strip_below, strip_sha256, max_abs_coefficient,
trace_pair_count, mod5_key_count, mod25_key_count, mod5_collision_groups,
mod5_max_fibre, mod5_capacity_shortfall, mod5_first_collision.
The first collision is the lexicographically minimum tuple
(norm, key, left, right), where each group and the strip are lexicographically
sorted, key=(S0,S1,r0,r1,r2,r3), and left/right are its first two scalars.
mod5_first_collision is {norm,key,left,right}. The strip digest is SHA-256
of compact json.dumps(sorted four-integer lists, separators=(',',':'))
encoded as UTF-8, without trailing newline. Tuples and lists serialize alike.
All other summary names have their literal meaning; strip_below means N<=940.
The wrapper compares complete normalized summary JSON, not decimal witnesses.

## 5. Execution, output and fixed failures

From a clean checkout of the public pin, follow AGENTS.md section 6 for the
first local run, capture exact stdout and stderr, and record the flat RUN.md
fields required by tools/check_verifier.py. Deterministic environment:
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1.
The current repository runner's per-verifier timeout is 600 seconds. Use
that same budget for the first local run. Command:

    python3 probes/P-J-TWO-TRACE-RESIDUE-DECODER-1/verify.py

Then use tools/check_verifier.py --base with the frozen main basis and the
ordinary required Python 3.12 GitHub x86_64/aarch64 jobs. Both architectures
must return exit zero, empty stderr and exact EXPECTED.txt byte identity.
No local x86_64 run alone supplies the two-architecture gate.

Zero tolerance. Preserve any identity, injectivity, normalization, image,
completeness, collision-capacity or frozen-count mismatch. Never relax a
threshold, rewrite pinned inputs or select a favorable subdomain after a
failure. A code failure with no completed record is disposed of under the
repository abandoned-pin rule; an actual fired mathematical falsifier is
recorded as such. Hash/custody, authority and missing-evidence faults STOP.

## 6. Scientific ceiling and exclusions

The infinite-domain statements require the written proof and independent
mathematical review. The finite capacities/minimum consume the exhaustive
audits and the required two-architecture replay. REVIEW.md discloses agent
exposure and does not call a same-code rerun independent confirmation.
RESULT.md must distinguish proof, finite computation and repository integrity.

No Canon, Registry, Frontier, GATES, workflow, existing note or existing probe
changes. No adopted physical apparatus, preparation, phase selection, event,
occurrence, persistence/reset, native-source completeness, SI scale, physical
clock, photon/P1, RH or unnamed L1-L6 lift. Two-architecture success is evidence
for a later separate fold, not an automatic Canon promotion.
