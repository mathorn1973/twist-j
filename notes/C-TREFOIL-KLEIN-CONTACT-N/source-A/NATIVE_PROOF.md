# Trojlístková relace a přesná mez původních operací

**NON-CANONICAL. Analytický důsledek veřejných vět Public Canon v103.** Tento text neposouvá stav Canonu. Tvrzení se týká pevných slov v afinních jednobuněčných generátorech a přesně vymezených čtení dosažitelného ocasu.

## 1. Veřejné vstupy

Základ je [Public Canon v103](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md). Používáme již doložené výsledky:

- NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION: lineární části pěti afinních generátorů na \(V=\mathbb F_5^6\) generují grupu řádu 200.
- U-NATIVE-CHART-AND-QDD-READBACK a U-COUNTER-REACHABLE-AMPLITUDE-CLASS: pro dosažitelné listy \(X_n\), \(n\ge3\), existují bijekce \(\ell_n:X_n\to\mathbb F_5^5\) s \(\ell_{n+1}d_n=\ell_n\).
- KERNEL-Z6-SYNCHRONIZATION a FIRED-COMMUTATOR-NOGO: na dosažitelném ocasu se spouštějí pouze \(b,d,e\); jejich lineární části leží v Kleinově čtyřgrupě.
- KERNEL-WEDGE-COUPLING: v deklarované rozšířené architektuře jsou obousměrné součtové styky dvojice buněk.
- KERNEL-CONNECT-ALL-K: při všech deklarovaných písmenech a těchto součtových stycích je pro \(k\ge2\) celý spojený nosič jedinou dosažitelnou složkou.

Řád 200 ani veřejné klasifikace zde nově nevyčíslujeme. Následující argument potřebuje jejich přesný rozsah, nikoli nové numerické vyhledávání.

## 2. Grupa pevných afinních slov

Označme
\[
\Gamma=\langle a,b,c,d,e\rangle\le\operatorname{AGL}(V).
\]
Její prvky jsou předem daná slova působící stejným způsobem na celý nosič; nejsou to libovolné programy vybírající další operaci podle stavu.

Projekce na lineární část je surjektivní homomorfismus
\[
\pi:\Gamma\longrightarrow L,\qquad |L|=200.
\]
Každý prvek jádra je translace \(t_v:x\mapsto x+v\). Množina jejich vektorů je aditivní podgrupa \(V\); protože základní těleso je prvotěleso \(\mathbb F_5\), je současně \(\mathbb F_5\)-podprostorem. Pro nějaké \(0\le r\le6\) proto platí
\[
|\ker\pi|=5^r,\qquad
|\Gamma|=200\cdot5^r=2^3 5^{r+2}.
\]
Přesná posloupnost se nemusí štěpit. Hodnotu \(r\) nepotřebujeme. Podstatný důsledek je
\[
3\nmid|\Gamma|.
\]

## 3. Obecné lemma o trojlístkové relaci

**Lemma.** V konečné grupě \(H\), jejíž řád není dělitelný třemi, platí
\[
ABA=BAB\quad\Longrightarrow\quad A=B.
\]

**Důkaz.** Položme \(K_0=\langle A,B\rangle\), \(C=AB\) a \(\Delta=ABA=BAB\). Z relace plyne
\[
\Delta A=B\Delta,\qquad \Delta B=A\Delta.
\]
Tedy \(\Delta^2\) je centrální v \(K_0\). Přitom
\[
\Delta^2=(ABA)(BAB)=(AB)^3=C^3.
\]
Řád \(t\) prvku \(C\) je nesoudělný se třemi. Existuje celé \(k\) s \(3k\equiv1\pmod t\), takže
\[
C=(C^3)^k\in Z(K_0).
\]
Původní relace nyní říká
\[
CA=ABA=BAB=BC=CB.
\]
Zkrácením prvku \(C\) vyjde \(A=B\). \(\square\)

Konečnost je podstatný předpoklad. Pouhá nepřítomnost prvků řádu tři v nekonečné grupě nestačí. Centralita se týká podgrupy generované \(A,B\), nikoli automaticky celého \(H\).

## 4. Důsledek pro požadovaný značený obraz

Trojlístková grupa má prezentaci
\[
B_3=\langle \sigma_1,\sigma_2\mid
\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2\rangle.
\]
Každý její homomorfismus do \(\Gamma\) tedy ztotožní oba generátory. Jeho obraz je cyklický. Nelze tímto způsobem uskutečnit dvě různé značené meridiánové operace s neabelovským obrazem \(2I\).

Závěr platí také pro podgrupy \(\Gamma\), pro restrikce na společně invariantní podmnožiny a pro faktory podle invariantní ekvivalence: výsledná grupa má opět řád nedělitelný třemi.

Přesné podmínky tohoto závěru jsou:

1. \(A,B\) jsou pevné grupové operace nebo jejich homomorfní obrazy.
2. Relace je rovností operátorů na celém deklarovaném invariantním nosiči. Shoda na jednom stavu nestačí.
3. Čtení skutečně proplétá celou příslušnou grupovou akci. Libovolný výstupní dekodér tento předpoklad nesplňuje.

**Tato věta nevylučuje geometrický trojlístek.** Vylučuje konkrétní způsob realizace jeho necyklického meridiánového obrazu. Neřeší libovolně stavově řízený původní \(U\), čtení s pomocným čítačem, nové styky mezi buňkami ani obecné prostorové konfigurace. Meridiánová akce se navíc nemusí fyzikálně shodovat s časovým krokem; požadavek takové shody musí být součástí konkrétního modelu.

## 5. Co přesně dovoluje dosažitelný ocas \(U\)

Z již doložených bijekcí \(\ell_n\), \(n\ge3\), dostáváme změnu souřadnic na časově rozšířeném prostoru:
\[
\Phi(n,x)=(n,\ell_n(x)).
\]
Její propletení s původním dopředným krokem má tvar
\[
\Phi U\Phi^{-1}(n,\ell)=(n+1,\ell).
\]
Jde o konjugaci jednostranných dopředných systémů. Posun na celém jednostranném ocasu není surjektivní automorfismus.

Tato změna souřadnic používá známý čítač. Netvrdí, že se původní kontrolní stav nemění. Zachované jsou souřadnice \(\ell\), nikoli jednotlivé původní souřadnice.

Ve třídě čtení s dostupným \(n\) existuje pro každé \(m\ge2\) a libovolné \(G:\mathbb F_5^5\to\mathbb Z/m\mathbb Z\) přesné čtení
\[
R_m(n,x)=n+G(\ell_n(x))\pmod m.
\]
Splňuje
\[
R_m(U(n,x))=R_m(n,x)+1.
\]
Při \(G=0\) se čte jen \(n\bmod m\).

Samotná existence takového propletení tedy nevybírá pětku. Nevylučuje, že ji mohou odlišit další nezávislé podmínky přípustnosti. Bez čítače nebo jeho dovolené rekonstrukce toto čtení nemusí sestoupit na omezený pozorovací port.

Obecnější již veřejná klasifikace pro bijekci \(L:Y\to Y\) je
\[
R(n,x)=L^nG(\ell_n(x)).
\]
Zachované celočíselné čtení má zvláštní tvar
\[
B(n,x)=b(\ell_n(x)),\qquad b:\mathbb F_5^5\to\mathbb Z.
\]
Bez další podmínky je \(b\) libovolné. Přiřazení uzlu jednomu zachovanému údaji proto samo nedokazuje geometrický původ ani fyzikální význam takového čtení.

Na celém \(\Omega\) je užší třída separabilních čtení odlišná; veřejná třináctitřídní klasifikace přes \(Q(x)\in\mathbb F_5^2/\{\pm1\}\) se s těmito 3125 dosažitelnými údaji nesměšuje.

## 6. Společná aktualizace nezávislých kopií

Po třetím kroku mají všechny hlavy synchronizovaný list
\[
z(x_n)=4+2\theta_{n-1}.
\]
Proto skutečně spuštěný generátor na každém pevném času závisí jen na hodinách:
\[
(0,0)\mapsto e,\quad (0,1)\mapsto b,\quad
(1,0)\mapsto b,\quad (1,1)\mapsto d.
\]
Každý pevný časový úsek tohoto ocasu tak působí na celý aktuální list jedním pevným afinním slovem.

Pro dvě hlavy na stejném listu:
\[
x'_{n+1}-x_{n+1}=M_{g_n}(x'_n-x_n).
\]
Stejně se chová konečný počet nezávislých kopií se společným počátkem hodin. Lineární části jsou společné a leží v uvedené čtyřgrupě. Tato konstrukce neposkytuje vzájemně závislý pohyb buněk; takový styk musí přijít z dalšího konkrétního pravidla.

## 7. Přesný kladný vzor v deklarované spojené architektuře

V již deklarované rozšířené architektuře jsou dovoleny styky
\[
P_c(x,y)=(x,y+x),\qquad Q_c(x,y)=(x+y,y).
\]
Zvolme na indexu dvojice buněk
\[
A=Q_c=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
B=P_c^{-1}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
Přímým násobením nad \(\mathbb F_5\):
\[
ABA=BAB=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
\[
A^5=B^5=I,\qquad (AB)^3=-I,\qquad A\ne B.
\]
Mocniny \(A\) a \(B\) dávají všechny horní a dolní elementární matice. Eliminací generují \(\mathrm{SL}_2(\mathbb F_5)\). Její řád je \(24\cdot5=120\): první sloupec je libovolný nenulový vektor a pro každý z nich má rovnice determinantu jedna právě pět řešení pro druhý sloupec.

Tyto matice jsou přesně reziduální značené meridiány:
\[
A=\overline T,\qquad
B=\overline S\,\overline T\,\overline S^{-1}.
\]
Jsou tedy kladným algebraickým vzorem pro zkoumaný most. Determinant jedna zajišťuje zachování \(x\wedge y\), nikoli automaticky prostorového uzlového typu.

Součtové styky jsou samostatně deklarované operace. Jejich nezávislé připuštění jako řízených nebo autonomně vznikajících styků původního \(U\) tím není prokázáno.

Při všech deklarovaných písmenech a součtových stycích je pro \(k\ge2\) celý nosič jedinou složkou. Číslo invariantní vůči každému takovému příkazu proto musí být konstantní. Zachování fyzikálního uzlu se má testovat pro konkrétní skutečnou dynamiku, nikoli automaticky pro celý ovladatelný soubor operací.

## 8. Nejbližší rozhodnutelný krok

Další přesné zadání musí nejprve určit nezávisle přípustný styk, úplný stav včetně pamětí a řízení, a rovnost celých operací. Potom se dá rozhodnout, zda jeho skládání poskytuje dva různé meridiány a zda vzniká požadovaný obraz \(2I\).

Faktor tři v řádu výsledného konečného grupového obrazu je nutná první podmínka. Jeho přítomnost není dostačující. Teprve doložená meridiánová akce se může spojit s nezávisle definovaným prostorovým nosičem a s ověřením zachování pod úplným skutečným krokem.

Konstrukce prostoru, která předem vloží trojlístek do čtení zachovaných dat, tento úkol neřeší. Stejně tak tabulka 120 grupových prvků sama ještě neurčuje body, spojení a nad/pod křížení v prostoru.

## 9. Nezávislá kontrola argumentu

Samostatný oponent ověřil lemma, přesnou afinní posloupnost, časovou konjugaci, libovolné cyklické cíle a kladné součtové matice bez nové enumerace. Jeho dvě zpřesnění jsou v tomto textu začleněna: centrální prvek leží v centru generované podgrupy a konjugace ocasu používá časově rozšířený jednostranný nosič. Doložený veřejný řád 200 byl vstupem důkazu, nebyl v této kontrole nově vypočten.

