# PILOT PIN

Tento soubor je poslední součástí předběhového balíku. Commit, který jej přidá
na větev `experiment/E-PHOTON-Z5-PHASE-MEASUREMENT-1`, je neměnný pilotní pin.
Jeho plný SHA bude po vytvoření zapsán do `PILOT_RESULT.md`.

Po tomto pinu se před spuštěním čtyř zmrazených řetězců nesmí měnit:

```text
PREREG.md
README.md
photon_z5.cpp
photon_z5_part1.inc
photon_z5_part2.inc
photon_z5_part3.inc
photon_z5_part4.inc
photon_z5_part5.inc
photon_z5_part6.inc
reference_check.py
analyze_pilot.py
SELFTEST_EXPECTED.txt
REFERENCE_EXPECTED.txt
SOURCE_MANIFEST.md
```

Povolené následné soubory jsou pouze surové pilotní výstupy, jejich analýza a
čestný terminální výsledek.
