# JIPC WP3F — zvednutí racionálního řezu na Re(s)>0 — návrh preregistrace (DRAFT v3)


Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
ŽÁDNÝ PIN, ŽÁDNÝ BĚH / PUBLIC-PIN-READY: NO**.

Verze 3 nahrazuje v2 po přechodu Public Canon na v74. Změny proti v2:
jediné zvedací lemma `LIFT_QPOS_TO_D` aplikované na pět identit
(EOC, REC, DUP, E-PULL, JOIN), WP3D jako veřejný merged-probe rodič
místo privátní premisy, jednoznačnosti pojmenované třídou a
ekvivalencí (POLICY §4 reading-family), transkriptové a preflight
závazky verifieru, a zmrazená půlceločíselná tabulka `Ĉ(k/2)`.

```text
HOLOMORPHIC_ROUTE        = PASS_CONDITIONAL
REGIME                   = A_SELECTED
PRIVATE_ROUTE_B          = CLOSED
PUBLIC_WP3D_PARENT       = MISSING (draft only; PR #572 nese v72 verzi,
                           v74 balík je na notes větvi tohoto PR)
WRITTEN_CONTRACT         = v3 IN NOTES
PUBLIC_PIN_READY         = BLOCKED
BASIS_AT_DRAFT           = Public Canon v74 (refreeze při pinu)
```

Tento dokument zůstává návrhem. Nevytváří claim, pin, veřejnou
premisu ani oprávnění k běhu.


## 0.0 REŽIM — rozhodnuto (cesta A)

1. nejdřív vznikne a bude sloučena veřejná proba
   `P-JIPC-WP3D-QPOS-MELLIN-1` (draft
   `WP3D_QPOS_PUBLIC_PREREG_DRAFT_v1.md` v této složce; připravený
   claim-lock text `CLAIM_LOCK_DRAFT_P-JIPC-WP3D-QPOS-MELLIN-1.md`);
2. teprve potom může vzniknout veřejná WP3F proba s plným
   `candidate-T` stropem.

Cesta B je **CLOSED / NOT SELECTED**.

## 0. Přesný cíl — pět identit, jedno lemma

Pro oblečená Mellinova semena WP3E (`E=(2,1,0,1)`, `O=(2,1,1,1)`,
`C=(4,2,0,2)`, váha `p_M`) na `D := {Re s > 0}`:

\[
\boxed{\hat E(s)\,\hat O(s)=\hat C(s)}
\tag{EOC-D}
\]

\[
\boxed{\hat C(s+1)=\frac{s}{2p_M}\,\hat C(s)}
\tag{REC-D}
\]

\[
\boxed{\hat C(s)\,\hat C(s+\tfrac12)=2^{\,3/2-2s}\,\hat C(2s)}
\tag{DUP-D}
\]

\[
\boxed{\hat E(s)=2^{\,s/2-1}\,\hat C(s/2)}
\tag{EPULL-D}
\]

\[
\boxed{\hat O(s)=\hat E(s+1)}
\tag{JOIN-D}
\]

Všech pět má na `Q_{>0}` exaktní svědky z veřejného WP3D (N3) a na
`D` se zvedají **jedním** lemmatem:

\[
\boxed{\text{LIFT\_QPOS\_TO\_D:}\quad
f\ \text{holomorfní na } D \text{ s efektivním jménem na každém
racionálním kompaktním obdélníku},\ f|_{\mathbb Q_{>0}}=0
\ \Longrightarrow\ f\equiv 0 \text{ na } D.}
\]

Koncovým uzlem zůstává `JIPC_WP3F_EOC_HOLOMORPHIC`; ostatní čtyři jsou
pojmenované koprodukty téhož grafu. Poznámka (žádný nový nárok):
(EOC-D) je přesně (DUP-D) v bodě `p = s/2` dosazená do (EPULL-D) a
(JOIN-D), protože `2^{s/2-1}·2^{(s-1)/2}·2^{3/2-s} = 1`. Verifier
přesto přehrává všech pět zvlášť — každá má vlastní jméno a stráž —
a WP3G potřebuje EPULL-D a JOIN-D jako samostatné věty na `D`.

### 0.1 Ne-nároky a reading-family

Nedokazuje se: meromorfní pokračování (WP3G), funkcionální rovnice,
Fourier/Poisson, Gamma objekt, kruhové `pi`, archimédovské místo,
nevymizení `Ĉ` na `D`, globální WP2 šev, L2–L6 lift; SAMPLING NOT
PROVIDED. Jména `STANDARD_PI_IDENTIFICATION`,
`CIRCLE_PI_IDENTIFICATION`, `MELLIN_SEEDS` atd. patří privátní JIPC
linii; Public Canon v74 žádnou takovou bránu ani řádek nenese a
žádná se nevytváří.

**Reading-family discipline (POLICY §4): NOT_APPLICABLE.** Tento
draft nenavrhuje žádnou rodinu fyzikálních čtení, dekodér, selekci
ani occurrence klauzuli. Jediné nároky jednoznačnosti jsou
matematické a pojmenovávají třídu i ekvivalenci:

1. *kladný `n`-tý kořen*: třída `{y ∈ R_{>0} : y^n = x}` pro dané
   `x > 0`; ekvivalence = rovnost v `R`; jednoznačnost z ryzí
   monotonie `y ↦ y^n` (POW-EXPLOG-ID);
2. *společný bod Machinových intervalů*: třída reálných čísel
   ležících v každém `hull(S_{q,N}, S_{q,N+1})`; ekvivalence = rovnost
   v `R`; jednoznačnost ze zmenšující se mezery — vlastní ji veřejný
   WP3D (Q7 krok 0), zde jen citováno.

## §1. TCB: `COMPLEX_BALL_MELLIN_TCB/v2`

Dědí se celý `COMPLEX_BALL_MELLIN_TCB/v1` z WP3E (exaktní `Q`
aritmetika, intervaly a komplexní boxy s vnějším zaokrouhlením,
`exp_R`/`exp_C` řadou s explicitním ocasem, `log_R`, kompaktní
Riemannova integrace + FTC, `C¹` substituce, midpoint lemma,
Cauchy-limitní jednoznačnost a lepení, holomorfnost lokálně
stejnoměrné limity, archimédovská kofinalita). Přírůstky (dva):

**IT-SEGMENT (registrované pravidlo):** nechť `r ∈ R_{>0}`, `c ∈ C`
a `B(c,r) ⊆ D` je otevřený eukleidovský disk (nikoli obdélníková
complex-ball reprezentace evaluátoru WP3E).
(i) Je-li `c ∈ R` a `f = 0` na reálném průměru `{c+x : x ∈ (−r,r)}`,
pak `f = 0` na `B(c,r)`.
(ii) Pro libovolné `c ∈ C`: je-li `f = 0` na neprázdné otevřené
podmnožině `B(c,r)`, pak `f = 0` na `B(c,r)`.
Racionalita středu ani poloměru se nevyžaduje. Vnitřní
Taylorův/Cauchyho důkaz je součástí registrace; žádná Cauchyho
normalizační konstanta nevstupuje do tvrzení ani do výpočtu.

**POW-EXPLOG-ID (drobné registrované rozhraní):** jednoznačnost
kladného `n`-tého kořene ve třídě a ekvivalenci §0.1(1). Nic
dalšího; žádný POW_RAT kalkul se nepřenáší.

Jména konstant použitá v N4 jsou přesně tři: `1/(2p_M)` (racionální
obálka z WP3E `3 < p_M < 16/5`, tedy `5/32 < 1/(2p_M) < 1/6`),
`2^{3/2-2s}` a `2^{s/2-1}`, obě realizované jako
`exp_C((3/2-2s)·log_R 2)` resp. `exp_C((s/2-1)·log_R 2)` — `log_R`
a `exp_C` řadou jsou /v1 položky. Každé z nich je **jméno s vlastní
chybou** vyhodnocované na téže přesnosti `m` jako rodičovské
aproximanty (viz N4); žádné se nepovažuje za exaktní konstantu.

## §2. Důkazový graf

### N0 — LIFT_QPOS_TO_D (lemma, dokazováno jednou)

Nechť `f` je holomorfní na `D` s efektivním jménem na každém
racionálním kompaktním obdélníku a `f(s) = 0` pro všechna
`s ∈ Q_{>0}`. Pak `f ≡ 0` na `D`. Důkaz = N5 (paprsek) + N6 (řetěz
disků) níže, formulované pro obecné `f`; N4 dodává pět konkrétních
`f`.

### N1 — MACHIN_BRIDGE (spotřeba WP3D Q7)

Cesta A: rovnost `p_I = p_M` vlastní veřejný WP3D (Q7: `A(1/q)=A_q`,
adiční zákon `C¹` substitucí, tři kompozice). Zde se **cituje**,
nedokazuje; samostatný důkaz z v2 je touto citací nahrazen a zůstává
v historii v2. Rodičovské věty se citují přesným zněním a jejich
artefakty jsou zamčené hashem v PREREG textu (kontroluje reviewer
při pinu; verifier žádné soubory nečte). Provenanční stráž: oblečená
semena sestupují z přesné aliasové třídy `p_M = p = pi_atan` WP3E
(kontrola definice a grafu, ne řetězce).

### N2 — SLICE_OBJECT_IDENTIFICATION (po N1)

Pro reálné `s ∈ Q_{>0}` se WP3E objekty rovnají WP3D objektům:

- **N2a POW_RAT_EXP_LOG_ID:** pro `x > 0`, `r = m/n` splňuje
  `exp_R(r·log_R x)` rovnici `y^n = x^m` a je kladné (produktový
  zákon `exp` + inverze `log`); POW-EXPLOG-ID (třída §0.1(1)) je
  ztotožní s WP3D hodnotou `x^r`. WP3D fixture „žádný exp/log ve
  třídě WP3D“ se nedotýká — políčkuje konstrukci uvnitř WP3D, ne
  identifikaci hodnot zde.
- **N2b SUP_EQUALS_LIMIT:** kladný integrand, monotónní síť řezů;
  monotónní supremum (WP3D TRUNC-0) = Cauchyho limita sítě (WP3E)
  z úplnosti.
- **N2c COFINAL_CUTS:** WP3E within-branch kompatibilita `u`-formy
  s poloosovou formou (WP3E §1.11) + kofinalita řezů
  `(δ,R) ↔ (e^{u_-}, e^{u_+})`. Žádné křížové čtení větví.

### N3 — RATIONAL_WITNESSES (spotřeba veřejného WP3D)

Z merged veřejné proby `P-JIPC-WP3D-QPOS-MELLIN-1`, pro `s ∈ Q_{>0}`:

- **N3-EOC:** `Ê(s)Ô(s) = Ĉ(s)` (WP3D Q8);
- **N3-REC:** `Ĉ(s+1) = s Ĉ(s)/(2p_M)` — z Q2 (`C(s+1) = sC(s)`),
  Q8a (`Ĉ(s) = 2(2p_M)^{-s}C(s)`) a Q7;
- **N3-DUP:** `Ĉ(s)Ĉ(s+½) = 2^{3/2-2s} Ĉ(2s)` — z Q5
  (`C(p)C(p+½) = 2^{1-2p}C(½)C(2p)`), Q8a a Q6+Q7
  (`(2p_M)^{-1/2} C(½) = 2^{-1/2}`);
- **N3-EPULL:** `Ê(s) = 2^{s/2-1} Ĉ(s/2)` — z Q8b
  (`Ê(s) = C(½)^{-s} C(s/2)`), Q8a a Q6+Q7 (`p_M^{s/2}/C(½)^s = 1`);
- **N3-JOIN:** `Ô(s) = Ê(s+1)` — Q2d ve WP3D (spojovací uzel) přenesený
  na oblečená semena (Q8).

Po N1+N2 jsou to výroky o WP3E objektech s vahou `p_M`.

### N4 — EFFECTIVE_NAMES pěti rozdílů

Jsou-li `P_j^{(n)}` WP3E aproximanty s chybou `≤ 2^{-(n+1)}` na
racionálním kompaktním obdélníku `K ⊂ D`, definuj n-uniformní
racionální sup-meze `M_j := sup̄_K|P_j^{(1)}| + 1` (racionální horní
mez konečné exponenciální sumy přes kraje `K`, exp-obálkou /v1;
`M_j` majorizuje každé `|P_j^{(n)}|` i `|F_j|`). Pět rozdílů:

\[
\begin{aligned}
f_{\mathrm{EOC}} &:= F_EF_O - F_C, \\
f_{\mathrm{REC}}(s) &:= F_C(s+1) - \kappa\,s\,F_C(s),\qquad \kappa := 1/(2p_M),\\
f_{\mathrm{DUP}}(s) &:= F_C(s)F_C(s+\tfrac12) - \lambda(s)\,F_C(2s),\qquad \lambda(s):=2^{3/2-2s},\\
f_{\mathrm{EPULL}}(s) &:= F_E(s) - \mu(s)\,F_C(s/2),\qquad \mu(s):=2^{s/2-1},\\
f_{\mathrm{JOIN}}(s) &:= F_O(s) - F_E(s+1).
\end{aligned}
\]

Posunuté obdélníky `K+1`, `K+½`, `2K`, `K/2` jsou racionální
kompaktní obdélníky v `D`, na nichž WP3E dodává jména. Konstanty
`κ`, `λ(s)`, `μ(s)` jsou jména podle §1 vyhodnocená na přesnosti `m`
(racionální obálka `κ` šířky `≤ 2^{-(m+1)}` z Machinovy obálky `p_M`
na BITS `m`; `exp_C` s explicitním ocasem pro `λ, μ`) a vstupují do
součinového pravidla stejně jako rodičovské aproximanty: pro součin
dvou jmen s n-uniformními mezemi `M_a, M_b` je chyba
`≤ (M_a + M_b) ε`, pro `s·F_C(s)` navíc racionální mez `sup_K|s|`,
pro každý další sčítanec `+1`. Každé `f` dostává rozvrh

\[
h := \min\{k : 2^k \ge \text{součet koeficientů}\},\qquad m := n+h+2,
\]

celková chyba `≤ 2^{-(n+3)}`. Před pinem se zmrazí jediný
deterministický algoritmus obálek, pořadí součtů a vnější
zaokrouhlení. Každé `f` je holomorfní na `D` s efektivním jménem na
každém racionálním kompaktním obdélníku.

### N5 — RAY_VANISHING (pro obecné `f` z N0)

Pro `σ > 0` zvol racionální `s_k → σ`; `f(s_k) = 0` (N3) a spojitost
s modulem z efektivního jména dává `f(σ) = 0`. Tedy `f = 0` na
`(0,∞)`.

### N6 — DISK_CHAIN_PROPAGATION (pro obecné `f` z N0)

Pro `s = σ + it ∈ D` polož `r = σ/2` a řetěz
`c_k = σ + i·sgn(t)·kσ/4`, `k = 0..K`, `K = ⌈4|t|/σ⌉`: každý disk
leží v `D`, `|c_{k+1} - c_k| = σ/4 < r`, `|s - c_K| ≤ σ/4 < r`.
Základna `B(c_0,r)` má reálný průměr `(σ/2, 3σ/2) ⊂ (0,∞)`, kde
`f = 0` — IT-SEGMENT(i); krok — IT-SEGMENT(ii). Po `K` krocích
`f(s) = 0`; tedy `f ≡ 0` na `D`. Auditní brána §3.5 přehrává jednu
racionální instanci.

### N7 — koncový uzel a koprodukty

Z N0 aplikovaného na pět rozdílů:

```text
JIPC_WP3F_EOC_HOLOMORPHIC    (sink)       Ê·Ô = Ĉ                     na D
JIPC_WP3F_REC_HOLOMORPHIC    (koprodukt)  Ĉ(s+1) = s Ĉ(s)/(2p_M)       na D
JIPC_WP3F_DUP_HOLOMORPHIC    (koprodukt)  Ĉ(s)Ĉ(s+½) = 2^{3/2-2s}Ĉ(2s) na D
JIPC_WP3F_EPULL_HOLOMORPHIC  (koprodukt)  Ê(s) = 2^{s/2-1} Ĉ(s/2)      na D
JIPC_WP3F_JOIN_HOLOMORPHIC   (koprodukt)  Ô(s) = Ê(s+1)                na D
```

THEOREM_CARRIER = WRITTEN_PROOF_NOT_FINITE_AUDIT. Povinné hrany:

```text
PUBLIC_WP3D_PARENT -> N1
N1 -> N2
N2 + PUBLIC_WP3D_PARENT -> N3
PUBLIC_WP3E_PARENT -> N4
N3 + N4 -> N5
N4 + N5 + IT_SEGMENT_RULE -> N6
N5 + N6 -> N0
N0 + N4 -> N7 (pět instancí)
```

`N4 → N5` je povinná hrana; `N4` není potomkem N3. Jediným sinkem je
N7-EOC; koprodukty jsou pojmenované listy téže větve; žádný primární
uzel není mrtvý.

## §3. Ohraničený auditní povrch verifieru

Verifier přebírá závazky WP3E a aktuální praxi: zero-arg; žádné I/O
(soubor, stdin, prostředí, hodiny, síť); jediný import
`fractions.Fraction`; žádná plovoucí čárka (žádné `** 0.5`, `sqrt`,
float/complex literál), žádný `ast.Div` (jen celočíselné `//` a
konstruktor `Fraction`); žádný random, subprocess, dynamický import,
`eval`/`exec`; tvrdý timeout 600 s; bajtová identita stdout na
x86_64 i aarch64, Python 3.12; **jediný stdout artefakt je
`EXPECTED.txt`** — žádný transkript se zakázanou příponou nebude
požadován. Preflight před jediným formálním během:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
požadováno: exit 0; stdout přesně PYTHON_STARTUP_CLEAN + LF; stderr prázdný
```

Přesné PASS řádky se zmrazí ve Field-4 stylu v PREREG před pinem;
soubor `EXPECTED.txt` se commituje až po jediném formálním běhu.
Rodičovské hashe (WP3D, WP3E) jsou zámek v textu PREREG, který
kontroluje reviewer při pinu — verifier je nečte a žádnou „readback“
bránu netiskne.

**Přehrávací okruh:** `Q[g, g^{-1}, h, h^{-1}] / (g^2 - π̂, h^2 - 2)`,
kde `g` je token `C(½)` (`π̂ = g^2`) a `h` token `2^{1/2}`; `h`
vstupuje do každé půlceločíselné hodnoty `Ĉ(k+½)` přes
`(2p_M)^{-(k+½)} = h^{-(2k+1)} g^{-(2k+1)}`, nejen do koeficientu
DUP-D. Žádná numerická hodnota `g` ani `h` se nevyhodnocuje.
Zmrazená tabulka (odvozená z `Ĉ(s) = 2(2p_M)^{-s}C(s)`, `C(1) = 1`,
`C(½) = g`, REC), kterou verifier **generuje** z REC a kotev, nikoli
opisuje:

```text
Ĉ(1)   = g^-2            Ĉ(3/2) = h^-3 g^-2
Ĉ(2)   = (1/2) g^-4      Ĉ(5/2) = (3/2) h^-5 g^-4
Ĉ(3)   = (1/2) g^-6      Ĉ(7/2) = (15/4) h^-7 g^-6
Ĉ(4)   = (3/4) g^-8      Ĉ(6)   = (15/4) g^-12
Ê(s)   = g^-s C(s/2)  (WP3D Q8b tvar; C(k/2) z REC a C(½)=g)
Ô(s)   = Ê(s+1)
```

Zmrazený formát stdout (hodnotově prostý):

```text
JIPC_WP3F_LIFT_AUDIT 1
ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS
PARENT_SENTENCE_REPLAY MACHIN POLY,CROSS3,DOMAINS PASS
SLICE_WITNESS_REPLAY EOC,REC,DUP,EPULL,JOIN S=1,2,3 RING=Q[g,g^-1,h,h^-1] PASS
NAME_SCHEDULES K=[1,3/2]x[-1/2,1/2] F=5 N=1 PASS
SAMPLE_BALL_OVERLAP S=3/2+i/2 BITS=2,3 F=5 PASS
CHAIN_GEOMETRY S=3/2+i/2 R=3/4 K=2 PASS
PROOF_CONTROLS 19/19 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
```

Brány:

1. `PARENT_SENTENCE_REPLAY`: exaktní přehrání citovaných rodičovských
   vět Q7 (polynomiální identita `(1-uv)^2+(u+v)^2=(1+u^2)(1+v^2)`,
   tři krácicí svědci, doménové podmínky) — skutečná sémantická
   replika, ne kontrola hashů.
2. `SLICE_WITNESS_REPLAY`: exaktní přehrání všech pěti identit
   v `s ∈ {1,2,3}` v přehrávacím okruhu podle zmrazené tabulky
   (např. `Ê(1) = 1`, `Ô(1) = Ĉ(1) = g^{-2}`; `Ĉ(2) = Ĉ(1)/(2g^2)`;
   `Ĉ(1)Ĉ(3/2) = h^{-1}Ĉ(2)`, tj. `h^{-3}g^{-4}` na obou stranách;
   `Ê(1) = h^{-1}Ĉ(½)` s `Ĉ(½) = 2(2p_M)^{-1/2}g = h`).
3. `NAME_SCHEDULES`: pro `K = [1,3/2]×[−1/2,1/2]` spočti zmrazeným
   postupem racionální sup-meze a posunuté rozvrhy pro všech pět
   `f` při `n = 1`, včetně obálek jmen `κ, λ, μ` na přesnosti `m`
   (algoritmus je zmrazený povrch; hodnoty vydá formální běh).
4. `SAMPLE_BALL_OVERLAP`: v `s = 3/2 + i/2` boxy obou stran každé
   z pěti identit při `b = 2, 3`; vně zaokrouhlené boxy se musí
   protínat a každý box splnit svůj zmrazený poloměrový rozpočet.
   Vnořenost ani zmenšení průměru se netvrdí.
5. `CHAIN_GEOMETRY`: racionální instance N6 pro `s = 3/2 + i/2`
   (`r = 3/4`, `K = 2`).
6. `PROOF_CONTROLS` (19, každá selhává na pojmenované stráži téhož
   kódu, který konzumuje PASS cesta): 1–4 mutace svědků brány 1
   (koeficient polynomu, křížový svědek, `uv ≥ 1`, znaménko
   indexace); 5 provenanční stráž aliasové třídy `p_M`; 6 křížové
   čtení `O := E(s+1)` v definiční vrstvě; 7 vynechaný N1; 8
   mutovaný rozvrh N4 (chybějící `+2`); 9 krok středů `σ`; 10
   `r = 2σ`; 11 mutovaný reálný průměr základny; 12 mutovaný svědek
   `s=1`; 13 nárok pokračování/FE (STOP stráž); 14 `Re s ≤ 0`; 15
   mutovaný koeficient REC-D (`κ ↦ 2κ`); 16 mutovaný exponent DUP-D
   (`3/2−2s ↦ 1−2s`); 17 mutovaná obálka jména `λ(s)` (ocas `exp_C`
   vynechán — stráž rozvrhu); 18 mutovaný exponent EPULL-D
   (`s/2−1 ↦ s/2`); 19 mutovaný posun JOIN-D (`s+1 ↦ s+2`).

## §4. Falzifikátory, integrity STOP a omezený fallback

`FIRED` vzniká pouze hotovou exaktní matematickou negací:

- F1: exaktní protipříklad vyvrátí některý psaný uzel N0–N7;
- F2: po nezávislém potvrzení aritmetiky vzniknou v témže povoleném
  bodě dva zvukové, navzájem disjunktní boxy pro strany některé
  z pěti identit;
- F3: exaktní výpočet vyvrátí zmrazenou doménovou podmínku,
  rozvrh jmen nebo geometrii řetězu, nikoli jen implementaci.

`STOP`, nikoli `FIRED`: průchod negativní mutace, drift rodičovského
hashe či textu, selhání autority, collision scanu, claim locku,
pinu, readbacku, preflightu, bezpečnosti, timeoutu, determinismu,
bajtů, transkriptového pravidla nebo architekturní integrity, a
každé selhání, které může být vadou verifieru. Projde-li omezený
audit, ale univerzální důkaz není přijat, výsledek je nejvýše
`BOUNDED-AUDIT-C` (týž štítek jako u WP3D) na zmrazeném konečném
povrchu.

## §5. Rozhodovací kontrakt a co žebřík staví

```text
CANDIDATE-T      = oba veřejní rodiče (WP3D merged + WP3E merged) +
                   přijatý psaný důkaz N0–N7 + připnutý audit + obě
                   architektury PASS   (RESULT.md status; stdout
                   končí řádkem RESULT PASS)
BOUNDED-AUDIT-C  = audit PASS, ale univerzální důkaz nebo rodič není
                   theorem-grade; platí jen konečný zmrazený povrch
FIRED            = hotová exaktní matematická negace
STOP             = integrita, kód, mutace, běh nebo autorita selhala
```

Stdout vyjadřuje pouze omezený audit; výběr stavu patří do
`RESULT.md`. Strop: candidate-T / L1.

**Co žebřík staví (poznámka, fenced, žádný nárok).** Kontrakt
`C(p)C(q) = C(p+q)B(p,q)` s pevným Beta integrálem `B` fixuje bare
`C` na `Q_{>0}` až na exponenciální faktor: v klasické měně je každé
kladné řešení tvaru `C(s) = b^{s}·Γ(s)` (podíl `C/Γ` je
multiplikativní, `φ(p)φ(q) = φ(p+q)`, tedy `φ(s) = b^{s}` z
jednoznačnosti kladného kořene). Most `C(½)^2 = p_M` pak dává
`b·Γ(½)^2 = p_M`, tj. `b = 1`: kontrakt + most fixují `C = Γ` přesně,
a `C(½)^2 = p_M` je výrok `Γ_R(1) = 1` v Γ-substitute měně.
(EPULL-D) je pak vztah reálného a komplexního místního faktoru
`Γ_R(s) = 2^{s/2-1}Γ_C(s/2)` bez importu Γ. To je feeder pro
`C-J-DEDEKIND-WEIL-ROAD-N` O1, ne jeho splnění; Γ se nikde
neimportuje a žádné místní čtení se netvrdí.

## §6. Otevřené závislosti — podmínky veřejného pinu

1. **Režim:** `A_SELECTED`; `B_CLOSED`.

2. **Veřejný WP3E lock:** PR #569 merged jako
   `9a4b479b0a7a9ce39772f77f16dd363602ec72c7`; parent-lock ponese
   pin `46004772f3a6510791adf2ae4afd14a8a9f7f5af`, PREREG SHA-256
   `af078f17645dc8b5ef78acefb53bf73b791045efd2147bf2d87ed5006e9bdd80`,
   verify SHA-256
   `373ff274abcc27e06b12e8aee1ebd0bfc0de6bebbc66ed69e1c53e87a06369d1`,
   stdout SHA-256
   `f51edb6ed4d7733abca72ea45e091cfa9241c36848b9509d532828e609cc2056`,
   formal result head `289ea861c6289f0e6426b1cabffd0c54fb7c059f`,
   status candidate-T / L1 / Canon unchanged. WP3E bez foldu není
   aktivní veřejné `[T]`.

3. **Veřejný WP3D-QPOS lock:** stav při tomto psaní: PR #572 nese
   v72 verzi draftu; refreeze na v74 a tento balík jsou na notes
   větvi téhož rodu (notes-lane PR nahrazující #572). Pořadí: merge
   notes-lane PR → claim-lock issue (text připraven) →
   `probe/P-JIPC-WP3D-QPOS-MELLIN-1` + attempt ref → pin → readback
   → preflight → jediný formální běh → `EXPECTED/RUN/RESULT` →
   x86_64+aarch64 → merge. Skončí-li WP3D pouze `BOUNDED-AUDIT-C`,
   strop WP3F klesá na `BOUNDED-AUDIT-C`.

4. **Veřejný WP3F claim lock:** po merge WP3D nový úplný collision
   scan (`git ls-remote --heads`, issues, PRs, `probes/`, registrové
   řádky a object/claim locky), pak jediný claim issue s aktuálním
   readback tuple, reading-family NOT_APPLICABLE + třídy
   jednoznačnosti §0.1, L1, result-exposed.

5. **Autorita a base:** tuple a `BASE_COMMIT` z tehdejšího `main`;
   refreeze každého pole při pinu.

6. **TCB a strojová smlouva:** před pinem zmrazit TCB/v2 (IT-SEGMENT,
   POW-EXPLOG-ID), úplný DAG včetně N0, algoritmus jmen a obálek
   (včetně `κ, λ, μ`), zaokrouhlení, prostředkové meze, všech 19
   kontrol, přehrávací okruh s generovanou tabulkou a přesné stdout
   bajty.

7. **Accepted verifier:** `PREREG.md` a nikdy nespouštěný
   self-contained `verify.py` se připnou společně; statický audit
   (py_compile + AST scan: 0 `ast.Div`, 0 float/complex literálů,
   1 import) je zapsán do PREREG jako checklist řádek. Žádný formální
   výpočet nesmí vzniknout dříve.

8. **Následník:** WP3G (meromorfní pokračování + globální identity)
   konzumuje N7-REC, N7-DUP, N7-EPULL, N7-JOIN; viz
   `WP3G_CONTINUATION_PREREG_DRAFT_v1.md`.
