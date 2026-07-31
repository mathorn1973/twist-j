# PREREG P-METRO-REDUCTION-ARROWS-4

```text
probe          P-METRO-REDUCTION-ARROWS-4
public lock    issue #196
owner item     METRO-REDUCTION-CALCULUS [O]
layer          L5 reduction calculus and pointwise L5 stream only.
               No lift to L6 is claimed.
scope claimed  obligation A (the four declared arrows) and obligation C
               (pointwise transported L5-stream invariance) only.
```

This probe does not close `METRO-REDUCTION-CALCULUS`. Obligations B
(forbidden transformations), D (common `q^k` blocking), and E (completeness
of `approx_red`) remain open. The row stays `[O]` and stays STOP.

Basis: Public Canon v25, tag `canon-v25`, activation/main commit
`ef1d2d917486dfb15cba3a81bd2309183c57f572`, content commit
`b914755b422bf79a8be637993b2edaa12a4333f8`, and `canon/CANON.md`
SHA-256
`53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb`
with 136831 bytes.

## Prospective-pin and known-result disclosure

Prior private development attempts exist. They remain outside the public
repository and are not evidence. This is a transparent known-result protocol
repair, not blind discovery.

`P-METRO-REDUCTION-ARROWS-4` is a fresh probe. At the time this file and its
accepted `verify.py` are committed, neither P4 file has been imported or
executed and no P4 formal output exists. Compilation, AST parsing, source
review, and other non-executing static checks are permitted before the pin.
The first formal execution is authorized only after public push and readback
of the immutable two-file pin. Any differing result, fired threshold, or
failure must be preserved.

## 1. Equation

Let

```text
P = (q,a,r,S,A0,{delta_(i,u)},enc_q,w)
```

be a `U_RF` tuple as typed in Public Canon v25: `q >= 2`, `a >= 1`,
`r >= 1`, `S` finite, `empty != A0 subseteq S`,
`delta_(i,u): S -> S` for `i in {1,...,a}` and `u in {0,...,q-1}`,
and `w: S -> Q^r`. The input basis, output basis, digit convention, and
padding convention are ordered and fixed. No commutation is assumed.

For a tuple of digit words `v=(v_1,...,v_a)`, coordinate 1 acts first:

```text
delta_v = D_a(v_a) o ... o D_1(v_1).
```

For `s in A0` and `n in N^a`, the pointwise L5 stream is

```text
Stream_P(s,n) = w(state_P(s,n)).
```

The following exact statements are frozen.

### E1: arrow 1, state relabeling

For a bijection `phi:S -> S'`, transport

```text
A0'             = phi(A0)
delta'_(i,u)    = phi o delta_(i,u) o phi^-1
w'              = w o phi^-1
alpha           = phi restricted to A0
input transport = identity
tau_R           = identity.
```

Induction over the ordered digit applications gives

```text
state_P'(phi(s),n) = phi(state_P(s,n))
```

and hence pointwise stream equality. Bijectivity is the complete
precondition.

### E2: arrow 2, reachable restriction

Define

```text
S_reach(P) = the closure of A0 under every single-digit map delta_(i,u).
```

Equivalently, `S_reach(P)` is the `Sigma*` orbit of `A0`, where
`Sigma={(i,u)}`. It is therefore closed under every digit map. Restricting
the carrier, digit maps, and output to `S_reach(P)` leaves every trajectory
from an allowed start unchanged, so the pointwise L5 stream intertwines with
`tau_R=identity`.

The one-shot set

```text
{delta_v(s): v is one V-tuple and s in A0}
```

need not equal `S_reach(P)`. A frozen exact witness distinguishes these
readings. Iterating V-tuples does equal the `Sigma*` orbit because each
single-digit action is itself a V-tuple action with empty words in the other
coordinates.

### E3: arrow 3, multi-action Nerode quotient

Define

```text
s ~_V t  iff  w(delta_v(s)) = w(delta_v(t)) for every V-tuple v.
```

The identity V-tuple shows that equivalent states have equal output.
For coordinate 1,

```text
delta_v o delta_(1,u)
  = delta_(u.v_1,v_2,...,v_a),
```

so `~_V` is always a congruence for every coordinate-1 digit map.
For coordinates `2,...,a`, congruence can fail when coordinate actions do
not commute. The exact finite precondition is therefore

```text
Pre_3(P): ~_V is a congruence for every delta_(i,u), i >= 2.
```

When `Pre_3(P)` holds, the quotient digit maps and quotient output are
well-defined. Induction over the fixed encoding gives

```text
Stream_(P/~_V)([s],n) = Stream_P(s,n)
```

pointwise. A frozen four-state witness proves the proviso is non-vacuous.
Exhaustion over the declared two- and three-state families decides the
frozen minimality statement.

### E4: arrow 4, coordinate permutation

A coordinate permutation is admitted only when coordinate names, input
indices, and the ordered input basis are transported together. The
transported composite is then the identical ordered list of digit actions,
so the pointwise L5 stream is unchanged.

The lookalike that permutes digit maps while retaining the old basis order is
not an admitted arrow. A frozen noncommuting witness shows that its state
composite can differ, and the F2 audit supplies exact stream witnesses.

### E5: obligation C, L5 invariance

E1 through E4 each prove exact pointwise equality of transported L5 streams
with `tau_R=identity`. This is the complete invariance claim of this probe.
No L5-to-L6 normalization, scientific-decision, terminal-value, physical, or
other cross-layer consequence is asserted.

## 2. Code

`verify.py` in this directory is the accepted exact verifier. It uses only
the Python standard library, integer arithmetic, and `fractions.Fraction`.
It uses no float, randomness, clock, filesystem access, network access,
subprocess, dynamic evaluation, or external data.

After the public pin, run exactly once from the repository root:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-METRO-REDUCTION-ARROWS-4/verify.py
```

External budget: under 120 seconds.

## 3. Carrier or data

There are no experimental data. The carrier is the frozen `U_RF` type.
The finite audit families are:

```text
F2   q=2, a=2, r=1, |S|=2, A0=S, binary output.
     4^4 digit-map assignments times 2^2 outputs = 1024 protocols.

F3   q=2, a=2, r=1, |S|=3, A0=S, binary output.
     27^4 digit-map assignments times 2^3 outputs = 4251528 protocols.

W4   one |S|=4 witness where ~_V fails congruence at coordinate 2.
WR   one |S|=4 witness separating one-shot V-image from Sigma* closure.
WP   one |S|=4 witness separating transported-basis permutation from the
     basis-fixed lookalike.

BOX index range {0,...,7}^2 with fixed-width-three, most-significant-digit-
     first binary encoding and retained leading zeros.
```

For the restriction audit, F2 additionally uses allowed starts `{0}`, `{1}`,
and `S`. In F3 the declared `A0=S`, so `S_reach=S` and the restriction is
identically the original protocol; no separate F3 closure enumeration is
needed.

## 4. Systematics

```text
S1  The minimality result is only for q=2, a=2, r=1, binary output, and
    |S| <= 3. It is not global over all q, a, r, or rational outputs.

S2  E1, E2, E3 quotient intertwining, E4, and E5 are exact algebraic
    statements. Finite checks on F2, F3, BOX, W4, WR, and WP audit the
    implementation and frozen witnesses; they do not replace the proofs.

S3  The F3 restriction is trivial because its frozen A0 is all of S.
    Exhaustive F3 work is used only for the E3 minimality decision.

S4  The verifier separately audits pointwise intertwining for arrows 1 and 2,
    the admitted Nerode quotient for arrow 3 on all F2 protocols, and the
    transported-basis arrow 4. Obligation C is exactly their L5 pointwise
    equality and has no L6 reading.

S5  Obligations B, D, and E are excluded. No normalization or cross-layer
    gate is owned.

S6  The first formal local leg is x86_64. The required GitHub leg is also
    x86_64. Byte identity therefore earns reproduction only; a
    computation-only statement remains at most C.
```

## 5. Failure threshold

```text
T1  Fail if any audited relabeling breaks transported pointwise equality.

T2  Fail if iterated V-closure differs from Sigma* closure anywhere in the
    declared F2 allowed-start audit, if the closure is not digit-map closed,
    if F2 reachable restriction changes a stream from an allowed start, or
    if the frozen F3 identity S_reach=S is false.

T3  Fail if WR does not have one-shot V-image strictly inside Sigma* closure.

T4  Fail if the coordinate-1 congruence identity fails, if W4 does not
    exhibit the frozen coordinate-2 failure, or if W4 has a coordinate-1
    failure.

T5  Primary falsifier: fail if exhaustive F2 or F3 finds any congruence
    counterexample. The counterexample counts must be exactly zero, making
    the frozen W4 four-state witness minimal in the declared family.

T6  Fail if an admitted F2 Nerode quotient is not well-defined or changes
    the pointwise stream anywhere in BOX.

T7  Fail if transported-basis coordinate permutation changes a stream, if
    the basis-fixed lookalike never changes one, or if WP is commuting.

T8  Fail if the combined obligation-C audit does not cover and certify all
    four admitted arrows at the frozen L5 scope.
```

Any one failed gate fails the probe. A fired threshold is recorded and
preserved. No threshold, family, layer, or scope may move after the pin.

## 6. Action layer

L5 only: typed reduction arrows and pointwise transported L5 streams.
No L6 normalization, scientific decision, terminal value, SI bridge,
physical reading, or other layer lift is claimed.

On success, the probe supplies evidence only for obligations A and C of
`METRO-REDUCTION-CALCULUS`. It proposes no registry row, no status change,
and no edit to `canon/CANON.md`, `canon/CORE.md`, `canon/FRONTIER.md`,
`canon/REGISTRY.tsv`, `canon/CHANGELOG.md`, or `canon/SHA256SUMS`.
Obligations B, D, and E remain open; the parent row remains `[O]` and STOP.
