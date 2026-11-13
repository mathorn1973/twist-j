# Review of the common finite source, clock and archive construction

2026-10-29. **PASS within the declared conditional analytical L1 scope.**
No blocking mathematical defect was found in the reviewed composition.
The package remains NON-CANONICAL; this review does not confer external
independent acceptance or a Canon status.

## Review identity and method

This is a fresh static mathematical review by a separate context of the
same assistant system used in preparing the proposal. The reviewer had
previously compared the public source scopes, but did not author this
new proof. The reviewer first assessed the complete written PROOF,
CONTRACT, README and SOURCE_COMPARISON directly, and only afterward read
the component derivations. A further context of the same system checked
the written clock construction directly, without first reading its helper
derivation. These are exposed-text analytical checks within one assistant
system, not external human or another-model peer review, blind discovery,
formal verification, or independent computational reproduction.

No scientific executable was run or imported. File reads and byte hashes
establish the reviewed text; they do not validate its mathematics. No
external repository write was made by the reviewing context.

## Reviewed text

The final scope of this verdict is fixed by these UTF-8 file bytes:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PROOF.md | 19206 | `6de316f4fdfa9dea8bb76dead1f173a917cca340cf79b6bc678e848e4523d561` |
| CONTRACT.md | 3880 | `2a9609233d1929700c15fdd0470e3227449fbeb8acf6345630142394b6481032` |
| README.md | 2685 | `5f56b8e50bb5af6a8fc0daccf724961d964deaa31f68e815d6ce849397ad209b` |
| SOURCE_COMPARISON.md | 3509 | `ed3a7f7f117032ec317d5cada7c363bf6a0a4017780c21239f699f3966f0b143` |

The cited public source revisions were checked during the preceding source
assessment: #1795 at `e4d165c5c5471ea5746013f7f8f5c394512f9884`, #1804 at
`181b8b0dd98e0a697311fb83ab61493c94fd9e20`, and #1774 at
`3de02b0eb898f1756e3626ee2881d596c72d0094`. They are distinct apparatus
contracts. Acceptance of their mere juxtaposition was not presumed.

## Concrete mathematical checks

### 1. System and active record target

[PROOF.md](PROOF.md), Section 1, retains the specified 16-dimensional
total-momentum-pi sector, all five energy eigenspaces and their full
degeneracies. The supplied computational-basis partition has ranks
4,3,3,3,3. Orthogonality of its projectors and unitarity of the modular
shifts prove that each writer is a complete unitary, including occupied
archive cells. Multiplication gives the displayed coherent-history
expansion on the fresh-zero input.

The target is correctly stated as `G_j=W_j...W_1`, not `V_g^j` on an
unrecorded system. In particular the history amplitudes retain earlier
projectors and correlations. A five-letter independent uniform law or an
individual occurred outcome does not follow and is not asserted.

### 2. Complete shells and the active-archive extension

Section 2 includes `Pi_E tensor I_R` in every shell isometry. Thus all
`5^N` archive degrees participate in the shell, rather than being hidden
inside a passive-reference qualification. The irrationality of sqrt5
makes different integer shell labels have different energies. For every
interior label, all five complementary source coordinates are in the
finite box, and the isometry covers its complete energy eigenspace.

Orthogonal block multiplication proves full unitarity, multiplicativity,
and conservation. The identity complement retains all incomplete shells;
no projection, renormalization, or omitted boundary sector occurs.

One wording refinement was requested and incorporated before this verdict:
not every vector with a boundary source coordinate belongs to the
incomplete-shell complement. For example an energy-4 component at source
coordinate `(0,n)` can belong to the complete label `(1,n)`. The final
text correctly places boundary-coordinate states belonging to complete
shells in their `J_t` ranges. The defining formulas required no change.

### 3. Source error for a complete prefix

The sine packet is normalized and supported at source coordinates
`2,...,M+1`. Its adjacent translation overlap is `cos(pi/(M+1))`, giving
`delta_M=2 sin(pi/[2(M+1)])`. Orthogonality of the extended energy
projectors bounds both dressing errors by this same number, independently
of archive degeneracy or reference dimension. The finite lift agrees
with the bilateral dressing on the entire prepared subspace; a net
energy-coordinate difference stays inside `0,...,M+3`.

Inserting one intermediate dressed target gives
`e_M=2 delta_M`. Exact multiplicativity is used before this estimate is
applied to `G_j`. It is therefore valid to use one `e_M` for every whole
prefix, without a factor `j` and without reasserting source independence
at later correlated stages. Initial independence of the supplied source
is explicitly required. The statement does not extend to an arbitrary
initially source-correlated input.

### 4. Hermitian stage generators

The finite spectral convention includes eigenvalue -1 at angle pi and
gives `||K_j||<=pi`. The linear generator embedding `Kappa_M` is zero on
the incomplete-shell complement. Exponentiation therefore produces the
identity there, exactly matching the boundary completion in `Gamma_M`.
The displayed exponential identity and full-space commutation with
`E_M` follow on every block.

Spectral functions and the shell embedding preserve identity factors on
archive cells outside the active stage. This claim concerns each stage
operator. It does not say that the finite Fourier clock switches those
stages perfectly at each real time.

### 5. Program geometry and the complete read window

Sections 3–4 use nonoverlapping pulse supports
`[(j-1)tau+tau/3,(j-1)tau+2tau/3]`. Each envelope has area one and zero
value and first derivative at its endpoints. The stated bounds
`h=6pi/tau` and `h1=18pi^2/tau^2` follow without a factor N because the
supports have disjoint interiors.

Every point in the initial packet support `[tau/12,tau/6]` crosses
exactly the first j complete pulses by time `j tau`. Throughout
`[N tau,(N+1)tau]`, all points lie beyond the last pulse and before a
wrap: the latest endpoint is `(N+1)tau+tau/6 < (N+2)tau`. The exact
auxiliary identities therefore cover the whole final interval, not only
its sampled endpoints. They hold for arbitrary joint source/system input.

### 6. Packet regularity and the unbounded comparison

The packet and its first derivative vanish at its endpoints, so the
periodic zero extension belongs to H^2. Its normalization and derivatives
give exactly

```text
||f'||=8sqrt3 pi/tau,
||f''||=192sqrt3 pi^2/tau^2,
C_f=(288sqrt3+54)pi^2/tau^2.
```

Bounded C^1 multiplication by A preserves H^1. Hence the self-adjoint
`D_C=P_C+A` has `Dom(D_C^2)=H^2`. The identity
`P_C^2=D_C^2-2AD_C+iA'+A^2` has the correct signs. Conservation of the
first two D_C graph norms controls `P_C^2` on the exact comparison orbit
for all times. This justifies the strong Duhamel step on that orbit and
its error `t C_f/(2Lambda)`; it does not assume P_C^2 is bounded on the
whole clock Hilbert space.

### 7. Positivity, boost phase and the translated finite packet

The integer boost is periodic and its conjugation gives precisely
`c_Lambda+D_C+P_C^2/(2Lambda)`, with `c_Lambda=Lambda/2+h`.
The potential bound proves positivity of the rotor and of its finite
compression. The complete finite Hamiltonian has the stated bound
`B_H=(Omega L)^2/(2Lambda)+2h`.

Fourier projection commutes with translation, and the correct identity is

```text
Q_L G_ell T_t f=exp(iLambda t) T_t Q_L G_ell f.
```

Consequently `chi_t` has exactly unit norm with the same p0 for every t.
The vector comparison includes `exp(-it c_Lambda)chi_t`. Replacing
chi_t by a plainly translated f_L without its extra phase would be an
error; the reviewed text explicitly avoids it. The clock need not return
to its initial position during this finite-stage program.

### 8. Interacting tail and finite compression

The initial auxiliary rotor energy is independent of the joint vector
because the potential vanishes on the original packet. Positivity and
energy conservation give `||P_C u(t)||<=C_E` on the actual interacting
orbit, and therefore the uniform Fourier tail `C_E/p_cut`.

Only the bounded potential couples retained and discarded Fourier modes.
The retained-component Duhamel estimate is accordingly
`t h C_E/p_cut`. At each nominated time the projected ideal vector is
exactly p0 times its normalized finite-clock target. Division by p0 yields
the stated eta(t). No extra final-tail term is missing: both final vectors
in this comparison already lie in the retained space. Comparison with an
unprojected target would be a different assertion.

### 9. Resource prescription and quantifier order

Section 8 chooses the source first, then the boost, then the cutoff.
There is no circular dependence. The two clock numerator terms are each
at most `epsilon_c/4`, while `p0>=sqrt3/2>1/2`, so the displayed
`eta(t)<=epsilon_c` holds for all `t<=T_h`. The source choice gives
`e_M<epsilon_s`. Restricting the explicit prescription to tolerances below
one loses no positive-tolerance existence claim: for a larger requested
tolerance one may use a smaller tolerance below one.

The full active dimension is
`16*5^N*(M+4)^2*(2L+1)`, with a declared old archive counted separately.
One chosen apparatus serves all specified times and inputs. Increasing
the horizon or tightening accuracy can change that apparatus; no
interchange of these quantifiers is used.

### 10. Joint comparison, references and records

The clock estimate is uniform on the whole joint source/system/archive
space, so it can first compare the actual evolution with the complete
lifted prefix. The source estimate then compares that prefix once with
the logical record process. Their triangle inequality gives precisely
`eta(t)+e_M`, including actual clock/source correlations.

The compared maps are isometries with common supplied clock and source
preparations. Tensoring with arbitrary passive references preserves the
operator estimate. Purification gives the asserted half-diamond and
trace-distance bounds, each capped at one. There is no conditioning or
unpaid success denominator.

Later ideal stages are unitary on the complement of earlier written
cells, so their joint reduced state with a passive reference is unchanged.
The actual process is controlled by the joint approximation at the stated
times; exact continuous-time nondisturbance of those cells is not claimed.
The separately designated old archive O is an exact identity factor of
the actual Hamiltonian. No old state is erased or silently replaced.

### 11. Exact conservation versus the time generator

Every lifted stage generator commutes with the entire additive account
E_M; the clock kinetic term, cutoff and scalar shift do also. Thus
`[H,I_C tensor E_M]=0` is an exact operator identity on the complete finite
carrier, independent of the approximation estimate or initial state.
The full distribution of this account is conserved, as is the generator
H under its own evolution.

These are different operators. The proof does not infer that the account
generates the implemented clock evolution. Adding E_M to H would produce
an additional energy-dependent free phase and require a changed target.
The initial additive moments follow from source independence; the bounds
for the actual finite generator follow from its own spectral interval.
Uncompressed idle-rotor moments are not substituted as finite-clock
equalities.

### 12. Preserved limitations

[CONTRACT.md](CONTRACT.md), [README.md](README.md) and
[SOURCE_COMPARISON.md](SOURCE_COMPARISON.md) preserve the boundaries needed
by the proof. The archive, logical partition, zero archive/clock terms in
the chosen account, coherent source and clock packets, exact couplings,
clean fresh cells and tick scale are supplied resources.

The result does not inherit original-position locality from #1795,
thermal preparation or a success probability from #1774, the original
26-state capture instrument, or native six-pentit implementation. It
does not evade the strict coincidence-support obstruction of #1804:
the new spectral interactions are not asserted to obey that support
restriction. The finite hold window is compatible with a moving clock
and later recurrence, not permanent self-stopping or an infinite fresh
message stream. Arbitrary intermediate measurements are outside the
uninterrupted evolution contract.

## Disposition

The written composition supplies its claimed conjunction within one
explicit finite mathematical model: active sequential records, a finite
source and clock, one static positive generator, exact conservation of
the declared additive account, and one uniform joint approximation for
all nominated prefixes and the final interval. The checks above address
the composition itself, rather than treating separate component results
as sufficient evidence.

The single wording correction about boundary-coordinate states is
incorporated in the hashed text. No mathematical construction change or
unresolved blocking defect remains in this review. External mathematical
acceptance, physical preparation, locality, finite manufacturing precision,
resource renewal and native admission remain separate from this verdict.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
