<!-- SPDX-License-Identifier: Apache-2.0 -->

# Záznam ověření mapy stavby stroje (NON-CANONICAL)

```text
STATUS:        NON-CANONICAL VERIFICATION RECORD, PRŮBĚŽNÝ
AUTORITA:      ŽÁDNÁ
METODA:        osm nezávislých čtenářů po shlucích (nativní U, kontaktní
               aparát, tepelná a energetická vrstva, aritmetika přenosu,
               polní automaty a zdroje, měření a výskyt, rozpracované PR,
               fyzikální žebřík), jedna syntéza, 23 klíčových tvrzení
               každé přezkoumané dvěma nezávislými rozhodčími s odlišnou
               optikou (text registru a Canonu proti primárním záznamům
               a přepočtu), výhradně čtení; mechanické kontroly
               check_assembly.py, check_loader_interface.py a
               check_native_counter_statistic.py
LOKÁLNÍ HLAVA: a8482d06 (main po sloučení PR #1673), Public Canon v109
FORMAL RUN:    NONE
```

Tento soubor je průběžný snímek: čtenáři a rozhodčí ještě běží. Konečná
tabulka verdiktů nahradí tento text ve stejném souboru.

## Verdikty klíčových tvrzení (průběžně)

| # | Tvrzení (zkráceno) | Verdikt | Korekce zapracovaná v mapě |
|---|---|---|---|
| K1 | STATUS.md deklaruje v109, hash a bajty; registr 609 a snímky v105 až v109 | CONFIRMED (2x) | |
| K2 | dvanáct řádků RELATIVE-CONTACT-* je T; evidence workbank reuse je INLINE_CANON, společný přístroj a minima PUBLIC_PROBE two-architecture | CONFIRMED (2x) | §1 mapy přeformulován: dvouarchitekturní evidenci mají minima a společný přístroj, obnova pro každé k má inline důkaz |
| K3 | CHANGELOG v109 věta o oddělených nosičích; v107 přidání O, v108 uzavření O -> T | CONFIRMED (2x) | |
| K4 | U-CARRY-MIRROR-FINITE-CIRCUIT C; 40348 primitiv, 62 registrů, 500 vstupů, inverze obrácené slovo | WEAK (2x) | „50 buněk včetně 48 pracovních“ je znění registru a CORE, ne těla oddílu; inverze je obrácené slovo s invertovanými primitivy; opraveno v §5 a ve smlouvě |
| K5 | generátory a..e, jen a je permutace souřadnic | CONFIRMED, WEAK | věta o afinitě stojí o 29 řádků dál, ne hned za blokem; strukturální glosa potvrzena přepočtem |
| K6 | rozsah RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY | CONFIRMED (2x) | |
| K7 až K23 | | čeká | |

## Mechanické kontroly

- `check_assembly.py`: 42 slotů, 45 hran, 68 odlišných citovaných řádků
  registru (51 T, 7 D, 1 C, 7 O, 2 F), všechny statusy souhlasí,
  `ASSEMBLY PASS`.
- `check_loader_interface.py`: 390625 párů na krabici, zbytky zachovány;
  zavaděč `(0, 0)`, hodiny `(2, 3)`, zdroj `(0, 2, 0)` s periodou 9;
  `LOADER-INTERFACE RESIDUE AUDIT PASS`.
- `check_native_counter_statistic.py`: shoda kvocientové tabulky na všech
  15625 hlavách, listy `z` v `{1, 4}` od tiku 3, obraz pripravenosti `(0, 1)`
  625 stavů, tabulka C1 až C3 Canonu reprodukována, inverzní vzorec ověřen
  pro `3 <= n < 65536`; 20 podpisů, 90 kolizních hran, chromatické číslo 5;
  `NATIVE COUNTER STATISTIC AUDIT PASS`.

## Co záznam nedělá

Nezakládá status, nepropaguje žádný kandidátský výsledek, nemění žádný
soubor mimo tento adresář a `notes/canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`,
a nenahrazuje kolizní sken ani rezervaci pro žádný navržený krok.
