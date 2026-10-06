# PREREG-DRAFT — P-ALG-CONTACT-REALIZATION-1

**NON-CANONICAL, L1; návrh před přezkumem, nikoli přijatý RunSpec.**
Datum 2026-10-06. Pevná navržená verze kompilátoru: `CW-ALG-1` ze `SPEC.md`.
Žádná nová sonda, verifier, vědecká enumerace ani expanze nativního slova nebyla při přípravě spuštěna. Tento soubor neopravňuje veřejný běh.

## Jedna otázka a oddělení sond

Rozhodnout přezkumem, zda přesně tato konečná gramatika realizuje algebraický cíl Pi_alg na plném nosiči včetně libovolných q,r, s úplnou inverzí a vymezenou dosažitelností. Zachovat rozdíl algebraického vykonávače a skutečného nativního slova. `P-CONTACT-RECORD-1` zůstává samostatná. Složení V=A_y T_alg A_x, jeho společná příprava a oba záznamy mají dostat samostatnou spojovací větu a nejsou úspěchovým kritériem této sondy.

## Před každým případným veřejným během

Příslušný vykonavatel musí přečíst tehdy aktuální STATUS, POLICY, AGENTS, CORE a relevantní veřejný frontier, obnovit autoritativní stav a splnit jeho currency gate, kolize a požadované přijetí návrhu. Konkrétní veřejné identifikátory sondy, commity, kontrolní SHA, reviewer a architektury se doplní až podle tohoto postupu. Historický zdrojový commit 68080edc12faf029de48181f0a384f66e42dbc04 není náhradou aktuální kontroly. Tento návrh neobchází případnou novější podmínku nebo předepsanou pauzu.

Před přijetím zmrazení musí být přezkoumány SPEC, tento návrh a budoucí verifier. Zmrazení musí pojmenovat neměnný commit, přesné SHA-256 všech vstupů a verifieru, příkazy, očekávané množiny testů a počty, verzovanou metriku a architekturní kontrakt. `SOURCE_PROVENANCE.json` je pouze provenance vstupních podkladů, nikoli takové přijaté zmrazení. Před přijetím pinů lze přezkumný návrh upravovat. Po přijetí pinů jsou kód, preregistrace a další zmrazené vstupy neměnné: žádný rebase, amend, force-push ani opětovné použití téhož frozen probe pro změněný obsah. Nutná oprava se řeší dispozicí původní sondy a případným nástupcem přesně podle tehdy platné veřejné politiky; nesmí přepsat zmrazený kód, preregistraci ani výsledky.

## Kontrolovatelný rozsah

Konečný důkaz realizace se přezkoumá analyticky: přesné homogenní listy, jejich priority, A1–A18, primitivita, souvislost hypergrafu do N, B1–B7 a dosazení sudé Pi_alg. Kontrola se týká této verze včetně originálního Z v A4 a W_a v A18. Varianty Z20, Z48, DP stromy a W_b-only nejsou součástí cíle.

Následující design je určen pro budoucí přesný verifier ve standardním Pythonu 3. Neobsahuje závislost na PHITORCH, NumPy, SIMD ani náhodném vzorkování. Verifier se nejprve sepíše, staticky přezkoumá a samostatně zmrazí; tento dokument jej nepředstírá jako již existující spuštěný program.

### A. Úplné malé mapy a syntaktické základy

- Ověřit přesné původní jedno­buněčné mapy a jejich involutivitu ve všech 5^6 stavech každé mapy; konjugace tau_q a bar c,d,e mají plnou očekávanou q mapu. Druhá buňka je divák. Explicitně ověřit, že raw listy uvnitř homogenizačních definic jsou terminály.
- Ověřit Walshův roundtrip na 5^4 pístových čtveřicích, polarizační matici K, B_read M=L5 B_read, M^-1 M=M M^-1=I a zachování h-nulové podmínky párovými A,B.
- Ověřit W_a,W_b na každé pístové dvojici a obou bitech. q,r účinek se odvozuje z úplných nativních tabulek a z příslušného exponentu; buď se kontroluje oddělenou úplnou tabulkou všech q,r, nebo se použije výslovně přezkoumaná algebraická faktorizační lemma. Verifier nesmí tvrdit plnou hrubou enumeraci X, pokud ji neprovedl.
- Ověřit pořadí 16 makrolistů, všech terminálů a pravidla precedence. Vygenerovat jen malý seznam 24 podepsaných permutačních matic pro R_ij; pro každou uspořádanou dvojici i,j prokázat shodu prvního krátkého reprezentantu s pořadím délka–lex délky nejvýše 23. Neprocházet doslova všechna 4^23 slova: BFS v tomto 24prvkovém grafu se stejným pořadím hran produkuje totéž první slovo, pokud je toto zdůvodnění součástí přezkumu.

### B. Identita maker a q-lift

- Translace A1/A2 a lineární makra A8/A9 se ověří jako afinní mapy úplných buněk kompozicí malých matic; nevyžadují expanzi žádného velkého seed slova.
- Důkaz A3/A4 musí zahrnout obě větve h a obě hodnoty bitu, s libovolnými pomocnými r; vstupní q se nesmí mlčky připravit. Příslušné q matice a translace se počítají přesnou afinní rekurencí, nikoli jen na q=0.
- Diference A5–A7 se kontrolují jako identity polynomových funkcí nad F5. Multiplikátor A13/A14 na všech 625 čtveřicích (xi_i,xi_j,f,g)∈F5^4; f,g jsou hodnoty kontrol nezávislých na obou pracovních souřadnicích. To ověřuje místní identitu, nikoli celou nativní expanzi.
- A15 a sedm kontrol L v A16 mají deklarované souřadnice, pořadí a pomocnou osu. Zkontrolovat nerekurzivnost priorit atomů a pokles počtu indikátorů v A14. Podporu A17/A18 a orientaci C_* ověřit přesnými cykly na konečném sjednocení podpor a jeho obrazech; analytický argument musí doložit fixaci doplňku.
- B3–B6 ověřit jako přesné permutační identity na minimálních symbolech. Analytický přezkum zvlášť pokrývá terminaci N-3, pevné pořadí hran a libovolnou velikost konečného nosiče.
- Q lift testuje obecnou kompoziční a inverzní rekurenci afinních dvojic H,t. Celý H_T není numericky vypočten; přesně jej určuje fixovaná gramatika. Úspěch nesmí být vykázán jako q identita ani jako replay T_alg na úplném nosiči.

### C. Atlas a malá cílová permutace

- Pro všech 5^8=390625 pístových dvojic: spočítat Gram a u nenulového Gramu přesný chart, encode/decode roundtrip, det L=1 a kuželosečkovou rovnici. Nulový Gram má 6625 pístových dvojic; všechny zůstanou zvlášť označeny jako nulová větev.
- Pro všech 2·5^8=781250 pístových/bitových stavů: dopředný a inverzní roundtrip Pi_alg, zachování L,n, přesné větvení, rovnost G'=MG na dosažitelné části, invariance dosažitelnosti oběma směry a druhá aplikace bez resetu. Obě r jsou v definici kopírované a q se tohoto referenčního algoritmu neúčastní; toto se musí uvést jako analytické rozšíření, nikoli předstíraná enumerace všech 2·5^12 stavů.
- Pro všech 124 nenulových Gramů a jejich přípustné j,eta: přesně 1280 redukovaných stavů; 640 bit0, 740 dosažitelných, 540 pevných bodů, deset dvoucyklů a 72 deseticyklů. Nezávislým průchodem 125 Gramů ověřit M orbitové maximální šířky a podmínku m*=5 právě na s(2,1,3), s≠0.
- Z analytických multiplicity 120·5=600 a libovolných r,q odvodit velikosti 450625 dosažitelných pístových/bitových stavů, 11265625 dosažitelných stavů T_alg z r=0,eta=0 s libovolnými q a 281640625 při libovolných r,q. Verifier musí odlišit tato tři čísla od velikosti jednorázové připravené množiny 5^10.

### D. Výslovně zakázané expanze a falešné závěry

Nespouštět expanzi T_alg, seznam všech slov délky N, celé N-3 konstrukční smyčky ani miliardové seed slovo. Nepřidávat alternativní native primitiva, novou paměť, runtime index, reset nebo přípravu mezi kroky. Netvrdit praktickou cenu T_alg, minimální délku, shodu s lex Pi, q identitu, plnou periodu 10 nebo čerstvý záznam při opakování V. Cíl M nesmí vstoupit do změny zdrojových bran, jejich řídicího čtení či kompilátorového seed mechanismu.

## Architektury a výsledky

Veřejný běh vyžaduje tentýž přesný PR head na x86_64 a aarch64, Python 3.12 a shodný SHA-256 zmrazeného verifieru. Obě architektury musí skončit exit code 0, mít prázdný stderr a surový stdout bajtově totožný s jediným committed EXPECTED.txt, zachyceným z prvního řádně připnutého dokončeného běhu. Nesmí se normalizovat konce řádků, mezery ani jiné bajty výstupu a nesmějí existovat odlišné architekturní EXPECTED soubory. Stejný PR head musí mít úspěšné obě architekturní kontroly i povinnou souhrnnou kontrolu. Úspěch jednoho hostu, dvou různých headů nebo dvě spuštění na téže architektuře nestačí. Před každým během se znovu ověří aktuální veřejná autorita; případné její další požadavky platí navíc.

Evidence uvádí neutrální údaje OS, architekturu, verzi/build Pythonu 3.12, přesný PR head, SHA-256 vstupů a verifieru, příkaz, surové stdout/stderr a exit code. Soukromá jména hostitelů ani místní identifikátory prostředí se nepublikují. Metadata závislá na prostředí patří do oddělené evidence, nikoli do deterministického stdout porovnávaného s jediným EXPECTED.

Výstup má být deterministický JSON s verzí schématu, verzí CW-ALG-1, SHA vstupů, přesnými počty, každou assertion, status PASS/FAIL a případným prvním úplným protipříkladem. Surové stdout, stderr a exit code se uchovají odděleně pro každou architekturu. Všechna nynější pole výsledku jsou **NOT RUN**.

## Kritéria rozhodnutí

Analytický reviewer musí přijmout celý generující a kompilační důkaz i pevnost q liftu. Případný verifier smí přidat pouze candidate-C v přesně provedeném omezeném rozsahu. Nesoulad priority, listové mapy, atlasu, inverze nebo domény je FAIL se zachovaným prvním svědkem; nesmí se přejmenovat za úspěch. Chybějící architektura, přijaté piny nebo nezávislý přezkum zůstává nesplněnou podmínkou. Samostatné přijetí této sondy ještě není společné začlenění v100.
