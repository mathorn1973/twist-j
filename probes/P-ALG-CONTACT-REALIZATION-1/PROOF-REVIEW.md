# Nezávislý statický přezkum důkazu Pi_alg a CW-ALG-1

**NON-CANONICAL. Dispozice přezkumu: PŘIJMOUT v níže vymezeném podmíněném rozsahu L1.**

Datum: 2026-10-06. Přezkum provedla samostatná kontrolní větev
`record_audit`, která není autorem `SPEC.md`. Předmětem je celý psaný
matematický důkaz ve [SPEC.md](SPEC.md), nikoli pouze přijetí verifieru.
Přezkoumané bajty mají SHA-256
`bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656`.
Jakákoli změna tohoto souboru vyžaduje nové posouzení změny.

Přezkum je přímé čtení definic a algebraických identit. Nebyl spuštěn ani
importován verifier, jeho jednotlivá funkce, vědecká enumerace nebo nativní
expanze. Níže uvedené počty jsou posouzené důsledky uvedených vzorců,
nikoli výsledky nového běhu. Přijetí znamená kladnou dispozici tohoto
přezkumu; není přijatým veřejným pinem, veřejným výsledkem, zápisem do
registru ani změnou statusu Canonu.

## 1. Přijaté tvrzení a jeho podmínky

Na úplném nosiči `X=F5^12×{0,1}` se přijímá následující podmíněné tvrzení:
při doslovných nativních mapách a obou branách `W_a,W_b` uvedených ve
SPEC, bez změny jejich řídicího čtení, určuje verze `CW-ALG-1` jedno konečné
nativní slovo

\[
T=\operatorname{Expand}(\mathrm{CW\!\!\!-ALG\!\!\!-1}(\Pi_{\rm alg}))
\]

s `rho T=Pi_alg rho`, kde `rho` zapomíná právě obě `q`. Na všech vstupních
stavech se obě `r` na konci slova přesně obnoví. Úplné působení má tvar

\[
T(f,q)=(\Pi_{\rm alg}f,H_T(f)q),\qquad H_T(f)\in GL_2(\mathbb F_5),
\]

přičemž konkrétní `H_T` určuje tatáž pevná syntaxe. Na přesně popsaném
`Omega_alg` je `G T=M G`, a tedy `D_C T=L5 D_C`. Úplnou inverzí je
`ReverseInvert(T)`. Nevyžaduje se příprava `q`, čisté pracovní `r`, další
registr ani reset bitu.

Jde o realizovatelnost konečným slovem v přijaté matematické abecedě L1.
Přezkum nedokazuje fyzické zavedení `W_a,W_b`, realizaci detektoru,
praktickou cenu, dostupnou délku expanze ani přenos do jiné protokolové
vrstvy. `Ucal_i` a samostatný kontakt nejsou předpokladem tohoto
algebraického důkazu. Spojovací věta o `A_y T A_x` se posuzuje zvlášť.
`Pi_alg` je výslovně jiná permutace než původní lexikografická `Pi`.

## 2. Zdrojové mapy, uzavřený faktor a primitivita

Walshova matice má inverzi `4 W^T`. Z její tabulky vychází determinantová
forma `4(st-uv)`; polarizace má přesně uvedenou regulární matici `K`.
Přímé násobení obou stran `B_read M=L5 B_read` dává řádky
`(1,0,2),(0,0,3),(1,2,3)` a `det B_read=1`. Uvedený vzorec `M^-1`
se složí s `M` z obou stran na identitu. Cílový krok čtení proto
nepotřebuje jinou matici nebo dodatečný výběr dekodéru.
Párové `A=(a,a)` a `B=(b,b)` jsou komutující involuce a mění `h` na `-h`.
Ve vzorci `W_i` proto druhé použití vrátí data i původní bit: je-li
`s=sigma(h)` a `k=s xor eta`, po první aplikaci má nové čtení orientaci
`s xor k=eta`, takže druhá aplikace použije opět `k`. Nulová větev je
identita. Tento argument zahrnuje oba vstupní bity a všechna `q,r`.

Žádné `q` neovlivňuje ponechané souřadnice nebo větev `W`; faktor
`F=F5^10×{0,1}`, velikosti `N=19531250`, je tedy uzavřený. Jeho tvrzená
minimalita rovněž platí: odlišný bit rozliší prázdné slovo; odlišný píst
rozliší translace a regularita `K`; rozdíl pouze v `r` vystaví `c` jako
nenulový pístový rozdíl a následná translace jej rozliší. Potřebné
translace jsou níže skutečně sestrojeny, takže zde není kruhový odkaz na
primitivitu nebo na cílové `M`.

Přezkoumány jsou oba případy klasifikace bloků invariantních vůči
translacím. V jedné vrstvě je blok koset svého translačního stabilizátoru,
což je podprostor nad `F5`. Protíná-li blok obě vrstvy, druhý průnik je
jediný koset téhož stabilizátoru. To dává právě dvě podoby v oddílu 5.1.

V odděleném případě mají obě bitové funkce `f_eta(h)` prostor period
právě `rad(h)=<r_x,r_y>`. Je-li `h(v)≠0`, hodnoty na přímce `t v`
zahrnují `0,h(v),-h(v)`, na nichž funkce není konstantní. Je-li
`h(v)=0`, ale polarizace s `v` není nulová, vhodná přímka `z+t v`
projede všech pět hodnot `h`. Jen radikál proto může obsahovat blokový
podprostor. Lineární část `c_x`, resp. `c_y`, převádí příslušnou
nenulovou složku `r` také do pístu, takže invariantní podprostor v
radikálu je nulový.

Ve spojeném případě dává `P` rozdíl `(0,d_x)` a invariance vůči `Q_cs`
také `(d_x,0)`; analogicky vzniknou `(d_y,0),(0,d_y)`. Tedy `d∈H` a
posun mezi vrstvami se vypustí. Obrazy dvojice `(z,0),(z,1)` pod `W_i`
vynutí `(A-I)z,(B-I)z∈H` pro `h(z)≠0`. Tyto aktivní vektory generují
celé `D`: pro libovolné `w` nenulový polynom `h(v+t w)` stupně nejvýše
dvě nemůže zmizet ve všech čtyřech nenulových `t`. Obrazy `A-I,B-I`
proto dodají všechny osy `S,U,T,R`; aplikace lineární části `c` na `r`
dodá zbývající `V`. Je tedy `H=D`. Translace jsou tranzitivní v každé
vrstvě a `W_a` vrstvy propojí. Důkaz primitivity je úplný a nepoužívá cíl.

## 3. Kontrola A1–A12: translace a atomy

Ve všech následujících identitách se součiny čtou zprava doleva a
komutátor je `FGF^-1G^-1`.

| Krok | Přezkoumaná identita a její rozsah |
|---|---|
| A1 | Pro afinní involuci `g(z)=Lz+t`, kde `L²=I,Lt=-t`, přímá kompozice `D_g P^-1 D_g P` dává `(x,y)→(x,y+t)`. Vektory `t_c=(1,0,2,0,0)` a `t_d=(0,1,0,2,1)` spolu s jejich obrazy pod `a,b` dávají uvedenými koeficienty postupně přesně `e_s,e_u,e_t,e_r,e_v`. |
| A2 | `Q_cs Y_j Q_cs^-1 Y_j^-1` posune první buňku o `e_j` a druhou obnoví. Pevné pořadí deseti translací a reprezentanti koeficientů proto určují každé `tau_v`. |
| A3 | Na `h≠0` je `W_i I_i W_i` pouze převrácením bitu; na `h=0` je `I_i`. Součin obou maker je tedy `AB` právě na nulové větvi a jinak identita. |
| A4 | `r` neovlivňuje `h`; `AB` je na `r` negace. Samotný komutátor s `tau_e_r` přičte na nulové větvi `-2`, druhá mocnina přičte `-4=1`; mimo ni je identita. Všechny ostatní faktorové souřadnice se obnoví. |
| A5 | `tau_-v U tau_v U^-1` dává rozdíl `f(z+v)-f(z)`, protože cíl `r` není řídicí proměnnou. |
| A6 | Posun v opačném pístu `K^-1 ell` přidá do `h` právě `chi` a samotné `chi` zachová. Čtyři diference `1-h^4` jsou `-4! chi^4=chi^4`. Platí pro kteroukoli z osmi Walshových pístových souřadnic a oba cíle `r`. |
| A7 | Tři uvedené diference jsou `4chi+1`, `2chi²+4chi+4`, `4chi³+chi²+4chi+1`. Následné odčítání a násobení koeficienty `4,3,4` izoluje přesně mocniny `chi,chi²,chi³`. |
| A8 | `H_0` je `(v_x,t_x)→(v_x-2r_x,t_x+2r_x)`. Konjugovaná kombinace s `a_x` přičte do `v_x` `-4r_x=r_x` a změny `t_x` se vyruší. |
| A9 | Komutátor před vnější inverzí přičítá do `v_x` `-r_y`; doslovná inverze proto dává `N23=E_2(xi_3)`. |
| A10 | Tři střihy dávají právě `(xi_1,xi_2)→(-xi_2,xi_1)` a `(xi_2,xi_3)→(-xi_3,xi_2)`. Ostatní faktorové souřadnice se vrátí. |
| A11 | Konjugace atomu má koeficient `epsilon_i epsilon_j^k`; umocnění stejným znaménkem jej opraví na 1. Exponent `-1` je syntaktická inverze. Čtverce obou čtvrtotáček generují změny znamének dvojic os a jejich permutační obrazy generují `S3`, tedy všech 24 podepsaných permutací determinantu 1. Jednoduchá cesta v jejich Cayleyově grafu má délku nejvýše 23. |
| A12 | Vnější `chi` se pod `J12` nemění a `J12 e_1=e_2`; konjugace tedy realizuje požadovaný atom do cíle 2 bez dalšího znaménka. |

Tyto jsou faktorové identity. Nepředpokládají, že celé příslušné slovo
fixuje nenulové `q`; úplné chování `q` zůstává určeno syntakticky.

## 4. Kontrola A13–A18: řízení a izolovaný třícyklus

Pro libovolné vstupní `u=xi_i,v=xi_j` a hodnoty kontrol `f,g`, nezávislých
na obou pracovních osách, dává A13 přímo

\[
[E_i(g),E_j(u^2)]:\quad v\mapsto v-2ug+g^2.
\]

Odečtením varianty s `-g` vzniká `v→v-4ug=v+ug`. Komutátor s
`E_i(f)` pak odečte `fg`; vnější inverze v A14 jej tedy přičte. Osa `i`
se obnoví pro libovolný obsazený vstup. A15 správně konjuguje kontrolu
na `(chi-c)^4`, takže po odečtení od konstanty 1 vznikne indikátor.

U všech tří řádků A16 jsou kontrolní proměnné mimo uvedenou dvojici
cíl/pomocná osa. Rekurze A14 používá doslovně levý prefix a poslední
indikátor; obě podvolání mají menší počet indikátorů, vnořené prohození
pracovních os nezmění nezávislost kontrol. Základ tvoří již definované
atomy. Zde se nepředpokládá čistá pomocná osa.

Orientace malých cyklů byla ověřena přímo. V rovině `(xi_1,xi_3)`
komutátor vodorovného a svislého podmíněného posunu posílá
`O→E→N_0→O` a ostatní body fixuje. Pro `xi_2=0` je další komutátor
součinem `(O,E,N_0)(E,E+N_0,2E)`, a tedy
`Psi=(O,E,E+N_0,2E,N_0)`. Mimo určené kontroly jsou obě strany identity.

Walshův vstup v A16 s `xi_2=0` odpovídá přesně pístům
`p_x=(3,0,3,0),p_y=(4,1,1,4)` a má `h=2`. Posunutá podpora druhého
pěticyklu je `{2E,3E,3E+N_0,4E,2E+N_0}`. `W_a` ponechá její bit-0
část a bit-1 část přesune na odlišné písty `A p` v bitu 0. Odlišnost
plyne již z `u_x=1`. Průnik s podporou `Psi` je tedy jediný faktorový
stav `(p,2E,0)`.

Pro permutace `F,G` s jediným společným bodem podpory `z` posílá
`[F,G]` postupně `z→Fz→Gz→z`; doplněk těchto tří bodů fixuje. Zde jsou
obrazy `Psi(2E)=N_0`, `Psi'(2E)=3E`. A18 tedy dává přesně orientovaný
`C_*=(zeta_0,zeta_1,zeta_2)` z oddílu 5.2, s jedinou bitovou kopií.
Tvrzení o tříbodové podpoře se týká faktoru, nikoli podpory úplného
slova na `X`: na zapomenutých `q` může slovo působit i nad jinými body.
Tento rozdíl nebrání dalším faktorovým konjugacím.

## 5. Hypergraf a kontrola B1–B7 pro obecný konečný nosič

Makroabeceda B1 má stejné faktorové působení jako původní abeceda,
obsahuje inverze a má pevné syntaktické pořadí. Homogenizace neodstraňuje
duplicitní řetězce. Hrany B2 jsou skutečné konjugace již sestrojeného
třícyklu, se správnou orientací obrazů všech tří bodů.

Konečná mez hypergrafu je doložena bez odvolání na enumeraci. Označíme-li
komponentní rozklad do délky `k` jako `P_k`, pak `P_k=P_(k+1)` znamená,
že každý generátor pošle každou komponentu do jedné komponenty: obrazy
všech jejích hran mají délku nejvýše `k+1`. Stejná inkluze pro inverzi
ukazuje, že jde o rovnost komponent, nikoli jen o zobrazení do menší
části. Rozklad je invariantní systém bloků. Primitivita a již existující
tříbodová hrana vylučují diskrétní rozklad; zbývá jediná komponenta.
Dokud není souvislý, počet komponent proto v každém kroku přísně klesá.
Začíná na `N-2`, takže uvedená mez `N` je postačující konečná mez.

Kontrola univerzálních permutačních identit a připojování:

| Krok | Přezkoumaný obecný důvod |
|---|---|
| B3 | Inverze `S_j`, cyklický přepis `S_i` a konjugace `S_j S_i^-1 S_j^-1` dávají ve všech třech uvedených případech přesně `(b,i,j)`. |
| B4 | `(b,i,j)(b,j,k)` fixuje `b` a dává `(i,j,k)`. Kanonický rozklad cyklu do transpozic respektuje působení zprava doleva. Shodný pár se ruší; sdílený pár `(p s)(s q)` je `(p s q)`; disjunktní pár je přesně uvedený součin dvou třícyklů. V sudé permutaci je počet transpozic sudý. |
| B5 | Rozšíření `p→a,q→b` je určeno vzestupným přiřazením. Při alespoň čtyřech starých bodech postkompozice transpozicí mimo `a,b` opraví paritu a oba obrazy zachová. Při třech bodech záměna `p,q` obrátí paritu; současná inverze hrany zachová požadovanou orientaci výsledné hvězdy. Konjugace tak vždy dává `(a,b,x)`. |
| B6 | Podpory `(p,q,r)` a `(p,x,y)` se protínají pouze v `p`; právě ověřené pravidlo komutátoru dává `(p,q,x)`. Po připojení `x` má původní hrana dva staré body a připojí `y`. |
| B7 | Každý řádný neprázdný `U` protíná v souvislém hypergrafu nějaká hrana s doplňkem. Každý netriviální krok přidá alespoň jeden bod, takže přesně `N-3` konstrukčních kroků včetně případných nečinných koncových kroků stačí. Indukce zachová všechny staré hvězdy a vyrobí nové. `Even_F(g)` potom dává každou sudou permutaci. |

Jde o důkaz pro obecný zde definovaný konečný nosič; úspěch tabulek na
malém počtu symbolů by sám nenahrazoval primitivitu, souvislost ani tuto
indukci. Podpora slov a tvrzení o fixovaném doplňku jsou opět faktorová.

Opačná grupová inkluze je správná: původní faktorové listy mají dvě
stejné bitové kopie, a jsou tedy sudé. Aktivních dat pro `W_i` je
`25(5^4-1)·4·5^3=7800000`; involuce `I_i` nemá v aktivních datech pevný
bod, protože mění nenulové `h` na `-h`. Na každou dvojici dat připadá
jedna transpozice na bitových stavech, celkem `3900000`. Také `W_i` je
sudá. Spolu s konstrukcí je tedy skutečně `Gamma=Alt(F)`.

## 6. Atlas, Pi_alg, parita a přesný dosah

Pro nenulové `g` má polynom `alpha+2t beta+t² gamma` alespoň jednu
nenulovou hodnotu mezi třemi předepsanými `t`. Volba prvního takového
`t` je jednoznačná. Z definice `L=(X+tY)D_a^-1` plyne `det L=1`.
Polarizace po převodu přes `L` dává `a Z11+Z22=2b`, takže vzorce pro
`xi,lambda,mu` dávají `xi²+lambda mu=kappa`.

U uvedené inverze je `det Z=(b²-kappa)/a=gamma` a polarizace `D_a,Z`
je `b`. Proto obnovené `Y=LZ,X=LD_a-tY` mají přesně původní
`alpha,beta,gamma`; znovuzvolení kanonického chartu vrátí stejný `t`.
Atlas je bijekce, nikoli pouze kódování reprezentantů vláken.
Pro `lambda≠0` je dekódování dělením `lambda` jednoznačné; pro
`lambda=0` zbývají právě kořeny `kappa`. Rozdělení kořenů do pozic 4 a 5
dává přesné šířky `5,6,4` a všechny jejich inverze.

Orbitové tvrzení je doloženo přímo nilpotentním tvarem v uvedené bázi
`e,v,w`. Pro `N=M+I` je `Ne=0,Nv=e,Nw=v`; dosazení dává
`kappa(Ae+Bv+Cw)=B²+3AC-C²` a
`kappa(M^k g)=kappa(g)+k C²`. Při `C≠0` se projdou všechny hodnoty
`kappa`; při `C=0,B≠0` je šířka 6; při nenulovém `Ae` je šířka 5 a
`Mg=-g`. To dokazuje přesně uvedené `m_*`, bez orbitového vyhledávání.

Na aktivní větvi se zachová celé číslo `ell=j+m eta`. Je `ell<m_*≤6`
a nová šířka je alespoň 4, takže rozklad na nový `j,eta` je vždy platný.
`m_*` je invariantní po orbitě; `M^-1` se stejným `ell` je proto
oboustrannou inverzí této větve. Neaktivní doplněk je od ní disjunktní
a je fixován. Nulový Gram je fixován pro oba bity. Obě `r` se ve všech
větvích doslovně zachovají.

Pro každé označení `(L,n,r_x,r_y)` je táž redukovaná permutace;
takových označení je `120·5·25=15000`, sudý počet. `Pi_alg` je proto
sudá bez předpokladu o paritě malé permutace. To je potřebný most k B7.

Kontrolované počty mají úplné analytické odvození. `M^5=-I,M^10=I` a
`M²-I=N(N-2I)`; nenulové body periody 2 jsou právě čtyři body osy `e`,
ostatních 120 má periodu 10. Aktivní redukce má tedy `4·5+120·6=740`
stavů, deset dvoucyklů a 72 deseticyklů. Nulový Gram má
`145+144·45=6625` pístových dvojic: počet singularních matic je
`625-|GL_2(F5)|=145`; pro nenulový rank-1 `X` normalizace na
`diag(1,0)` dává `Y22=0,Y12Y21=0`, tedy 45 možností. Atlas má 600
pístových označení pro každý `(g,j)`, takže připravená nenulová redukce
má `(5^8-6625)/600=640` stavů a s bitem 1280; z nich je 540 fixovaných.

Přesný dosažitelný uzávěr z celé vrstvy `eta=0` je

\[
\Omega_{\rm alg}=\rho^{-1}\bigl(\{G=0,\eta=0\}\cup
\{G\ne0,\ j+m(\kappa(G))\eta<m_*(G)\}\bigr).
\]

Každý aktivní cyklus navštíví maximální šířku, kde je jeho zachovaný
slot v bitu 0; neaktivní slot nikdy nezačíná v bitu 0. To dokazuje oba
směry dosažitelnosti. Faktorová velikost je
`6625·25+740·15000=11265625`, po zahrnutí všech `q` pak `281640625`.
Celá počáteční `q` vlákna jsou bijektivně přenášena, a proto jde skutečně
o úplný pullback, i když `H_T` není identita. Při počátečním
`r_x=r_y=eta=0` je uzávěr samotného `T` přesně průnik s oběma `r=0`,
velikosti `11265625` na `X`. Toto není tvrzení o uzávěru složení s
čtečkami. Vně `Omega_alg` je fixován faktor; úplná mapa `q` tam nemusí
být identita.

## 7. Konečnost syntaxe a úplný q lift

Homogenizace v (11) končí na doslovných nativních listech. `e_i d_i`
je `q_i→q_i+1` a faktor fixuje; uvedené bar-makro má proto `q_i→-q_i`
a stejný faktor jako původní list. Jsou to úplné involuce. Atomy A6/A7
mají přednost před A11 a dvě zvláštní definice N21/N23 mají přednost
před svými obecnými aliasy. Nedochází k cyklické definici. A15/A16
snižují počet indikátorů; malé a velké seznamy mají meze 23 a N; B7
má pevný počet kroků. Všechny volby mají předepsané pořadí a orientaci.
Záporné exponenty se zachovají jako inverze, nikoli jako faktorově
ekvivalentní čtyři kopie.

Žádný krok tedy nevolá neomezený vyhledávač slova pro cíl. Seznamy,
permutace a jejich rozklady určují konečné zapojení při konstrukci;
nejsou dalšími souřadnicemi stroje. Existence konečné definice není
tvrzením o proveditelné ceně její úplné expanze.

Z úplných listových map plyne trojúhelníkový tvar
`(f,q)→(F_w(f),H_w(f)q+t_w(f))`, protože faktorová trajektorie je
nezávislá na `q`. Všechny listové matice jsou invertibilní. Kompoziční
vzorce SPEC vzniknou dosazením afinních map, včetně vyhodnocení
`H_U` na mezistavu `F_V(f)`; inverzní vzorec nejprve obnoví `f`.
Homogenní makroabeceda má nulové `t`, a proto je na hranici celého
`T` nulové také `t_T`. Neznámé `q` se nepřipravuje ani nemaže.

Tím je přijato obecné tvrzení `H_T(f)∈GL_2(F5)` i to, že jeden
konkrétní `H_T` určuje přesně zvolená syntaxe. Jeho hodnoty nejsou
numericky předloženy ani zaměněny za `I`. Syntaktická reverze invertuje
úplné slovo; zvláštní kompilace `Pi_alg^-1` by mohla mít jiný q lift a
nelze ji bez důkazu použít místo této inverze. Stejně tak z faktorové
periody 10 neplyne `T^10=I` na úplném nosiči.

## 8. Dispozice a zbývající podmínky

V přezkoumaných bajtech nebyla nalezena matematická překážka tvrzení
vymezeného v oddílu 1. Obecný důkaz primitivity, A1–A18, konečné
souvislosti a B1–B7, bijektivity a parity atlasu, přesného dosahu a
úplného syntaktického liftu se **přijímá v podmíněném rozsahu L1**.
Tato dispozice se neopírá o případný úspěch omezeného verifieru a
nezvyšuje vědecký status změnou označení.

Pro veřejnou formální sondu zůstávají samostatně nutné aktuální
repozitářová autorita, přijetí a neměnné veřejné připnutí úplného
kontraktu/verifieru/vstupů, řádně zaznamenané běhy a architekturní
evidence podle tehdy platných pravidel. Tento přezkum žádný z těchto
kroků neoznamuje jako vykonaný. Pro společné v100 navíc zůstává oddělené
přijetí nezměněného `P-CONTACT-RECORD-1` a spojovací věty o `V`.
Ani samostatné přijetí tohoto důkazu není společným začleněním v100.
