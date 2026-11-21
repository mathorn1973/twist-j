# PREREG: C-PHOTON-CONTACT-SOURCE-OPT-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1182
Branch: `notes/photon-contact-source-opt-20260926`

## 1. Basis

Public Canon v92 is the sole authority.

The only mathematical input is the general simple-cycle complex-source
inequality already derived in public-main
`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md`:

`
C_gamma <= a(h)^m r(h)^(c+O_+) s(h)^O_-.
`

No draft result is an authority dependency.

## 2. Exact rational source family

Restrict to

`
h=log t,   t in {2,3,...,32}.
`

Then exactly

`
a_t = (t^2+1)^6/(64 t^11),
r_t = 2(t^4+1)/(t^2+1)^2,
s_t = 4t^2/(t^2+1)^2.
`

For a simple cycle satisfying

`
O_+ <= rho m
`

and after discarding the beneficial factor `s_t^O_-`, the same
nonbacktracking count used in FULL-MEASURE gives a per-length sufficient
factor

`
q(t,rho)=a_t(1+6r_t)r_t^rho.
`

This item asks only whether `q(t,rho)<1` for the frozen source/density grid.

## 3. Frozen density grid

Use exactly

`
rho=k/24,  k=0,...,24.
`

Test densities from largest to smallest. For each density test
`t=2,...,32`.

Since `rho=k/24`, do not introduce algebraic approximations. Test the exact
equivalent inequality

`
[a_t(1+6r_t)]^24 * r_t^k < 1.                           (G)
`

The largest `rho` admitting at least one exact PASS is the audit result.

Within that density, choose the `t` minimizing the exact 24th-power
quantity in (G). Ties are resolved by the smaller `t`.

No source outside `2,...,32`, no density outside the frozen 1/24 grid and no
post-result interpolation is allowed.

## 4. Required special test

The verifier must separately report the exact result for

`
rho=1/2.
`

This is motivated by, but does not claim completeness for, width-one
rectangular ribbons whose reinforcing-contact density approaches one half.

## 5. Candidate implication

If the audit finds a density `rho_*>0` and a source `t_*`, the written
candidate-T implication is:

For every unit simple cycle with

`
O_+ <= rho_* m,
`

the existing source/path argument is subcritical at `h=log t_*`, after
discarding the helpful `O_-` factor.

A later signed-slice fold may combine this with the deterministic
`ell^2/m` estimate from #1176. This item itself does not claim a new
`Xi_L` bound.

## 6. Exact audit

Before first execution, commit and read back this file and `verify.py`.

The verifier must:

1. derive `a_t,r_t,s_t` as `Fraction`;
2. independently verify the `h=log t` algebra by clearing denominators;
3. test the exact frozen `rho,t` grid using (G);
4. report the largest passing density and minimizing source;
5. report the exact numerator/denominator of the 24th-power certificate;
6. report the separate `rho=1/2` result;
7. verify `s_t<1<r_t` for every frozen t;
8. print the scientific boundary.

No floats, external libraries, optimization packages, random search or fitted
thresholds.

## 7. Boundary

This is source-parameter arithmetic only. It does not prove that all simple
cycles satisfy any reinforcing-contact density bound. It does not exploit
`O_-`, control current networks, bound full `Xi_L`, prove P1 or establish
a massless phase.

No Canon, Registry, Frontier, probe, tool, workflow or release files change.
