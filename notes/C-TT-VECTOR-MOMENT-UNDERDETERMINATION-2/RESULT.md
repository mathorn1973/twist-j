# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 result

Incubation candidate. No authority. Nothing here promotes anything.
Parent `TT-VECTOR-STATE-NORMALIZATION` stays `[O]` / STOP and is untouched.

Date 2026-08-17. Prereg frozen and hashed before first execution. The first
execution of the pinned verifier is the one reported.

## Verdict

```text
P1  family agreement through degree 3        candidate-T   no falsifier fired
P2  universal degree-4 separator set         candidate-T   no falsifier fired
P3  value table reads the index              candidate-T   no falsifier fired
P4  spectra of the squared readout           candidate-T   no falsifier fired
P5  action table and diagonal collapse       candidate-T   no falsifier fired
P6  degree-5 inventory, the p = 5 signature  candidate-T   no falsifier fired
P7  fixed-modulus cumulant, family-wide      candidate-T   no falsifier fired
parent TT-VECTOR-STATE-NORMALIZATION         [O] / STOP    unchanged
```

Verifier: 40 of 40 gates PASS, exit 0, empty stderr, on both legs.
Breaker: 11 of 11 gates PASS, exit 0, empty stderr, zero breaks, both legs.

## Pins

```text
PREREG.md    sha256 4e2d4b8291d16bd288fa25eccf8d7f04eb8b0ab3df576766c9ca43fd76f4e8f6  11978 B
verify.py    sha256 a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67  13802 B
breaker.py   sha256 1ea4b98e174c5271f17310f76c60dad1051faa512fe2393a58d5297cfb899738   9809 B
EXPECTED.txt sha256 711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c   3013 B
BREAK.txt    sha256 cf6902200fa6bf9a8896dc95099fb5aa3900ce2f1c1eb6ca75d6e8b210e9a642    986 B
```

PREREG.md and verify.py were hashed together before the verifier was executed
for the first time. Both stdout files are byte-identical across the two legs
recorded in `RUN_TWO_ARCH.md`.

## Proofs

Notation as in the preregistration: `z = zeta_5`, monomial
`M = prod_x v_x^{p_x} conj(v_x)^{q_x}`, nets `n_x = p_x - q_x`, degree
`d = sum_x (p_x + q_x)`, `S = sum_x n_x`, `W = sum_x x n_x`.

### Lemma 0, closed forms

Under `A`, site independence and orthogonality of the characters of `Z/5`
give `E_A[M] = prod_x [n_x = 0 mod 5]`. Under `B_m`,
`M = z^{t_0 S} z^{m W} prod_x eps_x^{p_x + q_x}`; averaging over `t_0` gives
the factor `[S = 0 mod 5]`, averaging over the signs gives
`prod_x [p_x + q_x even]`, and the survivor is `z^{m W}`. These are the two
formulas the breaker uses, and BRK-3 binds them to full enumeration on every
monomial of degree at most 5 on all six laws.

### P1

Let `d <= 3`. If some `p_x + q_x` is odd, then `E_{B_m} = 0` for every `m`;
and `E_A = 1` would force `n_x = 0 mod 5` at every site, which with
`|n_x| <= d <= 3 < 5` forces `n_x = 0` and hence every parity even, a
contradiction, so `E_A = 0` too. If every parity is even, `d` is even, so `d`
is 0 or 2. At `d = 0` all laws give 1. At `d = 2` one site carries `(1,1)`,
`(2,0)` or `(0,2)`. For `(1,1)`: `n = 0` everywhere, `S = 0`, `W = 0`, so
`E_A = 1` and `E_{B_m} = z^0 = 1` for every `m`. For `(2,0)` and `(0,2)`:
`E_A = 0`, and `S = 2` or `-2`, not `0 mod 5`, so `E_{B_m} = 0`. Equal in
every case, for every `m`, hence for all fifteen pairs. Linearity extends
this to every polynomial of degree at most 3. QED

### P2 and P3

At `d = 4`, if `E_A = 1` then `|n_x| <= 4 < 5` forces `n_x = 0` everywhere,
hence every parity even, `S = 0`, `W = 0`, hence `E_{B_m} = z^0 = 1` for
every `m`. So wherever `A` reads 1, all six read 1. A separator involving `A`
therefore has `E_A = 0` and needs the `B` survivor: every parity even and
`S = 0 mod 5` with not all `n_x` zero. Degree 4 with even site parities is
one site of weight 4 or two sites of weight 2. One site: `(4,0)`, `(3,1)`,
`(2,2)`, `(1,3)`, `(0,4)` give `S = 4, 2, 0, -2, -4`; only `(2,2)` survives
and it has `n = 0`, so it is no separator. Two sites `x != y`: nets in
`{+2, 0, -2}` with `|S| <= 4`, so `S = 0` forces the pair `(+2, -2)`, which
is exactly `v_x^2 conj(v_y)^2`. That is the twenty.

For a pair `B_m, B_{m'}` with `m != m'`, a separator is a monomial where the
survivor exists and `z^{m W} != z^{m' W}`, that is every parity even,
`S = 0 mod 5`, and `(m - m') W != 0 mod 5`, that is `W != 0 mod 5`. Among the
degree-4 survivors, the single-site `(2,2)` and the two-site `(1,1)(1,1)`
have `n = 0` everywhere, hence `W = 0`; the twenty have `W = 2(x - y)`, which
is nonzero mod 5, and `2 (m - m') (x - y)` is a product of three units of
`Z/5`, hence nonzero. So the separator set of every one of the fifteen pairs
is exactly the same twenty monomials. The values are
`E_A = 0` and `E_{B_m} = z^{m W} = z^{2 m (x - y)}`; on the diagonal
`v_x^2 conj(v_x)^2` every law reads 1. QED

### P4

Under `B_m`, `eps_x^2 = 1`, so `w_x = z^{2 t_0 + 2 m x}` and
`C^w_{xy} = z^{2 m (x - y)}`, hence
`S_w(k) = sum_r z^{(2m - k) r} = 5 delta_{k, 2m mod 5}`. Under `A`,
`t -> 2t` is a bijection of `Z/5`, so `w` is again iid uniform on the fifth
roots and `S_w = 1`. `Bmix` averages the four spectra with `m = 1, 2, 3, 4`;
since `2m` then ranges over `{2, 4, 1, 3}`, the average is
`(5/4)(1 - delta_{k,0})`. For `Pi_w`, the relevant monomials have `S = 4`,
not `0 mod 5`, under every `B_m`, and a nonzero net under `A`, so `Pi_w = 0`
throughout. QED

### P5

Pushforwards. `(rho_u v)_x = v_{u^{-1} x} = eps_{u^{-1} x}
z^{t_0 + m u^{-1} x}`: an affine exponent with slope `m u^{-1}` and a
relabeled iid sign field, so `rho_u B_m = B_{u^{-1} m}`.
`(gamma_u v)_x = sigma_u(eps_x z^{t_0 + m x}) = eps_x z^{u t_0 + u m x}`:
slope `u m` and `u t_0` uniform, so `gamma_u B_m = B_{u m}`. Composing,
`(D_u v)_x = sigma_u(v_{u^{-1} x}) = eps_{u^{-1} x} z^{u t_0 + m x}`: the
slope is exactly `m` again, so `D_u B_m = B_m` for every `u` and every `m`.
The two single actions move the index by inverse multiplications and the
diagonal is their cancellation. `A` is fixed by all three because a relabeling
of an iid field and the bijection `t -> u t` preserve its law, and `Bmix` is
fixed because both single actions permute `{B_1, ..., B_4}`. The index is
recoverable from any single configuration of `B_m` as `e_1 - e_0 = m`, so the
five laws are pairwise distinct and the orbit maps are exact, not merely
onto. The operators commute because `gamma` acts pointwise on values and
`rho` permutes sites; the verifier checks both composition orders on every
supported configuration. The peak map: `S_w` of `B_m` peaks at `2m`, and
`2 * 3 = 6 = 1 mod 5`, so the member with peak `k_0` is `B_{3 k_0 mod 5}`,
giving the table `k_0 = 0, 1, 2, 3, 4` to `m = 0, 3, 1, 4, 2`. Together with
P1 this proves the corrected form of the withdrawn claim E1: arbitrary peak
placement is compatible with full diagonal four-fold invariance, translation
invariance, deterministic modulus, and degree-3 agreement with `A`. QED

### P6

An odd total degree forces some site parity odd, so `E_{B_m} = 0` for every
`m`; hence no two `B` laws separate at any odd degree, and any separator from
`A` at `d = 5` must have `E_A = 1`: every `n_x = 0 mod 5` with
`sum (p_x + q_x) = 5`. Either some `|n_x| = 5`, which forces
`p_x + q_x >= 5 = d`, so the monomial is `v_x^5` or `conj(v_x)^5`; or every
`n_x = 0`, which forces an even degree, a contradiction. The ten fifth powers
have `E_A[v_x^5] = E[z^{5 t}] = E[1] = 1` and `E_{B_m}[v_x^5] =
E[eps_x] z^{5(t_0 + m x)} = 0`. The fifth power is the first monomial at
which the fifth-root structure of `A` collapses configuration by
configuration; this is the arithmetic signature of `p = 5` inside the
moment hierarchy, stated here as arithmetic and not as physics. QED

### P7

Every law of the six has `|v_x|^2 = 1` pointwise, so `E[|v_x|^4] = 1`; with
`C_{xx} = 1` and `P_{xx} = 0` the fourth cumulant is
`K_{xx} = 1 - 0 - 2 = -1`, the value `-a^4` at `a = 1` of the -1 statement
S2, now exhibited across the whole family. QED

## What did not fire

None of F1 to F8. Every gate is an exact equality over `Q(zeta_5)`, an exact
set equality, or an exact measure equality; no threshold exists that could
have been moved. The breaker found no break: in particular BRK-4 proves the
diagonal collapse for every moment of degree up to 6, strictly beyond the
verifier's degree-5 sweep, and BRK-5 proves the two orbit statements at the
moment level on an independent code path.

## Relation to candidate -1

Candidate -1 froze the pair `(A, B_0)` and the Wick no-go, and disclosed the
family as a post-freeze amplification that it was not allowed to import. This
candidate freezes the family properly, adds the value table, the degree-5
inventory and the full action table with the diagonal collapse, and touches
nothing in the -1 directory. The -1 pins remain byte-exact. The two
candidates target the same single registry row per the owner ruling of
2026-08-17.

## Consequence for the parent, stated without inflation

Unchanged in kind from -1, sharpened in degree: the data left free by second
order plus degree-3 functionals is not one bit but a full `Z/5` index plus
its mixtures, it is read exactly by the twenty fourth moments, and the
freedom survives the strongest symmetry available here, the diagonal
four-fold action. Any admissible normalization must freeze fourth-moment
data, the complete state, or an explicit non-Gaussian closure rule. The
parent stays `[O]` / STOP. No gate is created; `canon/GATES.tsv` is not
touched; `w = v^2` remains an `L1` algebraic map and `S_w` the power spectrum
of the squared readout, not a tensor spectrum and not `r_T(k)`.
