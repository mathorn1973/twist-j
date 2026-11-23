# Round 9 opposition and dispositions

NON-CANONICAL. No authority. Same-session internal review, not an external referee report.

## Team and separation

The requested two groups worked in stages under the four-active-agent limit.

Development: the root Astra coordinated source reading and proofs; r9_develop_astra reviewed the Gram implications and final local proof; r9_period_sol traced actual periods and the word-prime lattice; r9_verify_sol wrote the verifier.

Opposition: r9_opposition_astra built the sharp all-input countermodel and independently derived the local conductor rule; r9_break_sol wrote a blind independent implementation; r9_local_opponent_sol checked the local source hypotheses and primary newform/Zelevinsky theorems; r9_global_opponent_sol checked the complete countermodel and the conditional global-period application.

The two code authors received only the same frozen scientific contract. Neither read the other's program or outputs before freezing. The paper reviewers did not inspect or execute those programs. Root published and read back both codes before their first scientific executions.

## Mathematical challenges and resolutions

| Challenge | Disposition |
|---|---|
| Does the diagonal Gram bound really control the actual P_u kernels? | Accepted, candidate-D, for the constructed positive normalization. Each orthonormal kernel basis vector contributes one to the squared Gram error, giving kappa<=e0. The first wording was corrected from “every vector” to “every member of an orthonormal basis.” |
| Is the abstract countermodel only an averaged Gram example? | No. Opponent construction meets each distinct pair's inequality with equality. The independent Sol review counted affine incidences directly, without relying only on the moment shorthand. |
| Does the computed coordinate witness maximize over all complex subspaces? | Accepted through the projection-trace upper bound and a coordinate subspace attaining it. No finite enumeration of all complex subspaces is claimed. |
| Could genuine group periodization or removal of the common Fourier-blind kernel fix the model? | No. Orthogonal raw seeds in the explicit semidirect group average to the same target factor. Every full Fourier projection in the active orbit is injective. The final text explicitly restricts to that orbit; other characters vanish. |
| Could exact Hecke balance fix the model? | No. Tensoring with regular group data and applying the generic corner preserves the intrinsic defect in every block. The Wedderburn component has dimension dim(e_psi V_alpha) dim V_alpha. |
| Does the no-go exclude every exponential estimate regardless of scale? | No. Final scope is failure of any uniform o(sqrt(sigma)) bound from the stated abstract properties. The consequence for an exponential bound additionally compares sigma with the chosen large parameter. No full-source scale realization is claimed. |
| Is the actual word-prime level hyperspecial? | Rejected. The two primitive split components with norm of valuation one produce the distinguished-column congruence, hence K_1 after conjugation. The ambient lattice computation includes the inverse and residue characteristic two. |
| Is complete splitting contained in HidaSetting itself? | No. The local theorem is explicitly at a split place with v(T_u)=1. The same-data eventual-family supplier residEv_of_GL and its assumptions are cited. |
| Are both primitive split components supplied? | Yes, under Fu_fixed and the integral orthogonal split. Scalar saturation localizes at both CM primes, and self-duality makes the second component a primitive covector. |
| Does row versus column K_1 require changing representations? | No. With d=diag(I,varpi^-1), K_col=d K_1 d^-1. Fixed dimensions belong to the same representation. |
| Does the conductor cutoff require genericity? | No. Atobe-Kondo-Yasuda covers every irreducible smooth complex representation over a characteristic-zero local field. Weight one forces the single tuple (0,...,0,1). |
| Is the exact spherical interval count valid with repeated Satake parameters? | Accepted independently by Astra and Sol. Superlevel intervals are nested or gap-separated; Zelevinsky applies to segment subrepresentations, which here are determinant characters. Repeated equal characters give k singleton intervals, not one. |
| Can GGP nonvanishing determine the source matrix ranks? | No. The theorem's existential scope, actual conjugated row, character match, packet and selected tests must be kept. A vanishing central value gives a conditional exclusion; nonzero values alone do not handle the selected tests or outer-integral phases. |
| Does the necessary graph-rank bound require orthogonal slices? | Literal support in surviving slices does. The final note specifies an orthogonal decomposition and also gives the annihilator formulation, which yields the same dimension bound for a direct sum. |
| Would a complete nonzero-entry graph suffice? | No. The Sol opponent supplied a Fourier-basis version of the incidence model with all matrix entries nonzero and the same positive defect. The added paper example labels its row lines as artificial, not actual automorphic constituents. |

## Program review and outcome

Both programs were independently frozen from PREREG.md before comparison, published at b83250a7db82d2a27de932617fb39f61cf6af823, and read back. Both first scientific runs passed A-D, as recorded in RESULTS.md.

No scientific-program error or mathematical falsifier fired. One driver preflight stopped before executing the development program because a hash was transcribed with 65 characters. CUSTODY.md preserves the stop and verifies equality of the unchanged author, public and local file bytes before the first execution.

## Remaining open obligations

The actual local conductor and Satake parameters of all global source constituents have not been enumerated. The source-specific Bessel tests, their compatible global constituents and the ranks after outer averaging have not been evaluated. The existing coarse Gram estimate remains available; an exponential improvement for the weighted intrinsic block defect is open.

No conclusion about RH, no new Lean verification, no public promotion and no Canon change follows from this round.
