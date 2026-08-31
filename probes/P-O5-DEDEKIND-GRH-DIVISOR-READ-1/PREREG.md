# P-O5-DEDEKIND-GRH-DIVISOR-READ-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / NO FORMAL RUN YET / CANON UNCHANGED**

Date: 2026-08-27.

This is the fresh successor of the abandoned pin
`P-O5-DEDEKIND-GRH-READ-1`. It freezes one analytic-number-theory
divisor-coordinate theorem for the public scalar split-prime channel `O_5`.
It does not prove or disprove RH or GRH and it does not construct analytic
continuation from the TWIST-J carrier.

## Public identity

```text
probe:             P-O5-DEDEKIND-GRH-DIVISOR-READ-1
public claim lock: issue #590
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-DEDEKIND-GRH-DIVISOR-READ-1
path:              probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1/
basis main:        bb2172c69c0448ff3eeffc3960db362bf419a75e
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, analytic number-theory read only
layer lift:        none
authority:         none until a later sealed Canon fold
```

The branch was refreshed to this exact main before the pin. The predecessor
identifier and its proposed row remain consumed. Merged probe
`P-O5-SQUAREFREE-CORE-1` is adjacent but is not an input, dependency or
evidence source.

## Abandoned predecessor

```text
probe:             P-O5-DEDEKIND-GRH-READ-1
issue:             #587, closed not_planned
pin:               0717455c537449f70180029057406af324b8c12e
terminal record:   8b0317edcb7f51b87635fe1ae2b2203473c5e97a
abandonment PR:    #589, merged
scientific result: none
```

The predecessor failed its frozen empty-stderr integrity threshold during
interpreter startup. This successor changes no mathematical theorem to repair
that event. It only freezes a clean interpreter-startup control.

## Proposed candidate row

At most one row may be offered to a later sealed fold:

```text
O5-DEDEKIND-GRH-DIVISOR-READ [candidate-T]

Let F=Q(sqrt(5)), chi=chi_5 and zeta_F=zeta L(s,chi). Let O_5 be the
public scalar split-prime factor registered by
J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]. Define

    widehat_O_5(s)
      = zeta(4s)/(zeta_F(s)L(2s,chi))
        * (1-5^(-4s))/(1-5^(-s))

by standard meromorphic continuation of the classical factors, and

    H_5(s)
      = L(2s,chi)/zeta(4s)
        * (1-5^(-s))/(1-5^(-4s)).

Then widehat_O_5=O_5 on Re(s)>1, H_5 is holomorphic and nowhere zero on
Re(s)>1/2, and H_5 widehat_O_5=1/zeta_F. Hence for every rho with
Re(rho)>1/2,

    ord_rho(widehat_O_5) = -ord_rho(zeta_F).

By the standard functional equation of zeta_F,

    GRH(zeta_F)
    iff widehat_O_5 has no pole on Re(s)>1/2.

This is a divisor-coordinate theorem, not a proof of pole-freeness.
```

## Falsifier first

The theorem is falsified by any exact defect in the frozen scope:

1. one split, inert or ramified local factor fails `H_5 O_5=zeta_F^-1`;
2. `widehat_O_5` fails to agree with public `O_5` on `Re(s)>1`;
3. `H_5` has a zero or pole on `Re(s)>1/2`;
4. the divisor multiplicity identity fails there;
5. the GRH equivalence uses symmetry not supplied by the functional equation;
6. one split orientation is selected, an inert or ramified prime is
   contaminated, or a Hecke/automorphic/target-zero input is imported.

Changed pinned bytes, stale basis, failed startup preflight, nonzero exit,
nonempty stderr, stdout mismatch, architecture disagreement or any threshold
move are integrity STOPs, not mathematical counterexamples.

## The six frozen fields

```text
EQUATION
  The local factor table, global H_5*widehat_O_5 identity, half-plane
  unit theorem for H_5, divisor identity and GRH pole-read equivalence.

CODE
  probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1/verify.py.
  Python standard library only. Exact integers and Fraction arithmetic.
  No float, complex approximation, special-function evaluation, network,
  random input, zero table or external package.

CARRIER
  F=Q(sqrt5), chi_5, the public scalar O_5, formal one-prime rational
  functions in T=p^(-s), formal Euler-factor exponent maps and integer
  divisor multiplicities.

SYSTEMATICS
  The two prime ideals over a split rational prime remain an unordered pair.
  O_5 is nontrivial only at split rational primes. Standard meromorphic
  continuation is an explicitly imported coordinate change and supplies no
  zero-free information.

THRESHOLD
  G01 through G08 must pass exactly. Five production-path mutations must
  fire. Stdout must equal one committed LF EXPECTED.txt byte for byte;
  exit zero and empty stderr are required in required architecture jobs.

LAYER
  NOT_APPLICABLE. Analytic number theory only. No L1-L6 lift and no
  probability, physical, decoder, observable or SI statement.
```

## 1. Frozen public source

Public Canon v67 registers, at formal Euler-factor scope for `Re(s)>1`,

\[
O_5(s)
=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}{1+p^{-2s}}
=
\frac{\zeta(4s)}
{\zeta(s)L(s,\chi_5)L(2s,\chi_5)}
\frac{1-5^{-4s}}{1-5^{-s}}.
\]

The source row explicitly owns no continuation, zero location, cancellation,
RH, physical or L2-L6 statement. This probe consumes only the safe-half-plane
identity.

`TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` is a separate ordinary-Mobius
augmentation problem and is untouched. Merged `O5-SQUAREFREE-CORE` evidence
is also separate and is not used below.

## 2. Classical inputs

Exactly four classical analytic facts are imported:

1. for `F=Q(sqrt5)`, `zeta_F(s)=zeta(s)L(s,chi_5)`;
2. `zeta_F` has its standard meromorphic continuation and functional
   equation, whose nontrivial zero multiset is symmetric about `Re(s)=1/2`
   together with complex conjugation;
3. Euler products for `zeta(w)` and primitive nonprincipal
   `L(w,chi_5)` converge absolutely and are nonzero on `Re(w)>1`;
4. every zero of `1-5^(-ks)`, `k>0`, has `Re(s)=0`, because taking
   absolute values gives `5^(-k Re(s))=1`.

No critical-strip zero data, target pole-free theorem, Mertens estimate,
explicit formula, Weil positivity, Hecke character or automorphic input is
admitted.

## 3. Exact local factor table

Write `T=p^(-s)`. For `F=Q(sqrt5)`,

```text
zeta_F,p^-1 =
  (1-T)^2   split,
  1-T^2     inert,
  1-T       p=5.
```

Define

```text
H_5(s)
  = L(2s,chi_5)/zeta(4s)
    * (1-5^(-s))/(1-5^(-4s)).
```

For `p!=5`,

```text
H_5,p(T) = (1-T^4)/(1-chi_5(p)T^2)
         = 1+T^2  at split p,
           1-T^2  at inert p.
```

At `p=5`, `H_5,5(T)=1-T`.

The public channel has

```text
O_5,p(T) = (1-T)^2/(1+T^2)  at split p,
           1                 at inert p and p=5.
```

Therefore prime by prime

\[
\boxed{H_{5,p}(T)O_{5,p}(T)=\zeta_{F,p}(s)^{-1}.}
\]

This also shows that the scalar channel is pure split: the inert and
ramified complement is entirely in `H_5`.

## 4. Safe-half-plane global identity

On `Re(s)>1`, absolute convergence permits multiplication prime by prime:

\[
\boxed{H_5(s)O_5(s)=1/\zeta_F(s).}
\]

Solving for `O_5` gives exactly

\[
O_5(s)
=
\frac{\zeta(4s)}
{\zeta_F(s)L(2s,\chi_5)}
\frac{1-5^{-4s}}{1-5^{-s}}.
\]

Thus the quotient below extends the public Euler product rather than defining
a different function on its original domain.

## 5. Standard meromorphic read

Define

\[
\boxed{
\widehat O_5(s)
=
\frac{\zeta(4s)}
{\zeta_F(s)L(2s,\chi_5)}
\frac{1-5^{-4s}}{1-5^{-s}}
}
\]

using standard meromorphic continuations of the displayed classical factors.
By Section 4, `widehat_O_5(s)=O_5(s)` on `Re(s)>1`.

This is a coordinate read. It is not an independent construction of
continuation and supplies no pole-free information.

## 6. H_5 is a unit on Re(s)>1/2

If `Re(s)>1/2`, then `Re(2s)>1` and `Re(4s)>2`.

By classical input 3, `L(2s,chi_5)` and `zeta(4s)` are holomorphic and
nonzero there. By input 4, neither finite correction factor vanishes or
blows up there. Hence

\[
\boxed{
H_5\text{ is holomorphic and nowhere zero on }\operatorname{Re}s>1/2.
}
\]

No statement about a zero of `zeta_F` was used.

## 7. Divisor identity

As meromorphic functions,

\[
H_5(s)\widehat O_5(s)=1/\zeta_F(s).
\]

Use the convention `ord_rho(f)>0` for a zero and `<0` for a pole.
For `Re(rho)>1/2`, Section 6 gives `ord_rho(H_5)=0`. Additivity of
meromorphic orders gives

\[
\boxed{
\operatorname{ord}_\rho(\widehat O_5)
=
-\operatorname{ord}_\rho(\zeta_F)
}
\qquad(\operatorname{Re}\rho>1/2).
\]

Thus a zero of `zeta_F` in that half-plane is exactly a pole of
`widehat_O_5` with the same multiplicity, and conversely. The pole of
`zeta_F` at `s=1` becomes a zero of `widehat_O_5`, not a pole.

## 8. GRH pole-read equivalence

If GRH holds for `zeta_F`, there is no nontrivial zero with `Re(s)>1/2`,
hence Section 7 gives no pole of `widehat_O_5` there.

Conversely, if `widehat_O_5` has no pole on `Re(s)>1/2`, Section 7 gives no
zero of `zeta_F` there. By standard functional-equation symmetry, any
nontrivial zero off the critical line would have a reflected partner on the
right. Therefore all nontrivial zeros lie on `Re(s)=1/2`.

Hence

\[
\boxed{
\operatorname{GRH}(\zeta_{\mathbb Q(\sqrt5)})
\iff
\widehat O_5\text{ is pole-free on }\operatorname{Re}s>1/2.
}
\]

This equivalence does not make either side true.

## 9. Frozen negative controls

The verifier routes five mutations through the same production constructors:

```text
B1  treat inert O_5 as the split factor;
B2  omit L(2s,chi_5) from H_5;
B3  reverse the ramified finite correction in H_5;
B4  omit L(s,chi_5) from widehat_O_5;
B5  delete one member of the unordered split orientation pair.
```

Each mutation must be rejected while the baseline is accepted.

## 10. Frozen clean-start control

Before the single accepted local verifier invocation:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

must return exit zero, exactly `PYTHON_STARTUP_CLEAN` plus LF, and empty
stderr. Failure is STOP and produces no scientific result.

The scientific command is

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-DEDEKIND-GRH-DIVISOR-READ-1/verify.py
```

## 11. Explicit nonclaims

This probe supplies no proof or disproof of RH or GRH, no independent
analytic continuation, no zero-free region, no summatory cancellation
estimate, no explicit-form positivity, no Hecke or automorphic character,
no selected global orientation, no probability or physical read and no
L1-L6 lift.

A later fold may decide the candidate row only after the public evidence
record is complete. This probe itself changes no Canon row.
