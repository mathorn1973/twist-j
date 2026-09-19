# Selector alphabet, cyclotomic carrier, and the missing state amplitude

**NON-CANONICAL. L1 only. Candidate-T proof statements below create no
public status, decoder, physical time, or cross-layer adoption.**

This is a component of the single scoped candidate
`C-U-SELECTOR-READING-STRUCTURE-N`, owned in issue #1074. It uses the native
architecture and synchronized-chart theorem in Public Canon v89 and the
existing marked J-Hodge operator. The positive representation correspondence
is a consolidation of existing mathematics, not a new native intertwining.
The new restricted obstruction concerns a reader whose source port contains
only the counter and the selector trace or selected index.

## 1. The integral alphabet correspondence

Let

```text
E = Z^{F5},  C e_i = e_(i+1),  eps(sum a_i e_i) = sum a_i,
N = sum_i e_i,  A = ker eps.
```

The basis labels are mathematical addresses. They are not coordinates of a
native checkpoint. The standard counting form makes `A` the root lattice
`A4`. Set `a_i=e_(i+1)-e_i`, with indices modulo five. These five generators
span `A`, and their only integral relation is `sum_i a_i=0`.

The map `C-I:E->A` is onto and has kernel `Z N`. Consequently it induces an
integral isomorphism

```text
E/(Z N) -> A,  [e_i] -> a_i.
```

With the existing project root `j=zeta_5`, the assignment

```text
Psi:A -> Z[j],  Psi(a_i)=j^i
```

is an integral isomorphism: the source generators and their sole relation
agree with the presentation of `Z[j]`. It satisfies `Psi C = j Psi`.
Therefore

```text
S = (I+C^2)|A,
Psi S = M_J Psi,  J=1+j^2,
Lambda^2(Psi) Lambda^2(S) = Lambda^2(M_J) Lambda^2(Psi).
```

Thus the alphabet construction does recover the existing integral J-step and
its exterior square as mathematical representations. The marked integral
conjugacy is already checked by
`probes/P-J-HODGE-PREDICTIVE-CLOSURE-1`; this note does not reclaim it.

In characteristic five, the regular alphabet module has the presentation
`F5[C5]=F5[t]/(t-1)^5`. Hence `C` is one unipotent block of length five,
and `C|A` reduces to one block of length four. This is not a semisimple
decomposition into a constant line and an augmentation complement: division
by five is unavailable. The rational splitting must not be reduced as if it
were an integral splitting. The integral quotient isomorphism induced by
`C-I` remains valid after reduction.

No statement here identifies the standard counting form on a chosen source
with the native checkpoint metric, or interprets the exterior-square
operator as the selected native update.

## 2. Selecting a branch is not adding both branches

For trace `z` and binary driver `t`, the actual fired index is

```text
i=z+2t,  e_i=C^(2t)e_z.
```

The group-algebra sum instead gives

```text
(I+C^2)e_z=e_z+e_(z+2).
```

These are different exact objects. The actual output has augmentation one;
the sum has augmentation two. This discrepancy exists before any dynamics
or statistical interpretation. Quotienting by the constant line does not
repair it: in `E/(Z N)`, the difference is one nonzero basis class,
`[e_(z+2)]` or `[e_z]`. The same mismatch remains after transporting this
quotient to `A` by `C-I`.

Likewise, the possible-alternative pair does not imply that the next trace is
`z+1`, or that a native checkpoint evolves by `I+C^2`. A probability average
would require a separately supplied measure and normalization; neither is
part of this identity.

There is also an inherited symmetry restriction. Canon section 2, “Every
selector-preserving architecture relabeling”, allows an arbitrary checkpoint
permutation `h` and generator-label permutation `pi`, but requires both
generator conjugacy and preservation of the selector with its driver fixed.
Those conditions force `pi(i)=i+c`. The native generator fixed-point counts
`625,25,25,1,1` then force `c=0`. Thus the nontrivial cyclic permutation of
the alphabet is not an allowed relabeling symmetry of the complete native
architecture. This is an existing theorem, not a new automorphism census.

## 3. Exact three-tick loss of initial trace information

Write `X=F5^6`, `z(x)=sum(x)`, and use the native generators exactly as in
Canon section 2. Directly summing their displayed coordinates gives

```text
z(a x)=z(x),
z(b x)=-z(x),
z(c x)=2-z(x),
z(d x)=2-z(x),
z(e x)=3-z(x).
```

For fixed bit `t`, let `T_t` be the induced trace update under the selected
generator `g_(z+2t)`. The preceding five formulas give the entire maps:

| z | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| T_0(z) | 0 | 4 | 0 | 4 | 4 |
| T_1(z) | 2 | 1 | 1 | 3 | 1 |

For every origin-zero head, the first three driver bits are `0,1,1`.
The first map has image `{0,4}`; the second sends these values to `{2,1}`;
the third sends both to `1`. Thus

```text
T_1 T_1 T_0(z)=1 for every z in F5,
z_3=1 for every x_0 in X.
```

On `{1,4}`, `T_0` is constantly `4` and `T_1` is constantly `1`. Induction
now gives the inherited synchronized-trace identity

```text
z_n=4-3 theta_(n-1),
i_n=4-3 theta_(n-1)+2 theta_n,       n>=3.
```

In particular, `theta_3=0` gives `i_3=1`. Both the current trace and current
fired index are independent of the initial checkpoint from tick three
onward. The allowed fired indices thereafter are `{1,3,4}`; the five-symbol
alphabet has not become a five-cycle in actual time.

## 4. Counter plus current index cannot supply a state-dependent amplitude

**Candidate-T, restricted no-go.** Let `V` be any set and let `L:V->V` be a
bijection. For each `x_0 in X`, evolve from
the native origin-zero state `(0,x_0)`. Suppose a single fixed family of
maps `r_n:F5->V`, allowed to depend arbitrarily on the counter `n`, satisfies
either

```text
r_n(z_n(x_0))=L^n v(x_0) for every n>=0 and every x_0,
```

or

```text
r_n(i_n(x_0))=L^n v(x_0) for every n>=0 and every x_0.
```

Then `v:X->V` is constant.

**Proof.** At `n=3` the left side equals `r_3(1)` for every initial head,
for either reader class. Applying `L^-3` proves
`v(x_0)=L^-3 r_3(1)` for every `x_0`. No linearity of the reader, finite
counter, finite image, continuity, or autonomous trace dynamics is assumed.

The J-Hodge operator is invertible, so the theorem applies to the proposed
J-Hodge target. A counter-only orbit `L^n v_0` remains possible, with
externally fixed `v_0`. What is excluded is obtaining a nonconstant
checkpoint-dependent initial amplitude from these current trace/index ports.
This is stronger in its counter allowance than the finite-reader premise of
`P-U-J-HODGE-CHECKPOINT-NOGO-1`, but narrower in its source port. It says
nothing against a reader that uses additional checkpoint coordinates.

## 5. Complete selector history still has only the initial trace as source

The trace recurrence is a closed deterministic recurrence on the five trace
values, driven by the fixed counter word. Therefore the entire trace and
selected-index histories from an origin-zero head depend only on `z(x_0)`.
Conversely, their time-zero index is `i_0=z(x_0)`. Full history thus separates
exactly five initial source classes, namely the trace fibres.

Consequently, allowing the full selector history and the counter in the
reader can restore at most this initial trace dependence. If an exact
invertible-target reading has source amplitude `v(x_0)`, it must factor as
`v=f(z(x_0))`. This is a statement about distinguishable source data, not a
claim that five selected values could not be mapped into a larger ambient
vector space.

One useful compatibility consequence is purely set-theoretic. Suppose the
same amplitude also factors through a source invariant `Q`, and one
`Q` fibre meets every trace fibre. For each `z`, choose an initial head
in that common `Q` fibre with trace `z`. All five values `f(z)` must then
equal the value on that one invariant fibre. Hence `v` is constant. The
explicit invariant `Q` in [the component proof](PROOF.md), section 5,
satisfies this condition: each of its fibres meets every trace sheet.
Therefore a source amplitude factoring through that `Q` and recoverable
from the complete selector history must be constant. This uses the
component proof, not the alphabet representation alone.

## 6. A native cyclic source already exists elsewhere

The claim that the selector alphabet is the only native candidate for a
regular cyclic module is too broad. The earlier candidate
`C-U-CYCLOTOMIC-SOURCE-CARRIER-N`, issue #1000, already proves that the
chronological native generator word

```text
d b d b e b e b
```

is the global translation by `(0,0,0,0,-1,+1)`. It cycles the five
preparations `I_s=(0,0,0,0,-s,s)`. Its rational augmentation module is the
marked `Q(j)` carrier with its exact trace-form/QDD Gram. The actual
three-tick shot on that preparation family transports the marking and is
the identity in the transported cyclotomic charts.

That result is a native kernel-word source symmetry, not a statement that
the selected time evolution repeatedly executes the eight-letter word. It
also does not identify the counter-dependent amplitude law sought here.

The source custody is issue-based. The
[complete proof and disposition](https://github.com/mathorn1973/twist-j/issues/1000#issuecomment-5666231316)
explicitly reports that no file commit or pull request was created. There is
therefore no repository path or commit to cite for that note. Its
[executable freeze](https://github.com/mathorn1973/twist-j/issues/1000#issuecomment-5666166781)
identifies Git blobs `a4da90ab3a0be567b3dfb8ca57d785d519cd083e` and
`ffcfaebcdcad7e547bf732e276ead9c63c60cbeb`, and its
[completed execution record](https://github.com/mathorn1973/twist-j/issues/1000#issuecomment-5666183081)
records two implementations on one local architecture. These are inherited
candidate results, not public two-architecture acceptance or Canon authority.

## 7. Remaining exact obligation

The algebraic correspondence `I+C^2 -> J -> Lambda^2 M_J` is available.
The actual selector supplies neither the sum of alternatives nor a
checkpoint-dependent amplitude after synchronization. A positive native
bridge must therefore specify another state-bearing port or coupling, with
its initial amplitude and update rule fixed before comparison, and prove
the required intertwining on that declared domain. The counter can index a
target orbit; this note does not derive the target orbit from native
selection or identify any coordinate with physical time.
