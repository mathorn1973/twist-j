# Separate analytical review

**NON-CANONICAL / L1 / same assisted session.** Date: 2026-10-12.
Reviewer: separate assistant agent, not the package-authoring agent.
Reservation: [#1474](https://github.com/mathorn1973/twist-j/issues/1474).

Disposition: **no blocking mathematical or contract defect found in the
three reviewed files at the hashes below.** This is a written-proof review,
not external peer review, a blind review, a computational audit, a public
gate or Canon promotion. The reviewer belongs to the same assisted session
and has access to its shared source snapshot. No scientific program was
authored, imported, compiled or executed for this review.

## Frozen review inputs

SHA-256 of the exact files read, before this review file was written:

| File | SHA-256 |
|---|---|
| README.md | `8537892100cbaba8869529002aa9f7402cabd8d7ada3119376f6bc08d832c6ce` |
| CONTRACT.md | `7bf56807d4dc9c2f605f91b456d21be99ed6e3d9fd8d0076d7b0cdd00f1e522a` |
| PROOF.md | `a65ed539d8691c08f85fa591773789e4eda87f8b64a27b1d448874b1a333acd5` |

The inherited receiver table, synchronized inverse and increment identity
were compared directly with U-NATIVE-RAW-RESIDUE-READOUT in canon/CANON.md
at public basis `5f54015ed8361e3a64cb10894397020ddfadd104`, lines 5267-5372.
This local source comparison is not a second remote authority/CI audit.

## Checks and reasons

1. **Binary weights and indices.** Substitution of each binary digit into
   the alternating-floor sum gives the stated integer weight
   `(2^(j+1)+(-1)^j)/3`. The four-step weight difference is
   `5*2^(j+1)`, so shifting supports by a multiple of four preserves S
   modulo five. In E_r the second column has exactly `10r-6` terms:
   its upper index is `10r-7`, inclusive. The two columns occupy distinct
   residues 0 and 1 modulo L, even for r=1. Hence E_r has `10r+6`
   bits, even parity, value zero modulo r and S residue one. O_r has
   exactly r bits, odd parity because r is odd, and S residue r.
2. **All-period realization.** Choosing H strictly above the largest
   support exponent separates the unshifted O_r and every shifted E_r
   block. Positive j_* in 1,...,5 supplies every required S residue,
   including zero, while keeping Q positive. Choosing K a sufficiently
   large multiple of L puts 2^K Q above m_0 without carries, preserves
   its digital statistics and makes it divisible by `2^a r=p`.
   Arbitrarily large K establishes the required arbitrarily late times;
   no finite calculation is used for the universal period quantifier.
3. **Actual same-context times.** An arbitrary finite context orbit is
   ultimately periodic even if its update is noninjective. The maximum
   of the 625 source thresholds is finite. From `m=m_0 mod p`, the odd
   time `n=2m+1` satisfies `n=n_0 mod p` directly. This step works for
   even p and never divides by two modulo p. The digital lemma therefore
   applies within a single sufficiently late context value.
4. **Receiver supports and constant target.** Solving the inherited
   inverse gives the stated forward formulas. At the late odd times,
   independently realized theta(m) and S(m) produce exactly both lines
   `q+r=1+c_k` and `q+r=4+c_k`, with all five points on each line.
   The displayed overlaps connect labels 0,2,4,3,1. Equality of a fixed
   reader on each intersection forces all five F(k) to coincide for
   any output set. The explicit k=2/k=4 collision is consistent with
   these same formulas. The converse constant reader is immediate.
5. **Actual driven update and startup.** The input to the transition
   n->n+1 is explicitly theta(n), while z_n stores theta(n-1).
   Thus its equality test produces precisely the canonical delta_n.
   For odd n both consecutive bits differ and the floor argument stays
   fixed; for even n the floor argument increases and the stated
   valuation-parity identity gives the same delta. The three startup
   transitions produce `(sigma_3,z_3,N_3)=(1,1,0)` at tick three.
   Induction gives the actual maintained summary for every n>=3,
   and the fixed inverse table gives the original residue for all 625
   admitted inputs. The primitive update is total on both input bits
   and every listed context, but is not claimed reversible.
6. **Cardinality and resource scope.** `2*2*5+3=23` is a valid explicit
   finite construction. The files consistently present it as an upper
   bound; they do not assert every ready state occurs or prove a lower
   bound. The exposed synchronized driver, readiness convention and
   abstract observer are supplied resources. They are not silently
   included in class A, and no physical acquisition, energy, apparatus,
   absence or source-erasure result is inferred.

The reviewed conclusions are the class-A all-finite-context obstruction
and the class-B explicitly driven existence construction, with their
different interfaces kept fixed. Neither numerical testing nor the older
twenty-summary ambiguity is substituted for the new universal proof.

This disposition applies only to the three byte snapshots above. Any
substantive modification requires a new review pin. Publication, public
readback, scientific execution and promotion remain outside this review.
