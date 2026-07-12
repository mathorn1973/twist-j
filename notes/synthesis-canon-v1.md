# Synthesis worklist (NON-CANONICAL)

Working notes of the Public Canon v1 synthesis. Nothing here is a
claim. Branch synthesis/canon-v1; session log at the bottom.

## Decisions

D1 basis frozen (see legacy/CUTOVER_AUDIT.md); D2 registry selection
rule; D3 neutral stable claim ids; D4 single Apache-2.0 license; D5
minimal initial reproductions: approved by the author 2026-07-12.
D6 cutover date: pending; set when Phase A is reviewable.

Standing rules of this synthesis: public statuses are conservative, at
most T in the genesis bundle, and internal sources keep their grades
in the cutover audit; no unproven independence claims (pi and ln phi
carry linear independence over the algebraic numbers only); a
status-labelled statement without a registry identifier is unfinished
draft material and must be registered with evidence, rewritten as a
definition or remark, or removed before the synthesis pull request
opens; every live registry row carries a concrete falsifier or a
decision condition, and check_canon.py rejects placeholders; a live
row whose decision condition cannot be stated faithfully is omitted
with a reason in the audit and queued here, never registered vaguely.

## Queue before the synthesis PR opens

1. Registry completion, cluster by cluster, each with evidence:
   Maxwell closure (next), alpha value (needs a high precision
   exact reproduction), cosmology register, coupling and metrology
   arc.
2. Deepen sections 14 and 15 from the sealed arc part bodies at the
   internal basis (they are stated here at frontier resolution).
3. Reconciliation audit rows for every added claim.
4. Deferred frontier rows, each returning only with a concrete
   falsifier or decision condition: W1-INTERFACE-PRINCIPLE,
   KERNEL-BRAID, TIMEQUANTUM-POTENTIAL, the internal O17 residual.
5. The pre PR inventory: sweep the Canon for every status-labelled
   statement without a registry identifier (grep for bracketed
   labels); each gets an identifier and registration, becomes a
   definition or remark, or is removed.
6. Full local check run, security audit, PR template fields.

## Two architecture witness

Recorded per push in the session log. Platforms are named neutrally:
operating system, architecture, Python version.

Recorded at the genesis push: Debian 13 x86_64 (Python 3.13.5), all
four reproductions byte identical against EXPECTED.txt, exit 0, empty
stderr; check_policy and check_canon (hardened) pass on that platform
(2026-07-12). Author platform Ubuntu 24.04 aarch64 (Python 3.12.3),
same result.

Recorded at the Born quartet push: Debian 13 x86_64 (Python 3.13.5),
all five reproductions byte identical against EXPECTED.txt, exit 0,
empty stderr; check_policy and check_canon (with the frontier
identifier parser) pass on that platform (2026-07-12). Author platform
Ubuntu 24.04 aarch64 (Python 3.12.3), same result.

Recorded at the Dirac ladder push: verifier 3240d355 and stdout
2f8d2036 byte identical on Ubuntu 24.04 aarch64 (Python 3.12.3) and
Debian 13 x86_64 (Python 3.13.5), 16/16, exit 0, empty stderr, both
runs recorded before the commit (2026-07-12). After the push, a
fresh checkout of the pushed head on Debian 13 x86_64 passed
check_policy, check_canon (60 claims), and all six reproductions
byte identical.

Color ladder staging candidate: verifier 5cd3a40c and stdout 9031fd6a,
12/12, exit 0, empty stderr in the pre-pin dry run. Formal records
begin only after the immutable GitHub candidate commit, through the
Phase A staging protocol in AGENTS.md; both architecture records are
pending at the candidate commit.

Gravity chain staging candidate: verifier e964fb6c and stdout
e74dd895, 12/12, exit 0, empty stderr in the pre-pin dry run, byte
identical on x86_64 and aarch64. Formal records begin only after the
immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Mass ladder staging candidate: verifier 68593371 and stdout
1ea07225, 8/8, exit 0, empty stderr in the pre-pin dry run, byte
identical on x86_64 and aarch64. Formal records begin only after the
immutable GitHub candidate commit, through the Phase A staging
protocol in AGENTS.md; both architecture records are pending at the
candidate commit.

Weinberg staging candidate: verifier cdff7689 and stdout eaeb163e,
6/6, exit 0, empty stderr in the pre-pin dry run, byte identical on
x86_64 and aarch64. Formal records begin only after the immutable
GitHub candidate commit, through the Phase A staging protocol in
AGENTS.md; both architecture records are pending at the candidate
commit.

## Session log

- s7 (2026-07-12): the Weinberg candidate: reproduce/weinberg
  (6/6: the face degree deg_f = Tr(J) = 3 on the power basis; the
  trace kernel of dimension 3 over Q and 125 = 5^3 points over F_5 by
  full enumeration, so B_quark = 1/3 = 1/dim ker(Tr); the tree value
  3/13 = deg_f/(V + 1) with V = 12 = d(d + 1) by two routes; the
  hypercharge law reproducing all seven standard model hypercharges
  exactly; the correction term phi^-4 = 5 - 3 phi, exactly positive,
  over 32 = 2^5; the parity of the committed form, pi even and delta
  free, with the single positive correction above the tree value at
  the form level). Three registry rows: WEINBERG-TREE T,
  HYPERCHARGE-LAW T, WEINBERG-FORM D (comparison fenced); registry 86
  claims. The audit omissions no longer list Weinberg. The cluster
  enters GitHub staging through the Phase A protocol.
- s6 (2026-07-12): the mass ladder candidate:
  reproduce/mass-ladder (8/8: the shared coefficient 89/5 = 18 - 1/p
  with 240 C = 4272; the exact exchange identity in Q, identically and
  on a rational sweep; the committed forms with their fenced sigma
  comparisons kept outside the witness; the proton as the homogeneous
  odd pi^5 carrier; the neutron as the unique mixed composite with
  Delta_EM open; the exact bridges xi phi^2 = 5, Q phi^2 = 2 pi,
  Q/xi = 2 pi/5; the algebraic side of the bridge defect, minimal
  polynomial x^2 - 18x + 36 irreducible; the parity law on thirteen
  named even entries and the three odd carriers at pi degrees 1, 3,
  5). Five registry rows: MU-TAU-COEFFICIENT T, MU-EXCHANGE-IDENTITY
  T, MASS-LADDER-FORMS D, PARITY-LAW T, BRIDGE-DEFECT T; registry 83
  claims. The audit omissions no longer list the mass ladder values.
  The cluster enters GitHub staging through the Phase A protocol.
- s5 (2026-07-12): the gravity chain candidate:
  reproduce/gravity-chain (12/12: the modulus chord J Jbar = 2 - phi =
  phi^-2 with N(J) = 1; the Kahler jet and the exact capacity monomial
  64 pi^3 phi^2, pi odd; the rank 1 lapse action closing the (00)
  algebra with lambda = 216 pi and H^2 = 72 pi rho; the three 2-planes
  coefficient; the Euler-Lagrange chain to the second Friedmann
  equation; the canonical Hamiltonian form; the forced fiber k_f = 1
  against G_nat = 27 = d^3 with V_cell = 864 pi; the fiber circle
  J = zeta (zeta + zeta^4); the exact bridge square g^2 = 1024 phi^4
  (3 - phi); the wall spelling at the equation layer). Three registry
  rows: KAHLER-CAPACITY T, FRW-CANONICAL-FORM T, GRAVITY-BRIDGE-LAW D
  (the equation layer; the SI value of G stays on the frontier);
  registry 78 claims. The audit omissions no longer list the gravity
  chain. The cluster enters GitHub staging through the Phase A
  protocol in AGENTS.md.
- s4 (2026-07-12): the color ladder candidate:
  reproduce/color-ladder (12/12 blocks, eleven rungs). Rungs 1 and 2
  close the D5 return group, integer mass law, torsors, holonomy,
  orientation, and the 3 = 1 + 2 dictionary. Rung 3 records the fired
  dynamical-color falsifier at F, then proves the 19200-element
  product-affine normalizer and reads its special-linear image as
  GL_2(F_5) at D. Rungs 4 to 11 close the 2I core, golden character
  table and spin lift, affine E8 and Catalan bridge, the rational
  Lucas fingerprint, the spectral class measure and invariant degrees,
  the Dickson ramified pair, Klein reduction and Artin-Schreier tower,
  and the integral lift. Fifteen registry rows: 12 T, 2 D, 1 F;
  registry 75 claims. The audit omissions no longer list the color
  ladder. The expensive 19200-candidate sweep was compressed without
  changing scope: five generators close to 40 x 480 and each
  generator permutes all 313 supports. The cluster now enters GitHub
  staging: commit the immutable candidate, record x86_64 and aarch64
  through the runner tool, validate both records, then fast-forward
  synthesis.
- s3 (2026-07-12): the Dirac ladder cluster:
  reproduce/dirac-ladder (16/16: the light cone pair with Pell parity;
  the spinor floor with the quartic irreducibility and the odd rung
  witness; the Fibonacci root with its Z conjugacy to the modulus
  carrier, the mod 5 towers with -I at half period, the J_4(2) Jordan
  block and an explicit 1-jet conjugator; the step form with
  coefficient set {1, i m}; the exact invariants, the mass shell, the
  rest coin of infinite order; the two distinct places with the
  Gaussian place swap; the checkerboard skeleton and Gauss tower; the
  fermionizer; the beat factorization; the Thue-Morse breath tower);
  twelve registry rows, 9 T and 3 D (the dictionary layer of the
  ladder enters at D, the first derived grade rows of the public
  registry); registry 60 claims; the audit omissions no longer list
  the Dirac ladder.
- s2a (2026-07-12): Born layer closed by three review fixes from the
  author: the half angle scope no longer counts the antipode (the
  normalized bisector exists exactly on the 11 non antipodal gated
  units; at u = -1 the bisector vanishes, the only square root of its
  norm is 0, not invertible); the order 16 minimality now excludes
  every smaller degree (16 divides none of 4, 24, 124); the audit no
  longer lists the Born quartet among omissions. New EXPECTED; both
  platform runs recorded before the commit: verifier cf6009aa and
  stdout 228e7335 byte identical on Ubuntu 24.04 aarch64 (Python
  3.12.3) and Debian 13 x86_64 (Python 3.13.5), 11/11, exit 0, empty
  stderr.
- s2 (2026-07-12): the frontier identifier parser in check_canon now
  rejects unregistered identifiers leading FRONTIER.md list items
  (negative tested); README gained the official channels and the
  candidate review note; the Born quartet cluster:
  reproduce/born-quartet (11/11: the cyclic Born unit group of order
  24, the half angle identity on every Born unit, the norm gate
  exactly on the squares with zeta_8 ungated, the normalized bisector
  witness on all gated units, both residual splits with their
  conjugation swaps, the integer spinor skeleton and its SL_2(F_25)
  shadow of order 8, the order staircase with exhaustive
  irreducibility); four registry rows at T; registry 48 claims.
- s1 (2026-07-12): gate hardening and genesis bundle. check_canon.py
  rejects placeholder falsifiers (concrete falsifier or decision
  condition required for every H, O, F row). The bundle: Canon
  candidate in nineteen sections with the concrete kernel definition
  in section 3; registry 44 claims (11 T with evidence, 8 by
  reproduction and 3 by inline derivation; 4 C, the census cluster;
  24 O and 5 H frontier rows, each with a concrete falsifier or
  decision condition); four reproduction witnesses: kernel 15/15,
  alpha-exact-lemma 5/5, born-faces 8/8, census 11/11 (including
  closure under both transitions and second window stability); four
  frontier rows explicitly omitted with reasons in the audit; core,
  frontier, changelog, SHA256SUMS, citation, status candidate line;
  basis frozen; audit mapping for all 44 rows; all checks green
  locally on Ubuntu 24.04 aarch64 (Python 3.12.3).
