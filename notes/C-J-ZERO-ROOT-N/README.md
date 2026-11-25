# Relative phase code, zero layers and a native two-digit write

**NON-CANONICAL / L1 / no authority.**
Analytical statements: candidate-T. New finite execution: candidate-C.
Owner: A. M. Thorn / codex-zero-root-20261125. Reservation: #2097.
Package: [PROMO-C-J-ZERO-ROOT-N.md](PROMO-C-J-ZERO-ROOT-N.md).

The proposed quadratic trace code and all-625-state relative reconstruction
are correct in their stated arithmetic setting. The relative reader has
the simpler exact form of an integer coefficient contrast. A supplied
25-input preparation also makes the unchanged native U write two actual
relative residues into two initially blank pistons after three ticks.
Existing phase references then give one fixed current-state reader,
without access to the counter or saved history, for every later tick.

## What has been established

| Result | Exact scope |
| --- | --- |
| Integral reconstruction | In O=Z[j], D_k=10n_(-k)-2 sum n_i and (D_k-D_0)/5=2(n_(-k)-n_0), for x=sum n_i rho^i. |
| All residue states | Four relative values modulo5 bijectively label all 625 states of O/5O. |
| Square-zero layer | Exactly 25 classes, x=sqrt5(a+b Delta), Delta=j^2-j^3. The characteristic-zero ring itself has no nonzero square-zero elements. |
| Raw quadratic code | F_k=D_k/5=c+2bk+3ak^2 modulo5; 125 raw words including the lift offset c, code [5,3,3]. |
| Full hierarchy | Anchored codes [4,4-r,r+1] and adjacent codes [5,4-r,r+2] on ell^r R_4, r=0,...,3. |
| Hermitian kernel | On R_m, the displayed pair has a five-element top-layer kernel exactly for even m; odd m has zero kernel. |
| Original native write | For E(u,v)=(-2u-v-3,0,v,0,3,2u), actual a,c,e gives (0,r_1,1,r_4,4,1+2u), with r_1=v-2u and r_4=-v. |
| Fixed retained reading | From cut3, AB and CD are invariant for A=p1+p1p, B=p4+p4p, C=p1-p1p-2, D=p4-p4p-1. The native sum z distinguishes the three initial BLANK cuts from PRESENT records on this prepared family. |
| Zero and absence boundary | E(0,0) gives PRESENT(0,0). A raw six-zero launch is outside the family and gives PRESENT(0,3); this is not a general absence detector. Four pistons without z cannot implement the declared readiness schedule. |
| Canonical source boundary | The natural four-coefficient source with common (q,r)=(0,1) has the same whole (q,r) history for all 25 root-layer inputs. The new preparation and piston port are different. |

Read [PROOF.md](PROOF.md) for the arithmetic proof and precise error models,
and [NATIVE-PROOF.md](NATIVE-PROOF.md) for the full-state native construction,
inverse and all-time continuation. [reference-PROOF.md](reference-PROOF.md)
proves the fixed current-state reader and its two negative controls.
The frozen executable checks are
[verify.py](verify.py), [break.py](break.py) and
[native_verify.py](native_verify.py), with the extending
[reference_verify.py](reference_verify.py). The two arithmetic implementations
were written separately from the frozen preregistration without reading
one another's source, but they belong to the same parent session and do
not constitute independent external confirmation.

## Executed evidence

Both arithmetic programs exit zero with empty stderr and byte-identical
451-byte [EXPECTED.txt](EXPECTED.txt). They cover all 625 states and every
ideal layer, all 125 raw quadratic codewords, all 1,250 three-phase
reconstructions, all 2,500 single raw-symbol errors, and all 500
single-symbol errors in the adjacent 25-word code.

The native audit exits zero with empty stderr and the exact 295-byte
[NATIVE-EXPECTED.txt](NATIVE-EXPECTED.txt). It checks all 25 inputs,
1,625 complete cuts, 1,600 complete transitions and inverses, and 1,550
tail readings and whole-state reconstructions through cut64. The natural
source control retains one common receiver history. The all-time claim
has a written invariant proof; it is not a horizon extrapolation.

The reference supplement exits zero with empty stderr and the exact
345-byte [REFERENCE-EXPECTED.txt](REFERENCE-EXPECTED.txt). It checks the
same 1,625 cuts: 75 BLANK readings and 1,550 correct PRESENT readings,
including 62 retained zero records. It verifies the invariant products,
the equal 25 four-piston projections at cuts2 and8, and the raw all-zero
control. This supplement reuses the frozen native implementation and
target evaluator; it is an extension, not an independent second native audit.

Commands, immutable pins, hashes and the single local architecture are in
[RUN.md](RUN.md). Ordinary repository CI is distinct from scientific
execution of these notes. No public two-architecture computation gate or
Canon promotion is claimed.

## Limits that matter

The raw c offset is not a third hidden state digit. Correlated errors
created by differencing must not be assigned an independent-symbol noise
guarantee. An error-correcting code exists here as a mathematical
construction; no autonomous native repair law has been demonstrated.

The native writer's correlated preparation is supplied, its capacity is
25 inputs, and its raw receiver is literal at cut3. The original
clock-assisted reader retains the data thereafter. The stronger reference
reader removes the counter from the observation interface by reading
four current pistons and the six-coordinate sum. The counter remains
in the native evolution. Neither observation is a physical detector or
an internally implemented decoder circuit. No arbitrary-625-input native
writer, autonomous repair or renewal protocol is asserted.

The original audit note and scripts requested by the owner remain
unrecovered. [PROVENANCE.md](PROVENANCE.md) preserves the four known
reservations and explicitly marks the missing original authorship,
coverage and file bytes. This new work is not substituted for that audit.
