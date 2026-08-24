# C-QDD-MATTERDATA-MINIMAL-SCHEMA-1-N

Status: NON-CANONICAL incubation. No public authority.
Target line: PUBLIC basis, no repository write.
Basis: Public Canon v61.
Main readback: bbfaec744ab635b75a195be46b6799f9eaf07dbd.
Content commit: 76b405033b41397cd62217bf3998ac9c26111964.
Canon SHA-256: e9ee0781e489e1c3951b978be567a19c5c7370708095631f966561efe03b6cb5.
Canon bytes: 334100.

## Question

Which subsets of the five frozen MatterData_QDD fields retain the complete direct-record equality on K_QDD? Is the current five-field record minimal?

## Frozen fields

For D_QDD_direct, use the five top-level fields exactly as registered:

- S = support_state,
- M = total_weight,
- B = branch_weights, the ordered raw pair (LOW,HIGH),
- R = density_state, ZERO_DENOMINATOR or DENSITY(matrix),
- N = normalized_weight_state, ZERO_DENOMINATOR or NORMALIZED(pair).

For a subset A of {S,M,B,R,N}, let D_A be the projected typed subrecord. Call A record-complete when

    D_A(x)=D_A(y) iff D_QDD_direct(x)=D_QDD_direct(y)

for all x,y in K_QDD.

## Preregistered targets

S1. Exactly 12 of the 32 field subsets are record-complete.

S2. A subset is record-complete iff it contains R and at least one of M or B.

S3. The inclusion-minimal record-complete subsets are exactly

    {M,R} and {B,R}.

S4. Sufficiency proof:

- M+R reconstructs Q=vv^T on SUPPORTED by A=M rho G^-1; the R tag handles ZERO.
- B+R reconstructs M by M=w_low+w_high, then applies the first clause.
- Once Q is reconstructed, the complete direct record is fixed.

S5. Necessity proof uses two exact frozen witnesses:

- Without R: v=(1,0,0,1) and v'=(1,1,0,0) have the same S,M,B,N but different Q and density.
- With R but without M and B: v=(1,0,0,0) and 2v=(2,0,0,0) have the same S,R,N but different M and Q.

S6. The five-field schema is therefore redundant as an equality carrier. R is indispensable; one raw scale-bearing field is indispensable; S and N are never needed for record completeness; M and B are interchangeable for equality because sum(B)=M.

## Required guards

- This classifies equality information only. It does not authorize deletion of fields from the public schema, because field ownership and downstream typing are separate design questions.
- No physical measure, Born probability, apparatus, event, stream, decoder completion, SI, or layer lift.
- The conclusion is conditional on the frozen direct Route A record and its exact field types.
- Branch ordering inside B remains frozen; no LOW/HIGH swap is allowed.

## Falsifiers

F1. The exact complete-subset count differs from 12.
F2. One subset outside the stated condition is complete, or one inside is incomplete.
F3. Either minimal set fails to reconstruct full equality.
F4. A proper subset of {M,R} or {B,R} is complete.
F5. Either necessity witness fails under the direct field arithmetic.
F6. The proof imports a Born/measure premise or changes field equality.

## Status rule

Complete proof plus exact exhaustive audit: candidate-T. Audit alone: candidate-C. Any F1-F6 falsifies the frozen proposal.
