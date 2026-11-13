<!-- SPDX-License-Identifier: Apache-2.0 -->

# Disclosed correction of full-field and maximal-real trace notation

NON-CANONICAL / L1 / no authority. Administrative correction record after
the reader-boundary revision also stopped. No complete corrected audit or
independent agreement is asserted here.

## Preserved second failure

The first execution of `break_reader_boundary.py` stopped with exit code 1
in `B:P27:immediate`, forward cut 39, on `B total area trace`. Its frozen
assertion expected 150 while its full-field trace function returned 300.
The exact first output of that revision remains unchanged in
`BREAK_READER_BOUNDARY_EXPECTED.txt`.

Reader-boundary source SHA-256:
`4ddb722421d5596079d1b7bbe6edd1c4e4f8c232d681704fad76a3f17ee8563e`.

Reader-boundary first-output SHA-256:
`c2c34de7f7448896732c60ecae934d9a1f395c05e2020a4bfa7ef817a0ca6ee9`.

The original `break.py`, original `BREAK_EXPECTED.txt`, reader-boundary
source and its failed first output all remain unchanged. The original
stronger memory endpoint assertion remains falsified as documented in
`CHECKER-CORRECTION.md`. The assertion that the FULL field trace of the
active total path area is 150 also remains false and preserved in both
prior sources. Neither failed first execution may be relabelled PASS.

## Exact scope reached before this STOP

Program order and the first failure establish that all 125 A cases
completed their 160 forward and 640 inverse attempts, including the
reader-boundary memory check, per-four-contact inverse restoration,
complete inverse resource return and the final counts of 25 positive
cases and five unchanged pre-reader blanks. This is 100000 A attempts.
No complete final JSON summary was emitted because B later stopped.

For `B:P27:immediate`, all 39 forward attempts passed the all-cut Gauss,
full `H_account` and `E`, charge, integrality, residue, current and ordinary
shadow checks. The initial complete account was 672. The source-only
replay endpoint and fifth-prefix fixture passed, as did source-prefix
non-disturbance, the completed port's source/field return, its exactly two
admissions, and archive retention at subsequent source cuts. The final
original source slots, slot 6 and field returned. The complete current
archive coordinates and norm pair `(0,35)` passed. Before the trace
assertion, the exact area checks passed:

- `H_source = 55 + 20 phi`;
- `H_port = 6 + 8 phi`;
- `H_path = 61 + 28 phi`.

The subsequent explicit doubled-area, source-admission, no-diagonal and
determinant assertions were not reached. No B inverse was executed, and
the other five B path/control runs were not reached. No broader B result
is inferred from this partial execution.

## Literal preregistration and pre-execution clarification

The preregistration uses the unqualified expression
`trace(H_path)=150`. Its field arithmetic and definition
`Q(v)=Tr_K(h(v))/2` use the degree-four field `K=Q(j)`, while `H_path` lies
in its degree-two maximal real subfield. Thus the unqualified word
`trace` does not identify which of these two field traces is intended.
The original checker interpreted that literal as the full degree-four
trace, yielding the false assertion now preserved.

The root session identifies a public clarification posted BEFORE the
first scientific execution in reservation
[#1955, comment 6714667576](https://github.com/mathorn1973/twist-j/issues/1955#issuecomment-6714667576):
150 is the maximal-real trace, equal to half the full `K` trace; the full
`K` trace is 300. The root also reports that `PROOF-PATH.md` states this
distinction. The breaker author was originally restricted to the frozen
preregistration and has not read that proof, the primary implementation,
or the primary output. This record attributes that pre-execution history
to the root session; the source correction below follows directly from
the already fixed exact area coefficients.

For `H = a + b phi`, `Tr_K(H)=4a+2b`, while
`Tr_real(H)=2a+b=Tr_K(H)/2`. Consequently the fixed active area gives
`Tr_K(61+28 phi)=300` and `Tr_real(61+28 phi)=150`. The fixed omitted-port
area gives `Tr_K(55+20 phi)=260` and `Tr_real(55+20 phi)=130`. These are
exact integer consequences of the unchanged area predictions, not
adjustments to their coefficients or tolerances.

## Separate explicit-trace source

`break_explicit_trace.py` retains the disclosed reader-boundary correction.
Relative to `break_reader_boundary.py`, only the trace-check block changes.
The prior active-only assertion

```python
            if selected is not None:
                require(trace(full_area) == 150, "B total area trace", trace(full_area), 150)
                require(scale(full_area, 2) == scalar_phi(122, 56), "B doubled area")
```

is replaced with two explicitly named trace assertions, covering active
and omitted ports. Exact division is checked without floating arithmetic:

```python
            full_k_trace = trace(full_area)
            real_trace, real_trace_remainder = divmod(full_k_trace, 2)
            expected_k_trace = 260 if selected is None else 300
            expected_real_trace = 130 if selected is None else 150
            require(full_k_trace == expected_k_trace, "B full K trace of path area",
                    full_k_trace, expected_k_trace)
            require(real_trace_remainder == 0 and real_trace == expected_real_trace,
                    "B maximal-real trace of path area", [real_trace, real_trace_remainder],
                    expected_real_trace)
            if selected is not None:
                require(scale(full_area, 2) == scalar_phi(122, 56), "B doubled area")
```

Explicit-trace source SHA-256:
`fe4cf5d7c2eb6d89debb1452ed559291b900ec1dde7a6ef12fe7dd5de7e6981c`.

No contact map, carrier, input, source word, port timing, archive response,
physical account, area coefficient or zero-tolerance threshold changes.
All other source bytes remain identical to the reader-boundary revision.
The full trace function used by `Q` and every account check is unchanged.
Every Gauss, account, residue, current, shadow, inverse, determinant and
causal-control assertion remains unchanged. The doubled-area assertion
remains unchanged. The preregistration and both failed prior sources are
preserved rather than rewritten.

This is a second disclosed post-failure checker revision. It is not a new
blind confirmation and cannot erase either previous STOP. At the writing
of this record it has not been executed. The root session must freeze the
new source and this disclosure and publicly record the correction before
its first execution. Any other scientific failure must stop the audit
rather than be adjusted away. Local evidence remains one architecture.
