# Retained phase references give a fixed current-state reader

PUBLIC / NON-CANONICAL / L1 / candidate-T analytical result. The separate
prospective finite audit is specified in [reference-PREREG.md](reference-PREREG.md).

## Invariant products on the written family

Keep the same prepared family and unchanged native state `U` from the
earlier supplement. At cut three its state is

```text
(p1,p4,p1p,p4p,q,r) = (0,r_1,1,r_4,4,1+2u),
r_1=v-2u, r_4=-v.
```

Put `A=p1+p1p`, `C=p1-p1p-2`, `B=p4+p4p`, `D=p4-p4p-1` in `F_5`.
The cut-three values are `A_3=1`, `C_3=2`, `B_3=r_1+r_4`, and
`D_3=r_1-r_4-1`. The complete state moves in the synchronized sheets
`X14={z=1 or z=4}`, where `z` is the sum of the six raw coordinates.
The generators actually selected there are `b,d,e`. Direct substitution
of their pinned coordinate rules gives

| Branch | New `A` | New `C` | New `B` | New `D` |
| --- | --- | --- | --- | --- |
| `b` | `-A` | `C` | `-B` | `D` |
| `d` or `e` | `-A` | `-C` | `-B` | `-D` |

For example, the `d,e` updates use the same first-piston coordinates
`(2-p1,3-p1p)`. The new `C` is `-p1+p1p-3=-C` in `F_5`. This table
proves that `AB` and `CD` are constant from cut three under every permitted
synchronized branch. Their initial values give `B_3=AB` and `D_3=3CD`.
Consequently a single time-independent function returns the original
residues as `3(AB+3CD+1)` and `3(AB-3CD-1)` at every cut from three.
The same table also gives `A_n=(-1)^(n-3)` and
`C_n=2(-1)^(n+theta_(n-1))` by the clock recursion of the earlier proof.
This last identity is an audit comparison. The reader uses the directly
available phase reference coordinates and never evaluates either exponent.

## Recognition of the completed record

At cuts zero, one and two, the sums `z` are `0,0,2`, respectively. At cut
three `z=1`; at every later cut the actual generators keep it in `X14`.
Thus the fixed predicate `z in {1,4}` recognizes the declared completed
record without a counter or saved context. Its complement yields BLANK.
On the zero input `u=v=0`, the state enters the same ready set and the
reader returns `PRESENT(0,0)`. The read function is total on `F_5^6` and
its BLANK/PRESENT meaning is established on the specified 25 trajectories.
The `q,r` coordinates are used only for the readiness sum, not for the
payload. This is an existing-state reference read at four piston
coordinates plus the sum. The earlier receiver-only, indexed read is a
different interface.

Reading the relative payload therefore needs no counter, source access
apart from those current references, stored input or history. The native
counter remains part of the whole autonomous state and the exact
continuation from the earlier proof. The reported BLANK/PRESENT tag and
payload do not define a state quotient through the write. At cut two the
reported tags are all equal and the following records take 25 values.

The existing no-write theorem concerns readers of already synchronized
checkpoints. Its maximal invariant is `R={V,-V}` with
`V=(A,B,chi(z)C,chi(z)D)` and `chi(z)=1,-1` on the respective sheets.
The two products here are the products of the corresponding pairs of
coordinates of `V`, so they factor through `R`. All three BLANK cuts are
outside those sheets. The write uses entry into synchronization, followed
by a constant payload along each synchronized orbit. This proves no
additional transmission or rewriting inside a synchronized orbit.

## Exact limit of the four-piston projection

At cut two `(p1,p1p)=(2,2)` and
`(p4,p4p)=(1-v+2u,4+v)`. As `(u,v)` ranges over `F_5^2`, the latter pair
ranges over every element of `F_5^2` exactly once. At cuts three through
seven the actual selected generators are `b,b,b,e,b`. Thus the cut-eight
reference is `A_8=-1`, `C_8=-2`, giving `(p1,p1p)=(2,2)` again. The
receiver pair ranges over every element at cut three by the literal write
formula, and each selected tail generator acts on it bijectively. It
still ranges over all 25 pairs at cut eight. The four-piston projection
sets at cuts two and eight are therefore exactly equal. No fixed function
of just those four coordinates realizes the declared BLANK at cut two
and PRESENT at cut eight across all 25 launches. This is an information
boundary for the stated preparation and readiness schedule, alongside the
positive construction with the readiness sum.

## Raw all-zero control

The raw origin-zero launch `(0,0,0,0,0,0)` is outside the supplied
family. Its actual steps `a,c,e` give the following checkpoints.

| Cut | Complete checkpoint | `z` |
| --- | --- | --- |
| 0 | `(0,0,0,0,0,0)` | 0 |
| 1 | `(0,0,0,0,0,0)` | 0 |
| 2 | `(2,1,2,1,1,0)` | 2 |
| 3 | `(0,0,1,3,1,1)` | 1 |

The fixed table reads BLANK on the first three checkpoints. The fourth
has the same reference seed `A_3=1,C_3=2` and receiver pair `(0,3)`.
After synchronization the same product identities give `PRESENT(0,3)`
at every remaining cut. The prepared ring-zero launch is
`E(0,0)=(2,0,0,0,3,0)` and reads `PRESENT(0,0)` after the write. Thus
the ready tag represents the declared prepared record, and the table
by itself fails as an absence test on arbitrary raw inputs.

## Pinned sources and limits

The parent native supplement is frozen at
`8c31f9d7f9d770d0a16a79960c69da2f5abc316c`. [Earlier native proof](https://github.com/mathorn1973/twist-j/blob/8c31f9d7f9d770d0a16a79960c69da2f5abc316c/notes/C-J-ZERO-ROOT-N/NATIVE-PROOF.md)

The authority for the original law is `canon-v117` at
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`. The normative `canon/CANON.md`
SHA-256 is `93a8d0c17ed88d93a62b56c44d65b6903c980654f7e5ea82da7e363a510a22a9`.
[Native conventions](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#native-one-shot-source-transfer-and-the-continuation-boundary)

The maximal invariant and the exact scope of the synchronized no-write
result are recorded separately in the same pinned Canon.
[U-NATIVE-INVARIANT-AND-NOWRITE](https://github.com/mathorn1973/twist-j/blob/6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed/canon/CANON.md#2-u-native-invariant-and-nowrite-t)

The preparation and the reader interface are explicit model inputs. The
result concerns the 25-state layer, one native write, and its continuing
mathematical record. It supplies no internal arithmetic reader circuit,
physical preparation or event, permanent-absence input, or renewal rule.
