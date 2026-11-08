<!-- SPDX-License-Identifier: Apache-2.0 -->

# TWIST-J: stavba celého stroje, mapa k 8. listopadu 2026

**Datum uzávěrky:** 8. listopadu 2026, noční průchod (UTC)
**Status:** NON-CANONICAL WORKING MAP
**Účel:** poctivě zjistit, jak daleko je stavba celého stroje, tedy úplného
konečného přístroje, který program od Public Canon v100 skládá po částech;
oddělit, co je dokázané, co spočítané, co přijaté a co otevřené; pojmenovat
rozhraní mezi částmi; a vybrat nejmenší další rozhodnutelné kroky.

Tato mapa není Canon, preregistrace, evidence ani návrh na změnu statusu.
Navazuje na `notes/PRACOVNI-MAPA-V81-2026-09-08/` (větev PR #907) a na
konsolidaci `notes/CONSOLIDATION-2026-11-07/` (větev PR #1952), kterou
nenahrazuje: konsolidace shrnuje celý Canon podle témat, tato mapa jen jednu
věc, stroj. Každé číslo níže je buď z registru, nebo z pojmenovaného souboru.

```text
STATUS:            NON-CANONICAL WORKING MAP
AUTORITA:          ŽÁDNÁ; autoritu deklaruje výhradně STATUS.md
VEŘEJNÝ CANON:     Public Canon v109 / canon-v109
CONTENT COMMIT:    2b0f94ec1e0874bff9141259e0b7da80e6681ea6
CANON SHA-256:     035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383
CANON BYTES:       1464066
REGISTR:           609 tvrzení; 465 T, 59 D, 40 C, 2 H, 24 O, 19 F; 26 živých H/O
MAIN PŘI ČTENÍ:    3c857642 (8. 11. 2026, po sloučení PR #1636 až #1638, #1746,
                   #1761, #1764, #1766, #1819, #1821, #1857, #1908, #1912, #1915);
                   main se během noci dál hýbal (uzavírání ABANDONED záznamů)
BASELINE:          mapa připravenosti v105 z 23. 10. 2026 (twistj-handoff)
FORMAL RUN:        NONE
PROBE/PREREG:      NONE
CANON/REGISTRY:    BEZE ZMĚNY
```

## 1. Výsledek na jednu stránku

Stroj dnes existuje jako **šest strojů na šesti nosičích**. Každý z nich je
uvnitř postaven přesně, s dodanými přípravami a spočítanými účty. Mezi sebou
je nespojuje žádná registrovaná věta kromě jediného konečného výpočtu
(zrcadlo přenosu, `U-CARRY-MIRROR-FINITE-CIRCUIT [C]`), a Canon jejich
neztotožnění říká výslovně: „The contact and native carriers keep separate
laws and interfaces“ (`canon/CHANGELOG.md`, v109).

- **Kontaktní nosič** (`O^m`, `O = Z[j]`) je nejúplnější: příprava, běh,
  záznam, čtení z archivů, obnova pracovního jádra a opakování pro libovolný
  konečný horizont `k` jsou registrované věty `[T]`: společný přístroj a
  ostrá minima mají dvouarchitekturní sondovou evidenci, obnova pro každé `k`
  (`RELATIVE-CONTACT-FINITE-WORKBANK-REUSE`) má inline důkaz indukcí a sondu
  pro `k = 3` jako podpůrný audit. Chybí mu
  prostředí a bootstrap, jeho zavaděč (322 kontaktů, pět vstupů) je
  NON-CANONICAL a mluví jiným vstupním dialektem než stopky, a nemá žádný most
  k nativnímu `U`.
- **Tepelný nosič** má od tohoto týdne všech devět stupňů cyklu dotčených:
  prostředí, bootstrap pracovního zásobníku a hlavních hodin a příprava
  registrů jsou tři sloučené analytické kandidáty bez verifieru
  (`C-THERMAL-REGISTER-PREPARATION-N`, `C-THERMAL-WORK-CLOCK-BOOTSTRAP-N`,
  `C-COMMON-TEMPERATURE-PREPARATION-N`); běh, záznam, dva pokusy a výměna
  jádra jsou věty `[T]` podmíněné dodanými premisami. Jeho energie není
  ztotožněna s energií koherentní procházky, na níž běží záznamový krok.
- **Nativní `U`** umí přenést jeden zbytek do společného přijímače, přesně ho
  přečíst z přijímače a čítače a jednou zapsat; dokázáno je, že samotný
  přijímač nestačí, že synchronizovaný zápis z BLANK do WRITTEN neexistuje a
  že žádný konečný autonomní kontext bez dodaného Thueova–Morseova bitu
  neobnoví čtení. Nemá obnovu ani opakování. Jediný výstup ven je zrcadlo
  přenosu na 62 registrech `F_5`, a to jen jako `[C]`.
- **Mimo cyklus** zůstává to, co z konstrukce dělá fyziku: zákon výskytu
  jednoho výsledku (přijatý na `[D]` v ETH-QDD-1/2, neodvozený), fyzikální
  realizace přístroje (čtyři vlastníci `[O]`, všichni na `STOP`) a převod
  jednotek. Program sám říká, že další konstrukce téhož druhu tyto vlastníky
  nepohnou; pohne jimi definiční práce.

Co se našlo a vyloučilo za posledních osm dní, v jedné větě na položku:
zavaděč pro všech pět vstupů existuje a má přesně pět úspěchů nad celými
čísly; stopky s deseti vstupy a dvěma razítky jsou potvrzeny; dvojice
pracovních bank se obnoví pro každé `k`; nativní fáze vlákna je ručička hodin
a nenese informaci o cestě; na kontaktním nosiči informaci o cestě nese počet,
ne účet; tepelný bootstrap se posunul až k jedné teplotě a jednomu palivovému
qubitu; a na kontaktním nosiči nelze z neutrální zásoby nabít pólovou výšku
ani doslovně okopírovat banku na čtyřech místech.

Co přidává tato noc: typovanou smlouvu stroje
(`notes/canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`), tabulku slotů a
rozhraní ověřenou mechanicky proti registru (`check_assembly.py`, 73 citovaných
řádků, všechny statusy souhlasí) a jeden přesný audit rozhraní: výstupní pár
zavaděče má zbytky `(0, 0)` modulo `1 - j`, hodinový pár stopek `(2, 3)` a
zdrojová trojice `(0, 2, 0)`, takže žádné kontaktní slovo nepřevede jedno
v druhé bez vypůjčených míst (`check_loader_interface.py`). A jeden vedlejší
přesný výsledek o nativní čtečce: dvacetihodnotový souhrn čítače
`(sigma_n, z_n, N_n mod 5)` z `U-NATIVE-RAW-RESIDUE-READOUT` není
nejmenší; `z_n` je nadbytečné, souhrn `(sigma_n, N_n mod 5)` o deseti
hodnotách stačí a nejmenší postačující souhrn má přesně pět tříd
(`check_native_counter_statistic.py`, výpočet nad podmíněnou větou Canonu,
žádné tvrzení). Stroj se tedy dnes nedá „dostavět“ sloučením částí; dá se
přesně říci, co z každé části chybí a co by muselo platit, aby se spojily.

## 2. Co se zde rozumí strojem

Vlastník stroj popisuje v knižním kompendiu (větev `main` repozitáře knihy,
`web/Konstrukce_ke_kapitolam.md`, kapitola 38, pododdíl „Od nativní
přípravy k homogennímu záchytu a přijímači“, řádek 1014; pět nejbližších
kroků programu je v pododdílu „Obraz fyziky podle TWIST-J na ubrousku a co
ještě chybí“) a jmenuje pět úkolů, které čekají „na uzavření hry do fyziky“: přístroj z původního kroku, zákon výskytu jednoho výsledku
místo deklarovaného Bornova čtení, společný nosič a sjednocení zachovávaných
účtů, převod jednotek a praktický konečnočasový režim záchytu pro obecné
přípravy. Tato mapa je rozepisuje do devíti stupňů jednoho uzavřeného cyklu:

```text
S0 PROSTŘEDÍ    S1 BOOTSTRAP   S2 PŘÍPRAVA   S3 ZAVEDENÍ   S4 BĚH
S5 ZÁZNAM       S6 ČTENÍ       S7 OBNOVA     S8 OPAKOVÁNÍ
```

a do čtyř mostů mezi nosiči (B1 kontakt a nativní `U`, B2 nativní `U` a
registry, B3 celočíselné nosiče a koherentní procházka, B4 tepelný nosič a
koherentní procházka). Přesné typy stupňů, nosičů a mostů jsou ve smlouvě
`notes/canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`. Pět úkolů vlastníka
leží takto: první je most B1 a vlastník `QUADRATIC-MEMORY-NATIVE-CONTACT [O]`;
druhý je mimo cyklus (oddíl 7); třetí jsou mosty B3 a B4; čtvrtý je
`METRO-EDGE-SCALE [O]` a `SCHEME-DICTIONARY [O]`; pátý je stupeň S4 na nosiči
K5 (konečný čas záchytu).

Tentýž autor to říká v kapitole 38 rukopisu Thornovými ústy (řádek 320):
„Co stroj nedává, je port ven: který účet přístroj v přírodě zapíše, který
výsledek a jak často, jak se znormuje společná akce a propojí s bezrozměrnou
vazbou α a co je modelová jednotka délky a času. A rozvrh, podle kterého
čte, mu zatím dodáváme zvenku. Dokud to chybí, jsou všechna čísla nahoře
o stroji. O přírodě začnou mluvit až s portem.“ Tato mapa měří přesně tu
větu: co stroj dává uvnitř, a kde je port.

Slovo stroj zde znamená matematický objekt na hladině L1. Věta o něm není
věta o světě; to je zásada programu a tato mapa ji nikde neobchází.

## 3. Kotva a metoda

Čteno bylo veřejné `main` po sloučeních z 8. 11. 2026 (00:07 až 00:33 UTC),
`STATUS.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`,
`canon/GATES.tsv`, příslušné oddíly `canon/CANON.md`, sondy a poznámky
posledních čtrnácti dnů, otevřené PR a větve (`git ls-remote`), konsolidace
z 7. 11. (větev PR #1952) a autorské podklady v `twistj-handoff` a v knize.
Lokálně prošly `tools/check_policy.py` (POLICY PASS) a `tools/check_ledger.py`
(LEDGER PASS, 609 claims, 26 gates). Osm nezávislých čtenářů po shlucích,
jedna syntéza a ověření klíčových tvrzení dvěma rozhodčími jsou zaznamenány
ve `VERIFICATION.md`. Statusy jsou výhradně slova programu: `T`, `D`, `C`,
`H`, `O`, `F` z registru; `candidate-T`, `candidate-C`, `PASS`, `UNRUN`,
`draft`, `NON-CANONICAL` ze souborů mimo registr.

## 4. Co se postavilo od mapy připravenosti v105 (23. 10.) do dneška

| Verze | Datum | Co přibylo pro stroj | Registr |
|---|---|---|---|
| v105 | 24. 10. | `HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T]`: záchyt, úplný prostorový proud a koherentní zápis přijímače v jednom zákonu, `p > 2/10^28`, asymptoticky | 577 |
| v106 | 27. 10. | sedm vět o koherentní procházce `W`, osm vět o konečných přístrojích (`THERMAL-ORIGINAL-PORT-APPARATUS`, `COMPACT-ACTIVE-RECORD-APPARATUS`, `LOCAL-THERMAL-TWO-ATTEMPT`, `OCCUPIED-RECORD-EXPORT-REUSE`, baterie, Diracův kontakt), návratová okna `U` | 593 |
| v107 | 1. 11. | integrální relativní kontakt: zákon, ostrá minima 12 a 27, kapacita bank `12N`, zbytková hranice pevného slova; otevřený vlastník společného přístroje | 598 |
| v108 | 3. 11. | společný přístroj pro dva experimenty na 56 místech uzavřen `O -> T`; čtyři věty o rytmu tří míst | 602 |
| v109 | 3. 11. | obnova týchž pracovních bank pro každé `k` (`26+25k` míst, účet `68+74k`, `2k` archivů); kopírka banky a překážka doslovné kopie; první tik, zrcadlo prenosu a 62-registrový obvod `[C]` | 609 |

Od v109 se registr nezměnil. Na `main` ale přibylo 1. až 8. 11. toto
(NON-CANONICAL, pokud není uvedeno jinak):

| Datum | Artefakt | Co to pro stroj znamená | Stav |
|---|---|---|---|
| 6. 11. | PR #1923, `notes/C-COMMON-COUNTER-PATH-PHASE-N` | nativní fáze vlákna je funkce čítače (žádná informace o cestě při společném čítači); na kontaktu nese cestu počet měnících kontaktů, nezávislý na hermitovském součtu `H` v `5 Z[phi]` (Theorem L, nalezen až po prvním běhu); hypotéza „počet mod 5 je lineární v H“ vystřelila | candidate-T, candidate-C, fired; bez dvouarchitekturního běhu |
| 8. 11. | PR #1908, `P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1` | jedno pevné slovo o 322 kontaktech nabije pólovou výšku `t` pro všech pět `t` v `{-2..2}`, pomocníci se vrátí, inverze 1288 kontaktů | PASS, candidate-C, obě architektury |
| 8. 11. | PR #1912, `P-POLE-HEIGHT-INTEGER-DOMAIN-1` | totéž slovo uspěje nad celými čísly právě pro těch pět `t` (55 dyadických válců, prázdná hranice) | COMPLETE, candidate-C |
| 8. 11. | PR #1915, `P-U-PAIR-PHASE-WORK-1` | nativní vlákno páruje tiky s přírůstky `+-e_k`, kapacita vyrovnání `2s`; žádný omezený koncový potenciál nedává nenulový lineární účet práce tik/zdvih | candidate-T, candidate-C |
| 8. 11. | PR #1857, `P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1` | stopky s deseti vstupy a dvěma razítky potvrzeny (100 hranic kroků, 200 konců čtení, 10 inverzí) | PASS, candidate-C |
| 8. 11. | PR #1819, #1821, `P-J-LAMBDA-CARRY-ARITHMETIC-1`, `P-CARRY-MOMENT-DEPTH-1` | vratný násobič `J` pro všechna `N` z malých sčítaček přenosu; přesné momenty přenosu se zpožděným mícháním zbytků; zdroje kompilátoru zrcadla | candidate-C s důkazy |
| 8. 11. | PR #1746, `notes/C-FORWARD-ONLY-CAPTURE-FILTER-N` + `reproduce/` | dopředný koherentní filtr po konečném nativním záchytu | NON-CANONICAL s reprodukcí |
| 8. 11. | PR #1761, #1764, #1766, tři tepelné poznámky | prostředí a téměř čisté registry; nabitý pracovní zásobník a hlavní hodiny z Gibbsových faktorů při třech teplotách (`D = 2^84`, `1 - q < 2^-82`); teplotní kontrast z jedné teploty a jednoho invertovaného palivového qubitu | candidate-T, analytické, bez verifieru |
| 8. 11. | PR #1636 až #1638, #1656, #1672, #1673 | uzavření šesti opuštěných pinů (K1 scaled bridge, Noether closure, Maurer–Cartan) jako ABANDONED | záznamy, ne věda |

Vyloučeno nebo vystřeleno ve stejném období: nabití pólové výšky `t = ±1`
čistě z neutrálních prvků s jedinou nabitou oporou (větve PR #1896, #1898,
candidate-T), zásoba `2u` (PR #1900), 131 ze 171 neutrálních zásob s
`Q <= 20` (PR #1902, #1904), hypotéza o úměře počtu a `H` (PR #1923),
sestup Gramových čteček přes nativní krok (PR #1950, obě hypotézy vystřelily)
a tři piny `P-INTEGER-K1-SCALED-BRIDGE-1..3` (vada součtu stavů, ABANDONED).
Rukopis ze 4. 11. ještě říká „tři vstupy z pěti umíme naložit jedním
společným slovem; všech pět zatím ne“; od 8. 11. platí všech pět.
Z knižního kroku „uzavřít pětivstupový zavaděč“ je tím splněna
existenční část; zbylých 31 nevysvětlených neúspěchů z censu zásob a
„propojit zavaděč s fázovou západkou a modální akcí“ zůstávají otevřené.

## 5. Stroj po částech

Tabulka `ASSEMBLY.tsv` má 42 řádků „stupeň/nosič“, každý s identifikátory
tvrzení, slovem statusu, cestou k evidenci a tím, co na místě chybí.
`check_assembly.py` ověřuje, že každé citované tvrzení existuje v registru se
stejným statusem, že každá poznámka a sonda existuje a že každý slot má
rozhraní. Výstup z 8. 11.: 73 odlišných citovaných řádků registru
(56 T, 7 D, 1 C, 7 O, 2 F), `ASSEMBLY PASS`.

Zhuštěně, `T`/`C` jsou statusy registru, `cand` sloučený NON-CANONICAL
kandidát, `-` prázdno:

```text
             S0    S1    S2    S3    S4    S5    S6    S7    S8
K1 nativní   -     -     T     -     T     T     T     -     -
K2 kontakt   -     -     T     cand  T     T     T     T     T
K3 registry  -     -     -     -     C     C     C     C     -
K4 pole      -     -     T     -     T     T     T     T     -
K5 procházka -     -     -     -     T     T     T     -     -
K6 tepelný   cand  cand  T+cand cand T     T     T     T     T
```

Účet na jeden cyklus, tam kde je cyklus dokázán, s přesnými čísly z Canonu;
žádný nosič nepočítá vlastní prostředí a žádný neobnoví spotřebovanou zásobu:

| Nosič | Jeden cyklus | Spotřeba čerstvé zásoby | Co se vrátí | Co zůstane |
|---|---|---|---|---|
| K2 kontakt | `U(a,d) = W K K W^-1`, 26870 kontaktů; `P_k` na `26+25k` místech, účet `68+74k` | dva čerstvé archivy na vstup, zbývající zásoba `2(k-j-1)` | celé 31místné jádro včetně bank, zdroje, hodin a voliče | `2k` archivů, které samy dekódují historii |
| K3 registry | 80705 primitiv a dva nativní tiky na vstup | jedna archivní buňka a jeden horní registr na uchované přenosy | 48 pracovních buněk a primární kontrolní bod po tiku | `high = s`, `archive = 3s`, druhý nativní výstup |
| K4 pole | řetězec `32N-1` souřadnic, celková energie 42 | žádná čerstvá banka; zdroj si ponechá 5 jednotek a druhý puls nevydá | 31souřadnicový přijímač v čase `N+1`, ukazatel `p = 1` | dvě jednotky v `q_(N-2)`; není to reset celého přístroje |
| K6 tepelný | dva pokusy pod jedním `H_local`; export záznamu `N` kol | `(N+1)S + 7N` zásobních qubitů; pásky, kazety, lázně a řadič se neobnoví | pracovní jádro výměnou, vnější historie v `3T_hold` | první výstup na pevných místech, exportované záznamy |
| K1 nativní | žádný cyklus | | | virtuální archiv v úplném stavu a čítači |

Čtení řádků:

- **K2 kontakt.** Jeden zákon (totální kontakt `C_rho`, přijetí při
  `x - y` v `2O`, `C^5 = I`), druhý dodaný primitiv `SWAP` („not a contact
  compilation“, `canon/CANON.md`, oddíl společného přístroje), účet
  `q(a) = (5 sum a_i^2 - (sum a_i)^2)/2`, kruhový součet a zbytky modulo
  `1 - j`. Čtecí jádro `S` o 535 kontaktech na 31 místech, kopírka `K` o 60
  kontaktech, cyklus `U(a,d) = W K K W^-1` a program `P_k` jsou doslovně
  skládatelné, protože sdílejí jeden označený nosič a abecedu. „Čerstvá banka“
  je `(-b, b)^5`, „záznam“ otočení jednoho páru o `rho`, „financování“
  znamená spotřebu čerstvosti předem umístěných bank při zachovaném účtu.
  Co Canon výslovně nedodává (`canon/CANON.md`, závěr oddílu o obnově
  pracovního jádra): syntézu surových vstupů, nakládání za běhu, autonomní
  rozvrh, regeneraci obsazených archivů, neomezenou historii na jednom
  konečném nosiči, kompilaci výměn do kontaktů, realizaci nativního `U`,
  fyzikální přístroj.
- **K6 tepelný.** `THERMAL-ORIGINAL-PORT-APPARATUS [T]`: pro `k >= 8` jeden
  kladný statický hamiltonián připraví zdroj a provede tři kroky `U_rec`,
  pravděpodobnost návěští `> 1/4`, všechno palivo, kopie a tepelné vady
  započteny, vlastní zachovaná energie, „no equality with original Q or
  measured-intervention closure“. `LOCAL-THERMAL-TWO-ATTEMPT [T]`: dva spotřební pokusy a
  výměna celého pracovního jádra, podmíněná chyba `< 2^-96`. Tři nové
  poznámky posouvají hranici přípravy: zásobník, hodiny a kurzor vznikají
  z Gibbsových faktorů, kontrast teplot z jedné teploty a paliva; každá sama
  říká, co zůstává dodané (nestacionarita, součinová hranice, vazby) a že
  neproběhl žádný výpočet ani verifier.
- **K1 nativní.** Deklarované `U` na `Omega = N_0 x F_5^6`, pět afinních
  involucí `a..e`, Thueův–Morseův volič. Umí: společnou připravenost a
  obnovu zdroje z úplného stavu a čítače (`U-NATIVE-COMMON-READY-SOURCE-RETENTION`),
  přenos zbytkového součtu a jeho přesné čtení z `(n, q_n, r_n)` s nejvýše
  dvacetihodnotovým souhrnem čítače (`U-NATIVE-RAW-RESIDUE-READOUT`), jeden
  rodinově specifický jednorázový přenos (`U-NATIVE-SOURCE-RECEIVER-RECORD`).
  Neumí, dokázáno: čtení jen z přijímače (`U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO`),
  trvalý zápis ze synchronizovaného BLANK (`U-NATIVE-INVARIANT-AND-NOWRITE`),
  autonomní kontext bez dodaného bitu (`U-RAW-RESIDUE-CONTEXT-BOUNDARY`),
  druhý přenos do čerstvého cíle v téže rodině
  (`U-NATIVE-RECORD-CONTINUATION-BOUNDARY`). Archiv je jen virtuální:
  „regenerating a history is not material recording“ (`canon/CORE.md`).
  Financované záznamy na doslovných nativních buňkách existují
  (`FIVE-PHASE-THREE-REFERENCE-RETAINED-RECORD`,
  `COMMON-HISTORY-FUNDED-AREA-RECEIVER`), ale jejich 182listový prefix je
  adresován zvenčí a jeho příprava a energie nejsou součástí účtu.
- **K3 registry.** Zrcadlo přenosu: skutečný první tik na 62 registrech
  `F_5`, 500 vstupů, 40348 primitiv, inverze je doslova obrácené slovo
  s invertovanými primitivy, 48 čistých pracovních buněk obnoveno. Je `[C]`, protože zapojení, rozvrh
  a druhý povolený nativní původ jsou dodané a nativní kroky nejsou globálně
  invertovány. Řádek `C` je doslova instance `N = 2` téhož kompilátoru
  (`layout(n)` má `14n + 22` buněk), jehož všeobecný vratný násobič `J`
  pro každé `N` (`136917 N` párových pulzů, `|c_j| <= 35` pro každý
  dosažitelný přenos) a momenty přenosu zůstávají NON-CANONICAL sondami
  sloučenými 8. 11.
- **K4 pole a buňkové zdroje.** Úplný konzervativní řetězec pro každé `N`,
  první příchod `N - 1`, práce `N`, návrat původního přijímače `N + 1`,
  vratný lokální ukazatel `C5`; financované zdroje a obsazené záznamy;
  rezidualní krok s vlastním záznamem. Návrat přijímače „is not a reset of
  the complete apparatus“ a odvození z `U` nebo `J` zůstává otevřené.
- **K5 procházka.** Spektrální čtení energie `H = i Log W`, baterie se
  přesným zachováním, vázaný pár, homogenní záchyt se zápisem. Záchyt je
  asymptotický; konečný čas pro obecné přípravy je otevřený (větve PR #1813,
  #1815, #1817, #1823 čekají na posudek).

## 6. Jak do sebe části zapadají

`INTERFACES.tsv` má 46 hran. Uvnitř nosičů jsou hrany většinou
`proved-composition`: na K2 celý řetězec S2 až S8 jednou větou, na K6
řetězec S0 až S8 (S0 až S3 jako kandidáti), na K1 S2 až S6, na K4 S2 až S7,
na K3 S4 až S7 jako `C`. Mezi nosiči jsou hrany buď
`declared-not-identified` (Canon sám říká, že to nejsou tytéž objekty), nebo
`missing-bridge`. Jediná dokázaná hrana mezi nosiči je B2 na úrovni `C`.

Čtyři mosty a co o nich dnes víme:

- **B1 kontakt a nativní `U`.** Pevné kontaktní slovo mění vektor zbytků
  modulo `1 - j` jen jednou permutací míst nezávislou na vstupu
  (`RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY [T]`). Z pěti nativních
  generátorů je permutací souřadnic jen `a`; `b`, `c`, `d`, `e` obsahují
  negace a posuny (`canon/CANON.md`, blok generátorů v oddílu o křivosti).
  Doslovné ztotožnění kontaktního slova s `U` na úrovni zbytků je tedy
  vyloučeno pro každé slovo, které na zbytcích není identita nebo `a`. To je
  poznámka odvozená ze dvou registrovaných řádků, ne tvrzení; říká, kde most
  být nemůže. Jediná brána z nativního do kontaktního světa je
  `(q, r) -> eta(q, r)` a ta je dokázaně slepá napříč rodinami zpráv
  (`U-CONTACT-SOURCE-NONINTERFERENCE [T]`).
- **K4 a K2, okruhová shoda bez přenosu.** Zdrojová souřadnice polního
  řetězce se ztotožňuje s `O = Z[j]` (`SOURCE-WORK-SHARP-SIX-DIGIT-REPRESENTATION [T]`,
  `A_f` je násobení `j`) a faktor `A = Z[J]` zdrojů JM je týž okruh
  s Gramovým blokem rovným dvojnásobku kontaktního účtu `q`
  (`JM-RESULTANT-TRACE-SEAM [T]`). Okruh je společný; žádná věta však
  nepřenáší připravený stav ani záznam z polní buňky na `O^m` nebo zpět.
- **B2 nativní `U` a registry.** Existuje jako konečný výpočet
  (`U-CARRY-MIRROR-FINITE-CIRCUIT [C]`). Povýšení by chtělo nativní tik na
  celé deklarované připravené množině bez dodaného původu a s inverzí, která
  není jen obrácené slovo.
- **B3 celočíselné nosiče a procházka.** `COHERENT-W-LOCALIZED-RING-CLOSURE [T]`
  odděluje surové `O`, amplitudy `O[1/5]` a zbytky `F_5` a dokazuje, že
  žádná unitální mapa `O[1/5] -> F_5` neexistuje. Poznámka #1923 ukazuje, že
  na kontaktu je veličina citlivá na cestu počtem, kdežto polostopa a
  hermitovský součet jsou funkce koncových bodů; vztah mezi nimi by byl
  normalizací amplitudy a „none follows from these results“. To je přesně
  třetí úkol vlastníka. Jediná registrovaná hrana mezi procházkou a nativním
  `U` je `COHERENT-W-LOCAL-NATIVE-NETWORK [T]`: stín surové `W` modulo pět
  je semikonjugovaný na `U_net`, tedy na buňkové nativní `U` s dodatečnou
  vazbou každý třetí tik, a Canon dodává, že tato vazba není odvozena
  z původního kroku; záznamový krok `U_rec` „is not an intertwiner“
  původního `U`.
- **B4 tepelný nosič a procházka.** Existuje na úrovni původního portového
  zařízení s vlastní energií; rovnost účtů není dokázána a bootstrap
  nestacionaritu dodává.

Výsledek dnešního auditu rozhraní uvnitř K2 (`check_loader_interface.py`,
výstup `check_loader_interface.stdout`): zavaděč vydává pár `(u + tB, u - tB)`
se zbytky `(0, 0)` pro všechna `t`, hodiny stopek jsou `(2, 3)`, zdroj
`(0, 2, 0)` po celé oběžné dráze s periodou devět; kontakt zachovává zbytky
(ověřeno vyčerpávajícím způsobem na 390625 párech z krabice `[-2, 2]^4`), takže
žádné kontaktní slovo nepřevede výstup zavaděče na vstup stopek bez
vypůjčených míst se zbytky 2 a 3 a bez odstavení páru se zbytkem 0. Spojení
zavaděče a stopek je přeznačení se zásobou, ne transformace páru. Výraz
„pólová výška“ není v žádném připnutém souboru definován; nabíjené množství
je celé číslo `t` v `B_t = t(1 - j^2)`.

Kde se aparátová linka vůbec dotýká fyzikálního žebříku, říká
`canon/DEPENDENCIES.tsv`: do vlastníka `QDD-INSTRUMENT-APPARATUS` vede
66 hran `BOUNDED_BY`, z toho 12 z aparátových řádků (osm nativních čtení a
hranic, `HOMOGENEOUS-CAPTURE-CURRENT-RECORD`, `FIELD-RETAINED-CONTACT-ARCHIVE`,
`SIGNED-PORT-OCCUPIED-REVERSIBILITY`, `FUNDED-CONTACT-INVOLUTION`); všech
dvanáct řádků `RELATIVE-CONTACT-*` a čtyři řádky zrcadla přenosu mají hrany
jen mezi sebou, k `J-UNIT` a k definicím, a žádnou ke slovníku, metrologii,
fotonu, barvě ani kosmologii. Stroj se tedy k fyzice váže výhradně jako
mez (bound), ne jako splátka (discharge), a kontaktní jádro se k ní neváže
vůbec.

Účtů je nejméně šest a jsou to různé veličiny: nativní zachované štítky,
kontaktní polostopa `Q`, vratnost registrů, celočíselná energie buněk,
spektrální energie `W` a holá energie `H_0` tepelných přístrojů (vedle nich
ještě spektrum hodin kompaktního přístroje a znaménkový účet Diracova
kontaktu). Žádný registrovaný řádek neztotožňuje dvě z nich; Canon to pro tepelné, spektrální a kontaktní účty říká slovy „none
of these statements equates its conserved account with every other time
generator“ (`canon/CORE.md`).

## 7. Co je vyloučeno

Hranice, které stavbu stroje omezují a jsou registrované nebo sloučené:

- uchování `N` výsledků vyžaduje alespoň `4N` měnících se pomocných míst a
  účet `12N`; čistá obnova banky při uchovaném výsledku neexistuje
  (`RELATIVE-CONTACT-RETAINED-BANK-CAPACITY [T]`);
- doslovná kopie banky na čtyřech místech bez další reference neexistuje
  (`RELATIVE-CONTACT-FOUR-PLACE-COPY-OBSTRUCTION [T]`);
- `B` pětihodnotových bank unese nejvýše `5^B` historií, takže jeden konečný
  nosič neunese neomezenou historii (`canon/CANON.md`, obnova pracovního jádra);
- čtení jen z aktuálního přijímače je konstantní; žádný konečný autonomní
  kontext nezávislý na zdroji to neopraví
  (`U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO [T]`, `U-RAW-RESIDUE-CONTEXT-BOUNDARY [T]`);
- pevná čtečka s konečnou pamětí nevyrobí z `U` nezávislé hody na všech
  délkách bloků (`U-FINITE-READER-INDEPENDENCE-OBSTRUCTION [T]`); ostré
  čtení pěti bodů volným kódováním s klasickým koncovým čtením neexistuje
  (`U-POINT-SOURCE-SHARP-READOUT-NOGO [T]`);
- měřitelná cesta A od substrátu k míře je prázdná
  (`ENTROPY-MEASURABLE-OBSTRUCTION [T]`, `ENTROPY-LAYER-BRIDGE [F]`) a
  kanonický selektor TM-SYM2 neexistuje (`TM-SYM2-MEASURE [F]`);
- žádná unitální mapa `O[1/5] -> F_5` (`COHERENT-W-LOCALIZED-RING-CLOSURE [T]`);
- omezený koncový potenciál s lineárním účtem tik/zdvih má nulové
  koeficienty (`P-U-PAIR-PHASE-WORK-1`, candidate-T);
- nabití liché pólové výšky z neutrálních prvků a zásoby `2u` (větve
  PR #1898, #1900, candidate-T).

## 8. Co chybí, seřazeno podle toho, co by posunulo celý stroj

Pořadí je podle přínosu pro uzavřený cyklus, ne podle snadnosti.

1. **Společný nosič a sjednocení účtů (B3, B4).** Bez něj zůstane prostředí
   a bootstrap na tepelném nosiči a obnova s archivy na kontaktním, a žádná
   věta neřekne „tento stroj od prostředí po opakování“. Vlastník: žádný
   registrovaný; nejbližší `SCHEME-DICTIONARY [O]`. Rozhodnutelný krok:
   zmrazit vložení a výrok, který účet se mapuje na kterou energii, na
   deklarované rodině příprav. Proveditelnost: otevřený výzkum.
2. **Přístroj z původního kroku (B1).** Vlastník
   `QUADRATIC-MEMORY-NATIVE-CONTACT [O]`; rozhodovací podmínka chce nezávisle
   připuštěnou `C` a globální permutaci s přesnou inverzí a certifikátem všech
   dosažitelných stavů; „missing interface, failed search, subclass no-go or
   failure of one C is STOP, not negative closure“ (`canon/FRONTIER.md`).
   Krok: nejdřív zmrazit přípustnou nativní třídu, teprve potom hledat.
   Proveditelnost: otevřený výzkum.
3. **Uzavřený cyklus na kontaktním nosiči (`CC-CONTACT` ve smlouvě).** Chybí
   dokázané S3 ve vstupním dialektu stopek. Krok: ohraničené hledání pevného
   slova, které z výstupu zavaděče a vypůjčené zásoby se zbytky 2 a 3 vyrobí
   `X_r` a vrátí pomocníky; případně kompilace pěti výměn do kontaktů
   (swapované páry mají shodné zbytky, čtyřmístná překážka se nevztahuje).
   Proveditelnost: dny; neúspěch hledání nic nedokazuje.
4. **Uzavřený cyklus na tepelném nosiči (`CC-THERMAL`).** Chybí čtečka
   jen z archivů a nezávislé přijetí tří bootstrap poznámek. Krok: posudek
   stejného typu jako `notes/C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N` a
   jeden verifier pro konečné součty v `PREPARATION.md`. Proveditelnost: dny.
5. **Povýšení B2 z `C`.** Krok: vratné slovo, které po uchování `h = s`,
   `k = 3s` vrátí oba registry na prázdno kopií do dvou čerstvých buněk, a
   spočítané čerstvé buňky na běh, srovnané se dvěma archivy na vstup u
   pracovních bank. Druhý krok: připojit `8` pětihodnotových buněk čítače
   k 62 registrům a zapsat celý osmikrokový rozvrh včetně obou nativních
   tiků jako jednu pevnou permutaci 70 buněk, aby rozvrh přestal být
   dodaným řízením (sekce 8 `notes/C-J-LAMBDA-CARRY-N/THEOREMS.md` už
   definuje hodinový unitár `V_N`, „not self-stopping“). Proveditelnost: dny.
6. **Nejmenší postačující statistika čítače pro nativní čtení.** Rozhodnuto
   touto nocí (`check_native_counter_statistic.py`): mapa `kappa -> (q_n, r_n)`
   je pro každé `n >= 3` funkcí souhrnu `T_n^read` (to je obsah inverzního
   vzorce ve větě), všech 20 hodnot souhrnu nastane před `n = 64`, graf
   kolizí mezi 20 podpisy má 90 hran a chromatické číslo 5. Souhrn
   `(sigma_n, N_n mod 5)` o deseti hodnotách stačí (`z_n` je nadbytečné),
   `N_n mod 5` samo nestačí a žádný postačující souhrn nemá méně než pět
   tříd; explicitní pětitřídní tabulka je ve výstupu skriptu. Je to důsledek
   registrované věty a konečného výpočtu, NON-CANONICAL; mění jen hranici
   S6/K1, ne stroj. Zbývá nezávislé přečtení a případně hezčí tvar tabulky
   (žádný afinní vzorec v `N`, `sigma`, `z` z 500 zkoušených nevyhovuje).
7. **Zákon výskytu.** Přijatý na `D`; po vlastní dohodě programu není slotem,
   který by konstrukce zaplnila (oddíl 9). Vlastníci
   `QDD-TERMINAL-EVENT-SEMANTICS [O]`, `QDD-INSTRUMENT-APPARATUS [O]`.
   Manifest přístroje v Canonu má 26 polí, z nich 24 `UNRESOLVED`
   (`projector_target_ids` jsou jen algebraické cíle,
   `l6_measure_boundary = REQUIRES_SEPARATE_GATE`). Jediný rozhodnutelný
   krok je tabulka pokrytí: pro nejlepší existující konstrukci (56místný
   společný přístroj nebo homogenní záchyt) zapsat ke každému z 26 polí,
   zda je pro ni definováno a kým; to nic nezavře, ale ukáže, kolik polí
   je definiční práce a kolik fyzika.
8. **Převod jednotek.** `METRO-EDGE-SCALE [O]`, `SCHEME-DICTIONARY [O]`;
   stroj k nim dnes nic nepřidává.

Procesní dluh, který stavbu brzdí, zaznamenala konsolidace z 7. 11.
(`UNMERGED-WORK.md`, větev PR #1952); její README zapisuje, že 8. 11. po
souhlasu vlastníka bylo šestnáct PR sloučeno (deset s obsahem, šest
záznamů ABANDONED) a patnáct překonaných PR zavřeno s ponechanými větvemi.
Otevřených PR je k ránu 8. 11. 189. Pro stroj z toho zbývá: rozhodnout šest
větví pólové výšky #1896 až #1906 (úplné záznamy, pro existenci překonané
slovem W322), posoudit #1910, #1917, #1930 s #1942, #1950 a #1953, #1956,
#1957 jedním posudkem na dvojici, a především custody: nároky v issues
#1920 až #1947 (čtení komutátoru kontaktu, společné hodiny, nativní
přenos číslic, statická Gaussova fáze, modální mezera, archiv absorpční
fáze a další) hlásí dokončené první běhy v samostatných git bundlech, které
„nejsou předkem veřejného main“ a nemají vzdálenou větev, přitom je #1930,
#1953 a #1957 už citují. Dokud nejsou na veřejné větvi, nejsou pro stroj
evidencí. Samostatně: PR #1952 má po sloučeních červené CI jen proto, že
`check_verifier.py` vidí v merge commitu šestnáct nových adresářů sond;
spraví to merge `main` do jeho větve.

## 9. Poctivý odhad, jak daleko stavba je

Měřeno stupni cyklu: na kontaktním nosiči je sedm z devíti stupňů
registrováno jako `T` (S2, S4 až S8) a osmý (S3) je sloučený kandidát;
na tepelném nosiči je dotčeno všech devět, z toho pět jako `T` a čtyři jako
kandidáti bez verifieru; na nativním nosiči čtyři z devíti. Měřeno mosty:
jeden ze čtyř, a ten jako `C`. Měřeno tím, co dělá stroj fyzikou: nula ze tří
(výskyt, realizace, jednotky), přičemž první z nich je podle textu programu
přijatá volba, ne nevyplněný slot.

Jinak řečeno: část „matematický stroj na jednom celočíselném nosiči se
spočítanou spotřebou“ je hotová z větší části a lze ji dnes formulovat jako
jednu větu s přesnou hypotézou (`CC-CONTACT`), jíž chybí jediný stupeň.
Část „stroj, který si sám připraví zdroj z tepla“ existuje jako analytický
kandidát na jiném nosiči. Část „stroj, který je fyzikou“ není o kousek blíž
než 23. 10.; registr to říká sám: 26 živých vlastníků z v105 zůstalo při
v105 až v109 beze změny. Jediný vlastník, který se v tomto období pohnul, je
`RELATIVE-CONTACT-COMMON-APPARATUS-OPEN`: ve v107 byl přidán jako `O` a ve
v108 uzavřen kladně `O -> T` konstrukcí na 56 místech; byl to matematický
vlastník uvnitř K2, ne fyzikální. Konsolidace ze 7. 11. formuluje totéž slovy „More
constructions of the same kind do not move those owners; the definition work
they ask for does.“ Tato mapa a smlouva jsou kus té definiční práce; věty
samy nedodávají.

Tempo posledních dnů (pět aktivací od 24. 10. do 3. 11., deset vědeckých
sloučení a šest uzavřených opuštěných pinů během jedné noci 8. 11.) šlo do
oplocení a do kompozice uvnitř K2 a K6. To je v souladu s metodou
programu, ale je třeba to říci nahlas: bez rozhodnutí vlastníka o mostech B1
a B3 (jaký nosič je „ten“ nosič) povede další tempo k sedmému stroji, ne
k jednomu.

## 10. Nejmenší další rozhodnutelné kroky

Proveditelné bez nové premisy, v pořadí podle oddílu 8:

1. Rozhodnout, zda `CC-CONTACT` je cílem příštího foldu: pak zmrazit kontrakt
   S3 (vstupní dialekt stopek, povolená zásoba) a spustit ohraničené hledání
   překladového slova; skript z této mapy dává nutnou podmínku (zbytky).
2. Objednat nezávislý posudek tří tepelných poznámek a #1923 ve stylu
   `C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N`; bez něj zůstane S0 až S2 na K6
   kandidátem a Theorem L bez přijetí.
3. Dořešit šest větví pólové výšky a #1950 jako záznamy (sloučit nebo
   uzavřít, větve nechat).
4. Spočítat nejmenší postačující statistiku čítače (oddíl 8, bod 6) a
   nejmenší energetické reprezentanty po hranicích `n <= 64` pro
   `U-NATIVE-UNIT-LIFT-OBSTRUCTION`; obojí je jednodenní přesný výpočet.
5. Teprve potom se vracet k B1 a B3, a to zmrazením tříd, ne hledáním.

Co udělala tato noc: smlouvu (`notes/canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`),
tabulky a jejich kontrolu (`ASSEMBLY.tsv`, `INTERFACES.tsv`,
`check_assembly.py`), audit rozhraní zavaděče (`check_loader_interface.py`)
a tuto mapu s ověřením (`VERIFICATION.md`). Nic z toho nemění registr.

## 11. Co tato mapa nedělá

Nezakládá status, nepropaguje žádný kandidátský výsledek, neotvírá sondu,
nemění `canon/`, nezavírá žádného vlastníka a nenahrazuje kolizní sken ani
rezervaci pro žádný z navržených kroků. Kde se liší od registru, platí
registr.

## 12. Soubory

- `README.md`: tato mapa.
- `ASSEMBLY.tsv`: 42 slotů stupeň/nosič s tvrzeními, statusy, evidencí a tím,
  co chybí.
- `INTERFACES.tsv`: 46 hran s druhem rozhraní a evidencí.
- `check_assembly.py`, `check_assembly.stdout`: mechanická kontrola obou
  tabulek proti `canon/REGISTRY.tsv` a stromu; `ASSEMBLY PASS`.
- `check_loader_interface.py`, `check_loader_interface.stdout`: audit
  zbytků zavaděče a stopek; `LOADER-INTERFACE RESIDUE AUDIT PASS`.
- `check_native_counter_statistic.py`, `check_native_counter_statistic.stdout`:
  nejmenší postačující souhrn čítače pro pevnou nativní čtečku zbytku;
  validace proti tabulkám Canonu, pak chromatické číslo 5;
  `NATIVE COUNTER STATISTIC AUDIT PASS`.
- `VERIFICATION.md`: metoda a verdikty ověření klíčových tvrzení.
- `../canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`: typovaná smlouva
  stroje, `STOP-DEFINITION`.
