# Původ podkladů a hranice ověření

**NON-CANONICAL — L1; česká konsolidace, 2026-10-03.**
Tato poznámka rozlišuje dostupné matematické argumenty, hlášené výpočty
a chybějící spustitelné podklady. Nevytváří veřejný status `T` ani `C`.
Práce je vymezena v [issue #1347](https://github.com/mathorn1973/twist-j/issues/1347).

## Veřejný základ

Autoritou je aktivní **Public Canon v97** podle veřejného `STATUS.md`.
Konsolidace vychází z veřejného `main` na commitu
`01821412879dba442e1c864c61855fb4a4dfea99`.

| Položka | Ověřená hodnota |
| --- | --- |
| Obsahový commit v97 | `82ecf0aac0ee79c947000968e71573d4c65d386d` |
| Cíl značky `canon-v97` | `738e0421bd15aaea5bb6ef2a56f1cab752d44de5` |
| SHA-256 `canon/CANON.md` | `257f83a386aad7d309f7017bd719b6212e3cffea60e4986caa5169d6543f108d` |
| Velikost `canon/CANON.md` | 897762 bajtů |

Při přípravě byly porovnány otisky všech pěti normativních souborů
s veřejným `canon/SHA256SUMS`; všechny souhlasily. Obsahový commit a značka
jsou předky uvedeného veřejného základu. Tato poznámka normativní soubory nemění.

Veřejný běh kontrol [37062307698](https://github.com/mathorn1973/twist-j/actions/runs/37062307698)
na tomto základu uspěl v úlohách x86_64, aarch64 i souhrnné kontrole.
To dokládá stav kontrol veřejného repozitáře. Nereprodukuje to nový program
se zachovanou historií, jehož zdroje v dodaných podkladech chybějí.

## Dodané textové podklady

1. `TWIST-J_MAPA_CTENI_KASKADY_A_SEDMI_NUL_2026-10-02_CZ.md`:
   mapa kaskády, šestinulového a sedminulového testu a tehdejší hranice kontaktu.
   SHA-256: `4a05494273293ce5f8b8636f9908545e9bcb79183663f276d2e90ef73ee674af`.
2. Uživatelské shrnutí společného kontaktu: dva porty, placené archivy,
   konečná rovnoměrná reference, energetický účet a rozlišení skutečného
   stavu pole od účinného vstupu archivních pravděpodobností.
   Jde o zprávu, nikoli o dodaný archiv zdrojového kódu.
3. `Vložený text.txt`, titul „J-kontakt: už stavíme stroj s pamětí“:
   jeden J kontakt s více následnými měřeními, trojúhelníková reference,
   uchování korelací a hlášená spustitelná realizace.
   SHA-256: `ec44817a8762a01c6081b9d376e058b7516d9d76e418edc806484ebb7b81d927`.

Otisky identifikují přečtené texty, nikoli důkazy o jejich tvrzeních.
Původní přílohy se zde nekopírují. Konsolidace přebírá matematické zadání
a samostatně uvádí předpoklady argumentů; zdrojové označení `candidate-T/C`
není zápisem do veřejného registru.

## Dostupné a nedostupné důkazy

| Tvrzení nebo podklad | Stav této konsolidace |
| --- | --- |
| Normalizace trojúhelníkového profilu, překryv, střední energie a porovnání s plochým profilem | Algebraicky přezkoumáno ze zadaných definic. |
| Sedmá nula a uvedené racionální příklady | Přezkoumáno za explicitních předpokladů energetického rozšíření a účinné mapy. |
| Skládání energetických rozšíření a celková chyba historie | Matematický argument s uvedenými podmínkami společných úplných bloků a zachování korelací. |
| Účet a počet kroků hlášeného programu s pracovními ukazateli | Konzistentní schéma; samo o sobě neověřuje úplný program na všech stavech. |
| Zdejší samostatná realizace dvou J kontaktů | V PROOF.md je úplná unitární dilatace placeného zápisu, energetický lift a společný výstup se čtyřmi archivy. Jde o analytický důkaz na přijatém nosiči, ne o rekonstrukci či běh dodaného programu. |
| Integrita 92/92 souborů | Hlášeno v uživatelském shrnutí; příslušný souborový balík zde nebyl ověřen. |
| 4 664 kontrol v původní mapě | Hlášený výsledek zdrojového textu, zde neopakovaný. |
| 5 955 kontrol a 35 úplných průchodů nového stroje | Hlášeno v novém textu; zdroje, očekávaný výstup a běhové záznamy nebyly dodány. |

Chybí původní balík označený `j-contact-20261003(1)` i
`J-KONTAKT_STROJ_S_PAMETI_2026-10-03.zip`. Odkazy s prefixem `sandbox:`
v dodaném textu nejsou veřejně dostupnými přílohami tohoto repozitáře.
Samotné uvedení názvů `verify_integrity.py` a `retained_machine.py`
nedokládá jejich obsah ani provedení.

Analytické kontroly provedlo několik agentů v téže pracovní konverzaci.
Znali předkládané výsledky a cíle kontroly. Jde o oddělené rozbory,
nikoli zaslepený externí posudek nebo nezávislou vědeckou reprodukci.
Pro tuto poznámku nebyl spuštěn nový formální vědecký běh; neobsahuje
verifikátor, `RUN.md` ani `EXPECTED.txt`. Repozitářové kontroly tuto absenci nenahrazují.

## Hranice vůči veřejnému Canon

Živý registr v97 již uvádí `FIELD-CONDITIONAL-POINTER-INSTRUMENT`,
`FIELD-COHERENT-POINTER-PREPARATION` a `FIELD-FETCHED-PROGRAM-CONTROL`
se statusem **T**, vždy v jejich přesně vymezeném rozsahu. Starší popis
těchto veřejných výsledků jako pouhých kandidátů není aktuální.
Tento status se nepřenáší na nový přístroj ani na nepřiložený program.

K ověření hlášené implementace je potřeba dodat zdroje, úplné definice
přechodů a okrajů, integritní manifest i původní běhové podklady.
Případná formální veřejná reprodukce musí následovat pravidla předregistrace
a nemůže zpětně vydávat toto čtení textů za provedený výpočet.
