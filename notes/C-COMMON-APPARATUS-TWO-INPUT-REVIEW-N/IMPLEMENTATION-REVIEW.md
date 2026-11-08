# Independent implementation review of PR 1871

Status: NON-CANONICAL / L1 / candidate-C finite evidence.
Target: PR 1871, head `26731e2bd7f1394b4d274528525e6d78cbe6bbf9`.
Probe: P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1.
Review owner: child session `/root/synthesis_breaker`.

## Verdict

The independently reconstructed program passes the frozen implementation
attack on all 100 ordered input pairs. No trajectory, invariant, reader,
timing, resource-disposition, count or inverse falsifier fired. After the
independent run finished, its actual word and outputs also matched the
author's pinned evidence at the exact target head.

The demonstrated behavior is two independently prepared inputs processed
through the same read core under one fixed mixed contact/SWAP program, with
both experiments' records retained. It uses supplied input cartridges, a
fixed schedule, four fresh memory banks and five explicitly supplied swaps.
It does not regenerate those banks or close a Canon owner.

## Exposure and code independence

The user and PR announcement disclosed the successful outcome, domain,
counts and output fingerprints. This is result-exposed review, not blind
discovery. Before writing and freezing review.py, the checker writer read
only the target CONTRACT.md, PROOF.md, PREREG.md, SOURCE-MAP.md and
PROVENANCE.md, plus the independently owned review preregistration.

The writer did not read or import target verify.py, EXPECTED.txt,
WORD535.txt or scientific logs before the independent source freeze or
before completion of its first scientific execution. The code uses its own
rho-basis arithmetic and reconstructs the oriented word from the displayed
block equations. It does not merely run the author verifier or assign
expected macro transitions to the executed array.

The independent public source pin is
`8199bb6297178ebeb001820d51b1a3882796ba29`. Public byte-identical readback
preceded execution. Its frozen hashes are:

| File | SHA-256 |
|---|---|
| PREREG.md | fcbdd315cb889a9e30aaccf62ff142cd634370e094b2090a7232103f3ea2ac90 |
| review.py | e615346185100da3aa68bc5d6432ac5781752ce16311a97cac71378586de1eb8 |
| REVIEW-SCOPE.md | 0e9a48d6d5c41dc2def54a911c45e8a3aa8e1e6673d2b99d6c98ebb71b75f482 |

Only syntax compilation, hashing and static inspection occurred before the
pin. The frozen code and scope were not edited after execution. The target
author's executable and output were opened only after the independent run
completed, for static comparison and output-format reconciliation.

## Independent arithmetic and complete checkpoints

The implementation uses `(1,rho,rho^2,rho^3)`, rho=j^2. Primitive rotation
uses an integer matrix; general multiplication uses cyclic convolution
followed by Phi_5 reduction. Both agree on every distinct contact difference.
The Gram form evaluates Q independently of the target's j-basis formula.
Hermitian conjugation is also evaluated explicitly in this independent
basis.

Every reached distinct ordered contact pair preserves its exact sum,
Hermitian account, Q and both labelled residues, and passes C^5=id and the
four-contact inverse. There were 58 such pairs, including pairs from the
separate source fixture and the inverse trajectories. Every reached loading
swap exchanges equal residues and preserves both complete pair accounts.

Expected states come from analytic source and clock phases, the declared
event/selector law and the bank alphabet. The actual array traverses every
primitive contact. Every complete R, S and reload checkpoint compares all
56 labelled coordinates. It also checks the ring sum 6, Q=156, the complete
labelled residue vector and the full Hermitian account. The latter is
`(96,0,36,36)` in the rho basis, equivalently
`60-36*j^2-36*j^3` in the j basis.

Both R calls restore their presented source and clock. Within one S, their
source phases are a and a-1 and their clocks are the same. The completed S
has source phase a+1 and clock phase k+1. The completed reload parks the
actual spent first source Y_(n+10), not the original Y_n. All these are
actual full-state checks, not assumed substitutions in the trajectory.

## Finite execution and counts

| Item | Independently checked total |
|---|---:|
| Ordered input pairs | 100 |
| Complete R checkpoints | 4000 |
| Complete S checkpoints | 2000 |
| Complete reload checkpoints | 100 |
| Designated events | 600 |
| Complete native inverse restorations | 100 |
| Trajectory contacts, forward plus inverse | 5,350,000 |
| Supplied swaps, forward plus inverse | 1000 |
| Separate analytic source-cycle fixture contacts | 18 |

The eighteen source-fixture contacts and local pair-identity calculations
are excluded from the trajectory count. Each forward trajectory has 10,700
contacts and five swaps; its inverse has 42,800 contacts and five swaps.
The inverse actually reverses the entire mixed word and applies four
contacts per reversed contact edge. All 56 coordinates return exactly.

All 46 designated auxiliary addresses have the same initial values and
account 128 for every input pair. The two allocated five-slot input
cartridges each have account 14. The domain is the full Cartesian product
of the two ten-input families; the second input is not selected from the
first result. Both are supplied before execution starts.

Stage-A support excludes every second-stage memory and queued-input address.
Stage-B support excludes the first-stage archives and parked old input.
Reload swaps touch only the two input cartridges. These structural support
checks prove literal retention inside the disjoint regions, and the reached
values are also checked at every full checkpoint. Within an active stage,
retention is asserted at complete R/S boundaries, not at each internal
contact of a read.

The event detector counts only the designated first contact of an active R,
requiring the actual marker change 0->u there. It does not count internal
marker motion as extra events. All six onsets and completions per input
pair have the correct contact and all-operation ordinals. The within-stage
gaps are 804 or 4011 contacts; stage-B offsets are 5350 contacts or 5355
mixed operations. No physical duration is inferred.

## Current-state reader attack

The independent reader is passed only the forty actual bank coordinates
11..50. It receives no source, queued or parked input, clock, event counter,
original label or expected answer. Each bank must exactly equal one M[p].
Blank M_empty is rejected; M[0] is a present zero-labelled record.

Differences 1 and 3 recover source inputs 0 and 1, respectively, and minus
the first label recovers each initial clock. The independent reader recovers
all four input labels on all 100 endpoints, and all 100 actual four-bank
codes are distinct.

All 24 standalone invalid inputs frozen in REVIEW-SCOPE.md are rejected:
all-blank and individually blank banks, two occupied pairs, zeroed or
orientation-reversed malformed coordinates, the three invalid differences
for either bank pair, and a truncated 39-coordinate interface. This is a
finite interface mutation audit; it is not a claim that these malformed
values are reachable detector states.

## Own run record

The root executed the frozen independent source with this command:

    python3 -u review_1871/review.py --dump-data review_1871/review-dump.json

Environment: Linux, x86_64, Python 3.12.14. Start:
`2026-11-03T07:28:05.229947Z`. Exit code was zero and stderr was empty.
The 1906-byte stdout EXPECTED.txt has SHA-256
`f98d6735fd07808fe3446fa7ca33ded877fa928537fb44bf672a3b3a6b443cb0`.
Engineering elapsed time was 2.108806592000292 seconds. This is run metadata,
not a physical interval or scientific performance threshold.

REVIEW-SCOPE.md fixes the independent canonical serializers. Its endpoint
payload is 63,981 bytes and its combined checkpoint payload is 3,966,631
bytes. Their independent digests remain unchanged; the scratch dump is
comparison material, not an input to the scientific checker.

## Post-run comparison with the exact author evidence

After the independent execution completed, these target bytes were fetched
at head `26731e2bd7f1394b4d274528525e6d78cbe6bbf9` and verified:

| Target file | SHA-256 |
|---|---|
| verify.py | fbee888930ac613c517c2ec0b4312c5b7b9860d1e1f21be21e9d12ba03cf0884 |
| EXPECTED.txt | 40a71401c28406605aea666a40fec5f773505d3a5b56b82897cdc09ad4c1952c |
| WORD535.txt | ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b |

The independently expanded S is exactly the same 535 oriented contacts as
the normative one-based literal word after subtracting one from each address.
The comparison checks order, multiplicity and orientation, not just support.

The independent and author hashes initially differ because the serializers
were frozen independently. compare_after_run.py reads only the already
observed independent scratch dump and exact pinned target files. It imports
or executes neither scientific implementation and does not rerun trajectories.
It converts the independent values to the author's concatenated compact-JSON
streams. S checkpoint numbering becomes tick+1. Event dictionaries use the
recorded ordinals; pre-read selectors are recovered from preceding actual
R/S/reload states and the declared initial selector A.

All seven published target digests then agree exactly:

| Published fingerprint | Result |
|---|---|
| Complete mixed program | identical |
| All 100 complete endpoints | identical |
| All 4000 complete R states | identical |
| All 2000 complete S states | identical |
| All 100 complete reload states | identical |
| All designated event records | identical |
| All actual bank codes and decoded inputs | identical |

COMPARISON.json preserves the converted hashes, matching counts and exact
source pins. The sorted actual record quadruples also equal the author's
published list. No frozen code, expected state or stdout was rewritten to
obtain this agreement.

## Editorial clarification and remaining scope

Ten addresses are allocated to the two input systems, while eight of their
coordinate values actually vary on the declared family: the third source
coordinate of each initially loaded Y_0/Y_1 is always zero. Wording that
literally says all ten coordinates vary should say ten allocated input
coordinates. The 46 designated common auxiliaries, their account 128 and
the complete accounting remain correct. This does not change a trajectory,
threshold, code or required resource allocation.

The witness supplies finite funded reuse of the same core with an independent
queued input and retained first records. Fresh memory falls from four banks
to zero. Each used bank still has account 30; freshness is not consumed
energy. Returning the selector to A does not make a used bank fresh.
The complete inverse restores preparation by removing records and is not
retention-preserving renewal.

This review does not require a raw-input loader, contact-only SWAP,
unbounded memory renewal or arbitrary external post-start choices that the
frozen contract does not assert. Conversely it does not infer any of them.
The supplied swaps, schedule, initial cartridges and finite two-experiment
horizon stay explicit. General interval measurement, physical energy/time,
native U and occurrence remain outside scope.

This independent execution is one x86_64 lane. Any two-architecture replay
of the target's exact pinned verifier and EXPECTED bytes must be established
separately from official CI evidence. Implementation agreement, that CI gate
and mathematical acceptance are distinct. No registry row, original probe,
PR merge or Canon status is changed by this review.
