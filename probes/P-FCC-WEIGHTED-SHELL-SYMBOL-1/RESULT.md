# P-FCC-WEIGHTED-SHELL-SYMBOL-1 result

Status: **candidate-T / L2 / SYMBOL-PROVED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes.
All 15 frozen gates passed. No scientific falsifier fired and no threshold or
coefficient moved.

## Result

For

```text
N = {2,4,8,10,16},
S_n = {v in Z^3 : |v|^2=n},
W* = (w2,w4,w8,w10,w16) = (6,1,15,1,1),
S(k) = sum_(n in N) w_n sum_(v in S_n) (cos(<k,v>)-1),
```

the complete shell sizes are

```text
(|S_2|,|S_4|,|S_8|,|S_10|,|S_16|) = (12,6,12,24,6).
```

The weight `W*` is the unique positive integral solution of minimum total
weight to

```text
-4w2 + 32w4 - 64w8 + 440w10 + 512w16 = 0,
```

and its total weight is 24.

With

```text
M_d(k) = sum_n w_n sum_(v in S_n) <k,v>^d,
```

the exact moments are

```text
M_2 = 648 |k|^2,
M_4 = 3168 |k|^4,
M_6 = 21888 sum_i k_i^6
      + 63360 sum_(i != j) k_i^4 k_j^2
      + 0 k_x^2 k_y^2 k_z^2,
```

where the last sum uses ordered pairs. Therefore

```text
S(k) = -324 |k|^2 + 132 |k|^4 + terms of degree at least six,
```

and the exact sixth-order term is anisotropic. The weighted multiset is
invariant under all 48 signed coordinate permutations.

## Proof and audit split

The finite proof in `PREREG.md` enumerates every shell by the complete square
partitions of the five norms, proves the unique minimum by eliminating every
positive solution of total at most 24, and derives the moment table by signed
permutation symmetry and exact multinomial expansion.

The verifier reconstructs the vectors, group action, bounded weight search,
moments, controls, and deterministic transcript independently. It audits the
written proof; it is not a finite substitute for an unstated continuum or
physical argument.

The sixth-order obstruction is exact: proportionality to
`21888 |k|^6` would require the ordered `k_i^4 k_j^2` coefficient `65664` and
the triple-square coefficient `131328`, whereas the frozen coefficients are
`63360` and `0`.

## Status ceiling

The proof in `PREREG.md` establishes this finite universal shell statement
independently of machine execution. After the required pull-request integrity
and architecture checks, it can support a later public row

```text
FCC-WEIGHTED-SHELL-SYMBOL [T], L2
```

only through a separate sealed Canon fold. Public Canon v71 is unchanged by
this probe.

## Scope firewall

This is one scalar spatial symbol on the displayed `Z^3` carrier. It neither
selects the FCC carrier nor derives `W*`, its scale, or flat flux from `J`, an
architecture, `U`, or a decoder.

It proves no temporal characteristic, Herm2 identification, global or tangent
null cone, Lorentz statement, Gibbs state, roughening, phase, propagator,
polarization, apparatus, continuum limit, or physical photon. It gives no
global remainder bound and consumes no L1, L3, L4, L5, or L6 lift.

## Pin and local run

```text
public claim issue:       #691
preregistration pin:      f4cafb63b4534c8c0864b0935117f2539ad11b07
verifier sha256:          7a853f0940a0c2794e40530270aebfe988a3b3596afb62d46db1bcd6413a1673
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       767
local stdout sha256:      3132f5185ac98f577b3931494c60b781fe381641f00ccd4c0be0574c698e42f6
```

The local run is one architecture lane only. The proposed theorem status is
proof-first; the pull-request workflow remains the required repository
integrity and independent two-architecture audit.
