# PREREG — nezávislý posudek PR #1959 (fáze 1), zmrazeno před prvním spuštěním review.py

Status: NON-CANONICAL. Posudek žádný status v kánonu nemění ani nezvyšuje.
Cíl: [PR #1959](https://github.com/mathorn1973/twist-j/pull/1959),
větev `codex/resonant-record-public-intake`, přesná hlava
`2dd5c7acaea30a9b6d39529044d05f85c2ce99ab` (jediný commit, rodič = veřejná
`main` `a8482d068156c8f42a390a81e817566b1c5abeda`), balík
`notes/C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N/` (dále „cesta PR“).
Autor posudku: relace Claude Code na větvi `claude/wonderful-wright-vw2x3f`,
2026-11-08. Jiná relace než autor PR a než přípravná relace intake.
Autorita: `STATUS.md` ACTIVE, Public Canon v109, tag `canon-v109`
(objekt `a33f63339b16b69725bf856e403610614143f81f`, aktivace
`650029c20408f1dd665983d72225d0d195fd030e`), obsahový commit
`2b0f94ec1e0874bff9141259e0b7da80e6681ea6`; souhlasí se SOURCES.md PR.

## 0. Expozice — tohle NENÍ slepý posudek

Na rozdíl od posudků #1862/#1865/#1879 nebyla autorova data skryta. Před
sepsáním tohoto souboru jsem v cestě PR přečetl **všechny** markdown soubory
(README, PROOF, PREREG, ERRATA, PUBLICATION, SOURCES, RESULT, RUN, REVIEW),
oba očekávané výstupy `EXPECTED.txt` a `BREAK_EXPECTED.txt` (576 B, devět
řádků s čísly kontrol) a `SHA256SUMS`. Dále jsem před zmrazením:

- jednou spustil autorovy `verify.py` a `break.py` beze změny z kořene
  checkoutu hlavy PR (Linux x86_64, CPython 3.13.18, prostředí
  `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`):
  oba exit 0, stderr 0 B, stdout 576 B bajtově shodný s oběma očekávanými
  soubory (`cmp` IDENTICKÝ, syrově, bez normalizace konců řádků);
- ověřil `sha256sum -c SHA256SUMS` (13/13 OK) a spustil
  `check_policy`, `check_canon`, `check_ledger`, `check_gate_contract`
  (vše PASS) na stromu hlavy PR;
- spustil **neformální** průzkumný skript (SHA-256
  `c0f4a5a4f92b89bc387f3fc5e6e771950a3de9b41b0e19974f4ca32fede1b38d`,
  není součástí posudku), který ověřil podmnožinu níže uvedených kontrol
  (J·J⁻¹, hodnotu c, h(c), Věta 1 na mřížce, Věta 2 na 6480 párech, E1–E4,
  bezdělitelnost nuly v O/2O, zámek/zpětnou reakci Věty 5, jmenovatele
  do n=25). Všechny prošly. Počet rezonančních párů 38 a počet B=0 seedů
  49 proto znám předem a níže je uvádím jako kritéria, ne jako slepé
  pozorování.

Co jsem **neotevřel** a do konce fáze 1 neotevřu: tělo autorova `verify.py`
a `break.py`. Z nich jsem viděl pouze výpis `grep` řádků `import`/`from`
(`__future__`, `fractions`, `itertools`, `math`, `sys`) a jmen funkcí
na úrovni modulu (`v_add`, `v_sub`, `v_neg`, `v_scale`, `v_mul`, `v_pow`,
`v_conj`, `v_div2_exact`, `v_in_2o`, `v_mod2`, `v_eps_mod5`, `h_pair`,
`phi_*`, `q_norm`, `colocated_step`, `check_cut_invariants`, `main`).
Žádný řádek jejich implementace jsem nečetl a `review.py` z nich nic
nepřebírá. Zdrojem kontraktu jsou výhradně rovnice v PROOF.md, PREREG.md,
ERRATA.md a README.md v cestě PR a předchůdce #1957 (PREREG.md ř. 104–144,
pouze pro označení vstupů P27/P35).

Tento soubor je sepsán a commitnut před prvním spuštěním `review.py`.

## 1. Kontrakt odvozený z textu PR (rovnice, ne očekávání)

- `O = Z[j]`, `1+j+j^2+j^3+j^4 = 0`; mocninná báze `(1,j,j^2,j^3)`
  (PROOF §1). Konjugace `j -> j^4`.
- `rho = j^2`, `phi = -j^2 - j^3`, `J = 1 + rho`; `phi^2 = phi + 1`
  (PROOF §1, ERRATA E2). `J^{-1} = -j - j^2` (PROOF 5.2).
- `h(v) = v*conj(v) = A + B*phi`, `Q(v) = 2A + B = Tr_{Q(phi)/Q}(h(v))`
  `= (1/2) Tr_{K/Q}(v*conj(v))`; `N(h(v)) = A^2 + AB - B^2 = N_{K/Q}(v)`;
  kvadratické formy `S0,S1,S2`, `A = S0 - S1`, `B = S1 - S2` (PROOF 2.1–2.5).
- Ko-lokovaný Gaussův nosič: slot `x` ve vrcholu A, sloty `v_r` ve vrcholu
  B, pole `F`; `G_A: F + x = 0`, `G_B: F - sum v_r = 0` (PROOF 1.1).
- Kontakt `C(x, v)`: `d = (v - x)/2`; není-li `d` v `O`, identita;
  jinak `i = (rho - 1) d`, `x' = x - i`, `v' = v + i`, `F' = F + i`
  (PROOF 1.2–1.3). Inverze slova: obrácené pořadí, každý kontakt čtyřikrát.
- Účty: `E_full = 2(Q(x) + sum Q(v_r))`, `H_full = 2(h(x) + sum h(v_r))`
  (PROOF 2.6–2.7); residua `eps(v) = sum v_i mod 5` jsou po slotech
  invariantní (PROOF §1.1).
- Věta 2 (A2): stav `(x,h,z,u) = (a, a+2c, 0, -2a-2c)`, `F = -a`, slovo
  `C(x,z) o C(x,h)`; druhý kontakt připuštěn a `x_2 = a` právě když
  `a = Jc`; v rezonanci trajektorie (3.5), `h(h_0) = h(h_1) + h(z_2)`,
  `Q(h_0) = 17A+B`, `Q(h_1) = 12A-4B`, `Q(z_2) = 5(A+B)`, plocha `2h(c)`.
- Věta 3 (A3): pět kanálů `h_k = (3+rho)c rho^k`, `z_k = 0`, `u_k = -h_k`,
  společník `u_x = -a_m`, vstup `x = a_m = Jc rho^m`, pevné desetikontaktové
  slovo `C(x,z_k) o C(x,h_k)` pro `k = 0..4`; one-hot právě když `c` není
  v `2O`; `O/2O` je těleso o 16 prvcích; sudý svědek: `m = 1`, `k = 0`.
- Prop. 2 (A4): `c = (1-rho) J^{-1} = (-1,-2,-2,0)`, `h(c) = 3 + 4phi`,
  `Q(c) = 10`, `Q(a_k) = 5`, `Q(h_{0,k}) = 55`, `Q(h_{1,k}) = 20`,
  `w_0 = 35`, plocha `6 + 8phi`; port se dvěma selektory
  (cíle `a_0 = 1 - rho`, `a_1 = (1-rho) rho^4`).
- Věta 4 (A5): konstantní kvantum `w_0 = 5(A+B)` → podíly práce i
  hermitovské podíly rovny podílům počtů.
- Věta 5 (A6): zámek na čerstvé nule, zpětná reakce (7.3), jmenovatele
  `2 b^n` pro `(a_0,b) = (5,4), (7,6)`.
- ERRATA E1–E6 jako samostatná tvrzení (viz R13).

## 2. Zmrazené vlastní konvence

K1 Prvek `O` je čtveřice `(v0,v1,v2,v3)` v mocninné bázi. `rho=(0,0,1,0)`,
   `J=(1,0,1,0)`, `phi=(0,0,-1,-1)`, `J^{-1}=(0,-1,-1,0)` (ověřuje se, ne
   předpokládá). Dvě násobení: (A) redukce modulo `1+j+j^2+j^3+j^4`,
   (B) cyklická konvoluce délky 5 s odečtem páté složky; shoda se kontroluje.
K2 `h(v)` počítám z **součinu** `v*conj(v)` (reálný prvek `A - B j^2 - B j^3`),
   nikoli z formulí S0/S1/S2; ty jsou kontrolovanou veličinou.
   Prvky `Z[phi]` jsou dvojice `(A,B)`; `Tr = 2A+B`, `N = A^2+AB-B^2`.
   `Tr_{K/Q}(v) = 4 v0 - v1 - v2 - v3`.
K3 Kontakt přesně podle §1 kontraktu; „připuštěn“ právě když všechny čtyři
   složky `v - x` jsou sudé. Inverze slova = obrácené pořadí, každý kontakt
   `C^4`. Primitivní řez = jedna aplikace kontaktu, připuštěného i
   odmítnutého. Na každém řezu se kontrolují `G_A`, `G_B`, celkový součet
   slotů, `eps` každého slotu, `E_full`, `H_full` (konvence K5).
K4 Pořadí slotů vrcholu B: Věta 2 `(h, z, u)`; Věta 3
   `(u_x, h_0, z_0, u_0, ..., h_4, z_4, u_4)`; port A4 `(u_x, h_0, z_0, u_0,
   h_1, z_1, u_1)`.
K5 Čítání řezů: Věta 2 — 2 dopředu + 8 inverze = 10 na pár; Věta 3 a port —
   10 + 40 = 50 na běh. Čítá se každá aplikace, i odmítnutá.
K6 Profily počtů pro Větu 4 (mé, dvanáct): `(1,0,0,0,0)`, `(0,1,0,0,0)`,
   `(0,0,0,0,1)`, `(1,1,1,1,1)`, `(2,1,0,0,0)`, `(0,0,3,0,0)`,
   `(1,2,3,4,5)`, `(5,4,3,2,1)`, `(7,0,0,0,1)`, `(2,2,2,0,0)`,
   `(1,0,1,0,1)`, `(10,1,1,1,1)`. Každá událost = jeden skutečný běh
   čerstvé banky, ne algebraický násobek.
K7 Primitivní polarizace pro Větu 5.3 (mé čtyři): `(1,0,0,0)`, `(1,1,0,0)`,
   `(0,1,-1,0)`, `(1,2,2,0)`. `cos(n omega)` počítám dvěma cestami:
   rekurencí `P_n` z (7.4) a Čebyševovou rekurencí
   `c_{n+1} = 2 cos(omega) c_n - c_{n-1}` v `fractions.Fraction`.
K8 Označení vstupů portu podle #1957 PREREG ř. 135 a 143–144: **P27 =
   vstup `a_1 = (1-rho) rho^4`**, **P35 = vstup `a_0 = 1 - rho`**; výstup
   `(Q(z_0), Q(z_1))`, kanál 0 má cíl `a_0`, kanál 1 cíl `a_1`.
K9 Serializace fingerprintů (pozorované hodnoty, bez kritéria): řádky
   `a0,a1,a2,a3|c0,c1,c2,c3\n` lexikograficky podle čtveřic; pro banku
   `c|m|x|h0,z0,h1,z1,h2,z2,h3,z3,h4,z4\n`. SHA-256 textu v UTF-8.
K10 Množiny: `G625 = {-2..2}^4`; `G81 = {-1,0,1}^4 \ {0}` (80 prvků) plus
   `(-1,-2,-2,0)` = 81 lichých seedů; sudé seedy = jejich dvojnásobky (81);
   páry Věty 2: `a` ze `{-1,0,1}^4` (81) × `c` z `{-1,0,1}^4 \ {0}` (80).

## 3. Kontroly (PASS právě když platí kritérium; jinak FAIL, exit 1)

R01 Prstenec. `j^5 = 1`, `Phi_5(j) = 0`, `phi^2 = phi + 1`,
    `Tr_{K/Q}(phi) = 2` (tedy `Tr_{Q(phi)/Q}(phi) = 1`, E2),
    `J * (0,-1,-1,0) = 1`, `J` je jednotka (determinant matice násobení
    ±1), `det(1 - rho) = 5`; násobení (A) == (B) na všech 6561 párech
    z `{-1,0,1}^4` a na `G625 × {j, rho, J, phi, c#}`.
R02 Formy. Na `G625`: `h` ze součinu == `(S0-S1, S1-S2)`;
    `2A+B == Tr_{K/Q}(v conj v)/2`; `A^2+AB-B^2 == det M_v`;
    pro `v != 0`: `2A+B > 0`.
R03 Konstanty. `h(1-j^2)=(2,1)`, `h(1-j^4)=(3,-1)`, `h(J)=(2,-1)`,
    `h(3+rho)=(10,-3)`; `(2+phi)(3-phi)=5` v `Z[phi]`; na `G625`:
    `h((rho-1)d) = (2+phi) h(d)` a `5 h(c) = (3-phi) h((rho-1)c)`;
    `h(3+rho) = 4h(J) + h(1-rho)`.
R04 Věta 1.3. Na `G625`: (2.10) oba vzorce; `Q((1-j^2)c) = 5(A+B)`,
    `Q((1-j^4)c) = 5A`, součet `5Q(c)`; rovnost obou členů právě když
    `B = 0`; počet seedů s `B = 0` **== 49**; protipříklad
    `c_1 = 1-j^2`, `c_2 = 1-j^4`: `Q(c_1)=Q(c_2)=5`,
    `Q((1-j^2)c_1)=15 != 10 = Q((1-j^2)c_2)`; E2: pro `c = 1` je `B = 0`,
    `Q((1-j^2)·1) = 5 != 10 = 5Q(1)`.
R05 Kontaktní zákon. Na všech 6561 párech `(x,v)` z `{-1,0,1}^4` s
    `F = -x`: odmítnut právě když některá složka `v-x` je lichá; odmítnutý
    je identita; připuštěný zachovává `x+v`, `eps(x)`, `eps(v)`,
    `Q(x)+Q(v)`, `h(x)+h(v)`, `F+x`; `C^5 = id`; `C^4` je inverze;
    plocha kroku `h(d)`.
R06 Věta 2. Na 6480 párech (K10): invarianty K3 na všech 10 řezech,
    inverze vrátí přesný počáteční stav, celkem **64800** řezů; první
    kontakt vždy připuštěn s `d_1 = c`; čtyři výroky
    `[adm2 ∧ x_2=a]`, `[adm2 ∧ F_2=-a]`, `[adm2 ∧ z_2!=0 ∧ x_2=a]`,
    `[a = Jc]` jsou na každém páru všechny pravdivé nebo všechny
    nepravdivé; počet rezonančních párů **== 38**; Prop. 1: pro
    `(a,c)=(1,1)` se součty slotů liší. Na 624 nenulových `c` z `G625` při
    `a = Jc`: trajektorie (3.5) včetně `d_2 = -c`, `F_2 = -a`,
    `h(h_0) = h(h_1) + h(z_2)`, `Q(h_0)=17A+B`, `Q(h_1)=12A-4B`,
    `Q(z_2)=5(A+B)`, plocha `h(d_1)+h(d_2) = 2h(c)`.
R07 Lemma 1. `Phi_5` nemá kořen v `F_2` a není dělitelný `t^2+t+1`;
    tříd modulo `2O` je 16; všech 225 součinů nenulových tříd je nenulových.
R08 Věta 3. Pro 162 seedů (81 lichých, 81 sudých) × 5 fází: invarianty
    K3 na všech 50 řezech, inverze vrátí počáteční stav, celkem **40500**
    řezů. Liché: one-hot (všechny `k != m` beze změny, `z_m' = (1-rho)c
    rho^m`, `h_m' = 2Jc rho^m`, `x,F` obnoveny), přesně 2 připuštěné
    kontakty z 10, `Q(z_m') = 5(A+B)`, `h(z_m') = (2+phi)h(c)`, plocha
    `2h(c)`, `E_full = 4Q(Jc) + 20Q((3+rho)c) = 352A + 16B` (E3),
    `H_full = 4h(Jc) + 20h((3+rho)c)` — **všech 81 PASS**. Sudé: pro
    `m = 1` je první kontakt kanálu `k = 0` připuštěn a `h_0` je na konci
    slova změněno; pro žádný sudý seed není banka one-hot ve všech pěti
    fázích — **všech 81 FAIL one-hot**. Fingerprint banky dle K9
    (pozorování).
R09 Prop. 2 / A4. `c# = (1-rho)(0,-1,-1,0) = (-1,-2,-2,0)`, není v `2O`,
    `h = (3,4)`, `Q = 10`; pro `k = 0..4`: `Q(a_k)=5`, `h(a_k)=(2,1)`,
    `Q(h_{0,k})=55`, `h=(18,19)`, `Q(h_{1,k})=20`, `h=(8,4)`,
    `Q(z_{2,k})=35`, `h=(10,15)`, plocha `(6,8)`, `a_0 = 1 - rho`;
    port dle K8: `P27 -> (0,35)`, `P35 -> (35,0)`, v obou případech `x,F`
    obnoveny a druhý kanál nedotčen.
R10 Věta 4. Pro 81 lichých seedů × 12 profilů K6: každá událost běží jako
    čerstvá banka; `W_k = N_k w_0`; `W_k · sum N = N_k · sum W` (celá čísla)
    a `H_k · sum N = N_k · sum H` v `Z[phi]`; pro `N_k > 0` je
    `W_k / N_k = w_0`; celkem **4860** kanálových porovnání.
R11 Věta 5.1–5.2. Pro 81 lichých seedů × 5 fází (405): na
    `(Jc rho^m, 2Jc rho^m, 0)` oba kontakty odmítnuty; na
    `(Jc rho^m, 2Jc rho^m, (1-rho)c rho^m)` první odmítnut, druhý
    připuštěn s `d_2 = -rho^{m+1} c`, výsledek
    `x' = (1+rho^2)c rho^m`, `z' = (1-rho^2)c rho^m`, přičemž
    `(x',z') != (-rho^{m+1}c, c rho^m)` (E6) a `x' != Jc rho^m`.
R12 Věta 5.3. Pro `(5,4)` i `(7,6)` a `n = 1..25`: `P_n` liché,
    `gcd(P_n, 2b^n) = 1`, `P_n / (2 b^n)` == Čebyševova rekurence
    (K7) jako `Fraction`; pro čtyři polarizace K7: `e_0 cos(n omega)` má
    aspoň jednu neceločíselnou složku pro každé `n`, zatímco
    `2 b^25 e_0 cos(n omega)` je celočíselné pro všechna `n <= 25`.
R13 Errata. E1: `(1,2,2,1) != c#`, `h = (2,3)`, `Q = 7`, `5(A+B) = 25`.
    E3: na `G625` platí `352A+16B`, a pro `c = 1` je `200A+60B = 200 !=
    352`. E4: pro všechna `d_2` z `G625`:
    `(-2d_2) - (rho-1)d_2 = -J d_2`, zatímco `(-2d_2) + (rho-1)d_2`
    se od `-J d_2` liší pro `d_2 != 0`. (E2 v R01/R04, E6 v R11.)
R14 Citlivost ověřovače (mutanty mimo hlavní běh): (a) kontakt s proudem
    `(1-rho)d` místo `(rho-1)d` musí porušit ekvivalenci R06 aspoň na
    jednom páru; (b) `J^{-1}` nahrazeno `(0,-1,0,-1)` musí porušit R01.
    PASS právě když oba mutanty jsou detekovány.

## 4. Závazný rozsah běhu a výstup

Plný rozsah bez vzorkování. `review.py` nečte žádný soubor, nezapisuje,
nepoužívá síť, náhodu ani float. Příkaz z kořene repozitáře:

```sh
env LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 notes/C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N-REVIEW-1/review.py
```

Tiskne řádek `Rxx PASS ...` nebo `Rxx FAIL ...` pro každou kontrolu,
pozorované počty a fingerprinty, a poslední řádek `RESULT PASS` (exit 0)
nebo `RESULT FAILURE` (exit 1). Výstup neobsahuje cesty, časy ani platformu.

Selhání se zaznamená beze změny. Oprava ověřovače je nová, samostatně
zmrazená revize; obě se uchovají. Žádný práh ani fixture se po zmrazení
nemění.

## 5. Fáze 2 (po zmrazení a běhu)

1. Ověřit hashe zmrazených souborů proti GitHubu, znovu spustit `review.py`.
2. Spustit autorovy `verify.py` a `break.py` beze změny z kořene checkoutu
   hlavy PR, uložit stdout/stderr, `cmp` proti očekávaným souborům.
3. Teprve poté otevřít těla `verify.py` a `break.py`, porovnat veličiny
   a mechanismy, každou položku označit MATCH / DIFF-CONVENTION / DIFF-REAL
   (`COMPARISON.json`).
4. Administrativní kontroly: `SHA256SUMS`, tabulka PUBLICATION.md, hashe
   v PREREG.md PR, autorství a předek commitu, `check_*`, CI běh, hledání
   soukromých údajů.
5. Rozhodnutí v `RESULT.md`: PASS / PASS S POZNÁMKOU / FAIL, co ověřil čí
   kód, co CI, co zůstalo neověřeno, co nezávislost je a co ne.
