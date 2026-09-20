# Conditional construction from reversible field arithmetic

**PUBLIC; candidate-T, L1, NON-CANONICAL.** This is a mathematical
sufficiency result in an explicitly enlarged operation family. It does
not derive that family from native `U`, identify a material interaction,
or fill the physical admission fields of the
[entrance contract](../P-QDD-UNINTERRUPTED-RECORD-1/ENTRANCE-CONTRACT.md).
No Hamiltonian is defined by taking a logarithm of the target operation.

## 1. Independently stated primitive family and timing convention

Work over `F5`. Adjoin three work registers `(w,v,u)`, each initially zero.
The arithmetic family consists of:

1. Reversible affine transformations on finitely many `F5` registers.
2. Reversible multiply-add transformations

   `M_(i,j;k,c): x_k <- x_k + c*x_i*x_j`,

   where `i,j,k` are three distinct register indices and `c in F5`.
   Controls and all other registers are unchanged. The inverse replaces
   `c` by `-c`.

This is a family defined for arbitrary field data, independently of the
particular LOW/HIGH target. Its availability is an **added assumption**.
In particular, native affine generators do not themselves supply this
multiply-add resource by definition. A decomposition in this family is an
arithmetic synthesis result, not evidence of physical admission.

The native state is `x=(p;q,r)`, with `p=(a,b,c,d)` and
`z=a+b+c+d+q+r`. Work registers are external to the native selector and
remain fixed during native ticks. A completed arithmetic block is applied
at a named native-counter cut. Any finite number of native ticks, with
either driver bit at each tick, may occur between completed blocks.

A balanced port addition with work-dependent value `A` means

`(q,r) <- (q-A,r+A)`.

An affine `A` uses one affine block. For `A=c*x_i*x_j`, with work-register
controls, it is the composition of the two allowed multiply-add gates to
`q` and `r`. **No native tick is allowed between these two halves.** They
form one completed balanced block for the interleaving theorem. The halves
commute, but each half separately need not preserve `z`; commutation alone
would not make an interposed native tick harmless.

This cut convention makes no physical zero-duration assertion. A physical
implementation must separately justify the duration, synchronization,
intermediate dynamics and decoupling of these blocks. The theorem permits
uninterrupted native ticks in its stated discrete schedule; it does not
prove that a laboratory pulse has this schedule or that `U` continues
unchanged inside either multiply-add half.

## 2. Native input and a work-register copy of the transported label

Start at counter `n>=3` on a fixed known sheet `z_n in {1,4}`. Let

`h_t(x)=(-1)^(t-3)(a+b+c+d)`.

The previously proved native transport theorem supplies, for every native
driver word on the stable union:

`h_(t+1)(F_b x)=h_t(x)`,

`F_b T_delta x = T_(-delta) F_b x`,

where `T_delta` is the balanced port translation. The symbol `b` in
`F_b` denotes a driver bit, not the named native generator. Native `U`
acts identically on the source and selector path before and after any
balanced translation on this region.

At a known current sheet, the label also has the equivalent expression

`h_t(x)=(-1)^(t-3)(z_t-q-r)`.

Thus extracting it into a work register is an affine reversible operation
on the joint registers. It can be defined directly using the four source
coordinates, or using `q,r` and the known sheet constant. This equality
does not identify `q+r` with a physical charge or supply the interaction
needed to copy it.

At the launch cut apply

`w <- w+h_n(x)`.

For the zero work input this gives `w=h`, where `h=h_n(x)`. Subsequently
`w` retains the launch label while native `U` runs. A coherent copy of a
basis label is meant here: no measurement or selection of a classical
value is performed. The work register is generally correlated with the
source until the final reversal.

## 3. Full five-value target and exact arithmetic schedule

The fixed target function is

`f(0)=0, f(1)=1, f(2)=f(3)=f(4)=2`.

Over `F5` it has the polynomial identity

`f(h)=h+h^2+h^3+3*h^4`.                                      (C1)

For example, the right side has values `0,1,2,2,2` at `0,1,2,3,4`.
This is the already fixed off-code extension, not a newly fitted
extension. On `F5*`, one may replace `h^4` by `1`, giving the cubic
`h^3+h^2+h+3`; the construction below retains (C1) including `h=0`.

After extracting `w=h`, perform the following work operations. Native
ticks may be interposed between any two rows.

| Operation | Work registers `(w,v,u)` after the operation |
| --- | --- |
| Initially | `(h,0,0)` |
| `v <- v+w` | `(h,h,0)` |
| `u <- u+w*v` | `(h,h,h^2)` |
| `v <- v-w` | `(h,0,h^2)` |
| `v <- v+u` | `(h,h^2,h^2)` |

Every multiplication uses distinct controls and a distinct target. No
square operation with two identical control registers is assumed.

Apply four balanced port blocks, with the indicated values. They may be
separated by arbitrary native ticks:

| Balanced block | Value added to `r` and subtracted from `q` |
| --- | --- |
| First, at counter `t_1` | `beta_(t_1)*w` |
| Second, at counter `t_2` | `beta_(t_2)*u` |
| Third, at counter `t_3` | `beta_(t_3)*w*u` |
| Fourth, at counter `t_4` | `3*beta_(t_4)*u*v` |

Here

`beta_t=(-1)^(t-n)`.

The first two blocks are affine; the other two use the paired
multiply-add construction from section 1. The four unweighted values
sum to the polynomial in (C1).

Finally reverse the work calculation:

| Operation | Work registers after the operation |
| --- | --- |
| Before reversal | `(h,h^2,h^2)` |
| `v <- v-u` | `(h,0,h^2)` |
| `v <- v+w` | `(h,h,h^2)` |
| `u <- u-w*v` | `(h,h,0)` |
| `v <- v-w` | `(h,0,0)` |
| At current counter `t`, `w <- w-h_t(x)` | `(0,0,0)` |

Native ticks may again occur between these completed blocks. The last
operation clears `w` using the **current** transported label, not an
inverse of the original source path. Since all source-touching work
operations preserve the native state and every completed port block
preserves `p,z`, the required equality `h_t(x)=h` still holds.

## 4. Exact interleaving theorem

Let `N=n+d` be a cut after work cleanup, possibly after additional native
ticks. Let `N_(n,d)` denote the native word actually applied throughout
the schedule, with all `d` ticks counted. The driver word and arithmetic
schedule are fixed independently of the source label. On the initially
chosen sheet and zero work registers, the construction satisfies

`Phi_(n,d)(x;0,0,0) = (N_(n,d) C_n x;0,0,0)`,               (C2)

where `C_n x=T_(f(h_n(x)))x`.

**Proof.** Completed work operations leave the native checkpoint
unchanged. Completed port blocks leave its source and trace unchanged.
Hence all native ticks stay in the stable union and select the same
generator as the reference free trajectory. In particular, source and
trace match that trajectory at every completed block and native tick.

A port increment `beta_t*A(h)` applied at counter `t` contributes at the
completion counter `N`

`(-1)^(N-t)*beta_t*A(h)=(-1)^(N-n)*A(h)`.

This follows by repeated native sign reversal. Balanced translations form
an additive group, so the four increments give exactly

`(-1)^d * (h+h^2+h^3+3*h^4) = (-1)^d*f(h)`.

The work table proves exact cleanup. Native label invariance proves the
last cleanup step even when native ticks have elapsed since extraction.
The final native point is therefore

`T_((-1)^d*f(h)) N_(n,d)x = N_(n,d) C_n x`,

which is (C2). No finite sample of words replaces this induction. QED.

The theorem is valid for every source point and every port value on the
chosen initial stable sheet, including `h=0`. Readiness of the native
port is not needed for this entrance identity; readiness remains needed
by the later clean-record protocol. The three work registers do require
the declared zero input. No all-state extension across other trace sheets
is asserted.

Each nonnative operation is a global permutation on its declared
registers. The native step is used only on a known sheet where its selected
affine generator is bijective. No inverse or unitary extension of global
native `U` is assumed.

## 5. Full coherent equality and absence of retained fine labels

Extend the stipulated point permutations linearly. On the canonical
four-point code `K_n`, each native tick is injective, and the three work
registers finish in the same state for every source label. Consequently
for every code amplitude `psi`,

`Phi_(n,d)(psi tensor |0,0,0>)`

`    = V_(n,d) psi tensor |0,0,0>`,                          (C3)

with the exact target `V_(n,d)` of the entrance contract and common phase
equal to zero. All sixteen code matrix units are carried to their target
matrix units; in particular none of the six HIGH off-diagonal units is
removed. Equation (C3) remains true after tensoring with an arbitrary
untouched reference and with prior records on which all operations act
as the identity.

The temporary work registers do distinguish fine labels, but this
information is reversibly removed from them. Retaining a copy of `w`,
measuring it, or leaving any unlisted environment correlated with it
would invalidate (C3). Cleanup is therefore part of the construction,
not permission to disregard an environment.

This is a full equality for the explicitly admitted mathematical
registers. It is not a factorization theorem for an unmodelled physical
controller, clock, field or environment. Such carriers must be added to
the physical witness before the entrance contract's equation (E2) can be
claimed for an apparatus.

## 6. Resource and physical interpretation

The arithmetic construction identifies a sufficient extra resource:
reversible multiplication of two field values, with clean work storage
and balanced access to the native port. It uses neither `C_n` itself nor
its LOW projector as a primitive. The primitive law is the same for any
polynomial target. The chosen sequence implements the previously frozen
function `f`.

The two multiplicative data-dependence layers in the forward computation
are `h -> h^2` and `(h,h^2) -> (h^3,h^4)`. This describes this circuit's
arithmetic structure; it is not a lower bound on physical interaction
time, the number of physical particles, or general quantum circuits.

Balanced blocks conserve `q+r` and `z` at their boundaries. These are
equalities of native coordinates, not statements about physical energy,
charge, spatial locality or a conservation law imported without a
dictionary. The three-register multiply-add primitive has a bounded
register support, but no physical spatial adjacency has been specified.

The construction still adds an intervention: `q,r` change. It does not
satisfy `feeds_U=false` merely because `p,z` remain on their free paths.
Nor does it show that source-dependent selector routing, alternative
nonlinear architectures or a larger physical operation family are
impossible. Those are distinct classes.

The remaining physical question is now concrete: does an independently
admitted carrier supply the nonlinear resource, clean preparation,
balanced port access, timing and complete output factorization used
above, or another law yielding the same coherent target? A mathematical
field circuit does not establish any of these physical facts. In
particular, it supplies no SI time scale, material archive, realized
single event or occurrence law. `QDD-INSTRUMENT-APPARATUS` stays open.
