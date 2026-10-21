# Even-timed contact: exact R3 test

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.

This probe asks whether the leading mod3 source plane of the literal
705-site apparatus avoids the stable kernel of its reduced propagation:

    rank_F3(Bbar^705 Dbar_v) = 2.

The complete prospective specification is in [PREREG.md](PREREG.md).
The outcome belongs in [RESULT.md](RESULT.md) after the public pinned run;
the exact scientific transcript is [EXPECTED.txt](EXPECTED.txt) and its
custody record is [RUN.md](RUN.md).

## Why this finite question matters

The actual schedule has two free steps between every pair of contact
opportunities. For T=F^2, each nonzero effective impulse belongs to a
fixed bounded integer alphabet. If R3 holds, its age j gives the exact
3-adic valuation nu-8j, with nu in {0,1}. The oldest effective impulse
then has a unique leading layer and cannot cancel with the younger ones.

[PROOF.md](PROOF.md) derives the consequence for every finite history,
without a contact-count cutoff: after a nonzero effective accepted
impulse, a state starting anywhere in ker(F^2-I) cannot end in that pure
pair space at any subsequent finite cut. This includes occupied initial
pure pairs, not arbitrary occupied amplitude states.

For the source's own positive quadratic energy, the complementary
component would consequently retain positive energy. The complete account
would be

    b_in-b_out = E_pair,out-E_in + E_perp,out,

with E_perp,out>0 after a nonzero effective history. This is a finite-cut
statement, not a uniform positive gap, a net-withdrawal sign theorem,
an asymptotic bound or a physical denomination.

A rank below two is a valid retained refutation of R3. It would remove
this particular obstruction proof; it would not construct a returning
native history.

## What is actually checked

[verify.py](verify.py) derives finite neighbours from weighted stencil
displacements. [check_independent.py](check_independent.py), authored in
a separate assistant context before seeing that code, builds unordered
edges from point distances. Both compute every entry of the final
705-by-2 image. The verifier compares the full images, obtains the rank
by two different algorithms and prints the full image plus a deterministic
nonzero minor or kernel direction. No scientific execution precedes the
public immutable pin.

The source definitions and unchanged domain are identified in
[SOURCES.tsv](SOURCES.tsv); [DOMAIN.tsv](DOMAIN.tsv) is the only runtime
data input. The current Canon and original apparatus are not imported.
[REVIEW.md](REVIEW.md) separates pre-run mathematical and code review from
the later computational evidence.

## Connection to the continuing programme

This is a new formal test prompted by #1605's
[APPARATUS-BRIDGE.md](https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/APPARATUS-BRIDGE.md).
Its literal apparatus source is already on public main. The test makes
no change to the prior PR and does not discharge #1596's native-carrier
obligation or change #1610's fixed independent review target.

The channel (0,pi)->(pi/2,pi/2), its missing translation to particles,
bank and controller, and the unit 2*sqrt(1+m^2)-2m remain separate
questions. In particular, positive energy in an apparatus complement
does not by itself identify where that Dirac energy difference is paid.
The exact m/atan(m)>1 result is preserved; an existence-cost or entropy
reading remains a hypothesis.

## Replay after the pin

    LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
      python3 probes/P-EVEN-CONTACT-3ADIC-TEST-1/verify.py

The required PR workflow must reproduce the committed exact stdout on
both x86_64 and aarch64. No merge or Canon fold is part of this probe.
