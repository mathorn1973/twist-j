# Plán formalizace v Lean 4: binární směrování a NB posloupnostní kritérium

```text
STATUS      NON-CANONICAL. Plán, ne kód. Žádný Lean soubor v tomto adresáři
            nebyl přeložen; v revizním sezení nebyl dostupný Lean toolchain
            (síť blokována). Identifikátory Mathlibu níže byly ověřeny
            čtením zdrojů pinovaného Mathlibu, pokud není řečeno jinak.
ENV         notes/lean-j-cyclotomic: leanprover/lean4:v4.30.0,
            Mathlib c5ea00351c28e24afc9f0f84379aa41082b1188f
DATE        2026-09-10
```

## 0. Zásady

- Formalizace patří do laboratoře `notes/lean-j-cyclotomic` jako nový
  modul, například `TwistJ/RHBinary/`. Podle README té laboratoře ruční
  build nevytváří žádný status; repozitářová CI Lean nestaví.
- Bagchiho věta (RH $\Rightarrow\mathbf1\in V$) v Mathlibu není a nesmí být
  přidána jako `axiom`. Každé tvrzení, které ji potřebuje, ji nese jako
  explicitní hypotézu `(hBagchi : RiemannHypothesis → one_mem_closure)`.
  Elementární směr ($\mathbf1\in V\Rightarrow$ RH) je formalizovatelný, ale
  patří až do fáze 3.
- RH je v Mathlibu definována jako `RiemannHypothesis : Prop`
  (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`):
  `∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2`.
- Postupovat od tvrzení bez analýzy k tvrzením s analýzou; každou fázi
  uzavřít `#print axioms` jako v `Audit.lean`.

## Fáze 1: celočíselné identity (bez Mathlib analýzy, jen `Nat`)

| # | Tvrzení | Lean náčrt | Opěrné lemma |
|---|---------|------------|--------------|
| 1.1 | $r_{mk}(n)=m\,r_k(\lfloor n/m\rfloor)+r_m(n)$ | `theorem rem_dilate (m k n : ℕ) (hm : 0 < m) : n % (m*k) = m * ((n / m) % k) + n % m` | `Nat.div_add_mod`, `Nat.mod_mod_of_dvd` (core), kandidát `Nat.mod_mul_right_div_self` (neověřeno v pinu) |
| 1.2 | popcount jako pevný bod: $f(n)=n\bmod2+f(\lfloor n/2\rfloor)$ | `(Nat.digits 2 n).sum` a `Nat.digits_add_two_add_one` / `Nat.digits_def'` | `Mathlib/Data/Nat/Digits/Defs.lean` (ověřeno) |
| 1.3 | $f_J(n)=[2^J\nmid n]$ pro iteraci $f_{J+1}=r_2+Cf_J$ | `def fJ : ℕ → ℕ → ℕ` rekurzí podle $J$; `theorem fJ_eq (J n : ℕ) (hn : 0 < n) : fJ J n = if 2^J ∣ n then 0 else 1` indukcí podle $J$ s `Nat.mod_two_eq_zero_or_one` | core `Nat.mod_two_eq_zero_or_one`, `Nat.dvd_iff_mod_eq_zero` (ověřeno) |
| 1.4 | $\Delta r_k(n)=1-k[k\mid n]$ (v `ℤ`) | `theorem delta_rem (k n : ℕ) (hk : 0 < k) : ((n+1) % k : ℤ) - (n % k : ℤ) = 1 - k * (if k ∣ n+1 then 1 else 0)` | `Nat.add_mod`, případová analýza `n % k = k-1` |
| 1.5 | rovnost rozdílů na stejné $S$-části (Věta 3.4) pro konečné kombinace | `Finset.sum` přes moduly, koeficienty v `ℚ`; z 1.4 | `Finset.sum_congr` |
| 1.6 | konečná překážka §4: $\mathbf1_{2\ (4)}\notin E$ | `theorem y_not_finite_comb (F : Finset ℕ) (hF : ∀ k ∈ F, 2 ≤ k) (c : ℕ → ℚ) : ¬ ∀ n, (if n % 4 = 2 then 1 else 0 : ℚ) = ∑ k ∈ F, c k * (n % k)`; dosadit $n=1$ a pak $n=L-2,L-1$ s $L=4\prod F$ | 1.4 a `Finset.prod` dělitelnost |
| 1.7 | $f(1)+f(q-1)-f(q)=0$ pro $S$-hladké moduly (dyadický případ $q=3$) | speciální případ 1.5 | |

Fáze 1 nepotřebuje reálná čísla ani limity a je vhodná jako první
`lake build` cíl. Odhad rozsahu: několik set řádků.

## Fáze 2: racionální formule periodické normy (§6 sondy)

Cíl: pro `q : Fin L → ℚ` a periodické rozšíření definovat
`blockSum j = ∑ n ∈ Finset.Ico (2^j) (2^(j+1)), q (n % L)` a dokázat

- 2.1 $A(M)=M\bar q+\eta(M\bmod L)$ (konečná identita, `Finset.sum_range` a
  dělení se zbytkem);
- 2.2 eventuální periodicita $b_j=2^j\bmod L$: existují $h,t$ s
  $b_{j+t}=b_j$ pro $j\ge h$ (holubník na `ZMod L`; `Nat.pow_mod`);
- 2.3 součet řady $\sum_j4^{-j}\,\text{blockSum}\,j$ v `ℝ` (nebo `ℚ` s
  `HasSum` v `ℝ`) se rovná uzavřené formuli; potřebné:
  `hasSum_geometric_of_lt_one`, `tsum_geometric_of_lt_one`
  (`Mathlib/Analysis/SpecificLimits/Basic.lean`, ověřeno), rozdělení řady
  na předperiodu a cyklus (`HasSum.add`, `hasSum_nat_add_iff`, sumace po
  třídách mod $t$ přes `Nat.divModEquiv` nebo `tsum_eq_tsum_of_ne_zero`).

Výstup fáze 2: `theorem binarySum_periodic_eq (q : Fin L → ℚ) : HasSum (fun j => (4:ℝ)⁻¹^j * blockSum q j) (closedForm q)`.
Z toho plynou přesné hodnoty $\|\mathbf1\|_B^2=2$, $\|a_j\|_B^2=3/(2\cdot4^j)$,
$\|\mathbf1-f_J\|_B^2=2/4^J$ a Gramova tabulka §7 jako `decide`/`norm_num`
instance na konkrétních `L`.

## Fáze 3: Hilbertův prostor a operátory

- 3.1 Prostor $H$: `MeasureTheory.Lp ℝ 2 μ` s `μ = Measure.sum (fun n => w n • Measure.dirac n)` na `ℕ`, nebo `lp` s váženým měřením; obě normy jako ekvivalentní.
- 3.2 $C$ a $D_2$ jako spojité lineární operátory (`ContinuousLinearMap`) s
  přesnými normami $\tfrac12$ a $2^{-1/2}$ v binární normě (fáze 2 dává
  identity na konečně nosných vektorech, hustota je dokončí).
- 3.3 Lemma 3.1 revize: `one_mem_closure → closure = ⊤` přes
  `Submodule.span`, `Submodule.topologicalClosure` a hustotu konečně nosných
  posloupností.
- 3.4 Lemma 3.5 revize: ekvivalence invariancí, čistě algebraicky z 3.3.
- 3.5 Elementární směr kritéria: $\lambda_\rho$ jako omezený funkcionál
  pro $\Re\rho>1/2$; potřebuje `riemannZeta`, sumaci
  $\sum_n r_k(n)(n^{-s}-(n+1)^{-s})$ a identitu
  $\Pi(r_k)(s)=\zeta(s)(1-k^{1-s})/s$ na $\Re s>1$ (`LSeries`,
  `LSeriesSummable_zeta_iff` v `Mathlib/NumberTheory/LSeries/Dirichlet.lean`,
  ověřeno) a analytické pokračování (`AnalyticOnNhd` + identita).
  To je nejtěžší část fáze 3.

## Fáze 4: co v Mathlibu chybí

- Bagchiho věta a Nyman–Beurling–Báez-Duarte kritérium: nejsou. Zůstávají
  hypotézou.
- Věta 3.6 (Hurwitzovo čtení vrstev): Mathlib má
  `hurwitzZeta (a : UnitAddCircle) (s : ℂ)`, `differentiableAt_hurwitzZeta`
  (v $s$), `hasSum_hurwitzZeta_of_one_lt_re`, `hurwitzZeta_residue_one`
  (`Mathlib/NumberTheory/LSeries/HurwitzZeta.lean`, ověřeno). Koeficientová
  část věty (Abelova sumace a identita Dirichletových řad pro $\Re s>1$) je
  formalizovatelná; **analytičnost $a\mapsto\zeta(s,a)$ v parametru** a
  identita nul v Mathlibu není, takže důsledek „nekonečně mnoho vrstev
  $\Rightarrow$ RH“ zatím formalizovat nelze bez nové teorie.
- $\beta(s)=L(s,\chi_4)$: `DirichletCharacter.LFunction` a
  `LFunction_eq_LSeries` existují
  (`Mathlib/NumberTheory/LSeries/DirichletContinuation.lean`, ověřeno);
  identita §5 sondy pro $\Re s>1$ je formalizovatelná.

## Pořadí prací a co se tím získá

1. Fáze 1 celá (jediný `lake build` cíl, `#print axioms` bez `sorry`).
2. Fáze 2 včetně konkrétních hodnot tabulky §7 pro $K\le4$.
3. Fáze 3.1–3.4.
4. Fáze 3.5 a koeficientová část 3.6.

Po kroku 2 je formálně ověřeno vše, co sonda počítá; po kroku 4 vše, co
sonda dokazuje, s výjimkou importu [1] a analytičnosti Hurwitzovy zety
v parametru. Žádný krok nemění status RH; Lean důkaz elementárních identit
není evidence o RH a podle README laboratoře nesmí být takto citován.
