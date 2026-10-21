# Zdroje a rozsah kontroly

## Veřejná autorita při zveřejnění poznámky

- Aktivní [Public Canon v104](https://github.com/mathorn1973/twist-j/blob/4a50e527d20018839f006ed312454b710e6486b4/canon/CANON.md), obsahový commit `4a50e527d20018839f006ed312454b710e6486b4`.
- Základ publikace a rozbalený tag `canon-v104`: `e6240e2689bb22aab5f02bad90b75d3692bb96d9`. Obsahový commit i tag jsou předky základu; všech pět normativních otisků souhlasí.
- `canon/CANON.md`: 1 262 204 bajtů, SHA-256 `c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d`. Aktivní soubor je bajtově totožný s kandidátem použitým při původním rozboru níže.
- [Vyhrazení této poznámky #1707](https://github.com/mathorn1973/twist-j/issues/1707). Zveřejňuje se již hotový analytický výsledek, nikoli předem neznámá výpočetní zkouška. Běžné kontroly repozitáře nejsou vědeckým přehráním důkazu.

## Původně prohlédnutý veřejný základ v103

- Aktivní zdroj při původním rozboru: Public Canon v103, obsahový commit `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`.
- `canon/CANON.md`: 1 052 518 bytů, SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`; místní dříve ověřená kopie porovnána se stavem uvedeným v STATUS.
- [Afinní jedinečnost](https://github.com/mathorn1973/twist-j/tree/canon-v103/probes/P-AFFINE-QUADRATIC-READING-1): zdroj druhého kroku důkazu, s přesnými předpoklady celé afinní akce.
- [Kánon v103](https://github.com/mathorn1973/twist-j/blob/01fb76f6b3b14a6a5ec05d0017ea922390ab6f66/canon/CANON.md): stopové párování, Gram a rozsah algebraických čtení.

## Původně prohlédnutý kandidát v104

- [PR #1704](https://github.com/mathorn1973/twist-j/pull/1704), první zachovaný kandidát; při původním rozboru byl označen „do not merge“ a odkazoval na tehdy připravovaného nástupce. Tento stav není matematickou námitkou k jednotlivým zde citovaným větám.
- Obsahový commit: `957b27ce26edbc13600b17c89b9ba870ed472716`.
- [Kánon kandidáta](https://github.com/mathorn1973/twist-j/blob/957b27ce26edbc13600b17c89b9ba870ed472716/canon/CANON.md): 1 262 204 bytů, SHA-256 `c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d`. Soubor skutečně stažen a otisk ověřen.
- Registr kandidáta: SHA-256 `abfa07b8b01820969cad68ae3a630b9420edc1f2be3203ab6ca6b646746035f5`.
- [Vydávací úkol #1700](https://github.com/mathorn1973/twist-j/issues/1700): výslovně stanoví existenční rozsah vydání a nevyžaduje globální jedinečnost dekodéru. Tento průzkum jedinečnosti jeho rozsah nemění.

## Analytická kontrola tohoto zápisu

### Navazující veřejné zdroje

- [PR #1681](https://github.com/mathorn1973/twist-j/pull/1681), sloučený zdroj `C-JM-RETAINED-PAIR-SOURCE-N`; prohlédnutý head `348132012dd506317d33c084461226a11686cf5d`, merge `202f70c87c8d790dbf3f329a0b54bb18bc7c5337`.
- [Přesný důkaz zdroje](https://github.com/mathorn1973/twist-j/blob/348132012dd506317d33c084461226a11686cf5d/notes/C-JM-RETAINED-PAIR-SOURCE-N/PROOF.md): obsahuje již zvolený program z₀, jeho čtyřsouřadnicovou matici, univerzální racionální reflexi a invariantní mřížku pro pevný program. Nová práce tyto konstrukce nevydává za nové; dokazuje jejich vazbu k výběru čtení.
- [PR #1699](https://github.com/mathorn1973/twist-j/pull/1699), sloučený zdroj `P-INTEGER-RETAINED-PAIR-SOURCE-1`; prohlédnutý head `2d218c6bde2335daed76e8ad3469074186b282e3`, merge `47128bdbf7650673b6f1bfc0c9ce8babb0c3b454`. Zdroj univerzálního zdvihu a zadaného celočíselného buněčného účtu; přímé vzorce byly čteny v připnutém kandidátu v104.
- `DRIFT-IS-THE-READ [T]` v původně prohlédnutém v103, oddíl 10: D=A₁ΣA₁=(1/5)[[3,−4],[−4,−3]]. Jde pouze o algebraické srovnání s nalezenou maticí, nikoli o povolení jejího nativního dynamického použití.

### Rozsah spolupracující kontroly

Věta o promíchání byla rozebrána dvěma spolupracujícími matematickými kontrolami v témže sezení. Obě obdržely hypotézu a navržené promíchání. Nezávisle sestavily důkaz konečnými rozdíly a identifikovaly nutnost celého racionálního prostoru. Následná kontrola ověřila celočíselnou involuci včetně nulového čitatele a přesné zachování společného obsahu. Hlavní autor znovu prošel každou implikaci, porovnal ji s uvedenými veřejnými zdroji a zapracoval protipříklady pro skládání a zásobník.

Jde o spolupracující analytickou kontrolu vystavenou zadání, nikoli o nezávislou vnější přejímku. Nebyl spuštěn žádný vědecký číselný ověřovač, žádná konečná enumerace není používána jako důkaz a není tvrzen výpočetní průkaz na dvou architekturách. Souborové otisky a kontrola balíčku jsou pouze kontrolou předání dokumentů.

Poznámka se zveřejňuje pod `notes/C-AFFINE-MIXING-READING-N/` jako NON-CANONICAL, L1, candidate-T. Registr ani kánon se tím nemění. Starší přiložené interní verze nejsou zdrojem současné autority. Není tvrzena novost obecné funkční věty v matematické literatuře.

Při pokračování byl výslovný JM invariantní podprostor nalezen jednou spolupracující větví a poté znovu analyticky odvozen druhou větví i hlavním autorem. Následná konstrukce pěti prokládaných buněk a pevného celočíselného jmenovatele byla posouzena odděleně od univerzálního gcd zdvihu. Kontroly znaly zadání a výsledek; nejsou vydávány za slepé nebo vnější nezávislé ověření. Ani při pokračování nebyl spuštěn nový vědecký program.

## Pokračování: pevná reference a racionální efekty

- V témže připnutém kandidátu byly přečteny `QDD-THREE-ATOM-PARTITION-COMPLETENESS [T]`, `QDD-OBSERVABLE-READING-FAMILY [D]` a `A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS [T]`. První dva rozlišují algebraické skládání zadaných kvadratických záznamů od volby jejich fyzikálního významu. Třetí výslovně dokládá, že normalizace na všech racionálních ortogonálních rámcích sama kvadratické váhy nevynucuje.
- Paul Busch, [Quantum states and generalized observables: a simple proof of Gleason's theorem](https://arxiv.org/abs/quant-ph/9909073), Phys. Rev. Lett. 91, 120403 (2003), [DOI](https://doi.org/10.1103/PhysRevLett.91.120403). Zdroj známého odvození stopové reprezentace z vah na efektech; přečten úplný text.
- Carlton M. Caves, Christopher A. Fuchs, Kiran Manne a Joseph M. Renes, [Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements](https://arxiv.org/abs/quant-ph/0306179), Foundations of Physics 34, 193–209 (2004); prohlédnut [úplný text v1](https://arxiv.org/html/quant-ph/0306179v1). Výslovně řeší i racionální prostory a odlišuje celou efektovou doménu od projektorových rámců. Obecná efektová věta v dodatku není nárokována jako nová.

Nová referenční konstrukce byla analyticky přepočtena hlavním autorem a další spolupracující větví: kolmost, pevnost reference, pětibuněčné kódování, celočíselný přechod a účet 165D²+(64/5)D²(q₊(x)+q₊(y)). Důkaz výběru z relativních vah byl kontrolován odděleně od kalibrace c=2/25; kalibrace používá normu referenční amplitudy, nikoli náklad zápisu jmenovatelů. Dodatek s racionálními efekty má samostatný důkaz v obecném racionálním Gramu. Ani zde nejsou provedeny fyzikální zkoušky předpokladů, vědecké výpočty nebo vnější přejímka.
