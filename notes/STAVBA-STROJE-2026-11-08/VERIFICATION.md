<!-- SPDX-License-Identifier: Apache-2.0 -->

# Záznam ověření mapy stavby stroje (NON-CANONICAL)

```text
STATUS:        NON-CANONICAL VERIFICATION RECORD
AUTORITA:      ŽÁDNÁ
METODA:        osm nezávislých čtenářů po shlucích (nativní U, kontaktní
               aparát, tepelná a energetická vrstva, aritmetika přenosu,
               polní automaty a zdroje, měření a výskyt, rozpracované PR,
               fyzikální žebřík), jedna syntéza, 24 klíčových tvrzení
               každé přezkoumané dvěma nezávislými rozhodčími s odlišnou
               optikou (A: text registru a Canonu; B: primární záznamy
               a přepočet vlastním skriptem), kritik úplnosti; výhradně
               čtení; mechanické kontroly check_assembly.py,
               check_loader_interface.py a check_native_counter_statistic.py
ROZHODČÍ:      48 posudků: 34 CONFIRMED, 14 WEAK, 0 CONTESTED, 0 REFUTED
LOKÁLNÍ HLAVA: a8482d06 (main po sloučení PR #1673), Public Canon v109
FORMAL RUN:    NONE
```

Každé WEAK je upřesnění znění, ne věcná chyba; všechna jsou zapracována
v `README.md` nebo ve smlouvě. Posudky jsou uloženy v záznamu relace;
tabulka níže je jejich souhrn.

## Verdikty klíčových tvrzení

| # | Tvrzení (zkráceno) | A / B | Korekce zapracovaná v mapě |
|---|---|---|---|
| K1 | STATUS.md deklaruje v109, hash a bajty; registr 609; snímky v105 až v109 | CONFIRMED / CONFIRMED | |
| K2 | dvanáct řádků RELATIVE-CONTACT-* je T; evidence obnovy je INLINE_CANON, společný přístroj a minima PUBLIC_PROBE two-architecture; žádný není živý vlastník | CONFIRMED / CONFIRMED | §1: dvouarchitekturní evidenci mají minima a společný přístroj, obnova pro každé `k` má inline důkaz |
| K3 | CHANGELOG v109 „separate laws and interfaces“; v107 přidání O; v108 uzavření O -> T; HISTORY událost | CONFIRMED / CONFIRMED | |
| K4 | U-CARRY-MIRROR-FINITE-CIRCUIT C; 40348 primitiv, 62 registrů, 500 vstupů, inverze obrácené slovo | WEAK / WEAK | „50 buněk včetně 48 pracovních“ je znění registru a CORE, ne těla oddílu; inverze je obrácené slovo s invertovanými primitivy (§5, smlouva B2) |
| K5 | generátory a..e; jen a je permutace souřadnic | CONFIRMED / WEAK | věta o afinitě stojí o 29 řádků za blokem, ne hned; glosa potvrzena přepočtem (b je znaménková permutace, c, d, e mají posuny) |
| K6 | rozsah RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY | CONFIRMED / CONFIRMED | |
| K7 | zavaděč: u, B, X, kontrakt I_t -> G_t, 322 kontaktů, inverze 1288, PASS; přesně pět úspěchů nad Z; obě architektury v merge commitech | CONFIRMED / CONFIRMED | |
| K8 | CONTRACT.md stopek: Y_n, X_k, 26 pomocných míst, účet 82, součet 4, WORD535 a jeho SHA-256, výsledek PASS s počty | CONFIRMED / CONFIRMED | |
| K9 | zbytky zavaděče (0,0), hodin (2,3), zdroje (0,2,0) s periodou 9; kontakt zachovává zbytky; přepočteno vlastním skriptem | CONFIRMED / CONFIRMED | |
| K10 | tepelný bootstrap: D = 2^84, tři teploty, 1 - q < 2^-82, bez verifieru; 1766 posouvá kontrast na jednu teplotu a palivový qubit | CONFIRMED / CONFIRMED | |
| K11 | rozsahy THERMAL-ORIGINAL-PORT-APPARATUS a LOCAL-THERMAL-TWO-ATTEMPT | WEAK / CONFIRMED | doplněno „all fuel, copies and thermal defects are counted“ a plné závěrečné znění „no equality with original Q or measured-intervention closure“ (§5) |
| K12 | čtyři věty CORE o neztotožnění účtů, nábojů a nosičů | CONFIRMED / CONFIRMED | |
| K13 | COHERENT-W-LOCALIZED-RING-CLOSURE: O[1/5], žádná unitální mapa do F_5 | CONFIRMED / CONFIRMED | |
| K14 | nativní čtení zbytku: dvacet hodnot stačí; čtení jen z přijímače ne; 23-stavový pozorovatel s dodaným bitem | CONFIRMED / CONFIRMED | |
| K15 | P-U-PAIR-PHASE-WORK-1: přírůstky ±e_k, kapacita 2s, a = b = 0; candidate-T/C, bez povýšení | CONFIRMED / CONFIRMED | |
| K16 | C-COMMON-COUNTER-PATH-PHASE-N: Proposition K, Theorem L, 135 proti 123, vystřelená hypotéza, ručička hodin, bez dvouarchitekturního běhu | WEAK / WEAK | Theorem L „found after the first run“; doplněno v §4 |
| K17 | rozhodovací podmínka QUADRATIC-MEMORY-NATIVE-CONTACT; pět vlastníků na STOP; 26 bran, jedna OPEN_DECISION | CONFIRMED / CONFIRMED | |
| K18 | sloučení 8. 11. a 6. 11.; aktivace v109 3. 11. | WEAK / WEAK | opuštěných pinů uzavřených 8. 11. je šest, včetně #1656 (P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1); opraveno v §4 a §9 |
| K19 | kniha: věta o pěti úkolech a pět nejbližších kroků | WEAK / WEAK | věta o pěti úkolech je v pododdílu „Od nativní přípravy k homogennímu záchytu a přijímači“ (řádek 1014), pět kroků v pododdílu „Obraz fyziky…“ (řádek 1271); opraveno v §2 |
| K20 | konsolidace 7. 11.: věta o definiční práci; počty STOP/BLOCKED/READY | WEAK / WEAK | věta je v SYNTHESIS.md oddíl 7; počty jsou v oddílu 6 téhož souboru, ne v README; mapa cituje jen větu |
| K21 | PR #1950: obě hypotézy sestupu vystřelily, 16/8, candidate-T/C, nesloučeno | CONFIRMED / CONFIRMED | |
| K22 | oba skripty reprodukují uložený stdout; statusy citovaných řádků souhlasí | WEAK / WEAK | rozhodčí ověřili aktuální čísla 42 slotů, 46 hran, 73 řádků (56 T) a všech 73 statusů; starší čísla v zadání tvrzení pocházela z dřívější verze tabulek |
| K23 | CORE o polním řetězci: N - 1, N, N + 1, ukazatel C5, „not a reset“, odvození z U otevřené; tři FIELD-* T | CONFIRMED / CONFIRMED | |
| K24 | CHANGELOG v106 (sedm plus osm plus jedna věta) a v105 (p > 2/10^28, asymptoticky, otevřené body) | CONFIRMED / CONFIRMED | |

## Mechanické kontroly

- `check_assembly.py`: 42 slotů, 46 hran, 73 odlišných citovaných řádků
  registru (56 T, 7 D, 1 C, 7 O, 2 F), všechny statusy souhlasí,
  `ASSEMBLY PASS`.
- `check_loader_interface.py`: 390625 párů na krabici `[-2, 2]^4`, zbytky,
  součet účtů i kruhový součet zachovány; zavaděč `(0, 0)`, hodiny `(2, 3)`,
  zdroj `(0, 2, 0)` s periodou 9; `LOADER-INTERFACE RESIDUE AUDIT PASS`.
- `check_native_counter_statistic.py`: shoda kvocientové tabulky `(z, q, r)`
  na všech 15625 hlavách a tiku 0 až 7, listy `z` v `{1, 4}` od tiku 3 do 64,
  obraz připravenosti `(0, 1)` 625 stavů, tabulka C1 až C3 Canonu
  reprodukována, inverzní vzorec ověřen pro `3 <= n < 65536`; 20 souhrnů,
  20 podpisů, 90 kolizních hran, chromatické číslo 5; projekce
  `(sigma_n, N_n mod 5)` postačující, `N_n mod 5` sama ne;
  `NATIVE COUNTER STATISTIC AUDIT PASS`.

## Mezery nalezené čtenáři a jejich vyřízení

1. Kontaktní čtenář: výstup zavaděče a vstup stopek mají různé zbytky a
   žádný soubor je neztotožňuje: zapracováno jako audit
   `check_loader_interface.py` a jako chybějící most S2 -> S3 na K2.
2. Nativní čtenář: minimalita dvacetihodnotového souhrnu není rozhodnuta:
   rozhodnuto skriptem `check_native_counter_statistic.py` (pět tříd).
3. Tepelný čtenář: tři bootstrap poznámky nemají žádný verifier a jsou
   do Canonu vepsány jen jako zmrazené premisy LOCAL-THERMAL-TWO-ATTEMPT:
   zapracováno v §5 a §8 (bod 4), verifier ponechán jako další krok.
4. Čtenář přenosu: řádek `C` je instance `N = 2` kompilátoru všech `N`;
   rozvrh je dodané řízení a lze jej zapsat jako čítač na osmi buňkách:
   zapracováno v §5 a §8 (bod 5).
5. Polní čtenář: jediná okruhová shoda polní buňky s `O` a JM faktorem je
   typová, bez přenosu stavu: zapracováno jako hrana S4/K4 -> S4/K2 a v §6.
6. Čtenář měření: zákon výskytu je přijatý slovník, žádná věta o nemožnosti
   vzorkování neexistuje: zapracováno v §7 a §8 (bod 7) a ve smlouvě.

## Co záznam nedělá

Nezakládá status, nepropaguje žádný kandidátský výsledek, nemění žádný
soubor mimo tento adresář a `notes/canon/DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT.md`,
a nenahrazuje kolizní sken ani rezervaci pro žádný navržený krok.
