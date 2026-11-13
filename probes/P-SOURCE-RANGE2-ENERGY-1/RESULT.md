# Completed diameter-two test: both settings inconclusive

**NON-CANONICAL. L1. Exact finite calculation under the pinned source premises.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1786](https://github.com/mathorn1973/twist-j/issues/1786).

Status: INCONCLUSIVE

The first execution of the publicly pinned verifier completed with exit zero,
empty stderr and `integrity=PASS`. It returned **LT for both signs** against
the preregistered squared threshold 5041/6272640000. Consequently both
per-sign dispositions and the overall disposition are INCONCLUSIVE.
No result, parameter or comparison was replaced after execution.

## Exact observations

Let D=4263532100619551101772231049835681915283203125. The unchanged
[EXPECTED.txt](EXPECTED.txt) records

```text
||v_+||² = (78528199745274604061507737570049654784
           +2970736380666141011876915666864963584 sqrt(5))/D
||v_-||² = (34308575708192801632564975453994614784
           +1166135837836318555548930117389123584 sqrt(5))/D
```

| Setting | Exact comparison with (71/79200)² | Disposition |
|---|---|---|
| Original psi_+ | Strictly smaller | INCONCLUSIVE |
| Original psi_- | Strictly smaller | INCONCLUSIVE |

The internal propagation retained all paths through seed powers -12 to 12.
Forward support counts were
`2,10,72,308,944,1958,3484,5518,8556,12326,17064,22894,29708`;
backward counts were
`2,8,28,85,302,722,1672,3048,4906,7704,11218,15672,21174`.
Every iterate passed its exact norm, support and parity checks, and every
nonzero iterate returned to its predecessor under the opposite step with
the required factor 625. Both source normalizations and the pinned second
and real fourth seed moments also passed. These checks validate the stated
finite computation; they do not independently establish its inherited
physical premises.

## Scientific implication

The fixed certificate used rho=2, ell=2, N=8 and the projection onto carrier
positions c<=90 or c>=104. Its rigorous uniform remainder is 1/15840.
The lower bound in [PROOF.md](PROOF.md), equation (A4), is not large enough
to exclude energy-action error below E0/1200 for either setting.

This failure of a sufficient bound does not show that any diameter-two
Hamiltonian meets that error, that the actual forbidden tail is small, or
that a change of source, energy, encoding or threshold is justified.
The diameter-two question remains open. The original source family,
all 26 old-memory labels and passive references are retained.

The conditional diameter-one obstruction in
[PR1785](https://github.com/mathorn1973/twist-j/pull/1785) at
`19f1c74a27684a22bf038c1e6fc1133f638fb613` is unaffected. The broader
positive finite constructions and their unresolved geometric locality
obligation are also unaffected. No new positive physical realization or
general no-go theorem follows from this result.

## Why increasing the cutoff alone cannot rescue this test

The following analytical deduction uses the completed exact output and the
already pinned remainder bound. It is not a new scientific run or a changed
acceptance comparison.

For both printed squared norms (a+b sqrt(5))/D, the positive integers obey
`a<79*10^36`, `b<3*10^36` and `D>4*10^45`. Since sqrt(5)<3,

    ||v_sigma||² < 22/10^9 < 1/6000².

Let F_sigma=P_4 b_2(U)f(U)psi_sigma be the infinite filtered vector in
PROOF.md, before its Fourier truncation. The same remainder estimate gives
`||F_sigma-v_sigma||<=1/15840`, hence

    ||F_sigma|| < 1/6000 + 1/15840
                < 1/6000 + 1/15000
                = 7/30000 < 1/1200.

Consequently no larger Fourier cutoff with this same ell=2 filter and
P_4 projection can certify the required obstruction through a valid bound
of the form `||v_sigma,N||-r_(2,N)`: that lower bound cannot exceed
`||F_sigma||`. This upper bound concerns only the selected filtered dual
signal. It is not an upper bound on the full forbidden energy tail
`||P_2 f(U)psi_sigma||`, nor does it establish a local realization.

The next analytical priority is a stronger dual test of the full forbidden
occupation output, including the object-parity channel omitted by this
carrier-only projection. Such a test needs its own derivation, declared
projection, verifier and public pin. It is not a revised outcome of this
probe; no such successor computation is claimed here.

## Custody and acceptance

The scientific pin is `c4584bb481e369338c2f90d2c2e7fd4eed3aec54`.
The verifier SHA-256 is
`17206c5fa79a0d9f0f3adbdffc0623e1b58bef930274ca8ba7ab2f3dd5c710c8`.
All three pinned files were read back from the public branch byte for byte
before the first scientific execution. Syntax compilation and static source
review were the only pre-pin checks. The first completed stdout is 936 bytes,
19 lines, SHA-256
`d91c1e680b7a081a5cc2c80d4912849fa649cf0f564dffd56e3e4ce38d1d216a`.
[RUN.md](RUN.md) records the local execution. Subsequent unchanged replays
are reproduction, not new selected scientific trials.

Required two-architecture CI evidence belongs in the pull request once
earned. No external independent review or Canon promotion is claimed.
Only this probe directory changes; Public Canon v105 remains the authority.
