# PREREG amendment 1: the R7 "For T" bullet

Status: NON-CANONICAL / L1. This amendment is part of the pinned
specification. It was written before the pin and before any execution
under this review.

PREREG.md is not edited. It keeps SHA-256
c4663f4ed3c40026125551b5d46b3aa63ab658d62f94ffe5103523e3e3e89455 from the
freeze commit acf69adba32e838a7891bb8b3c1e4386abaf690f.

## Defect

PREREG section 6, R7, "For T" bullet, reads:

> Q(1+2j-2j^3-1)=Q(j-j^3)=5 and Q(1+j-j^3)=7.

The first equality is false:

- 1+2j-2j^3-1 = T-1 = 2j-2j^3 = 2(j-j^3);
- Q(2x) = 4Q(x), and Q(j-j^3) = (5*2-0)/2 = 5;
- so Q(T-1) = 20, not 5.

The intended object is a = (T-1)/2 = j-j^3, with T = 1+2a. This is the
object STOCK-BOUND.md section 2 uses, and the one the next sentence of the
same bullet already names ("the cyclic product (1+a) abar with a=j-j^3").
The defect is a typing error in the review's own specification. It is not
a property of the target.

## How it was found

Two of the code-free mathematical reviewers of the pre-run lane, S7 and S8,
each in its own fresh context, reported it independently (S7-F1, S8-F1 in
MATHEMATICAL-REVIEW.md). Two adversarial skeptics checked S7-F1, and
neither refuted it. The coordinator rechecked it by hand.

The checker writer had implemented the bullet literally, as two checks:
`T - 1 == j - j^3` and `Q(T - 1) == 5`. Both must fail. The two static
conformance readers did not flag them, because the code matched the frozen
text.

No execution was involved. Nothing under this review had been executed, and
no result of any execution informed the amendment.

## Reading adopted for the run

The bullet is read as follows. The checks are:

- T-1 = 2(j-j^3);
- Q(T-1) = 20;
- a = (T-1)/2 = j-j^3 has Q(a) = 5;
- Q(1+a) = 7;
- the cyclic product (1+a) abar has coefficients (2,0,-2,-1,1), unchanged.

The coordinator changed the four corresponding lines of review.py (the R7
block after "T and S readings") to this reading before the pin.

- **Removed:** the two literal checks above.
- **Added:** `T - 1 == 2(j - j^3)`, `Q(T - 1) == 20` and
  `Q(j - j^3) == 5`.
- **Unchanged:** every other check, case and expected value of R7 and of
  every other item.

The net effect is one more executed check than the literal version would
have had.

Section 10 of PREREG.md applies unchanged to every other item. If R7 fires
for any other reason, the run fails.
