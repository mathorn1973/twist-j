# Nezávislý slepý posudek PR #1862 — fáze 1

Složka `/work/posudek` obsahuje právě tři soubory:

- `PREREG.md` — zmrazený seznam kontrol C0–C12, kontrakt odvozený jen
  z markdown textů PR a mé explicitně zmrazené konvence K1–K8
  (sepsáno před prvním spuštěním ověřovače).
- `review.py` — můj vlastní ověřovač psaný od nuly: vlastní přesná
  polynomiální aritmetika prstence `Z[t]/(1+t+t^2+t^3+t^4)`, vlastní
  kompilace slova kontaktů z maker V/D a mintermů, vlastní kontrolní
  součty a fingerprinty hranic (konvence K6/K7).
- `README.md` — tento popis.

## Nezávislost

Autorka posudku je Emmy (Muse Wonder Full), jiná rodina modelů, než
má autor PR. Vycházela jsem pouze z textů
`notes/C-COLLATZ-CONTACT-STEP-RECORD-N/*.md` v slepém checkoutu
(85255b14f40a7a853d261ffcc19dc96fa850be44, bez historie gitu).
Autorovy soubory `verify.py`, `break.py`, `EXPECTED.txt`,
`BREAK-EXPECTED.txt`, `COMPARISON.json` a `SHA256SUMS` byly skryté
a neotevřela jsem je; žádný očekávaný výstup se nečte a závěr
`review.py` je dán pouze jeho vlastním výpočtem. Tabulka (m,v) se
v kompilátoru počítá z definice `3n+1`, nikoli přepisuje z textu
(s textem se srovnává jen jako kontrola C3). Konvence, kam text
nedosáhne, jsou zmrazené v `PREREG.md` §2 a při pozdějším porovnání
s autorem je bude třeba převést (zejména serializace fingerprintů).

## Spuštění

```sh
cd /work/posudek
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 review.py
```

Program tiskne PASS/FAIL ke každé kontrole C0–C12 a končí nulou
jen při úplném PASS. Kontrola C9 (4096 skip případů) je výslovně
na úrovni abstraktních maker, ne primitivní replay; ostatní běhy
(trajektorie, obsazená pokračování, inversy) jedou primitivními
kontakty. Plný běh autorova programu ani porovnání s jeho výstupy
v této fázi neproběhlo — patří do fáze 2 po zmrazení tohoto kódu.
