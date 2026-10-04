# Lambda-six decoder: public interface contract for independent review

Provisional public probe `P-J-LAMBDA6-DECODER-INTERFACE-1`. L1 arithmetic; NON-CANONICAL. This contract may be read before either implementation is frozen. It contains no author implementation or private test answers. No scientific execution is authorized by this document: the coordinator must first release authority/collisions and publish the formal preregistration/verifier pin. The old rational-modulus-25 probe remains unchanged.

## Mathematical carrier and exact representation

`O=Z[zeta]`, `1+zeta+zeta^2+zeta^3+zeta^4=0`, coefficient order `(1,zeta,zeta^2,zeta^3)`, `lambda=1-zeta`, `J=1+zeta^2`, `phi=-zeta^2-zeta^3`. Scalar equality is literal equality of four integer coefficients. Domain `A941={alpha in O:1<=N(alpha)<=941}`; this includes every J translate, with no sign restriction on its integer exponent.

For `alpha=(a,b,c,d)`:

```text
u=a*a-a*b+b*b-b*c+c*c-c*d+d*d
v=a*b-a*c-a*d+b*c-b*d+c*d
N=u*u+u*v-v*v
S0=2*u+v, S1=3*u-v.
```

A syntactically well-formed reading is `(s0,s1,r)`, with two arbitrary exact integers and six canonical integers `r=(r0,...,r5)`, each in `[0,4]`. The digits are least significant first and denote `sum(r_i*lambda^i) mod lambda^6 O`. They are neither base-five original coordinates nor a rational-modulus residue. Well-formed readings need not belong to the image of A941.

Canonical digits are defined uniquely by repeated reduction modulo lambda: the next digit is the coefficient sum modulo five, subtract that integer constant, and divide by lambda in O. Exact ideal congruence is the equality relation. In particular `(5)=(lambda)^4`, not an equality of those generators.

## Python public API, fixed names

`Scalar` is a tuple of four integers and `Digits` a tuple of six integers. Public scalar/digit arguments accept tuple or list, with exact specified length; elements must have `type(value) is int`. Booleans, floats, strings, generators, and wrong lengths are rejected. Results always use tuples. There is no coercion, implicit residue reduction, or acceptance of noncanonical digits.

`InvalidReading` is a subclass of `ValueError`. Malformed readings or readings outside the exact image are rejected by this exception; exact message text is not part of the contract. Malformed or out-of-domain arguments to `encode` raise `ValueError`. No result is silently approximated.

```text
encode(alpha) -> (s0, s1, digits)
decode(s0, s1, digits) -> Decoded
T6(s0, s1, digits) -> (new_s0, new_s1, new_digits)
T6_inverse(s0, s1, digits) -> (new_s0, new_s1, new_digits)
```

`encode` is defined on all and only A941 and returns the exact observation `D6(alpha)`. A returned frozen `Decoded` record has exactly these fields:

```text
coefficients: Scalar       # original alpha
strip_coefficients: Scalar # unique beta with 0<=v(beta)<u(beta)
unit_exponent: int         # alpha=J^unit_exponent beta; may be negative
norm: int                 # N(alpha)=N(beta)
```

`decode` is a total recognizer/inverse: for every syntactically or semantically invalid reading it terminates by raising InvalidReading; for every exact image reading it terminates with the unique original alpha and the specified normalized data. For every alpha in A941, `decode(*encode(alpha)).coefficients==alpha`. For every accepted reading, `encode(decoded.coefficients)` equals the original reading exactly. An invalid datum changed into another valid datum is not a detectable corruption under this contract.

The oriented strip is half-open: include `v=0` and exclude `u=v`; equivalently include `A/B=1` and exclude `A/B=phi^4`. No altered bound, strip, finite unit orbit, restricted sign of exponent, or selected codebook is permitted.

## Exact data dynamics

T6 and T6_inverse act on ALL syntactically well-formed readings, even readings not in the exact image; they reject malformed inputs. Their equations are

```text
T6(s0,s1,r)         = (s1, 3*s1-s0, digits(J*representative(r)))
T6_inverse(s0,s1,r) = (3*s0-s1, s0, digits(J^-1*representative(r))).
```

All residue operations take place in `O/lambda^6 O`, and `J^-1=-zeta-zeta^2`. Both compositions are the identity on every well-formed reading. They preserve exact-image membership in both directions. On every alpha in A941:

```text
T6(*encode(alpha)) == encode(J*alpha)
T6_inverse(*encode(alpha)) == encode(J^-1*alpha).
```

Normalization transports traces and the residue together by these inverse data maps. A decoder proof must cover integral but nonrepresentable trace pairs, positivity/norm rejection, both strip boundaries, termination before representability is known, and reversal of every normalization step.

The residue ring has cardinality `5^6` and characteristic 25: `5*1` is nonzero, whereas `25*1` is zero. Therefore its additive group is not isomorphic to the additive group of `F5^6`. Six base-five digits give a set representation only; data operators must carry in the ideal ring, not use componentwise arithmetic modulo five. There is no claim of running-time or total apparatus-resource improvement.

## Independent review and scientific limits

The independent reviewer must freeze its own arithmetic, ideal test, adversarial test design and verifier bytes before reading the author's `decoder.py` or `primary.py` (the latter was provisionally named verify.py before coordinator integration). The reviewer may use this public contract and already exposed public mathematical sources. Its later program may call the public API as a black box; author-implementation exposure after its own freeze must be recorded. The coordinator's `verify.py` wrapper enforces the public input manifest and runs both author and independent verifiers. Static source/proof review is separate from pre-pin scientific execution.

The inherited norm inequality establishes injectivity because equal traces imply `N(alpha-beta)<=16*941=15056`, whereas a nonzero element of lambda^6 O has norm at least `5^6=15625`. The inherited exact strip bound is `[-8,8]^4`. These are disclosed proof inputs, not blind predictions. The proof must establish image recognition as well as uniqueness. No claim of physical measurement, noise correction, finite storage of unbounded traces, preferred dictionary, or minimality among other observation types is made.
