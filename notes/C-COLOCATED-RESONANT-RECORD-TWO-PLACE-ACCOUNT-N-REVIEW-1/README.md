# Nezávislý posudek PR #1959 — fáze 1 (zmrazení)

## Co složka je

Nezávislý posudek podle protokolu posudků #1862/#1865/#1879 pro
`C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N`
([PR #1959](https://github.com/mathorn1973/twist-j/pull/1959), hlava
`2dd5c7acaea30a9b6d39529044d05f85c2ce99ab`), psaný z textů PR
(PROOF.md, PREREG.md, ERRATA.md, README.md, SOURCES.md) a z #1957
PREREG.md ř. 104–144 (jen označení vstupů P27/P35).

- `PREREG.md` — zmrazený seznam kontrol R01–R14 s přesnými kritérii
  PASS/FAIL, vlastní konvence K1–K10, prohlášení o expozici a plán fáze 2.
  Commitnuto jako `f2e0e0dfdc2a7c594cc438f7e3258e1afa5a2c93` před prvním
  spuštěním ověřovače.
- `review.py` — vlastní implementace od nuly: čistý stdlib, exaktní
  celočíselná aritmetika a `Fraction`, dvě nezávislé reprezentace násobení
  v `O = Z[j]` (redukce modulo `Phi_5` a cyklická konvoluce délky 5),
  `h(v)` ze součinu `v·conj(v)` (ne ze vzorců S0/S1/S2), vlastní kontaktní
  zákon, vlastní nosič s kontrolou Gaussových zákonů, součtu, reziduí a obou
  účtů na každém primitivním řezu, vlastní slova (selektor, pětikanálová
  banka, dvoukanálový port), vlastní inverze (obrácené pořadí, `C^4`),
  determinanty matic násobení pro normy, Čebyševova rekurence pro
  `cos(n omega)`, dva mutanty pro kontrolu citlivosti. Nečte a nezapisuje
  žádný soubor.
- `README.md` — tento popis.

## Expozice (podstatné)

Toto **není slepý posudek**. Před sepsáním PREREG jsem přečetl všechny
markdown soubory PR, oba očekávané výstupy a SHA256SUMS, jednou spustil
autorovy programy a ověřil repozitářové kontroly; viz PREREG.md §0.
Neotevřená zůstala těla autorových `verify.py` a `break.py` (jen výpis
importů a jmen funkcí). Kritéria v PREREG proto u počtů 38 a 49 nejsou
slepé predikce; jsou to známé hodnoty, které můj kód přepočítává od nuly.

## Jak se to pouští

```sh
env LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 notes/C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N-REVIEW-1/review.py
```

Exit 0 jen při úplném PASS R01–R14, jinak 1. Výstup nemá cesty, časy ani
platformu.

## Výsledek zaznamenaného běhu (fáze 1)

Mezi napsáním a prvním spuštěním byla v `review.py` opravena jediná věc:
v R05 dostal dvouslotový nosič neutralizační společníka `-(x+v)`, bez něhož
by počáteční stav nesplňoval `G_B` a konstruktor by každý pár odmítl.
PREREG.md se neměnila.

První běh: exit 0, stderr prázdný, všech čtrnáct kontrol PASS,
`RESULT PASS`. Klíčová čísla (všechna vlastním přepočtem):

```
R04 B0_count=49
R06 pairs=6480 cuts=64800 resonant=38 grid_seeds=624
R08 seeds=162 cuts=40500 odd_onehot_pass=81 even_onehot_fail=81 even_witness_m1_k0=81
R09 c#=-1,-2,-2,0 h=3+4phi Q=10 helper 55->20 quantum=35 port P27=(0,35) P35=(35,0)
R10 profiles=12 channel_checks=4860
R11 lock=405 backreaction=405
R14 oba mutanty detekovány
FP_B0       c60ce0b9db823a7cc537b88fd27f89600a36414e8ce13dfa390e9a850b97ae78
FP_RESONANT 9e1f6899511d1071c1b3ff928793fd17fd031b1f5bb9fe4327d363a186918e29
FP_BANK     b56d71dcec5d2d215f5dda43612788ee47fe3ae71ca8bc225b006ca57936e5ab
```

Fingerprinty jsou hodnoty mé serializace (K9); autorovy výstupy žádné
fingerprinty neobsahují, takže se s ničím neporovnávají.

## Rozsah a meze

Ověřeno strojem: konečné instance Vět 1–5 a Propozice 2 na mřížkách
`{-2..2}^4`, `{-1,0,1}^4`, 81 lichých a 81 sudých seedech, všech pěti
fázích, mých dvanácti profilech počtů, obou modech do `n = 25`, a errata
E1–E4, E6. Obecné důkazy v PROOF.md (indukce nad `n`, argument tělesa
`F_16`, iff-směry) jsou ověřeny jen na těchto konečných množinách a
čtením; strojově dokázány nejsou. Nic se netvrdí o fyzikální realizaci,
Bornově pravidle, výběru módů ani o statusu v kánonu; kandidát zůstává
NON-CANONICAL / L1, jak PR sám deklaruje. Porovnání s autorovými programy
patří do fáze 2 (RESULT.md, COMPARISON.json).
