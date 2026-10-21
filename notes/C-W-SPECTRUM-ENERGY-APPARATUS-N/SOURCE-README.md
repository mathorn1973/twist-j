# TWIST-J: spektrum W a energetický přístroj

Začni souborem RESULT.md. Obsahuje celý výsledek v češtině, konkrétní
konstrukci, chybové meze a přesné hranice tvrzení.

## Obsah

- RESULT.md: hlavní výklad a závěry.
- agents/spectrum_locality/PROOF_GLOBAL_SPECTRUM_AND_LOCALITY.md:
  globální mezera, přesný logaritmus, prostorové odhady a větvová
  nejednoznačnost skutečné práce.
- agents/spectral_lift/SPECTRAL_APPARATUS.md: přesný přístroj pro celé
  omezené spektrum, konečná kapacita, všechny chybové konstanty,
  polohový odhad a autonomní doplnění.
- PROOF_MOVING_REFERENCE_v2.md: dvě skutečné kopie W, přesné společné
  translace, nepromítnutý limit odezvy a relativní hmotnost.
- agents/sources_review/ a agents/spectrum_locality/REVIEW_MOVING_REFERENCE.md: nezávislé
  analytické přezkumy; autoritativní změny zdrojů a primární literatura.
- inputs/: nezměněné relevantní dřívější důkazy kontaktní větve a
  konečné binomické přípravy, s otisky a cestami původu.
- PREREG.md, CERTIFICATE_SCHEMA.md, SOURCE_FREEZE.json: specifikace
  a otisky před novými vědeckými spuštěními.
- verify.py a agents/sources_review/verify_independent.py: dvě
  nezávislé implementace přesné algebraické kontroly.
- runs/: zachované první běhy, stdout, stderr, metadata a certifikáty.
- AUDIT_RESULT.json: PASS_FIRST_ATTEMPTS a shoda certifikátů.
- COORDINATE_CLARIFICATION.md: rozsah jediného textového upřesnění.
- FINAL_MANIFEST.json: konečný seznam a kontrolní otisky souborů.

## Reprodukce bez přepsání prvních běhů

Oba verifikátory vyžadují jeden výstupní soubor, který ještě neexistuje.
Například z kořene rozbaleného balíčku:

    python3 verify.py /tmp/w-spectrum-primary-new.json
    python3 agents/sources_review/verify_independent.py /tmp/w-spectrum-independent-new.json
    cmp /tmp/w-spectrum-primary-new.json /tmp/w-spectrum-independent-new.json

Soubor run_one.py záměrně odmítá přepsat již existující runs/primary
nebo runs/independent. Úspěšný konečný audit ověřuje formální identity
celého symbolu, nikoli numerickou mřížku hybností. Spektrální a
přímointegrální věty vyžadují přiložené důkazy.

Konečná kapacita nové baterie není konečný počet kvantových stavů.
Přesné zachování energie není tvrzení o přesně uskutečněném cílovém
kanálu. Prostorový útlum H není bez dalšího prostorovým obvodem celého
přístroje. Tyto rozdíly jsou součástí konstrukce, nikoli dodatečnou
změnou původních závěrů.
