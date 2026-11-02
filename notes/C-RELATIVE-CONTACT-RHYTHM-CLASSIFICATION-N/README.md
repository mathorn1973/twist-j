# Contact-triple periods, sharp accounts and reading limits

**NON-CANONICAL / L1 / no authority.**
Candidate: `C-RELATIVE-CONTACT-RHYTHM-CLASSIFICATION-N`.
Owner: A. M. Thorn / Codex-rhythm-publication-20261102.
Reservation: [issue #1854](https://github.com/mathorn1973/twist-j/issues/1854).

For the supplied integral contact on three marked slots, this proposal
classifies every least period and rejection count. It also proves sharp
relative-account bounds and separates a return of the chosen marker from a
return of the complete state. The general results are **candidate-T**;
finite exact audits are **candidate-C** until the applicable public gates.
No public status is changed by this directory.

## Model and result

Let `O=Z[j]`, `1+j+j^2+j^3+j^4=0`, `rho=j^2`. A contact preserves the
pair sum and multiplies its difference by `rho` when the difference belongs
to `2O`; otherwise it is the identity. One tick is `F=C23 C12`, with `C12`
first. This contact and its accounts are inherited from
`RELATIVE-CONTACT-INTEGRAL-LAW [T]` in [the Canon](../../canon/CANON.md).
The three-slot schedule is a supplied premise.

Write `Q(z)=Tr(z*conjugate(z))/2`, `E=sum Q(x_i)`, `S=sum x_i`, and
`M=3E-Q(S)`. For a non-diagonal orbit, let `d` be its **maximum**, over the
whole orbit, of `min(v2(a-b),v2(b-c))`. Let `R` count actual refusals during
one least period; an admitted diagonal identity is not a refusal.
With `A_d=(4^(d+1)-1)/3`, the complete classification is:

| Primitive type | Least period P | Refusals R | Sharp minimum M |
|---|---:|---:|---:|
| One refused edge, one admitted identity | A_d | 4^d | 4*4^d |
| Two refused edges | 2A_d-1 | 2*4^d | 4*4^d |
| One active five-cycle | 5A_d | 5*4^d | 12*4^d |

The complete diagonal is separate: `P=1`, `R=0`, `M=0`. Every other orbit,
including non-diagonal fixed states, satisfies `3P <= 2M-5`.
The proof includes the exact first-return law
`F^(1+4r(y))(2y)=2F(y)` and the sharp eight-tick search for common parity.

The third type has five deepest states, spaced `A_d` ticks apart, while
the complete period is `5A_d`. An explicit pair has equal `E,S,M`, equal
local residues modulo `(1-j)` and identical infinite depth histories,
but periods 5 and 25. Thus unlimited observation of that history need not
recover the complete period.

At fixed `S,M`, coefficient reduction modulo `m` is injective when
`3m^2>M`. The exact shell `E=32,S=4` has 2,895 states. Its smallest
injective integer modulus is 5 and its smallest injective power of two is
8. Coefficient reduction `O/5O` is different from `O/(1-j)`.
The concentration marker gives only 63 infinite-history classes. Exactly
42 samples identify these classes when the shell is known; waiting for two
actual marks can take 81 ticks, including a first sample at tick zero.

## Review and replay

Start with [PROOF.md](PROOF.md), then [PREREG.md](PREREG.md) for the frozen
publication/replay contract, and [SOURCES.md](SOURCES.md) for prior exposure
and the precise code lineage. The pin and actual run are recorded in
[RUN.md](RUN.md). From the repository root:

```sh
python3 -B notes/C-RELATIVE-CONTACT-RHYTHM-CLASSIFICATION-N/verify.py
```

The runner uses only the Python standard library and exact integers. It
executes temporary copies of three audit programs, checks exact stdout and
generated-data hashes, and cross-checks the descent classifier against every
state of the independently enumerated shell. Large generated tables are
temporary, not evidence imported as an archive.

These are adapted, result-exposed implementations. Their agreement is
reproduction and a same-session cross-check, not a blind independent-author
review. The repository's two-architecture `check` validates a notes-only PR
but does not execute its scientific scripts. The local scientific replay
is one x86_64 lane. Promotion requirements are in
[PROMO-C-RELATIVE-CONTACT-RHYTHM-CLASSIFICATION-N.md](PROMO-C-RELATIVE-CONTACT-RHYTHM-CLASSIFICATION-N.md).

## Boundary

The proof concerns the declared three-slot arithmetic dynamics. `Q` is an
arithmetic account, and a tick belongs to the supplied schedule. The note
does not derive this contact from native `U`, identify measured energy or
time, construct the marker-to-bit contact, implement an interval counter,
or fund a retained record and its renewal. The canonical
`RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [O]` remains open.
The five-step excursions replacing refusals belong to the doubled orbit;
the original refusal remains an identity.

All material in this directory is original author project work under the
repository's Apache-2.0 license.
