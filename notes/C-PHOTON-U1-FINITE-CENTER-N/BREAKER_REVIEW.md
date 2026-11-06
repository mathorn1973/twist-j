# Independent analytical and implementation review

**PUBLIC-source, NON-CANONICAL; no authority.** Candidate
C-PHOTON-U1-FINITE-CENTER-N. Author: A. M. Thorn, independent breaker
session, 2026-10-23. Original work: Apache-2.0.

## Independence and source boundary

The mathematical contract was read from `PREREG.md`, publicly pinned at
`b7be3d00495330e4ac00441b865f9009e54a6299` (10129 bytes, SHA-256
`87e2f1f6265e2524b84ff3c298d166ac51f9fcdc6374b5961971392684d6d97e`).
The breaker has not read `verify.py`, `z7_exact.py`, their output or their
comparison digest. It imports neither implementation. This independence is
of implementation, not blindness to the mathematical predictions, which
were discussed before this source was written.

The global sharpness witnesses were obtained analytically before the
preregistration: the breaker requested an independent analytical helper,
which found the alternating transverse-parity construction. Its formulas
were supplied to the primary owner before either computational audit.
The primary implementation can therefore legitimately use those exposed
witness formulas, but the resulting comparison is not a blind prediction.
The local incidence bound itself is inherited from #1196.

At this review's initial writing, no scientific execution of `break.py`
has occurred. Static syntax inspection and source hashing are permitted.
The owner must freeze and publicly read back this source before execution.
Execution results and any failed first run belong in the separate run and
result records; this analytical review does not assert a computational PASS.

## Analytical verdict and sharp boundaries

Normalized Haar character integration selects `Bn+J=0` over the integers
for U(1), or modulo N for Z_N, with the identical coefficient
`2^(|P|-|supp(n)|) exp(i<n,a>)`. Thus

    N > max_e(sum_p |B_ep| + |J_e|)

is sufficient for literal equality of the complete finite source functions.
All cycles remain present. No primal-field bijection, gauge fixing, or
restriction to homologically trivial cycles is used.

For the ordinary four-torus the proposed threshold seven is globally
sharp on the admitted even sizes. The stated parity witness has
`Bn=N j`, nonzero j, and support `N L^4/2`, for every N=2,...,6.
The U(1) admissible set is a subset of the modulo-N set; at zero source all
coefficients are positive, giving strict partition inequality. This is a
full-lattice construction, stronger than a local incidence-word alias.

For inserted numerators the N=6 witness and J=j give `Bn+J=7j`.
Consequently the threshold eight is sharp for the full class of conserved
integer currents with maximum coefficient one. This current consists of
alternating signed winding loops. It is not one simple contractible loop;
no sharpness claim for that narrower observable class follows.

For the integral stack source, `W=<n,stack>` pairs a cycle with a closed
integral cochain. Moving the stack changes the cochain by an exact one and
does not change W. Averaging its `L_mu L_nu` translates gives the uniform
source, proving the full source-function identity in the integer-closed
ensemble. The same conclusion transfers to N>=7; it is not an extension
of the weaker Z5 first-derivative seam identity to arbitrary source strength.

The characteristic function identity gives `F''(0)=Var(W)`. A finite torus
contains both zero winding and either orientation of a fundamental sheet,
all with positive weight, so its exact variance is strictly positive. This
does not bound the thermodynamic limit from below. Cube-boundary updates
alone preserve W; a frozen W trajectory cannot certify the full measure.

## Independent exact implementation

`break.py` uses integer vectors of length six in `Z[z]/Phi_7(z)`. It first
multiplies modulo `z^7-1` and then removes the sixth coefficient using
`1+z+...+z^6=0`. Real values are converted to the common basis only for the
prescribed digest; the full six-coordinate reconstruction is checked.
Positivity is certified by exact rational root isolation and an explicit
quadratic interpolation error bound, never by decimal approximations.

The imaginary source score is evaluated without field division:

    D_k=(z^k-z^-k)/w_k
       =z^k-z^(2k)+z^(3k)-z^(4k)+z^(5k)-z^(6k).

Its product with w_k is checked directly. Conditional probabilities are
normalized by a cubic norm formed using cyclotomic automorphisms, retaining
exact integer numerators and a positive integer denominator.

Both two-dimensional tests enumerate every constrained plaquette vector.
Grouping identical sufficient statistics takes place only after that
enumeration. The actual incidence matrix is checked to have rank A-1 over
F7, which, together with the zero total curl, verifies uniform gauge
multiplicity and the `7^(-(A-1))` normalization.

The independent uniform reader uses

    [A - sum D_k^2 + 2(sum D_k)^2]/(2 A^2),

and the stack reader uses `(1+D_first^2)/2`. Twisting the stack by one
residue replaces exactly one weight factor rather than differentiating a
copied formula. A separate ternary dual enumeration retains both winding
sectors and exposes the false zero response caused by their removal.

The incidence-word census, actual four-torus witnesses, all fundamental
sheets and elementary cube boundaries, single three-cube and single disk
are separately constructed. The sampler's PRNG path is not reproduced;
the contract explicitly does not require that from the breaker. No audit
here supplies equilibrium, practical mixing, a phase, or a physical photon.

## Remaining review limitations

The universal theorem rests on the written character argument, not finite
enumeration. The finite audit tests its specified arithmetic and geometric
instances. Shared scientific predictions and shared preregistration are
disclosed. This is an independently authored program in one agent team,
not external blind acceptance and not a two-architecture public gate.
