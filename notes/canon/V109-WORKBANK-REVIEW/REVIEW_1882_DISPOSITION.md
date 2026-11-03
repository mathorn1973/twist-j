# Disposition of the separate workbank reviews in PR1882

NON-CANONICAL / L1. Proposed v109 proof clarification and review disposition.
No frozen probe, Canon claim, registry entry, tag or release changes here.

## Evidence reviewed

[PR1882](https://github.com/mathorn1973/twist-j/pull/1882) at
`c9ab9cfdab202e677053c289bc94c46ff548af9b` contains a completed computational
comparison and a separate mathematical proof review of PR1879 at
`d6a5f77169d1027a22959c41aa5a45a783643a3e`. The review folder is
`notes/C-RELATIVE-CONTACT-WORKBANK-REUSE-REVIEW-1/`. Its draft packaging is
not itself a negative mathematical verdict. Conversely its COMMENTED review
submission is not an APPROVED merge submission. Source integration and final
Canon release remain separate reviewed actions under the repository protocol.

The implementation report gives PASS WITH NOTES and no real disagreement.
It reconstructs the program from block definitions, compares all 1000 complete
three-input endpoints and inverses, and after unblinding identifies its word
with the same 535-contact fixture. Its RLE/cache traversal has the same
403050000-contact inventory but does not visit every literal contact in all
trajectories; the original PR1879 verifier does. The report explicitly
separates these mechanisms and the author's finer internal checkpoints.

The mathematical report examines 90 statements: 75 hold, eight have an
expositional gap, six are finite computations, and one unqualified archive
retention sentence is false when read as including the literal inverse.
It finds no false mathematical lemma and accepts the finite-k induction as
complete, conditional on the four specific clarification points below.
Its own supplementary program is not included: quoted sample and finite
outputs are reported review evidence, not a new reproducible artifact here.

The review declares a blind implementation phase and separate mathematical
assessment. Preserve that declaration and the explicit limited exposure;
do not confuse these new artifacts with the earlier copier-author report
whose authorship correction is retained in README.md. This integration's
static checks are not another independent mathematical verdict.

## Exact custody and chronology

The current review payloads were read from the exact commit above. All seven
entries in its SHA256SUMS match. The later mathematical review is outside
that older manifest, so its exact hash is recorded independently here.

| Review-relative file | Bytes | SHA-256 |
| --- | ---: | --- |
| `PREREG.md` | 15092 | `4e0ff6ccd685649dfd56bf3ab4e6292e14f6501c60d892fd74ae9bb48e30da33` |
| `review.py` | 39558 | `faef109eb9499d6df9673e7946350f9a38b9fc65ec529a977d8241583ca95ffb` |
| `RESULT.md` | 7415 | `6834c1f3f372a307c0e85b9707ff181140466443ff791893fed07229a0c44bf6` |
| `COMPARISON.json` | 14300 | `c58f08f9cd6d179e0ef3ed4d86dfa5b7cbd47cced7b0bd758b23ac4f3442ddad` |
| `RUN-REVIEW.txt` | 1690 | `cd39721409a5542045459af4f2dedcbee5b84c201cf0b5a5ed771a041156d3de` |
| `mathreview/MATHEMATICAL-REVIEW.md` | 44303 | `3fbb38594502a88863bb83fffc5ac2f31b969174552097db46b5e9ef30d904c3` |

README.md, PREREG.md and review.py are byte-identical to public freeze
`7bc66bcc315c5a9d13595d2698212c2d8cbc9b4b`. The README at that freeze already
reports the first implementation runs. Therefore this Git pin establishes
custody before the repeated phase-two run and unblinding, not public
preregistration before the very first execution. Local preregistration before
that first execution is the reviewer's reported chronology. No stronger
public-first-run claim is made.

PR1882's successful notes CI is repository-integrity evidence, not execution
of review.py. The original PR1879 science was separately replayed on both
architectures in run41680260019; README.md records the actual jobs and hashes.
The reviewer's inability to inspect those logs does not negate that separately
verified evidence. No supplied reviewer program was executed in this
integration; no source exposure or output is presented as newly prospective.

## 1. P1.2: make the half-trace identity explicit

Let K=Q(j), j a primitive fifth root, and z=sum_(i=0..3) a_i*j^i with
integer coefficients. For an exponent m in [-3,3], Tr_K/Q(j^m) is 4 if
m=0 and -1 otherwise. Expanding z*bar(z) gives

    Tr(z*bar(z)) = 4 sum_i a_i^2 - sum_(i!=k) a_i*a_k
                 = 5 sum_i a_i^2 - (sum_i a_i)^2.

Thus the account in PR1879 is exactly Q(z)=Tr(z*bar(z))/2. For a carrier
with H=sum_l z_l*bar(z_l), E=sum_l Q(z_l)=Tr(H)/2. Preservation of the full
Hermitian H therefore implies preservation of E. Multiplication by rho=j^2
preserves z*bar(z), since rho*bar(rho)=1. This also anchors the equal accounts
of the five bank phases. These are direct identities and agree with the
existing RELATIVE-CONTACT-INTEGRAL-LAW [T]; no sampled calculation is needed.

## 2. P5.1/R2: separate the word definition from its finite identification

Define S by the chronological blocks in PR1879 PROOF section 5. Its algebraic
proof applies to that defined word. Identifying the expanded list with
WORD535.txt is a separate finite transcription check: all 535 ordered pairs,
after the stated one-based/zero-based conversion, must agree.

The original frozen verifier checks the fixture against its block-built word;
both required architecture replays passed. The separate PR1882 comparison
also reports token-by-token equality after its blind word construction, and
the mathematical review reports the same literal comparison. The fixture
SHA-256 is
`ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b`.

A v109 fold must label this identification as finite exact list comparison,
with those distinct evidence sources, rather than deriving byte identity
from an abstract group argument. This distinction changes neither S nor the
already executed program. No additional scientific run is claimed here.

## 3. P5.8: supply the missing F16 coset argument

Work in O/2O=F16. Write rho=j^2, H=<rho>, w=1+rho and b=1+rho^2.
The order of rho is five. Characteristic two gives b=w^2 and

    w^3=(1+rho)(1+rho^2)=1+rho+rho^2+rho^3=rho^4.

If w=rho^t, then 3t=4 modulo five, hence t=3. That would imply
1+rho+rho^3=0; subtracting this from Phi_5(rho)=0 in characteristic two
gives rho^2+rho^4=0, or rho^2=1, contrary to order five. Thus w is not in H.
Also w and b are nonzero. If H*w and H*b met, some rho^a*w=rho^d*b
would give w=rho^(a-d), using b=w^2, again a contradiction. Therefore the
clock and memory cosets are disjoint. This supplies precisely the bridge
used to reject inactive clock-memory contacts; it proves no larger decoder
or arbitrary occupied-bank write property.

## 4. P5.13: prove the shortened inverse word

Use chronological left-to-right words, as in PR1879. Put A=A0 and B=Bc.
For E=A B A^4 B^4, reverse the literal contacts and replace each by its
fourth power. The unreduced inverse word is

    B^16 A^16 B^4 A^4.

Because A^5=B^5=id on the complete carrier, B^16=B and A^16=A. Thus
E^-1=B A B^4 A^4, exactly the ten-contact block used in the construction.
This is a global word identity, including refused and diagonal contacts;
it does not rely on random test states. O2^4 is likewise the exact inverse
of O2. The surrounding read proof can therefore use these inverse blocks
on the actual occupied checkpoint, as stated.

## 5. R8/A2: retain the exact time horizon

The wording to use in the v109 synthesis is:

> During the forward program P_k, once an archive's copy has completed,
> no subsequent primitive of that forward program addresses it, erases its
> record, or returns it to M_empty. The literal inverse P_k^-1 deliberately
> erases the records and restores blank archives; it is not a reset that
> preserves the records.

For k=3 the three fresh archive pairs become two, one, zero at complete
cycle boundaries. This is a property of the declared forward protocol,
not a monotone state function of all reversible dynamics. Original PR1879
RESULT.md and PROOF section 7 already give the forward-only scope. The
unqualified README sentence and the first preregistration retention sentence
are qualified here for the proposed fold; frozen source bytes stay intact.

## 6. A3/S2 and the quantified conclusion

Before a separate Canon decision, say "candidate proof by induction of a
family for every specified finite horizon", not an unqualified "proved
family". State the quantifiers explicitly:

    for each k>=1 fixed in advance, there exists its carrier and fixed P_k,
    such that every input tuple in I^k satisfies the stated endpoint.

The carrier has 26+25k slots, account 68+74k, and 2k initially fresh permanent
banks. No one fixed finite carrier or program is supplied for all k.
Use "four-place / two-pair copy obstruction" to distinguish that theorem
from the unrelated canonical four-auxiliary-slot preparation minimum.

The review confirms the finite-k induction without another mechanism being
missing: restored ready core, disjoint future archives, actual input parking
and untouched complete complements are precisely its induction hypotheses.
The 1000-tuple computation is the separately frozen k=3 audit; it is not the
proof for general k. Account 290, six archive banks with account180, and two
fresh target banks per retained experiment remain unchanged. They are
initial stock accounts, not burned energy, and give no storage optimum.

## Release disposition

The four derivation bridges and the retention/terminology corrections above
are concrete proposed fold text. They address the specific findings without
altering sealed PR1879 or manufacturing a new reviewer run. The existing
three candidate scopes in CLAIMS.md keep their precise falsifiers. Accepted
mathematics, computational corroboration, reviewer provenance and the final
reviewed release decision must remain distinct.

The separate native receiver/carry candidate PR1884 is not covered by these
reviews and still needs its own mathematical assessment. Its F5 carrier,
explicit routing and native origins must not be silently identified with
this contact-bank apparatus. No native physical interconnect, occupied-archive
regeneration, autonomous input choice or indefinite operation is closed here.
