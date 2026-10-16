# Independent endpoint-restoration certifier: exact target and bounded design

**NON-CANONICAL / L1 mathematical derivation and source-first design / lane B.**
Original work Apache-2.0, A. M. Thorn, 2026-10-13.
Reservation [#1484](https://github.com/mathorn1973/twist-j/issues/1484).
The governing contract is immutable
[4302c31f07823b2a843e3702ca14620c1917b853](https://github.com/mathorn1973/twist-j/blob/4302c31f07823b2a843e3702ca14620c1917b853/notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md),
especially Sections 5 and 8.

This lane now supplies the complete mathematical target, an independent
finite evaluation algorithm, input bindings, scope and a bounded future
implementation contract. It supplies no executable accepted verifier or
numerical result. No stored vector was propagated, restored or normalized
in this dispatch. The only remote read extracted five existing custody
receipts from the closed inventory; it did not open a numerical executable.

The primary classical D3 wave, native F5 time sidecar and these seven-mode
Hilbert endpoints are distinct types. Certifying the legacy restoration
does not identify its Hamiltonian, energy or time with the classical port.

## 1. Inherited input and the gap being addressed

The immutable old numerical source is
[bca348445715c03f4cdc3af6079207024dd40332](https://github.com/mathorn1973/twist-j/tree/bca348445715c03f4cdc3af6079207024dd40332/probes/P-U-CA40-DP5-FULL-CLOSURE-1).
Its preserved first outcome is
[6f378a1ba9b39fa1c29188b61a2e6507a92eb9d5](https://github.com/mathorn1973/twist-j/tree/6f378a1ba9b39fa1c29188b61a2e6507a92eb9d5/probes/P-U-CA40-DP5-FULL-CLOSURE-1).
Saved audit A at
[8a357a65089bd977673e67899190d4c201c79279](https://github.com/mathorn1973/twist-j/blob/8a357a65089bd977673e67899190d4c201c79279/notes/C-U-CA40-FULL-PULSE-INDEPENDENT-AUDIT-N/CAMPAIGN_AUDIT.md)
checked custody and exact aggregation, not restored coherence rectangles.

Here the first target is a **conditional independent restoration** from
the exact stored endpoint vectors and valid supplied branch-parameter
intervals. It does not independently validate the old MPFR construction
of those intervals or reconstruct unarchived propagation nodes.
An independent force/linear-history preparer is a separate next level.

No old source module, MPFR routine, displacement implementation, numerical
binary or propagated runtime state is imported or executed. The operator
identity is shared public mathematics; implementation independence is not
blindness or historical novelty.

## 2. Serialized endpoint contract

There are seven oscillator modes, dynamic total-occupation cutoff L=8,
dimension 6435, six branches and 120 retained initial columns. Generate the
basis independently as all nonnegative seven-tuples nu with |nu|<=8,
graded by |nu| and ascending first coordinate recursively within each grade.
The first 120 entries have |nu|<=3. Bind that basis to the saved basis.json.

Final endpoints.bin is little-endian interleaved(real,imag) binary64,
in case-major, thermal-column-major, basis-major order. Its size is exactly

    6 * 120 * 6435 * 2 * 8 = 74131200 bytes.

This final layout is not the eight-lane checkpoint layout. Every finite
binary64 value is decoded as an exact signed dyadic; reject NaN/infinity,
truncation, trailing bytes, wrong order and boolean/numeric impersonation.
Do not normalize, phase-fit, compress away a nonzero component or replace
a final state with a reset/window state.

The independently audited copied inventory binds:

| File relative to full-state | Bytes | SHA-256 |
|---|---:|---|
| basis.json | 103064 | ec66eca09652f6d5d5ee80f7beb592e72bfd31cd71d5a92ba52093d6d7970f61 |
| components.bin | 69120 | 581e371bce1fd72b1abab5f837b4e33786bada00a6e2de14d750542877928c41 |
| endpoints.bin | 74131200 | 7d67034f594bdc923794b61e019c3566b860d6bfe942143ff5c6a06d2b66066f |
| metadata.json | 6773 | 7c2edd7701efad8a2db8af997d97c704a6460b1aeb3487d5503ac0083800fff2 |
| result.json | 312313 | 49940669a1954abaa52a230d1e40d76bc9bc7cef0b6eb395b1c57f10176f3e31 |

The inventory itself is 2424474 bytes, SHA-256
b540e5135c5d0b81f7c4e7b5ee8bf0a0ac9f08bf6812b1931b113666a40700c8.
Input context is the naturally closed 500-us campaign. The binding names
public mathematical data, not an attestation of the original execution.
Original and closed offline copies remain unchanged.

This dispatch has not independently bound the serialized campaign input
`exact_input.txt` to its byte count, SHA-256 and final-custody receipt.
That association is an inherited, unreviewed condition here, not a closed
input-to-endpoint provenance claim. Before any successor execution, its
source pin must bind that file and receipt as well as the five files above
and verify their association with the same campaign. This is an open part
of lane B even though the endpoint evaluation target is fully specified.

## 3. Exact restored quantities and operand convention

For pair (a,b) in the fixed order
(0,1),(0,2),(1,2),(3,4),(3,5),(4,5), use valid branch rectangles
alpha_a,j,alpha_b,j and phase intervals Phi_a,Phi_b at the common final time:

    delta_j=alpha_a,j-alpha_b,j,
    theta_ab=Phi_a-Phi_b+Im sum_j conjugate(alpha_b,j)*alpha_a,j.

The displacement convention is

    D(delta)=exp(sum_j(delta_j a_j^dagger-conjugate(delta_j)a_j)).

For the exact stored vectors y_a,r and y_b,r, the target is

    Gamma_ret(a,b)
      =exp(i theta_ab) sum_(r=0)^119 p_r
          <y_b,r | D(delta) | y_a,r>,
    p_r=(20/21)^7*(1/21)^(|nu_r|).

Weights remain unequal and unnormalized. The all-thermal linear reference is

    Gamma_linear(a,b)
      =exp(i theta_ab)*exp(-(11/20) sum_j |delta_j|^2),

because nbar=1/20. Both formulas retain the same relative Weyl phase.
The target is not the raw overlap, a separate branch-phase fit or a
displacement exponential built from a truncated position matrix.

The branch intervals in result.json are rounded outward versions of the
old high-precision branch values. Reconstructing delta/theta from them may
be wider than the original directly prepared pair intervals. Such width
is not a discrepancy or a reason to tune phases.

## 4. Finite exact normal-ordering theorem

Let Pi_L project onto total occupation<=L. For the finite stored bra/ket,
the normal-ordering identity gives exactly

    <y_b|D(delta)|y_a>
      =exp(-||delta||^2/2)
        <y_b|Pi_L exp(A_plus) exp(A_minus) Pi_L|y_a>,
    A_plus=sum_j delta_j a_j^dagger,
    A_minus=-sum_j conjugate(delta_j)a_j.

On the finite ket, every lowering product of degree>L vanishes.
After lowering, occupation is still<=L. In the subsequent raising
exponential, every product that raises beyond L has zero overlap with
the finite bra, and only raising remains, so it can never return.
Therefore, as an operator on the finite space V_L=ran Pi_L,

    Pi_L D(delta) Pi_L
      =exp(-||delta||^2/2)
        [sum_(k=0)^L (Pi_L A_plus Pi_L)^k/k!]
        [sum_(k=0)^L (Pi_L A_minus Pi_L)^k/k!].          (B1)

Both degree-zero terms in (B1) are I_(V_L). If the identity is instead
written on the full Fock space, sandwich its right-hand side in Pi_L;
otherwise the degree-zero term would act outside V_L.

The two factors must keep this order. Each is a polynomial of degree 8,
not a Taylor approximation with an omitted displacement tail.

For a second, independent coefficient-level specification, in one mode,

    <m|D(delta)|n>
      =exp(-|delta|^2/2)*sqrt(m!n!)
         sum_(l=0)^min(m,n)
          delta^(m-l)*(-conjugate(delta))^(n-l)
           /[l!(m-l)!(n-l)!].                         (B2)

Derivation: lower n to l, then raise l to m. Seven-mode coefficients
are products of these one-mode coefficients. Formula (B2) and the
collective-ladder polynomial (B1) agree coefficient by coefficient.
Small fixture comparisons must use both constructions. No finite sample
substitutes for the all-finite-vector proof.

This proves only the exact finite stored-vector matrix element. The
old propagated-vector errors and thermal omission still belong to
their own accounts; they are neither removed nor charged again here.

## 5. Independently bounded arithmetic

The intended implementation uses integer/rational directed dyadic
intervals, not the old C++ or MPFR code. It starts with exact dyadic vector
components and outward parameter rectangles.

For ladder coefficients sqrt(n), n=0..8, at fixed binary precision P=192,
compute q=floor(sqrt(n*2^(2P))) with integer square root. Then

    q/2^P <= sqrt(n) <= (q+1)/2^P,

with coincident endpoints when the integer square is exact. State the
positive-root convention. Complex rectangular addition/multiplication
uses exact rational extrema; rounding each endpoint down/up to the
P-bit dyadic grid preserves enclosure. Shared-parameter dependencies
may widen rectangles; they do not invalidate interval containment.

All ladder vectors are updated by fresh arrays; prohibit input/output
aliasing. Apply the degree 8 lowering polynomial first, then the projected
degree 8 raising polynomial, with factorial weights and accumulation
explicit. No state normalization or coefficient pruning is allowed.

Only elementary scalar exponentials remain. For a real phase interval
I_theta with midpoint c and radius r, evaluate the exact complex polynomial

    T_N(c)=sum_(k=0)^N (i*c)^k/k!, N=256.

Taylor's integral remainder on the real phase path gives
|exp(i*c)-T_N(c)|<=|c|^(N+1)/(N+1)! because |exp(i*t)|=1.
Also |exp(i*theta)-exp(i*c)|<=r. Thus each coordinate of exp(i I_theta)
is enclosed by the corresponding polynomial coordinate plus/minus

    r + |c|^257/257!.

For x>=0, the real polynomial sum_(k=0)^256(-x)^k/k! has remainder
at most x^257/257!, since derivatives of exp(-x) have modulus<=1
on the interval from 0 to x. An uncertain nonnegative argument with
midpoint c_x and radius r_x adds at most r_x by the same Lipschitz bound.
Compute the Gaussian at x=||delta||^2/2 and the thermal exponential at
x=(11/20)||delta||^2. Intersecting their sound intervals with [0,1],
or phase coordinates with [-1,1], is allowed; fitting to a unit circle
or a desired old rectangle is not.

The proposed fixed argument guards are |c|+r<=64 radians for theta
and 0<=x<=64 for either real exponential. Outside them report the
frozen resource/domain outcome, not an unproved bound. These guards
are implementation choices, not physical restrictions or a claim
about the actual data until the accepted validator reads them.

## 6. Algorithm, comparison and pair accounting

A complete implementation must:

1. Bind and rehash exact_input.txt and its final-custody receipt together
   with all five named endpoint inputs and validate the independent basis/layout,
   original final-time labels, six cases and 120 thermal weights.
2. Reconstruct parameter rectangles and phase conventions directly from
   branch metadata, keeping their validity as an explicit premise.
3. For all 720 pair/column overlaps (six pairs times 120 columns), apply (B1),
   include the scalar Gaussian and form the exact weighted inner product.
4. Rotate each weighted sum and independently evaluate Gamma_linear.
   Produce six sound complex rectangles and all coefficient/remainder bounds.
5. Recompute the witness-center magnitude interval and arithmetic halfwidth.
   Carry the old independently audited numerical and thermal radii as
   declared dependencies, counting the center uncertainty only once.
6. Classify precision and discrepancy separately with exact rational
   comparisons; retain any wide or unresolved new enclosure.

A stored old rectangle is **covered** only when the entire new sound
rectangle is contained in it. Disjoint real or imaginary intervals give
a **conflict**. Overlap without containment is **not decided**: overlap
alone does not independently certify the old enclosure. These diagnostics
must be separate from construction of the new valid enclosure.

A complete new enclosure may support a fresh conditional pair conclusion
without proving that every old interval endpoint was correct. Preserve
the old result, even on conflict; do not overwrite it with a new estimate.
A source/parameter-premise disagreement requires diagnosis, not automatic
physical falsification or phase adjustment.

## 7. Fixed bounded successor proposal

Before execution, a new public probe must bind its accepted implementation,
all five endpoint-input hashes plus the serialized-input bytes/hash and
final-custody receipt, source exposure, scalar precision P=192, degree 256,
argument guards, basis, pair order, all 720 overlap slots and failure codes.
It must contain self-contained arithmetic/enclosure proofs, a static security
review and exact positive/negative controls. No such probe is reserved,
pinned or executed by this notes-only document.

Proposed first resource contract: one invocation, 600 seconds total including
hashing, fixtures and all 720 overlaps, memory ceiling 2 GiB, at most 8 workers,
no propagation, network, adaptive precision, column subsampling, cutoff
ladder, source repair, retry or resume. This is a cap, not a performance
prediction. Any partial coverage or time/resource exhaustion is
NOT_CERTIFIED, with the first output/receipts retained.

Required controls include zero displacement/phase with exact retained
weight, one-mode vacuum and single-excitation coefficients from (B2),
adjoint/conjugate conventions, swapped branches, nonunit endpoint norms,
an intentional wrong Weyl sign, understated elementary remainder,
truncated/reordered payloads, wrong thermal weights and a center-width
double-count trap. Controls are mathematical fixtures, not a second
floating propagator.

Outcomes need two separate fields: new-restoration coverage/soundness
and old-rectangle comparison. A passing complete new certificate must
record 720 overlaps and six pairs. COVERED/CONFLICT/NOT_DECIDED comparisons
must never be collapsed into a midpoint match or a blanket physical PASS.
No production runtime or successful numeric certificate is claimed here.

## 8. Scope after this design

This lane closes the written finite-normal-ordering/evaluation specification
and gives a concrete next implementation contract. It leaves actual code,
security review, exact first fixtures and the production restoration run
pending. Even successful execution would remain conditional on valid
branch alpha/Phi intervals and the inherited propagation error account.
The serialized-input custody association above is also still open.

Independent reconstruction of the force model, linear history and MPFR
parameter preparation is a separate B-next task. Per-cell quintic/node
enclosures cannot be recovered from boundary snapshots. No ion experiment,
new long simulation, physical source-preservation result, classical-port
energy identification or Canon/status change follows.
