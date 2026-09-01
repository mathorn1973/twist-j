# E-PHOTON-Z5-PHASE-MEASUREMENT-1 — pilot

Tento adresář obsahuje nulově-evidenční technický pilot přesné míry

```text
mu_L(A) proportional product_p W((dA)_p),
W=(4,phi^2,phi^-2,phi^-2,phi^2),
t=1.
```

Nejde o výsledek fáze. Pilot ověřuje kód, přesný přechod, míchání a základní
měřitelnost veličin. Produkční blokátory jsou uvedeny v `PREREG.md`.

## Překlad a samokontrola

Vyžaduje C++20 a hlavičky Boost.Multiprecision.

```sh
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic photon_z5.cpp -o photon_z5
./photon_z5 --self-test > selftest.out
cmp selftest.out SELFTEST_EXPECTED.txt

python3 reference_check.py > reference.out
cmp reference.out REFERENCE_EXPECTED.txt
```

## Zmrazené pilotní běhy

```sh
./photon_z5 --L 6 --t 1 --seed 0xE742060000000001 --start cold \
  --thermal-sweeps 256 --measurements 256 --between-sweeps 4 --max-n 2 \
  > pilot-L6-cold.txt

./photon_z5 --L 6 --t 1 --seed 0xE742060000000002 --start hot \
  --thermal-sweeps 256 --measurements 256 --between-sweeps 4 --max-n 2 \
  > pilot-L6-hot.txt

./photon_z5 --L 8 --t 1 --seed 0xE742080000000001 --start cold \
  --thermal-sweeps 512 --measurements 256 --between-sweeps 8 --max-n 3 \
  > pilot-L8-cold.txt

./photon_z5 --L 8 --t 1 --seed 0xE742080000000002 --start hot \
  --thermal-sweeps 512 --measurements 256 --between-sweeps 8 --max-n 3 \
  > pilot-L8-hot.txt
```

Analýza:

```sh
python3 analyze_pilot.py \
  pilot-L6-cold.txt pilot-L6-hot.txt \
  pilot-L8-cold.txt pilot-L8-hot.txt \
  > PILOT_ANALYSIS.txt
```

Návratový kód nula znamená pouze
`PILOT_KERNEL_PASS_PRODUCTION_BLOCKED`. Nenulový kód znamená
`STOP_MIXING_OR_INTEGRITY`.

## Poznámka k Polyakovově smyčce

„Smeared Polyakov loop“ zde znamená prostorový průměr kořenů jednotky přes
příčné řezy, stejně jako v použité mřížové diagnostice. Neprovádí se gradientní
tok ani APE vyhlazování.

## Poznámka ke korelátoru

Program počítá orientační součet podélných `C+` a příčných `C-` členů a jeho
poměr proti periodickému zákonu čtvrté mocniny. Pilotní formát zatím neukládá
všechny členy po jednotlivých konfiguracích, takže korelátor nemá oprávněnou
blokovou chybu a nesmí nést fázové rozhodnutí.
