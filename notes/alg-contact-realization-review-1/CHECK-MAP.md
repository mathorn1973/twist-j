# P-ALG-CONTACT-REALIZATION-1: mapa konkrétního verifieru

**NON-CANONICAL, L1; návrh k přezkumu před pinem. Výsledek vědeckého běhu: NOT RUN.**
Program je `verify.py`; jediný pomocný modul je `compiler_identity_checks.py`. Nemění matematickou verzi CW-ALG-1, SPEC ani preregistraci. Při jeho přípravě a statickém přezkumu nebyl importován ani spuštěn program, žádná jeho matematická funkce ani pomocný modul. Kontrola AST/`compile` zdrojového textu není vědecký běh.

Jednotkou počtu v tabulce je **vstupní řádek příslušné smyčky**, nikoli počet jednotlivých `require`, nativních listů, stavů plného nosiče nebo opakování téhož argumentu. Na jednom řádku může proběhnout několik samostatně pojmenovaných assertions. První neúspěšná assertion zastaví běh s úplným svědkem a FAIL/exit 1. Čísla níže jsou předepsané meze a očekávané počty, nikoli již naměřené výsledky.

## Zdrojová vazba a importní rozhraní

`source_bindings` porovná surový SHA-256 SPEC a PREREG-DRAFT s explicitními konstantami ve verifieru. Obsahové otisky `verify.py` a `compiler_identity_checks.py` vypíše také; jejich povolené hodnoty musí současně určit přijatý veřejný pin. Otisk samotného verifieru není vložen rekurzivně do jeho vlastního obsahu.

Import definuje konstanty, funkce a třídu; nezačne vědecké kontroly, čtení souborů, výpis ani konstrukci gramatiky. `main()` je chráněn `if __name__ == '__main__'`. Pomocný kompilátorový modul se importuje teprve uvnitř `main`; při importu veřejného atlasového rozhraní proto není potřebný. `main` před tím vypne zápis bytecode. Výstup zapisuje přímo jako UTF-8 bajty s jediným LF pomocí `sys.stdout.buffer.write`, bez platformní změny konců řádků.

Rozhraní pro následnou oddělenou sondu:

| Funkce | Přesný vstup a výstup |
|---|---|
| `gram(p)` | `p=(x0,x1,x2,x3,y0,y1,y2,y3)`; vrací `(alpha,beta,gamma)` |
| `kappa(g)`, `width(g)`, `orbit_width(g)` | vstup je Gramova trojice; `width` nepřijímá samotné kappa |
| `target(g)`, `target_inverse(g)` | přesné M a M^-1 |
| `chart(g)` | pro nenulové g vrací `(t,a,b)`; pro nulové g je nedefinovaný |
| `atlas_encode(p)` | `(g,L4,n,j)`, nebo `None` na nulovém Gramu |
| `atlas_decode(g,L4,n,j)` | původní osmisložkový pístový vektor |
| `pi(p,eta)`, `pi_inverse(p,eta)` | dvojice `(p_out,eta_out)` |
| `reachable(p,eta)` | přesná pístová/bitová část Omega_alg |
| `native_apply(z,leaf)` | úplný stav `z=(x4,rx,y4,ry,eta,qx,qy)`, celkem 13 položek; rx na indexu 4, ry 9, eta 10, qx 11, qy 12 |

Případná byte-identická kopie pro kompozici se musí ověřit proti SHA před importem. Použití tohoto API samo neprovede nativní T_alg a neposkytuje jeho H_T matici.

## Claim → funkce → množina → druh → závislost

| Claim / assertions | Funkce | Přesná množina a počet řádků | Druh kontroly | Co ještě nese důkaz |
|---|---|---|---|---|
| Přímé původní mapy a,b,c,d,e souhlasí s Walshovou tabulkou, q tabulkou a jsou involuce | `check_native_cells` | 5 písmen × všech 5^6=15625 úplných jednobuněčných vstupů = **78125** | úplná konečná enumerace jedné buňky | druhá buňka je divák; nejde o enumeraci celého X |
| tau_q přičítá 1 a bar c,d,e mají q→−q, správný faktor a úplnou involuci | `check_native_cells`, `native_word_apply`, `bar` | tau_q **15625**; tři homogenní makra ×15625 = **46875** | skutečné provedení těchto malých nativních slov | raw listy uvnitř homogenizace jsou terminály; k velkému seed se toto provedení nerozšiřuje |
| Odpovídající mapy buňky y a neporušený divák | `check_native_cells` | všech pět písmen a15625 vstupů = **78125** identit konjugace výměnou buněk | úplná jednobuněčná tabulka a explicitní indexy | společný `native_cell` a stejné homogenizační slovo pro obě buňky |
| Walshova inverze, B_read M=L5 B_read, M MI=MI M=I, velikost SL2 | `check_native_cells` | **625** Walshových vstupů; **3** maticové rovnosti; **625** kandidátů SL2, očekáváno120 | přesné konečné/ maticové kontroly | identifikace normativních souřadnic je ve SPEC |
| Pořadí16 maker, originální A4 a A18, priority všech atomů, konečnost závislostí bez cyklu | `check_grammar_and_affine`, `Grammar`, `syntax_inventory` | **108** atomů:64 A6/A7,1 A8,1 A9,14 A11,28 A12; **3** konstanty; přesný DAG dosažitelný ze seed, těchto108 atomů a10 bar maker | kontrola konkrétní syntaktické gramatiky | `syntax_inventory` počítá unikátní uzly DAG, ne astronomický počet rozvinutých listů; univerzální CW se nekonstruuje |
| Původní translace A1/A2 a N21/N23 jsou správné i pro obsazená q,r | `check_grammar_and_affine`, `affine_word` | **12** úplných13×13 homogenních afinních matic:10 translací +2 shearů | přesné symbolické afinní matice nad F5 | úplné nativní mapy jsou ověřené předchozí tabulkou; matice13 zahrnuje12 datových souřadnic a konstantu |
| Vektor v_chi v A6 opravdu způsobí h→h+chi a správně převádí souřadnice | `check_grammar_and_affine` | **8** kovektorů: K v_chi=ell a Walsh roundtrip; navíc K=K^T | přesná lineární identita, nikoli vzorek pístů | bilinearita h spojuje identitu se všemi písty; tato bilinearita se samostatně porovnává na všech390625 párech |
| První R_ij podle délka–lex a správná znaménka | `signed_rotation_data`, `check_grammar_and_affine` | **24** dosažených podepsaných matic, **96** hran, **6** vybraných uspořádaných dvojic i,j | úplný malý Cayleyův graf | BFS připojuje list zprava, tedy násobí matici zprava; dosažené cesty a všech96 shortlex relaxací dokazují minimalitu mezi slovy této abecedy. Žádných4^23 slov se nevypisuje |
| W_a,W_b jsou involuce i pro libovolná q,r a správně přenášejí bit | `check_contact_macros`, `suffix_model` | všech **6250** `(h,eta,rx,ry,qx,qy)` ×2 brány = **12500** | úplná suffixová tabulka | algebraická faktorizační lemma: W používá h,eta a párové a/b; pístová část se nezávisle kontroluje úplně níže. Nejde o hrubou enumeraci X |
| E_a,E_b,K0 a původní Z=[K0,tau_r]^2, oba cíle r, libovolné q,r, oba bity | `check_contact_macros` | E: **12500**, K0: **6250**, Z: **12500**; doména stejných6250 vstupů | úplná tabulka přesného modelu párových pístových involucí a suffixů | tagy sledují obě komutující pístové involuce; větvení je nezávislé na tagech,q,r. Jejich zrušení pro každou pístovou dvojici nese tato identita spolu s úplným pístovým průchodem |
| Úplná q matice E,K0,Z, získaná skládací rekurencí | `model_word_q_lift`, `check_contact_macros` | stejné E/K0/Z řádky, q matice se skládá po každém modelovém listu a porovnává na všech q | přesná afinní rekurence + úplné q tabulky | r translace použité v modelu mají q identitu doloženou plnými maticemi A1/A2. Jen pro tato konkrétní Z je ověřeno H=I; nic takového se nepřenáší na T_alg |
| A5 konečná diference vrací pracovní vstup a zapisuje rozdíl | `check_polynomial_macros` | všech **3125** funkcí F5→F5 ×5 kontrol ×5 obsazených cílů = **78125** | úplná tabulka polynomových/funkčních hodnot nad F5 | odpovídající makra jsou certifikovanými translacemi/sheary; neprovádí se velké nativní slovo |
| A6 čtvrtá diference a A7 monomy | `check_polynomial_macros` | **25** `(h,chi)`; **15** dvojic `(stupeň1..3,chi)` | identity funkcí nad F5, nikoli formální koeficientový důkaz nad neurčeným tělesem | lineární kovektorová vazba A6 je ověřena výše |
| A11/A12 přenesou správný monom do správné osy | `check_polynomial_macros` | A11:6 dvojic×4 stupně×125 pracovních vektorů = **3000**; A12:7 vnějších kontrol×4 stupně×125 pracovních vektorů×5 kontrolních hodnot = **17500** | úplná konečná konjugace shearů na pracovních souřadnicích | realizaci příslušných atomů a přesný q lift určuje původní gramatika, ne tyto faktorové sheary |
| A13/A14 správně násobí kontrolní hodnoty a vrací pomocnou osu | `check_polynomial_macros` | všech **625** `(xi_i,xi_j,f,g)` | úplná funkční tabulka faktorové identity | f,g nesmějí záviset na cíli/pomocné ose; konstruktor `indicator_product` to kontroluje |
| A15 indikátor a A16 sedm kontrol | `check_polynomial_macros`, `Grammar.indicator_product` | A15 **25** dvojic; A16 všech **78125** sedmic L, právě1 aktivní | úplná tabulka kontrol + kontrola rekurzivní syntaxe | součin má pevný levý prefix/poslední faktor; rekurze vždy snižuje počet kontrol, konstruktor odmítá překryv s pracovními osami |
| K1, Psi, jejich podpory a inverze | `check_seed_support`, `workspace_k1`, `workspace_psi` |2 hodnoty aktivace×2 bity×125 pracovních vektorů = **500** | úplná konečná faktorová tabulka | aktivace celého pístového vstupu je určena samostatně ověřenými indikátory |
| A18 průnik podpor a přesná orientace jediného třícyklu | `check_seed_support`, `factor_psi`, `factor_psi_prime` |2 pístové dvojice `{p,Ap}`×25 r×2 bity = **100**; podpory10 a10, průnik1, výsledný cyklus3 | úplná tabulka na analyticky určeném sjednoceném nosiči | fixace vnějšího doplňku plyne z A16/A17 a konjugace W_a; q není tímto faktorem enumerováno ani prohlášeno za identitu |
| B3/B4 a pravidla párování transpozic | `compiler_identity_checks.run_checks` | B3 **12**, B4 **60** na5 starých symbolech; **225** uspořádaných dvojic transpozic na6 symbolech (15 stejných,120 s průnikem,90 disjunktních) | úplné malé permutační identity | dosazení libovolných názvů bodů a fixace doplňku nese obecná identita ve SPEC |
| Canonical Even, Attach2 včetně obou lichých oprav a B6 | `compiler_identity_checks.run_checks` | všech **435** sudých permutací starých množin velikosti3..6; Attach2 **204**; B6 **108** | konečná enumerace s pevným vnějším sentinelovým bodem | neenumeruje se obecná velikost nosiče. V B6 se kontrolují obě připojení i zachování starých hvězd |
| Obecná skládací rekurence H,t | `check_q_lift` | **2** souřadnicové rovnosti v řídkém polynomovém okruhu nad F5 se **14** neurčitými koeficienty/vstupy | skutečná formální koeficientová kontrola | koeficienty U se vyhodnocují v F_V(f), koeficienty V ve f; nepoužívá se faktorová identita místo q liftu |
| Úplná inverze afinních q přenosů a bijekce každého vlákna | `check_q_lift` | všech **480** matic GL2(F5) ×25 translací = **12000** afinních map; ×25 q = **300000** bodových inverzí | úplná konečná enumerace | skutečné H_T zůstává určeno neexpandovanou gramatikou; netvrdí se syntéza každé enumerované mapy |
| M/M^-1, skutečné orbitové šířky a přímý Jordanův argument | `check_reduced_orbits` | všech **125** Gramů a **1250** dvojic Jordanův vstup/k=0..9 | úplná konečná kontrola | SPEC obsahuje obecné algebraické odvození; očekávané Gramovy orbity jsou1×1,2×2,12×10 |
| Redukovaná Pi_alg, inverze, přesná dosažitelnost a cykly | `check_reduced_orbits` | všech **1280** přípustných nenulových `(g,j,eta)`;640 připravených,740 dosažitelných | úplná konečná enumerace a BFS z celé připravené množiny | multiplikace každého cyklu15000krát dokazuje sudost plného faktoru;1280 není faktor celé nativní abecedy |
| Úplný atlas, Gram/polarizace a párová A/B znaménka | `check_atlas_and_piston_bit` | všech **390625** pístových dvojic;6625 nulových;640 nenulových bloků po600 | úplná konečná enumerace | `(L,n,j)` jsou pouze souřadnice původních pístů, žádná paměť navíc |
| W_a/W_b písty/bit, oba směry inverze | `check_atlas_and_piston_bit` |2 brány×2 bity×390625 pístů = **1562500** | úplná pístová/bitová enumerace | suffixová lemma s úplnými q,r tabulkami výše rozšiřuje závěr na celé X |
| Pi_alg, oba směry inverze, L/n/slot, doména, cíl a druhý krok bez resetu | `check_atlas_and_piston_bit` | všech **781250** pístových/bitových stavů;450625 dosažitelných, z toho60000 s bitem1 | úplná konečná enumerace referenční permutace | není to provedení nativního T_alg; jeho realizaci nese CW-ALG-1 |
| Plné počty a domény T_alg | stejná funkce + `check_reduced_orbits` |11265625 pro uzávěr z r=0,eta=0 s libovolným q;281640625 při libovolných r,q; připravená množina5^10=9765625 | aritmetický důsledek přesných multiplicity | Pi_alg kopíruje obě r; nativní q vlákna jsou bijektivní. Nejde o dosažitelný uzávěr kompozice V |

## Co se záměrně nepouští a čím je to nahrazeno

Program konstruuje pouze konečný syntaxový DAG atomů a seed, přesné malé afinní matice a uvedené konečné tabulky. `native_word_apply` má pevnou rozpočtovou pojistku a je volán jen pro malá homogenizační slova. Není volán pro C_star, CW(Pi_alg), T_alg ani N-3 připojovacích kroků. Nevytváří seznam všech slov délky N, neočekává čisté pracovní registry a nenahrazuje Pi_alg nativním primitivem.

Následující závěry zůstávají výslovnými analytickými závislostmi:

- klasifikace systémů bloků a primitivita z SPEC5.1;
- souvislost hypergrafu konjugovaných podpor do délky N z SPEC5.3;
- přenos ověřených lokálních identit na přesný syntaxový DAG A1–A18 při libovolných pracovních hodnotách;
- univerzální dosazení B3–B6, konečnost N−3 a deterministický kompilátor B1–B7;
- globální trojúhelníkový lift, konečná rekurence H_T a inverze **téhož** pevného slova;
- úplná q vlákna a přesné navrácení r na hranici T_alg.

Žádný PASS omezených kontrol sám neoznamuje přijetí těchto důkazů, veřejné začlenění sondy ani v100. Program nevypočítá H_T, netvrdí H_T=I, plnou periodu10, praktickou délku slova ani nové čerstvé záznamy při opakovaném V.

## Běh, výstup a změny před pinem

Navržený jediný vědecký příkaz je `python verify.py` v tomto adresáři, na Pythonu3.12, až po přijatém veřejném pinování a aktuální currency gate. Architektury a přesný PR head, surová bajtová shoda stdout s jediným committed EXPECTED.txt z prvního řádně připnutého dokončeného běhu, exit0/prázdný stderr a souhrnná kontrola se řídí nezměněným PREREG-DRAFT a aktuální politikou. Žádná normalizace stdout není dovolena.

Známé assertion/ValueError se převádějí na jedno deterministické FAIL JSON a exit1. Neočekávaná implementační chyba také znamená FAIL s typem chyby, nikdy přeskočení kontroly nebo úspěch. Program nepíše výsledkové soubory ani EXPECTED; stdout/stderr zachytí autorizovaný vykonavatel odděleně.

Před pinem jsou tento zdroj a mapa určeny ke statickému přezkumu. Po pinování se zmrazené vstupy nepřepisují; opravy vyžadují postup dispozice a případného nástupce podle veřejné politiky. Aktuální stav tohoto dokumentu nepředstírá, že jakýkoli vědecký běh již proběhl.
