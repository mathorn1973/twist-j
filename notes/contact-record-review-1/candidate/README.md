# Kontaktní záznam s chráněným prvním výsledkem

NON-CANONICAL, L1. Návrh jediné sondy P-CONTACT-RECORD-1 před veřejným pinem.

Za výslovně přijatých map W_b a Ucal_i, jednorázové přípravy a pevného
koncového čtení platí řetězec

\[
K_i\longrightarrow\mathcal U_iK_i\mathcal U_i
\longrightarrow(r_x,r_y)\longrightarrow m_x=r_x^2.
\]

[PROOF.md](PROOF.md) obsahuje úplné definice, mapy a inverze na
F5^12×{0,1}, ostré minimum samostatné tří­stavové reference v deklarované
klasické jednovolací třídě, složení druhé čtečky z úplného obsazeného výstupu
první a ochranu m_x po každém listu druhé čtečky. Vložené r_i má pět stavů,
tři pracovní hodnoty na oracle rozhraní a dva garantované koncové výsledky.
Vazba čte q_i; h ani volba experimentu nejsou jejími řídicími vstupy.

Úplná aktivní čtečka není obnovitelný archiv: už druhé stejné použití
může vrátit flag na nulu, pátá mocnina je identita. Dokončený nulový test
je úplným stavem totožný s nepoužitým vstupem. Záznam proto sám nepotvrzuje
dokončení. Ochrana prvního čtverce platí pro uvedené druhé slovo, nikoli
pro d_x,e_x,Ucal_x či celý původní provoz. Nedokazuje fyzickou realizaci,
nerušivý detektor, autonomní implementaci nebo termodynamickou cenu.

## Přesný rozsah ověřování

[PREREG.md](PREREG.md) fixuje šest polí a nulové tolerance.
[verify.py](verify.py) používá pouze Python 3.12 standard library a přesnou
aritmetiku. Malé afinní, bilineární a větvové kontrakty dokazují úplný
kontakt; úplné tabulky potom ověřují čtení a skládání. Pět pevných
pístových svědků je zvlášť označenou doslovnou diagnostikou, nikoli
náhradou důkazu či novou velkou enumerací.

Formální běh patří až za veřejný pin preregistrace a přijatého ověřovače
podle POLICY.md. Tento návrh dosud nemá nový formální RUN ani EXPECTED.
Po pinování se spouští z kořene repozitáře:

    python3 probes/P-CONTACT-RECORD-1/verify.py

Vyžaduje se exit0, prázdný stderr a byte-identical stdout proti jedinému
EXPECTED.txt na obou veřejných architekturách a úspěšný agregát check.
Samostatný přesný důkaz a výpočetní evidence mají odlišnou evidenční roli.

## Původ podkladů

Návrh konsoliduje čtyři dříve zmrazené místní reporty z 2026-10-06:

- q-holonomy: úplná mapa K_i a její doslovné slovo;
- q-readout: tabulka Ucal_i, jednovolací minimum a hranice opakování;
- two-contact-records: skutečná druhá čtečka z obsazeného výstupu první;
- square-readout, ADDENDUM: listová invariance r_x².

Jejich obsahové otisky a rozsahy nese [SOURCES.json](SOURCES.json). Jde
o podpůrnou místní jednoarchitekturní evidenci; není závislostí běhu tohoto
ověřovače. Veřejné tvrzení má samostatný důkaz a definice zde. Nekopírují
se historické interprety, binární soubory, velké výstupy ani osobní údaje.
Všechny mapy jsou buď uvedená původní písmena, jejich složeniny, nebo
výslovné vstupy rozšířené architektury již použité ve zdrojových reportech.

Samostatná entropická bilance původního autonomního U se do této sondy
neimportuje. Landauerův vztah není její závěr ani nový zákon TWIST-J.
QUADRATIC-MEMORY-NATIVE-CONTACT a fyzičtí vlastníci zůstávají ve svých
veřejných statusech; návrh nedává podklad pro jejich přesun.
