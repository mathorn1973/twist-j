# Post-synchronization boundary for fresh affine payload records

**NON-CANONICAL analytic draft — 2026-10-29.**

This note states a conditional mathematical boundary for the unchanged native
update. It is intended to accompany a positive, prepared one-shot construction;
it does not withdraw that construction or claim that all native transfer is
impossible. No scientific code, exhaustive enumeration, or new validation run
was used to obtain the argument below. This note is not an accepted theorem,
registry entry, physical prediction, or change of public status.

The source basis is Public Canon v106 at main commit
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`, specifically the named sections of
[the pinned Canon](https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/canon/CANON.md)
identified in Section 7. The statement is a direct analytic consequence of
the displayed native formulas and the native Thue–Morse driver. No claim of
novelty relative to the Canon is made.

## 1. Exact domain and record contract

All checkpoint arithmetic is in `F_5`. Write

```text
x = (a,b,c,d,q,r),
z(x) = a+b+c+d+q+r,
theta_n = popcount(n) mod 2,
F_t(x) = g_(z(x)+2t mod 5)(x),
U(n,x) = (n+1,F_(theta_n)(x)).
```

The generator order is `(g_0,g_1,g_2,g_3,g_4) = (g_a,g_b,g_c,g_d,g_e)`.
The letter `g_b` denotes a generator, whereas the bare letter `b` in a
checkpoint denotes its second coordinate.

Let `Lambda` be any message set and let `E: Lambda -> F_5^6` be any family of
preparations at the same counter origin zero. Define the actual native
trajectory

```text
x_lambda(n) = pr_checkpoint U^n(0,E(lambda)).
```

Fix one common integer `m >= 3`. Native synchronization gives the reachable
sheet

```text
X_m = {x : z(x)=4+2 theta_(m-1)}.
```

In particular, every `x_lambda(m)` lies on this one sheet. Although every
point of `X_m` is reachable, the argument does not assume a physical method
for preparing an arbitrary point at counter `m`.

The target observation is one fixed affine map

```text
H: F_5^6 -> F_5^d,       H(x)=Lx+h,
```

where `d` is any finite nonnegative integer. Projection onto a fixed subset
of the six original raw coordinates is a special case. Fresh readiness
means equality of the **complete target state** at the common time `m`:

```text
H(x_lambda(m)) = h_ready                 for every lambda.       (R1)
```

Equality of decoded BLANK labels alone does not satisfy (R1).

A current-target reader may be any total function

```text
D: N_0 x F_5^d -> Y.
```

It is allowed the actual counter, arbitrary nonlinearity, and arbitrary
time dependence through that counter. It receives no message label, saved
preparation, retained target history, or additional message-dependent input.
Common fixed parameters may be included in its definition.

For a proposed payload `f: Lambda -> Y`, permanent readback means that for
each message there is a finite `N_lambda >= m` such that

```text
D(n,H(x_lambda(n))) = f(lambda)          for every n >= N_lambda. (R2)
```

The onset may depend on the message. The requirement is nevertheless
readback at **every** sufficiently late native counter, not only at selected
sampling times.

## 2. Statement

**Conditional boundary.** Under the unchanged native update and contracts
(R1)–(R2), the payload `f` is constant.

Equivalently, no fixed affine target that is completely message-independent
at a common synchronized checkpoint can acquire a nonconstant permanent
payload readable from its current state, even when the reader receives the
actual counter.

This does not forbid a source-independent completion marker. For example,
a counter-dependent reader can change a common label at a prescribed time.
The excluded object is a permanent record that distinguishes messages which
were absent from the complete target state at `m`.

## 3. Common affine form of the synchronized native tail

The stable selector table is

| Current `z` | Driver bit `t` | Selected generator | Next `z` |
| --- | --- | --- | --- |
| 1 | 0 | `g_b` | 4 |
| 1 | 1 | `g_d` | 1 |
| 4 | 0 | `g_e` | 4 |
| 4 | 1 | `g_b` | 1 |

For actual origin-zero trajectories at every `j >= 3`,

```text
z_j = 4+2 theta_(j-1).
```

Thus the selected generator at a common counter is the same for every
reachable head label. More precisely,

```text
g_b is selected at step j  iff  theta_j != theta_(j-1).           (L1)
```

Define the coordinate permutation

```text
P(a,b,c,d,q,r) = (c,d,a,b,q,r),       P^2=I.
```

The three selected generators have the exact affine forms

```text
g_b(x) = -P x,
g_d(x) = -x+c_d,       c_d=(2,1,3,4,1,1),
g_e(x) = -x+c_e,       c_e=(2,1,3,4,2,1).
```

Let `B(m,n)` count the selections of `g_b` at steps `m,...,n-1`. Since the
linear parts `-P` and `-I` commute, composition of the common selected word
gives, for every `x_m in X_m`,

```text
x_n = (-1)^(n-m) P^(B(m,n)) x_m + c_(m,n),                       (L2)
```

where `c_(m,n)` is the common affine offset of that word. It depends on
`m,n`, but not on the message or on the point `x_m` within the sheet. This
uses the affine extension of the common generator word; it does not assert
that the globally state-selected map is affine or injective.

Equation (L1) yields the parity identity

```text
B(m,n) mod 2
  = sum_(j=m)^(n-1) (theta_j XOR theta_(j-1)) mod 2
  = theta_(n-1) XOR theta_(m-1).
```

Therefore

```text
x_n = (-1)^(n-m)
      P^(theta_(n-1) XOR theta_(m-1)) x_m + c_(m,n).              (L3)
```

For two messages the common translation cancels:

```text
x_lambda(n)-x_mu(n)
  = (-1)^(n-m) P^(theta_(n-1) XOR theta_(m-1))
    (x_lambda(m)-x_mu(m)).                                      (L4)
```

This is an identity on the actual synchronized native trajectories, not a
claim about freely selected commands.

## 4. Infinitely many common times erase every fresh affine distinction

Put `eta=theta_(m-1)`. For every integer `k >= 1`,

```text
theta_(2^k)=1,       theta_(2^k+1)=0.
```

Consequently the following explicit times have
`theta_(n_k-1)=theta_(m-1)`:

```text
if eta=1:    n_k=2^k+1;
if eta=0:    n_k=2^k+2.                                        (L5)
```

Taking `k` sufficiently large ensures `n_k >= m`, and these times are
unbounded. At each such time the permutation in (L4) is the identity:

```text
x_lambda(n_k)-x_mu(n_k)
  = (-1)^(n_k-m) (x_lambda(m)-x_mu(m)).                           (L6)
```

By affinity and (R1),

```text
H(x_lambda(n_k))-H(x_mu(n_k))
  = (-1)^(n_k-m) L(x_lambda(m)-x_mu(m))
  = 0.                                                        (L7)
```

Thus the complete target states are again equal across all messages at
infinitely many common future times. Their common value need not equal
`h_ready` and need not be the same at different `n_k`. The proof requires
neither a literal raw reset nor a recurrence of the complete checkpoint.

To prove the boundary, fix any two messages `lambda,mu`. Select one of
the times (L5) larger than both finite onsets `N_lambda,N_mu`. The reader
then receives the identical counter and identical complete target state
for the two messages. Equation (R2) forces

```text
f(lambda)
 = D(n_k,H(x_lambda(n_k)))
 = D(n_k,H(x_mu(n_k)))
 = f(mu).
```

The pair was arbitrary, so `f` is constant. No uniform onset across the
whole family is needed. This completes the analytic proof.

## 5. Sharper corollary for the native port and closed raw blocks

The permutation `P` preserves the four raw coordinate blocks

```text
(a,c),       (b,d),       q,       r.
```

Every selected synchronized generator acts separately on these blocks,
with a common counter-dependent choice of affine map. A target formed by
a union of these blocks is therefore closed on the synchronized family.
If its complete state is common at `m`, its complete state is common at
**every** later counter. Its whole subsequent target history is common as
well. A history processor with common initialization and only this history
and common clock inputs cannot distinguish the messages.

For the single port coordinate `r`, equation (L3) reduces to

```text
r_n = (-1)^(n-m) r_m + kappa_(m,n),                              (P1)
```

with a source-independent offset. Therefore a common ready `r_m` cannot
become a source-dependent pulse displacement under unchanged synchronized
evolution, even at a single prescribed later counter. A desired nonconstant
controlled paired shift

```text
T_(f(source))(p;q,r) = (p;q-f(source),r+f(source))
```

would require a nonconstant source-dependent change of `r`; (P1) excludes
that creation from the common ready port in this class.

This is consistent with the inherited paired-port transport law. A
displacement already inserted at preparation is transported as
`delta -> (-1)^(n-m) delta`. Transport of a pre-existing displacement is
not its native source-controlled writing from a common ready port.

Actual port values are not independent of all retained head labels:
`r_m` itself may vary. The claim is that the **port evolution map** is
common, and hence cannot turn independent source variation into a new
port distinction when `r_m` is fixed.

A target that contains only one member of a piston pair is not necessarily
closed. It can receive temporary information from the other member during
a swap. Sections 2–4 still exclude a nonconstant permanent current-target
record if its complete state was common at `m`.

## 6. Scope and compatibility with a positive one-shot construction

The common reachable sheet is essential. The stable union
`X_1 union X_4` by itself is not the same domain: preparations choosing
different initial stable sheets at one counter can select different next
generators and port offsets. Such a phase-dependent first step is not
covered by the assertion that all synchronized messages use a common
word. Every actual origin-zero family does occupy a common sheet from
counter three onward.

The canonical one-shot source transfer uses the transient generator `g_a`
before synchronization:

```text
(lambda,0,-lambda,0,0,0) -> (0,lambda,0,-lambda,0,0).
```

The receiver is already message-dependent at counter one. The permanent
completion mark becomes available at counter three, but that does not
make the receiver a fresh common-ready target at counter three. The
one-shot writer therefore does not satisfy premise (R1) at the proposed
post-synchronization starting point and is not contradicted.

Likewise, a new prepared one-shot construction that transfers information
during the initial transient must be checked on its own declared
preparations and full states. The present boundary does not determine
whether such a transient construction exists or what it can write.

For a general affine target, the proof excludes permanent readback from
the current target state. It does not exclude temporary readback, selected
sampling times, or retaining an informative intermediate observation in
additional memory. The all-history exclusion in Section 5 is restricted
to the closed raw blocks stated there.

The argument does not classify arbitrary nonlinear definitions of a
subsystem. It does not cover a changing target map `H_n`, a moving address,
a message-dependent start or sampling rule, an off-sheet reset, a new input
after the declared preparation, an added coupling, or a larger architecture.
These are changes to the stated contract, not conclusions of this note.

In particular, this result does not identify physical locality, a
Hamiltonian, Born occurrence, proper time, a Lorentz carrier, an energy
resource, or a material implementation of the reader. It is a boundary
inside one exact finite native model.

## 7. Overlap with existing Canon results

All entries below refer to the pinned Canon named at the start. They remain
the accepted source statements; this draft introduces no replacement row.

| Existing section | Relevant content and relation to this note |
| --- | --- |
| `KERNEL-Z6-SYNCHRONIZATION` | Supplies the common actual reachable sheet from counter three and its 3125 states. The stable two-sheet union alone is insufficient for the common-word argument. |
| `U-NATIVE-CHART-AND-QDD-READBACK` | Supplies the synchronized chart, retained labels, and all-clock affine coordinate formulas. The present calculation isolates the common signed permutation acting on differences. |
| `U-STABLE-PAIRED-PORT-TRANSPORT` | Supplies the stable selector table and transport of an already present paired displacement. It does not assert that the displacement is created by an endogenous actuator. |
| `U-NATIVE-INVARIANT-AND-NOWRITE` | Classifies invariant fixed checkpoint readers and uses actual recurrence to exclude a distinct synchronized BLANK followed by permanent WRITTEN output. It allows nonlinear fixed checkpoint readers, but does not give those readers the unbounded absolute counter. This note instead assumes a common complete affine target state across messages and allows an arbitrary counter-dependent current-target decoder. These are different contracts. |
| `U-FINITE-HISTORY-CLOCK-PHASE` and its finite-window no-write statement | Actual finite decorated words recur; a fixed finite-window reader cannot first change from synchronized BLANK to a permanent value. It allows nonlinear fixed window readers but excludes growing history and the unrestricted absolute counter. The proof here uses only the explicit times (L5), not the finite-word recurrence theorem. |
| `U-NATIVE-RECORD-CONTINUATION-BOUNDARY` | For its particular one-shot family, all later message differences remain in one memory direction. A fresh fixed raw target or fixed affine observation cannot acquire that message later. Its family-specific result is stronger about the complete intervening history. The present draft ranges over arbitrary synchronized preparation families, but for a general affine target proves only infinitely many future common states and the resulting permanent-record obstruction. |
| `U-ORIGIN-AFFINE-COMMON-RESET-BOUND` | A common raw affine observation at counter two permits at most two raw values at counter three, and at most one eventual nonblank label under its fixed decoder contract. That theorem treats the last transient step; this note starts at any common counter `m>=3` and permits an arbitrary counter-dependent decoder. |
| `U-ORIGIN-NONLINEAR-TWO-MESSAGE-READOUT` | Uses a nonlinear global coordinate chart and the initial transient. Its existence is not a native local detector or a counterexample to the fixed-affine synchronized contract. |
| `U-FIXED-FAMILY-READOUT-COMPLEXITY` and `U-ALTERNATIVE-AFFINE-SEMANTIC-READOUT` | Distinguish common decoded BLANK from common raw readiness. The displayed affine semantic witnesses can retain message information in different raw blank values, so they do not meet (R1). |

The useful content of this draft is the explicit contract and short
unbounded-time proof under that contract. It should not be described as a
new general no-writing theorem, a physical no-go theorem, or evidence
against the already established transient one-shot record.

## 8. Mathematical failure conditions and validation status

A failure of the proof would require, on the declared origin-zero
synchronized domain, a failure of at least one load-bearing statement:

- The common-sheet selector condition (L1).
- The common signed-permutation difference identity (L4).
- The explicit native-bit identities used in (L5).
- Affine cancellation from complete target equality (R1) to (L7).

A proposed counterexample to the record boundary must give the unchanged
native preparation family, one fixed affine target with complete equality
at a common `m>=3`, one common reader of only the current target and actual
counter, and a nonconstant payload retained at every sufficiently late
counter. Merely exhibiting a temporary target distinction, a decoded BLANK
with hidden payload, or a writer in the initial transient does not meet
that counterexample contract.

**Validation status:** analytic derivation only in this note. No executable
scientific validation, cross-architecture replay, independent acceptance,
or public promotion is asserted.
