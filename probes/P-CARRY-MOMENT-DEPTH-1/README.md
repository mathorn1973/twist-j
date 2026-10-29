# Exact carry moments with delayed residue mixing

**NON-CANONICAL. Action layer L1.**

This probe audits the accompanying analytical theorem for a declared
cyclotomic digit carrier. A first-order residue condition does not cover the
real units phi and phi^-1. The new small-depth argument includes these units
after two digits and supplies an exact finite-length moment formula without
reading its cross moments from the dynamic program it is compared against.

## Statement and boundary

Work in O = Z[zeta_5], with lambda = 1-zeta_5, J = 1+zeta_5^2 and
Q(x) = Tr(x conjugate(x)). The input is a supplied uniform word of length N,
the initial carry is zero, and the digit alphabet is either {0,1,2,3,4} or
{-2,-1,0,1,2}. Its mean is mu and its variance is 2. For a unit u, choose
s = rep_D(res(u)) and admit the moment theorem only at

```text
h = v_lambda(u-s) in {1,2,3}.
```

The complete finite formula and a rational error bound are in `PROOF.md`.
Their limit on this admitted class is

```text
lim E Q(C_N) = mu^2 Q(u-1) + 2 Q(u/J) + 12.
```

For the counting alphabet the minimum is 36, exactly at J and conjugate(J).
For the balanced alphabet it is 20, exactly at the ten units
±zeta^k phi^-1, k=0,...,4. Eight have depth one and the two real members have
depth two. Balanced ±1 have zero carry at every length and are outside the
theorem; the algebraic expression is not their actual mean. The depth-four
unit phi^5 is an explicit admission boundary.

## Prospective audit

`PREREG.md` freezes the equations, supplied measure, systematics, failure rules
and finite inventory before execution. `verify.py` is standalone standard
Python with exact integer and Fraction predicates. It compares 1,200 finite
moment predictions and 1,194 rational error bounds against an independent
carry distribution, with 9,360 complete small words, inverse-edge checks,
known J/J^-1 graph closures and scope controls.

The formula predicts the diagonal cross moments from the proved depth rule.
No observed DP moment is substituted into it. The complete-word check
multiplies the input polynomial once and extracts digits independently of the
streaming recurrence. Earlier numerical outputs were known before this work;
this is an audit of the new written argument, not a blind discovery test or
a retrospective preregistration of that earlier calculation.

The first execution follows the public source pin and readback. Its unchanged
stdout belongs in `EXPECTED.txt`; execution metadata belong in `RUN.md` and
the disposition in `RESULT.md`. Until these files exist, this directory records
preparation only. The two architecture jobs must compare against the same
committed stdout. The analytical universal claims rest on the proof rather
than extrapolation from the finite inventory.

## Physical scope

Multiplication by a unit permutes every finite word space, preserving a
supplied uniform output-word law. Its carry distribution and the selected
quadratic reading can still depend on the unit and digit representatives.
The carry mirror C -> -u^-1 C is preserved. A difference between forward and
inverse quadratic readings does not by itself determine dissipated energy,
work, pulse cost or a physical time arrow.

No physical word source, occurrence law, identification of Q with energy,
or derivation from the native finite update is asserted. No Canon file,
registry row, frontier owner, status or workflow is changed by this probe.

The separate reversible carry implementation remains in
[PR #1819](https://github.com/mathorn1973/twist-j/pull/1819), pinned before its
own execution. This moment audit neither replaces that circuit nor changes
its gate bound.
