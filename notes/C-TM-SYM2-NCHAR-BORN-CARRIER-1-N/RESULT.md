# C-TM-SYM2-NCHAR-BORN-CARRIER-1-N result

```text
STATUS:       NON-CANONICAL
ISSUE LOCK:   #377
PUBLIC BASIS: Public Canon v46
DECISION:     MATHEMATICAL-CARRIER
PUBLIC ROWS:  unchanged
```

## 1. Odd sheet line

For every free complement orbit `O={w,Nw}`, let

```text
H_O=Q^O,
(S_N a)(w)=a(Nw).
```

In either ordered chart the swap matrix is

```text
[[0,1],[1,0]].
```

Thus

```text
H_O^-=ker(S_N+I)=Q(1,-1)
```

is one-dimensional. Swapping the two sheets sends `(1,-1)` to `(-1,1)`,
which is the same projective line. Therefore `P(H_O^-)` is defined without a
sheet representative.

[NON-CANONICAL candidate-T]

## 2. Source character and zero-state distinction

The #375 source satisfies

```text
omega(Nw)=-omega(w).
```

So its N-character is exactly the odd character selecting `H_O^-` as a
representation line.

This does not make the instantaneous state `omega|_O` nonzero. On the
palindrome orbit

```text
O_B={010,101}
```

one still has

```text
omega|_(O_B)=(0,0).
```

The carrier line and the instantaneous source state are therefore different
typed objects. The carrier exists even when the current carried by one stream
sample is zero.

## 3. Born square on the projective odd line

Use the standard rational Gram on `H_O` and the two coordinate effects. Every
nonzero representative of the odd line has the form

```text
(x,-x), x!=0.
```

Its norm is `2 x^2`, so the normalized coordinate Born law is independent of
`x`, its sign, and the sheet order. Only after this invariance proof is made,
the two probabilities evaluate to

```text
(1/2,1/2).
```

Hence the Born law is total on all three N-orbits, including the palindrome
orbit. No reference amplitude, phase, support orientation, or free parameter
is used.

[NON-CANONICAL candidate-T mathematical carrier]

## 4. Quotient composition

Independently, the public W3 child transfer descends to

```text
T_Q=[[0,1,1],
     [1,0,1],
     [1,1,0]].
```

Its unique normalized stationary vector solves `T_Q p=2p`. Only after solving,
it evaluates to equal three orbit weights.

Compose this quotient law with the projective odd-line Born law. The resulting
window measure is total and normalized. Only after the composition, all six
word weights evaluate equally, each to `1/6`.

Pushing forward through every bijective selector chart gives the same line
measure. The exact audit checked all `6!=720` bijections, hence in particular
all frozen 48 selectors. No gauge enlargement or representative selection is
needed.

[NON-CANONICAL candidate-T mathematical statement]

## 5. Breaker and audit

The breaker, frozen before the positive verifier, and the independent exact
audit agree:

```text
C1 PASS  odd line dimension one
C2 PASS  projective line independent of sheet order
C3 PASS  source N-character matches; palindrome current stays zero
C4 PASS  Born law independent of scale/sign/representative
C5 PASS  carrier law total on all three orbits
C6 PASS  quotient composition and all 720 charts coherent
```

No numerical target was used to select the carrier.

## 6. The public Born boundary fires as a status boundary

The current public dependency is not merely a generic statement that some
quadratic map is allowed. Its Registry text is

```text
MEASURE-BORN-VERB [D]:
  the measure read as the Born square of the verb,
  resting on the exact BORN-FACE-WEIGHTS theorem layer.
```

The intrinsic odd-sheet carrier above is a Born square of the N-character
representation. It is not, by itself, the registered J/verb amplitude and it
does not rest on `BORN-FACE-WEIGHTS`.

Therefore calling it a physical specialization of `MEASURE-BORN-VERB` would
widen the public dictionary by wording alone. This incubation refuses that
move.

The mathematical carrier is valid, but C7 does not pass the current public
Born dependency.

## 7. Decision

```text
DECISION: MATHEMATICAL-CARRIER
```

This route proves a cleaner theorem than #376 at the two-sheet level:

```text
orientation character
  -> unique projective odd sheet line
  -> unique normalized coordinate Born law
```

with no phaseful coefficient refinement. But the current public physics
requires `MEASURE-BORN-VERB`, so this cleaner carrier cannot replace #376 as
the physical bridge without a separate public dictionary change.

The comparison is therefore sharp:

```text
#376  physically compatible candidate-D bridge, because it reaches the
      registered verb/Born dictionary, but it carries that D condition.

#377  more intrinsic mathematical Born carrier, candidate-T at its finite
      representation scope, but not authorized as the registered physical
      Born-of-the-verb reading.
```

No Canon, Registry, frontier, dependency, gate, selector, gauge, decoder,
D_matter, or public status changes here.
