# A two-residue write under the unchanged native update

PUBLIC / NON-CANONICAL / L1 / candidate-T analytical result. The prospective
finite audit is specified separately in [NATIVE-PREREG.md](NATIVE-PREREG.md).

## Relative coordinates on the 25-state layer

Let `j` be a primitive fifth root of unity, `O=Z[j]`, `ell=1-j`, and
`rho=j^2`. The reduction of `Phi_5` modulo five is `(X-1)^4`, so
`O/5O = F_5[ell]/(ell^4)`. Its ideal `(ell^2)` consists of the 25 states
`x=u ell^2+v ell^3` for independent `u,v` in `F_5`.

Write an integral lift of `x` as `sum_i a_i j^i` with `i=0,...,4`. For
exponents modulo five, `Tr(j^m)=5[m=0]-1`. Therefore the exact integer
quotient before reduction is `2(a_{-2k}-a_0)`. This immediately shows
independence of the common shift of all five coefficients and of the lift
modulo `5O`. The four differences require only field coefficients modulo
five. On the present layer choose the lift with `a_4=0` and

```text
(a_0,a_1,a_2,a_3)=(u+v,-2u-3v,u+3v,-v).
(r_0,r_1,r_2,r_3,r_4)=(0,v-2u,4u+2v,-2u-2v,-v) in F_5^5.
```

The two retained values give `v=-r_4` and `u=3(v-r_1)`. They encode the
entire layer and determine the other relative values without an absolute
trace. The trace identity proves the comparison and supplies no native
operation.

## Native preparation and first three cuts

Use the pinned native generator definitions below, in coordinate order
`(p1,p4,p1p,p4p,q,r)`. Arithmetic on these coordinates is in `F_5`. Write
`z` for the sum of all six coordinates and `theta_n` for the parity of the
binary digit sum of the native counter `n`. Increment `n` once and apply
the generator at index `z+2 theta_n` in `(a,b,c,d,e)`.

```text
a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)
b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)
c(p1,p4,p1p,p4p,q,r) = (2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r)
d(p1,p4,p1p,p4p,q,r) = (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r)
e(p1,p4,p1p,p4p,q,r) = (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r)
```

At counter zero, supply `A=-2u-v-3` and the checkpoint
`E(u,v)=(A,0,v,0,3,2u)`. The raw receiver `(p4,p4p,q)` begins at
`(0,0,3)` for every input. The other three positions form the supplied
source block. They are correlated by the single balancing equation `z=0`.
The full launch is injective in `(u,v)` with `u=3r` and `v=p1p`. No
coordinate of the launch, considered as a function over the complete layer,
equals `r_1=v-2u`.

The first three native bits are `0,1,1`. On the displayed family the cuts are

| Cut | Complete checkpoint | `z` | Next generator through the write |
| --- | --- | --- | --- |
| 0 | `(A,0,v,0,3,2u)` | 0 | `a` |
| 1 | `(0,A,0,v,3,2u)` | 0 | `c` |
| 2 | `(2,1-v+2u,2,1-A-2u,3,-2u)` | 2 | `e` |
| 3 | `(0,v-2u,1,-v,4,1+2u)` | 1 | |

The generator `c` combines the prepared `v` and `2u` in its cross-feed to
the receiver, which now contains `1-r_1`. The following `e` gives the
literal `r_1` and `r_4` in the two receiver pistons. The datum `r_4` is a
relocated rescaling of one raw input digit. Both are literal only at the
declared write cut and any other cuts satisfying the same equality. The
record-time `BLANK` convention for cuts zero through two does not impose
raw receiver constancy after launch.

## Retention, closed receiver and whole-state continuation

For every `n>=3`, `z_n=4+2 theta_(n-1) mod 5`. This holds at cut three. If
the next bit differs from the previous bit, the selector is `b` and
negates `z`. If the next bit equals the previous bit, the selector is `d`
for `z=1` and `e` for `z=4`. Those choices preserve `z`. This proves the
formula by induction, gives a common future word for all 25 messages and
uses only the counter already in the state.

Let `P=p4`, `P'=p4p`, `B=P+P'`, and `D=P-P'-1`. Each synchronized step
negates `B`. It preserves `D` for `b` and negates `D` for `d` or `e`.
Consequently

```text
B_3 = (-1)^(n-3) B_n,
D_3 = (-1)^(n+theta_(n-1)) D_n,
r_1 = 3(B_3+D_3+1),
r_4 = 3(B_3-D_3-1).
```

The second sign at cut three is one. Its successive ratio is minus one
exactly when consecutive bits agree. The equations prove that the same
function of `(n,P,P')` returns the two residues at every admitted cut from
three. The read function returns the distinct tag `BLANK` for `n<3`. A
counterless persistent literal pair is a different contract.

With the existing counter, the receiver triple itself has a closed tail
update on the family. For the three synchronized branches, it is

| Branch | `(P,P',q)` after the step |
| --- | --- |
| `b` | `(-P',-P,-q)` |
| `d` | `(1-P,4-P',1-q)` |
| `e` | `(1-P,4-P',2-q)` |

The counter chooses the actual branch as above. Before cut three the
common receiver is open to the source. In particular it cannot predict
the next raw receiver from its own identical launch states.

For exact whole-state recovery at any `n>=3`, recover `(u,v)` from the
current reader, form the displayed complete cut-three checkpoint, and use
the deterministic synchronized word to advance it to cut `n`. Equivalently
retain the full native checkpoint and use the unchanged update directly.
Either procedure keeps every native coordinate and the counter. The map
from the time-indexed admitted receiver pair to the time-indexed admitted
whole state is a bijection on the tail and transports the actual
continuation. Each synchronized branch is involutive on complete
checkpoints and is known from the counter. The prefix on the prepared
family is inverted by `e,c,a` in chronological order. This gives the
exact inverse on the admitted trajectory slices including the launch.
A global inverse on arbitrary native heads is outside the statement.

## Natural coefficient control and limits

In the separate control, prepare the four ordinary monomial coefficients
of `x` in the pistons and `(q,r)=(0,1)` on every input. The four
coefficients sum to zero on `(ell^2)`. The closed native quotient `(z,q,r)`
has the same initial value and successive branch on every launch, so the
entire `(q,r)` history is identical across the layer. The two relative
values vary over all 25 words. This obstruction applies to that restricted
port and preparation, with or without a counter or a saved history.

The construction encodes all 25 source states into existing raw memory
positions and retains the result through a declared clock-assisted
mathematical reading. Source routing and the balancing relation are
construction choices. No unique or forced preparation, internal detector
implementation, reusable write, or physical event is established. The
625-state ring and the supplied integral contact and H3 carriers are
outside the native write theorem.

## Pinned sources

The public activation is `canon-v117` at
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed` with content commit
`d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`. The normative source
`canon/CANON.md` has SHA-256
`93a8d0c17ed88d93a62b56c44d65b6903c980654f7e5ea82da7e363a510a22a9` and
`canon/CORE.md` has SHA-256
`6b5e15ce3bc50b38bcbea3c77cac5873e43b8d799a508388f775436e1de5baef`.

- The original carrier and the rule against decoder feedback. [Native state and typed readings](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CORE.md#native-state-and-typed-readings)
- The exact original generators and a prior five-message family. [Native conventions and one-shot record](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#native-one-shot-source-transfer-and-the-continuation-boundary)
- The `eca` restriction on the initial `z=0` sheet and the synchronized chart signs. [Native checkpoint chart](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#u-native-common-ready-source-retention-t)
- The quotient law used in the natural coefficient control. [Native apparatus history factor](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#5-u-native-apparatus-history-factor-t)
