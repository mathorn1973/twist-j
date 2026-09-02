# P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1 preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**.

Public claim lock `#780` was opened before the branch and immutable pin.
These bytes have no scientific or Canon authority. The accepted `verify.py`
may be read, parsed, compiled, and inspected statically, but it must not be
executed before the immutable public pin has been committed, pushed, and read
back.

```text
PROBE_ID            P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1
TARGET_CLAIM        TM-CHECKPOINT-HULL-STABLE-IMAGE
MODE                PROOF-FIRST / RESULT-EXPOSED
ACTION_LAYER        L1 only
THEOREM_CARRIER     WRITTEN_PROOF_NOT_FINITE_AUDIT
AUTHOR_OF_RECORD    A. M. Thorn
OWNER               A. M. Thorn
CLAIM_LOCK          #780
BRANCH              probe/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1
PATH                probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1/
PUBLIC_STATUS       NONE; candidate-T is available only after the pinned run
                    and required public checks; active T requires a later fold
```

## Authority and collision pin

This preregistration is pinned to this public readback:

```text
STATE:          ACTIVE
CANON:          Public Canon v74
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v74
TAG_OBJECT:     796b09aef958a9021b93cff0df7f300ef95f5337
TAG_TARGET:     05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT: 2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:   2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:    389246
BASE_COMMIT:    8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
```

At that base the content commit and tag target are ancestors of `main`, the
five normative hashes pass, and `canon/CANON.md` is byte-identical to the
declared v74 content. No collision was found for the target claim, probe
identifier, path, or branch in the public registry, probe tree, public issues,
or remote heads. The authority, issue, path, registry, object-lock,
claim-lock, and remote-head scans were repeated immediately before issue #780
and again before the pin. They passed. A later changed normative input or
target scope does not mutate this pin and requires a separately reviewed
successor.

## Prior exposure and novelty boundary

The conclusions and predecessor algorithms were exposed in the internal,
non-authoritative candidates `C-TM-CHECKPOINT-REVERSOR-1` and
`C-TM-CHECKPOINT-STABLE-CORE-2`, including local executions on one
architecture family. This probe is not blind discovery. The exact public-form
`verify.py` beside this preregistration has not been executed. Its result must not be
inferred from the internal bytes; the public formal gate begins only after its
own immutable pin and readback.

The public parent `TM-SHEET-SYNCHRONIZING-GRAPH [T]` already owns the induced
sheet maps, the exact Thue-Morse factors through length sixteen, nine-letter
synchronization, the unique nonsynchronizing word
`w* = 10100101`, its sheet action, and the invariant sheet graph. The new
content is the lift from that five-sheet theorem to the complete checkpoint
hull: its stable image, invertible restriction, exact reversor, full-hull
collision, and natural extension. No existing public claim is restated as a
new discovery.

Dependencies intended for a later Canon fold:

```text
TM-CHECKPOINT-HULL-STABLE-IMAGE  REQUIRES  DEF-KERNEL-GENERATORS
TM-CHECKPOINT-HULL-STABLE-IMAGE  REQUIRES  DEF-SELECTOR
TM-CHECKPOINT-HULL-STABLE-IMAGE  REQUIRES  TM-SHEET-SYNCHRONIZING-GRAPH
```

No measure claim, entropy bridge, decoder bridge, or cross-layer gate is part
of this probe.

## 1. Equation and carrier

All checkpoint arithmetic is in `F_5`. Let

```text
X_cp          = F_5^6,
z_6(psi)      = sum_j psi_j mod 5,
X_z           = {psi in X_cp : z_6(psi)=z},
K_TM          = the two-sided Thue-Morse subshift,
(S_K kappa)_m = kappa_(m+1),
F_eps(psi)    = g_(z_6(psi)+2 eps mod 5)(psi),
X_hull        = K_TM x X_cp,
V_hull(kappa,psi) = (S_K kappa,F_(kappa_0)(psi)).
```

The five public generators are ordered

```text
(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e).
```

Define

```text
h(kappa)          = 4+2 kappa_(-1) mod 5,
X_stab            = {(kappa,psi) in X_hull : z_6(psi)=h(kappa)},
i_stab(kappa)     = 4+2(kappa_(-1)+kappa_0) mod 5,
(rho kappa)_m     = kappa_(-m-1),
R_cp(kappa,psi)   = (rho kappa,g_(i_stab(kappa))(psi)).
```

`X_hull` has the product topology, with `K_TM` compact and `X_cp` finite
discrete. Thus `X_hull` is compact Hausdorff, `V_hull` is continuous, and
`X_stab` is closed.

For the natural extension put

```text
Nat(V_hull)
  = {(x_n)_(n in Z) in X_hull^Z : V_hull(x_n)=x_(n+1) for every n},
(S_nat x)_n = x_(n+1),
e_0(x)=x_0.
```

`Nat(V_hull)` is an auxiliary inverse-limit **L1 state carrier**. It is not a
decoder log, realized-event stream, physical history, or L5 object.

## 2. Frozen candidate theorem

Every clause below has status ceiling `candidate-T / L1` after the immutable
public run and required checks. None has active public status before a later
Canon fold.

### SC1 — invariant checkpoint stable image

`V_hull(X_stab)=X_stab`. On `X_stab` the live selector equals
`i_stab(kappa)`. For

```text
(kappa_(-1),kappa_0) = 00,01,10,11
```

the branches are respectively `e,b,b,d`, and each is a bijection

```text
X_(h(kappa)) -> X_(h(S_K kappa)).
```

### SC2 — invertibility on the stable image

The restriction `V_stab=V_hull|X_stab` is a homeomorphism with

```text
V_stab^(-1)(kappa,psi)
  = (S_K^(-1) kappa,
     g_(i_stab(S_K^(-1) kappa))(psi)).
```

### SC3 — exact checkpoint reversor

`rho(K_TM)=K_TM`, `rho^2=id`, and `rho S_K rho=S_K^(-1)`. The map `R_cp`
is an involutive homeomorphism of `X_stab` and

```text
R_cp V_stab R_cp = V_stab^(-1).
```

This is reversibility of the exact mathematical checkpoint dynamics on
`X_stab`. It is not a physical time-reversal statement about a decoder,
instrument, interaction, trial law, or observation.

### SC4 — exact finite-time stable image

```text
V_hull^9(X_hull)
  = X_stab
  = intersection_(n>=0) V_hull^n(X_hull).
```

Nine is the least exponent with this property. For every subset
`Y subset X_hull` satisfying `V_hull(Y)=Y`, one has `Y subset X_stab`.
`X_stab` is called the finite-time stable image or synchronized reversible
core. It is not called an attractor and is not selected as the physical
carrier.

### SC5 — full-hull noninjectivity

For any `kappa in K_TM` with `kappa_0=0`, let

```text
y     = (0,4,0,0,0,0) in X_4,
psi_b = b(y) in X_1,
psi_d = d(y) in X_3.
```

Then `psi_b != psi_d` but

```text
V_hull(kappa,psi_b)=V_hull(kappa,psi_d)=(S_K kappa,y).
```

Thus `V_hull` is not injective and is not a homeomorphism on `X_hull`; it is
not reversible there in the standard dynamical-systems sense. No broader
semigroup no-go or claim about differently defined reversal relations is
made.

### SC6 — natural extension equals the stable image

Evaluation at zero is a homeomorphism

```text
e_0: Nat(V_hull) -> X_stab
```

and a conjugacy

```text
e_0 S_nat = V_stab e_0.
```

Its inverse sends `x in X_stab` to the unique bi-infinite orbit
`(V_stab^n x)_(n in Z)`. This is a theorem about the auxiliary L1 natural
extension only; it does not retype a public decoder or event stream.

## 3. Written proof

### 3.1 SC1 and SC2

Write `u=kappa_(-1)` and `v=kappa_0`. On `X_stab` the source sheet is
`4+2u`, so the live selector is

```text
(4+2u)+2v = 4+2(u+v) mod 5 = i_stab(kappa).
```

For `(u,v)=00,01,10,11` this is `4,1,1,3`, namely `e,b,b,d`. Directly from
the public sheet table, these branches carry the source sheets
`4,4,1,1` to the target sheets `4,1,4,1`, exactly
`h(S_K kappa)=4+2q`. Each public generator is an involution, hence each
restriction is a bijection. This proves SC1.

After one forward step, applying the same edge branch from the inverse-shifted
base undoes the involution. Conversely, applying the proposed inverse first
and then the forward branch does the same. The displayed maps are continuous,
so `V_stab` is a homeomorphism and SC2 follows.

### 3.2 Universal reversal invariance of the Thue-Morse hull

Let `t_n=s_2(n) mod 2`. For `0<=n<2^k`, subtraction from the `k`-bit word of
all ones complements every bit, so

```text
s_2(2^k-1-n)=k-s_2(n).
```

For even `k` this gives

```text
t_(2^k-1-n)=t_n.
```

Take an arbitrary factor

```text
w=t_j t_(j+1) ... t_(j+ell-1)
```

and choose even `k` with `j+ell<=2^k`. Put `a=2^k-j-ell`. For
`0<=r<ell`,

```text
t_(a+r)
  = t_(2^k-1-(j+ell-1-r))
  = t_(j+ell-1-r).
```

Thus the factor starting at `a` is exactly `reverse(w)`. The complete
Thue-Morse language is closed under reversal. Every finite block of
`rho kappa` is the reversal of a finite block of `kappa`; hence
`rho(K_TM) subset K_TM`. Since `rho^2=id`, equality follows. The identities
`rho^2=id` and `rho S_K rho=S_K^(-1)` are immediate from the indices.

This universal argument is load-bearing. A finite factor check is only an
audit and is not substituted for it.

### 3.3 SC3

The adjacent bits are exchanged by `rho`, so

```text
i_stab(rho kappa)=i_stab(kappa).
```

The branch `g_(i_stab(kappa))` carries the sheet `h(kappa)` to
`h(rho kappa)` by the same four-case table used in SC1. Therefore `R_cp`
maps `X_stab` to itself. The branch is involutive, `rho^2=id`, and the
selector is unchanged, so `R_cp^2=id`.

For the reversor identity, the inner `R_cp` and the following `V_stab` use
the same branch `g_(i_stab(kappa))`, which cancels with itself. At the outer
`R_cp` the selector is

```text
i_stab(S_K rho kappa)
  = 4+2(kappa_(-1)+kappa_(-2))
  = i_stab(S_K^(-1) kappa),
```

and the base is `rho S_K rho kappa=S_K^(-1)kappa`. The result is exactly the
inverse in SC2. This proves SC3.

### 3.4 SC4

For every length-nine Thue-Morse factor
`u=kappa_0...kappa_8`, the public parent theorem says that its sheet
composition is the constant map with value

```text
4+2 kappa_8 = h(S_K^9 kappa).
```

Therefore `V_hull^9(X_hull) subset X_stab`. By SC2,
`V_hull^9(X_stab)=X_stab`, while `X_stab subset X_hull`; hence the reverse
inclusion holds and

```text
V_hull^9(X_hull)=X_stab.
```

SC1 then gives `V_hull^n(X_hull)=X_stab` for every `n>=9`, proving the
intersection equality.

Sharpness uses the occurring word `w*=10100101`. Its public sheet action
sends initial sheet `0` to sheet `2`, while its last bit is `1`, so the
required stable sheet after eight steps is `4+2=1 mod 5`. Starting with the
zero checkpoint in `X_0` therefore gives a point of
`V_hull^8(X_hull)` outside `X_stab`. If an earlier image had already equalled
`X_stab`, forward invariance would force the eighth image to equal
`X_stab`; thus nine is least.

If `V_hull(Y)=Y`, then

```text
Y=V_hull^9(Y) subset V_hull^9(X_hull)=X_stab.
```

This completes SC4.

### 3.5 SC5

The displayed states lie on sheets `1` and `3`. At current bit zero their
selectors are therefore `b` and `d`. Since both generators are involutions,

```text
F_0(b(y))=b^2(y)=y,
F_0(d(y))=d^2(y)=y.
```

The states are distinct, while their base coordinates also acquire the same
shift. This proves the collision and SC5.

### 3.6 SC6

Let `(x_n)_(n in Z)` belong to `Nat(V_hull)`. For every `r>=0`, the point
`x_0` has the predecessor `x_(-r)`, so

```text
x_0 in V_hull^r(X_hull).
```

SC4 gives `x_0 in X_stab`. SC2 then makes every positive and negative
coordinate uniquely equal to `V_stab^n(x_0)`. Conversely, every point of
`X_stab` has that unique bi-infinite orbit. Thus `e_0` is bijective and
intertwines the two shifts.

`Nat(V_hull)` is closed in the compact product `X_hull^Z`, hence compact;
`X_stab` is Hausdorff. Evaluation is continuous, so the continuous bijection
`e_0` is a homeomorphism. This proves SC6.

## 4. Code

`verify.py` is a zero-input, Python-standard-library-only exact audit. It uses
integer arithmetic modulo five, reads no files, uses no network or subprocess,
and has deterministic ASCII stdout with a final newline. It checks:

```text
I01  public pin identity, arguments, and deterministic environment;
C01  all five generator involutions, (bc)^5, trace laws, sheet maps;
C02  every one of the ten sheet arrows is a full leaf bijection;
L01  the registered Thue-Morse factor counts and finite reversal audit;
S01  SC1 branch table and full checkpoint-leaf bijections;
S02  SC2 inverse identities on every required window and leaf state;
S03  SC3 index bookkeeping and reversor identities;
S04  nine-step synchronization and the sharp eight-step obstruction;
S05  the explicit SC5 collision;
S06  the finite stable-image reductions used by the written SC6 proof.
```

The written proof, not finite sampling, carries the universal language,
topological, inverse-limit, and all-subset statements. A future formal run
must use the repository command

```text
python3 probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1/verify.py
```

under the deterministic public environment and external timeout required by
the repository. A mismatch in the embedded claim lock must stop before any
scientific gate.

## 5. Carrier and data

The complete carrier is the public `F_5^6` checkpoint with its five declared
affine involutions, the two-sided Thue-Morse hull, and the product
`X_hull`. `X_stab` is the displayed closed graph subset. The verifier rebuilds
all finite checkpoint states and the finite substitution-language audit from
definitions. There is no external data.

## 6. Systematics and failure threshold

The shift convention and edge-centred reversal are load-bearing. Words act in
temporal order. Sheet labels are `z_6` values and are not the checkpoint
coordinate named `q`. The exponent nine means the least `n` with
`V_hull^n(X_hull)=X_stab`; it is not an attraction-rate or physical-time
claim. Natural-extension points are auxiliary L1 states, not L5 event logs.

A single exact counterexample to any SC1--SC6 equality, inclusion,
bijectivity, collision, least-exponent statement, reversal identity, or
natural-extension conjugacy falsifies the corresponding candidate clause.
An invalid environment, argument, claim-lock mismatch, exception,
unreadable pin, nonempty stderr, unexpected exit, or cross-architecture byte
mismatch is integrity `STOP`, not scientific falsification. Frozen thresholds
do not move after the public pin.

The intended exit map is:

```text
0  every frozen audit gate passes;
1  integrity STOP;
2  an exact scientific audit gate is falsified.
```

## 7. Scope firewall

No Borel probability, invariant measure, Haar measure, `A_A` member,
`ENTROPY-LAYER-BRIDGE` consequence, physical carrier, transient-state
disposition, arrow of time, physical time reversal, decoder, instrument,
trial, event, observation, probability, SI quantity, or L2--L6 lift is
claimed. No uniqueness of the reversor is claimed. The four-phase hull is a
separate lane. Public Canon v74, its Registry, Frontier, dependencies, gates,
and release remain unchanged by this probe and by the later probe result; any
active `[T]` treatment belongs only to a separately claimed v75 fold.
