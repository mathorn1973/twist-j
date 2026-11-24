# Result

Status: PASS  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-JOINT-VARIATION-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1645  
Pin: fe5456f1aac8adcc3fdb0222df81f7e2fc773977

## Observed first execution

The first formal primary execution completed with exit zero and empty
stderr. Its separately authored rational/direct-coordinate breaker also
completed with exit zero and empty stderr. Their unmodified 19-line
certificate bytes were identical. The primary appended two success lines,
producing the 589-byte, 21-line stdout preserved exactly in EXPECTED.txt.
Its SHA-256 is
a8b2315bf4a69ed4a9bd8490868dd9224b3e973c967bf2db4b90bc9efee3f7f7.

No preregistered falsifier fired. No frozen file, definition, fixture,
threshold, or implementation changed after the prospective pin. This is
a completed gate. RUN.md records the actual local environment and custody;
architecture receipts are to be recorded in the draft PR after observation.

| Finite audit | Observed result |
| --- | --- |
| Actual normative authority | All five file sizes and hashes match Public Canon v103 |
| Hermitian transports | 133 exact closure, inverse, determinant and trace-cost checks |
| Source holonomy | 95 exact commutator/combined-shear checks |
| Unrestricted carrier | 172 core fixtures and 4128 funded cases, with all five motion/reflection categories |
| Corrupt images | 684 individual field/source numerator corruptions rejected by the exact inverse guard |
| Ready histories | 390 records: ten words, three source contexts, counters 0 through 12 |
| History payload SHA-256 | 7ac8f2d388c3b593680cbb2a3c3f0b92a672f9634bd86c57894f9d0bd8be060c |
| Joint local action | 720 exact reduced TT-plus-source central differences vanish |
| Off-shell action | 36 exact derivatives match the signed gradient formulas; every off-shell fixture has a nonzero derivative |
| Complete funded paths | Nine least periods: 2,4,6,2,4,6,2,4,6 |
| Sharp first-step bank | 89368 for word 0011 in context a=0; bank 89367 reflects |
| Negative controls | All seven preregistered interventions behave as specified |
| Primary/breaker agreement | All 19 certificate lines agree as raw bytes, including every final LF |

The 720 executable variations comprise five independent TT field
coordinates and one scalar source coordinate at each selected counter.
The remaining spatial metric, lapse and shift directions are established
analytically in PROOF.md; they are not included in that executable count.

## Exact coupled law earned

For m=324 and ell=(1,-1,0,0,0), the new selected dynamics are

    (Delta_c^2+L) h_n = chi_n ell / m^n,
    (Delta_c^2+1) chi_n = a - <ell,h_n>/m^n.

Both right-hand coupling terms are retained at every counter. They follow
from one quadratic action with the canonical full metric action A_2,
the coupling chi_n<ell,V_11-V_22>/(2m^n), and the selected source action

    -1/2 sum (Delta chi)^2 + sum (chi^2/2-a chi).

The full first variation is derived before evaluating the TT
representative. On that representative, both coupled residuals vanish
exactly. The source variation includes the reciprocal metric term; it
is not replaced by an integer one-coordinate optimality condition or
an added constraint multiplier. The off-shell checks test the source
residual sign independently of its on-solution cancellation.

The source kinetic sign is negative relative to the TT field sector.
This is an explicit selected model choice, not a theorem that integer
storage requires this sign. No physical matter admissibility or positive
physical Hamiltonian follows from the PASS.

## Integer carrier, source realization and finite account

The sufficient common scale

    D_n=2*m^(n(n-1)/2),  P_n=D_n h_n,  Y_n=D_n chi_n

gives an exact update using integers only. The unrestricted core is
(P,W,Y,V,H,k): 5+5+1+1+8+1=21 integer coordinates, with k>=1.
The two older-slice inverse residuals provide six necessary-and-sufficient
divisibility conditions by m^(2k-1) at the preceding counter k.

The Hermitian register is transported by
M(Y'-Y)=A B(Y'-Y) A^(-1) B(Y-Y'). On the ready family

    (H_Y)_8=(9Y^2,-5Y^2,1,0,-2Y,Y,-Y,0),

its c1 coordinate reads the source numerator Y and
N(H_Y)=294Y^4+52Y^2+4. On arbitrary core states H is an independent
invertible register; the actual scalar source entering the update is Y.
This distinction is part of the full-carrier theorem.

Adding bank b>=0 and direction gives 23 coordinates. Domain and bank
reflection define a total bijection with inverse Rev F Rev and conserved

    E+b,  E=1+k+||P||^2+||W||^2+Y^2+V^2+N(H).

The account is proper, so every fixed-account shell is finite. On a
ready path, the exact budget to include counters 1 through N is the
prefix maximum max(E(x_1),...,E(x_N))-E(x_1). An admitted path of N
vertices has least funded period 2N. No global monotonicity of E is used.

Because the field coordinate sum remains one, this encoding has

    E(x_n) >= ||P_n||^2 >= D_n^2/5
           = (4/5)*m^(n(n-1)),  n>=1.

This is a cost bound for the declared common-scale representation.
D_n is not claimed primitive or optimal, and the bound is not a
universal lower bound for every exact representation of the history.

## Concrete witnesses

For word 0010, the two fixed contexts a=-1 and a=+1 give

    P2(-)=(487,167,-230,130,94),
    P2(+)=(491,163,-230,130,94),
    D2=648,
    h2(+)-h2(-)=ell/162.

Here a is a fixed parameter in each model context and also sets chi_1.
This is a context comparison, not an intervention on the initial source
alone with an otherwise identical constant forcing.

For word 0011 in the single context a=0, chi_0=chi_1=0. The field
itself generates a nonzero source:

    P2=(94,165,165,94,130), Y2=1, D2=648,
    chi2=1/648.

One counter later,

    P3=(22236121,-2269621,-2269620,22236120,28091448),
    Y3=105047, D3=68024448,
    h3-h3(free)=ell/68024448.

The control retaining only the first field-to-source impulse has
chi3=1/648. The actual continuing feedback instead gives

    chi3(joint)-chi3(first-only)=71/68024448.

Thus the reciprocal response is present after the initial impulse.
Disabling all backreaction keeps the zero source and free field, and
disabling only field coupling removes the metric contrast while the
source still responds to the free field.

For the same zero-source ready state, E(x_1)=10 and E(x_2)=89378.
Bank 89368 reaches counter two with bank zero; 89367 reflects before
that step. The first admitted two-vertex path has least period four.

## All-counter statements beyond the finite replay

PROOF.md establishes the exact integer closure and inverse, full-carrier
funded bijection, full first variation, and the following causal bounds
for all n>=1, all ten words and all three declared source contexts:

    |chi_n-chi_n(free)| < 2/323,
    |chi_n| < 648/323 < 3,
    ||h_n-h_n(free)||_inf < 1630/209304 < 1/125,
    -299/500 < h_n(r) < 499/500.

The metric diag(-1,1+h_n(r),1-h_n(r),1) therefore has signature
(-,+,+,+) and determinant less than -999/250000 at every counter.
The proof uses the named canonical free-history bound plus a new
simultaneous causal induction for the two coupled variables. This
all-counter statement is not inferred from the 390 finite records.
On the unrestricted carrier, the declared degeneracy counterexample
still exists; the metric theorem is a theorem about the ready histories.

## Interpretation and remaining obligations

The earned result is an exact integer realization of a selected discrete
TT-field/scalar-source model with continuing reciprocal coupling, a
joint stationary action, reversible finite-budget admission, and a
uniform Lorentz-signature theorem on the ready histories.

The five-site derivative, marked dipole, attenuation, source law and
kinetic sign, common scale, source monitor, and bank remain declared
comparison choices. The model does not derive these choices from native
TWIST-J U. The bank is an arithmetic storage/admission account, not an
identified gravitational energy, and the counter is not a physical clock.
Nonlinear Einstein dynamics, physically admissible matter, a native-U
realization and a continuum manifold limit remain open. Canonical status
and experimental agreement are not asserted.
