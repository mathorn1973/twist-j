# Nezávislá kontrola souřadnicového výsledku

**NON-CANONICAL.** Vlastní přesná implementace oponenta prošla 94 kontrolami, exit 0, prázdný chybový výstup. Oponent četl pouze zmrazený prereg; nepoužil autorův kód ani jeho výsledky.

Úplný nezávislý důkaz, koeficientový certifikát, prostředí, běhy a auditní poznámka jsou beze změny v PROOF.txt. Přesné koeficienty a jednotlivé kontroly obsahuje report.json. Manifest oponenta je zachován jako manifest.json.

## Reprodukce původního zdroje

Skript check.py obsahuje pevné cesty:

    /tmp/twistj-trefoil-coordinate-20261017/PREREG.md
    /tmp/twistj-trefoil-coordinate-breaker-20261017/

Pro reprodukci umístěte přesný soubor PREREG.md z části author do první složky a nezměněný check.py do druhé. Potom spusťte:

    python3 /tmp/twistj-trefoil-coordinate-breaker-20261017/check.py

Skript potřebuje pouze standardní knihovnu Pythonu. Vypíše souhrn a do své výstupní složky zapíše report.json. Zachycené původní deterministické výstupy jsou v tomto balíčku jako stdout.txt a stderr.txt; detail běhů je v execution.json.

Balení kód ani jeho cíle neupravuje. Prostředí původní kontroly bylo x86_64, CPython 3.12.14. Nejde o kontrolu na dvou architekturách.

## Přesná auditní hranice

První úspěšný pomocný běh obsahoval časový údaj elapsed_seconds. Oponent jej poté odstranil z reportu a souhrnného stdout a uchoval dva bitově shodné deterministické běhy. Původní výstupní názvy byly mezitím přepsány. Zmrazený prereg, cíle, aritmetika ani kontrolní logika se nezměnily.

Původní zdroj byl přesně obnoven zpětnou aplikací zaznamenané změny do recovered/check-first-run.py. Je označen jako obnovený; jeho otisk souhlasí s původně zaznamenaným otiskem. Původní report ani stdout se za uchované soubory nevydávají. Vlastní vysvětlení oponenta je v PROOF.txt a recovered/README.txt.

Pro reprodukci tohoto dodání je rozhodující uchovaný check.py s SHA-256

    0e75951089d8ee86ed81c6c66babbc72d6750117127ea17f6aaecfdae9c4273b

a jeho report.json s SHA-256

    54afe0e79087137a4f5008fcd65c25a154ed4611fe119563599966342999f8ab

