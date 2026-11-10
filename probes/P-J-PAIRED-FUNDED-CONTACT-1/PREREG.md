# P-J-PAIRED-FUNDED-CONTACT-1

NON-CANONICAL / L1. Proposed law and reading: candidate-D. Analytical
statements: candidate-T conditional on the declared model. Finite audit:
candidate-C, with no canonical promotion through this probe.
Owner: A. M. Thorn, paired-J funding session, 2026-11-09.
Reservation: https://github.com/mathorn1973/twist-j/issues/1968.
Base: 629a9d4058501f938dc91a690c3eb59a914493d1, ACTIVE Public Canon v110.
Content: c8197bcc807de1f62248463aec77f7ac7ab46f85.

## Question, equation and carrier

Does one total integer four-slot rule realize a nontrivial relative J step
paid by a second actual pair, preserving the full Hermitian account and both
pair sums, with an exact inverse on every admitted or refused state?

The complete carrier is O^4, O=Z[j], Phi_5(j)=0. Set rho=j^2,
J=1+rho, Jinv=-j-j^2, phi=-j^2-j^3 and t=J*conjugate(J)=2-phi.
A cell is its four integer coefficients in (1,j,j^2,j^3). Set
h(x)=x*conjugate(x), q(x)=Tr(h(x))/2 and E(z)=sum_i q(z_i).
All four slots count, including the payer. No uncounted scalar store,
control bit, discarded register or outside work source is present.

For z=(x,y,u,v), refuse unchanged if either x-y or u-v is outside 2O.
Otherwise write c=(x+y)/2, d=(x-y)/2, e=(u+v)/2, f=(u-v)/2.
If d=f=0, fix the state. For the remaining parity-admitted states define

    Dplus:  h(f)=t*h(d)
    Dminus: h(d)=t*h(f).

On Dplus send (c,d,e,f) to (c,J*d,e,Jinv*f). On Dminus send it to
(c,Jinv*d,e,J*f). On neither surface use identity. Return the four slots
(c+d,c-d,e+f,e-f) with the new differences. Exact equality in O decides
these guards, without real approximations. The two nonzero surfaces are
predicted to be disjoint and exchanged by the two inverse branches.

The rule is a new supplied four-slot primitive. It is not asserted to be
compiled from the old rho contacts, or selected by the native U clock. The
balance surface is necessary and sufficient for the specified reciprocal
pair of relative steps to conserve the full Hermitian sum. No completeness
claim over every conceivable conservative contact is made.

## Frozen analytical predictions and witnesses

PROOF.md proves integrality, complete involution, both pair sums, full H and
proper E conservation, conservation of each relative difference norm and
2-adic valuation, and exact exchange of h(d),h(f). It proves that simply
applying J and Jinv unconditionally is not conservative, while accepting
only Dplus and fixing everything else is not injective. Thus refusal and
reverse orientation must be accounted for, not added after observing data.

For a in {-1,+1}, primary blank-target preparations are

    (2a,0,2 rho J,0),     accounts (8,12)->(10,10), total 20;
    (2a,0,rho J,-rho J),  accounts (8,6)->(10,4), total 14.

Their target output is (a(1+J),a(1-J)); the common payer is independent of a.
The second example uses the sharp initial payer account 6 within this fixed
reciprocal/full-H model for that target pair. It is not a minimum over other
payer laws. A centered example (a,-a,rho J,-rho J) has accounts
(4,6)->(6,4), total 10. In all examples applying the same rule again restores
all coordinates. The payer preparation is supplied and independent of a.
The sign read Tr(a(1-J))=a is only the one-step target
reading. No record retention beyond the second invocation is claimed.

For each fixed K>=1 a supplied word using one target pair (a,-a) and K
payer pairs (rho^i J^i,-rho^i J^i), i=1..K, advances the target to
(a J^K,-a J^K). It contacts successive payer pairs once and leaves all
others unchanged. Total initial E=2+2 L_(2K+1), L_0=2,L_1=1. Exact reverse
order restores every target and payer. This is finite prepared stock and a
supplied schedule, not automatic selection or perpetual operation.

For scalar h(z)=A+B phi, define T=2A+B=q(z) and the exact symbolic
X=sqrt(5)B. Then T^2-X^2=4 N_K/Q(z), and J multiplication sends
(T,B) to ((3T-5B)/2,(-T+3B)/2). This is an algebraic 1+1 Lorentz reading
with rapidity magnitude 2 log(phi), distinct from the existing amplitude
count convention. No physical momentum, mass, proper time, constant
acceleration, gravity, equivalence principle or radiation is inferred.

The blank-target witness changes the complete residue histogram modulo
1-j. It therefore cannot be a word of the original rho contacts and
whole-slot permutations on the same four slots, or with all added slots
restored. New primitive admission remains explicit.

## Exact verifier and frozen inventory

Accepted source is verify.py. The full source set is PREREG.md, PROOF.md
and verify.py. Commit, publish and read back all three before the first
scientific run. No import, execution or scientific dry run precedes that
pin. Static syntax compilation and hashing are permitted.

The verifier uses standard-library integer arithmetic only. Its polynomial
four-coefficient calculation and five-coefficient cyclic calculation are
both written by the same author. Agreement is a representation cross-check,
NOT blind or independently authored confirmation. Scientific outputs and
new SHA-256 digests are not known at preregistration.

The accepted inventory is fixed:

1. All 625 cells in {-2,-1,0,1,2}^4: full h and q, J inverse,
   real-field coordinates, norm and Lorentz identities in both representations.
2. All 6561 four-slot states over the ordered alphabet
   [0,1,-1,j,-j,j^2,-j^2,j^3,-j^3]: complete map, guard classification,
   full invariants, relative norm/valuation and exact involution.
3. All d,f in {-1,0,1}^4, c in {0,1}, e in {0,j}: 26244 centered states,
   the same complete checks plus both necessity/sufficiency balance tests
   for the unconditional forward/inverse reciprocal proposals.
4. All 80 nonzero d in {-1,0,1}^4, epsilon in {-1,+1}, ell=0..4,
   c in {0,1}, e in {0,j}, with f=epsilon*rho^ell*Jd: 3200 matched
   forward states and their inverse images. Exact forward branch and
   half-difference formulas must hold throughout.
5. Both signs of all three explicit prepared examples, with 16 repeated
   applications of the same rule and the stated account transfers.
6. K=1..15 and both signs: all 240 forward steps and all 240 backward
   steps of the supplied finite-stock word, complete state restoration,
   every total H/E and the formula E=2+2 L_(2K+1).
7. k=0..64: J^k norm-one, q(J^k)=L_(2k), Lorentz recurrence;
   k=1..13 traces of 1-J^k equal the disclosed prefix
   (1,3,7,15,26,33,22,-25,-119,-242,-318,-195,326).
8. Exact negative controls: unfunded (2,0,0,0) reciprocal proposal changes
   E from 8 to 10; forward-only balance/refusal has two preimages;
   source/payer residue histogram changes in the stated new primitive.

Every hashed audit row uses compact JSON with sort_keys=True,
separators=(',',':'), ensure_ascii=True, followed by one LF; tuples serialize
as arrays. Loop order is the written order and Python product lexicographic
order. Digest rows include the case label, entire input, branch and entire
output. The report records exact inventory counts, branch counts, digests,
example accounts and finite-horizon accounts. One deterministic compact JSON
object and LF is printed. No time, host identifier or random value enters it.

## Systematics and falsifiers

Zero tolerance. A nonintegral division, disagreement of representations,
overlap of nonzero branch surfaces, wrong state/branch/account, loss of any
specified invariant, failed involution, wrong witness or finite-chain
continuation, missing case or failed negative control fires that prediction.
No input is removed and no threshold is changed. Exceptions are not caught
and converted into a success. Nonzero exit, nonempty stderr or a timeout is
not a pass. Preserve source and result/abandoned-pin history as POLICY.md
requires, without reuse of a consumed identifier.

Run assertions enabled from the repository root with standard-library
Python 3. Remove inherited PYTHON* and TWISTJ* variables; set
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, LC_ALL=C, LANG=C, TZ=UTC.
The verifier limit is 600 seconds. Record actual command, platform,
architecture, Python, exit, stdout/stderr bytes and hashes in RUN.md; preserve
stdout as EXPECTED.txt. Use unchanged repository checks. Required PR jobs
must reproduce the same accepted verifier and EXPECTED bytes on x86_64 and
aarch64 with Python 3.12. Replays do not establish independent authorship.

## Scope and exclusions

This is conditional L1 existence and a complete guard classification for
one declared reciprocal-step family, not a native-U gate, physical law,
universal reservoir, all-carrier positive entropy or Born derivation.
The four-slot interaction, chosen account, grouping and prepared payer
remain supplied. There is no derived autonomous contact selection or
constant-acceleration interpretation. The finite-stock word costs growing
prepared resources. No Canon, registry, workflow or existing gate changes.
