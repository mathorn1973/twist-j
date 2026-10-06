# P-CONTACT-RECORD-1 — samostatné přijetí pro formální sondu

NON-CANONICAL, podmíněný L1 kontrakt. Dispozice 2026-10-06.
Vlastník: `v100-contact-review-20261006`, veřejná rezervace [#1385](https://github.com/mathorn1973/twist-j/issues/1385), přezkumná předloha [#1388](https://github.com/mathorn1973/twist-j/pull/1388).

Přijímá se přesný původní důkaz a omezený ověřovač z notes commitu
`8128286127f1a48b01ebda1a5c1e7a0d88d46095`, bez změny rozsahu.
Samostatný [PROOF-REVIEW.md](PROOF-REVIEW.md) dokládá statické matematické
čtení a vlastní odvození úplných map, inverzí, minimální reference a prefixové
ochrany. Přezkum provedl oddělený agent v téže pracovní relaci; nepředstírá
externí institucionální posudek. Koordinující vlastnická session přijímá jeho
dispozici pro tento přesný podmíněný L1 důkaz a povoluje následující formální pin.

Pět původních souborů PROOF.md, PREREG.md, README.md, SOURCES.json a verify.py
se přenáší bajtově beze změny. PACKAGE.json obsahuje jejich jednotlivé otisky
a původ. Ověřovač má SHA-256
`99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134`;
preregistrace `24a24ee5b055fec4b6a1cd6ebb5b4a3ffcec2e0e078b5f5937111e8a253ba4cd`;
důkaz `805137842d66894b36cc5cef17b45bf1c67b81570bf9eb8a4c77c9394d40abf5`.
Historické označení návrhu v původní preregistraci/README zůstává zachováno;
tato samostatná dispozice je přijímá pro formální fázi a nemění žádnou rovnici,
doménu, počet, práh ani důkazní hranici.

Příkaz z kořene repozitáře je `python3 probes/P-CONTACT-RECORD-1/verify.py`.
První běh následuje až po pushi a veřejném byte readbacku celého pinu.
Místní prostředí je Linux, CPython 3.12; limit 600 s. Potom jeden přesný
EXPECTED.txt a RUN.md, RESULT.md. Následné veřejné x86_64 a aarch64 běhy
musí použít tentýž PR head, Python 3.12, shodný verifier, exit 0, prázdný
stderr a bajtově shodný stdout. Platí aktuální POLICY, nikoli starší zkrácený
jednorunnerový popis v AGENTS. Žádné spuštění nepředcházelo přijetí a pinu.

Přijímá se pouze deklarovaný rozšířený přístroj s W_b, Ucal_i, počáteční
přípravou a pevným čtením jako předpoklady. Nedokazuje se jejich fyzická
dostupnost. Původní kontaktní věta dovoluje oba počáteční bity; nevyžaduje
eta=0. Nevkládá se T_alg a nemění se na spojovací větu.

Přijetí důkazu, správnosti omezeného ověřovače a úspěch budoucího běhu jsou
tři různé skutečnosti. Tento záznam neobsahuje vědecký PASS ani přidělení
kanonického statusu T. Canon v99 a status vlastníků zůstávají beze změny.
