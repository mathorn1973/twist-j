# P-CM-ALTERNATING-PENCIL-1 adversarial record

Route: no counterexample found. The independent attack program exited zero,
wrote empty standard error, and ended with `RESULT 5/5 ALL PASS`.

```text
source: probes/P-CM-ALTERNATING-PENCIL-1/break_it.py
source_sha256: 0870c628346dcd7499cf453fcbff3c8ed25e370ea316fbd20d9cde0355c82786
source_bytes: 12498
source_lines: 466
command: python3 probes/P-CM-ALTERNATING-PENCIL-1/break_it.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: macOS 26
architecture: aarch64
python: CPython major 3 minor 13 patch 13
run_started_utc: 2026-08-06T10:20:37Z
run_finished_utc: 2026-08-06T10:20:37Z
executions: 1
exit_code: 0
stdout_sha256: 6dc623f6088e0b4a8a68343f12ecaa6c027f6288015d1ba6270803b3602d37e8
stdout_bytes: 338
stdout_lines: 6
stdout_cr_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
public_return: issue 281 comment 5203358233
```

## Attempted attacks

A1 enumerated all 130 units `(+/-1) j^k phi^m` with `0<=k<5` and
`-6<=m<=6`. Exactly the ten elements `+/-j^k` fixed `Omega_1`.

A2 enumerated all `5^6=15625` integral alternating four by four matrices
whose six upper entries lie in `-2..2`, then filtered by Pfaffian `+1` or
`-1`. The full action was tested through `j`, `j^-1`, `phi`, `phi^-1`, `J`,
and `J^-1`, which generate the action together with the trivial sign action.
Preservation here means that the generator and inverse orbit remains in the
rank-two pencil. It does not mean pointwise fixation of one form. Among the
unimodular matrices, orbit containment in the pencil agreed exactly with
pencil membership.

A3 checked all `101^2=10201` pairs with `-50<=a,b<=50`, strictly wider than
the preregistered box, and found no mismatch between the computed Pfaffian
and `a^2-a b-b^2`.

A4 solved the scalar pullback equation for the declared list
`-1,j,j^-1,phi,phi^-1,J,J^-1`. The only scalar multiplier found was `+1`,
and it occurred only for the three listed roots of unity.

A5 used a distinct five-coefficient cyclic quotient representation and the
factorization

```text
lambda_1/5 = j(1+j+j^2)(1-j)/5.
```

It constructed the trace Gram matrix from the inverse-different generator
`(1-j)/5` followed by the displayed unit factor. The resulting matrix agreed
entry by entry with `Omega_1`.

## Exact output

```text
PASS A1 unit search fixes Omega_1 only at the ten roots of unity
PASS A2 small unimodular forms have a pencil orbit exactly in the pencil
PASS A3 wider coefficient box has no Pfaffian mismatch
PASS A4 declared unit scalar pullbacks yield only multiplier +1
PASS A5 inverse-different reconstruction agrees with Omega_1
RESULT 5/5 ALL PASS
```

The attack source imports no code from `verify.py`. No registered falsifier
fired, and no finite threshold was moved.
