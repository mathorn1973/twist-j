# External review and author response

NON-CANONICAL / L1. Date: 2026-11-09. Overall disposition:
**Conditional / text-level consistent.** The all-parameter claims remain
candidate-T; this review does not supply unconditional analytical acceptance.

This is a coordinator-written English record of the external AI-assisted review reported
through A. M. Thorn, including Emmy's assessment, Thorn's subsequent assessment
and the author response. It is not a byte copy of an original Emmy report or
an independently signed source-hash attestation. The
[earlier same-session review](https://github.com/mathorn1973/twist-j/blob/33a393e3af8344b31c1e6bedc8e5638be6aa8b26/notes/C-SIGN-TRANSPORT-RECORD-CONSOLIDATION-N/REVIEW.md)
is preserved separately at its original commit.

## Reviewed source and method

Emmy manually reviewed the
[analytical construction at 33a393e3](https://github.com/mathorn1973/twist-j/blob/33a393e3af8344b31c1e6bedc8e5638be6aa8b26/notes/C-SIGN-TRANSPORT-RECORD-CONSOLIDATION-N/CONSTRUCTION.md).
The review was textual and mathematical. It did not run the scientific
verifier, formalize the argument in Lean, or independently compare source
hashes. An auxiliary numerical check attempted during the review produced
no usable result and supplies no evidence here.

Emmy was not a coauthor of this new construction. Her role, if any, in the
predecessor primitive and network probes is not established by this record.
This scope is distinct from the author-side static reviews and from the
separately recorded two-architecture finite audit.

The reported checks covered:

- The total B involution, its admitted branches and refusal behavior.
- The common-preparation encoder and emissions {1,3} versus {2,3}.
- The positive and negative return tables and their common return period.
- The whole-data-rail alias that defeats an unqualified instantaneous reader.
- The counted clock, local receiver windows and intermediate-layer boundaries.
- The stated complete resource totals and supplied architecture's scope.

## Conditional verdict and retained requests

Emmy's reported final verdict was **Conditional / text-level consistent**.
She retained two requests for the presentation:

1. Make coefficient conjugation and exact evaluation of the gate guards explicit.
2. Display the stepwise H/E account, beyond its initial and final totals.

After receiving the author's source citations and algebraic expansions,
Thorn accepted the coefficient-conjugation formula and the per-gate
Delta H=0 argument. His assessment is that these are exposition requests,
not missing mathematical conservation proofs. He nevertheless retained the
overall conditional candidate-T disposition.

These positions are recorded separately. Thorn's assessment is not treated
as Emmy withdrawing either request or granting unconditional acceptance.
The following response makes the existing definitions and conservation
argument explicit without changing the frozen construction.

## Author response: exact conjugation and guards

[Frozen PROOF.md, line 61](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md#L61)
defines h(z)=z conjugate(z). In O=Z[j], complex conjugation sends j to
j^(-1)=j^4. For z=c0+c1*j+c2*j^2+c3*j^3 it is therefore

    conjugate(z) = (c0-c1) - c1*j + (c3-c1)*j^2 + (c2-c1)*j^3.

The [frozen verifier, lines 74-81](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L74)
contains this coefficient map followed by exact multiplication for h.
Multiplication reduces modulo 1+j+j^2+j^3+j^4; equality is equality of the
four integer coefficients. The parity guard checks that all coefficients
of both pair differences are even. On that domain, the balance guards
compare h(v) with g*h(u), or h(u) with g*h(v), exactly, with the stated
nonzero conditions. The clarified factor is g=J conjugate(J)=2-phi,
and g^(-1)=1+phi. No approximate norm test is substituted.

## Author response: every gate and layer conserves the account

[Frozen PROOF.md, lines 92-95](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md#L92)
already states the local argument: the accepted branch exchanges h(u) and
h(v), while the centers c,d remain fixed. In expanded form,

    H_four = 2*h(c)+2*h(d)+2*h(u)+2*h(v).

On the forward branch h(v)=g*h(u), so

    Delta H = 2*((g-1)*h(u)+(g^(-1)-1)*h(v)) = 0.

On the reverse branch h(u)=g*h(v), so

    Delta H = 2*((g^(-1)-1)*h(u)+(g-1)*h(v)) = 0.

All refusal branches are identity. Each marked pair sum is fixed, so S is
preserved; E=Tr(H)/2 is preserved by linearity. This is a full-carrier
per-gate proof, not merely an equality between prepared endpoints.

All source, interface and conveyor gates are this same B. The clock adds
only disjoint B blocks in the joint conveyor layers. Unchanged cells retain
their accounts; summing disjoint blocks and composing layers preserves S,H,E
after every gate and layer. The frozen proof states this explicitly at
[line 486](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md#L486).
The displayed total accounts evaluate that invariant on the preparation.

## Author-side source custody and limits

The coordinator compared the original construction with the
[frozen PROOF.md at 015c6b6f](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md).
Their mathematical bodies, from the section 1 heading up to the section 11
heading, are byte identical: 21,029 bytes, SHA-256
`4fb14655a213c75ce6b69978b7fe064c7f4d461e4ec99464a56b66203579edb8`.
The original complete construction is 23,394 bytes, SHA-256
`0c4631607466abec0a9c66535cc1e47702454321598e2c2fc17012d4afaf608c`;
the complete frozen proof is 24,103 bytes, SHA-256
`d7ffeaf4b9e2a9f528fcaaecfc945cd9f7eea30ac8f868734dbf406f9f5a0f39`.
This is author-side custody evidence, not a comparison attested by Emmy.

PREREG.md, PROOF.md and verify.py remain unchanged at the frozen source pin.
The clarifications above change no gate, preparation, schedule, reader,
account, theorem scope, finite audit inventory or expected output. They do
not retroactively make the review unconditional. The finite audit remains
candidate-C evidence; the supplied architecture and reader remain candidate-D.
The remote record is occupied-region delay memory, not a stationary point
latch or a physical detector theorem. PR #1973 remains a draft; no Canon,
registry or release promotion is asserted by this record.
