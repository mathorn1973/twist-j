# PREREG — nezávislý slepý posudek PR #1961 (fáze 1), zmrazeno před prvním spuštěním review.py

Status: NON-CANONICAL. Posudek žádný status v kánonu nemění ani nezvyšuje.
Cíl: [PR #1961](https://github.com/mathorn1973/twist-j/pull/1961),
větev `codex/s3-loader-contract`, přesná hlava
`73f3cb4946b05f5d63aba1c279642f77c699caef` (čtyři commity nad veřejnou
`main` `a8482d068156c8f42a390a81e817566b1c5abeda`, autor i committer
A. M. Thorn), balík `notes/C-S3-HEIGHT-PHASE-INTERFACE-N/` s podsložkou
`CONSTRUCTIVE-3/` (dále „cesta PR“). Autor posudku: relace Claude Code na
větvi `claude/wonderful-wright-vw2x3f`, 2026-11-08; jiná relace než autor PR.
Autorita: `STATUS.md` ACTIVE, Public Canon v109, obsahový commit
`2b0f94ec1e0874bff9141259e0b7da80e6681ea6`; shodně se SOURCES.md PR.

## 0. Slepý režim a expozice

**Neotevřeno a do konce fáze 1 neotevřu:** v cestě PR všechny `*.py`
(`search.py`, `CONSTRUCTIVE-3/verify.py`, `audit.py`, `assembly.py`),
všechny `*EXPECTED*.txt`, oba `SHA256SUMS`, oba `RESULT.md`, oba `RUN.md`.
Z nich neznám žádný řádek, žádný hash ani žádný výstup.

**Přečteno (texty PR):** `README.md`, `CONTRACT.md`, `PREREG.md`,
`PROOF.md`, `SOURCES.md`, `REVIEW.md` v kořeni a `README.md`, `PREREG.md`,
`PROOF.md`, `REVIEW.md` v `CONSTRUCTIVE-3/`. Dále veřejné předchůdce
v `main` `a8482d06`: `probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/CONTRACT.md`
a jeho `WORD535.txt` (SHA-256 `ca6bdd7a…c916b`, ověřeno),
`probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/PROOF.md` a `PREREG.md`,
řádky s definicí `G_t` a `X` v `probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/`.
Pro konvence jsem přečetl `PREREG.md` dřívějšího posudku
`notes/C-RELATIVE-CONTACT-WORKBANK-REUSE-REVIEW-1/` a výpis jmen funkcí jeho
`review.py`; jeho kód nepřebírám a nečetl jsem ho.

**Expozice výsledků:** tělo PR a zpráva zadavatele uvádějí 95 kontaktů,
15 slotů, účet stocku 80, sedm přidaných slotů, `39+25k` slotů, `27345k`
kontaktů, `5(k-1)` SWAPů, 19 cyklů, 2 597 775 kontaktů, 50 SWAPů,
114 hraničních kontrol, seznam 14 případů, „tři první běhy prošly“ a
„3790 primitivních řezů“ (PREREG PR). Čísla proto nejsou slepé predikce;
níže je přepočítávám od nuly a tam, kde jsou věcná, je dávám za kritérium.
Nic z toho mi neříká, jak vypadají autorovy výstupy ani jejich hashe.

Tento soubor je sepsán a commitnut před prvním spuštěním `review.py`.

## 1. Kontrakt odvozený z textu (rovnice, ne očekávání)

- `O = Z[j]`, `Phi_5(j) = 0`, báze `(1,j,j^2,j^3)`; `rho = j^2`, `u = 1-j`,
  `B = 1-rho`, `J = 1+rho`, `X = 1+j-2j^3`, `phi = -j^2-j^3`,
  `phi^2 = phi+1`; `Q(z) = (5 sum z_i^2 - (sum z_i)^2)/2 = Tr(h(z))`,
  `h(z) = z conj(z) = a+b phi`, `Q = 2a+b`; `eps(z) = sum z_i mod 5`
  (CONTRACT §1).
- Kontakt `C(a,b)`: není-li `a-b` v `2O`, identita; jinak
  `s=(a+b)/2`, `d=(a-b)/2`, `(a,b) -> (s+rho d, s-rho d)`; `C^5 = id`,
  `C^-1 = C^4`; SWAP celých slotů je dodaná involuce (CONTRACT §1).
- Vstupy `I_t = (u+tB, u-tB, 0, 0, X, 2, J, -J)`, `t=-2..2`; `G_t` je prvních
  šest; cíl hodin na slotech 6,7 je `(rho^(t+2) J, -rho^(t+2) J)`
  (CONSTRUCTIVE-3/PROOF §1).
- Stock: `a_1=u, a_2=u-JB, a_3=u-B`; `x_-2=u-JB, x_-1=u-B, x_0=u,
  x_1=u+rho B, x_2=u+rho JB`; `d_s = -B x_s/J` pro `s=-1,0,1,2`;
  sloty 8..10 `a_1..a_3`, 11..14 `d_-1..d_2`; brána `g` = slot 5 (hodnota 2),
  registr výšky `x` = slot 0 (PROOF §1).
- Slovo: `P = C(0,8) C(0,9) C(0,10)`; `M_s = C(x,d_s) C(d_s,g)` na slotech
  `(0, 12+s, 5)`; `E = C(5,7)`, `T = C(6,7)`, `W_p = E T^(5-p) E^4 T^p`;
  `M_s^-1 = C(d_s,g)^4 C(x,d_s)^4`; `P^-1 = C(0,10)^4 C(0,9)^4 C(0,8)^4`;
  `A = P [prod_(s=-1..2) M_s W_(s+2) M_s^-1] P^-1`, 95 kontaktů, inverze 380
  (PROOF §2–§5).
- Cílový koncový bod: `A(I_t, Z) = (G_t, rho^(t+2)J, -rho^(t+2)J, Z)` pro
  všech pět `t` (PROOF §5, PREREG PR).
- Předpovědi: tabulka stocku v PROOF §6 (sedm hodnot, `h`, `Q`),
  `E_Z=80`, `H_Z=33+14phi`, `Sigma_Z=(-4,-10,-6,-10)`, `-B/J = 1+2j+2j^2`,
  `h(B/J)=3+4phi`, `h(x_-1)=h(x_0)=3-phi`, `h(x_1)=7-4phi`,
  `h(x_2)=10-5phi`, `x_2=(1-j)^2`; 15slotová příprava `Q=119+10t^2`,
  `H=52+15phi+(4+2phi)t^2`; 8slotový vstup `Q=39+10t^2`, residua
  `(0,0,0,0,0,2,2,3)` (CONTRACT §2, PROOF §6).
- Starý aparát (VARIABLE-ARRIVAL CONTRACT, WORKBANK PROOF §5): 31 slotů
  `I(n,r) = (Y_n, X_r, 0, u, 0, 0, w, 0, M_empty, M_empty)` s `w=1+rho`
  (= naše `J`), `b=1+rho^2`, `Y_n = F^n(0,2,0)`, `F = C(0,1)C(1,2)`,
  `X_r = (rho^r w, -rho^r w)`, `M_empty=(-b,b)^5`, `M[p]` otáčí pár `p`
  o `rho`. Slovo `S` z bloků `O1, A0, Bc, O2, E_c, L_p, SCAN_q, W_A, W_B,
  D, V, R, S = R F^-1 R F F T`, `|S|=535`, totožné s `WORD535.txt`;
  `W = S^10`; `W I(n,r) = (Y_(n+10), X_r, 0,u,0,0,w,0, M[-r], M[-r-Delta_n])`,
  `Delta_0=1, Delta_1=8`.
- Kopírovač `W6 = C14 C14 C45 C14 C14 C14 C16 C16 C16 C16 C14 C16`
  (one-based místa), `K(a,d)` = `W6` pro `p=0..4`, `q=p+1 mod 5`, místa
  `(a+2p,a+2p+1,a+2q,a+2q+1,d+2p,d+2p+1)`, 60 kontaktů;
  `U(a,d) = W K(11,a) K(21,d) W^-1`, 26870 kontaktů (WORKBANK PROOF §3, §6).
- Sestava (CONTRACT §4, PROOF §6 s `h=7`, `c=95`, `s=0`): adresy
  0..30 starý aparát; 31..36 `G_t`; 37..43 stock; 44..43+20k archivy po
  etapách (A_i na 44+20i, B_i na 54+20i); poté kazety po pěti slotech,
  `k-1` kusů. Lokální porty `A`: `(31,32,33,34,35,36,3,4)` a dále
  `37..43`. Mezi etapami `i` a `i+1` SWAP `(0,1,2,31,32)` s pěti adresami
  kazety `i` v zobrazeném pořadí. Program `A U_i A^-1` pro `i=1..k`
  s `5(k-1)` SWAPy; `N=39+25k`; kontaktů `27345k`; inverze `109380k`;
  `E_total=177+78k+10 sum t_i^2`,
  `H_total=70+37phi+k(30+18phi)+(4+2phi) sum t_i^2`,
  `Sigma_total=(1+4k,-9-2k,-6,-12)`; společná pomocná příprava `39+20k`
  slotů s účtem `177+60k`; dekodér jen z archivů:
  `d = p_A - p_B mod 5`, `d=1 -> n=0`, `d=3 -> n=1`, `r=-p_A`, `t=r-2`.
- Případy sestavy (PREREG PR): všech deset `k=1` vstupů `(n,t)`, dále
  `((0,-2),(1,2))`, `((1,-1),(0,1))`, `((0,0),(1,0))`,
  `((0,-2),(1,2),(0,0))`; 14 případů, 19 cyklů.
- Analytické výroky kořenového PROOF: F16 fakta (`J=u^2`, `u^3=j^4`,
  `u` řádu 15, `u/J` mimo `<rho>`), nutné podmínky oddělení stop
  (sousední výšky mají různé stopy; aspoň tři stopy; při úplném
  nedemoličním koncovém bodu všech pět stop různých).

## 2. Zmrazené vlastní konvence

K1 Prvek `O` je čtveřice `(v0,v1,v2,v3)`; dvě násobení (redukce modulo
   `Phi_5`, cyklická konvoluce délky 5) se kříží. `h` ze součinu
   `v conj(v)`, ne ze vzorců; `Q` uzavřeným tvarem i jako `Tr(h)`.
K2 Kontakt přesně podle §1: `C(i,k)` dá `s+rho d` slotu `i` a `s-rho d`
   slotu `k`, `d=(slot_i - slot_k)/2`. Slova chronologicky zleva doprava,
   adresy nulové. Inverze slova = obrácené pořadí, každý kontakt čtyřikrát;
   SWAP zůstává SWAP. Primitivní řez = jedna aplikace (i odmítnutá).
K3 Invarianty: na každém primitivním řezu kompilátoru a všech kontrolních
   běhů R04–R07 kontroluji součet, `H`, `Q` a residua celého stavu. V sestavě
   (R10–R11) kontroluji na každém kontaktu párové invarianty (součet páru,
   `Q` páru, `h` páru, obě residua) a úplné invarianty stavu na pojmenovaných
   hranicích; každý kontakt se skutečně provede a počítá. Cache rozlišných
   párových přechodů je povolena, každá položka se spočte doslovně včetně
   párových invariantů.
K4 `S` skládám z bloků WORKBANK PROOF §5 (nulové adresy) a porovnávám
   kontakt po kontaktu s `WORD535.txt` (one-based → nulové; orientace
   `C(a,b)` se bere z řádků souboru). Tvar `WORD535.txt` čtu jen jako
   zdrojová data, jeho hash ověřuji proti CONTRACT.
K5 Pořadí hranic v jedné etapě: start, po `A`, po `W`, po `K_A`, po `K_B`,
   po `W^-1`, po `A^-1`, po SWAP-bloku (je-li). Dekodér čte jen archivní
   sloty.
K6 Serializace fingerprintů (jen moje): prvek `a0,a1,a2,a3`; stav = sloty
   v rostoucí adrese spojené `;`; slovo = tokeny `Ci,k` / `Si,k` spojené `;`;
   stopa = řetězec `A`/`R` délky slova. SHA-256 hex nad UTF-8.
K7 BFS předchůdce (R15): uzel = pětice úplných 8slotových stavů v pořadí
   `t=-2..2`; hrany `(a,b)`, `0<=a<b<8`, lexikograficky; identity se
   přeskakují, přesně shodné pětice se deduplikují (první předchůdce);
   hloubka ≤ 6, strop navštívených 20000 včetně kořene, při stropu se
   další neviděné dítě nevkládá ani netestuje; cíl = sloty 6,7 rovny
   `(rho^(t+2)J, -rho^(t+2)J)` u všech pěti. Výsledek je pozorování.
K8 Mutanty (R14) běží mimo hlavní běh na kopii konfigurace.

## 3. Kontroly (PASS právě když platí kritérium; jinak FAIL, exit 1)

R01 Prstenec a F16. `Phi_5(j)=0`, `phi^2=phi+1`, `J(-rho-rho^3)=1`,
    `rho^5=1`; obě násobení shodná na všech 6561 párech `{-1,0,1}^4` a na
    `{-2..2}^4 × {j,rho,u,B,J,X,phi}`; `Phi_5` nad `F_2` bez kořene a
    nedělitelný `t^2+t+1`; v `O/2O` (16 tříd) žádný součin nenulových
    tříd není nulový; obraz `rho` má řád 5; `u` má řád 15, `u^3 = j^4`,
    `J = u^2`, `B = J` mod 2, `u J^-1` není v `<rho>` mod 2, `w^3=rho^4`
    a `w` není v `<rho>` mod 2, `b = w^2` mod 2; `h(u)=3-phi`,
    `h(B)=2+phi`, `h(J)=2-phi`, `h(X)=5+5phi`, `h(2)=4`,
    `h(1+rho^2)=1+phi`; `Q(u)=Q(B)=5`, `Q(X)=15`, `Q(2)=8`, `Q(J)=3`,
    `Q(b)=3`; `Q` uzavřeným tvarem == `Tr(h)` na `{-2..2}^4`; `Q>0` pro
    nenulové.
R02 Kontaktní zákon. Na všech 65536 párech z `{-1,0,1,2}^4`: připuštěn
    právě když rozdíl sudý po složkách; odmítnutý je identita; připuštěný
    zachovává součet páru, `Q` páru, `h` páru a obě residua; `C^5=id`;
    `C^4` inverze; `C(a,b)` a `C(b,a)` dávají tutéž dvojici hodnot
    (orientace nemění párové zobrazení); rovné vstupy jsou pevné.
R03 Konstanty stocku. `x_s` dle §1; `J d_s = -B x_s` (přesné dělení);
    sedm hodnot slotů 8..14 == tabulka PROOF §6 včetně `h` a `Q`;
    `E_Z=80`, `H_Z=33+14phi`, `Sigma_Z=(-4,-10,-6,-10)`; `-B/J=1+2j+2j^2`;
    `h(B/J)=3+4phi`; `h(x_-1)=h(x_0)=3-phi`, `h(x_1)=7-4phi`,
    `h(x_2)=10-5phi`; `x_2=(1-j)^2`; pro všech pět `t`: `Q(I_t)=39+10t^2`,
    residua `I_t` `(0,0,0,0,0,2,2,3)`, `Q(I_t,Z)=119+10t^2`,
    `H(I_t,Z)=52+15phi+(4+2phi)t^2`; `Q(u+tB)+Q(u-tB)=10+10t^2`.
R04 Separátor. Pro každé `t`: stopa `P` je přesně (sudá `t` připouští
    `C(0,8)`; `t=±2` připouští `C(0,9)`; `t=±1` připouští `C(0,10)`; vše
    ostatní odmítá); po `P` je slot 0 roven `x_t`; parity `x_t` mod 2 jsou
    v pořadí `t` rostoucím `1+j^2+j^3, j+j^2, 1+j, j^3, 1+j^2`, pět různých
    nenulových tříd; `P^-1` po `P` vrátí přesně vstup; invarianty K3.
R05 Značky. Pro všech 20 dvojic `(t,s)` na stavu po `P`: `t≠s` → oba
    kontakty `M_s` odmítnuty, stav beze změny; `t=s` → první připuštěn,
    slot `d_s` je poté přesně 0 a slot 0 je `x_s+d_s`, druhý připuštěn a
    dá `(d_s,g)=(B,J)`; `M_s^-1` ihned po `M_s` vrátí stav; invarianty K3.
R06 Zapisovač. 24 případů: aktivní `g=J`, hodiny `(J,-J)`, `p=1..4`: `E`
    připuštěn, všech `5-p` kontaktů `T` odmítnuto, `E^4` vrátí `g=J` a
    hodiny fáze 0, `T^p` dá `(rho^p J,-rho^p J)`, brána `J`; neaktivní
    `g=2`, hodiny fáze `r=0..4`, `p=1..4`: všech deset kontaktů kromě `T`
    odmítnuto, hodiny po slově přesně fáze `r`, brána 2; invarianty K3.
R07 Kompilátor. Slovo `A` má přesně 95 kontaktů a je pro všech pět `t`
    doslova stejné; pro každé `t`: koncový bod
    `(G_t, rho^(t+2)J, -rho^(t+2)J, Z)` po složkách, pouze sloty 6,7
    změněny; invarianty K3 na všech 95 řezech a 380 řezech literální
    inverze, inverze vrátí přesný vstup; celkem **2375** řezů; stopy pěti
    vstupů jsou po dvou různé, zvlášť u sousedních `t`; počet připuštěných
    kontaktů na vstup a fingerprint stop a koncových bodů (pozorování).
R08 Formule sestavy. Z mých vlastních sestavených počátečních stavů
    pro všech 14 případů: `N=39+25k`; `E_total=177+78k+10 sum t_i^2`;
    `H_total=70+37phi+k(30+18phi)+(4+2phi) sum t_i^2`;
    `Sigma_total=(1+4k,-9-2k,-6,-12)`; pomocné sloty (vše mimo `5k`
    vstupních) mají společný stav pro všechny případy téhož `k` s účtem
    `177+60k`; každý archivní pár účet 60; délka dopředného programu
    `27345k` kontaktů a `5(k-1)` SWAPů, inverze `109380k` a `5(k-1)`.
R09 Slovo `S`. Moje `S` z bloků má 535 kontaktů a je kontakt po kontaktu
    (včetně orientace) rovno `WORD535.txt`; délky bloků
    `L_p=10, SCAN=80, E_c=10, W_A=W_B=105, D=9, V=23, R=261`; `|W|=5350`,
    `|W^-1|=21400`, `|K|=60`, `|U|=26870`; `K(11,a)` na `(M[r],M_empty)`
    dá `(M[r],M[r])` pro všech pět `r` s 41 připuštěnými z 60.
R10 Stopky. Pro všech deset `(n,r)`: `W I(n,r)` == uzavřený tvar
    `(Y_(n+10 mod 9), X_r, 0,u,0,0,w,0, M[-r], M[-r-Delta_n])`;
    `W^-1` vrátí `I(n,r)`; úplné invarianty na hranicích každého `S`.
R11 Sestava. Pro 14 případů (19 cyklů): doslovný dopředný program a
    doslovná inverze; na hranicích K5 úplný stav == odvozená předpověď
    (po `A`: hodiny `X_(t+2)`, zbytek startu; po `W`: pracovní banky
    `M[-r], M[-r-Delta_n]`, `r=t+2`, zdroj `Y_(n+10)`; po kopiích: archivy
    etapy = tyto záznamy, pracovní banky obnoveny; po `W^-1`: jádro
    `I(n,r)`; po `A^-1`: hodiny `(J,-J)`, `G_t`, stock; po SWAPech: další
    vstup v jádře, předchozí zaparkován); dříve dokončené archivy jsou na
    všech pozdějších hranicích beze změny; dekodér jen z archivů vrátí
    přesnou posloupnost `(n_i,t_i)`; úplná inverze vrátí počáteční stav;
    residua vyměňovaných slotů jsou před každým SWAPem rovna; úplné
    invarianty (součet, `H`, `Q`, residua) na každé hranici; součet
    kontaktů dopředu i zpět přes 19 cyklů **== 2597775**, SWAPů **== 50**;
    počet hraničních kontrol a fingerprint finálních stavů (pozorování).
R12 Čerstvost. Počet čerstvých archivních párů po etapách je `k, k-1, …, 0`;
    pracovní banky jsou po každé etapě `M_empty`; žádný archiv není
    `M_empty` na konci dopředného programu.
R13 Analytika kořenového PROOF v konečném rozsahu. (a) sudé `t` ve
    třídě bez stocku: `u`, `rho^b J` a 0 jsou po dvou různé mod 2 pro
    všechna `b`; (b) pro `t` a `t+1`: `2Q(B)=10`, `Q(1-rho^2)=5`,
    `J(1-rho)=1-rho^2`, `39+10t^2 ≠ 39+10(t+1)^2` pro `t=-2..1`;
    (c) stopy `A` splňují nutnou podmínku (b) a mají aspoň tři třídy.
R14 Citlivost. Mutant (a): hodinové semeno `(J,J)` místo `(J,-J)` musí
    porušit koncový bod R07 aspoň u jednoho `t`; mutant (b): `a_2`
    nahrazeno `u+JB` musí porušit R07. PASS právě když oba detekovány.
R15 BFS předchůdce dle K7 (pozorování): výsledek `FOUND` /
    `INCONCLUSIVE` / `NO_GOAL_IN_COMPLETE_ORBIT`, počet navštívených,
    dosažená hloubka. Pokud by můj BFS našel svědka v prohledaném prefixu,
    je to DIFF-REAL vůči deklarovanému INCONCLUSIVE (kořenový README);
    jinak se porovná jen klasifikace a počty.

## 4. Závazný rozsah běhu a výstup

Plný rozsah bez vzorkování. `review.py` čte jediný soubor:
`probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/WORD535.txt` z kořene
repozitáře (veřejný fixture v `main`, nikoli soubor PR); nic nezapisuje,
nepoužívá síť, náhodu ani float. Příkaz z kořene repozitáře:

```sh
env LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/review.py
```

Tiskne `Rxx PASS|FAIL …`, pozorované počty a fingerprinty, poslední řádek
`RESULT PASS` (exit 0) nebo `RESULT FAILURE` (exit 1). Bez cest, časů a
platformy. Provozní limit, který si sám dám: 900 s; překročení hlásím jako
neúplný běh, ne jako FAIL kontraktu.

Selhání se zaznamená beze změny. Oprava ověřovače je nová, samostatně
zmrazená revize; obě se uchovají. Žádné kritérium se po zmrazení nemění.

## 5. Fáze 2

1. Ověřit hashe zmrazených souborů proti GitHubu, znovu spustit `review.py`.
2. Spustit autorovy `verify.py`, `audit.py PRIMARY_STDOUT`, `assembly.py`
   a `search.py` beze změny z kořene čistého checkoutu hlavy PR, uložit
   stdout/stderr, `cmp` proti očekávaným souborům.
3. Teprve poté otevřít autorův kód, RUN.md, RESULT.md a SHA256SUMS; porovnat
   veličiny, MATCH / DIFF-CONVENTION / DIFF-REAL (`COMPARISON.json`).
4. Administrativa: `SHA256SUMS`, piny v PREREG PR, autorství a předci čtyř
   commitů, pořadí pin → výsledek v historii, `check_*`, CI log, hledání
   soukromých údajů.
5. `RESULT.md`: PASS / PASS S POZNÁMKOU / FAIL, co ověřil čí kód, co CI,
   co zůstalo neověřeno, co nezávislost je a co ne.
