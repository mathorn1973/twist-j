# Independent review: general quadratic two-coordinate readout

NON-CANONICAL / L1 / candidate-T.

Original mathematical review by a separate collaborating agent within the
authoring session, with the candidate formulas disclosed. This is not an
external independent audit. Author A. M. Thorn, Apache-2.0.

Reviewed scope: the 550 states of the jointly prepared family used in
PR #1536, with six required meanings BLANK and PRESENT(k), k in F5,
and an arbitrary fixed decoder. Completed audits were not rerun.

## Criterion

For any proposed pair (P,Q), a suitable decoder exists if and only if
each fiber of the restricted map (P,Q):S->F5² is monochromatic under
the required label L:S->{BLANK,PRESENT(0),...,PRESENT(4)}. Equivalently,

    L(x) != L(y) => (P(x),Q(x)) != (P(y),Q(y))  for every x,y in S.

Necessity follows because a function cannot decode one code to two
meanings; sufficiency defines the decoder on each nonempty fiber and
extends it arbitrarily to unused codes. The criterion does not require
the 25 blank preparations to have a common raw pair (P,Q).

## Checked construction

In F5, set

    A=a+c, B=b+d, C=a-c-2, D=b-d-1,
    z=a+b+c+d+q+r.

The first coordinate is linear and the second is quadratic:

    P=A+2z,
    Q=(1+2B)D+3BC.

Use the total decoder

    delta(P,Q)=BLANK              if P=0,
                 PRESENT(-P²Q)   otherwise.

At x0 and x2=x0, the established prefix gives A=1,B=0,z=2,D=mu.
Consequently P=0,Q=mu, and the decoded output is BLANK.

At x1, the prefix gives A=3,B=2,z=0,C=lambda. Thus P=3 and
Q=(1+4)D+6C=C=lambda. Since -3²=1 in F5, the decoded output is
PRESENT(lambda).

At every tail point n>=3, B=0: it is zero at x3 and each selected
generator b,d,e sends B to -B. Hence Q=D. The established tail has
A,z in {1,4} and mu=zD/A. Therefore

    P²=A²+4Az+4z²=1-Az+4=-Az,
    -P²Q=AzD=A²(zD/A)=mu.

Since Az is nonzero, P²=-Az is nonzero and this case cannot be decoded
as BLANK. This proves the full prescribed history for all 25
preparations and all times covered by the established synchronized-tail
induction, including all 550 points.

## Adversarial collision checks without enumeration

* Blank versus present: P=0 versus P!=0 separates them exactly.
* First-present versus tail: first-present uses P=3 and Q=lambda.
  A tail code with P=3 has -P²=1, so it necessarily has the same label
  Q=lambda. Their codes may coincide and their required labels agree.
* Two tail points with equal P,Q have equal -P²Q and therefore the
  same required message. Differences in the unused preparation lambda
  and in the remaining tail phase cannot change the decoded value.
* All zero messages remain PRESENT(0) whenever P!=0, whereas blanks
  remain BLANK even when Q=0.

The construction uses all 25 codes on the required set: all five codes
with P=0 are blank; the 20 codes with P!=0 appear in the tail. It is
valid for arbitrary decoding, but does not meet a stronger requirement
that every blank preparation have a common raw reader state.

## Conclusion and limits

No mathematical defect was found in this direct algebraic construction.
It gives polynomial degree at most two, with only one quadratic
coordinate. The established general affine two-coordinate impossibility
then implies that the least polynomial degree in the requested class is
exactly two. The two excluded exact-coding subclasses in PR #1536 are
unchanged and are not contradicted.

This is mathematical readout existence on the stated jointly prepared
family. It does not construct a physical instrument, transmit between
disjoint sectors, create information, or change the native U or Canon.
