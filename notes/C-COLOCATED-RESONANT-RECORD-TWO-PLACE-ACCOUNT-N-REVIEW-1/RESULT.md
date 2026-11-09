# Posudek PR #1959 (C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N) — fáze 2

## Rozhodnutí: PASS S POZNÁMKOU

Mezi mým zmrazeným ověřovačem a autorovými programy nebyl nalezen žádný
skutečný rozpor (DIFF-REAL: 0). Čtení důkazu PROOF.md s ERRATA.md nenašlo
matematickou chybu nad rámec už opraveného znaménka E4. Poznámky níže se
týkají rozsahu, mechanismu a provenience, ne čísel.

Kandidát zůstává **NON-CANONICAL / L1**, jak sám deklaruje: analytická
tvrzení podmíněná candidate-T, konečná evidence candidate-C. Tento posudek
žádný status v kánonu nemění a není dvouarchitekturovou vědeckou bránou.
Přijetí do kánonu je rozhodnutí vlastníka kánonu.

## Zmrazení a druhý běh

Zmrazení ověřeno z GitHubu (contents API při commitu
`1d5c58675145d9799aff4b4b0a84f4ac73c49a58`): blob id a velikosti
`PREREG.md` 9aec74cd… 14713 B, `README.md` dbe586f8… 4094 B, `review.py`
7455d3f6… 26611 B se rovnají lokálním `git hash-object`. SHA-256:

```
c0406d6ce6b3fbf2d4378658c6a0ca501521c44df15d0ff9304a83c74408684f  PREREG.md
0c5520e2fcdef00644d0c325437106593bf3c8358ae3e09b507529cb1256aa5a  README.md
a84df55b72d49c47390668df22d1abfd3cc30da86fd223662efee6f963014f1c  review.py
```

PREREG.md byla commitnuta samostatně jako
`f2e0e0dfdc2a7c594cc438f7e3258e1afa5a2c93` před prvním spuštěním
ověřovače. Druhý běh `review.py` (Linux x86_64, CPython 3.13.18, prostředí
dle README): exit 0, `RESULT PASS`, R01–R14 PASS, stdout 1628 B bajtově
shodný s během fáze 1 (sha256 `13a2271f…2a85d8`), stderr prázdný
(`RUN-REVIEW.txt`, `RUN-REVIEW-STDERR.txt`). Teprve potom byla otevřena
těla autorových programů.

## Autorovy programy na tomto stroji

Spuštěno beze změny z kořene čistého checkoutu hlavy PR
`2dd5c7acaea30a9b6d39529044d05f85c2ce99ab` (strom po bězích beze změn):

| Program | Exit | stderr | stdout | `cmp` proti očekávanému |
| --- | ---: | ---: | ---: | --- |
| `verify.py` | 0 | 0 B | 576 B, sha256 `a9e13f04…04c1f4` | EXPECTED.txt: **IDENTICKÝ** |
| `break.py` | 0 | 0 B | 576 B, sha256 `a9e13f04…04c1f4` | BREAK_EXPECTED.txt: **IDENTICKÝ** |

Syrová bajtová shoda bez normalizace konců řádků. Autorův RUN.md
zaznamenává na Windows selhání přímého porovnání (CRLF). Na Linuxu toto
selhání nenastává; jde o artefakt textového režimu stdout na Windows,
ne o vlastnost programů. `sha256sum -c SHA256SUMS`: 13/13 OK. Tabulka
PUBLICATION.md (11 řádků) sedí bajt i hash; piny PROOF.md, verify.py,
break.py v autorově PREREG.md sedí; piny README.md a SOURCES.md tam popisují
původní needitované bajty, jak PUBLICATION.md uvádí.

## Porovnání R01–R14 (jednostranné vyřízení)

Podrobnosti s čísly řádků jsou v `COMPARISON.json`.

- **R01–R04 (prstenec, formy, konstanty, Věta 1):** MATCH. B0_count 49 na
  obou stranách jako čítač. Determinant matice násobení pro normu kontroluje
  `break.py` i já; `verify.py` jen `phi_norm`.
- **R05–R06 (kontakt, Věta 2):** MATCH. 6480 párů, 64800 řezů, 38
  rezonančních v `{-1,0,1}^4`, 624 seedů v `{-2..2}^4`. Autorův výstup
  tiskne `PAIRS=6480` a `RESONANT_GRID2=624` jako literály, smyčky je však
  přesně realizují; `CUTS` a `RESONANT_GRID1` jsou čítače.
- **R07–R08 (F16, Věta 3):** MATCH. 162 seedů, 40500 řezů, 81/81, svědek
  `m=1,k=0` na obou stranách. Uzavřený tvar `E_full = 352A+16B` (E3)
  kontroluji jen já; autor kontroluje pouze zachování účtu.
- **R09 (A4, port):** MATCH včetně označení P27 → vstup `(1-rho)rho^4`,
  P35 → vstup `1-rho`, shodně s #1957 PREREG ř. 135 a s mou K8.
- **R10 (Věta 4):** DIFF-CONVENTION v mechanismu, MATCH v závěru. Autor
  násobí jednu jednokanálovou událost počtem (`W_k = N_k·w`), já jsem každou
  událost skutečně proběhl jako čerstvou pětikanálovou banku (6075 běhů).
  Autorův RESULT.md tuto algebraickou povahu A5 sám přiznává.
- **R11 (Věta 5.1–5.2):** MATCH, 405/405.
- **R12 (Věta 5.3):** DIFF-CONVENTION ve fixtures polarizací a křížové
  kontrole (já Čebyšev ve `Fraction`), stejný závěr do `n = 25`.
- **R13 (errata):** bez autorského runtime protějšku; E1, E3, E4 ověřeny
  jen mým kódem a čtením.
- **R14 (citlivost):** oba mutanty detekovány; autor obdobnou kontrolu
  nemá, což není požadavek.

## Poznámky (žádná není věcná neshoda)

1. **`break.py` není druhý audit, jen druhá reprezentace.** Zrcadlí
   `verify.py` blok po bloku: stejné fixtures, profily, pořadí slotů,
   přírůstky čítačů a doslovně stejné výstupní řetězce. Liší se jen
   5-cyklický okruh modulo diagonála, neredukovaný posun `(2v-x+F)/4` a
   maticové stopy/determinanty. PR to sám popisuje jako „independent
   cyclic representation“ a žádný samostatný posudek netvrdí; tento posudek
   je tedy první strukturálně oddělená implementace.
2. **Literály ve výstupu.** `6480`, `624`, `625`, `16`, `35`, `55->20`,
   `6+8phi`, oba páry portu, `81`, `12`, `25` jsou tisknuté konstanty, kryté
   smyčkami a aserty, ne naměřené čítače. Čítače jsou `B0_COUNT`,
   `RESONANT_GRID1`, `CUTS`, `ODD/EVEN`, `CHANNEL_CHECKS`,
   `DEAD_TIME_LOCK`, `BACKREACTION` a `ASSERTIONS`.
3. **Provenience zůstává na autorově záznamu.** Lokální zdrojový pin
   `19ff5935…` a výsledek `f7e2ea7d…` nejsou ve veřejném repozitáři;
   tvrzení „nula vědeckých běhů před pinem“ nelze veřejně ověřit a PR to
   v PUBLICATION.md říká. Toto je intake po lokálním běhu, ne prospektivní
   veřejný pin; status candidate-C na jedné architektuře je proto správný
   strop. Můj replay přidává druhé x86_64 prostředí (Linux, CPython 3.13),
   ne druhou architekturu.
4. **Závislost na nesloučených návrzích.** Premisy pocházejí z draft PR
   #1930, #1956 a #1957 (všechny `behind` vůči `main`); SOURCES.md je
   přepisuje jako samostatné podmíněné vstupy a PROOF §2 (2.6) přebírá
   úplný účet `K+V+H` z #1930 jako premisu. Ověřil jsem konzistenci s
   deklarovanými rovnicemi, ne odvození těchto premis z jejich zdrojů.
   Pořadí slučování je věc vlastníka.
5. **Jmenovatele pro všechna `n`** (Věta 5.3) a iff-směry Vět 2 a 3 jsou
   obecná tvrzení; strojově jsou kryta jen na konečných množinách, obecně
   čtením důkazu (indukce mod `p`, těleso `F_16`, integrální obor). Čtení
   je souhlasné.
6. **Drobnost k výstupu na Windows.** Otevření stdout s `newline="\n"`
   (nebo zápis bajtů) by příště odstranilo CRLF rozdíl z RUN.md; není to
   vada výsledku.

## Co ověřil čí kód a v jakém rozsahu

Můj `review.py`: R01–R14 dle PREREG, mřížky `{-2..2}^4` a `{-1,0,1}^4`,
81 lichých a 81 sudých seedů, 5 fází, mé profily a polarizace, errata,
mutanty. Autorův `verify.py`/`break.py`: bloky A1–A6 na týchž mřížkách
a seedech s vlastními profily/polarizacemi; A5 algebraicky. Obecné věty
z PROOF.md ani jedna strana strojově nedokazuje.

## Co CI

Workflow `policy.yml` spustil `check_policy`, unit testy, `check_canon`,
`check_ledger`, `check_gate_contract`, a `check_verifier.py --base` /
`check_reproduce.py --base` skončily `NOT APPLICABLE` (log běhu
42468892459). Vědecké programy pod `notes/` CI nespouští, přesně jak PR
uvádí. Lokálně na stromu PR: `POLICY PASS`, `CANON PASS v109 claims=609`,
`LEDGER PASS`, `GATE CONTRACT PASS`; unit testy zde hlásí 2 chyby
`test_probe_replay_context` kvůli mělkému klonu bez historických pinů
(CI s plnou historií prošlo). Commit PR: autor i committer
`A. M. Thorn <thorn@twistj.com>`, jediný rodič `a8482d06…` = `main`,
14 souborů, jen `notes/`, bez soukromých cest, adres či CRLF.

## Co zůstalo neověřeno

Původ a nezávislost premis z #1930/#1956/#1957; fyzikální výběr módů
`(5,4)` a `(7,6)`; Bornovo pravidlo, autonomní dobíjení, nativní U,
akční škála (PR je výslovně netvrdí); replay na aarch64; custody lokálního
pinu.

## Co nezávislost je a co ne

Je: PREREG a `review.py` psané bez četby těl autorových programů, vlastní
design (dvě násobení, `h` ze součinu, vlastní nosič a slova, determinanty,
Čebyšev, mutanty), zmrazené a přečtené zpět z GitHubu před porovnáním.
Není: slepost vůči výsledkům — všechny autorovy texty a oba očekávané
výstupy jsem znal předem (PREREG §0), a specifikace (rovnice, mřížky,
seedy, slovo) je převzata z textu PR, takže všechny tři programy ověřují
týž deklarovaný kontrakt, ne správnost jeho premis.
