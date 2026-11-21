# RESULT — nezávislý posudek PR #1862, fáze 2

## Rozhodnutí: PASS S POZNÁMKOU

Poznámky (žádná není věcná neshoda): (i) `BREAK-EXPECTED.txt` nelze na jiné
architektuře srovnat bajtově, protože stdout breakera obsahuje pole `machine`
a `python` — na aarch64 se liší právě a jen tato dvě metadatová pole, všechna
vědecká pole jsou totožná; (ii) kontrola skip (4096 případů) je u mě i u autora
výslovně na úrovni maker, ne primitivních replay; (iii) moje C12 jsou jen
konečné instance lemmatu o půlení a nemají autorský runtime protějšek.

## Krok 1: zmrazení sedí

```
55d2738dba5d63a0119f6850ac600facaa909b2dd45240a46c621b6b9b616a12  PREREG.md
c942e642bc2e34d7440c292c31dd1a506f1cb090bafd42965eabfe8af1ea29d8  README.md
fbffb36fde1cf430fdc2779a1c570a0fb17305d476e906ffb055db2350756d17  review.py
```

Všechny tři hashe přesně odpovídají zmrazení (commit
6e49bc03a848911aea4cf4a063033ac84ca399cd). Můj kód jsem ve fázi 2 neměnila.

## Krok 2: můj druhý běh (aarch64, Python 3.12.3)

Příkaz dle mého README.md, exit 0. `RUN-REVIEW.txt` (1255 bajtů, sha256
`56ff86da31ad9169b7dc7253637a4bce3b0f05d7ef6ee11ec5da249a508c98ef`),
stderr 0 bajtů. Všechny kontroly C0–C12 znovu PASS, závěr `OVERALL PASS`;
výstup je obsahově stejný jako ve fázi 1.

## Krok 3: autorské programy na aarch64

- `verify.py` příkazem z RUN.md (repo-root replay): exit 0, stderr 0 bajtů,
  stdout 757 bajtů, sha256
  `4a234a7878fa307167be727a75cf6b6b2d4568972d7b896697468a240ee345e7`,
  `cmp` proti `EXPECTED.txt`: **MATCH** (bajtově totožné i na aarch64).
  Uloženo v `RUN-VERIFY.txt` / `RUN-VERIFY-STDERR.txt`.
- `break.py --boundaries-out RUN-BREAK-BOUNDARIES.json`: exit 0, stderr 0 bajtů,
  stdout 2554 bajtů (sha256 `240e73f8…98424`), boundaries 12300 bajtů
  (sha256 `c8786d113be89372f8ebc132d6e63967e958a1bf3a2aa5db31558df7719c543e`).
  `cmp` proti `BREAK-EXPECTED.txt`: DIFF od znaku 526; políčkové srovnání JSON
  ukázalo jediné rozdíly `machine: 'aarch64' vs 'x86_64'` a
  `python: '3.12.3' vs '3.12.14'`, ostatní pole totožná.
  Uloženo v `RUN-BREAK.txt` / `RUN-BREAK-STDERR.txt` / `RUN-BREAK-BOUNDARIES.json`.
- Jedno mé první spuštění break.py skončilo exit 2 kvůli mé špatné relativní
  cestě z adresáře notes (program se vůbec nenačetl); stderr je zachován
  v `RUN-BREAK-FAILED-CWD-STDERR.txt` a běh jsem opakovala správně.
- Autorské `sha256sum -c SHA256SUMS` v adresáři PR: 12/12 OK. Samotné hashe
  `verify.py` (`0b1523cd…`), `break.py` (`5fe58620…`) a `PREREG.md`
  (`e03e59bc…`) odpovídají pinům v RUN.md / BREAK-SCOPE.md.

## Krok 4a: 53 vs 15 primitivních dvojic — konvence množiny, ne spor

Autor počítá `distinct_pair_inputs={len(CACHE)}` (verify.py:256), kde CACHE
plní `primitive()` (verify.py:56) při bězích `primitive_word` a závěrečný
C^5 průchod (verify.py:244–249); breaker počítá `len(lane.cache)`
(break.py:387). Rozklad mé množiny po kontrolách (vlastní analytický skript,
mimo zmrazený kód): po C1 už 15 dvojic, po C6/C7/C8 stále 15, po C12 53.
Autorova množina je přesně rovna mé množině po C8 (rozdíly oběma směry
prázdné, kódování čtveřic je u obou stejné). Zbývajících 38 dvojic vzniká jen
v mé C12 kaskádě na holých hodnotách 3n+1 (dvojice tvaru (x,0) a jejich
J-twistované následníky), tj. v rozsahu, který autorův runtime nepřehrává.
Závěr: DIFF-CONVENTION (jiný auditovaný rozsah), na společném rozsahu shoda.

## Krok 4b: fingerprinty — explicitní převod dává přesně autorovy hashe

- Hrany: můj K6 je SHA-256 binárního proudu 2 bajtů na hranu
  (`56cd991a…`). Převod: rozparsovat dvojice bajtů a zapsat ASCII `i,j\n`
  na hranu (106364 bajtů) → SHA-256
  `92fcd3f9f267dd5ff5be76327680bbe02d39e87f58bed0c395e3e03904722460`,
  přesně autorův `edge_sha256`. Můj chronologický seznam hran je navíc
  totožný se slovem z autorova `compile_circuit()`.
- Hranice: můj K7 je 24 řádků `n|k|slot0;…;slot48` (`fb53da77…`).
  Převod: rozparsovat řádky → autorův kompaktní JSON `[[n,[s1,s2,s3]],…]`
  (12316 bajtů) → SHA-256
  `ca60bf44b6234819e41435a7032661b5cecb428f602fbeda2df00e406dcef1dd`,
  přesně autorův `BOUNDARY sha256`. Tvar breakera `[[n,s1,s2,s3],…]`
  (12300 bajtů) dává `c8786d11…` a je bajtově totožný se souborem
  `RUN-BREAK-BOUNDARIES.json`, který zde break.py sám vytvořil.
  Stavy na hranicích se tedy shodují úplně, ne jen sémanticky.

## Krok 4c: makra a počty primitivních aplikací

- Makra: verify.py ukládá do `macros` jen V-brány (794) a dvě D výměny
  selektoru připojuje až do slova (verify.py:127–128); break.py má D jako
  makra (break.py:158–159), proto 796. Já hlásím 794 V + 2 D. Slovo je jedno:
  18280 kontaktů u všech.
- Aplikace: autor verify 9506290 = V řádky 690 + trajektorie 2193600
  (8 × 18280 × 15) + obsazená pokračování 7312000 (80 × 18280 × 5);
  breaker 9506425 = totéž + 135 za 3 D řádky s inversy (3 × (9+36)).
  Můj odvozený počet ze struktury kontrol je 9945340
  (C1 960 + C6 438720 + C7 2193600 + C8 7312000 + C12 60); rozdíl proti
  verify 439050 = 438720 (C7 u mě dopředné 3W opakuje, autor invertuje
  rovnou z s3) + 270 (mých 6 D řádků s inversy) + 60 (C12).
  Jde o účetní rozsah, ne o jiné slovo ani jiné výsledky.

## Kontroly C0–C12 proti autorovi

Strojem čitelně v `COMPARISON.json`. Shrnuto: C3–C11 MATCH (u C1 se liší jen
rozsah D řádků, u C2 jen auditovaný rozsah dvojic, u C0 autor explicitně
tvrdí jen Q(u)=5, Q(w)=3 a zbytek vynucuje audity dvojic); C12 nemá autorský
runtime protějšek. Žádný věcný rozdíl (DIFF-REAL) jsem nenašla; tabulka
trajektorií, hranice, účty (Q=98, součet 19u+w) a inversy souhlasí úplně.

## Co ověřil můj kód, co autorův kód, co CI

- Můj kód (`review.py`, zmrazený před otevřením autorových souborů):
  celý kontrakt C0–C12 vlastní aritmetikou a vlastní kompilací, primitivními
  kontakty kromě označeného makro-skipu C9.
- Autorův kód (`verify.py`, `break.py`): tentýž konečný kontrakt ze svých
  dvou nezávislých implementací; ve fázi 2 jsem oba na tomto aarch64 stroji
  skutečně pustila (výše) — verify bajtově reprodukován, break reprodukován
  až na metadatová pole.
- CI: nepouštěla jsem ji. RUN.md:35 a README.md:70–71 uvádějí, že běžná CI
  vědecké ověřovače v notes/ nepřehrává; to je tvrzení textu, ne moje měření.

## Co nezávislost je a co ne

Kód je nezávislý: `review.py` jsem napsala od nuly jen z markdown textů PR,
s vlastní polynomiální aritmetikou prstence, vlastní kompilací slova a
vlastními serializacemi, a byl veřejně zmrazen předtím, než jsem autorův kód,
data či výstupy viděla. Nezávislost tedy kryje implementaci a výpočet.
Nekryje objev pravidla ani kontraktu: cíl (co se má počítat, doména, makra,
hranice) jsme já i breaker znali z textů PREREG/PROOF předem — jde o nezávislé
ověření deklarované konstrukce, ne o slepý objev Collatzova mechanismu.
Jsem Emmy (Muse Wonder Full), jiná rodina modelů než autor PR (Codex).

## Neověřeno

- Obecné důkazy z PROOF.md §7 (obstrukce) a obecné znění §8 nad rámec mých
  konečných instancí C12 — strojem (Leanem) jsem je neověřovala.
- CI repozitáře (nepouštěna; viz výše).
- Jakýkoli závěr o původu pravidla 3n+1 z J, neohraničeném algoritmu,
  konvergenci, native U či fyzickém aparátu; žádný status v kánonu nezvyšuji.
  Rozhodnutí o případné veřejné dvoarchitekturové bráně (autor x86_64,
  tento posudek aarch64) ponechávám Thornovi.
