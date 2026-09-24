# Fotonová větev: přímý odhad b − 25χ a přesné odečtení malých složek

- **Working item:** C-PHOTON-BCHI-DIRECT-BOUND-N
- **Owner issue:** #1143
- **Author:** A. M. Thorn
- **Date:** 22 September 2026
- **Scope:** PUBLIC, NON-CANONICAL; no authority
- **Scientific ceiling:** candidate-T for the written analytical consequences; no phase promotion.

Pracovní matematický rozbor po samostatném agentním přezkumu. Níže uvedené věty mají napsaný důkaz; přezkum není formální přijímací postup ani dvouarchitekturní vědecké ověření. Nejde o formální sondu, změnu Canonu ani důkaz fotonové fáze.

**Výsledek:** plošné složky s omezeným průměrem dávají v infračervené limitě stejný příspěvek do \(b\) a \(25\chi\). Lze je společně odečíst. Pro jejich rozdíl navíc platí výslovná konečněobjemová mez

\[
\boxed{|\Delta_{\le R,L}(t)|\le t^2R^2(R+1)^4.}
\]

To zpřesňuje přímý útok na \(b-25\chi\): kladný rozdíl musí pocházet ze složek, jejichž průměr není omezen žádným pevným \(R\). **Vyhodnocenou kladnou dolní mez pro skutečnou váhu \(W\) tento zápis ještě nedává.**

Další práce na P1 přinesla také **novou vyhodnocenou mez pro skutečnou pevnou míru**:

\[
\boxed{Q_{\partial p}/Q_0\le1/16,}
\]

místo dosavadní záruky \(1/2\). Pro \(k\) čtyřhranových bloků a \(s\) jednotlivých hran s navzájem disjunktními plaquettovými okolími platí \(Q_j/Q_0\le2^{-(4k+s)}\). [Samostatný úplný důkaz](CURRENT-BOUND.md) obsahuje přesnou normalizaci, ostrou místní konstantu a použití v úplném modelu. Tento odhad pevných proudových sektorů ještě nedává odhad jejich vzdálenostní korelace ani vyhodnocenou \(\chi_*\).

## 1. Ověřený výchozí stav

Veřejný základ je Public Canon v91:

- `main = canon-v91 = 11b66d4755a697031157f0e10dc1898a7d5b6379`;
- obsahový commit `b89b0c80bb5cebddade567f31a979aaf42f1d9dd` je předkem `main`;
- `canon/CANON.md`: 772678 bajtů, SHA-256 `6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1`; načtené bajty souhlasí;
- opravené předání je na commitu `fbd3ac887b313732d68bfb6c6da64115482b681a` v [PR #1142](https://github.com/mathorn1973/twist-j/pull/1142), který byl při kontrole otevřený a nesloučený;
- [běh 35716224777](https://github.com/mathorn1973/twist-j/actions/runs/35716224777) má úspěšné oba architekturní běhy i souhrnný `check` pro tento commit.

Matematickými podklady jsou [rozklad podle souvislých složek #1112](https://github.com/mathorn1973/twist-j/issues/1112), [proudová Hessova matice a kritérium b–χ #1122](https://github.com/mathorn1973/twist-j/issues/1122) a [opravené předání](https://github.com/mathorn1973/twist-j/blob/fbd3ac887b313732d68bfb6c6da64115482b681a/notes/C-PHOTON-V91-LIMIT-HANDOFF-N/README.md). Načtené důkazy z veřejných Git objektů mají identifikátory `5e96b9378d29a2e68f1e03a21098b0f425a9ac80` a `b828f5906e1102c1bb550998f60dbca3a9f79cdc`.

Příbuzná [poznámka #1123](https://github.com/mathorn1973/twist-j/issues/1123) omezuje konečně zdvižené celočíselně uzavřené složky při nejnižším momentu toru a [#1124](https://github.com/mathorn1973/twist-j/issues/1124) dává podmíněné kritérium jejich směrového souhlasu. Zde zahrnujeme také vadové složky s hranicí dělitelnou pěti, odečítáme jejich společný člen a zachováváme původní uspořádanou limitu. Výsledky při nejnižším momentu nejsou důkazem této limitní identifikace.

Konstanta 243 z původního maticového důkazu #1139 se zde nepoužívá. Ani kladná místní variance, ani úspěšné kontroly repozitáře neurčují znaménko infračerveného rozdílu.

## 2. Pevná míra a veličiny

Pracujeme na izotropním periodickém čtyřrozměrném kvádrovém komplexu délky \(L\), kde \(L\) je sudé a \(V=L^4\). Používáme přesně plošné vyjádření původní váhy

\[
W(f)=2+\zeta_5^f+\zeta_5^{-f},\qquad
\mu_L(n)\propto 2^{-|\operatorname{supp}n|}
\mathbf1_{\{\partial n\equiv0\pmod5\}},
\quad n_p\in\{-1,0,1\}.
\]

Proud je \(j=\partial n/5\). Orientace stěn mají indexy \(01,02,\ldots,23\). Pro kanonicky orientované stěny se středem \(c_p\) definujeme

\[
S^L_{n,II}(q)=\frac1V\mathbb E_L
\left|\sum_{p:\operatorname{ori}(p)=I}n_p e^{-iq\cdot c_p}\right|^2.
\]

Na ose \(q=te_1\ne0\) platí přesná identita z #1112:

\[
\lambda(t)=4\sin^2(t/2),\qquad
25S^L_{j,00}(te_1)=\lambda(t)S^L_{n,01,01}(te_1),
\]
\[
\Delta_L(t)=S^L_{n,02,02}(te_1)-S^L_{n,01,01}(te_1).
\]

Všechny limitní výroky níže zachovávají pořadí původního předání: nejprve přípustný místní termodynamický limit a teprve poté \(t\to0\). Samotná místní konvergence nedokazuje bodovou konvergenci celých Fourierových hustot. U těch nadále požadujeme původní přípustný společný limitní profil; žádná nová existence ani záměna limit se nepředpokládá.

## 3. Rozklad podle průměru souvislých složek

Obsazené stěny jsou sousední, sdílejí-li hranu. Jejich souvislé složky označíme \(\Gamma(n)\). Každá složka je samostatně uzavřená modulo pět: všechny obsazené stěny u jedné hrany totiž patří do téže složky.

Zafixujme celé \(R\ge1\) a \(L>2R+4\). Za malou označíme složku, kterou lze souvisle zvednout z toru do \(\mathbb Z^4\) při zachování incidencí a jejíž středy stěn mají v tomto zdvihu průměr v normě \(\ell^\infty\) nejvýše \(R\). Složky obtáčející torus, které takový zdvih nemají, jsou velké. Kritérium je invariantní vůči posunům, záměnám souřadnic i obrácení znamének.

Položme

\[
n=n^{\le R}+n^{>R},\qquad
j^{\le R}=\partial n^{\le R}/5,\qquad
j^{>R}=\partial n^{>R}/5.
\]

Oba proudy jsou celočíselné. **Obě části jsou náhodné veličiny v jedné původní míře \(\mu_L\); netvrdíme jejich nezávislost.**

Podmíněně při daném obsazeném nosiči lze každou souvislou složku samostatně obrátit \(n^\gamma\mapsto-n^\gamma\). Tím se zachová míra, všechny podmínky modulo pět i výběr malých složek. Obě lineární veličiny rozvineme po souvislých složkách. Každý smíšený člen obsahuje jednu malou a jednu velkou složku; obrácení první z nich změní znaménko právě tohoto členu. Jeho podmíněná střední hodnota je nula. Po sečtení vymizí celá smíšená kovariance. Totéž platí pro proudy, které jsou lineárními obrazy těchto částí. Dostáváme přesné kovarianční rozklady

\[
\boxed{S_n=S_{n^{\le R}}+S_{n^{>R}},\qquad
S_j=S_{j^{\le R}}+S_{j^{>R}}.}
\]

Všechny čtyři kovariance jsou kladně semidefinitní. Wardova identita platí pro každou část zvlášť.

## 4. Věta: malá část se v rozdílu přesně vyruší

Označme

\[
A_{R,L}(t)=S^L_{n^{\le R},01,01}(te_1),\qquad
B_{R,L}(t)=S^L_{n^{\le R},02,02}(te_1).
\]

**Věta.** Pro každý přípustný mřížový moment \(t\in[-\pi,\pi]\) platí

\[
A_{R,L}(0)=B_{R,L}(0)=u_{R,L},
\]
\[
\boxed{|B_{R,L}(t)-A_{R,L}(t)|\le t^2R^2(R+1)^4.}
\tag{1}
\]

**Důkaz.** Rovnost v nule plyne ze záměny souřadnic 1 a 2 v původní míře i ve výběru malých složek.

Pro jednu takovou složku a orientaci \(I\) pišme

\[
F_{\gamma,I}(t)=\sum_{p\in\gamma,\ \operatorname{ori}(p)=I}
n_p e^{-itc_{p,1}},\qquad
m_{\gamma,I}=\#\{p\in\gamma:\operatorname{ori}(p)=I\}.
\]

V použitém zdvihu je \(|c_{p,1}-c_{q,1}|\le R\). Po spárování dvojic \((p,q)\) a \((q,p)\) je čtverec formfaktoru součtem reálných kosinů. Z nerovnosti \(|1-\cos s|\le s^2/2\) dostáváme

\[
\big||F_{\gamma,I}(t)|^2-|F_{\gamma,I}(0)|^2\big|
\le\frac{t^2R^2}{2}m_{\gamma,I}^2.
\]

Pro jednu orientaci leží středy na posunuté celočíselné mříži. V kvádru o hraně \(R\) jich je nejvýše \((R+1)^4\), takže

\[
m_{\gamma,I}^2\le(R+1)^4m_{\gamma,I},\qquad
\sum_{\gamma\text{ malá}}m_{\gamma,I}\le V.
\]

Z přesného složkového rozkladu #1112 tudíž plyne

\[
|A_{R,L}(t)-A_{R,L}(0)|\le\frac{t^2R^2(R+1)^4}{2},
\]

a stejná mez pro \(B\). Sečtením a použitím rovnosti v nule dostáváme (1). Důkaz nepoužívá znaménko rozdílu na jednotlivých složkách. Je tedy slučitelný i se zápornou 21stěnnou složkou z #1112. □

### Důsledek pro stejné limitní profily

Malost složky u označené stěny \(p\) je místně určitelná. Prozkoumáme obsazenou složku v kvádru \(B_{R+1}(c_p)\). Dosáhne-li stěny se středem mimo \(B_R(c_p)\), nemůže být malá. Jinak prozkoumaný límec potvrzuje, že jsme našli celou složku, a ověříme její souřadnicové rozpětí nejvýše \(R\). Podmínka \(L>2R+4\) dovoluje tuto kontrolu v jednoznačném místním zdvihu.

Kovariance malé části má dosah nejvýše \(R\): dvě její stěny vzdálenější než \(R\) nemohou patřit téže malé složce a příspěvky různých složek se vyruší obrácením znamének. Pro pevné \(R\) tedy po místním limitu dostáváme spojitý trigonometrický polynom. V každém společném profilu \(\omega\) existuje společná hodnota \(u_R^\omega\), pro kterou

\[
b_{\le R}^\omega=u_R^\omega,
\qquad 25\chi_{\le R}^\omega=u_R^\omega.
\]

Druhá rovnost plyne z Wardovy identity malé části při \(t\ne0\) a ze spojitosti při \(t\to0\). Kde existují oba úplné koeficienty, platí

\[
\boxed{b^\omega-25\chi^\omega
=b_{>R}^\omega-25\chi_{>R}^\omega.}
\tag{2}
\]

Stejné odečtení funguje pro liminf a limsup, protože se odečítá skutečná limita malé části. **Číslo \(u_R^\omega\) se může mezi profily lišit.** Nelze je proto vytáhnout před oddělené infimum a supremum v definicích \(b_*\) a \(\chi_*\), pokud jeho společná hodnota nebyla dokázána.

### Rostoucí odstraněný průměr

Mez (1) dovoluje odstranit i rostoucí rodinu složek. Po původním místním limitu zvolme při \(0<|t|\le1\)

\[
R(t)=\lfloor |t|^{-1/4}\rfloor.
\]

Pak

\[
\boxed{|\Delta(t)-\Delta_{>R(t)}(t)|\le16|t|^{1/2}\longrightarrow0.}
\tag{3}
\]

Pro každé pevné \(t\) je \(R(t)\) konečné a objemová podmínka se plní před přechodem \(t\to0\). Nejde o dosazení nejnižšího momentu konečného toru.

Pokud by úplný rozdíl měl dolní limitu \(\delta>0\), musela by pro každý pevný \(R\) přetrvat alespoň taková příčná odezva velké části: \(\liminf_{t\to0}S_{n^{>R},02,02}(te_1)\ge\delta\). Odečítaná proudová část je totiž nezáporná. Toto je nutná podmínka, nikoli prokázaná vlastnost skutečného modelu.

## 5. Proč úplný odhad krátkého dosahu může cíl zrušit

Předpokládejme v jednom symetrickém přípustném profilu, že jeho Fourierovy hustoty jsou skutečně identifikovány s Fourierovými hustotami místní nekonečnoobjemové míry, a že

\[
\sum_{x\in\mathbb Z^4}|C_{n,II}(x)|<\infty,
\qquad I=01,02.
\]

Tato identifikace je dodatečný předpoklad: samotná místní konvergence ji nezaručuje. Postačující silnější podmínkou je stejnoměrná absolutní sčitatelnost konečněobjemových kovariancí včetně stejnoměrně mizejících vzdálených ocasů. Fourierovy hustoty místní míry jsou při uvedené sčitatelnosti spojité i v nule. Záměna souřadnic dává

\[
S_{n,02,02}(0)=S_{n,01,01}(0).
\]

Proto přímo z osové Wardovy identity plyne

\[
\boxed{\Delta_0=0,\qquad b=25\chi.}
\tag{4}
\]

Při uvedené identifikaci profilu tedy kladný rozdíl vyžaduje porušení této absolutní sčitatelnosti plošných korelací. **To nebrání rychlému poklesu proudových korelací.** Plošná a proudová kovariance jsou různé veličiny; proud vzniká použitím hranice a nese další rozdílové faktory.

## 6. Výslovná horní mez proudového koeficientu

Následující odhad lze použít na celý proud nebo, s pevně zvoleným \(R\), na skutečný proud \(j^{>R}\). Druhá možnost přímo navazuje na odečtení v (2). Označme zvolenou proudovou kovarianci \(C(00;x)\).

Předpokládejme, že se pro ni podaří dokázat **rovnoměrně v přípustných konečných objemech** skutečný odhad

\[
|C_L(00;x)|\le A r^{|x|_{1,L}},\qquad A\ge0,\quad 0<r<1,
\tag{5}
\]

kde \(|x|_{1,L}\) je periodická vzdálenost. Každý z uvažovaných proudů je hranicí periodického plošného pole, a proto má nulový celkový proud v každém směru. Rovnoměrná mez (5) umožní přenést do místního limitu jak nulový součet kovariance, tak její druhý moment. Platí pak

\[
\chi=-\frac12\sum_x x_1^2 C(00;x),\qquad
0\le\chi\le\frac A2\sum_x x_1^2r^{|x|_1}.
\]

Čtyřrozměrný součet se vyhodnotí přesně:

\[
\sum_{k\in\mathbb Z}r^{|k|}=\frac{1+r}{1-r},\qquad
\sum_{k\in\mathbb Z}k^2r^{|k|}=\frac{2r(1+r)}{(1-r)^3},
\]
\[
\boxed{\chi\le\chi_{\rm upper}
=A\frac{r(1+r)^4}{(1-r)^6}.}
\tag{6}
\]

Tato formule je vyhodnocením geometrického součtu. **Konstanty \(A,r\) pro skutečnou váhu \(W\) zde dokázány ani vyhodnoceny nejsou.** Samotný zápis (6) tedy není hledaným certifikátem \(\chi_*\).

### Ostřejší odhad se zachovanými znaménky

Pro konečný prostorový ořez \(K\) vezměme

\[
T_{K,L}=-\frac12\sum_{|x|_1\le K}x_1^2C_L(00;x).
\]

Pokud bude navíc doložena chyba místního přiblížení \(|C_L(00;x)-C^\omega(00;x)|\le e_{K,L}(x)\), dostáváme

\[
\chi^\omega\le T_{K,L}
+\frac12\sum_{|x|_1\le K}x_1^2e_{K,L}(x)
+\frac A2\sum_{m>K}w_m r^m,
\tag{7}
\]

kde přesná váha slupky v \(\mathbb Z^4\) je

\[
w_m=\sum_{|x|_1=m}x_1^2
=\frac{4m^5+20m^3+6m}{15},\qquad m\ge1.
\]

Zbytek řady lze přesně získat z (6) odečtením prvních \(K\) členů. Na rozdíl od úplného použití absolutních hodnot se v \(T_{K,L}\) zachová rušení znamének. Pro mez přes všechny profily musí platit stejné doložené chyby pro všechny profily, které původní předání připouští.

Ani odhad interakce dvou izolovaných proudových sektorů, ani potlačení podle velikosti nosiče nesmíme dosadit místo (5). Je třeba dokázat přechod ke kovarianci v úplné normalizované míře, včetně zbývajících proudových sektorů.

## 7. Co tento krok uzavírá a co dál chybí

Tento soubor uzavírá jednu konkrétní analytickou otázku: omezeně velké plošné složky nemohou nést nenulový limitní rozdíl \(b-25\chi\). Přesně známe jejich společný limitní příspěvek i horní mez chyby jeho odstranění.

Navazující čtyřhranový důkaz již zlepšuje globální koeficientovou mez jedné elementární smyčky z \(1/2\) na \(1/16\). Pro přímou kladnou uzávěru však stále chybějí dvě skutečné vlastnosti pevné míry:

1. **Vyhodnocená horní mez proudové tuhosti.** Dokázat odhad závislý na vzdálenosti pro úplnou proudovou kovarianci, případně pro \(j^{>R}\), a dosadit skutečné konstanty a objemové chyby do (6) nebo (7). Exponenciální pokles je postačující možnost; není nezbytný.
2. **Vyhodnocená dolní mez příčné odezvy.** Dokázat v tomtéž přípustném limitním profilu, že velké plošné složky nesou příčnou odezvu větší než horní mez příslušného proudového příspěvku. Po odstranění malé části musí být chyba alespoň tak přesně řízena, jak vyžaduje (1).

Je možné pracovat s původními \(b_*\) a \(\chi_*\), nebo po přesném společném odečtení s veličinami velké části. V obou případech je nutné dokončit skutečné číselné porovnání. **Žádná kladná hodnota \(b_{\rm lower}-25\chi_{\rm upper}\) z tohoto rozboru zatím nevzešla.**

P1, původní podmínky S1/P2, spektrální přechod S7 i `PHOTON-MASSLESS-PHASE` zůstávají otevřené. Text nijak nerozhoduje o skutečné fotonové fázi a nepovyšuje žádný výsledek do Canonu.

## 8. Rozsah kontroly

Samostatný agentní přezkum před zveřejněním potvrdil hlavní konečněobjemovou nerovnost, rozklad a momentové vzorce. Zde jsou již zapracována jeho tři upřesnění: obracení po jednotlivých členech, místní určitelnost malosti a výslovná limitní identifikace v oddílu 5. Nejde o slepý přezkum ani o formální povýšení.

Důkaz rozkladu a meze (1) je analytický: používá samostatné obracení souvislých složek, symetrii souřadnic, nerovnost pro kosinus a spočítaný počet stěn v konečném kvádru. Vzorec (6) plyne součinem čtyř jednorozměrných řad. Pomocná kontrola přesnou racionální aritmetikou porovnala prvních dvanáct koeficientů slupkové řady s uvedeným polynomem; nejde o měření korelací \(W\), formální sondu ani další architekturní potvrzení.

Původní nový text: Apache-2.0.
