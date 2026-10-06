# Complete source-table contact and reader classification

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Candidate: C-CONTACT-INTERFACE-CLASSIFICATION-N. Public owner lock: #1396.
Disposition: analytical classification complete; exact local audit PASS;
public integration and any promotion remain separate.

## 1. Main finding

The frozen source-table restrictions permit exactly four complete contact
laws. They do not select the supplied v100 law. The marked reader task is
more rigid: every admitted reader table is obtained from the supplied one
by the explicitly frozen q translations and internal reference relabelings.
These are conditional algebraic facts about the declared classes, not
independent admission of their premises.

Let h be the declared polarized determinant reading, I=b_x b_y and
tau_i=e_i d_i. The control class contains every globally reversible table

    W(s,eta)=(I^a(h,eta) s, beta(h,eta)),

with arbitrary binary a,beta on F5 times {0,1}. The h=0 branch is
unrestricted; pointwise involutivity is not an admission requirement.
There are exactly 4608 such complete W maps, of which 600 are involutions.

Every complete K_(W,i)=[W I W^-1,tau_i] restores all coordinates except
q_i, on which it acts by q_i -> q_i+3 chi(h). The four laws are:

| chi(1)chi(2) | chi(h) in F5 | All W | Involutive W |
|---|---|---:|---:|
| 00 | 1-h^4 | 512 | 24 |
| 01 | 1+2h^2+2h^4 | 1024 | 96 |
| 10 | 1+3h^2+2h^4 | 1024 | 96 |
| 11 | 1 | 2048 | 384 |

All have chi(0)=1 and chi(-h)=chi(h). Their complete action is independent
of occupied eta. Their inverse subtracts 3 chi(h). The v100 W_b is the
00 witness, with literal table ID 0102023131; it is one of 24 involutive
controls with the same full contact endpoint. Requiring W itself to be
unique is therefore stronger than requiring the contact law to be selected.

The analytical mechanism is C_S4(J) times S4 times S4, with an eight-element
centralizer on h=0 and independent S4 choices on the two nonzero sign pairs.
Conjugates of the sign flip are exactly the three four-point matchings.
Two matchings invert the native q coordinates and one does not. The
commutator retains that single distinction on each sign pair. The proof
uses the full source identity I tau_i I=tau_i^-1 and explicitly covers
states fixed by I; it does not assume that tau preserves a chosen I orbit.

## 2. Reader classification and occupied memory

Each P_q permutes the marked active labels {0,1,2} and fixes native r=3,4.
All and only the tables satisfying

    P_(q+3)^-1 P_q(0)=1 for every q

are classified. Writing a_q=P_q(0) gives P_q(1)=a_(q+2), and the third
image is forced. The tables are exactly the proper three-colorings of
the five-cycle q -> q+2. This proves the complete census:

| Comparison | Result |
|---|---:|
| Literal admitted P tables | 30 |
| Pointwise involutive P tables | 5 |
| Literal complete endpoint maps, including occupied r | 5 |
| P tables for each literal complete endpoint | 6 |
| Table orbits under q translation | 6 |
| Involutive-table orbits under q translation | 1 |
| Endpoint orbits under q translation | 1 |
| Table orbits under internal S3 relabeling | 5 |
| Table orbits under q translation times internal S3 | 1 |

Full endpoint equality holds exactly when P'_q=L P_q for one common
L in S3. These internal relabelings cancel from the full endpoint, even
on occupied references, but do not preserve pointwise involutivity.
Each endpoint has exactly one pointwise-involutive representative.
The five endpoint maps differ on occupied r and are conjugate by actual
native q translation. All stated actions and stabilizers are proved in
PROOF.md; no physical-equivalence statement is added to these algebraic
comparisons.

For any admitted contact and reader the full paired endpoint is

    q' = q+3 chi(h),
    r' = P_(q')^-1 P_q(r),

with all other coordinates unchanged. Its inverse is

    q = q'-3 chi(h),
    r = P_q^-1 P_(q')(r').

There are twenty complete paired maps, four laws times five occupied
endpoint types. Their prepared outputs reduce to the four laws:
r=0 gives r'=chi(h), for every unknown q. Two separate ready queries at
h=1 and h=2 distinguish them in the frozen query class. One binary query
cannot distinguish four laws. This count supplies no preparation, reset,
detector or archive. The existing three-state minimum is not claimed anew.

## 3. Evidence and independence

The full-carrier argument is in PROOF.md. PROOF-CHECK.md was derived in
a separate agent context before its author read PROOF.md. REVIEW.md
then records a line-by-line review of the exact proof pin. Two wording
corrections were requested and resolved; neither changed the mathematics
or membership classes. The final reviewed proof SHA-256 is
8c7de381aab7fddfd151a0b63dc7fecee961fa5679e18329c20da7dbc1541234.

The primary verifier and independent breaker were both Git-frozen before
either execution. The breaker received no primary code, counts or outputs
before its own pin. The primary constructs every control from orbit
permutations and inspects all 6^5 reference tables. The breaker scans all
4^10 raw control tables using only bijectivity for admission and constructs
readers independently from all 3^5 ready-column assignments. Its complete
reduction is proved in the module documentation and independently in the
analytical notes. Neither program imports a repository verifier.

Both programs audit all 15625 native cell inputs and all 390625 piston
pairs. Each checks all 4608 admitted controls on both q ports, both eta
layers and every pair of q values in the finite lift. Each also directly
replays the native contact and inverse for the frozen 460800 full-state
witness cases. Those witness cases fix q_other and both references as
specified in PREREG.md; they are not an enumeration of all 488281250
states of X. The proof transfers the result to the complete carrier.
The breaker additionally checks every I-fixed data point through all
eight zero-branch controls and both bit values. Both methods inspect all
admitted reader tables and their full occupied-reference inverses and
frozen equivalences.

The first primary run took 15.763834233 seconds; the first breaker run
took 7.844376484 seconds, under the separately enforced 180-second limit.
Both returned exit 0, empty stderr and the same 571 stdout bytes:

    stdout SHA-256:
    4480997f001ee8781237422e44a66aaf31a46a8a076bd0e7fa50b007721b22ee
    control census SHA-256:
    83bfd84ee71a9eb13a0b179175f8fb75e57d47920db7858853c96deaa7affe59
    reader census SHA-256:
    f721d7500218861fd4580c6b0576b74430fffc898f8e6a2a1992f7307bdea3eb

There was no failed first run, corrective implementation change or rerun.
Both executions used the same x86_64 architecture and CPython 3.12.14.
These timings measure audit programs, not the length or implementation
cost of T_alg or V.

The independent implementation and proof review were produced in separate
agent contexts within this coordinated session. They are not an external
human review or evidence from a second architecture. The analytical proof
supports candidate-T within these notes; finite executions support only
candidate-C. The actual execution record is RUN.md. Ordinary notes CI
does not execute these scientific programs as a public two-architecture
gate.

## 4. What the result changes and leaves open

The contact-law ambiguity has a precise two-bit description once the
declared h,I and table-dependence premises are fixed. The v100 response
requires both nonzero sign pairs to be inactive. The source identities
alone permit the other three choices as well. An admission argument must
therefore justify that restriction or an appropriate independently
justified equivalence; another existence construction in this class does
not select it. The larger choices of actual W/P tables and five occupied
endpoint types remain explicitly counted.

This study was motivated retrospectively by the known v100 interface.
Neither the table class nor the marked reader experiment has been
independently selected physically. No result about all possible native
controls or apparatus classes is asserted. C, W_a, preparation, fixed
endpoint interpretation and their admission remain outside the note.
Equality of contact or reader endpoints does not identify W prefixes,
the compiled T_alg word, its q lift or replacements inside V.

No Canon, registry, frontier, gate, sealed probe, workflow or release is
changed. QUADRATIC-MEMORY-NATIVE-CONTACT remains O; there is no new layer
lift, characteristic-zero readout, occurrence law or empirical number.
The proposed later disposition is recorded in
PROMO-C-CONTACT-INTERFACE-CLASSIFICATION-N.md.
