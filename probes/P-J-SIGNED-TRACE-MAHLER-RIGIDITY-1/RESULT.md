# P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1 result

Status: **candidate-T / L1 / J-SIGNED-TRACE-MAHLER-RIGIDITY-CONFIRMED /
PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes. No
scientific falsifier fired and no threshold moved.

## Result

Let

```text
f(X)=X^4-3X^3+bX^2+cX+1 in Z[X],  b,c even,
tau=phi^2=(3+sqrt(5))/2.
```

If `f` has no unit-circle root and exactly two roots outside and two inside the
unit circle, counted with multiplicity, then

```text
M(f) >= tau,
```

with equality if and only if

```text
f(X)=Phi_5(X-1)=X^4-3X^3+4X^2-2X+1.
```

The theorem is global. Its universal quantifier is carried by the exact
sign/exterior-resolvent proof in `PREREG.md`, not by a finite scan. The
verifier audits the complete coefficient surface containing every possible
counterexample with `M(f)<=tau`.

## Frozen A0-A3 ladder

The four preregistered decisions are

```text
A0 SINGER             FALSE
A1 ORIENTED           FALSE
A2 SIGNED TRACE       TRUE, unique equality f_J
A3 DISPLACEMENT UNIT  TRUE, the A2 corollary
```

The broad primitive order-15 binary class does not select `f_J` by this
Mahler-minimality criterion. The exact strict-lower witness

```text
h(X)=X^4-X^3+1
```

lies already in A1 and satisfies `M(h)<=sqrt(3)<tau`. The distinct polynomial
`f_J(-X)` is an A1 equality tie, and the reciprocal of `f_J` is the matching
`p_L` equality tie in A0. Thus both the lower bound and uniqueness fail before
signed trace is imposed.

## Exact audit

```text
binary p_L/p_R controls       PASS, irreducible and exact order 15
target controls               PASS, 2/2 split, Phi_5 shift, H factor
A0 coefficient candidates    3300
A1 coefficient candidates    1650

A2 coefficient candidates     165
H root strictly outside       127
residual root profiles          8 with one outside
                                1 with two outside
                               29 with three outside
unit-circle residuals           0
unique 2/2 survivor             (b,c)=(4,-2)

A3 coefficient candidates      11
H root strictly outside        10
unique residual/survivor        (b,c)=(4,-2)
```

The Cayley/Bezout route counts the roots of `f` relative to the unit circle;
the independent Sturm component detects strict exterior-resolvent roots
outside `[-3,3]`. Endpoints are retained exactly, with no float or tolerance.

## Why the status ceiling is candidate-T

The written proof establishes the universal A2 inequality and unique equality
case, including the exact negative-sign gap

```text
M > (3+sqrt(13))/2 > tau.
```

The finite verifier is an audit of every possible at-or-below-threshold
coefficient row and of all exact controls. This combination supports a later
`T` row at L1 after the required public two-architecture gate and separate
Canon fold. A3 earns no additional claim because `f(1)=1` is unnecessary.

## Scope firewall

This result classifies characteristic polynomials only. It does not classify
integral matrix conjugacy, ideal classes, marked lifts, bases, or integral
realizations. Signed trace is sufficient only inside the frozen A0-A3 ladder;
it is not derived from `J`, not claimed necessary outside that ladder, and not
a selector of an exponent, orientation, prime, binary place, or physical
carrier.

No decoder, event, apparatus, probability, Born law, dynamics, entropy,
spacetime, force, SI value, physical generation count, or L2-L6 lift is
assumed or concluded. In particular, the trace value three is not a reading
of `GENERATIONS-L3`.

```text
SAMPLING NOT PROVIDED.
```

## Publication boundary

This probe changes no Canon, registry, frontier, dependency, evidence, gate,
status, tag, or release file. It seals the mathematical result and its
evidence only. The maximum later public use is one separately locked row:

```text
J-SIGNED-TRACE-MAHLER-RIGIDITY [T], L1.
```

The public claim lock is issue 562 and the immutable preregistration pin is
`95b3faf0b257f649e64e1adf728b6982719a6e59`.
