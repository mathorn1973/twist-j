# P-O5-DEDEKIND-GRH-READ-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / NO FORMAL RUN YET / CANON UNCHANGED**

Date: 2026-08-27.

This probe freezes one analytic-number-theory read theorem. It does not prove
or disprove RH or GRH. It identifies the divisor of the meromorphically
continued public pure split-orientation scalar channel with the negative
divisor of the Dedekind zeta function of the golden real field on the open
right half of the critical strip.

## Public identity, authority, and action layer

```text
probe:             P-O5-DEDEKIND-GRH-READ-1
public claim lock: issue #587
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-DEDEKIND-GRH-READ-1
path:              probes/P-O5-DEDEKIND-GRH-READ-1/
basis main:        7dd25c7c21202c560d8a31774971c7c6200fca76
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, analytic number-theory read only
layer lift:        none
authority:         none until a later sealed Canon fold
```

The public issue was opened only after a collision search across current and
historical issues, pull requests, branches, the Public Canon v67 tree,
Registry, Frontier, dependencies, gates, evidence, and the rapidity probes.

## Proposed candidate row

At most one row may be offered to a later sealed fold:

```text
O5-DEDEKIND-GRH-READ [candidate-T]

For F = Q(sqrt(5)) and chi = chi_5, let O_5 be the scalar split-prime
orientation factor registered by J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION
[T]. Define its standard meromorphic read by

    widehat_O_5(s)
      = zeta(4s)/(zeta_F(s)L(2s,chi))
        * (1-5^(-4s))/(1-5^(-s)).

It agrees with O_5 on Re(s)>1. On Re(s)>1/2 the complementary factor

    H_5(s)
      = L(2s,chi)/zeta(4s)
        * (1-5^(-s))/(1-5^(-4s))

is holomorphic and nowhere zero, and

    H_5(s) widehat_O_5(s) = 1/zeta_F(s).

Hence ord_rho(widehat_O_5) = -ord_rho(zeta_F) for every
rho with Re(rho)>1/2. By the standard functional equation of zeta_F,
GRH(zeta_F) is equivalent to widehat_O_5 having no pole in
Re(s)>1/2. This is a read equivalence, not a proof of pole-freeness.
```

No status is earned by this preregistration. The written proof is the proposed
theorem-grade evidence. The post-pin verifier audits only exact algebraic,
local-factor, divisor, symmetry, and source-firewall mechanisms.

## Falsifier first

One exact counterexample to any frozen statement below falsifies the
corresponding candidate theorem:

1. one split, inert, or ramified local factor fails
   `H_5 O_5 = zeta_F^-1`;
2. the displayed quotient does not agree with the public `O_5` Euler product
   on `Re(s)>1`;
3. `H_5` has a zero or pole at a point with `Re(s)>1/2`;
4. the divisor identity
   `ord(widehat_O_5) = -ord(zeta_F)` fails at one point in that half-plane;
5. the implication from absence of right-half zeros to GRH uses symmetry not
   supplied by the standard functional equation;
6. the construction selects one of the two split prime-ideal orientations,
   identifies `O_5` with a Hecke or rapidity character, or makes it nontrivial
   at an inert or ramified prime;
7. a target zeta-zero theorem, an equivalent Mertens estimate, or the desired
   pole-free conclusion enters the construction as an input.

The following are integrity STOPs rather than mathematical counterexamples:
a changed pinned byte, stale basis, parser or verifier failure, nonzero exit,
nonempty stderr, stdout mismatch, architecture disagreement, or a claim
outside the frozen analytic-number-theory scope.

## The six frozen fields

```text
EQUATION
  The local factor table, the global H_5 * widehat_O_5 identity, the
  half-plane unit theorem for H_5, the divisor identity, and the GRH
  pole-read equivalence in the exact forms proved below.

CODE
  probes/P-O5-DEDEKIND-GRH-READ-1/verify.py. Python standard library only;
  exact integers and Fraction arithmetic; exact polynomial and rational
  function identities; finite exact divisor and symmetry audits; no float,
  complex approximation, special-function evaluation, network, random input,
  zero table, or external package.

CARRIER
  F = Q(sqrt(5)), chi_5, the public scalar split-prime factor O_5, formal
  one-prime rational functions in T=p^(-s), formal global Euler-factor
  exponent maps, and integer divisor multiplicities.

SYSTEMATICS
  The two prime ideals above a split rational prime are an unordered
  orientation pair. Exchange of the pair is gauge for this scalar read.
  O_5 is nontrivial only at split rational primes. Standard meromorphic
  continuation is disclosed as an imported classical coordinate change.
  It is not an independently constructed continuation and carries no
  zero-free information.

THRESHOLD
  G01 through G08 must pass exactly. Every frozen production-path mutation
  must fail at its named witness. Stdout must equal one committed LF
  EXPECTED.txt byte for byte; exit zero and empty stderr are required on
  x86_64 and aarch64.

LAYER
  NOT_APPLICABLE. Analytic number theory only. No state, manifold, boundary,
  support, stream, measure, probability, decoder, observable, physical
  dictionary, or L1-L6 lift.
```

## 1. Public source theorem and collision boundary

Public Canon v67 registers
`J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]`. For
`Re(s)>1` it owns

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

It explicitly owns no continuation, zero location, cancellation estimate,
RH statement, physical read, or higher-layer lift. This probe consumes that
safe-half-plane identity and adds no evidence credit to it.

Public Canon v67 also registers
`TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`. That row owns a different problem:
derive ordinary Möbius cancellation at the augmentation `X_p -> 1` from the
integral rapidity shell. It targets an RH-strength Mertens estimate for
`zeta(s)`. The present probe neither widens nor closes that row and does not
use it as evidence.

Closed issue #310, `C-J-DEDEKIND-WEIL-ROAD-N`, concerns a J-native completion
and a Weil-form route for the quartic CM field `Q(zeta_5)`. The present field
is the real quadratic floor `Q(sqrt(5))`, and the target is only the divisor
read of the already public scalar factor `O_5`. No object, protocol verdict,
or evidence is inherited from that Note.

The earlier internal JIPC real-even/real-odd/complex duplication program is
not an input. Its protocol distinctions remain useful background, but its
target belongs to `Q(zeta_5)` and its old quarantine has no authority over
this fresh public probe.

## 2. Classical inputs, all disclosed

The proof imports exactly four standard analytic-number-theory facts.

### A1. Quadratic Dedekind factorization

For

\[
F=\mathbb Q(\sqrt5),\qquad \chi=\chi_5,
\]

the Dedekind zeta function factors as

\[
\zeta_F(s)=\zeta(s)L(s,\chi).
\]

At a rational prime, with `T=p^(-s)`, the inverse local factors are

\[
\zeta_{F,p}(s)^{-1}
=
\begin{cases}
(1-T)^2,&\chi(p)=1\quad\text{(split)},\\
1-T^2,&\chi(p)=-1\quad\text{(inert)},\\
1-T,&p=5\quad\text{(ramified)}.
\end{cases}
\]

### A2. Standard continuation and functional equation

The completed Dedekind zeta function of `F` has its standard meromorphic
continuation and functional equation. Its nontrivial zero multiset is stable
under reflection across `Re(s)=1/2`, together with complex conjugation.

### A3. Safe Euler-product nonvanishing

The Euler products of `zeta(w)` and the primitive nonprincipal
`L(w,chi_5)` converge absolutely and are nonzero on `Re(w)>1`.

### A4. Elementary one-prime zero location

For an integer `k>0`, every solution of

\[
1-5^{-ks}=0
\]

has `Re(s)=0`. Indeed, taking absolute values gives
`5^{-k Re(s)}=1`; because `5>1` and `k>0`, this forces `Re(s)=0`.

No zero table, zero-free theorem in the critical strip, Mertens estimate,
explicit formula, Weil positivity theorem, Hecke character, automorphic
input, or target pole-free statement is admitted.

## 3. The exact local split

Define

\[
H_5(s)
=
\frac{L(2s,\chi)}{\zeta(4s)}
\frac{1-5^{-s}}{1-5^{-4s}}.
\]

For `p != 5`, the local factor is

\[
H_{5,p}(T)
=
\frac{1-T^4}{1-\chi(p)T^2}.
\]

Therefore

\[
H_{5,p}(T)
=
\begin{cases}
1+T^2,&p\text{ split},\\
1-T^2,&p\text{ inert}.
\end{cases}
\]

At `p=5`, the `L(2s,chi)` local factor is one, while the correction cancels
the fourth-power factor:

\[
H_{5,5}(T)
=
(1-T^4)\frac{1-T}{1-T^4}
=
1-T.
\]

The public factor has the local table

\[
O_{5,p}(T)
=
\begin{cases}
\dfrac{(1-T)^2}{1+T^2},&p\text{ split},\\
1,&p\text{ inert or }p=5.
\end{cases}
\]

Consequently, prime by prime,

\[
H_{5,p}(T)O_{5,p}(T)
=
\zeta_{F,p}(s)^{-1}.
\]

This proves both that `O_5` is pure split and that the inert and ramified
complement belongs entirely to `H_5`.

## 4. Global identity on the safe half-plane

Absolute convergence on `Re(s)>1` permits multiplication prime by prime.
The local identity yields

\[
\boxed{
H_5(s)O_5(s)=\frac1{\zeta_F(s)}
}
\qquad(\operatorname{Re}s>1).
\]

Solving for `O_5` recovers exactly the public closed formula:

\[
O_5(s)
=
\frac{\zeta(4s)}
{\zeta_F(s)L(2s,\chi)}
\frac{1-5^{-4s}}{1-5^{-s}}.
\]

Thus the quotient below is an extension of the public Euler product, not a
different function on its original domain.

## 5. Standard meromorphic read

Define

\[
\boxed{
\widehat O_5(s)
=
\frac{\zeta(4s)}
{\zeta_F(s)L(2s,\chi)}
\frac{1-5^{-4s}}{1-5^{-s}}
}
\]

using the standard meromorphic continuations of the displayed classical
factors. By Section 4,

\[
\widehat O_5(s)=O_5(s)
\qquad(\operatorname{Re}s>1).
\]

This definition supplies a coordinate in which the Dedekind zero divisor can
be read. It does not construct continuation from the rapidity shell and does
not supply pole-freeness.

## 6. The complementary factor is a unit on the right half-strip

Assume `Re(s)>1/2`. Then

\[
\operatorname{Re}(2s)>1,\qquad
\operatorname{Re}(4s)>2.
\]

By A3, `L(2s,chi)` and `zeta(4s)` are holomorphic and nonzero there.
By A4, neither `1-5^{-s}` nor `1-5^{-4s}` vanishes there. Hence

\[
\boxed{
H_5\text{ is holomorphic and nowhere zero on }
\operatorname{Re}s>\frac12.
}
\]

Equivalently, `H_5` is a holomorphic unit on that half-plane.

## 7. Divisor identity

By definition,

\[
H_5(s)\widehat O_5(s)=\frac1{\zeta_F(s)}
\]

as a meromorphic identity. Use the convention that
`ord_rho(f)>0` is a zero and `ord_rho(f)<0` is a pole. For
`Re(rho)>1/2`, Section 6 gives

\[
\operatorname{ord}_\rho(H_5)=0.
\]

Additivity of meromorphic orders gives

\[
0+\operatorname{ord}_\rho(\widehat O_5)
=
-\operatorname{ord}_\rho(\zeta_F),
\]

therefore

\[
\boxed{
\operatorname{ord}_\rho(\widehat O_5)
=
-\operatorname{ord}_\rho(\zeta_F)
}
\qquad(\operatorname{Re}\rho>1/2).
\]

In particular, every zero of `zeta_F` to the right of the critical line is a
pole of `widehat_O_5` with the same multiplicity, and conversely.

The pole of `zeta_F` at `s=1` becomes a zero of `widehat_O_5`, not a pole.
It does not obstruct the pole-free criterion.

## 8. GRH as pole-freeness of the pure split channel

If GRH holds for `zeta_F`, there is no nontrivial zero with
`Re(s)>1/2`. By Section 7, `widehat_O_5` has no pole there.

Conversely, suppose `widehat_O_5` has no pole on `Re(s)>1/2`. Section 7
then gives no zero of `zeta_F` in that half-plane. By A2, every nontrivial
zero off the critical line has a reflected partner on the other side. The
absence of right-half zeros therefore excludes left-half zeros as well.
Every nontrivial zero lies on `Re(s)=1/2`, which is GRH for `zeta_F`.

Hence

\[
\boxed{
\operatorname{GRH}(\zeta_{\mathbb Q(\sqrt5)})
\iff
\widehat O_5
\text{ has no pole on }
\operatorname{Re}s>\frac12.
}
\]

This theorem is a change of exact coordinates. It does not establish either
side.

## 9. Meaning of pure split-orientation channel

The integral rapidity lift retains two Laurent directions
`X_p` and `X_p^-1` above a split rational prime. Their exchange is the
orientation involution. The scalar factor `O_5` depends only on the unordered
pair:

\[
\frac{(1-T)^2}{1+T^2}.
\]

It contains no `X_p`, is fixed by `X_p <-> X_p^-1`, and is one at every inert
or ramified prime. Therefore:

```text
pure:
  no inert or ramified prime contributes a nontrivial O_5 local factor;

split-orientation:
  the source is the two-direction split shell;

channel:
  the output is the scalar exchange-invariant read of the pair.
```

It is not one selected orientation, not a character of the rapidity group,
not a Hecke character, and not a twist.

## 10. Exact verifier gates

The one accepted post-pin command is

```text
python3 probes/P-O5-DEDEKIND-GRH-READ-1/verify.py
```

The verifier is an audit of the written proof, not an analytic oracle.

### G01. Local factor table

Using exact polynomial rational functions, verify all three identities

```text
split:     ((1-T)^2/(1+T^2)) * (1+T^2) = (1-T)^2
inert:     1 * (1-T^2)                  = 1-T^2
ramified:  1 * (1-T)                    = 1-T
```

and verify that only the split `O_5` factor is nontrivial.

### G02. Global formal factor bookkeeping

Represent `zeta(s)`, `L(s,chi)`, `L(2s,chi)`, `zeta(4s)`, and the two
ramified factors by independent formal generators. Verify exactly that the
frozen exponent maps of `H_5` and `widehat_O_5` add to
`zeta(s)^-1 L(s,chi)^-1`.

### G03. Half-plane unit guard

Verify the exact affine implications

```text
sigma > 1/2  =>  2 sigma > 1,
sigma > 1/2  =>  4 sigma > 2,
```

and the complete component ledger showing that every factor of `H_5` is
nonzero there by A3 or A4 and that no `zeta_F` target factor enters `H_5`.

### G04. Divisor multiplicity law

Audit exact integer orders and the identity

```text
ord(H_5)=0
ord(H_5)+ord(widehat_O_5)=-ord(zeta_F)
therefore ord(widehat_O_5)=-ord(zeta_F).
```

The written meromorphic-order proof supplies the universal statement.

### G05. Functional-equation symmetry logic

Enumerate every symmetric zero-offset subset in a frozen finite model and
verify that absence of positive offsets is equivalent to support only at zero.
The written functional-equation proof supplies the unrestricted theorem.

### G06. Orientation-pair and pure-support guard

Verify star invariance of the two-direction split coefficient, rejection of a
one-orientation mutation, and that the `O_5` support table contains only the
split prime type.

### G07. Production-path negative fixtures

The same constructors used by G01 and G02 must reject:

1. an inert prime assigned the split `O_5` factor;
2. omission of `L(2s,chi)` from `H_5`;
3. reversal of the ramified correction in `H_5`;
4. replacement of `zeta_F` by `zeta` alone;
5. deletion of one split orientation.

Every mutation must fail at its named exact witness.

### G08. Source firewall

The verifier reads and parses its own source. It requires LF-only text, a
final LF, standard-library imports from the frozen allowlist, no floating or
complex literal, and no network, subprocess, random, external package,
special-function evaluator, dynamic execution, or target-zero data route.

## 11. Exact output and run protocol

The formal run is valid only after the public pin records the exact bytes,
SHA-256 values, Git blobs, and commit containing this file and `verify.py`.
The verifier is then executed once from those immutable bytes under:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Pass requires:

```text
G01-G08: PASS
negative fixtures: all FIRED
exit code: 0
stderr: empty
stdout: byte-identical to committed EXPECTED.txt
```

The pull-request workflow must replay the unchanged verifier on GitHub-hosted
x86_64 and aarch64 with Python 3.12. A one-architecture local run is the
accepted formal record but is not by itself the public two-architecture
computation gate.

## Explicit nonclaims

This probe supplies no proof or disproof of RH or GRH, no independent
continuation, no zero-free region, no Mertens estimate, no explicit formula,
no Weil positivity, no Hecke or automorphic character, no global orientation
selector, no probability, no physical interpretation, no J-specificity
result, no Canon status move, and no L1-L6 lift.

Failure of a future transfer candidate is `CANDIDATE_REJECTED` or `STOP`
unless a complete frozen class supports a universal negative theorem. The
present read theorem does not pre-authorize that future class or its gates.
