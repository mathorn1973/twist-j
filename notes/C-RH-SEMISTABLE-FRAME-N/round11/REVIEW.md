# Round 11 paper review and evidence boundary

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: C-RH-SEMISTABLE-FRAME-N.
Session: ChatGPT-Astra-Sol-20261123-R11.
Public issue #2070 and existing draft PR #2071.

## 1. Scoped outcome

The two Astra paper lanes and the Sol global-period reader accept the
following deductions after the corrections below:

- **candidate-D:** the actual split odd-hook pair is neutral, and its
  twisted Jacquet module is nonzero exactly when h_v>=2*r_S+1.
  This is an identification and application of classical theory.
- **candidate-D, conditional on the genuine full geometric and parameter
  suppliers:** h_v=n_G for every contributing row at every split finite
  place where it is spherical. Therefore the particular locally excluded
  V_bad of round 10 is zero.
- **candidate-D:** for an individual embedded smooth automorphic row and
  compact smaller quotient, nonzero full Fourier coefficient of the fixed
  rational type is equivalent to a nonzero period against some
  unrestricted smaller automorphic constituent.
- **Open:** the full global kernel and the required sum-of-ranks bound on
  every target subspace for the actual selected P_u.

The result is stronger than the referee's proposed h_v>=n_G-1, because
the source's all-adjacent-gap lemma excludes even a single unit gap.
It does not turn local visibility into a selected global nonvanishing
or concentration theorem.

## 2. Internal review roles

The coordinator integrated source correspondence, proof and dispositions.
An Astra development reader checked the source's actual full HH, gap
supplier, discrete-series normalization and Labesse hypotheses.
A second Astra independently opposed the local equivalence, spectral
argument, transfer and Satake-annulus deductions. A Sol reader checked
the global GGP theorem, the fixed-type visibility lemma and the final
rank quantifiers.

This is same-session internal paper opposition. The reviewers could read
the proof; it is not a blind code confirmation, an external referee
report, a Lean proof or a two-architecture computation. All three
reviewers returned scoped approval with the corrections recorded here.

## 3. Challenges and dispositions

| Challenge | Disposition |
|---|---|
| Does the source character really give a neutral model? | The split middle space is Fz plus ker(ell), with ell(z)=-T_u!=0. The long chain and zero complement give the odd hook and an even neutral grading with g_1=0. The first-superdiagonal trace character agrees with log. |
| Does the r_S=0 boundary violate the orbit argument? | Corrected explicitly. Ranks allows m=2; then N=1 and A=H=0. The local equivalence is automatic. Only for r_S>=1 does setting ell(z)=0 change the stated Jordan type. |
| Is the 1987 theorem enough for all smaller orbits? | Attribution corrected: the maximal-orbit result is used through GGS's precise restatement; GGS Theorem E provides the interior-orbit converse. The full 1987 publisher text was not read here. |
| Does highest derivative mean exactly the defined Satake count? | The spherical representation is the irreducible induction attached to the unlinked degree-one height intervals. Endpoint truncation has order equal to their number, including repeated singleton intervals. No temperedness assumption is hidden. |
| Does the flag converse use the right dimension and character convention? | Corrected the filling space to the k-dimensional zero-chain complement ker(ell). On the left orbit N/H_x the functional integrates against chi, so L(n.f)=chi(n)L(f). |
| Can a nonzero Jacquet module of an orbit subquotient disappear in the representation? | Exactness of twisted Jacquet on complex smooth unipotent representations is stated and justified. Right exactness alone would be inadequate. |
| Could there be a unit gap at the join of the two weight lists? | The actual row_parameter_gaps_large proof explicitly covers the join. Cl=0 yields every gap greater than n_G*m^10. No inference from a nonempty word set or integrality of Delta is needed. |
| Is lamS the Harish-Chandra parameter or the lowest K-type? | The source specifies the latter through a shifted formula. The classical minimal-K-type identity recovers lambda_S as the Harish-Chandra parameter. Integrality of lambda_S-rho also follows from mu-2*rho_noncompact. |
| Does finite-dimensionality apply only to selected rows? | FinX.finHH applies to the entire bounded-convolution range on automorphic L2. Spectral projections preserve that range; a continuous component would create infinitely many orthogonal nonzero images. Actual RowsBij suppliers identify the infinity type. |
| Is base change known only at almost all places? | Labesse Corollary 5.3 explicitly matches every unramified or split place, including the selected T_u places. Regular algebraic weight and real degree at least two supply the stated case. Arbitrary abstract D7 data do not. |
| Can Speh shifts use a different normalization or cancel? | With |z|_C=z*bar(z), neighboring holomorphic infinitesimal-character entries in every nontrivial Speh block differ by one. This is not an angular-character exponent. Multiset union does not cancel entries. |
| Can different cuspidal factors have adjacent local parameters? | The strict Jacquet-Shalika annulus is the same for every factor. A ratio of absolute value q or q^(-1) is impossible even across factors. The original closed-half-plane holomorphy statement was checked. |
| Is a local factor itself cuspidal? | Wording corrected to the local component of a global cuspidal factor. The Rankin-Selberg argument uses the contragredient, avoiding the ambiguous phrase unitary dual. |
| Which big cell is stable under the actual N? | The auxiliary proof now names U^+ w_0 B/B with B containing N and U^+=N semidirect-product U_M. This avoids the alternate opposite-cell convention. |
| Does BPC imply a period for every larger representation? | No. Its existence theorem begins with a given discrete Hermitian pair and a nonzero central value; the form and automorphic members are existential. Its refined theorem additionally needs an everywhere-tempered cuspidal pair and selected-vector factors. |
| Does our transfer verify all BPC assumptions? | No. It alone proves neither cuspidality of every row, the discrete-Hermitian Asai conditions for a selected pair, nor everywhere temperedness. These are not silently supplied. |
| Does the unrestricted visibility lemma descend to the quotient? | H(F) normalizes N and preserves psi. The function on compact [H] has a nonzero spectral component; pairing with its conjugate gives a Bessel period in the bilinear convention. Apply it to an individual embedded copy. |
| Does one successful copy eliminate multiplicity kernels? | No. The note explicitly retains actual isotypic kernel directions and does not infer a rank statement from isomorphism classes. |
| Does representation-level distinction force selected-vector nonvanishing? | No. Other tensor factors can be chosen so the remaining scalar functional is nonzero, and that functional still has nonzero kernel in dimension at least two. |
| Is the final rank inequality merely sufficient? | It is exactly equivalent to the concentration bound by the earlier dual-rank identity. The common-global-kernel mass bound is only necessary. |

## 4. Explicit boundary of the new theorem

The conclusion h_v=n_G uses all of the following:

1. The actual unitary automorphic realization, the bounded source
   convolution, the full finite range, and the supplied correspondence
   with the abstract target. It does not follow from an abstract matrix
   witness without those identifications.
2. The actual parameter family or its explicit all-gap hypotheses,
   the matching discrete series at all real places, and the real field
   degree f>=2. The proof recovers the required Harish-Chandra
   normalization from the supplied minimal type.
3. Labesse's discrete base-change theorem with its stated regular-weight
   hypotheses, the GL discrete-spectrum classification, and the strict
   Jacquet-Shalika bound for the unitary cuspidal factors.
4. A split finite place at which the contributing row is spherical.
   This is the local setting of the round 10 bad-type definition.

The conclusion excludes a specified local obstruction. It makes no claim
that all global Fourier coefficients are injective, all selected periods
are nonzero, the rows are everywhere tempered, or the RH proof has been
simplified to an established algebraic concentration estimate.

For positive epsilon_* it is enough, as a necessary first condition, to
control dim(K_glob)/D by epsilon_*. Exact zero is stronger than required.
The simultaneous inequality for every target subspace remains the actual
task. The sharp abstract counterexample from round 9 is unchanged.

## 5. Custody and execution boundary

The public basis and selected live-source comparison are recorded in
SOURCE_MAP.md. Round 11 began from the immutable round 10 delivery tree.
Only round11/ and the candidate's parent index/handoff are changed.
All earlier frozen preregistrations, programs, first-run records and
proofs remain untouched.

The referee's note reports finite-field checks. Their counts are not
claimed as this team's executions, independent confirmations or Lean
verification. No new scientific computation was planned or run in round
11, so no new verifier, breaker, PREREG or candidate-C execution record
is created. Repository integrity checks are delivery checks, not
scientific evidence.

The files are newly written English mathematical exposition, review
dispositions and links. No third-party PDF or implementation is imported.
The work remains under the existing named item and draft PR, with no
Canon, registry, workflow, release, merge or authority changes.
