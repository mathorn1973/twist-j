# Review of the local auxiliary completion

Review verdict: no blocking defect found at the declared scope.
Scope: NON-CANONICAL, NEW_DECLARED L1, conditional candidate-T, a=0 and E_hom=0.
This is same-session, analytically exposed review, not blind external review.

## Review provenance and prospective custody

The reviewer participated in the same-session analytic discussion, separately
checked the scalar identity and commutator signs, and read the complete
PREREG.md, SOURCE.md and PROOF.md before the pin. After the two code authors
completed their separate implementations, the reviewer read both complete
programs against the textual contract. The reviewer did not execute or import
either program or evaluate its fixtures. Familiarity with the proposed result
is disclosed; implementation separation is not independent discovery of the
mathematics.

The public prospective receipt is
https://github.com/mathorn1973/twist-j/issues/1663#issuecomment-6279633121 .
It records publication and byte-for-byte readback of all six frozen files
before scientific execution, at pin
`45648ac0d495a55a6c76e90dfd0fe56e042bf224`, with parent
`8e1f6538a09c8ef012a0a9971d501119f13d52ee`.
The reviewer also read this receipt. FROZEN.sha256 binds the five scientific
source files. The program hashes independently checked during static review
are exactly those in that receipt:

- verify.py: `4e0851457983a344f3ab8d6544b6837abb8df2b06fc89cbd5fad8e4d86f5cd03`.
- breaker.py: `a01328ab545e4ad0c8e5750496e2654b511ef169349e90729969346c29948613`.

The published pin and its files are retained unchanged. This review and the
run documentation are subsequent records, not changes to the preregistration.

## Mathematical review

The weighted decomposition is essential and is implemented as stated:
Q belongs to ker(B^T W), while P maps into ker B^T and satisfies P^T Q=Q.
The auxiliary decomposition, density sum, fixed-endpoint summation by parts,
and scalar second-order identity have consistent signs. The formal pullback
then proves the full off-shell Ward identity without using field equations
or dividing by their residuals. Both auxiliary variations stay in their
original constrained spaces.

The raw commutator is retained as a nonzero off-shell quantity proportional
to neighboring Euler gradients. The skew correction performs zero action
work and cancels that coefficient, including its multiplier derivative at
alpha=0. It is the adjusted generators, not the raw ones, that commute off
shell through order two. Endpoint f=0 is a tangent convention and is not an
extra endpoint equation.

The termwise locality argument proves multiplier-pair radius at most one
uniformly in T. The 900 finite polarizations audit that assertion; they do
not replace its proof. The independent combinatorial counts are 237
state/parameter cases and 900 distant pairs. The dense negative-control
checks were prospective obligations, not assumed outcomes before the run.

The formal coordinate interpretation in RESULT.md is correctly limited.
The multiplier decomposition is invertible on its declared subspaces, and
the field substitution has identity leading term, so it has a formal inverse
modulo epsilon^3 without any finite-epsilon determinant assumption. No new
coordinate is added. This supports equivalence through the stated order to
scalar-lapse mechanics plus algebraic auxiliary pairs. It does not establish
an exact finite-epsilon equivalence, a uniformly local inverse in all orders,
or new gravitational dynamics.

The proof does not require positivity. In particular, setting E_hom=0 does
not establish any nontrivial positive-energy prepared history. Physical
preparation, metric admissibility, higher orders, native U and layer lifts
remain outside the result.

## Implementation and security review

The primary uses exact central polynomial differences and polarization. The
breaker uses product-rule formulas, dual arithmetic, and a separately
assembled action Hessian. Source inspection found no companion-source read,
earlier-probe import, expected payload digest input, or hidden shared runtime
dependency. Both compute the actual transformations and their multiplier
derivatives for the commutator, rather than checking its predicted formula
alone. The eight defect controls test the frozen omissions or sign changes.

The payload order and rational serialization agree with PREREG.md: S then
W/G/B for each state and parameter, followed by L, the two E records, and the
eight N records. Endpoint fields, bond auxiliary variations, and interior
edge variations use the specified flattening ranges. Certificate field order
and the 237/900 counters also match the contract.

The programs use only the Python standard library. Their file reads are the
five declared normative Canon files. The primary invokes only the fixed
standalone breaker with the same interpreter and -I, without a shell. Source
review found no network access, credential access, external mutation, or
unreviewed dependency. Scientific output is written to stdout; the primary
requires the breaker's unmodified bytes, empty stderr and successful exit.

## First-run evidence and remaining acceptance

After the public pin receipt, the coordinator performed the first formal
run recorded in RUN.md. The reviewer subsequently read RUN.md, RESULT.md
and EXPECTED.txt; the reviewer did not perform an additional execution.
That x86_64 run reports exit 0, empty stderr, matching raw implementation
certificates, all 237 case families, 900 locality checks and all eight
detected controls. Its 506-byte, 19-line stdout has SHA-256
`4049702b5a4f64374dd560a45c51889bd7eefdba4ac6f8f52aeae86bb7e3ebd9`.
The common payload digest is
`2d06df6788972c5bf4c9476036d81dea1c991d3822fa7b2e0ca2c176ba94e091`.
No frozen falsifier fired.

At this first-run review, the required x86_64/aarch64 pull-request replay is
pending. Agreement between two implementations in one local run is not by
itself a two-architecture gate, external peer review, or Canon promotion.

The earlier abandoned #1656 and completed-failed #1657 remain unchanged.
The frozen predecessor #1658 and the field-only obstruction #1662 are not
repaired or reopened. This probe explicitly changes the latter's field-only
premise. The separately owned #1659 is not resumed or used as completed
evidence. No previous failure threshold or scientific source is changed.
