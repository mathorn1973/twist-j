# PREREG: P-J-HODGE-SEMILINEAR-MEMORY-1

**FORMAL PUBLIC PROBE / NO CANON PROMOTION.**

Owner: A. M. Thorn / J-Hodge semilinear memory session 2026-09-19.
Action layer: L1.
Issue lock: #1070.
Branch: `probe/P-J-HODGE-SEMILINEAR-MEMORY-1`.
Authority: Public Canon v89; base main
`08d7984d97c85d89d0b22a400762a5140fcb3bb5`.
The author explicitly authorized use of the connected GitHub commit identity.

## Carrier

Let `V=A4 tensor Q` in the marked root basis, `C` the marked five-cycle,
`M=I+C^2`, `W=Lambda^2 V`, `L=Lambda^2 M`,
and `K=sqrt(5)*` the integral scaled Hodge operator. Put
`F=Q(sqrt(5))`, with nontrivial automorphism `sigma`.

Over F define
```text
P_+=(I+K/sqrt(5))/2,    P_-=(I-K/sqrt(5))/2,
W_+=im P_+,             W_-=im P_-,
E_J=im P_+ + im(P_- L P_+).
```

Let `A_c=Lambda^2 C` and use the rational B1 projectors
```text
T=(I+A_c+A_c^2+A_c^3+A_c^4)/5,   R=I-T.
```

For a rational substrate state `w in W_Q`, write its plus coordinate as
`x=P_+ w`. In the frozen sigma-conjugate bases of W_+ and W_-,
`P_- w=sigma(x)`.

## Frozen targets

G1. Exact Hodge/J commutation split:
```text
K L K^-1 T = L^-1 T,
(KL-LK)R = 0.
```

G2. In the frozen conjugate Hodge bases there are exact F-linear matrices
`A,B:F^3->F^3` such that for every rational substrate state
```text
x' = A x + B sigma(x),
rank_F(B)=1.
```

G3. The displayed update is Q-linear/semilinear but not F-linear. In
particular there is an exact witness x with
```text
S(sqrt(5)x) != sqrt(5) S(x).
```

G4. The fixed-J future admits an exact four-dimensional F-linear realization
`(x,u)` on E_J, with present output x. The stacked present/next observation
map has rank four. Therefore four is minimal among F-linear exact predictive
realizations with this frozen three-coordinate output. No set-theoretic
minimality is claimed.

G5. The visible primary axis `T_+=P_+ im T` is one-dimensional. If y is its
frozen rank-one output coordinate, every E_J trajectory satisfies
```text
y_(n+2)=3 y_(n+1)-y_n.
```

G6. The datum `(x_n,y_(n-1))` determines the full four-dimensional E_J state
uniquely and F-linearly. Equivalently, present triple plus one previous axial
scalar has observation rank four.

G7. In the frozen conjugate primary basis, the one-step 2x2 boost block has
diagonal coefficient `3/2=L_2/2` and conjugate-coupling magnitude
`sqrt(5)/2=sqrt(5) F_2/2`. The deterministic marked basis fixes the actual
off-diagonal signs; they are printed rather than changed after execution.

G8. `P_-=sigma(P_+)` entrywise, and the hidden primary coordinate in G2-G7
is exactly the sigma-conjugate channel.

G9. The accepted arbitrary-word boundary remains: allowing all future A5/J
words requires six predictive coordinates. The four-dimensional result is for
one fixed marked J / one selected Sylow-5 axis only.

G10. No native-U intertwiner is asserted. This probe concerns the marked
multiplication step L. The merged counter/carry and native word no-go probes
are context, not premises that promote this algebra to a physical clock.

## Code and failure threshold

`PROOF.md` supplies the universal semilinear, recurrence and minimality
arguments. `verify.py` uses Python standard-library `Fraction` and an exact
two-component implementation of Q(sqrt(5).) It reconstructs all matrices from
the marked A4 data and audits G1-G8. G9-G10 are scope boundaries tied to
accepted public predecessors.

No floating point, randomness, network input, external package, fitted
tolerance or post-run basis adjustment is permitted. Any exact failure of
G1-G8 fires the corresponding target. Integrity/runtime failure is STOP.

Only static syntax compilation is allowed before the public pin.

## Explicit nonclaims

The mathematical negative-norm coordinate is not identified with physical
time. The sentence "time is a counter" remains a reading. No physical spatial
dimension, observer, decoder, occurrence law, measure, SI quantity, Canon
promotion or L2-L6 lift follows from this probe.
