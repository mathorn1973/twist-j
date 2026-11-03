# Posudek PR #1879 (P-RELATIVE-CONTACT-WORKBANK-REUSE-1) — fáze 2, porovnání

## Rozhodnutí

**PASS S POZNÁMKOU.** V žádné srovnané veličině nebyl nalezen skutečný
rozpor (DIFF-REAL: 0). Poznámky se týkají rozsahu a mechanismu mého
ověření, ne čísel autora; jsou vypsány níže a v COMPARISON.json.
Tento posudek nemění status v kánonu; autorův kandidát zůstává
NON-CANONICAL / L1 / candidate-C tak, jak sám deklaruje.

## Zmrazení a druhý běh mého ověřovače

SHA-256 souborů ve /work/posudek sedí přesně se zmrazením
(commit 7bc66bcc315c5a9d13595d2698212c2d8cbc9b4b):

- PREREG.md 4e0ff6ccd685649dfd56bf3ab4e6292e14f6501c60d892fd74ae9bb48e30da33
- README.md 0d8bb9ba6031ea315e58ed54dc7130f5491789a27aa1766ad3fea4b523a84ff9
- review.py faef109eb9499d6df9673e7946350f9a38b9fc65ec529a977d8241583ca95ffb

Opakovaný plný běh (`python3 review.py`, 1000 trojic i 1000 inverzí)
bez jakékoli změny kódu: exit 0, `RESULT: PASS (full)`, K1–K9 PASS.
Výstup je uložen v RUN-REVIEW.txt (sha256
cd39721409a5542045459af4f2dedcbee5b84c201cf0b5a5ed771a041156d3de,
1690 B) a RUN-REVIEW-STDERR.txt (prázdný, sha256
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855).
Teprve po tomto běhu byly otevřeny autorovy soubory.

## Porovnání K1–K9 (jednostranné vyřízení)

K1: obsahově shoda; obě strany kříží 4- a 5-koeficientovou aritmetiku
a invarianty použitých párů. Sčítání pár-katalogů má odlišnou jednotku
(autor 86 map / 66 orbit / 27 hodnot; já 229 položek (délka běhu, pár)
/ 63 rozlišných párových vstupů + vyčerpávající box 65536 párů):
DIFF-CONVENTION, žádná společná veličina se neliší.
K2: MATCH ve všem (101 slotů; účet 290; součet [8,0,0,0]; pomocné
86/248; vstupy 15/42; měnící se adresy přesně [0,1,3,4,91,92,94,95,
96,97,99,100]; vektor reziduí po složkách totožný). Autor navíc
hlásí úplný hermitovský účet [108,0,-74,-74], který můj běh fáze 1
nepočítal; z mé zmrazené přípravy jsem ho ve fázi 2 dopočítala
stejně.
K3: MATCH. Dekodér čte na obou stranách jen šest archivních bank,
pravidlo (pa-pb) mod5 v {1,3} je totožné, 1000 dekódovaných trojic,
1000 rozlišných historií; můj převod jeho digestu historií sedí.
K4: MATCH na všech koncových bodech; poznámka: autor kontroluje
uvnitř W mezistavy (60000 čtení, 30000 kroků zápisu, 9000 událostí),
já jen celé W a hranice etap. Jeho tick-formule jsem nezávisle
neodvozovala; mé hrubší členění je rozdíl rozsahu, ne výsledku.
K5: MATCH (u mne 30000 hranic modulů kopírovače a 3000 obnov jádra,
stejně jako jeho čítače; liší se jen, že je netisknu jako čítače).
K6: MATCH. K7: MATCH (viz 4d). K8: MATCH ve všech počtech; liší se
mechanismus (viz 4a). K9: syrové fingerprinty se liší jen
serializací; po explicitním převodu sedí všechny (viz 4b).

## Body 4a–4d

(4a) Počet kontaktů: autorovo číslo v EXPECTED.txt je doslova
`"trajectory_contact_applications":403050000` a je to čítač stroje:
`apply` ve verify.py (ř. 226–237) navštíví každý literální kontakt
jednotlivě (cache je jen na uspořádaný pár jednoho kontaktu,
certifikovaná po orbitách, ř. 186–224), přičítá délky slov a na
ř. 705 asertuje rozdíl od startu hlavního korpusu; lokální audity
(8400+960+18=9378 kontaktů) jsou před tímto startem (ř. 596, 613).
Žádné RLE. Moje číslo 403 050 000 je tatáž definice a tatáž hodnota
(80610+322440 na trojici, krát 1000), ale trajektorie u mne běží přes
auditované běhy stejných hran C^k: rovnocennost s literálním slovem
jsem v běhu prokazovala dekompresí každého slova, přepočtem každé
cache položky a necacheovaným literálním průchodem trojice 0, takže
můj počítadlový mechanismus je derivace z délek, ne 403 milionů
jednotlivých návštěv jako u autora. Shoda hodnoty i definice, rozdíl
provedení: DIFF-CONVENTION u mechanismu, MATCH u veličiny.

(4b) Fingerprinty: autorova serializace je kompaktní JSON
(verify.py ř. 463–464) nad tokeny ["C"/"SWAP",i,j] a nad
[parametry, koncový stav] bez oddělovačů mezi trojicemi
(ř. 686–687, 737–740). Moje (konvence V8) jsou „C{i},{k};" tokeny
a stavy samotné s novým řádkem. Explicitní převod: moje zmrazené
slovo/stavy přepsané do autorova JSON dávají přesně jeho hodnoty —
program a0e78fe4…, inverze ccc21b19…, koncové stavy 5fa52c61…,
historie dekodéru bff60f74… (plné hodnoty v COMPARISON.json).
Spojení tedy existuje a je úplné; žádný bod rozcházení nezůstal.

(4c) Slovo S proti WORD535.txt: po jediné normalizaci (autorův
soubor je 1-based) je můj seznam 535 kontaktů token po tokenu
totožný s parsovaným WORD535.txt i s interním S ve verify.py.
Je to doslova tentýž program; moje fáze 1 ho složila jen z bloků
PROOF.md, bez souboru.

(4d) Čerstvá archivní kapacita: moje posloupnost dvojic [3,2,1,0]
je přesně autorových 6,4,2,0 čerstvých bank (z jeho `archives()`
pro completed=0..3; EXPECTED hlásí permanent_archive_banks 6,
RESULT.md pokles šesti bank na nulu). Mřížka sedí: 6 bank /
60 slotů / přípravný účet 180, tj. 2 banky / 20 slotů / 60
na pokus. MATCH.

## Co ověřil můj kód, co CI a co zůstalo

Můj zmrazený kód na tomto stroji ověřil: celý deklarovaný k=3
kontrakt nezávisle od nuly — všech 1000 trojic dopředu i 1000 úplných
inverzí se všemi kontrolami K1–K9, lokální identity kopírovače,
účty a dekodér (fáze 1), a ve fázi 2 opakováním téhož běhu.
Autorův plný běh jsem podle zadání neopakovala: jeho přehrání na
x86_64 i aarch64 provedlo CI (sdělení Thorna; logy CI v tomto
checkoutu nemám a sama jsem je neviděla, v repozitáři je autorův
RUN.md/RESULT.md o prvním běhu x86_64). S autorovým EXPECTED.txt
jsem srovnala každou veličinu strukturálně (COMPARISON.json),
včetně toho, že autorův verify.py počítá kontakty opravdu
literálně a jeho PROGRAM/INVERSE_PROGRAM jsou op po opu totožné
s mými.
Zůstává NEOVĚŘENO: reprodukce autorova běhu na obou architekturách
mnou osobně; obecná indukce pro libovolné konečné k (strojově
je ověřen jen k=3; formule jsem jen dosazovala); autorovy vnitřní
tick-mezistavy W jinak než přes koncové body. Netvrdí se nic
o nekonečném provozu ani o fyzikální realizaci.

## Co nezávislost je a co ne

Je: review.py byl napsán ve slepém režimu bez autorova verify.py,
EXPECTED.txt, WORD535.txt, RESULT.md, SOURCES.tsv a bez historie
gitu, jen z rovnic a textů PR; preregistrace předcházela prvnímu
spuštění; trojice souborů byla publicly zmrazena (hashy výše)
předtím, než jsem autorovy soubory poprvé otevřela, a druhý běh
proběhl před jejich otevřením. Převody ve fázi 2 jsou post-hoc
a jako takové označené; žádná zmrazená veličina se po otevření
neměnila.
Není: cíl byl znám z veřejného textu PR (PREREG/PROOF včetně
koncových formulí a počtů), takže jde o nezávislou reimplementaci
známého kontraktu, ne o slepý objev. Stejně jako autor (PROVENANCE)
pracuji se zpřístupněným svědkem kopírovače z textu; matematická
přijatelnost důkazů v PROOF.md je věc samostatného matematického
posouzení, tento strojový posudek ověřuje deklarovaný konečný
kontrakt a shodu obou implementací, ne větu samotnou.
