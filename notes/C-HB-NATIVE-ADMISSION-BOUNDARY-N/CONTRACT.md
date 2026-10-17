# Contract: compilation classes for the frozen funded contact H_B

**NON-CANONICAL / L1 / analytical. This contract grants no native
authority.** Candidate `C-HB-NATIVE-ADMISSION-BOUNDARY-N`, lane
[#1498](https://github.com/mathorn1973/twist-j/issues/1498). Immutable
sources, blobs and hashes are in `SOURCES.json`. A. M. Thorn,
Apache-2.0.

## 1. The target (supplied premise, read only)

The target is exactly the map `H_B` of the #1496 contract at
`b7636a334b09fcc68422bcd6cc6e15334d416c59`, unchanged. At one contact
instant the complete carrier is

```text
K_B = (n, x, u, v, A_tape, B_tape, k, w, b, sigma, other)
n in N_0, x=(a,b,c,d,q,r) in F_5^6, u,v in Q^D,
A_tape,B_tape: the two inherited Q^4-valued two-slot tapes,
k in {0,1}, w in Q, b in Q cap [0,B], sigma in {+1,-1}, B >= 0 fixed.
```

`D`, `L`, `E_D`, `E_full`, `S` and `ell` are the inherited classical
objects (#1485, #1489). With `a(q,r) = S eta(q,r)`,
`H = 2I - L`, and the inherited difference

```text
Delta_sigma(u,v;q,r) = E_D(u, v + sigma*a(q,r)) - E_D(u,v)
                     = sigma <v - Hu/2, a(q,r)> + ||a(q,r)||^2/2,   (1)
```

`H_B` accepts iff `0 <= b - Delta_sigma <= B`, and then sends
`(v,w,b,sigma)` to
`(v + sigma*a(q,r), w + Delta_sigma, b - Delta_sigma, -sigma)`;
otherwise it is the identity on the complete state. All other
components are fixed. Equality is literal equality of the complete
state; no coordinate is quotiented, normalized or discarded. That
`H_B` is an involution preserving `E_full + b`, `E_full - w` and
`b + w` is an inherited #1496 theorem, used as a premise. `H_B` is
not a native letter, not a battery, and not a global inverse of `U`.
No replacement target, threshold or budget is proposed here.

## 2. Frozen native alphabet (audit object of Q0)

On `x=(a,b,c,d,q,r) in F_5^6` (all operations mod 5), the #1489 formulas,
to be compared literally in `PROOF.md` against the Canon v101 "Native
conventions" formulas `(g_a,g_b,g_c,g_d,g_e) = (g_0,...,g_4)`, are:

```text
g0(a,b,c,d,q,r) = (b,a,d,c,q,r)
g1(a,b,c,d,q,r) = (-c,-d,-a,-b,-q,-r)
g2(a,b,c,d,q,r) = (2-c, 1+r-d, 2-a, 1-r-b, 1-q, -r)
g3(a,b,c,d,q,r) = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
g4(a,b,c,d,q,r) = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
z6(x) = a+b+c+d+q+r,
z6 o (g0,g1,g2,g3,g4) = (z6, -z6, 2-z6, 2-z6, 3-z6).
```

Each `g_i(x) = M_i x + c_i` is affine; `g_0,g_1` are linear in these
coordinates and `g_2,g_3,g_4` have nonzero shifts, so `g_i(0) != 0` for
some `i` is not a contradiction. The native update is the
selector-defined `U(n,x) = (n+1, g_{z6(x)+2*theta_n mod 5}(x))` with
`theta_n = popcount(n) mod 2`. A freely chosen generator word, one
state-selected `U` step, and a compiler gate reading current `(q,r)`
are three different admissibility levels and are never identified in
this note. A generator involution is not an inverse of `U`.

## 3. Permission table (origins, frozen)

| # | Permission | Origin |
|---|---|---|
| P-U | Original selector update `U` on `N_0 x F_5^6` | `CANON-ADMITTED` (Canon native conventions) |
| P-G | Fixed words in `g_0..g_4` as maps of the `F_5^6` factor | `CANON-ADMITTED` as defined maps; Canon also defines word compositions `N_w`. This does not make a free word an autonomous `U` run |
| P-F | Inherited classical step `F` on its own factor | `EXPLICITLY-SUPPLIED-COMPARISON` (#1485/#1489 noncanonical contracts) |
| P-ETA | Lift `eta(q,r) in (1/2)Z^4`, insertion `S eta in Q^D` | `EXPLICITLY-SUPPLIED-COMPARISON` (#1489). Not an `F_5`-additive homomorphism; interface debt |
| P-HB | Carrier extension `(b,sigma)`, law `H_B`, formula (1) | `EXPLICITLY-SUPPLIED-COMPARISON` (#1496 target premise) |
| P-CTRL | Finite controller/stage states inside a contact word | `EXPLICITLY-SUPPLIED-COMPARISON` (grammar of §4; #1489 supplies only its external schedule) |
| P-FC | Finite-controlled rational translations (§4) | `EXPLICITLY-SUPPLIED-COMPARISON` (this contract's grammar) |
| P-WAVE | Exact read of occupied `(u,v)` through `Delta_sigma` into control or payment | `EXPLICITLY-SUPPLIED-COMPARISON` in `Gamma+`/`Gamma_sb` only; **not Canon-admitted** (Q4 audits this) |
| P-CMP | Exact order comparison of rational store quantities into a control bit | `EXPLICITLY-SUPPLIED-COMPARISON` in `Gamma+` only; **not Canon-admitted** |
| P-REG | Exact rational register-to-register addition | `EXPLICITLY-SUPPLIED-COMPARISON` in `Gamma+` only; **not Canon-admitted** |
| P-CLK | Autonomous reusable clock, reset, physical timing/addressing | `UNSUPPLIED` |
| P-PHYS | Physical contact, SI work, entropy, occurrence, Born law | `UNSUPPLIED`, outside L1 here |

A note cannot grant itself native authority: every
`EXPLICITLY-SUPPLIED-COMPARISON` kind is an analytical comparison
grammar, never evidence that Canon admits the operation natively.

## 4. Frozen primitive grammars

Split the complete state into **finite data**
`Fin = (n, x, k, sigma, s)`, where `s` ranges over a finite control
set `Ctrl` declared by the candidate word (an extension of `K_B`),
and **rational data** `Reg = (u, v, A_tape, B_tape, w, b)` together
with any declared rational ancillas. `other` is fixed by every
generator below. A **contact-stage word** is a finite composition of
the generators of one grammar, applied at the inherited contact stage:
no `U` tick (which would increase `n`, while `H_B` fixes `n`) and no
classical `F` step (a different stage of the inherited schedule) may
occur inside the word. Compilers using extra ticks or stage changes
are a different contract and are outside Q1-Q3.

Compilation equality has two strictly separate scopes:

- **COMPLETE:** the word, as a map on `K_B x Ctrl x Anc`, equals
  `H_B` on the `K_B` components and the identity on `(s, Anc)` return
  values specified by the candidate, for **all** occupied auxiliary
  values, with initialization of `(s, Anc)` — if used at all —
  depending only on the finite data `(n,x,k,sigma)`.
- **INITIALIZED:** the same equality only on the subcarrier where
  declared ancillas start at declared constant initial values and
  are restored to them at the end. An INITIALIZED result must never
  be reported as COMPLETE.

### Grammar Gamma_fc (finite-control coupling)

Generators, each a permutation of the extended carrier:

- (a) **fixed native word:** `x -> W x` for one fixed word `W` in
  `g_0..g_4`; all else fixed.
- (b) **finite-controlled native letter:** `x -> g_{j(Fin)}(x)`,
  `s -> s'(Fin)` for arbitrary functions `j, s'` of the finite data
  only; `Reg` fixed.
- (c) **finite-controlled rational translation:** each rational
  register `R in Reg` (including tapes) goes to `R + C_R(Fin)`, and
  `s -> s'(Fin)`, for arbitrary functions of the finite data only;
  `(n,x,k,sigma)` fixed except through `s` (a `sigma` flip encoded in
  `s` is allowed only if the candidate declares that encoding; the
  exported `sigma` output must then be read from the final finite
  state by a fixed finite decoding).

Crucially, in `Gamma_fc` no increment, control transition or letter
choice may depend on any exact rational value in `Reg`.

### Grammars Gamma_wb and Gamma_sb (one-sided blindness)

`Gamma_wb` ("wave-blind") is defined like `Gamma_fc`, except the
functions in (b) and (c) may depend on `Fin` and on the exact values
`(w,b)`, but never on `(u, v, A_tape, B_tape)` or rational ancillas
fed from them. `Gamma_sb` ("store-blind") is defined likewise with
dependence allowed on `Fin` and `(u, v, A_tape, B_tape, w)`, but never
on `b`. In both grammars rational increments are added to registers;
a register value may influence a later increment only through the
declared dependence of that generator. `Gamma_fc` is contained in
both forms. These two grammars are incomparable and are frozen as
separate complete classes for Q1 and Q2.

### Grammar Gamma+ (declared exact-arithmetic extension)

`Gamma+` is `Gamma_fc` plus three explicitly supplied generator kinds
acting on one declared rational ancilla `d in Q` and one control bit
`beta in {0,1}` inside `Ctrl`:

- (K_wave) **exact difference transfer:**
  `d -> d + eps * Delta_sigma(u,v;q,r)` with `eps in {+1,-1}`
  selected by `Fin` (including `beta`); all else fixed.
- (K_cmp) **exact bounded comparison:**
  `beta -> beta xor 1[0 <= b - d <= B]`, or
  `beta -> beta xor 1[0 <= b - Delta_sigma(u,v;q,r) <= B]`;
  all else fixed.
- (K_reg) **register addition:** `R -> R +/- d` for one declared
  rational register `R`; all else fixed.

`Gamma+` is used only at INITIALIZED scope (Q3) with declared
ancilla initialization `d = 0`, `beta = 0`, unless `PROOF.md`
explicitly proves a stronger scope. Adding `H_B` itself, or any
generator defined by its accepted/rejected output table, as a
primitive is forbidden in every grammar above.

## 5. Frozen differentiating witnesses

Fix finite data `n = 1`, `x = (0,0,0,0,0,1)` so `(q,r) = (0,1)`,
`k = 0`, `sigma = +1`, and rational data `u = 0`, both tapes zero,
`w = 0`, `B = 2/5`. Write `a_* = a(0,1) = S e_1 != 0` and
`e_* = ||a_*||^2/2 = 2/5` (inherited #1496 values). For `t in Q` let
`S_t` be this complete state with `v = t a_*` and `b = 2/5`; by (1)
at `u = 0`, `Delta_+(S_t) = (2t+1) e_*` (inherited formula).
Frozen test states: `S_0` (empty wave), `S_2` (occupied wave,
shortage side), `S_{-2}` (occupied wave, overflow side), and the
store pair `S_0` with `b = 2/5` versus `b = 0`. These states, not
the five prepared receiver rows, are the differentiating tests for
Q1 and Q2; their `H_B` actions are derived in `PROOF.md` from (1).

## 6. Success, failure and exclusions

Q1/Q2 are decided positively only by an explicit word with COMPLETE
equality on `K_B` for every `B >= 0` instance of the target family
(the word may be given uniformly in `B`), both directions, arbitrary
occupied `(u,v, tapes, w, b)`, both rejection reasons, and
`sigma in {+1,-1}`. They are decided negatively only by a proof
covering every word of the respective frozen grammar. Q3 is decided
only at its declared INITIALIZED scope. The final verdicts allowed
are those of `PREREG.md`, each with its exact scope. This note does
not claim the owner rows `QUADRATIC-MEMORY-NATIVE-CONTACT` or
`QDD-INSTRUMENT-APPARATUS`, does not reopen funding, budgets,
cardinalities, the 5/25 census or any finite audit, and asserts no
physical, probabilistic or cross-layer statement.
