# Slepý nezávislý posudek PR #1865 — fáze 1

Tato složka je vlastní nezávislý ověřovač kontraktu
`C-CONTACT-AFFINE-NUMERATOR-CASCADE-N` z textů PR #1865
(`notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/` v checkoutu
`b67b5f0783a81bd38475eefc4d10dfaa4ff78bda`), psaný slepě ve fázi 1.

Nezávislost: autorův `verify.py`, `blindbreak.py`, `EXPECTED.txt`,
`BREAK-EXPECTED.txt`, `COMPARISON.json` ani `SHA256SUMS` nebyly otevřeny,
spuštěny ani použity jako očekávané hodnoty; v checkoutu jsou skryté
(seznam v `/work/repo/twist-j.SLEPY-REZIM.md`). `review.py` nečte žádný
soubor. Všechny kontroly srovnávají iterované primitivní kontakty proti
uzavřeným tvarům a symbolickým identitám odvozeným jen z rovnic a textu PR
(a citovaného kánonového řádku `RELATIVE-CONTACT-INTEGRAL-LAW` `[T]`,
/canon/REGISTRY.tsv:595, jen jako jméno autority kontaktu). Fingerprinty
jsou podle mé vlastní zmrazené serializace (PREREG.md, konvence K4) a
s autorovými čísly se v této fázi neporovnávají; při pozdějším porovnání
bude třeba převést konvence K1–K5 z PREREG.md.

Soubory:

- `PREREG.md` — zmrazený seznam kontrol R01–R17 s kritérii PASS/FAIL,
  sepsaný před prvním spuštěním ověřovače.
- `review.py` — vlastní implementace od nuly: dvojí násobení v O=Z[j]
  (redukce modulo 1+j+j^2+j^3+j^4 a cyklická konvoluce délky 5), dvojí Q
  (uzavřený tvar a Tr(z*z̄)/2), kontakt z definice, vlastní sestavení
  15-hranového slova, čtečka jen z aktivního + 13 kaskádních slotů,
  plná inverze (obrácené hrany, 4 kontakty na hranu), symbolické
  kontroly přes sympy. Přesná celočíselná aritmetika, žádný float.

Spuštění (z této složky):

```sh
cd /work/posudek
python3 review.py --scope full     # plný rozsah: 2048 + 576 + 225 + svědek
python3 review.py --scope sample   # jen ladicí podvýběr, ne výsledek posudku
```

Program tiskne PASS/FAIL pro každou kontrolu R01–R17, počty, rozdělení
hloubek a mé fingerprinty; skončí kódem 0 jen při úplném PASS, jinak
vypíše `RESULT FAILURE` a skončí kódem 1.

Negativní sonda (kopie mimo tuto složku, `/tmp/negprobe/`): jediná změna
poslední hrany `(0,15)` na `(0,14)` dává `RESULT FAILURE`, exit 1,
s FAIL u R08, R09, R10, R13 — ověřovač tedy porušení slova opravdu hlásí.

Rozsah tvrzení: symbolické kontroly R05–R07 (a R02/R03/R16 algebra) jsou
identity nad deklarovanými definicemi; ostatní je konečný výpočet na
korpusech z PREREG.md. Mez 4352 (R16) je ověřena jen jako nutná podmínka
ze zachování Q, žádná dosahující konstrukce se netvrdí ani nehledá.
Posudek nic netvrdí o opakovaném provozu, obnově zdroje, volbě q=3,
fyzikální realizaci ani o statusu v kánonu a žádný status nezvyšuje.
