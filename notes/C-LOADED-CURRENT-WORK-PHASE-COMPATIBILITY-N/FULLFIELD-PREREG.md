# Prospective full-field action audit

**NON-CANONICAL / L1. Additive source, unexecuted before its own pin.**

This extension is separate from the earlier reduced source pin. Its final
accepted bytes, verify_fullfield.py and public readback must be frozen before
its first scientific execution. A later run record replaces no earlier result
or failure. Static corrections before this pin are not scientific runs.

## Claim and scope

Audit the equations and exposed hand-derived conclusions of
FULL-FIELD-PHASE.md on the fixed periodic 27-site, thirty-labelled-direction
D3 carrier, z=1/27 and matched source edge (1,1,0). This is a reconstruction
from public #1926/#1927 equations, not original-source replay. Universal
statements depend on the written proof; finite tests are candidate-C on their
actual execution architecture. No measured target or alpha is an input.
Same-session review is not independent scientific acceptance.

## Fixed definitions

R=Z[1/6], O=Z[j], Phi5(j)=0; exact coefficient equality in the power basis.
All arithmetic uses integers and fractions. Keep all thirty directions and
all periodic aliases. M,d0,d1,K,D, B=z M^-1 E, the free map, source-before-free
calendar, full energy E_G, alternating form Omega_G, and primitive action
Gamma=Omega_G(s,Ts)/4 are fixed by the proof. The increment for a macrostep
is the SUM at its separate collision and free cuts, not a new chord action.
Modulo-five and modulo-twenty-five reductions invert only denominators
coprime to five. No rounding, truncation, tolerances or random sampling.

The verifier independently implements K twice: M(L-d0 d0* M), and the
literal weighted pair-curl d1* M2 d1. It uses one cyclotomic representation
with explicit conjugation, trace and alternating form; these two K paths
are algorithmic cross-checks, not independent authorship. All field states
retain 27 sites and thirty labelled directions, stored sparsely without
truncating nonzero entries.

## Exact finite inventory

Let o=(0,0,0), ell=(1,1,0), v=(1,-1,0). Write delta_(direction,site)*a
for the link field with value a at that labelled edge and zero elsewhere.
Write delta_site*a for a vertex field, grad=d0, and mode(a) for the field
with sole component v equal to f(r)*a, where f=2 on sum(r)=0 modulo3 and
f=-1 otherwise. All coordinate arithmetic is modulo three.

The ordered eight (A,B) fixtures, indexed zero through seven, are:

0. (0,0).
1. (mode(1),mode(j)).
2. (mode(J),mode(phi)).
3. (delta_(ell,o),0).
4. (0,delta_(ell,o)*J).
5. (grad(delta_o),grad(delta_(1,0,0)*j)).
6. (delta_(ell,o)+delta_((1,0,1),(0,1,0))*phi,
   delta_((2,0,0),(2,0,1))*J+delta_((1,0,1),(0,1,0))/2).
7. (mode(1)/2+grad(delta_o)/3,mode(j)/3).

For each fixture, compare both K implementations on A and B (sixteen
comparisons in total), literal free inverse, exact energy conservation,
nonnegative fixture energy, preserved weighted divergence, alternating
self-pairing, and direct Gamma against formula (F7). The latter also must
admit reduction modulo twenty-five. Check the complete stencil counts,
shell multiplicities, scalar diagonal8/9, marked weight1/54, Q(J)=3,
Omega(1,j)=1, and the published marked K diagonal23/1458.

On fixture1, check exact transversality, D eigenvalue3/4 on both A and B,
and weighted HALF-TRACE norm g(A,MA)=2. The scalar weighted profile norm
c_v sum f^2 is1; it must not be confused with the half-trace norm of the
ring element1. Check the initial energy837/16. Run four free ticks; at
each cut the marked source collision must accept d=0 and leave the full
state unchanged, each free Gamma must be1053/256, and core energy must
remain fixed. Check reverse action orientation, full-state return MODULO
FIVE after four ticks and failure of exact rational return. Single action
residues are3 modulo5 and13 modulo25; the four-step sum residue is2 for
both moduli. The actual encoded pointer history from zero is13,1,14,2.
Reverse the four free operations and recover the entire initial core and
pointer. This is not an exact closed-field holonomy experiment.

Use eighteen loaded fixtures: backgrounds1,5,6 crossed with d in
{0,J,phi} and source triples (0,0,0),(1,-1,1). Adjust only B_ell(o) to

    2*(4d-2y+x+e)+(KA)_ell(o)/z.

This engineers precisely the stated d. Check admission, displacement,
complete energy, preserved actual Gauss defect, literal collision inverse,
Gamma_C=B(d), integer actual field work, exact five-collision base return,
five-collision action5B(d), and old monodromy as the appropriate encoded
label increment. Then perform the actual source-before-free macrostep,
check complete energy and Gauss defect, and reverse both core and pointer.
A nonzero initial Gauss defect in an arbitrary occupied fixture is retained,
not mislabeled a charge-free or Gauss-zero preparation.

Use two refused fixtures x=y=e=0,A=0 with B_ell(o)=1/2 and1/3. Check
nonadmission, complete collision identity, zero current and action, and
the full macrostep-plus-pointer inverse including subsequent propagation.

Use cold prepared sources e=J and e=216J with (x,y,e)=(e,-e,e), A=B=0.
Perform exactly three source-before-free macrosteps, preserving the actual
source, field and pointer throughout. Expected admissions are1,0,0 and
1,1,0 respectively. The unscaled J history is an inherited #1927 control.
The third refusal for216J is an exposed prediction of this reconstruction,
not a guarantee established by the available original #1927 result.
The first actual field work is5 times the squared
amplitude. Check the published second unscaled J displacement
(85/108,193/216,-23/216,193/216) for the unscaled source. Record every actual signed work and encoded pointer label rather
than replacing refusals by refreshed preparation. Check complete energy,
preserved Gauss defect and integer actual works; reverse all three
macrosteps and recover the whole initial state and pointer. This tests
three attempts only, not indefinite rejection or long-time emission.

For the two-pair pointer, test all25 labels and all25 increments,625 cases:
actual ordinary-contact digit control must equal addition modulo25,
preserve account8, and invert by subtracting the increment. Test100
complement cases: each increment on (0,0,0,0), (1,0,1,-1),
(1,-1,1,0), (J,-J,1,-1). These must be outside the prepared25-state
set and fixed by the declared complement extension.

Finally run both literal five-contact readers on all25 prepared labels.
The first-changed helper indices must read the two ordered digits. Check
combined pointer/reference account48 and the complete inverse of both
readers, including all references. The figure48 is the auxiliary pointer
and reference cost, not the complete field/source preparation account.

## Output, resource and execution contract

The standard-library source emits deterministic ASCII lines with a final
newline: scope, carrier, fixture counts, exact Gamma/residues, the explicitly
limited quotient return, pointer/complement/reader counts, one actual cold
history line for each amplitude, and the assertion count with PASS. Cold
lines include all three admission bits, actual signed works and pointer
labels. There are no timings or machine names in scientific stdout.
The exact serialization in the prospectively frozen source is authoritative;
EXPECTED is the actual first successful output, never a fabricated run.

Each formal local execution has a wall-time ceiling900seconds and memory
ceiling1GiB. These are resource limits, not mathematical conclusions. A
resource failure is retained honestly; any proposed revised execution
contract must be recorded separately before another run, without rewriting
the first attempt. Record command, environment, timing, exit status, exact
stdout/stderr and hashes. A clean repeat checks byte identity. Any second
architecture execution must use the same frozen source and compare the
same output bytes; it is reproduction, not independent proof acceptance.

## Falsifiers and evidence handling

Every asserted exact equality has threshold zero mismatches. Any failure,
nonzero exit or stderr is retained at the immutable additive pin. Do not
repair pinned source and call a second run the first run. A corrected
successor requires its own prospectively pinned source and explicit
relation to the failure. A missing fixture, wrong Gauss convention or
changed primitive calendar is a substantive defect, not permission to
move the test after observing output.

The expected values above are exposed hand derivations or explicitly
attributed inherited source controls, not blind predictions. Publish and
read back the complete additive source and hashes before running; then
preserve its exact first output and all execution metadata. Earlier reduced
runs are not evidence for this implementation. Repository CI that does not
execute this note is not evidence for its scientific assertions.

## Out of scope

No original-source replay, parameter fitting, physical phase selection,
coherent interference, fixed-contact compiler, physical twenty-fifth root,
empirical receiver, alpha, absolute action unit, long-time emission,
eight-acceptance return theorem, Canon modification or scientific promotion.
