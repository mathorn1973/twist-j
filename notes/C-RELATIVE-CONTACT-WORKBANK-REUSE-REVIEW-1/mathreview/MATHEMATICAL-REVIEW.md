# Matematický posudek důkazového textu PR #1879 (twist-j)

Checkout: `d6a5f77169d1027a22959c41aa5a45a783643a3e`, základ v108
`17de90b58f814238e151aac77badde6654b52627`. Posudek je nezávislý na výpočetním
posudku. Nic v repozitáři, v PR ani v kánonu nemění a žádný status nezvyšuje.
Texty PR samy sebe správně označují `NON-CANONICAL / L1`, výsledek běhu
`candidate-C` a důkazní argumenty jako kandidátské, čekající na přijetí
(PROOF.md:3-7, PREREG.md:165-167, RESULT.md:3,74-79).

## 0. Rozsah, metoda a celkový verdikt

PR mění proti základu přesně 10 souborů, všechny v
`probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/` (PREREG.md, PROOF.md,
PROVENANCE.md, README.md, RESULT.md, RUN.md, SOURCES.tsv, WORD535.txt,
EXPECTED.txt, verify.py). Ve složce `notes/` ani v `canon/` PR nic nemění;
ověřeno `git diff --name-only 17de90b..HEAD`. Předmětem tohoto posudku je
důkazový text v `.md` souborech sondy. Soubor verify.py jsem jako kód
neposuzoval ani nespouštěl; je předmětem samostatného výpočetního posudku.
Místa níže zkracuji: PRF=PROOF.md, PRE=PREREG.md, RM=README.md, RES=RESULT.md,
PROV=PROVENANCE.md, vše v adresáři sondy. Řádky kánonu cituji z checkoutu
(`canon/REGISTRY.tsv`, `canon/CANON.md`); /canon/REGISTRY.tsv je bajtově
totožný (ověřeno `cmp`).

Hodnotil jsem každé lemma v místě, kde je vysloveno, za předpokladu předchozích
vyslovených lemmat; zděděné závislosti na mezerách uvádím u jejich zdroje (§3
níže), neopakuji je u každého důsledku. Rozhodující identity jsem nezávisle
přepočítal vlastním kódem psaným jen z definic PROOF.md (okruh
Z[j]/(1+j+j²+j³+j⁴) v bázi 1,j,j²,j³, kontakt dle PRF:39-41, bloky dle
PRF:247-261), uloženým mimo výstup posudku v `/tmp/mathrev/own_check.py`;
rozhodující výstup cituji doslova v příloze A. Vlastní výpočet je nezávislá kontrola,
nenahrazuje symbolické důkazy; kde je tvrzení samo konečné, uvádím to.

**Celkový verdikt.** Matematické jádro je správné: lokální kopírovací identita,
60kontaktní kopírovač banky, čtyřmístná obstrukce, identita W na 31slotovém
jádru, cyklus U a obecná konstrukce P_k drží. Nenašel jsem žádné věcně chybné
lemma. Nalezené vady jsou: čtyři místa, kde text používá identitu bez
uvedeného odvození (polostopa Q; shoda bloků s WORD535; disjunktnost kosetů;
že zapsané slovo E_c⁻¹ je inverzí), a dvě neomezené formulace o nedotčenosti
archivů v RM/PRE, které bez omezení na dopředný program doslova nedrží, protože
literární inverzní program archivy maže. Vše, co je jen spuštěný konečný
korpus k=3 (1000 trojic), je v textech od obecného symbolického tvrzení správně
odděleno.

## 1. Tabulka všech tvrzení a lemmat

Nález: DRŽÍ / DRŽÍ S MEZEROU / NEDRŽÍ / POUZE KONEČNÝ VÝPOČET.

### 1.1 PROOF.md §1: okruh, kontakt, invarianty

| ID | Tvrzení (jedna věta) | Nález | Kde |
|---|---|---|---|
| P1.1 | Q(z)=(5Σzᵢ²−(Σzᵢ)²)/2 je celočíselná a pozitivně definitní. | DRŽÍ | PRF:26-35 |
| P1.2 | Q je kladná polostopa z·z̄, a proto zachování H dává zachování E=ΣQ. | DRŽÍ S MEZEROU | PRF:31-35,55 |
| P1.3 | Na připuštěné větvi jsou s,d,i výstup celočíselné a připuštěnost trvá (výstupní rozdíl 2ρd). | DRŽÍ | PRF:37-44 |
| P1.4 | C⁵=id, C⁻¹=C⁴ na celém párovém nosiči; diagonála i odmítnuté páry jsou pevné; každé konečné slovo je globální bijekce. | DRŽÍ | PRF:43-47 |
| P1.5 | Párová hermitovská identita dává zachování Σ a H při každém kontaktu. | DRŽÍ | PRF:49-55 |
| P1.6 | ε (zobrazení j↦1) se zachovává na každém označeném slotu; SWAP zachovává Σ,H,E a obecně permutuje označená rezidua. | DRŽÍ | PRF:55-58 |
| P1.7 | Násobení celého stavu ρ komutuje s každým kontaktem. | DRŽÍ | PRF:60-63 |
| P1.8 | Φ₅ mod 2 je ireducibilní, tedy O/2O≅F₁₆, ρ má řád 5, 1+ρᵉ≠0 mod 2 (e=1..4), zejména b≠0 mod 2. | DRŽÍ | PRF:65-70 |

### 1.2 PROOF.md §2: kód banky a lokální identita

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P2.1 | b=(0,−1,−1,−1), Q(b)=3; čerstvá i každá platná banka má E=30, součet 0, rezidua (3,2)⁵. | DRŽÍ | PRF:74-85 |
| P2.2 | Pět záznamů M[p] je navzájem různých a žádný není M_empty (ani M[0]). | DRŽÍ | PRF:83-85 |
| P2.3 | Pro (−ρᴾb,+ρǫb) je kontakt připuštěn právě když P=Q mod 5; pak obě fáze rostou o 1, i při opačném pořadí znamének. | DRŽÍ | PRF:87-91 |
| P2.4 | Tabulka hranic bloků slova W6=A²BA³D⁴AD pro (P,Q,R,S)∈{(0,0,0,0),(1,0,0,0),(0,1,0,0)} je správná. | DRŽÍ | PRF:93-112 |
| P2.5 | Počty připuštěných kontaktů v řádcích jsou 10,6,5 a admisní slova jsou AARAAAAAAARA, RRAAAARRRRAA, RRRRRRAAAARA. | DRŽÍ | PRF:114-118 |
| P2.6 | Značka v p se zkopíruje do cíle, značka v q či jinde nechá cíl čerstvý; oba zdrojové páry jsou na hranici 12 kontaktů obnoveny, uvnitř být nemusí. | DRŽÍ | PRF:120-125 |
| P2.7 | Příklad (0,0,1,1)→…→(2,1,1,2) vyvrací rozšíření tabulky na libovolné obsazené cíle; není klasifikací obsazených slov. | DRŽÍ | PRF:127-135 |

### 1.3 PROOF.md §3: 60kontaktní kopírovač banky

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P3.1 | K(a,d) je pro disjunktní banky pevně specifikováno pěti moduly W6 (q=p+1), celkem 60 kontaktů bez volby závislé na vstupu. | DRŽÍ | PRF:139-147 |
| P3.2 | K(a,d): (M[r],M_empty)→(M[r],M[r]) pro každé r∈Z/5 (indukce přes 5 modulů, zdroj obnoven na každé hranici, dřívější cílové páry nedotčeny). | DRŽÍ | PRF:149-155 |
| P3.3 | Celkový počet připuštěných kontaktů je 6+5+3·10=41 z 60, nezávisle na r. | DRŽÍ | PRF:157-159 |
| P3.4 | Globální ρ-ekvivariance dává všechny současné rotace identit (15 lokálních, 25 bankových); rotovaná čerstvá banka je ρᵗ·M_empty, ne spřažení rotovaného zdroje s nerotovaným cílem. | DRŽÍ | PRF:161-167 |
| P3.5 | Slovo používá jen 20 souřadnic, účet 60 a součet 0; zdroj je roven M[r] na všech hranicích modulů; netvrdí se neměnnost na primitivní úrovni ani zápis do obsazeného cíle. | DRŽÍ | PRF:169-173 |
| P3.6 | Literární inverze K má 240 kontaktů a obnoví vstup na každém úplném stavu; není tvrzena involučnost ani minimalita. | DRŽÍ | PRF:175-180 |

### 1.4 PROOF.md §4: čtyřmístná obstrukce

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P4.1 | Pro b≠0 neexistuje pevné slovo F kontaktů na 4 místech s F(E)=E i F(A)=T=ρE (z ekvivariance F(T)=T a bijektivity by A=T, spor). | DRŽÍ | PRF:184-197 |
| P4.2 | Závěr se týká jen doslovného kopírování s daným působením na prázdný stav; nezakazuje jiný kód, referenční pár ani 20místný one-hot kopírovač, jehož rodina není uzavřená vůči ρ. | DRŽÍ | PRF:199-204 |

### 1.5 PROOF.md §5: 31slotové čtecí zařízení

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P5.1 | Vyspellované definice slova souhlasí s deklarovaným zdrojem WORD535 a důkaz nepoužívá žádný zaznamenaný běh jako premisu. | DRŽÍ S MEZEROU | PRF:208-211 |
| P5.2 | F(Y_a)=Y_{a+1} pro všech 9 zdrojových stavů (rotace páru (u_e,w_e), odmítnutí u nuly, obrat přes (0,2)). | DRŽÍ | PRF:230-243 |
| P5.3 | T(X_r)=X_{r+1}; všechny zobrazené zdrojové i hodinové stavy jsou různé. | DRŽÍ | PRF:236-243 |
| P5.4 | Délky L_p,SCAN_q,E_c,W_A,W_B,D,V,R,S jsou po řadě 10,80,10,105,105,9,23,261,535. | DRŽÍ | PRF:245-265 |
| P5.5 | O1 posílá (prostředek zdroje,g)=(2,0) na (w,u) právě ve fázi Y₀, v ostatních odmítá a nechává g=0. | DRŽÍ | PRF:269-270 |
| P5.6 | Hraniční tabulka E_c pro (g,c,h)∈{0,u}²×{w} je správná včetně řádku (u,u,w)→(u,0,2). | DRŽÍ | PRF:271-284 |
| P5.7 | O2 při t=0 vytvoří (h,t)=(w,u) právě v řádku (u,u,w), jinak na (w,0) odmítá. | DRŽÍ | PRF:284-285 |
| P5.8 | Ve F₁₆ je w³=ρ⁴, w∉⟨ρ⟩, b≡w² mod 2, a proto jsou kosety ⟨ρ⟩w a ⟨ρ⟩b disjunktní. | DRŽÍ S MEZEROU | PRF:287-290 |
| P5.9 | Při t=u je C(3,10) na ρʳw připuštěn právě pro r=0 a mění (w,u) na (b,u₂); při t=0 odmítá pro každé r. | DRŽÍ | PRF:292-293 |
| P5.10 | Na surových hodinách a paměťovém páru (−ρᵛb,ρᵛb) je L_p identita, i pro obsazený pár (oba kontakty hodiny–paměť odmítají, paměťové C⁴ a C se ruší). | DRŽÍ | PRF:294-296 |
| P5.11 | Hradlovaný sken čerstvého páru sleduje zobrazenou posloupnost (b,−b,b)→…→(b,−ρb,ρb); druhý blok odmítá, neb (1+ρ⁴)b≠0 mod 2. | DRŽÍ | PRF:298-307 |
| P5.12 | Pět skenových kroků potká fázi 0 právě jednou, při p=−r; hradlovaná čerstvá banka se stane M[−r]; neaktivní sken zachová čerstvou i platně obsazenou banku; zapsané páry se v témže skenu znovu nenavštěvují. | DRŽÍ | PRF:307-311 |
| P5.13 | Po SCAN_q obnoví O2⁴ a E_c⁻¹ přesně (g,c,h,t); změní se jen vybraná čerstvá banka. | DRŽÍ S MEZEROU | PRF:249,313-314 |
| P5.14 | D při pomůcce w prohodí (u,0)↔(0,u) a fixuje (0,0); při w₂ fixuje všechny tři (uvedené posloupnosti stavů jsou správné). | DRŽÍ | PRF:316-327 |
| P5.15 | V prohodí tokenový pár právě když g=u a obnoví (g,h); V(7,8)V(6,7) cyklí A→B→skip→A; O1⁴ obnoví zdroj a g. | DRŽÍ | PRF:327-332 |
| P5.16 | Úplné R obnoví předložený zdroj, hodiny, g=t=0, h=w; mimo fázi 0 nemění selector ani banky; ve fázi 0 píše M[−r] jen do vybrané čerstvé banky (skip: nikam) a cyklí selector, na dosažitelné rodině. | DRŽÍ | PRF:334-340 |
| P5.17 | Přesný seznam událostí v 10 krocích je dle tabulky pro s=0 i s=1 (po 3 událostech, čtvrtá není); Δ₀=1, Δ₁=8. | DRŽÍ | PRF:342-352 |
| P5.18 | W=S¹⁰ (5350 kontaktů) splňuje W·I(s,r)=(Y_{s+10},X_r,0,u,0,0,w,0,M[−r],M[−r−Δ_s]) pro všech 10 vstupů, ovladače opět ready. | DRŽÍ | PRF:352-356 |
| P5.19 | Záznamy trvají na hranicích R a S dopředného stupně (ne uvnitř čtení); literární W⁻¹ má 21400 kontaktů a obnoví I(s,r) právě z tohoto obsazeného stavu. | DRŽÍ | PRF:358-361 |

### 1.6 PROOF.md §6: jeden cyklus zápisu, kopie a uncompute

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P6.1 | U(a,d)=W·K(11,a)·K(21,d)·W⁻¹ má 5350+60+60+21400=26870 kontaktů. | DRŽÍ | PRF:365-372 |
| P6.2 | U(a,d): (I(s,r),M_empty,M_empty)→(I(s,r),M[−r],M[−r−Δ_s]) pro každé (s,r)∈{0,1}×Z/5. | DRŽÍ | PRF:374-384 |
| P6.3 | Obnoveny jsou tytéž adresy pracovních bank 11..30 a počáteční zdroj/hodiny, ne dopředně vyvinuté hodnoty; žádný externí reset, kopie zůstávají v odlišných počítaných souřadnicích. | DRŽÍ | PRF:386-390 |
| P6.4 | Identita se rozšíří o libovolný nedotčený úplný komplement včetně starších archivů; použité archivní banky neobnovuje do čerstvosti. | DRŽÍ | PRF:392-394 |
| P6.5 | Ve dvou kopiích je přesně 82 připuštěných kontaktů; žádný celkový admisní počet pro W ani U není potřeba. | DRŽÍ | PRF:395-396 |

### 1.7 PROOF.md §7: pevný rozvrh pro předem daný konečný počet vstupů

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P7.1 | Pro k≥1 zafixované předem dávají adresace jádra, archivů A_j,B_j (j=0..k−1) a kazet (j=1..k−1) přípravu na doméně Iᵏ se všemi 2k archivy i pracovními bankami prázdnými a stejnými ovladači/archivy pro každou n-tici. | DRŽÍ | PRF:400-411 |
| P7.2 | P_k=U₀Π₁U₁…Π_{k−1}U_{k−1} závisí jen na k a adresaci, nikdy na hodnotách vstupů; všechny vstupy jsou přítomny od začátku, žádný post-start vstup se nepřijímá; rozvrh je dodaný, ne autonomní ovladač. | DRŽÍ | PRF:413-424 |
| P7.3 | Indukční invariant po U_j (jádro I(s_j,r_j) vč. čerstvých bank a ready ovladačů; archivy i≤j zapsané, i>j čerstvé; kazety i≤j drží předchozí obnovené vstupy, i>j původní čekající) plyne ze základny §6 a kroku Π_{j+1} následovaného U_{j+1}. Podrobně §4. | DRŽÍ | PRF:426-444 |
| P7.4 | Koncový stav je podle vzorce (jádro drží poslední vstup, archivy všechny záznamy, kazety předchozí vstupy). | DRŽÍ | PRF:446-450 |
| P7.5 | Po dokončení vlastní kopie se žádná pozdější primitiva slova P_k archivní banky nedotýká (souřadnice i adresy doslova zůstávají); zdrojová banka kopírovače je zaručena jen na hranicích modulů a W⁻¹ ji maže. | DRŽÍ | PRF:452-455 |
| P7.6 | P_k má 26870k kontaktů a 5(k−1) swapů; nezkrácená literární inverze 107480k kontaktů a 5(k−1) swapů; nejde o optimální délky ani fyzikální časy. | DRŽÍ | PRF:457-460 |
| P7.7 | Pro k=3: archivy 31..90, kazety 91..95 a 96..100, 101 slotů, 80610 kontaktů a 10 swapů dopředu, inverze 322440 a 10; korpus 10³=1000 trojic, součty trajektorií 403050000 kontaktů a 20000 swapů. | DRŽÍ | PRF:462-468 |

### 1.8 PROOF.md §8: účty a dekódování z aktuálního stavu

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P8.1 | Q(u)=5, Q(w)=Q(b)=3; zdroj E=8,Σ=2; hodiny E=6,Σ=0; ovladače E=8,Σ=2; obě banky E=60,Σ=0; tedy I(s,r) má E=82,Σ=4. | DRŽÍ | PRF:472-475 |
| P8.2 | Pro přípravu s k vstupy: slotů 31+20k+5(k−1)=26+25k, E_celkem=82+60k+14(k−1)=68+74k, Σ_celkem=4+2(k−1)=2(k+1). | DRŽÍ | PRF:477-481 |
| P8.3 | 5k vstupních adres přispívá 14k; zbylých 26+20k auxiliárních adres má společný počáteční stav a účet 68+60k; na každém vstupu je zdrojová souřadnice 2 nulová, mění se jen 4 souřadnice. | DRŽÍ | PRF:483-487 |
| P8.4 | Pro k=3: E=290, Σ=8, vstupních 15 adres/účet 42, ostatních 86 adres/účet 248, mění se 12 hodnot; jsou to počáteční účty, ne „spálená energie“. | DRŽÍ | PRF:489-492 |
| P8.5 | Rezidua: Y_a (0,2,0), X_r (2,3), ovladače (0,0,0,0,2,0), banky (3,2)⁵; na připravované rodině nechávají i reload-swapy úplný označený vektor reziduí beze změny; nic není z účtu vynecháno. | DRŽÍ | PRF:494-501 |
| P8.6 | Čtečka porovná 10 aktuálních souřadnic s pěti přesnými vzory M[p] a prázdnou/neplatnou banku odmítne (prázdná není label 0); pro labely (a,a') je d=a−a'=Δ_s, s dle d∈{1,3}, r=−a; jiný rozdíl je mimo kontrakt. | DRŽÍ | PRF:503-514 |
| P8.7 | Aplikace čtečky na všech k párů obnoví celou uspořádanou vstupní n-tici; archivní čtení je injektivní na všech 10ᵏ vstupech. | DRŽÍ | PRF:515-516 |
| P8.8 | Podmíněná mez 5ᵇ≥10ᵏ pro čtení jen z b označených pětistavových bank bez jiného data/stavu přítomnosti; k=3 vyžaduje ≥5, konstrukce dává 6 (obecně 2k), což je horní mez, ne minimum, a ne věta nemožnosti pro jiné kódy. | DRŽÍ | PRF:518-529 |
| P8.9 | Po U_j zbývají v dopředném prefixu 2(k−j−1) čerstvých archivních bank; nejde o globálně monotónní veličinu na nosiči, inverze archivy obnoví a žádná konečněstavová ireverzibilita se neodvozuje. | DRŽÍ | PRF:531-537 |

### 1.9 PROOF.md §9 a ostatní soubory sondy

| ID | Tvrzení | Nález | Kde |
|---|---|---|---|
| P9.1 | Rozsah §9 (rodina pevných konečných rozvrhů na explicitně fondovaných nosičích; univerzální indukce vs audit k=3; výslovný seznam: žádná syntéza surového vstupu, post-start vstup, kompilace swapů jen kontakty, obnova všeho při zachování záznamů, neomezeně znovu použitelný konečný archiv, minimum, nejkratší program, native-U, autonomie, měřená energie/čas/výskyt) je v souladu s důkazem. | DRŽÍ | PRF:541-562 |
| R1 | Rovnice v PREREGu, kontaktní zákon, SWAP a invarianta jsou tytéž jako v PROOF §1; globální O-linearita se netvrdí. | DRŽÍ | PRE:31-43 |
| R2 | S je 535kontaktní v108 slovo vůči nezměněnému WORD535 (uveden SHA-256), W=S¹⁰, inverze obrácením pořadí a C⁴, bez zkracování. | DRŽÍ S MEZEROU | PRE:46-52 |
| R3 | W6/K definice, K má 60 kontaktů, dvě K stojí 120 kontaktů na pokus, zdroj má jednu značku a cíl je prázdný. | DRŽÍ | PRE:54-62 |
| R4 | Třístupňový rozvrh (cíle 31+20h, swapy (i,91+5h+i)), celkem 80610/10 dopředu a 322440/10 inverzně, žádná vstupní volba hran či adres. | DRŽÍ | PRE:64-73 |
| R5 | Nosič O¹⁰¹, účty ovladače 8, banky 30, vstupy 14, auxiliárních 86 slotů/248, vstupních 15/42 (12 se mění), celek 290/Σ8, všech 8 bank zpočátku prázdných, 1000 trojic. | DRŽÍ | PRE:77-91 |
| R6 | Žádné přiřazení během vývoje; po 3 stupních jádro drží vstup 3 a kazety vstupy 1,2 v původních přípravách, všechny záznamy zůstávají. | DRŽÍ | PRE:93-98 |
| R7 | Predikce záznamů (M[−r],M[−r−Δ_n]), zdroje Y_{n+10}, hodin X_{r+10}, obnova bank na hranicích modulů (ne vnitřně), kopírovač není involuce, inverze 240. | DRŽÍ | PRE:102-110 |
| R8 | Dříve dokončené archivy nejsou „žádnou následnou primitivou“ adresovány; čtečka musí z 6 bank obnovit 1000 trojic bez pracovních bank/zdroje/kazet/labelů. | DRŽÍ S MEZEROU | PRE:112-118 |
| R9 | Celostátní inverze záměrně zruší záznamy a obnoví i 6 prázdných archivů, není retenční reset; počet čerstvých párů v dopředném protokolu je 3,2,1,0. | DRŽÍ | PRE:120-124 |
| R10 | Předepsaný vyčerpávající inventář ověřovače (1000 dopředných + 1000 inverzních trajektorií, 403050000 kontaktů, 20000 swapů) je jako důkaz jen konečný výkon na korpusu k=3, ne obecný důkaz pro k. | POUZE KONEČNÝ VÝPOČET | PRE:126-154 |
| R11 | Úspěšný běh podporuje jen candidate-C; PROOF dává kandidátské obecné argumenty k nezávislému přijetí; vzorce 26+25k a 68+74k s 2k čerstvými bankami; žádný pevný nosič pro neomezenou historii; kapacitní mez podmíněná. | DRŽÍ | PRE:165-177 |
| A1 | Souhrn v README tří pokusů jedním programem na 101 slotech pro 1000 trojic se dvěma znovu použitými pracovními bankami je věcně správný. | DRŽÍ | RM:6-11 |
| A2 | „Žádný zadržený archiv není vymazán ani znovu učiněn čerstvým“ bez časového omezení. | NEDRŽÍ | RM:13-17 |
| A3 | Odrážky „real advance“ včetně „proved family for every specified finite horizon“ přeceňují formálně stav před přijetím (věcně kryto PRF §7 až na mezery §3 níže). | DRŽÍ S MEZEROU | RM:27-35,37-41 |
| A4 | Záporný rozsah v README (žádný neomezený provoz na konečném nosiči, regenerace, autonomie, syntéza, contact-only swapy, native-U, monotonie, termodynamika; délky 12/60 jsou horní meze) je správný. | DRŽÍ | RM:43-49 |
| V1 | PASS hlášené v RESULTu pro všech 1000 trojic (obnova jádra, parkování vstupů, dekódování ze 6 bank, 1000 inverzí) je vykázaný konečný běh verify.py na korpusu k=3, ne matematický důkaz pro jiné k; v tomto posudku nespouštěn. | POUZE KONEČNÝ VÝPOČET | RES:3-35 |
| V2 | Počty v RESULTu kontrolních bodů a trajektorií (60000/30000/30000/30000/6000/3000/2000/9000; 80610,322440,403050000,20000; 86 map/27 hodnot) jsou aritmeticky konzistentní; jejich výkon je konečný běh, zde neověřen. | POUZE KONEČNÝ VÝPOČET | RES:31-44 |
| V3 | Oddělené kontroly 40 rotovaných kopií (8400 kontaktů), 3 mezních případů (960) a zdrojového 9cyklu (18) jsou konečné kontroly téhož běhu. | POUZE KONEČNÝ VÝPOČET | RES:46-50 |
| V4 | Účty 290, Σ=8, H=108−74j²−74j³, auxiliárních 248, vstupů 42, pracovních bank 60, archivů 180 (beze změny záznamem) jsou správné (nezávisle přepočteno, §6). | DRŽÍ | RES:52-56 |
| V5 | Hashe slov a koncového digesta v RESULTu jsou výstupní/custody hodnoty běhu, ne matematická lemmata; zde nepřepočítávány. | POUZE KONEČNÝ VÝPOČET | RES:58-65 |
| V6 | Rozhodovací plocha správně odděluje provedený korpus k=3 od kandidatní indukce pro každé specifikované k a netvrdí přijetí ani změnu kánonu. | DRŽÍ | RES:69-84 |
| V7 | Čerstvá archivní kapacita klesne na hranicích tří cyklů z 6 bank na 0 a vše ostatní (regenerace, neomezený provoz aj.) zůstává mimo výsledek. | DRŽÍ | RES:86-92 |
| S1 | Kvalifikace v PROVENANCE: obstrukce předpokládá b≠0; C⁵=id, ale ne každý připuštěný stav má nejmenší periodu 5 (diagonála). | DRŽÍ | PROV:36-38 |
| S2 | Žádné nejkratší 12/60 ani všekódové tvrzení se neodvozuje; „čtyřslotová obstrukce“ má algebraický důkaz bez BFS závislosti. | DRŽÍ S MEZEROU | PROV:43-48 |
| W1 | WORD535.txt v sondě je bajtově týž soubor jako v108 zdroj a jeho 535 párů je doslova slovo S postavené z bloků PRF §5 (ověřeno vlastním parsováním a sha256sum/cmp). | DRŽÍ | WORD535.txt:1-48; PRE:47-49 |
| W2 | RUN.md, SOURCES.tsv a EXPECTED.txt obsahují custody/hash/výstupní záznamy tohoto běhu bez dalších matematických lemmat; v tomto posudku nehodnoceny jinak než W1/V5. | POUZE KONEČNÝ VÝPOČET | RUN.md:1-47; SOURCES.tsv:1-10; EXPECTED.txt:1 |

## 2. Každý nález kromě DRŽÍ bez výhrad: mezera a co ji zavře

### P1.2 (PRF:32-35,55): polostopa Q je použita bez odvození

Text definuje Q vzorcem a hlásí „Q is the positive half-trace of
z·conjugate(z)“, načež z párové identity pro H usoudí „Thus H and E are
preserved“ (PRF:55). Párová identita sama dokazuje H, nikoli E; přechod
E=Tr(H)/2 stojí na neuvedené rovnosti Q(z)=Tr_{Q(j)/Q}(z·z̄)/2. Rovnost je
pravdivá (vlastní kontrola stopové formy: příloha A); v textu je to mezera.
Zavře ji buď krátký výpočet stopové formy v bázi 1,j,j²,j³, nebo výslovná
citace RELATIVE-CONTACT-INTEGRAL-LAW [T] (canon/REGISTRY.tsv:595;
canon/CANON.md:13584), kde je zachování účtu před i po stopě dokázáno. Bez
toho jsou výroky o Q(ρz)=Q(z) (PRF:81-82) a všechny E-účty formálně
neukotvené; věcně jsou správné.

### P5.1 a R2 (PRF:208-211, PRE:46-49): shoda bloků s WORD535 je tvrzena, ne ukázána

Matematický důkaz §5 je veden pro slovo S *definované* bloky PRF:247-261.
Že toto S je doslova v108 slovo v souboru WORD535.txt, je přepisní (transkripční)
tvrzení o seznamu 535 párů, které text důkazu neobsahuje; PREREG je deleguje
na ověřovač („checked contact by contact against the unchanged WORD535.txt“).
To je věc konečného výpočtu, ne symbolického kroku. Mezera v textu je
uzavřitelná přesně a nezávisle: vlastní parsování WORD535.txt a doslovné
porovnání se seznamem S z bloků dalo `exact literal == S from PROOF blocks:
True` (příloha A), soubory jsou bajtově identické s v108 zdrojem
(sha256 `ca6bdd7a…c916b`, příloha A). K uzavření v PR stačí tuto kontrolu
výslovně deklarovat jako součást důkazní identifikace slova (což PREREG pro
ověřovač dělá); samotná PROOF.md by neměla shodu prezentovat jako důkaz,
nýbrž jako identifikaci ověřenou konečným porovnáním seznamu.

### P5.8 (PRF:287-290): krok „tedy kosety jsou disjunktní“ není rozepsán

Z w∉⟨ρ⟩ samotného disjunktnost ⟨ρ⟩w ∩ ⟨ρ⟩b neplyne; je nutný mezičlánek
b≡w² (mod 2), tedy w·b⁻¹≡w⁻¹ (mod 2), takže společný prvek kosetů by dal
w∈⟨ρ⟩. Text obě fakta uvádí v jednom odstavci, ale spojení nevypíše. Rovněž
odvození v=3 z w=ρᵛ kubením používá char. 2 při krácení 2ρ³ v Φ₅(ρ)=0, což
není řečeno. Zavře jedna věta s výše uvedenými rovnostmi ve F₁₆. Věcně drží
(vlastní výpočet ve F₁₆: příloha A). Na tomto lemmatu stojí odmítání
hodin–paměť v L_p (P5.10) a z něj sken (P5.12).

### P5.13 (PRF:249,313-314): že zapsané slovo E_c⁻¹ je inverzí E_c, není odvozeno

Zápis E_c⁻¹=B_c·A₀·B_c⁴·A₀⁴ (PRF:249) není nezkrácená literární inverze
(tou by bylo 40 kontaktů); rovnost se skutečnou inverzí používá C⁵=id na
jedné hraně k redukci B¹⁶=B, A¹⁶=A v obráceném pořadí. Text identitu používá
k obnově (g,c,h,t) po skenu (PRF:313). Zavře ji jedna věta s redukcí mocnin,
resp. přímé ověření působení na relevantních stavech. Věcně drží (vlastní
kontrola skládání na 50 náhodných stavech i na tabulce E_c: příloha A).
Důsledek P5.13, a tedy W_A,W_B v P5.16, na ní dědičně stojí.

### R8 a A2 (PRE:113-115, RM:16-17): neomezené formulace o archivním nedotčení

Podrobně §5 níže. PRE:113 „never addressed by any subsequent primitive“
je zachránitelné kontextem, RM:16-17 „No retained archive is erased or made
fresh again“ doslova nedrží, protože literární inverze P₃⁻¹ archivy maže
a obnovuje do M_empty (PRE:120-121 správně říká opak pro inverzi). Oprava
je formulační, matematický obsah (retention během dopředného slova) drží.

### A3 (RM:33): „proved family“ před přijetím

Odrážka o „a proved family for every specified finite horizon“ vystavuje
kandidátský důkaz jako hotový. RM:37-38 to v dalším odstavci správně vrací
(„must accept … before any Canon fold“), ale souhrnná odrážka má znít
„a candidate proof, by induction, of a family…“. Stav po tomto posudku:
indukce v §7 je úplná (§4 níže); celek dědí mezery P1.2, P5.1, P5.8, P5.13,
které jsou po doplnění vět uzavřené. Žádné zvýšení statusu z tohoto posudku
neplyne.

### S2 (PROV:36,46-48): terminologický střet „four-slot“

PROV:36 „The four-slot no-copy argument“ a PROV:46 „The four-slot obstruction“
označují *čtyřmístnou* (dvou-párovou) obstrukci z PRF §4, kde čtyři jsou
souřadnice dvou párů. V kánonu ale „four-slot“ je vázáno na
RELATIVE-CONTACT-FOUR-SLOT-MINIMUM [T] (canon/REGISTRY.tsv:596): přesně čtyři
*auxiliární* sloty na O²⁶ a účtové meze 27/12. PR zaměnu věcně nedělá (žádnou
z mezí nepoužívá; viz §7), ale název ji omylem evokuje. Oprava: všude říkat
„four-place / two-pair obstruction“ jako v nadpisu PRF §4 (PRF:182).

### Položky POUZE KONEČNÝ VÝPOČET (R10, V1-V3, V5, W2)

Nejsou chybné, ale jejich důkazní síla je výkon konečného korpusu, ne symbolické
lemma; v tomto posudku NEBYLY spuštěny (verify.py jsem nespouštěl), takže
jejich „PASS“ jako fakt zde zůstává NEOVĚŘENO a patří výpočetnímu posudku.
Zavření v tomto ohledu neznamená dodělat důkaz v PROOF.md, nýbrž nezávisle
zreprodukovat běh (mimo rozsah zadání tohoto posudku). Moje vlastní přepočty
(příloha A) pokrývají mimo jiné všech 10 vstupů pro W a U, všech 100 párů pro
k=2 a vzorky pro k=3,4; to jsou také jen konečné kontroly a ne nahrazují
symbolické důkazy ani úplný běh pro 1000 trojic.

## 3. Co je dokázáno obecně a co jen na konečném korpusu

**Obecně symbolicky** (textem PRF, s mezerami §2): §1 pro libovolné stavy
a slova (∀a,c∈O; každá konečná posloupnost); §2 pro všechny fáze Z/5 včetně
protipříkladu, který je obecnou výpočtovou větou o fázích; §3 pro každé
r∈Z/5 a každé ρᵗ; §4 pro každé b≠0 a *každé* pevné slovo F (věta nemožnosti,
ne výčet); §5 pro všech 10 vstupů (s,r)∈{0,1}×Z/5 a dosažitelnou rodinu, ne
pro libovolné obsazené přepsání (PRF:338-340 to správně ohraničuje a můj
přepočet potvrzuje, že hradlovaný sken obsazené banky obecně identita není);
§6 pro všech 10 vstupů a libovolný nedotčený komplement; §7 pro každé předem
fixované k≥1 a každou n-tici z Iᵏ — kvantifikace je ∀k ∃ nosič/program,
ne ∃ nosič ∀k; §8 dekódování i podmíněná kapacitní mez pro obecné k.

**Jen konečný výpočet:** identifikace bloků s WORD535 (535 párů, přesně
ověřitelné a zde ověřené, ale je to porovnání seznamů, P5.1); veškerý RESULT
(korpus 1000 trojic jen pro k=3, 3 pokusy na vstupní trojici, kontrolní body
a hashe); PREREGův inventář běhu; 40 rotovaných a 3 mezní audity jako výkon,
přestože jejich matematické identity obecně plynou z P3.4 a P6. PROOF tuto
hranici hlásí správně (PRF:541-546: „the 1000-case execution, when performed,
will audit the separately frozen k=3 realization“; RES:77-79: „the executed
corpus is k=3. No numerical audit of all k … is claimed.“) Žádný text
v PR nedovozuje obecné k z běhu k=3 ani naopak.

## 4. Návrh důkazu pro libovolné předem stanovené k: verdikt

**Jednostranný závěr: indukce v PRF §7 je úplná jako matematická indukce,
není to náčrt.** Netvrdí zdaleka, že jeden pevný konečný stroj běží pořád;
tvrdí přesně ∀k≥1 (k zafixováno před volbou vstupů, PRF:400) ∃ nosič se
26+25k sloty, přípravu s 2k předem čerstvými archivy a k−1 předehrannými
kazetami a pevné slovo P_k, ∀ vstupy z Iᵏ. K úplnosti samotného indukčního
slepence nechybí žádný nový mechanismus. Celek dědičně stojí na lematech
§3/§5/§6 (mezery P5.1, P5.8, P5.13 uzavřitelné dle §2), na indukci samotnou
nemá vliv mezera P1.2 (účty, ne stavová identita).

Kontrola po složkách. *Uzemnění:* j=0 je §6 (U obnoví I(s₀,r₀), zapíše
A₀,B₀) aplikované na počáteční přípravu PRF:408-411, rozšířené o komplement
(ostatní archivy čerstvé, kazety původní) dle P6.4; invariant tedy drží po U₀.
*Předpoklad:* invariant po U_j je vyčerpávající po složkách stavu (PRF:429-436):
jádro přesně I(s_j,r_j) včetně čerstvých pracovních bank a ready ovladačů,
archivy i≤j zapsané, archivy i>j stále M_empty, kazety i≤j drží parkované
předchozí vstupy, kazety i>j dosud nedotčené čekající vstupy. *Krok:*
Π_{j+1} mění definitoricky jen sloty 0..4 s kazetou j+1 (PRF:413-415), tedy
nechává ovladače (5..10), obě čerstvé pracovní banky (11..30) i všechny
archivy nedotčené, a jádro se stane přesně I(s_{j+1},r_{j+1}); U_{j+1} pak
dostává přesně dokázané ready jádro plus dva *skutečně* čerstvé archivy
(invariance i>j), zatímco celý obsazený předchozí stav (staré archivy,
zaparkované i čekající kazety) je komplement, o němž P6.4 platí pro
libovolné hodnoty, protože hrany U jej nezmiňují. Tím je invariant pro
j+1 obnoven ve všech složkách; krok nikde nedosazuje původní auxiliární
stav za skutečně použitý, jak text správně zdůrazňuje (PRF:443-444).

*Co krok spotřebovává a co obnovuje* (to je místo, na němž by rekurze mohla
padnout, a zde sedí): zdroj a hodiny *obnoví* U zpět na právě zpracovaný
vstup (ne na dopředný obraz), ten se swapem zaparkuje a další vstup se
dodá z předehrané kazety, nikoli regenerací; ovladače jsou ready na začátku
i konci (R je obnovuje, W je vrací, W⁻¹ navrátí totéž); pracovní banky
W zapíše, K je na hranicích modulů vrátí do obsazeného stavu po W a teprve
W⁻¹ do M_empty, tedy jsou na příští pokus opět čerstvé na týchž adresách;
naproti tomu krok *nevratně spotřebuje* čerstvost přesně dvou archivních
bank (A_{j+1},B_{j+1}) a frontovou roli jedné kazety. Obojí je předem
zaplaceno v počtu 2k resp. k−1 pro deklarované k a invariant je účtuje.
Jediná formální drobnost, kterou by strojová formalizace musela rozepsat,
je obsah kazet jako počáteční rovnice (PRF:408 „has five slots for
(Y_{s_j},X_{r_j})“ čtená spolu s doménou na PRF:401 a invariantou PRF:435-436)
a disjunktnost adresních intervalů z PRF:403-406; obojí je z textu bez
další myšlenky uzavřitelné a závěr to nemění. Včetně hraničního k=1
(žádné kazety, žádný Π, P₁=U₀) konstrukce funguje; ověřil jsem vlastním
výpočtem P_k pro k=1 (všech 10), k=2 (všech 100), k=3 (24 trojic) a k=4
(4 čtveřice) vůči vzorci koncového stavu z vlastního sestrojení slova
(příloha A) — nezávislá kontrola, ne podstata důkazu.

## 5. Formulace o neomezenosti: nález a opravená znění

Žádné tvrzení v PROOF.md netvrdí nekonečný provoz konečného přístroje,
nekonečnou obnovu ani uniknutí spotřebě archivní kapacity. Naopak dobré
pojistky jsou na místě: nadpis PRF:398 „for any declared finite number“,
PRF:533-537 (čerstvá zásoba 2(k−j−1), žádná globální monotonie),
PRF:541-543 („a family … on explicitly funded carriers“), PRF:555-558
(„no claim of … an indefinitely reusable finite archive“), PRE:168-169
(„it does not claim one fixed finite carrier works for unbounded history“),
RM:44-45, RES:87-89. Slovo „permanent“ v sondě znamená „během dopředného
programu nedotčené a adresou pevné“, jak přesně říká PRF:452-453 („no later
primitive of P_k touches it“); poslední commit totéž doplnil do RES:27-28.

Dvě věty bez tohoto omezení doslova neplatí vůči literární inverzi, která
archivy maže a obnovuje do prázdna (PRE:120-121, RES:34-35):

1. RM:16-17: „Archive capacity is consumed at the declared cycle boundaries.
   No retained archive is erased or made fresh again.“
   Opravená formulace: „During the forward program P₃ no written archive
   is addressed again, erased, or returned to M_empty; fresh pairs fall
   3,2,1,0 at cycle boundaries. The literal inverse P₃⁻¹ does erase the
   records and restore blank archives; it is not a retention-preserving
   reset.“
2. PRE:113-114: „Previously completed permanent archives are never addressed
   by any subsequent primitive.“
   Opravená formulace: „…by any subsequent primitive of the forward program.“
   (druhá věta PRE:114-115 omezení „through all later forward operations“
   už má, první je třeba sjednotit.)

Doporučení bez vlivu na platnost: PRF:544 „The universal finite-k induction“
má v téže větě kvantifikovat nosič závislý na k (odkaz na PRF:541-542 to
de facto činí), tedy psát „For each k fixed in advance, the k-stage induction
…; no single carrier or program serves all k.“ Tím se předejde čtení
∃ stroj ∀k, které text nikde vědomě netvrdí.

## 6. Vlastní přepočet čerstvé archivní kapacity pro tři pokusy

Počítám z definic, ne z výsledného textu. Baza nezávislá na textu:
b=1+ρ², ρ=j², b=(0,−1,−1,−1) v bázi j, takže Q(b)=(5·3−(−3)²)/2=3.
Jedna banka je 5 párů, tj. 10 slotů, záznamy tvořeny hodnotami ±ρᵗb, každá
s Q=3, tedy účet banky 30, ať prázdná, či zapsaná (M[p] má rovněž 10 takových
hodnot). Na jeden pokus použije U přesně dvě kopírovací slova K(11,a),
K(21,d) se dvěma *odlišnými čerstvými* cílovými bankami; kopírovač vyžaduje
čerstvý cíl (P2.7 ukazuje, že obsazený cíl obecné tvrzení porušuje), po kopii
je banka obsazená a v dopředném slově už se k ní nevrací. Spotřeba
čerstvosti je tedy přesně 2 banky na pokus. Pro 3 pokusy je to
2·3=6 bank, 6·10=60 slotů, účet archivů 6·30=180 před zápisem i po něm
(spotřebovaná je *čerstvost*, nikoli účet E; E je kontaktem zachováno).

Celý účet k=3 tím sedí po složkách nezávisle: jeden vstupní systém
(Y,X) má 8+6=14; ovladače (0,u,0,0,w,0) mají Q(u)+Q(w)=5+3=8; dvě pracovní
banky 60; archivy 180; dva čekající vstupy 28; aktivní vstup 14;
součet 14+8+60+180+28=290, Σ (součet v O) 2+2+2+2=8. Auxiliárních adres
(kromě 15 vstupních) je 6 ovladačů +20 pracovních +60 archivních =86
s účtem 8+60+180=248. Očekávání ze zadání (2 banky/pokus, 6 celkem, 60 slotů,
180 v archivech) je potvrzeno výpočtem z definic a souhlasí s texty
(PREREG:85-90, PRF:489-490, RES:52-56), kde není v tomto bodě chyba.
Rozhodující výstup vlastního kódu (doslova, příloha A):

    account k=3 slots=101 (26+25k=101) E=290 (68+74k=290) Sigma=(8, 0, 0, 0) aux_slots=86 auxE=248 archive_banks=6 archive_slots=60 archiveE=180
    k=3 archive consumption: per attempt 2 banks x10 slots x30 acct; total 6 banks 60 slots 180 acct(180 expected)
    archive E before/after recording per bank: 30 [30, 30, 30, 30, 30]

a pro obecná k tentýž kód dal složeninu 26+25k, 68+74k, 2(k+1), 2k bank
(P8.2), takže škálování spotřeby je lineární a žádné „uniknutí“ archivům
konstrukce neobsahuje: (k+1). pokus na nosiči pro k není programován ani
možný bez nových čerstvých bank.

## 7. Návaznost na kánon (citace jménem řádku a statusem)

Citace jsou z checkoutu (shodné s /canon, ověřeno `cmp` pro REGISTRY):
RELATIVE-CONTACT-INTEGRAL-LAW [T] (canon/REGISTRY.tsv:595; canon/CANON.md:13584),
RELATIVE-CONTACT-FOUR-SLOT-MINIMUM [T] (canon/REGISTRY.tsv:596;
canon/CANON.md:13656), RELATIVE-CONTACT-RETAINED-BANK-CAPACITY [T]
(canon/REGISTRY.tsv:597; canon/CANON.md:13795),
RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T] (canon/REGISTRY.tsv:599;
canon/CANON.md:14316). Žádný z nich tento posudek ani PR nezvyšuje.

Na **RELATIVE-CONTACT-INTEGRAL-LAW [T]** navazuje PRF věcně přímo: §1 je
jeho přestavení pro nový kontext (tentýž kontakt, C⁵=I, C⁻¹=C⁴ — kánon říká
„inverse replaces ρ by ρ⁻¹“, na připuštěné větvi totéž, neb C⁴ posílá d na
ρ⁴d=ρ⁻¹d; zachování součtu, hermitovského účtu, polostopy i reziduí mod 1−j).
Záměnu jsem neshledal; jediná vada je chybějící explicitní citace u
polostopy (P1.2 výše).

Na **RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T]** navazuje PR jako na
bezprostředního předchůdce a činí tak správně: přebírá jeho 31slotové
čtecí jádro, slovo WORD535 a 10vstupovou rodinu {0,1}×Z/5, ale ne jeho
úplný program na O⁵⁶ ani jeho účty. Kanonická věta je dvoupokusová na
O⁵⁶ s celkovým účtem 156 a společným auxiliárním účtem 128, se 4 archivy
rozlišujícími 100 párů a se všemi utracenými vstupy i bankami ponechanými
v dopředných konečných stavech, bez obnovy použité paměti. Nové tvrzení
je na jiném, větším nosiči (k=3: O¹⁰¹, účet 290, auxiliárních 248, 6 archivů)
a právě přidává kopii do nových čerstvých bank plus W⁻¹, které jádro
obnoví. Záměna 156 za 290 se v PR nevyskytuje: můj grep přes všechny `.md`
sondy nenašel v této souvislosti žádné 156 ani 128 a 290 je konzistentně
na PRE:90, PRF:489, RM:14, RES:52. Kánonická věta třetí pokus výslovně
klade mimo svůj rozsah a PR ji nerozšiřuje odkazem, nýbrž předkládá novou
konstrukci kandidátského statusu (PRE:177 „is not reopened“, RES:82-84).

S **RELATIVE-CONTACT-RETAINED-BANK-CAPACITY [T]** není konstrukce ve sporu
a nenavazuje na ni chybným použitím. Ta věta zakazuje vrátit použitou banku
do počátečního stavu při zachovaném výstupu a *přesném návrátu každého
jiného zdroje*; zde jiný zdroj — čerstvé archivy — se právě mění
(prázdné→obsazené) a kazety zas parkují vstupy, takže hypotéza věty splněna
není. Pracovní banky se obnoví proto, že záznam byl předtím přenesen do
jiného spočítaného místa nosiče, nikoli čistou regenerací; text žádnou
čistou ani autonomní obnovu netvrdí (PRF:555-558). Číselně je měnící se
auxiliární odběr 20 slotů/účet 60 na jeden zadržený pokus, hluboko nad
analogickými dolními tvary 4/12 té kanonické věty, ale jde o jiný výstupní
kontrakt, takže věta se tu cituje jen jako kontext konzistence, ne premisa.

**RELATIVE-CONTACT-FOUR-SLOT-MINIMUM [T]** není v PR použit jako premisa
a záměna mezí 12/27 se nestala: v kánonu jsou 27 (kladný cíl) a 12
(značený cíl) minimální počáteční auxiliární *účty* přesně čtyřslotové
přípravy konkrétních známovstupových přechodů na O²⁶, ne délky slov ani
účty bank. V PR se 12 vyskytuje jen jako počet kontaktů lokálního modulu
W6 (PRF:72,123 a jinde) a 27 jen jako výstupní počet internovaných hodnot
v RES:43; ani jednou ne jako čtyřslotová účtová mez. Jediný nález je
pojmenování „four-slot“ pro čtyřmísté kopírovací obstrukce v PROV (S2 výše);
věcné odvození jí nedotčeno.

## 8. Shrnutí počtů a podmíněnost závěrů

Tabulka v §1 obsahuje všechny věty a lemmata důkazových textů PR, celkem
90 položek. Strojový součet (příloha B): bez výhrad drží 75; s mezerou jsou
P1.2, P5.1, P5.8, P5.13, R2, R8,
A3 a S2; doslova nedrží jediná neomezená formule A2 (RM:16-17); jen konečný
výpočet jsou R10, V1-V3, V5 a W2. Jednostranné závěry z §4-7: indukce pro
předem dané k je úplná (a závisí na uzavřitelnosti dílčích mezer §5 PROOF);
archivní spotřeba je 2 čerstvé banky na pokus, pro k=3 celkem 6 bank/60 slotů/
účet 180, lineárně v k; návaznost na všechny čtyři citované kanonické věty
je správná a záměna účtu 156/290 ani mezí 12/27 se v PR nevyskytuje.

## Příloha A: rozhodující výstup vlastního nezávislého výpočtu (doslova)

Kód: `/tmp/mathrev/own_check.py`, psán z definic v PROOF.md, bez použití
autorova verify.py. Nejdůležitější řádky skutečného výstupu (exit 0):

    rho= (0, 0, 1, 0) u= (1, 0, -1, 0) w= (1, 0, 1, 0) b= (0, -1, -1, -1)
    Q(u),Q(w),Q(b)= 5 3 3
    Q == Tr(z*conj(z))/2 on 200 random: True
    F16 rho(order)= [1, 4, 15, 2, 8, 1] w= 5 w^3= 8 rho^4= 8 b= 14 w^2= 14 1+rho^e nonzero e1..4: [True, True, True, True] w in <rho>? False cosets <rho>w,<rho>b disjoint? True
    bank E empty/marked= 30 [30, 30, 30, 30, 30] sums zero: True residues: [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]
    opp admission P=Q only: True
    W6 (0, 0, 0, 0) -> [(0, 0, 0, 0), (2, 2, 0, 0), (2, 2, 0, 0), (0, 0, 0, 0), (4, 0, 0, 4), (4, 0, 0, 4), (0, 0, 0, 0)] admword AARAAAAAAARA count 10
    W6 (1, 0, 0, 0) -> [(1, 0, 0, 0), (1, 0, 0, 0), (1, 1, 1, 0), (4, 4, 1, 0), (4, 4, 1, 0), (0, 0, 1, 0), (1, 0, 1, 1)] admword RRAAAARRRRAA count 6
    W6 (0, 1, 0, 0) -> [(0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (4, 1, 0, 4), (4, 1, 0, 4), (0, 1, 0, 0)] admword RRRRRRAAAARA count 5
    W6 (0, 0, 1, 1) -> [(0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (1, 1, 1, 1), (2, 1, 1, 2)] admword AARAAARRRRAA count 7
    K r=0 ok=True admitted=41/60
    K r=1 ok=True admitted=41/60
    K r=2 ok=True admitted=41/60
    K r=3 ok=True admitted=41/60
    K r=4 ok=True admitted=41/60
    F(Y_a)=Y_a+1 all9: True T(X_r)=X_r+1: True
    lengths Lp,SCAN,Ec,WA,D,V,R,S = 10 80 10 105 9 23 261 535
    WORD535 pairs: 535 exact literal == S from PROOF blocks: True unordered-pair equality: True
    W I(s,r) formula all 10: True W len 5350 Winv len 21400
    U len: 26870
    U all10: True
    P_k k=1 tested=10 ok=True contacts=26870 swaps=0 slots=51 inv_contacts=107480
    P_k k=2 tested=100 ok=True contacts=53740 swaps=5 slots=76 inv_contacts=214960
    P_k k=3 tested=24 ok=True contacts=80610 swaps=10 slots=101 inv_contacts=322440
    P_k k=4 tested=4 ok=True contacts=107480 swaps=15 slots=126 inv_contacts=429920
    random pairs C^5=id,C^4 inverse,rho-equivariance,sum/H/E/eps (300): True
    Ec then Ec_inv on 50 random (g,c,h): True
    SCAN gated fresh -> M[-r], clock/t restored: True
    SCAN inactive preserves fresh+occupied: True
    K not involution (exists r K^2 != id on prep): [(0, True), (1, True), (2, True), (3, True), (4, True)]
    rotated K corollary all t,r (25): True
    full Hermitian H for k=3 prep (j-basis): (108, 0, -74, -74) RESULT claims (108,0,-74,-74)
    residue vector prep == EXPECTED labelled_residue_vector: True len 101

Identita souborů WORD535 (samostatný příkaz, doslova):

    ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b  probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/WORD535.txt
    ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b  probes/P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1/WORD535.txt
    WORD535_FILES_IDENTICAL

(cesty výše zkráceny na rep-relative; příkaz dával absolutní cesty
v checkoutu, hodnoty hashů i verdikt jsou doslovné.)

## Příloha B: strojový součet hodnocení tabulky

Počet napočtený skriptem jen z řádků tabulky (ID a sloupec Nález), doslova:

    90
    Counter({'DRŽÍ': 75, 'DRŽÍ S MEZEROU': 8, 'POUZE KONEČNÝ VÝPOČET': 6, 'NEDRŽÍ': 1})
    ['P1.2', 'P5.1', 'P5.8', 'P5.13', 'R2', 'R8', 'R10', 'A2', 'A3', 'V1', 'V2', 'V3', 'V5', 'S2', 'W2']

(druhý seznam jsou všechny položky mimo DRŽÍ, v pořadí tabulky). Součet
souhlasí s výčty v §8: mezery 8, jen konečný výpočet 6, nedrží 1.



