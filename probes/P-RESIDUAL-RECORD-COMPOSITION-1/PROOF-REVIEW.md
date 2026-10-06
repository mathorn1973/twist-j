# V100-JOIN-1 — samostatná dispozice důkazního přezkumu

**NON-CANONICAL, L1. Statický matematický přezkum existujícího spojovacího důkazu, 2026-10-06.**

**Dispozice: spojovací důkaz je přijatelný v přesně deklarovaném podmíněném L1 rozsahu.** Nenalezena blokující matematická chyba ve složení na úplném nosiči, jeho inverzi, jednorázových záznamech, přesném obrazu přípravy ani doméně pokračování. Doporučení je podmíněno přesnými dvěma důkazními závislostmi uvedenými níže. Neznamená již provedené veřejné přijetí, formální PASS ani připravenost společného foldu v100.

Tento záznam vznikl odděleným přezkumným čtením celého PROOF a vlastním odvozením spojovacích kroků v téže agentní pracovní relaci. Přezkoumávající se dříve účastnil přípravy algebraické specifikace a jejího ověřovače; nejde o externí institucionální ani personálně nezávislý posudek algebraické závislosti. Nezměnil se PROOF, jeho preregistrace, žádná závislost ani verifier. Nebyl spuštěn ani importován žádný matematický program. Výpočty otisků a porovnání Git blobů pouze identifikují přezkoumávané bajty.

Jde o přezkum již předloženého V100-JOIN-1, nikoli o novou definiční předlohu nebo rozšíření věty. P-CONTACT-RECORD-1 zůstává samostatným kontraktem i samostatným přezkumem.

## Předmět a pevné důkazní závislosti

Předmětem je celý [PROOF V100-JOIN-1](https://github.com/mathorn1973/twist-j/blob/af25e9b9717c27a05bd29e19f857e5a4ed301a4b/notes/residual-record-composition-review-1/PROOF.md), předložený v [PR #1390](https://github.com/mathorn1973/twist-j/pull/1390). Jeho SHA-256 je `7736730cc186669859f0d714e2790fea8a461129c7fbaf922a024eb90149273a`; surový Git blob `814cccda758e90aa8cc94b9f3bf3fadccff8020b` se shoduje s místní přezkoumávanou kopií. Commit je identifikací předlohy, nikoli přijatým formálním pinem.

| Závislost | Přesná verze a použitý obsah |
|---|---|
| Veřejný základ | [Public Canon v99](https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md), commit `68080edc12faf029de48181f0a384f66e42dbc04`: původní nosič, mapy, pístové čtení a pevná reziduální data. |
| P-CONTACT-RECORD-1 | [Původní PROOF](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PROOF.md), SHA-256 `805137842d66894b36cc5cef17b45bf1c67b81570bf9eb8a4c77c9394d40abf5`: úplný K_i pro libovolné q,r, involutivní Ucal_i, ready identita a univerzální listová ochrana r_x² ve druhé čtečce. |
| P-ALG-CONTACT-REALIZATION-1 | [SPEC CW-ALG-1](https://github.com/mathorn1973/twist-j/blob/13081b0dec64ab99386a8cd06759b152e3e05636/notes/alg-contact-realization-review-1/SPEC.md), SHA-256 `bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656`: konkrétní Pi_alg, atlas a aktivní doména, konečný konstrukční překlad se zmrazenou předností maker, úplné zvednutí a inverze téhož slova. |

Kontaktní závislost prošla odděleným statickým odvozením jejího původního omezeného L1 kontraktu. Tento spojovací posudek ji nerozšiřuje o reziduální krok ani nemění její preregistraci. U algebraické závislosti se zde kontroluje správnost použití jejích přesných závěrů; tento záznam nenahrazuje samostatný přezkum univerzality kompilátoru. Algebraický atlas sám není povolenou nativní branou. Konečné nativní slovo je dodáno právě konstrukčním důkazem CW-ALG-1, nikoli referenční implementací atlasu nebo budoucím PASS její enumerace.

Historické odkazy určují matematický základ. Neosvědčují aktuální stav veřejné autority, přijetí závislostí ani povolení dalšího běhu; to vyžaduje samostatnou aktuální procedurální kontrolu.

## Úplné mapy a skutečné faktorové klíče

Úplný nosič obsahuje osm pístových souřadnic, dvě q, dvě r a jeden bit: `X=F5^12 × {0,1}`, tedy 488281250 stavů. Faktor f zapomíná právě q. Tvrzení o faktorovém působení nativního kompilátoru se správně nepřenáší na čtečky Ucal, které q do r skutečně čtou.

Z úplného kontaktního kontraktu a involutivity každého P_q plyne pro d=delta(Gp) na celém X

\[
\mathcal A_i:(q_i,r_i)\longmapsto
(q_i+3d,P_{q_i+3d}P_{q_i}(r_i)).
\]

První Ucal může vytvořit libovolnou obsazenou referenci; K_i je již dokázán pro takový vstup. Proto tu není skrytý předpoklad r_i=0 uprostřed slova. Ostatní souřadnice se na konci obnovují a d nezávisí na r,q,eta.

Algebraická závislost dává na celém faktoru `Pi_alg(p,r,eta)=(R(p,eta),r)`, kde R na r nezávisí. Stejná vlastnost nebyla bez důkazu připsána původní lexikografické Pi. U přesného překladu je úplná mapa

\[
T_{\rm alg}(f,q)=(\Pi_{\rm alg}f,H_fq),\qquad H_f\in GL_2(F5).
\]

H_f je funkce skutečného vstupního faktoru a pevného slova. Gramatika, přednost maker, syntaktické mocniny a reverzní inverze určují jeden konkrétní lift; faktorově shodná slova nejsou automaticky shodná na q. Nikde ve spojovacím důkazu není potřeba H_f=I.

V rovnici (4) je správný klíč **f_x po prvním A_x**, tedy včetně `rhat_x=P_(q_x+3d0)P_(q_x)(r_x)`. Pro obecný obsazený vstup může tento faktor záviset na původním q. Není proto odvozeno, že V na každém pevném původním faktoru působí afinně v q. Rovnice (4) místo toho skládá skutečné úplné mapy v pořadí A_x, T_alg, A_y a používá přesně skutečný výstup v_y pro druhou čtečku. To je dostačující a správné i pro obsazené r a oba bity.

## Hlavní připravený krok a úplná inverze

Na S0 jsou r_x=r_y=eta=0 a zbývajících deset souřadnic je libovolných. Počet `5^10=9765625` je tedy správný. Bodová tabulková identita `P_(q+3d)P_q(0)=d` pro d=0,1 dává po A_x přesně r_x=delta(g), r_y=0 a eta=0. Tento stav patří do aktivní domény algebraického svědka pro všechny písty; první již obsazený záznam není překážkou, neboť Pi_alg obnovuje obě r globálně.

Po T_alg je Gram Mg a první záznam zůstává delta(g). A_y začíná se skutečně připraveným r_y=0, proto pro libovolné skutečné v_y zapíše delta(Mg). Tak je na jedné a téže úplné trajektorii dokázána celá rovnice (5). Z matice M plyne prostřední složka Mg rovna `4(alpha+beta+gamma)`; protože 4^4=1 v F5, uvedená formule pro delta(Mg) je správná. Přímým násobením mají obě strany `B_read M=L5 B_read` řádky `(1,0,2)`, `(0,0,3)`, `(1,2,3)`. Tato pevná identita převádí Gramový krok na již zvolené čtení D_C, bez dodatečné volby matice podle výstupu.

Inverze čtečky je skutečná dvoustranná inverze: nejprve q_i=q_i'−3d, potom `r_i=P_(q_i'−3d)P_(q_i')(r_i')`. Po dosazení se stejné involuce P ruší ve správném pořadí. Výstupní písty čtečky dovolují určit stejné d jako na vstupu.

Úplnou inverzi V jsem navíc zkontroloval v jejím skutečném pořadí. Z výstupu nejprve podle výstupního Gramu zrušíme A_y a obnovíme jeho vstupní q i r_y. Z takto získaného faktorového výstupu f2 obnovíme `f_x=Pi_alg^-1(f2)`. Teprve tento faktor určuje správnou matici H_(f_x), jejíž inverzí obnovíme u. Nakonec zrušíme A_x podle Gramu obnovených pístů. Tím se vracejí všechny původní souřadnice; žádný q klíč se nevyhodnocuje v nesprávném bodě. Inverze T je ReverseInvert **téhož** kompilovaného slova, nikoli nezávislá kompilace faktorové inverze.

## Přesné S1 a ekvivalence s návratem do S0

U nenulového Gramu atlas ukládá `ell=j+m(kappa(g)) eta`. Aktivní část ponechává ell, L,n a r a mění g na Mg. Pro aktivní výstup s Gramem g′ má tedy předobraz šířku `m_prev=m(kappa(M^-1 g′))`; jeho vstupní bit je0 právě tehdy, když `ell′<m_prev`.

Tuto ekvivalenci jsem zkontroloval i mimo aktivní část, aby podmínka (10) nebyla pouze implikací na předem vybrané doméně. U neaktivního nenulového výstupu je `ell′>=m_*(g′)`. Každý platný slot s eta′=0 má ell′=j′ menší než aktuální šířka, která nepřevyšuje m_*. Neaktivní bod tedy má eta′=1 a R^-1 jej fixuje. Současně `m_prev<=m_*`, takže nerovnost (10) je nepravdivá. Ekvivalence platí i tam. Na nulovém Gramu R fixuje celý bod a vstupní bit je0 právě při eta′=0.

Zbývají obě reference. Pro každý q a d je mapa r↦P_(q+3d)P_q(r) bijektivní a zobrazuje0 právě na d. Její inverze tedy obnovuje0 **právě tehdy**, když výstupní r=d. Proto z podmínek (9) druhá inverzní čtečka obnoví r_y=0. Slotová podmínka obnoví eta=0 a předchozí Gram M^-1g′. Protože T nechává obě r beze změny, první inverzní čtečka obnoví r_x=0 právě z `r_x′=delta(M^-1g′)`. To dokazuje současně nutnost i postačitelnost přesných podmínek S1 na celém X.

Volnost q′ v S1 neplyne z neodůvodněné afinnosti obecného V. Na připraveném vstupu však první zápis dává r_x=delta(g) **nezávisle na q**, takže pro každý původní p je faktor `f_x=(p,delta(g),0,0)` pevný. Příslušná úplná mapa q má proto tvar

\[
q' = H_{f_x}(q+3\delta(g)e_x)+3\delta(Mg)e_y,
\]

což je bijekce F5². Inverzní R zároveň dává jediný původní p při splněné slotové podmínce. Proto je každé uvedené q′ přípustné a má právě jeden předobraz v S0. Údaj `|S1|=9765625` i přesná mezilehlá rozhraní v oddílu5 jsou oprávněné; nezůstává žádná dodatečná skrytá podmínka na q.

## Tři různé domény a pokračování dynamiky

Podle atlasové závislosti je maximální šířka nenulové M-orbity5 na nenulové přímce s(2,1,3), jinak6. Každá aktivní orbita pevného slotu ell<m_* navštíví Gram s maximální šířkou, kde tentýž slot má eta=0. Naopak neaktivní nenulové body a nulové body s eta=1 nelze z eta=0 dosáhnout, neboť je Pi_alg fixuje. To pro faktor dokazuje přesný T-dosah uvedený v (7). Protože počáteční q vlákna jsou celá a každé H_f je bijekce, faktorový argument skutečně platí i na úplném nosiči. Obě r se na konci T nemění.

Zkontroloval jsem také účtování velikostí z přesných atlasových počtů závislosti. Nulových pístových párů je6625; nenulová aktivní část má740 redukovaných stavů a každý má `|SL2(F5)|·5=600` realizací L,n. Pístová/bitová část Omega má tedy `6625+740·600=450625` stavů. Pro libovolná r,q dostáváme `450625·25·25=281640625`. Pro samotné T ze S0 jsou r pevně nulové, a proto velikost je `450625·25=11265625`. Jde o odvození počtů z atlasové věty, nikoli o tvrzení, že byly právě enumerovány všechny tyto stavy.

Obě A_i i jejich inverze ponechávají písty a bit na konci beze změny; membership v Omega na q,r nezávisí. Proto obě čtečky zachovávají Omega v obou směrech, stejně jako T. Na této invariantní doméně každý úplný V mění Gram právě pomocí M. Indukce tedy správně dává rovnici (8), včetně n=0, bez opětovné přípravy eta.

Omega není zaměněna za přesný opakovaný dosah V ze S0. Čtečkové koncové permutace zachovávají množinu `{0,1,2}` a T obnovuje r. Dokončené V kroky proto z připravených referencí nikdy nedosáhnou3 nebo4, zatímco Omega je připouští. Skutečný dosah je správně ponechán jako `union_(n>=0) V^n(S0)`; jeho velikost nebo rovnost s jinou uzavřenou formulí se netvrdí. Omezení makrokonců zároveň neomezuje povolené mezistavy nativních listů: celý nosič X zůstává potřeba.

## Obnova záznamu, prefixy a jednorázovost

První záznam se po T obnovuje v syrové souřadnici r_x, protože globální koncová identita r_x T=r_x platí i pro obsazený registr. To přímo dává (11), neboť delta je0 nebo1. Tvrzení se nevztahuje na každý vnitřní list obrovského T; důkaz zde správně nevyrábí prefixový invariant z pouhé koncové identity.

Použití kontaktní prefixové ochrany v (12) je oprávněné i po T. V samostatném kontaktním důkazu je ochrana odvozena listově na **každém úplném vstupu**: každý list druhé čtečky r_x buď fixuje, nebo neguje. Nevyžaduje připravený bit, původní písty, nulové q, neobsazené r ani stejnou hodnotu delta jako v prvním zápisu. Platí tedy pro skutečný stav T A_x z, i když T změnilo písty a bit. Indukce přes všechny prefixy A_y včetně prázdného dává konstantní r_x²=delta(g). Tím se přesně odděluje obnova po T a ochrana během následné čtečky.

Základní tabulková ready identita je použita pouze při počátečním r_x=0 a při dosud nepoužitém r_y=0. Při opakování V mohou být reference obsazené a jejich obecná mapa není novým nastavením na delta. Rovnice (8) proto správně tvrdí pokračování čtené reziduální dynamiky, nikoli čerstvý pár záznamů při každém kroku. Inverze odstraní také záznamy; nedává restart se zachovaným archivem. Nulový záznam zůstává nerozlišitelný od nepoužitého nulového experimentu bez dalšího údaje o dokončení.

Celý argument používá jen jedinou počáteční přípravu. Symboly atlasu, mezifaktorů a H jsou matematickými popisy existujících souřadnic a pevného slova, nikoli novými uloženými registry, resetem, čítačem nebo adaptivní volbou brány. W_a,W_b a Ucal_i zůstávají výslovnými architekturními předpoklady. Věta neodvozuje jejich fyzickou realizaci ani dostupnost z původního autonomního U.

## Dispozice a veřejná hranice

Doporučuji přijmout **existující spojovací důkaz V100-JOIN-1 bez změny jeho rozsahu**, po samostatném přijetí potřebných přesných kontaktních a algebraických závěrů. V rámci těchto premis nebyla nalezena první matematická překážka společného složení. Zkontrolované závěry jsou úplná mapa a inverze, přesný krok a dvojice jednorázových záznamů na S0, charakterizace S1 pomocí úplné inverze, správné rozlišení dosažitelných domén a obnova prvního záznamu po T s následnou omezenou prefixovou ochranou.

Tento posudek nedokládá provedení kompilovaného slova, výsledek budoucího verifieru, veřejné přijetí písemných důkazů ani splnění aktuálních pinů a běhových bran. Přijetí verifieru, přijetí věty a veřejné začlenění jsou odlišné události. Před společným v100 musí mít každá požadovaná sonda vlastní přijatý rozsah, neměnný formální pin, skutečnou předepsanou evidenci a přezkum podle aktuálního repozitáře; potom teprve následuje společné začlenění. Tento samostatný přezkumný záznam nemění Canon, kontaktní kontrakt, stav otevřených vlastníků ani fyzické závěry.
