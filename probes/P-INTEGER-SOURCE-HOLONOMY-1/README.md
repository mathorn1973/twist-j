# Integer source holonomy: first complete apparatus

NON-CANONICAL, L1. A conditional construction toward an integer gravity
program, with an exact obstruction to a direct fixed-precision K1 bridge.

**Outcome:** a complete source-controlled Hermitian loop with an occupied
receiver, explicit reversible update and positive arithmetic resource
account was constructed and passed its first pinned exact audit. The two
separately written implementations agreed on all complete certificates.
This is not a derived spacetime metric or general relativity.

Ownership: https://github.com/mathorn1973/twist-j/issues/1632

## Read the result

- [RESULT.md](RESULT.md): findings, actual finite evidence, scope and next obligations.
- [PROOF.md](PROOF.md): universal algebra, funding inverse, K1 denominator theorem and exact representation boundaries.
- [PREREG.md](PREREG.md): the complete frozen state, equations, tests and falsifiers, published before any run.
- [SOURCE.md](SOURCE.md): v103 authority, source custody and every NEW_DECLARED admission.
- [RUN.md](RUN.md), [EXPECTED.txt](EXPECTED.txt), [FROZEN.sha256](FROZEN.sha256): run provenance, literal stdout and immutable-input hashes.

The public PR's checks and description carry the observed x86_64/aarch64
job readbacks for the final reviewed head. That evidence is distinct from
the first local run and does not create a Canon promotion.

## Reproduce

From the repository root, using Python 3.12 and the standard library:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-INTEGER-SOURCE-HOLONOMY-1/verify.py
```

The entry point runs its own author audit and then the independent
`breaker.py` in a separate process. Successful output must be byte-for-byte
identical to EXPECTED.txt. All assertions are exact; no floating-point
tolerance is used. A scientific FAIL remains a completed scientific record
and is not repaired under the sealed identifier.

## The construction

Work over O=Z[j], phi=-j^2-j^3 and J=1+j^2. A=diag(J,phi) preserves
the determinant of a Hermitian register by congruence. Together with
B(q)=[[1,q],[0,1]], the source-selected loop is

```text
A B(q) A^-1 B(-q) = [[1,q(-2+j-j^2)],[0,1]].
```

The complete state stores source s, link control q, pointer H, reference
R, detector Z, phase p, bank b and direction epsilon. A six-phase bare
bijection exchanges s/q, traverses the loop, and adds H-R to Z. The actual
map funds each elementary operation using E=1+s^2-sq+q^2+N(H)+N(R)+N(Z),
where N(H)=Tr_(Q(j)/Q)(tr(H^2)). If a step is unaffordable, it reverses
the stored direction. The full map is bijective and preserves E+b.

For the same occupied detector with Z01=j, the prepared source signs
-1 and +1 require sharp banks 716 and 772. Their final j coefficients
are zero and two, so a fixed reading returns the sign. Old detector
contents can be reconstructed from the retained full state.

## The bridge boundary

For every declared K1 source word and n>=1, the least common denominator
d_n of the exact rational K1 slice obeys

```text
v_3(d_n)=4(n-1).
```

This is proved for every counter. The computation checks all ten words
through counter 24 as an audit. No fixed denominator works for the full
history. Since every fixed-energy shell of the selected apparatus is
finite, even an arbitrary fixed rational current-state reader on such a
shell cannot produce a complete K1 history.

The next construction must state how precision/history resources enter
the complete state, and how a pointer transport becomes a metric and a
geometric source law. The current bank is a chosen arithmetic account;
the phase is chosen control storage. Neither has yet been admitted as
native energy or physical time.
