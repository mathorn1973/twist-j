# Proof: exact permission kinds needed by H_B, and where they stop

**NON-CANONICAL / L1 / candidate-T analytical proof (self-reviewed,
not independently reviewed).** All equalities are exact over `F_5`
and `Q`. The grammars, target, witnesses and verdict labels are those
frozen in `CONTRACT.md` and `PREREG.md`. Inherited statements are
named as premises; only the labelled new statements are claimed here.

## 1. Q0: the native alphabet audit

Write each generator as `g_i(x) = M_i x + c_i` on
`x=(a,b,c,d,q,r) in F_5^6`. For an affine map `x -> Mx + c`,

```text
(Mx+c) composed with itself sends x to M^2 x + (M+I)c,
```

so it is an involution for every `x` iff `M^2 = I` and `(M+I)c = 0`
(sufficiency by substitution; necessity by `x=0` and then the
standard basis). Reading `M_i` and `c_i` from the frozen formulas:

- `g_0`: `M_0` swaps `a<->b` and `c<->d` and fixes `q,r`; disjoint
  transpositions, so `M_0^2=I`; `c_0=0` (linear).
- `g_1`: `M_1(a,b,c,d,q,r)=(-c,-d,-a,-b,-q,-r)`. Applying `M_1` to
  `(-c,-d,-a,-b,-q,-r)` returns `(a,b,c,d,q,r)` component by component
  (e.g. first output `-(-a)=a`); hence `M_1^2=I`; `c_1=0` (linear).
- `g_2`: `M_2(a,b,c,d,q,r)=(-c,-d+r,-a,-b-r,-q,-r)`,
  `c_2=(2,1,2,1,1,0)`. With `y=M_2 x`:
  `M_2 y = (-y_c, -y_d+y_r, -y_a, -y_b-y_r, -y_q, -y_r)`
  `= (a, (b+r)-r, c, (d-r)+r, q, r) = x`, so `M_2^2=I`. And
  `M_2 c_2 = (-2,-1,-2,-1,-1,0) = (3,4,3,4,4,0)`, whose sum with
  `c_2` is `(5,5,5,5,5,0)=0` in `F_5`; hence `(M_2+I)c_2=0`.
- `g_3`: `M_3=-I`, `c_3=(2,1,3,4,1,1)`; `M_3^2=I` and `M_3+I=0`.
- `g_4`: `M_4=-I`, `c_4=(2,1,3,4,2,1)`; same conclusion.

Therefore `g_i^2=I` for all five, symbolically, on the whole carrier.
For `z_6(x)=a+b+c+d+q+r`, direct summation of the output coordinates
gives `z_6` under `g_0` (a permutation), `-z_6` under `g_1`,
`7-z_6=2-z_6` under `g_2` (constants `2+1+2+1+1=7`; every variable,
including `r` via `r-r-r`, has coefficient `-1`),
`12-z_6=2-z_6` under `g_3`, and `13-z_6=3-z_6` under `g_4`, exactly
the frozen table. The shifts are genuinely affine:
`g_2(0)=(2,1,2,1,1,0)`, `g_3(0)=(2,1,3,4,1,1)`,
`g_4(0)=(2,1,3,4,2,1)` are nonzero while `g_0(0)=g_1(0)=0`; no
contradiction with linearity of `g_0,g_1` or with the `z_6` table
arises. The Canon v101 "Native conventions" formulas are literally
these maps (its `1-d+r` is `1+r-d`); the index order and carrier are
the same as #1489, so there is no discrepancy to report. None of this
supplies an inverse for the selector-defined `U`, whose chosen letter
depends on the current `(z_6(x), theta_n)`: generator involutions do
not prove `U` bijective, in agreement with the inherited #1489 limit.
This discharges Q0 as an audit; the finite census #1492 (premise, not
rerun here) is consistent with it.

## 2. Two fibre lemmas (new)

Recall `Fin=(n,x,k,sigma,s)` with `s` in a finite control set, and
`Reg` the rational registers including declared ancillas. Call a
rational ancilla **clean** (relative to a grammar) when its whole
trajectory is determined without reading the registers that grammar
is blind to. Ancilla initial values under COMPLETE scope depend only
on `(n,x,k,sigma)`, hence agree on the states paired below (occupied
equal values may equally be chosen).

**Lemma W (wave-blind fibre form).** Let `W` be any `Gamma_wb`
contact-stage word, of any finite length, any finite `Ctrl`, and any
generator functions allowed by `CONTRACT.md`. Take two complete
states with identical `Fin`, identical `(w,b)`, identical `other`,
and identical clean ancillas, but arbitrary possibly different
`(u,v,A_tape,B_tape)`. Then along `W` the two trajectories have
identical `Fin`, identical `(w,b)`, identical clean ancillas, and
identical increments of every rational register at every step. In
particular the net increments of `v`, `w` and `b` are the same for
both states.

*Proof.* Induction on the word length. A type-(a) generator changes
only `x` by a fixed word, identically for both. In types (b) and (c)
every letter choice, control transition and register increment is a
function of `Fin`, `(w,b)` and clean ancillas only — by the induction
hypothesis these arguments coincide, so the outputs coincide; clean
ancillas stay clean because their increments read no wave data.
`Gamma_wb` has no other generators. ∎

**Lemma S (store-blind fibre form).** Let `W` be any `Gamma_sb` word.
Take two complete states identical in `Fin`, `(u,v,A_tape,B_tape,w)`,
`other` and clean ancillas, differing only in `b`. Then along `W`
all non-`b` components and all register increments, including the
increment of `b` itself, are identical for both states; only the
value of `b` carries its initial difference through.

*Proof.* The same induction, with allowed arguments
`(Fin,u,v,tapes,w, clean ancillas)`, which coincide by hypothesis at
every step because their increments coincide. The `b` increment is
one of those functions, hence is also identical. ∎

Both lemmas quantify over the complete frozen classes: no bound on
word length, control size or the (finite-data) functions is assumed.
`Gamma_fc` is a subclass of both grammars, so every consequence for
`Gamma_wb` or `Gamma_sb` holds a fortiori for `Gamma_fc`.

## 3. Q1: no wave-blind compilation of H_B (new theorem)

**Theorem 1.** No `Gamma_wb` word — and therefore no `Gamma_fc`
word — equals `H_B` at COMPLETE scope, already for the single
instance `B=2/5`.

*Proof.* Use the frozen witnesses of `CONTRACT.md` §5:
`(q,r)=(0,1)`, `a_*=S e_1 != 0`, `e_*=||a_*||^2/2=2/5`, `u=0`, tapes
zero, `w=0`, `b=2/5`, `sigma=+1`, `v=t a_*`. Formula (1) gives
`Delta_+ = t||a_*||^2 + ||a_*||^2/2 = (2t+1)e_*`. Hence:

- `S_0`: `Delta=2/5`, `b-Delta=0 in [0,2/5]`: **accepted**;
  `H_B` sends `v` to `a_*` (increment `a_* != 0`), `w` to `2/5`,
  `b` to `0`, `sigma` to `-1`.
- `S_2`: `Delta=2`, `b-Delta=-8/5 < 0`: **rejected** (shortage);
  `H_B` is the identity, so the `v` increment is `0`.
- `S_{-2}`: `Delta=-6/5`, `b-Delta=8/5 > B`: **rejected**
  (overflow); `v` increment `0`.

`S_0`, `S_2`, `S_{-2}` have identical `Fin` and identical `(w,b)`.
By Lemma W every `Gamma_wb` word gives them the same `v` increment,
while `H_B` gives `a_*` on `S_0` and `0` on the other two — a
contradiction. Both rejection reasons are witnessed. ∎

*Scope remarks.* This is a statement about `H_B`, whose order is
two; the inherited infinite-order obstruction against the unlimited
`C` (#1496 `R_fin`) is vacuous here and is not reused. It is also
strictly wider than the inherited #1496 test that refutes one
fixed-empty-wave pricing rule on `v=a_*`: Theorem 1 covers every
finite-control word whose control and payment never read the exact
occupied wave, with the new occupied witnesses `S_2`, `S_{-2}`. It
does not exclude words outside the frozen contact stage (extra
`U`/`F` ticks), which are a different contract.

## 4. Q2: no store-blind compilation of H_B (new theorem)

**Theorem 2.** No `Gamma_sb` word — and therefore no `Gamma_fc`
word — equals `H_B` at COMPLETE scope, already for `B=2/5`.

*Proof.* Take `S_0` as above with `b=2/5` and the same complete
state with `b=0`. For `b=2/5`, `H_B` accepts and the `v` increment
is `a_* != 0`. For `b=0`, `Delta=2/5` and `b-Delta=-2/5<0`, so
`H_B` rejects and the `v` increment is `0`. The two states differ
only in `b`; by Lemma S every `Gamma_sb` word gives them the same
`v` increment — a contradiction. ∎

Theorems 1 and 2 concern incomparable classes and neither implies
the other. Jointly they prove, within these frozen grammar forms,
that **two distinct exact-read permission kinds are necessary** for
any complete contact-stage compilation of `H_B`: (i) an exact read
of the occupied wave data `(u,v)` (through `Delta_sigma` or any
quantity separating the `S_t` family as `Delta_sigma` does), and
(ii) an exact read/comparison of the bounded store `b` against the
acceptance bounds. Finite native data, however large the finite
controller, cannot substitute for either kind.

## 5. Q3 unresolved: an initialized algebraic recipe, not a typed compilation

Necessity of reading (`K_wave`, `K_cmp`) does not by itself pay.
Inside frozen `Gamma+` the only payment generator, `K_reg`, adds the
ancilla `d` to a register **unconditionally**. The natural recipe
"transfer `Delta` to `d`, compare, then pay `d` into `(w,b)`" fails
even as algebra on rejected states: on `S_2` it would add `Delta=2`
to `w` and move `b` to `2/5-2=-8/5`, outside the carrier
`Q cap [0,B]`, where `H_B` is the identity. The failure of this one
unconditional-payment recipe is not a no-go theorem for `Gamma+`.

### 5.1 Correction: the bounded-store typing defect

`CONTRACT.md` §4 requires every generator to be **a permutation of
the whole extended carrier**. The store is bounded,
`b in Q cap [0,B]`, while the ancilla `d` ranges over all of `Q`.
Any register-addition instance landing in `b` is therefore not even
a self-map of the declared carrier: for `K_reg` with `R=b`, and
likewise for the `K_guard` instance `b -> b-d` at `beta=1` proposed
in an earlier version of this section, the admitted state

```text
B = 2/5, b = 0, d = 1, beta = 1   maps to   b' = -1 notin [0, 2/5].
```

Hence neither instance is a globally admitted primitive under the
frozen contract. This includes an **unresolved typing defect inside
the frozen `Gamma+` definition itself** (its `K_reg` instance on
`b`); `CONTRACT.md` is frozen and is not silently edited here, so
the defect is recorded, not repaired. A separately frozen successor
must type every addition landing in the bounded store. Theorems 1
and 2 are unaffected: their fibre lemmas quantify over the wider
generator forms, and restricting to globally typed permutations only
shrinks those classes, so the no-go conclusions only strengthen.

Merely refusing an out-of-range subtraction (identity instead) does
not repair invertibility: with `B=1`, `d=1/2`, `beta=1`, guarded
subtraction with refusal sends `b=1/2` to `b'=0` (applied) and also
`b=0` to `b'=0` (refused), with all other components fixed — two
complete inputs, one output. A different carrier or a genuinely
reversible payment primitive belongs to a separately frozen
successor and is outside this revision.

INITIALIZED scope does not waive any of this. INITIALIZED restricts
the required *final equality* to an initialized subcarrier with
ancillas restored; the requirement that each primitive itself be a
global permutation of the whole extended carrier is a separate,
independently frozen clause. Correctness of `beta` along the
initialized execution shows safety on that execution path only. The
earlier presentation of the calculation below as a compiled word in
globally admitted primitives ("Theorem 3") is therefore
**withdrawn as a compilation claim**.

### 5.2 Retained statement: initialized algebraic recipe only

Let the label `Gamma++` denote the *proposed* ingredient set
`Gamma+` plus guarded register addition

- (K_guard) if `beta=1` then `R -> R +/- d`, else the identity,
  origin `EXPLICITLY-SUPPLIED-COMPARISON`, outside frozen `Gamma+`,

without any claim that its `b`-instances are globally typed (they
are not, by §5.1). What survives is the following narrower
algebraic fact about executions started at `(d,beta)=(0,0)`:

**Recipe (initialized algebra, not a compilation).** Starting from
ancillas `d=0`, `beta=0`, the following five steps produce exactly
the `H_B` output on the `K_B` components for every `B>=0`, both
`sigma`, and all occupied states, and restore `(d,beta)=(0,0)`
along that execution:

1. `K_wave (+1)`: `d := Delta_sigma(u,v;q,r) =: D`.
2. `K_cmp (b,d)`: `beta := 1[0 <= b-D <= B]`.
3. Guarded apply: the finite-controlled translation
   `v -> v + beta*sigma*a(q,r)` (a function of the finite data
   `(q,r,sigma,beta)`), the flip of `sigma` iff `beta=1` (`sigma`
   is carried as a declared control component, updated by a
   `Fin`-function and exported by projection, as `CONTRACT.md`
   §4(c) permits), together with `K_guard` payments `w -> w+d`,
   `b -> b-d` applied iff `beta=1`. Along this initialized
   execution `beta=1` implies `b-d in [0,B]` by step 2, so the
   executed values stay in range (execution-path safety only, not
   global typing of the step, §5.1); if `beta=0` nothing in this
   step moves.
4. `K_wave (eps)` with `eps=+1` if `beta=1`, else `-1` (selected by
   `Fin`): after step 3 the current difference is `-D` on the
   accepted branch (inherited #1496 reverse identity) and `D` on
   the rejected branch, so `d` becomes `D-D=0` in both cases.
5. `K_cmp (state)`: `beta -> beta xor 1[0 <= b - Delta_current <= B]`.
   On the accepted branch `b - Delta_current = (b-D)+D = b`, which
   lies in `[0,B]`, so `beta` returns to `0`; on the rejected branch
   the flag recomputes to `0` and `beta` stays `0`.

Along an execution started at `(d,beta)=(0,0)` the accepted branch
performs exactly
`(v,w,b,sigma) -> (v+sigma*a, w+D, b-D, -sigma)` with `D=Delta_sigma`,
the rejected branch is the identity, and `n,x,u`, both tapes and `k`
never move; that output is the definition of `H_B`, with ancillas
restored as shown. This checks the five-stage *algebra*; by §5.1 it
does **not** establish a word in globally defined admitted
primitives, at INITIALIZED or COMPLETE scope.

Guarded payment is accordingly only a **proposed sufficient
ingredient for a future separately frozen, completely typed
reversible extension**. Its necessity is not proved, no minimality
of any extension is proved, and no `Gamma+` no-go is proved.

### 5.3 Exact outstanding Q3 obligations

Q3 as frozen (compile or obstruct in `Gamma+`) remains
**unresolved**, for two separate reasons: (i) the frozen `Gamma+`
typing defect for additions into the bounded store `b` (§5.1) must
first be repaired in a separately frozen successor whose every
generator is a permutation of its whole declared carrier; (ii) in
such a completely typed class one must then either compile `H_B`
at a declared COMPLETE or INITIALIZED scope or prove a class
no-go, and any necessity/minimality statement about a guard kind
requires its own proof. Native admission of `H_B` is therefore not
completed in any form by this note.

## 6. Q4: warrant audit

The Canon surfaces audited at the pins in `SOURCES.json` — the
"Native conventions" (generators and `U` on `F_5^6` only), the
`QUADRATIC-MEMORY-NATIVE-CONTACT [O]` contract (which requires an
*independently frozen* alphabet with all data-dependent register
controls and counts clock/program states as resources, for a
different finite `F_5^12 x {0,1}` target), and the CORE summaries
(which keep the `CW-ALG-1` `W` gates and reader couplings as declared
premises and state that no native contact is thereby compiled) —
admit **no** cross-register operation that reads exact rational wave
data, compares exact rational store quantities into native control,
adds rational registers under native control, or writes rational
amplitudes from native data. The supplied noncanonical contracts
supply `eta`, `C_*` and `H_B` as explicit comparison maps, not as
Canon admissions; each says so in its own text. Therefore both kinds
that Theorems 1-2 show necessary (`P-WAVE`, `P-CMP`), register
arithmetic (`P-REG`), and the proposed guarded ingredient of §5
remain **UNSUPPLIED** by Canon, no typed compilation is established
(§5.1), and the native-admission verdict is
`NATIVE_ADMISSION_UNSUPPLIED/STOP`. This is an absence of warrant in
the audited public text, not a theorem that no future native law
could contain such a kind, and it does not decide the owner row.

## 7. Exported interface

```text
carrier: K_B of CONTRACT §1, literal complete-state equality;
  extensions Ctrl (finite), d in Q, beta in {0,1} only where declared
native projection: (n,x) is fixed by H_B and by the initialized
  recipe of §5.2; an arbitrary word in the declared comparison
  grammars can contain x -> g_i(x) and need not fix x.
  Contact-stage words keep n fixed
source family: a(q,r)=S eta(q,r), inherited; five prepared receivers
  are a subfamily, never the compilation domain
admitted primitives, by origin: table in CONTRACT §3
forward map: H_B as target; no replacement proposed
inverse: H_B itself (inherited involution) on the complete K_B
compilation results:
  Gamma_wb / Gamma_sb / Gamma_fc: no COMPLETE word exists (Thm 1, 2);
    these no-gos concern the specified grammars, not every possible
    native contact
  Gamma+ (frozen): Q3 UNRESOLVED; compilation neither shown nor
    excluded; unresolved typing defect for K_reg additions into
    bounded b (§5.1)
  Gamma++ label (proposed ingredients incl. K_guard): initialized
    algebraic recipe from (d,beta)=(0,0) only (§5.2), ancillas
    restored along that execution; NOT a globally typed compilation
clock/program/stage: contact stage only; no U tick (n fixed), no F
  step inside the word; autonomous clock/reset UNSUPPLIED
energy: store b in Q cap [0,B] and ledger w are inherited target
  components; no new budget, finiteness or battery claim is made
signed outputs/records: none produced here; two-cut outputs remain
  the inherited #1489 consequences on the funded forward branch
physical interpretation: NONE (L1 only); no layer bridge passed
required from any future component: first a separately frozen,
  completely typed reversible grammar (every generator a permutation
  of its whole carrier); then in such a class either a compilation
  at declared scope or a no-go, with any guard necessity/minimality
  proved separately; plus an independently warranted admission of
  the exact-read kinds and the inherited schedule/clock obligations
finite rejection witnesses: S_2 (shortage), S_{-2} (overflow)
  against every wave-blind word; S_0 with b=0 against every
  store-blind word, at (q,r)=(0,1), B=2/5, as computed in §§3-4
conservative verdict: CLASS_NO_GO_WITH_SCOPE for Gamma_wb, Gamma_sb
  (hence Gamma_fc) at COMPLETE scope; native admission of H_B
  UNSUPPLIED/STOP; QUADRATIC-MEMORY-NATIVE-CONTACT remains O
```
