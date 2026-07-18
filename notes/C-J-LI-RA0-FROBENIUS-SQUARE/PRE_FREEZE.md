# RA0 Frobenius-square pre-freeze

```text
STATUS:          PRE_FREEZE. NON-FORMAL. NON-CANONICAL.
MACHINE STATUS:  NOT RUN.
CONTROL:         this checkpoint creates no PIN.md, EXPECTED.txt, or RUN.md.
EXECUTION:       the verifier must not be run before a later PIN.md names the
                 immutable preparation commit and repeats its hash and size.
DECISION:        RA0-FROBENIUS-SQUARE is FIRED by the proof-first G0/G7 and
                 K1 arguments; no machine result is claimed here.
BASIS:           Public Canon v8 at d94d4a94976a9b5d27db3a1c586e4886697daabb
                 and notes/j-li-q-moment-n2 at
                 4845f4af44b01eecee423864feff55f627db11c4.
READ-ONLY CHECK: public main bbe751090ef1b832c7674746b140d0a7a8d83570;
                 STATUS there declares Public Canon v9. No v9 content is
                 imported and no status is lifted by this check.
```

The verifier freezes nine exact gates:

```text
R01 finite regression of the encoded root-filter quotient on n <= 125;
R02 finite encoded-identity regression of the von-Mangoldt module and
    counterfeit 5^m tower subtraction on n <= 125;
R03 finite C4 regular-block and trivial-sector determinant algebra;
R04 separate ramified local-5 line;
R05 strict G0 guard: the primitive-output bridge is absent;
R06 finite sanity over integer exponents m=1,...,8 only;
R07 exact K1 kill from the p=2 atom;
R08 finite conditional counting witness (atoms derived, never tabled);
R09 finite coupled-block determinant / Schur-complement identity; the det_2
    reading uses the exactly zero trace of the off-diagonal perturbation.
```

`R01` and `R02` are regression checks of identities encoded on both sides;
they are not independent proofs of the analytic Euler statements.  `R06`
only checks the displayed finite exponent list and does not prove an
infinite-dimensional Schatten assertion.  In `R09`, zero trace makes the
finite-dimensional regularized determinant equal the ordinary determinant;
the infinite operator-ideal lemma remains proof-first.

Machine assertions are integer, `Fraction`, or exact polynomial arithmetic.
There are no floats, external files, network calls, subprocesses, random
inputs, zeta evaluations, zero lists, or prime tables.  Finite multiplicative
atoms are derived by trial division inside the verifier.  This finite
derivation is only a test fixture and does not claim the missing infinite
`J` primitive-output bridge.

The infinite statements (Euler divergence, prime number theorem,
Riemann-von Mangoldt, relative zeta determinant, and operator-ideal lemmas)
remain proof-first imports in the recon document.
