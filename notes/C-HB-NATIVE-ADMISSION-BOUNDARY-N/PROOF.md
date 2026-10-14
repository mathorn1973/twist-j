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

## 5. Q3: the payment must also be guarded (new construction and gap)

Necessity of reading (`K_wave`, `K_cmp`) does not by itself pay.
Inside frozen `Gamma+` the only payment generator, `K_reg`, adds the
ancilla `d` to a register **unconditionally**. The natural word
"transfer `Delta` to `d`, compare, then pay `d` into `(w,b)`" therefore
fails on rejected states: on `S_2` it would add `Delta=2` to `w` and
move `b` to `2/5-2=-8/5`, outside the carrier `Q cap [0,B]`, where
`H_B` is the identity. Whether some other `Gamma+` word simulates a
guarded payment through its comparison/receiver channels is **not
decided here**; no insufficiency theorem for `Gamma+` is claimed.

What is shown is that exactly one further declared kind closes the
construction. Let `Gamma++` be `Gamma+` plus the single kind

- (K_guard) **guarded register addition:** if `beta=1` then
  `R -> R +/- d` for one declared rational register `R`, else the
  identity; all else fixed. Origin:
  `EXPLICITLY-SUPPLIED-COMPARISON`, outside the frozen `Gamma+`.

**Theorem 3 (initialized sufficiency in `Gamma++`).** With ancillas
`d=0`, `beta=0` initially, the following word equals `H_B` on the
`K_B` components for every `B>=0`, both `sigma`, and all occupied
states, and restores `(d,beta)=(0,0)`:

1. `K_wave (+1)`: `d := Delta_sigma(u,v;q,r) =: D`.
2. `K_cmp (b,d)`: `beta := 1[0 <= b-D <= B]`.
3. Guarded apply: the finite-controlled translation
   `v -> v + beta*sigma*a(q,r)` (a function of the finite data
   `(q,r,sigma,beta)`), the flip of `sigma` iff `beta=1` (`sigma`
   is carried as a declared control component, updated by a
   `Fin`-function and exported by projection, as `CONTRACT.md`
   §4(c) permits), together with `K_guard` payments `w -> w+d`,
   `b -> b-d` applied iff `beta=1`. If `beta=1` then
   `b-d in [0,B]` by step 2, so the carrier is preserved; if
   `beta=0` nothing in this step moves.
4. `K_wave (eps)` with `eps=+1` if `beta=1`, else `-1` (selected by
   `Fin`): after step 3 the current difference is `-D` on the
   accepted branch (inherited #1496 reverse identity) and `D` on
   the rejected branch, so `d` becomes `D-D=0` in both cases.
5. `K_cmp (state)`: `beta -> beta xor 1[0 <= b - Delta_current <= B]`.
   On the accepted branch `b - Delta_current = (b-D)+D = b`, which
   lies in `[0,B]`, so `beta` returns to `0`; on the rejected branch
   the flag recomputes to `0` and `beta` stays `0`.

The accepted branch performs exactly
`(v,w,b,sigma) -> (v+sigma*a, w+D, b-D, -sigma)` with `D=Delta_sigma`,
the rejected branch is the identity, and `n,x,u`, both tapes and `k`
never move; that is the definition of `H_B`. ∎

Theorem 3 is an **INITIALIZED** result in an explicitly extended
comparison grammar. It is not a COMPLETE equality for occupied
ancillas, it does not decide Q3 inside frozen `Gamma+`, and none of
its kinds is thereby admitted natively. Its precise content is: the
missing permission, beyond exact wave read and exact store
comparison, is one guarded exact payment kind; with it, a five-step
initialized compilation exists.

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
Canon admissions; each says so in its own text. Therefore every kind
that Theorems 1-3 show necessary or sufficient —
`P-WAVE`, `P-CMP`, `P-REG`, `K_guard` — remains **UNSUPPLIED** by
Canon, and the native-admission verdict is
`NATIVE_ADMISSION_UNSUPPLIED/STOP`. This is an absence of warrant in
the audited public text, not a theorem that no future native law
could contain such a kind, and it does not decide the owner row.

## 7. Exported interface

```text
carrier: K_B of CONTRACT §1, literal complete-state equality;
  extensions Ctrl (finite), d in Q, beta in {0,1} only where declared
native projection: (n,x) fixed by H_B and by every word considered
source family: a(q,r)=S eta(q,r), inherited; five prepared receivers
  are a subfamily, never the compilation domain
admitted primitives, by origin: table in CONTRACT §3
forward map: H_B as target; no replacement proposed
inverse: H_B itself (inherited involution) on the complete K_B
compilation results:
  Gamma_wb / Gamma_sb / Gamma_fc: no COMPLETE word exists (Thm 1, 2)
  Gamma+: compilation NOT SHOWN and NOT excluded (open simulation
    question for guarded payment)
  Gamma++ = Gamma+ + K_guard: explicit INITIALIZED word exists
    (Thm 3), ancillas (d,beta) initialized and restored to (0,0)
clock/program/stage: contact stage only; no U tick (n fixed), no F
  step inside the word; autonomous clock/reset UNSUPPLIED
energy: store b in Q cap [0,B] and ledger w are inherited target
  components; no new budget, finiteness or battery claim is made
signed outputs/records: none produced here; two-cut outputs remain
  the inherited #1489 consequences on the funded forward branch
physical interpretation: NONE (L1 only); no layer bridge passed
required from any future component: an independently warranted
  admission of exact wave read, exact store comparison and guarded
  exact payment, at COMPLETE occupied-ancilla scope, or a proof
  that Gamma+ (or another independently admitted class) simulates
  the guard; plus the inherited schedule/clock obligations
finite rejection witnesses: S_2 (shortage), S_{-2} (overflow)
  against every wave-blind word; S_0 with b=0 against every
  store-blind word, at (q,r)=(0,1), B=2/5, as computed in §§3-4
conservative verdict: CLASS_NO_GO_WITH_SCOPE for Gamma_wb, Gamma_sb
  (hence Gamma_fc) at COMPLETE scope; native admission of H_B
  UNSUPPLIED/STOP; QUADRATIC-MEMORY-NATIVE-CONTACT remains O
```
