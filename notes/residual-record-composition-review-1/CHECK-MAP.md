# V100-JOIN-1: konkrétní ověřovač a mapa tvrzení

NON-CANONICAL, L1. Návrh k přezkumu pro P-RESIDUAL-RECORD-COMPOSITION-1.
Tento soubor popisuje skutečný kód `verify.py`, nikoli výsledek jeho běhu.
Před veřejným pinem nebyl program, jeho import ani žádná jeho vědecká funkce
spuštěna. Níže uvedené počty jsou přesné meze odvozené ze zdrojových smyček;
nejsou získaným stdout, `EXPECTED.txt`, `RUN.md` ani tvrzením PASS.

`PROOF.md` a `PREREG-DRAFT.md` se tímto souborem nemění. Rozsah tvoří úplné
malé tabulky, přesná termová symbolika a již deklarovaný redukovaný atlas.
Obrovské nativní slovo není sestaveno ani provedeno.

## Úplný stav a závislosti

Věta se týká celého `X=F5^12×{0,1}`, všech pístů, neznámých q, obsazených r
a obou bitů. Číselná tabulka čtečky má pořadí `(qx,qy,rx,ry)`. Symbolická
mapa má pořadí `(piston_bit,q,rx,ry)`; `piston_bit` reprezentuje všechny
pístové souřadnice a eta. Symbolický klíč `H` je celý skutečný faktor
`(piston_bit,rx,ry)` po první čtečce. Nevynechává obsazené r.

Ověřovač za běhu vyžaduje dvě **přesné místní kopie**:

- `contact_dependency.py`: beze změny existující kandidátní zdroj
  P-CONTACT-RECORD-1; před formálním pinem se vyžaduje jeho přijetí;
- `algebra_dependency.py`: beze změny konkrétní zdroj
  P-ALG-CONTACT-REALIZATION-1 / CW-ALG-1.

Jejich `VERIFIER-PINS.json` má schéma
`V100-JOIN-1/dependencies/v1` a pole `dependencies` obsahující právě dva
objekty s položkami `name`, `filename`, `sha256`, `source_commit`,
`source_path`. Jména jsou `contact`, `algebra`; názvy souborů jsou přesně
ty uvedené výše. Commit musí mít 40 hexadecimálních znaků, SHA-256 64,
zdrojová cesta musí být veřejná relativní cesta pod `notes/`. Každý objekt
odkazuje na skutečně veřejný commit zdroje; samotný syntaktický test commitu
není důkaz veřejného přijetí. Veřejnou dostupnost a přijetí ověřuje předpinový
přezkum. VERIFIER-PINS.json nyní váže algebraický kód na veřejný review commit
`a7c5d72a0ff0ab0af0b1de18ae3f18af134529d3` a nezměněný kontaktní kód na
`8128286127f1a48b01ebda1a5c1e7a0d88d46095`. Jsou to obsahové vazby
poznámkových předloh, nikoli již přijaté formální piny. Samostatné přijetí
obou závislostí musí být doloženo před formálním pinem složení.

`load_dependencies` nejprve načte a ověří hashe **obou** souborů, teprve
potom je importuje. Jejich `main` se nespouští. Import je součástí budoucího
připnutého běhu; při nynější přípravě se neprovádí. Není potřeba síť,
měnitelný Canon ani externí checkout. Program nezapisuje pyc ani jiné soubory.
Manifest a obě kopie musí být součástí téhož budoucího pinovaného balíčku.

## Mapa funkcí, tvrzení, typu a rozsahu

| Funkce / kontrola | Přesné tvrzení | Typ a konečný rozsah | Důkazní krok |
|---|---|---|---|
| `load_dependencies` | Použité zdroje mají přesné připnuté bajty a dvě určená rozhraní | 2 SHA-256; kontrola před jakýmkoli importem | PROOF §1, §3 a §7; provenance není vědecký výsledek |
| `audit_reader_tables`, tabulka P | P odpovídá jednotlivým záměnám a každé P_q je involuce | Úplných 25 dvojic `(q,r)` | PROOF §3, rovnice (1); samostatný CONTACT důkaz |
| `reader_formula`, `audit_reader_tables` | Celé A_i i A_i^-1, obě inverzní kompozice, oba nezměnění diváci, bijektivita, ready a inverse-ready iff | `2 strany × 2δ × 5^4 = 2500` úplných vláknových vstupů | PROOF (1), (6); všechny ostatní souřadnice vrací CONTACT |
| `audit_linear_fibres` | Každé H∈GL2(F5) bijektivně přenáší celé q-vlákno a má deklarovanou obousměrnou inverzi | 625 kandidátních matic; všech 480 regulárních × 25 q = 12000 řádků | PROOF (3), (6); SPEC přesná rekurence H,t |
| `audit_symbolic_composition`, `s_A`, `s_T`, `s_V` | Úplná rovnice V (4), skutečný klíč H po A_x, návrat obou obsazených r po T, obě úplné inverzní kompozice | 4 možné dvojice `(δ0,δ1)`; nezávislé symboly pístů/bitu, q, r_x,r_y; 8 identit roundtrip | PROOF (3)–(6), (11) |
| `audit_target` | B_read M=L5 B_read, obě inverze M a δ(Mg)=1−(α+β+γ)^4 | Všech 125 Gramových trojic | PROOF §2, (5), (8) |
| `slot_map`, `audit_slots_and_s1` | Celá redukovaná permutace, obousměrná uzavřenost Omega, cílový krok na ní, přesný obraz ready bitu | 1280 nenulových slotů + 2 celé nulové větve; dopředná i zpětná kontrola | PROOF (7), (8); SPEC algebraický atlas a jeho nezávislost na L,n,r |
| `slot_s1`, `audit_slots_and_s1` | S1 právě tehdy, když úplná inverze obnoví S0, včetně libovolně obsazených výstupních r | `1282 × 25 = 32050` slotových/registrových řádků | PROOF (9), (10), §5; inverse-ready iff ze všech q v tabulce A |
| Vážené čítače v `audit_slots_and_s1` | Velikosti S1, Omega a dosahu samotného T při r=0 | Váhy 600 pístových párů na nenulový slot a 6625 nulových pístových párů; úplné q vlákno má 25 stavů | SPEC atlas a přesný nulový počet; PROOF §5 |
| `audit_prefixes_and_boundaries` | Čtverec r_x se nemění po žádném listu A_y ani jeho syntaktické inverze | 2 směry × 16 voleb znamének čtyř W × 5 r_x × 15 hranic = 2400 hranic | PROOF (12); CONTACT přesný listový kontrakt |
| Negativní hranice ve stejné funkci | Čtverec není obecně binární ani globálně chráněný; opakování celé čtečky může mazat; dokončený nulový test je totožný s nepoužitým | 5 čtverců, původní přesné negativní svědky a 25 nulových čtecích vstupů | PROOF §6 a samostatný CONTACT rozsah |

## Proč oddělené malé tabulky pokrývají obecné složení

Neprochází se kartézský součin 480 matic se všemi 488281250 stavy X.
Čtečka závisí právě na `(q_i,r_i,δ)` a její úplná tabulka pokrývá všechny
tyto hodnoty; druhou dvojici drží jako libovolného nezměněného diváka.
Písty a bit vrací podle samostatného CONTACT důkazu. Každé q-vlákno
prostředního slova je celé přeneseno maticí H_f. Všech 480 možných matic je
ověřeno samostatně, ale konkrétní volbu H_f stále určuje pevné CW-ALG-1.

Termový systém `s_*` pak provede přesné obecné složení. Používá výhradně
následující pravidla: sčítání vektorových posunů modulo 5, `P_q P_q=I`,
`R^-1 R=R R^-1=I`, `H_f^-1 H_f=H_f H_f^-1=I`. Poslední pravidlo platí
**jen pro strukturálně totožný úplný faktorový klíč**. Žádné H se nemění
na identitu, H s odlišnými klíči se neruší a H nekomutuje s čtečkou ani
s posunem. Dvě výslovné negativní assertiony tuto hranici kontrolují.
Při inverzi T se klíč sestaví až z obnoveného faktoru, nikoli z konečného
záznamu po A_y. Symbolické zrušení obou kompozic proto ověřuje i správné
pořadí obnovy libovolných obsazených r a neznámého q.

Toto je mechanizovaná kontrola uvedeného kompozičního lemmatu. Její
pravidla nejsou novou axiomatikou stroje: P-involuce má úplnou tabulku,
invertibilita H má úplnou GL2 tabulku, R/inverze a skutečný přípustný
CW-ALG-1 lift mají samostatný přesný konstrukční důkaz. Kontrola nenahrazuje
přezkum toho konstrukčního důkazu ani nevykonává jeho nativní slovo.

## Přesnost S1 a nulového vlákna

Nenulový atlas má 1280 slotových stavů `(g,j,eta)`. Pi_alg ponechává
`L,n,r` beze změny a slotový zákon je na nich nezávislý. Funkce `slot_map`
použije přesný připnutý atlas při `L=I,n=0` pouze k vyhodnocení tohoto
**úplného deklarovaného kvocientu**. Tento výběr není tvrzením o enumeraci
všech pístů a jeho univerzalitu dodává důkaz nezávislosti atlasu, nikoli
jeden reprezentant. Celá větev `g=0` je podle definice Pi_alg identita;
v kódu ji reprezentují dva symbolické sloty, po jednom pro každý bit.
Nejde o záměnu jednoho nulového pístového svědka za všechny nulové písty.

Pro každý výstupní slot se projde všech 25 hodnot `(r_x,r_y)`. Kritérium S1
se porovná s přesnou podmínkou připravené inverze, odvozenou z předchozího
slotu a obou úplných tabulek čteček. Ty již ověřují pro každé q ekvivalenci
`A_i^-1(y,r)_r=0` právě tehdy, když `r=δ`; libovolná bijekce H_f před tuto
ekvivalenci nepřidává omezení q. Proto výsledný S1 obsahuje všech 25 q
na každém vyhovujícím pístovém/bitovém/registrovém stavu a žádný jiný stav.

Váhy jsou důsledkem algebraického atlasu: `|SL2(F5)|·5=120·5=600`
pístových párů pro každý nenulový `(g,j)`, na nulovém Gramu je 6625 párů.
Kód kontroluje `|S1|=9765625`, `|Omega_alg|=281640625` a
`|Omega_alg∩{r_x=r_y=0}|=11265625`. Přesný opakovaný dosah V ze S0 se
neenumeruje a není ztotožněn s Omega_alg. Omezení r∈{0,1,2} platí na
makrohranicích, nikoli uvnitř nativního slova.

## Prefixová a výsledková hranice

Čtyři W_b v A_y mohou podle skutečných pístů a bitu měnit znaménko r_x.
Kontrola zahrne všech 16 kombinací těchto znamének. To je bezpečná širší
množina než realizovatelné větve: každá skutečná větev do ní patří, žádná
nesplnitelná kombinace není vydávána za trajektorii stroje. Každá jednotlivá
akce `r→r` nebo `r→−r` zachovává čtverec pro všech pět r. Indukce přes
celé pevné slovo pak platí pro všechny úplné vstupy X. Přesný význam
jednotlivých listů je závazkem samostatné CONTACT závislosti.

Tento prefixový audit se nevztahuje na T_alg. Prostřední slovo vrací první
registr až na svém konci podle globálního faktorového kontraktu. Binární
význam obou výsledků se zaručuje jen při jediné počáteční přípravě S0.
Nevytváří se completion bit, archiv ani nové připravené reference pro další V.

## Budoucí provedení a stdout

Po řádném přijetí, veřejném pinování všech čtených souborů a kontrole
aktuálního postupu repozitáře je vstupem Python 3.12 a příkaz `python3 verify.py`
v této složce. Program zapíše jediný deterministický JSON řádek s LF,
stavem `PASS_LIMITED_COMPOSITION_CONTRACTS`, čítači a přesnými hashi závislostí.
Neobsahuje čas, cestu stroje ani architekturu. Nenulový exit, neprázdný stderr,
selhání assertionu nebo neshodné bajty nejsou PASS. Skutečné EXPECTED/RUN/RESULT
mohou vzniknout až po tomto budoucím řádném běhu.

První neúspěšná assertion zapíše přesné označení tvrzení a reprodukovatelný
protipříklad. Vláknové řádky zahrnují stranu, delta, všechny čtyři vstupní
hodnoty a příslušné výstupy; symbolické identity zahrnují dvojici delta,
celý zdroj a výsledné termy. GL2 kontroly zapisují H a q, slotové kontroly
celý slot a jeho obrazy, prefixové kontroly směr, všechny volby znamének,
počáteční r a přesnou pozici listu. Selhání čítače obsahuje skutečný počet.
Program končí při prvním selhání v pevně určeném pořadí kontrol.

Program výslovně vypisuje, že nespustil CW-ALG-1 expanzi, nativní T_alg,
nativní V, úplnou enumeraci X ani census opakovaného dosahu V. Výstup malých
kontrol nezvyšuje status těchto neprovedených operací ani kandidátních důkazů.
