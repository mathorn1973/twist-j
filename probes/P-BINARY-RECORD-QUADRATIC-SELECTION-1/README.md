# Binary records and quadratic selection

The [proof](PROOF.md) classifies an exact elementary relation family and
refutes two unrestricted structural routes to a Born square. The
[preregistration](PREREG.md) and verifier were published together at
`c157fa9258ed01fb71320feba5a2c223daeb749e` before execution. The mathematical
proofs and witnesses were already known; the audit is openly result-exposed.

The main conclusions are:

- Equality-only k-ary relations decompose into equality-pattern orbits of
  falling-factorial size. Their complete injection-stable atomic valuation
  class is stated in the proof.
- Binary matched records permit W=a*d+b*d*(d-1); a square requires a=b.
- A total reversible covariant writer with fresh cells can retain its source
  and every older record while producing the diagonal, linear-size graph.
- On the adopted v80 integer channels, an infinite power family obeys the
  listed scalar symmetries and zero laws; one explicit LOW pair is 1/11 versus
  1/6. Full frame/record conformance is not asserted for the alternative.
- Nonzero unsigned counting cannot remain nonnegative and biadditive on the
  whole signed group completion.

Run from the repository root with Python >=3.10:

```text
python3 probes/P-BINARY-RECORD-QUADRATIC-SELECTION-1/verify.py
```

The finite audit uses only standard-library exact integers and rational
arithmetic. It has 109538 checks and must match [EXPECTED.txt](EXPECTED.txt)
byte for byte with exit 0 and empty stderr. See [RUN.md](RUN.md) for the public
pin and actual local environment, and [RESULT.md](RESULT.md) for disposition.
The arbitrary-size statements are proved, not inferred from enumeration.

This is L1 mathematics and a symbolic writer. It does not claim that the
alternative reader or writer is physically realized, falsify Born's empirical
rule, or close any QDD physical owner. The motivating research program is
[NON-CANONICAL incubation #884](https://github.com/mathorn1973/twist-j/pull/884).
