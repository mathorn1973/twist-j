# R3 is confirmed; the finite-history obstruction applies

Status: PASS (R3_CONFIRMED).
PUBLIC / NON-CANONICAL / L1. A. M. Thorn, 2026-10-18.
SPDX-License-Identifier: Apache-2.0.

The pinned first run gives exactly

    rank_F3(Bbar^705 Dbar_v)=2.

Both separately authored implementations agree on every entry of the
705-by-2 image, and both rank algorithms return two. This completes the
sole preregistered finite condition. The all-finite-word consequence
below uses the written proof that was fixed and independently reviewed
before that condition was evaluated.

The local finite result is earned; the required public two-architecture
computation gate is supplied by the draft PR's exact-head workflow.
No public replay is predeclared by this result record. The mathematical
all-word claim remains a non-canonical candidate for theorem review,
with no automatic Canon or physical promotion.

## Exact certificate and custody

Public preregistration pin:

    3c4855829770229b87d6c86740a215f78b213056

[PREREG.md](PREREG.md), both programs, the domain, source manifest,
[PROOF.md](PROOF.md) and prospective [REVIEW.md](REVIEW.md) were pushed,
publicly read back byte for byte and fetched as a Git commit before the
first scientific run. All eight remain unchanged.

The first two lexicographic output rows, at zero-based indices 0 and 1,
are

| Index | Domain coordinate | Image row |
| ---: | --- | --- |
| 0 | (-8,0,0) | (1,1) |
| 1 | (-8,1,1) | (2,0) |

Their determinant is 1*0-1*2=-2=1 mod3, so the image has rank at least
two. It has only two columns, hence rank exactly two. This is the
preregistered first nonzero minor, not a witness chosen by a new search
after changing the test.

- Full image: all 705 rows are present in [EXPECTED.txt](EXPECTED.txt).
- Canonical image TSV SHA-256:
  e4caba49d46afe390e06cc4703f482701a042268c412e833f95f64f730f2411d.
- Reduced operator nonzero entries: 15742.
- Scientific stdout: 5210 bytes, one line, SHA-256
  92b0c3fefdc0b4e24c1ea4532057adef7bf8a8654e288ec7cb07d47fe79208ce.
- First run: Ubuntu 24.04.3 LTS, x86_64, CPython 3.12.14; exit zero,
  empty stderr; elapsed 1.422278 seconds within the frozen 600-second limit.

[RUN.md](RUN.md) contains the actual times, neutral environment, public
commit metadata, exact file and stream hashes, and clean-checkout custody.

The separate code and proof review contexts also inspected this actual
stdout after completion. They checked its hash, complete image dimensions,
the stated minor and its application to the unchanged conditional proof.
This is exposed result review, not an additional architecture run.

## Consequence for every finite actual history

Use the literal amplitude map F of the supplied apparatus, its actual
two-free-step contact spacing, and

    T=F^2,
    H_pair=ker(T-I)=ker(F-I) direct_sum ker(F+I).

Each effective accepted impulse has source coordinate alpha in
|alpha_1|<=2, |alpha_2|<=3. Refusal has effective coordinate zero;
an accepted zero impulse can still affect its retained control sign.

R3 now establishes the previously conditional statement in
[PROOF.md sections 4-7](PROOF.md): for every nonzero effective impulse
and every age j>=0,

    v3(T^j D_src alpha)
      =v3(v(T^j D_src alpha))
      =nu(alpha)-8j,   nu(alpha) in {0,1}.

The oldest nonzero impulse in any finite effective word has a unique
lowest valuation, separated from every younger term by at least seven.
Its contribution cannot cancel. The sum w satisfies (T-I)w!=0.

For EVERY initial pure pair z_in in H_pair, the endpoint of an actual
finite guarded history has the form

    z_out=F^M z_in+F^r w,
    (T-I)z_out=F^r(T-I)w.

F is invertible. Therefore, once a history contains a nonzero effective
accepted impulse, every subsequent finite cut lies outside H_pair.
It cannot return to a pure pair or to zero. This includes initial pure
pairs with occupied tapes. It covers arbitrary guard selections, native
counter values, source labels, buffers, signs, capacities and refusals
that the actual apparatus permits, because their effective words form
a subset of the larger class already proved.

This is not an extrapolation from sampled contact histories. The only
finite computation is the stable-kernel rank condition. The universal
step is the unchanged valuation argument, exposed to review before the
result. No semisimplicity of the reduced map over F3 is assumed.

## What the bank must include

The supplied positive quadratic form splits by its orthogonal pure-pair
projection:

    E_cl(z_out)=E_pair,out+E_perp,out.

For an initial pure pair with energy E_in, the actual funded contact
and recorded work preserve

    E_pair,out+E_perp,out+b_out=E_in+b_in,
    W_out-W_in=b_in-b_out=E_pair,out-E_in+E_perp,out.

After a nonzero effective history, the proven obstruction gives

    E_perp,out>0

at every finite later cut. A two-mode account that discards this
component is therefore incomplete for those histories. At a fixed
pure-pair projection, the algebraic minimum obtained by discarding the
complement is not attained by such a history.

A falling pair energy can still offset this positive complementary term.
Consequently this result does not fix the sign of the net bank
withdrawal. It provides no uniform positive energy gap, no approximation
rate and no asymptotic lower bound.

For a completely zero initial amplitude, E_in=0 gives the sharper
corollary b_in-b_out=E_pair,out+E_perp,out>0 after a nonzero effective
history. The full initial deposit cannot return to the bank at any
finite later cut. This follows directly from the pinned proof and
account, not from an additional computation. W records the same energy
change and is not added as a separate energy reservoir.

The occupied-state guard uses the full initial account:

    E_in+b_in-B <= E_star <= E_in+b_in.

Blank-preparation funding simplifications are not extended to arbitrary
occupied initial pairs.

## Falsifiers and surviving limits

No preregistered scientific falsifier fired: the rank is two, the full
images and ranks agree, source/data hashes and structural checks pass,
the run exits zero and stderr is empty. No threshold, source, domain,
exponent, alphabet, timing, verifier or proof was changed after the pin.

The following are outside the earned conclusion:

- histories containing only zero effective impulses, which retain free
  amplitude evolution even if control signs change;
- arbitrary initial amplitude states outside H_pair;
- unbounded rational impulse alphabets or a different timing schedule;
- infinite-time limits, arbitrarily close approximation and a uniform
  positive residual-energy lower bound;
- a native preparation theorem or admission of the supplied rational
  contact as an operation of the original native TWIST U;
- the physical channel (0,pi)->(pi/2,pi/2), its particle/bank/controller
  translation, and identification of any term with 2*sqrt(1+m^2)-2m.

#1596 therefore retains its STOP_UNTYPED boundary. #1605's previous
analytical results and #1610's fixed review target are not rewritten.
The earlier Hilbert value 3/20 and seven-dimensional closure are
separate analytical statements, not computational results of this probe.
The exact m/atan(m)>1 is preserved; its existence-cost or entropy
interpretation remains a hypothesis.

## Result-directed next obligation

For this fixed apparatus, a nonzero finite contact history cannot be
closed exactly within the pure pair. A continuing account must retain
the complementary amplitude energy, or explicitly declare and justify
a changed operation, alphabet or schedule before testing its effect.
The remaining native bridge must independently type the particle,
bank and controller carriers and their energy units. The present
positive complementary term is not itself that missing translation.
