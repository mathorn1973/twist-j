# Výsledek nezávislého posudku PR #1865 (fáze 2)

Rozhodnutí: **PASS S POZNÁMKOU**.
Žádný DIFF-REAL mezi mým zmrazeným ověřovačem z fáze 1 a autorovými
programy nebyl nalezen. Poznámky (ne porušení kontraktu) jsou dole.
Kandidát zůstává NON-CANONICAL / L1, jak ho značí texty PR; tento posudek
žádný status v kánonu nezvyšuje a nic netvrdí o opakovaném provozu,
obnově zdroje, volbě q=3 silou J ani o fyzikální realizaci.

## Pořadí a zmrazení

Sha256 souborů v /work/posudek před jakýmkoli během fáze 2 seděly přesně
na zveřejněné zmrazení (commit d5d9b3231a4086d75790cbd4f81cd212aaecf5cc):
PREREG.md 26a091d8…, README.md a133f5c5…, review.py df438b62…
(plné hodnoty v COMPARISON.json). Můj kód se ve fázi 2 neměnil.

## Běhy na tomto stroji (aarch64, Python 3.12.3)

- Můj `review.py --scope full`: exit 0, `RESULT PASS`, PASS R01–R17,
  stejná klíčová čísla jako ve fázi 1.
  [RUN-REVIEW.txt](RUN-REVIEW.txt) 944 B, sha256
  6d26f41137bb10bdd0334591285afac81d1c217925b688e2fe8849ff737c682e;
  stderr 0 B.
- Autorův `verify.py` (env a příkaz dle jeho RUN.md, z kořene repa):
  exit 0, stdout 747 B sha256 6512d4a2…; `cmp` proti jeho
  EXPECTED.txt: IDENTICKÝ. Stderr 0 B.
- Autorův `blindbreak.py`: exit 0, stdout 993 B; `cmp` proti jeho
  BREAK-EXPECTED.txt: LIŠÍ SE, ale políčkový JSON diff našel jediné dvě
  rozdílné položky z 25: `architecture` x86_64→aarch64 a
  `python` 3.12.14→3.12.3. Všechna vědecká pole (počty, hashe,
  histogram) jsou shodná. Stderr 0 B.
- Autorovo `sha256sum -c SHA256SUMS` v jeho složce: 12 souborů OK,
  exit 0.

## Jednostranné vyřízení 4a–4d

4a Počty: moje 2048/576/225/1, 2850 inverzí a 213750 kontaktů == autor
   (verify i blindbreak). Jak autor počítá (verify.py): aplikace počítá
   čítač `APPLICATIONS` v `word()` (ř. 88), tedy 15 dopředu + 60 inverze
   = 75 na případ, včetně cache hitů (`contact` ř. 59–61 vrací CACHE,
   ale čítač běží); závěrečný audit párů (ř. 200) volá `contact` přímo a
   do APPLICATIONS se nepočítá. `distinct_pair_inputs=len(CACHE)`
   (ř. 212) = 48772, měřeno až po uzávěru auditu párů.
   Poznámka: ř. 212 tiskne `forward_cases=2850 native_inverses=2850`
   jako pevné literály, ne čítače. Smyčky (ř. 181, 187, 191, 196) ale
   dávají přesně 2048+576+225+1 volání `audit` a každé asertuje jednu
   plnou inverzi (ř. 169–170), takže literály jsou pravdivé, jen
   nejsou naměřené. Blindbreak `native_inverse_cases` počítá jako
   součet korpusů (ř. 290) a aplikace čítačem `Lane.calls` (ř. 170).
   Můj kód inverze i kontakty přímo počítá (2850; 2850×75=213750)
   a rozlišené páry sbírá během dopředného i inverzního slova: 48772.
4b Histogram: můj {1:1024, 2:512, 3:256, 4:128, 5:64, 6:32, 7:16, 8:8,
   9:4, 10:2, 11:1, 12:1} == autorův DEPTH_COUNTS (verify) i
   q3_depth_histogram (blindbreak) == můj nezávislý přepočet z v2(3n+1).
   Korpus pokrývá každou hloubku 1..12 (verify to i asertuje:
   set(counts)==1..12). Hloubky 11 a 12 mají po jednom případu.
4c Fingerprinty: syrové se liší jen serializací. Moje hrana
   `0>1;…;0>15` (65 B) dává 70209eab…; autorova `i,j\n` (66 B, verify
   ř. 207) eb37b5b2…. Explicitní převod mého payloadu (parse `;`/`>`
   → řádky `i,j\n`) dal přesně eb37b5b2…. Můj boundary payload
   (řádky `n=…|slot;…`, 379591 B) dává 9ed972dd…; autorův kompaktní
   JSON `[[n,state],…]` bez koncového \n (449224 B, verify ř. 208)
   e7aa8abf…. Parse mých řádků a re-emise autorovým JSON dal přesně
   e7aa8abf… a výsledný payload je `cmp` IDENTICKÝ s payloadem z
   autorova `blindbreak.py --boundaries-out` (449224 B): všech 2048
   finálních stavů je tedy shodných stav po stavu. Verdict:
   DIFF-CONVENTION syrově, MATCH po převodu.
4d Meze: 4352 ani obecné 272(m²−n²) netestuje žádný autorův program
   (grep ve verify.py i blindbreak.py: žádný výskyt 4352/2460/6812 ani
   rozdílu účtů; blindbreak jen tiskne řetězec účtu `272*n^2+12`).
   Moje R16 ověřila jen aritmetiku 2460→6812 a symbolickou identitu
   jako nutnou podmínku. PR to samo značí symbolicky, ne jako běhový
   test: PROOF.md ř. 281–299 („separate necessary account bound“),
   BREAK-SCOPE.md ř. 77–79 („not an extra executable test“),
   REVIEW.md ř. 192 („symbolic boundary, not an extra executed test“).
   Dosažení meze nikdo netvrdí ani neověřuje.

## Co ověřil čí kód a v jakém rozsahu

Můj review.py: R01–R17 dle PREREG fáze 1. Obecné symbolické identity
(sympy): prefix C01/C02 pro volná q,n; účet a součet zdroje; jeden
kaskádní krok C(2Y,0); Q≥0 přes vlastní čísla; normy; algebra meze.
Konečné korpusy 2048+576+225+svědek: uzavřené tvary, přijetí/odmítnutí,
čtečka, inverze, archivy, páry, záporné sondy čtečky (R14).
Autorův verify.py a blindbreak.py: tytéž konečné korpusy a asserty
(formule, účty, součty, rezidua, páry C^5/inverze, inverze, DEPTH_LIMIT);
obecné symbolické kroky jen textem PROOF.md, ne programem. Blindbreak
navíc explicitně kontroluje sled přijetí a lichost m; verify přijetí
samostatně nezaznamenává (plyne mu z tvarů a čtečky).
Podrobná mapa R01–R17 je v COMPARISON.json.

## Co CI

Jediné workflow (.github/workflows/policy.yml) běží tools/check_* a
`tools/check_verifier.py --base …`, který vybírá jen změněné složky
pod `probes/` (changed_probes, parts[0]=="probes"). Vědecké programy
v `notes/` CI tedy nespouští — shodně s tvrzením PR. Žádné zde běhy
nejsou důkazem od CI; dvouarchitekturovou vědeckou bránu kánonu jsem
neposuzoval (můj aarch64 replay obou autorových programů je jen
pozorování na tomto stroji, autorovy záznamy jsou x86_64).

## Co zůstalo neověřeno

Obecná věta mimo moje symbolické identity a text PROOF.md (tu jsem
strojově nedokazoval v Leanu); příprava zdroje E_q z jednoho surového
slotu, obnova/reload, dosažení meze 4352, neomezená hloubka/opakování,
fyzikální interpretace, status v kánonu. Negativní sonda z fáze 1
(záměna hrany) zůstává jen v /tmp/negprobe.

## Co nezávislost je a co ne

Je: fáze 1 psaná slepě jen z rovnic a textů PR, vlastní PREREG a kód
zmrazené a zveřejněné před otevřením autorových souborů; jiné
serializace, dvojí násobení a dvojí Q uvnitř mého kódu; autorovy
programy ve fázi 2 jen spuštěné a srovnané, neměněné.
Není: nezávislost na specifikaci — rovnice, korpusy, svědek i konvence
slova jsou převzaté z textu PR, a všechny tři programy tedy ověřují
týž deklarovaný kontrakt, ne různé formalizace. Autorovy dvě větve
vznikly v autorových podagentních relacích (kontext úkolu), takže
shoda verify×blindbreak sama samostatný posudek nenahrazovala; tento
posudek je třetí, osobně oddělená implementace. Shoda po převodu
konvencí dokládá stejnou matematiku na daných vstupech, ne správnost
premis (zdroj, zisk q, čtečková normalizace) ani žádný fyzikální nárok.
