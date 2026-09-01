# JIPC WP3G — rekurentní meromorfní pokračování a globální identity — návrh (DRAFT v1)


Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
ŽÁDNÝ PIN, ŽÁDNÝ BĚH**. Skeleton následníka WP3F; nic nezakládá.

```text
LADDER_STEP              = 3 + 4 (pokračování + globální identity)
PARENTS_REQUIRED         = merged veřejné WP3F (N7-EOC, N7-REC, N7-DUP,
                           N7-EPULL, N7-JOIN), WP3E, WP3D
FOURIER_NEEDED           = NE (pokračování i globální identity jsou algebraické)
BASIS_AT_DRAFT           = Public Canon v74 (refreeze při pinu)
```

## 0. Přesný cíl

Na `D = {Re s > 0}` má WP3F pět identit: `Ĉ(s+1) = sĈ(s)/(2p_M)`
(REC-D), `Ĉ(s)Ĉ(s+½) = 2^{3/2-2s}Ĉ(2s)` (DUP-D),
`Ê(s)Ô(s) = Ĉ(s)` (EOC-D), `Ê(s) = 2^{s/2-1}Ĉ(s/2)` (EPULL-D),
`Ô(s) = Ê(s+1)` (JOIN-D) — všechny jako věty na `D`, ne jen na
`Q_{>0}`.

WP3G dokazuje:

1. **MEROMORPHIC_CONTINUATION:** `Ĉ`, `Ê`, `Ô` mají jednoznačné
   meromorfní pokračování na celé `C` s efektivními jmény na každém
   racionálním kompaktním obdélníku v kladné racionální vzdálenosti
   od pólů;
2. **POLES_AND_RESIDUES:** póly `Ĉ` jsou přesně `s = −k`, `k ∈ N_0`,
   jednoduché, s rezidui
   \[
   \operatorname{Res}_{s=-k}\hat C=\frac{2\,(2p_M)^{k}(-1)^{k}}{k!}\neq 0 ;
   \]
   póly `Ê` jsou `s = −2k`, póly `Ô` jsou `s = −2k−1`;
3. **GLOBAL_IDENTITIES:** všech pět identit platí jako identity
   meromorfních funkcí na celém `C`.

Bod 3 je obsahem interní povinnosti `O-SCALAR-SEAM` („globální
meromorfní identita“); jeho případná registrace je samostatné fold
rozhodnutí — Canon nemá JIPC řádky.

## 1. Konstrukce (rekurentní, bez Fouriera)

Pro `N ∈ N` polož na `D_N := {Re s > −N} \ {0,−1,…,−N+1}`

\[
\hat C_N(s):=\frac{(2p_M)^{N}\,\hat C(s+N)}{s(s+1)\cdots(s+N-1)} .
\]

- **Konzistence:** z REC-D na `D` plyne `Ĉ_{N+1} = Ĉ_N` na
  `D_N ∩ D_{N+1}` (jedno použití REC-D v bodě `s+N`); `Ĉ_1 = Ĉ` na
  `D`. Sjednocení definuje meromorfní `Ĉ` na `C`.
- **Hodnoty v celých bodech:** iterací REC-D z `Ĉ(1) = 1/p_M > 0`
  je `Ĉ(m) = 2(2p_M)^{-m}(m−1)! > 0` pro celé `m ≥ 1`; nevymizení
  `Ĉ` v kladných celých bodech je tedy věta (z kladnosti `p_M`),
  nevymizení jinde se netvrdí.
- **Rezidua:** v `s = −k` (`0 ≤ k < N`) je
  `Res = (2p_M)^N Ĉ(N−k) / ∏_{j≠k}(j−k) = (2p_M)^N Ĉ(N−k) /
  [(−1)^k k! (N−k−1)!]`, a dosazením `Ĉ(N−k)` z předchozího bodu
  `Res_{s=−k}Ĉ = 2(2p_M)^k(−1)^k/k!`, nezávisle na `N`; nenulové,
  tedy pól je jednoduchý.
- **Ê a Ô:** z EPULL-D a JOIN-D na `D` je pokračování
  `Ê(s) := 2^{s/2-1}Ĉ(s/2)`, `Ô(s) := Ê(s+1)` legitimní (identity
  jsou věty na celém `D`, ne jen na `Q_{>0}`); póly `s/2 = −k`
  resp. `(s+1)/2 = −k`.
- **Efektivní jména:** na racionálním kompaktním obdélníku
  `K ⊂ D_N` v kladné racionální vzdálenosti `d` od pólů má
  `1/∏(s+j)` racionální horní mez `d^{-N}` a WP3E jméno `Ĉ(s+N)` na
  `K+N`; násobení jménem `(2p_M)^N` (obálka z `p_M`). Žádné nové
  TCB.

## 2. Globální identity

Obě strany každé z pěti identit jsou meromorfní na `C` (složení
pokračování s afinními mapami `s ↦ s+1, s+½, 2s, s/2`) a rovnají se
na `D` (WP3F). Rozdíl je meromorfní na souvislé oblasti
`C \ (diskrétní množina pólů)` a mizí na otevřené podmnožině `D`;
IT-SEGMENT(ii) s řetězem disků přes libovolný bod mimo póly (řetěz
se pólům vyhýbá volbou poloměrů `< min. vzdálenost od pólů`) dává
`≡ 0`. V pólech se rovnost čte jako rovnost reziduí; z REC-D ve
tvaru `Ĉ(s) = (2p_M)Ĉ(s+1)/s` plyne

\[
\operatorname{Res}_{s=-k-1}\hat C
=\frac{2p_M}{-k-1}\operatorname{Res}_{s=-k}\hat C ,
\]

což z `2(2p_M)^k(−1)^k/k!` dává `2(2p_M)^{k+1}(−1)^{k+1}/(k+1)!`
(kontrola `k = 0..3` exaktně). Verifier přehrává tento reziduální
řetěz v okruhu `Q[π̂, π̂^{-1}]`.

## 3. TCB

`COMPLEX_BALL_MELLIN_TCB/v2` (WP3F) beze změny: pokračování je
algebraické (dělení polynomem, afinní kompozice), identity jdou
IT-SEGMENT. Žádný Fourier, Poisson, kruhové `pi`, žádná funkcionální
rovnice, žádné nevymizení mimo celé body.

## 4. Auditní povrch (návrh)

```text
JIPC_WP3G_CONTINUATION_AUDIT 1
ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS
RESIDUE_CHAIN K=0..6 RING=Q[pi,pi^-1] PASS
INTEGER_VALUES M=1..6 RING=Q[pi,pi^-1] PASS
CONSISTENCY_OVERLAP N=1,2 S=1/2+i/2 BITS=2,3 PASS
GLOBAL_IDENTITY_BALLS S=-3/2+i/2 F=5 BITS=2,3 PASS
POLE_AVOIDING_CHAIN S=-3/2+i/2 D=1/2 PASS
PROOF_CONTROLS 12/12 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
```

Rodičovské hashe jsou zámek v textu PREREG (kontroluje reviewer);
verifier žádné soubory nečte a žádnou readback bránu netiskne.
Kontroly (min. 12): mutované reziduum (`k! ↦ (k+1)!`), mutovaný
faktor `(2p_M)^N`, řetěz procházející pólem, obdélník dotýkající se
pólu (`d = 0`), mutovaná konzistence `Ĉ_{N+1} ≠ Ĉ_N`, nárok
nevymizení mimo celé body, nárok funkcionální rovnice, `s` v pólu,
mutovaný pól `Ê` (`−2k ↦ −k`), mutovaná celočíselná hodnota
(`(m−1)! ↦ m!`), mutovaný rozvrh jmen, provenanční stráž `p_M`.

## 5. Ne-nároky a STOP hranice

Nedokazuje se: funkcionální rovnice `s ↔ 1−s` (vyžaduje
Fourier/Poisson, a před nimi identifikaci periody `exp_C` s
`2p_M` — samostatná budoucí proba, navrhované jméno
`P-JIPC-EXP-PERIOD-1`, v této složce nerozepsaná), nevymizení `Ĉ`
mimo celé body (samostatný uzel, potřebný pro logaritmické
derivace), Gamma objekt jménem, kruhové `pi`, archimédovské místo,
L2–L6.

## 6. Podmínky pinu

Po merge veřejného WP3F; collision scan; claim lock s tehdejším
readback tuple; TCB beze změny; verifier nikdy nespouštěný do pinu;
preflight; `EXPECTED.txt` jediný stdout artefakt.
