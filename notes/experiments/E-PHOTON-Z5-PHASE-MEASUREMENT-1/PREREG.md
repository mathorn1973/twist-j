# E-PHOTON-Z5-PHASE-MEASUREMENT-1 — pilotní předregistrace

**Stav:** NON-CANONICAL / PILOT-ONLY / ZERO EVIDENTIAL WEIGHT  
**Veřejná rezerva:** issue #742  
**Větev:** `experiment/E-PHOTON-Z5-PHASE-MEASUREMENT-1`  
**Adresář:** `notes/experiments/E-PHOTON-Z5-PHASE-MEASUREMENT-1/`  
**Datum:** 2026-09-01  
**Vlastník:** A. M. Thorn

Tento dokument zmrazuje pouze první technický pilot. Pilot smí ověřit nosič,
přechodové jádro, míchání, autokorelace a měřitelnost veličin. Nesmí vydat
žádný závěr o fázi. Každý výstup nese doslovný stav
`EVIDENTIAL_STATUS ZERO_PILOT_ONLY`.

Produkční měření nezačne, dokud nejsou uzavřeny blokátory v §10 a zveřejněna
samostatná produkční předregistrace. Pilotní hodnoty se nesmějí použít k
posunutí fyzikálního bodu, výběru příznivých rozměrů ani k dodatečnému návrhu
rozhodovacích mezí.

## 1. Autorita a hranice

```text
STATE:                 ACTIVE
CANON:                 Public Canon v74
AUTHORITY:             mathorn1973/twist-j main
MAIN AT PILOT DESIGN:  c44b1c12b64b4e09d1721f3a2245a97ddd5dfb7f
TAG:                   canon-v74
CONTENT_COMMIT:        2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:          2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
```

Pilot spotřebovává nekanonickou uzavírací mapu
`notes/canon/PHOTON-PROGRAM-CLOSURE-V74.md`, ale nemění Canon, Registry,
Gates, Frontier, release ani vědecký stav `PHOTON-MASSLESS-PHASE [O]`.

## 2. Pevný fyzikální kandidát

Periodický nosič je

```text
K_L=(Z/LZ)^4,
A in C^1(K_L;Z5),
F=dA in C^2(K_L;Z5).
```

Všechny linkové proměnné se sčítají. Žádné gauge fixing se při měření
nepoužívá. Jednolinkové aktualizace mají kladnou pravděpodobnost pro všech pět
hodnot, takže konečný řetězec je ireducibilní na celém `C^1(K_L;Z5)`.

Pevná obličejová váha je

```text
W(0)=4,
W(1)=W(4)=phi^2=1+phi,
W(2)=W(3)=phi^-2=2-phi,
phi^2=phi+1.
```

Měřená míra je pouze

```text
mu_L(A) proportional product_p W(F_p),
t_physical=1.
```

Tento pilot neobsahuje žádné proměřování `W^t`. Hodnota `t=1` je v programu
vynucena doslova; jiná hodnota ukončí běh chybou.

## 3. Přesné přechodové jádro

Program používá postupnou jednolinkovou tepelnou lázeň. Pro každý link a
každou kandidátní hodnotu se přesně v `Z[phi]` spočítá součin šesti dotčených
obličejových vah. Neprovádí se desetinné přiblížení stacionárních
pravděpodobností.

Náhodné číslo dodává čítačový `Philox4x32-10`. Pro 64bitový tah `r` a přesný
kumulativní součet `C` z celkového součtu `S` se kategorie vybírá přesnou
algebraickou nerovností

```text
r S < 2^64 C.
```

Znaménko prvku `a+b phi` se rozhoduje celočíselně přes znaménko
`(2a+b)+b sqrt(5)`. Široké mezivýsledky používají pevný 256bitový celý typ.
Tím je posloupnost stavů nezávislá na knihovním generátoru desetinných čísel a
na zaokrouhlení `long double`.

Zmrazené pořadí je lexikografické:

```text
sweep -> site 0..L^4-1 -> direction 0..3 -> candidate 0..4.
```

Studený počátek má všechny linky nula. Horký počátek používá nezávislý proud
Philox a přesné odmítnutí pro rovnoměrnou hodnotu v `Z5`.

## 4. Programy a otisky před pilotem

```text
photon_z5.cpp
  sha256 cff060200d245d9888ae22a1cc0af9321d03f4f990118d16253d626ea74189d5

reference_check.py
  sha256 d750fd99fc16ea13dda0d7766725e92b68e75c91c4ec4689eea123e7581b7a3e

analyze_pilot.py
  sha256 0ad70b46041b0af32c57c7b0925d5770872ece3a008f959e6f9714b01ad1c4ab

SELFTEST_EXPECTED.txt
  sha256 b091329be8d77ff30dff152f750b960c8ced43d56a2c21820d8c0ea975ef380e

REFERENCE_EXPECTED.txt
  sha256 b03760a2793506daf7b4defd50042e163dea32bface798945862a19f3f50fb32
```

Zmrazený překlad:

```text
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic photon_z5.cpp -o photon_z5
```

Pilotní návrh byl před připnutím zkontrolován také pomocí Clang 17. Oba
překlady vracejí tentýž samokontrolní text a stavový otisk
`eaa7bcbe93566b43`.

Samostatný Pythonový program nevolá C++ kód. Znovu sestavuje Philox, aritmetiku
`Z[phi]`, gauge transformaci, lokální tepelnou lázeň a tři úplné průchody na
`L=3`. Musí vrátit tentýž stavový otisk.

## 5. Pilotní řetězce

Přesně tyto čtyři řetězce jsou pilotní. Žádný další pilotní řetězec nevstoupí
do rozhodnutí níže.

```text
L=6 cold seed=0xE742060000000001 thermal=256 measurements=256 between=4 max_n=2
L=6 hot  seed=0xE742060000000002 thermal=256 measurements=256 between=4 max_n=2
L=8 cold seed=0xE742080000000001 thermal=512 measurements=256 between=8 max_n=3
L=8 hot  seed=0xE742080000000002 thermal=512 measurements=256 between=8 max_n=3
```

Příkazy jsou uvedeny v `README.md`. Každý běh musí mít prázdný stderr,
návratový kód nula a přesně 256 po sobě jdoucích řádků `SAMPLE`.

## 6. Pilotní veličiny

Každý zaznamenaný stav obsahuje:

```text
průměr log W(F_p)
prostorově průměrovanou Polyakovovu smyčku a její poloměr
pětinásobnou směrovost v souhrnu řetězce
hustotu nenulových vírových obličejů
obalení a největší souvislou vírovou složku
hustotu a váženou délku proudu m=(d f)/5
obalení, počet a největší složku monopolového proudu
lokální TWIST skóre G
stavový FNV-1a otisk linků a cache toku
souhrnný orientovaný obličejový korelátor C(n)
```

„Obalení vírové složky“ je v tomto pilotu podporný geometrický ukazatel:
používá zdvojená střediště obličejů a nekonzistentní zdvih cyklu na periodické
mříži. Není to ještě úplná klasifikace homologie s nábojem a násobností.

Monopolový proud se počítá z hlavního celého zástupce
`f in {-2,-1,0,1,2}`. Dělitelnost pěti a nulová diskrétní divergence se
kontrolují při každém měření; porušení běh okamžitě zastaví.

Korelátor používá dvanáct podélných členů `C+` a dvanáct příčných členů `C-`
a porovnává jejich součet s periodickým cílem `n^-4+(L-n)^-4`. Pilot však
neukládá úplná surová data potřebná pro blokový jackknife korelátoru. Jeho
číselná hodnota je proto pouze diagnostická a nevstupuje do pilotního PASS.

## 7. Zmrazená analýza míchání

`analyze_pilot.py`:

1. ověří hlavičku přesného modelu, `t=1` a nulovou důkazní váhu;
2. ověří počet a pořadí vzorků;
3. spočítá integrovanou autokorelační dobu Geyerovým počátečním kladným
   párovým součtem;
4. spočítá konzervativní směrodatnou chybu jako maximum chyb přes bloky
   velikostí `1,2,4,...` s nejméně osmi bloky;
5. porovná horký a studený řetězec při stejném `L`;
6. zkontroluje podíl různých stavových otisků.

Pilot projde pouze tehdy, když:

```text
každý řetězec má 256 vzorků
nejméně 90 % stavových otisků je různých
ESS >=16 pro logw, Polyakovův poloměr, vírovou a monopolovou hustotu
|mean_hot-mean_cold|/hypot(SE_hot,SE_cold) <=4 pro stejné čtyři veličiny
všechny integritní a nulově-evidenční značky jsou přítomné
```

## 8. Pilotní výstupy

Povolené jsou právě dva terminální výsledky:

```text
PILOT_KERNEL_PASS_PRODUCTION_BLOCKED
STOP_MIXING_OR_INTEGRITY
```

Ani jeden z nich není fázový výsledek. Zakázány jsou v tomto balíku zejména
řetězce `PHOTON_EVIDENCE`, `CONFINED_EVIDENCE`, `Z5_BROKEN_EVIDENCE` a jejich
slovní náhrady.

Pokud pilot neprojde, nesmí se přepsat. Další pokus musí mít nový očíslovaný
pilotní protokol a veřejně vysvětlenou změnu.

## 9. Co pilot může změnit

Pilot může před produkčním pinem určit pouze:

```text
potřebné zahřívání
potřebný odstup mezi vzorky
paměťový a časový rozpočet
formát úplných surových korelačních dat
potřebný rozsah checkpointů
zda je nutná změna aktualizačního algoritmu kvůli míchání
```

Nesmí změnit `W`, `t=1`, produkční rozměry podle fyzikálního výsledku ani
základní fázovou rozhodovací gramatiku.

## 10. Produkční blokátory

I při pilotním PASS zůstává produkce blokována, dokud nejsou připnuty:

```text
B1  nezávislý duální proudový výpočet a numerické Wardovy kontroly
B2  úplná surová data korelátoru a blokový/jackknife odhad jeho chyb
B3  předem číselně stanovené produkční rozhodovací meze a okna
B4  checkpoint/restart s otiskem stavu a přesným pokračováním čítače
B5  druhá úplná implementace nebo předem zmrazená nezávislá kontrolní podmnožina
B6  nejméně dva horké a dva studené řetězce pro každé produkční L
B7  produkční L={8,12,16,24,32} a veřejný plán výpočetního rozpočtu
```

Produkční předregistrace musí vracet přesně jednu z již vyhrazených hodnot:

```text
PHOTON_EVIDENCE
CONFINED_EVIDENCE
Z5_BROKEN_EVIDENCE
MULTIPHASE_OR_TRANSITION
AMBIGUOUS_FINITE_SIZE
STOP_MIXING
STOP_INTEGRITY
```

Pilot nemůže předjímat, která z nich nastane.
