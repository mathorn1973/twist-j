# Přesné promíchání uvnitř již zadaného zdroje JM

**Stav:** NON-CANONICAL, L1, candidate-T. Jde o analytický důsledek výslovných definic Public Canon v104 a o podmíněnou větu o čtení. Nebyl spuštěn vědecký ověřovač. Text neodvozuje nové přechody z původního konečného pravidla \(U\) a neztotožňuje je s ním.

Výchozími řádky Public Canon v104 jsou `JM-RESULTANT-TRACE-SEAM`, `JM-RETAINED-RATIONAL-PAIR-SOURCE` a `JM-INTEGER-PAIR-INVOLUTION`. Níže používaná matice \(U_z\) je přesně matice tohoto zdroje. Není to nově přidaný směšovač. Novým nezávislým předpokladem zůstává oddělené a samostatně zachovávané čtení dvou níže určených logických kanálů.

## 1. Jeden již přípustný program

Kandidát používá

\[
S=\{z\in\mathbb Z^8:b_1-b_2-b_3\equiv0\pmod3\},
\qquad
G=\operatorname{diag}(5I_4-\mathbf1\mathbf1^{\mathsf T},4I_4),
\]

\[
q(z)=z^{\mathsf T}Gz,
\qquad
B_Q=\{z\in S:0<q(z)\le Q\},\qquad Q\ge8.
\]

Zvolme jednou provždy

\[
z_0=(1,0,0,0,0,0,0,0).
\]

Poslední čtyři souřadnice splňují podmínku modulo tři. První diagonální prvek \(G\) je čtyři, takže

\[
z_0\in S,\qquad q(z_0)=4,\qquad z_0\in B_Q
\quad\text{pro každé deklarované }Q\ge8.
\]

Tento program není vybírán podle výsledků čtení. Je pevný a jeho přípustnost plyne přímo z definice zdrojové třídy.

Položme

\[
V_0=\mathbb Q^9,\qquad G_0=\operatorname{diag}(1,G),
\qquad W=V_0\otimes_{\mathbb Q}V_0,
\qquad L=G_0\otimes G_0.
\]

Základní vektor \(e_0\) označuje referenční souřadnici. Označme \(\eta=(0,z_0)\in V_0\), tedy první souřadnici zdroje za referencí. Potom

\[
\langle e_0,e_0\rangle_{G_0}=1,\quad
\langle e_0,\eta\rangle_{G_0}=0,\quad
\langle\eta,\eta\rangle_{G_0}=4.
\]

## 2. Dva přesně určené kanály se stejnou vahou

Ve \(W\) definujme

\[
e=e_0\otimes e_0,\qquad
t=\eta\otimes\eta,\qquad
\ell=e_0\otimes\eta+\eta\otimes e_0,
\]

\[
\boxed{r=4e-t,\qquad s=2\ell.}
\]

Vektory \(e,t,\ell\) jsou navzájem kolmé pro \(L\). Jejich kvadráty norem jsou po řadě \(1,16,8\). Odtud přímo

\[
\boxed{\langle r,r\rangle_L=32,
\quad \langle s,s\rangle_L=32,
\quad \langle r,s\rangle_L=0.} \tag{1}
\]

V označených souřadnicích tenzoru \((0,0),(0,1),(1,0),(1,1)\) mají tyto vektory tvar

\[
r=(4,0,0,-1),\qquad s=(0,2,2,0),
\]

a všechny ostatní souřadnice jsou nulové. Jde o celočíselné vektory a o pevně zadanou racionální rovinu \(H=\operatorname{span}_{\mathbb Q}\{r,s\}\).

## 3. Matice JM na této rovině

Pro zvolený program je ve vzorci zdroje

\[
A=1+q(z_0)=5,\qquad d=A(A-1)=20,
\]

\[
y=e_0+\eta,\qquad w=y\otimes y=e+\ell+t,
\qquad v=Ae-w=r-\frac12s.
\]

Původní zdrojová definice tedy zní

\[
U_{z_0}=I-\frac{v v^{\mathsf T}L}{20}.
\]

Z (1) dostaneme

\[
\langle v,r\rangle_L=32,\qquad
\langle v,s\rangle_L=-16.
\]

Po dosazení do téže matice

\[
U_{z_0}r=r-\frac{32}{20}\left(r-\frac12s\right)
=-\frac35r+\frac45s,
\]

\[
U_{z_0}s=s+\frac{16}{20}\left(r-\frac12s\right)
=\frac45r+\frac35s.
\]

Rovina \(H\) je proto invariantní a v její uspořádané bázi \((r,s)\) platí přesně

\[
\boxed{U_{z_0}|_H=
\frac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}.} \tag{2}
\]

Tato matice je involuce. Věta o jednom promíchání z `PROOF.md` na ni dopadá přímo s \(a=-3/5\), \(b=4/5\). Není nutná změna znaménka, další přechod ani odkaz na podobnou matici z jiného oddílu programu.

## 4. Promíchání celých amplitudových vektorů

### 4.1 Připojený racionální nosič

Nechť \(A_0\) je libovolný racionální vektorový prostor, na kterém zdrojový přechod nepůsobí. Rozšíření \(U_{z_0}\otimes I_{A_0}\) splňuje pro všechna \(x,y\in A_0\)

\[
(U_{z_0}\otimes I_{A_0})(r\otimes x+s\otimes y)
=r\otimes\frac{-3x+4y}{5}
+s\otimes\frac{4x+3y}{5}. \tag{3}
\]

To je totožnost na celém racionálním nosiči. Pro její důkaz není potřeba zvolit normu na \(A_0\). Je-li navíc pro připojený nosič dána kladná metrika, je tato totožnost slučitelná s odpovídajícím tenzorovým rozšířením zdrojové izometrie. Obecný vektor vlevo nemusí být jednoduchým tenzorem; výrok se neomezuje na nezávislé čisté vstupy.

V případě \(A_0=K=\mathbb Q(\zeta_5)\) získáváme promíchání celé dvojice \((x,y)\in K^2\). Jde o dva koherentní kanály uvnitř společného nosiče. Nejde o výměnu ani mísení dvou celých nezávislých 81rozměrných portů.

### 4.2 Čtyři prokládané celočíselné buňky

Stejnou lineární totožnost lze uskutečnit bez tvrzení o zakódování obecného provázaného kvantového stavu. Zvolme pevnou racionální bázi

\[
(1,\zeta_5,\zeta_5^2,\zeta_5^3)
\]

a pišme \(x=(x_0,\ldots,x_3)\), \(y=(y_0,\ldots,y_3)\) v této bázi. Do čtyř samostatných buněk vložme racionální vektory

\[
\boxed{C_j=r x_j+s y_j,\qquad 0\le j<4.} \tag{4}
\]

Každá buňka má pouze čtyři možné nenulové souřadnice:

\[
(C_j)_{00}=4x_j,\quad
(C_j)_{01}=(C_j)_{10}=2y_j,\quad
(C_j)_{11}=-x_j.
\]

Kódování je injektivní a jeho pevné dekódování je

\[
\boxed{x_j=(C_j)_{00}/4,
\qquad y_j=(C_j)_{01}/2.} \tag{5}
\]

Při celočíselném zápisu \(C_j=X_j/D_j\), \(D_j>0\), se tedy čte

\[
x_j=(X_j)_{00}/(4D_j),\qquad
y_j=(X_j)_{01}/(2D_j).
\]

Každá racionální dvojice má takový zápis. Obsah \(\gcd(X_j,D_j)\) není součástí tohoto amplitudového čtení; různé obsahy mohou nést dodatečnou zachovanou informaci.

Na každou ze čtyř buněk aplikujme právě existující \(\widehat U_{z_0}\) z `JM-INTEGER-PAIR-INVOLUTION`. Jeho definice používá

\[
N=20I-vv^{\mathsf T}L,
\qquad N^2=400I,
\]

\[
m=\gcd(X_0,\ldots,X_{80},D),\quad
Y=NX,\quad M=20D,\quad
g=\gcd(Y_0,\ldots,Y_{80},M),
\]

\[
\widehat U_{z_0}(X,D)=(mY/g,mM/g).
\]

Tento úplný celočíselný přechod zachovává obsah, je involucí na všech buňkách a splňuje \(X'/D'=U_{z_0}(X/D)\). Jeho důkaz je převzat z uvedeného zdrojového řádku; nevyžaduje, aby buňka byla připravena ve stavu \(e\).

Ze (2), (4) a (5) tedy čtyři pevné aplikace, jedna na každou buňku, dávají pro všechna racionální \(x,y\)

\[
\boxed{(x,y)\longmapsto
\left(\frac{-3x+4y}{5},\frac{4x+3y}{5}\right).} \tag{6}
\]

Kódovaná rodina je při tomto přechodu uzavřená. Neomezenost racionálních vstupů se neopírá o neomezenou množinu programů: program \(z_0\) je stále stejný a přípustný. Rozsah \(B_Q\) omezuje program, zatímco samotná \(\widehat U_{z_0}\) je definována na celé celočíselné buňce.

Tento výrok sám nestanoví společný konečný rozpočet placeného zdroje pro všechny takové vstupy. Náklady změny čitatelů, jmenovatelů a řadiče se posuzují odděleně.

### 4.3 Pět buněk zároveň nese celé afinní působení

Pro napojení na afinní jedinečnost je výhodnější pětibuněčné kódování. Zachovává jednoduchost předchozí konstrukce a současně převádí afinní souměrnosti na výměny celých buněk.

Pišme

\[
x=\sum_{j=0}^3a_j\zeta_5^j,\qquad \sigma_x=\sum_{j=0}^3a_j,
\]

\[
c(x)=\left(a_0-\frac{\sigma_x}{5},\ldots,
a_3-\frac{\sigma_x}{5},-\frac{\sigma_x}{5}\right).
\]

Pak \(c(x)\) leží v racionální nadrovině součtu nula a

\[
\sum_{i=0}^4c_i(x)\zeta_5^i=x,
\qquad
\sum_{i=0}^4c_i(x)^2
=\sum_{j=0}^3a_j^2-\frac{\sigma_x^2}{5}
=\frac25q_+(x). \tag{A}
\]

Zobrazení \(c\) je racionální lineární bijekce mezi \(K\) a touto čtyřrozměrnou nadrovinou. Poslední rovnost používá přesný tvar \(\operatorname{Gram}(q_+)=(5I_4-\mathbf1\mathbf1^{\mathsf T})/2\), nikoli hledanou funkci čtení.

Pět buněk nyní kóduje dvojici vzorcem

\[
\boxed{C_i=r\,c_i(x)+s\,c_i(y),\qquad 0\le i<5.} \tag{B}
\]

Z každé buňky se jako dříve čte \(c_i(x)=(C_i)_{00}/4\) a \(c_i(y)=(C_i)_{01}/2\); potom \(x=\sum_i c_i(x)\zeta_5^i\) a obdobně \(y\).

Pět pevných aplikací \(U_{z_0}\), jedna na každé buňce, uskuteční znovu přesně (6). Součty pěti souřadnic zůstávají nulové. Násobení \(D_J=\zeta_5^2\) přesouvá souřadnici s indexem \(i\) na index \(i+2\) modulo pět. Galoisovo \(u(\zeta_5)=\zeta_5^2\) přesouvá index \(i\) na \(2i\) modulo pět. Oba přechody jsou tedy permutace stejných pěti buněk, proveditelné jejich úplnými výměnami. Na logických vektorech působí současně jako

\[
(x,y)\longmapsto(hx,hy),\qquad h\in\mathcal G.
\]

Promíchání i celá potřebná afinní akce tak mají jeden společný přesný nosič. Používáme třídu operací uzavřenou na skládání jednotlivých zdrojových involucí a výměn buněk. Libovolná permutace je součin výměn; její vykonání původním pevným časovým protokolem zdroje se tím neodvozuje. Není třeba přidávat nový afinní operátor uvnitř buňky.

### 4.4 Omezené celočíselné provedení s pevným jmenovatelem

Předchozí úplný přechod \(\widehat U_{z_0}\) zůstává správný. Pro pětibuněčnou rodinu existuje také jednodušší invariantní celočíselná podmřížka, na které není třeba měnit jmenovatel.

Položme

\[
T=\begin{pmatrix}-3&4\\4&3\end{pmatrix},\qquad
\Lambda=\{(p,q)\in\mathbb Z^2:q\equiv2p\pmod5\}.
\]

Pro \((p,q)\in\Lambda\) jsou

\[
p'=\frac{-3p+4q}{5},\qquad
q'=\frac{4p+3q}{5}
\]

celá čísla, a navíc

\[
q'-2p'=2p-q\in5\mathbb Z.
\]

Proto \((T/5)\Lambda=\Lambda\); rovnost, a ne pouze inkluze, plyne z \(T^2=25I\). Na celočíselných buňkách

\[
(X,D)=(rp+sq,D),\qquad (p,q)\in\Lambda,\quad D\in\mathbb Z_{>0},
\]

je tedy přesně definována involuce

\[
\boxed{(rp+sq,D)\longmapsto(rp'+sq',D).} \tag{C}
\]

Na racionálním podílu jde stále o tutéž \(U_{z_0}\). Jde však o **jiné celočíselné provedení na omezeném invariantním nosiči** než \(\widehat U_{z_0}\): jmenovatel zůstává pevný a společný obsah se obecně zachovávat nemusí. Vratnost (C) plyne přímo z involuce na \(\Lambda\), takže se žádná původní informace neztrácí. Nesmí se přenášet tvrzení, že (C) je definována na každé celé buňce, ani ji nazývat totožnou s úplným přechodem zachovávajícím obsah.

Pro pět buněk použijme společný \(D>0\), čitatele \(X_i=rp_i+sq_i\) a podmínky

\[
(p_i,q_i)\in\Lambda,\qquad
\sum_i p_i=\sum_i q_i=0.
\]

Tyto podmínky zachovává jak součin pěti přechodů (C), tak každá permutace buněk. Všechny racionální dvojice \((x,y)\in K^2\) jsou pokryty: stačí zvolit \(d>0\) tak, aby všechna \(d c_i(x),d c_i(y)\) byla celá, a položit

\[
D=5d,\qquad p_i=Dc_i(x),\qquad q_i=Dc_i(y).
\]

Pak jsou oba čitatelé dělitelné pěti, a tedy patří do \(\Lambda\). Jestliže naopak \(M\) odstraňuje jmenovatele původních čtyř mocninných koeficientů obou prvků, bezpečná přímá volba je \(D=25M\); vyvážené souřadnice totiž mohou přidat další faktor pět.

Úplně celočíselné souřadnice získáme zápisem \(q=2p+5k\). Pro pět buněk je nosič

\[
(A_4\oplus A_4)\times\mathbb Z_{>0},\qquad
A_4=\{a\in\mathbb Z^5:\textstyle\sum_i a_i=0\},
\]

kde stav označujeme \((p,k,D)\), a promíchání má jednoduchý tvar

\[
\boxed{(p,k,D)\longmapsto(p+4k,-k,D).} \tag{C2}
\]

Druhé použití vrátí přesně \((p,k,D)\). V těchto souřadnicích se vůbec nedělí. Zpětné čtení je \(c(x)=p/D\), \(c(y)=(2p+5k)/D\).

Odlišnost od zdvihu zachovávajícího obsah je konkrétní: jednopárový stav \((p,q,D)=(0,5,5)\) přejde na \((4,3,5)\). Obsah \(\gcd(rp+sq,D)\) klesne z pěti na jedna, přesto je přechod přesně vratný. Chceme-li příklad uvnitř pětibuněčného kódu, použijeme současně tuto dvojici a její záporný protějšek, ostatní tři nulové, se společným \(D=5\).

Zdrojový důkaz PR #1681, oddíl 4 (připnutý odkaz v `SOURCES.md`), již připouští pro pevný program invariantní mřížku \(\mathbb Z^{81}+U_z\mathbb Z^{81}\). Výše uvedená \(\Lambda\) je konkrétní invariantní podmřížka v určené dvourozměrné rovině, sestavená z téže racionální matice. Nevytváří jiný racionální přechod.

### 4.5 Skutečný buněčný účet se při tomto provedení nemění

Na omezeném nosiči (C) platí

\[
E_{\rm cell}(X,D)=X^{\mathsf T}LX+D^2
=32(p^2+q^2)+D^2.
\]

Matice \(T/5\) zachovává \(p^2+q^2\) a \(D\) se nemění. Proto každá z pěti buněk zachovává přesně svůj již zadaný účet \(E_{\rm cell}\). Pro jejich součet navíc (A) dává

\[
\boxed{
\sum_{i=0}^4E_{\rm cell}(X_i,D)
=\frac{64}{5}D^2\bigl(q_+(x)+q_+(y)\bigr)+5D^2.
} \tag{D}
\]

Při pevném \(D\) je tedy pohyblivá část tohoto konkrétního účtu po odečtení pevné referenční ceny a vydělení zobrazenou známou škálou právě součtem dvou \(q_+\). Tato totožnost nabízí přímé napojení na již zadaný účet; není pouze důkazem existence libovolné pozitivní formy.

Výrok se týká součinu pěti pevných přechodů na uvedených buňkách a jejich výměn. Neříká, že celý původní autonomní placený zdroj vykoná tuto posloupnost zdarma: jeho program, hodiny a řadič mají další položky účtu. Nevztahuje se ani na úplný přechod \(\widehat U_z\) mimo omezený nosič (C).

## 5. Co tento přechod vynutí, je-li účet oddělený

Nechť \(f,g:K\to\mathbb R_{\ge0}\), \(f(0)=g(0)=0\). Výslovně předpokládejme následující pravidlo čtení:

1. Na celé pětibuněčné rodině (B) je sledovaný účet přesně \(f(x)+g(y)\). Závisí pouze na racionálně dekódovaných amplitudách, nikoli na obsahu celočíselného zápisu nebo na volbě společného jmenovatele.
2. Součet \(f(x)+g(y)\) se sám zachovává při součinu pěti zdrojových přechodů dávajících (6) a při permutacích buněk odpovídajících oběma afinním generátorům, pro všechna \(x,y\in K\). Rozdíl tohoto účtu se nevyrovnává změnou zásobníku nebo jiného účtu.

Podmínka zachování při promíchání dává funkcionální rovnici

\[
f\left(\frac{-3x+4y}{5}\right)
+g\left(\frac{4x+3y}{5}\right)
=f(x)+g(y). \tag{7}
\]

Zesílení věty v `PROOF.md`, oddíl 2, platí pro každé nenulové racionální \(a,b\) s \(a^2+b^2=1\), tedy i pro \(a=-3/5\), \(b=4/5\). Smíšené druhé rozdíly (7) nutí obě funkce být součtem kvadratické a racionálně lineární funkce. Nezápornost na malých kladných i záporných racionálních násobcích odstraní lineární členy. Dosazení \(y=0\) pak dává

\[
\frac9{25}f(x)+\frac{16}{25}g(x)=f(x),
\]

takže \(f=g\). Jde o jednu společnou kvadratickou formu se stejným měřítkem v obou kanálech. Není předem předpokládána spojitost, měřitelnost, stupeň ani shoda obou funkcí.

Současná afinní invariance odděleného účtu znamená

\[
f(hx)+g(hy)=f(x)+g(y),\qquad h\in\mathcal G.
\]

Dosazením \(y=0\) a \(x=0\) získáme samostatnou afinní invarianci obou funkcí. Není nutné mít přechod, který by působil afinně pouze na jednom z kanálů. Afinní věta použitá v oddílu 3 téhož důkazu následně určí

\[
\boxed{f(x)=g(x)=c\,q_+(x),\qquad
q_+(x)=\operatorname{Tr}_{\mathbb Q(\sqrt5)/\mathbb Q}(x\bar x),
\quad c\ge0.} \tag{8}
\]

Nenulové čtení dává \(c>0\); jedna kalibrační hodnota určí zbývající násobek.

**Oddělenost a samostatné zachování tohoto logického účtu jsou nezávislé předpoklady.** Matice JM již dodává přechod (6), afinní akce se provádí výměnami a (D) dodává konkrétní odpovídající buněčný účet. Samotná existence přístroje však neurčuje, že každé fyzikální čtení musí mít tuto oddělenou podobu. Zvláště to neplyne jen ze zachování bankovního účtu \(E+b\) v `JM-FUNDED-INTEGER-PAIR-SOURCE`: jeho změnu může zásobník vyrovnat. Totožnost (D) je přesnějším tvrzením na výslovně omezeném nosiči s pevným jmenovatelem.

Při uvedených předpokladech na čtení nejde o kruhový důkaz: konkrétní matice je známá před volbou hledaných \(f,g\), zatímco (8) je až závěr. Nejde však ani o odvození této matice z původního \(U\). Zdroj JM byl sám definován za použití vybrané metriky \(L\), a tuto závislost výsledek neodstraňuje.

## 6. Přesná překážka pro mísení celých buněk

Předchozí realizace nepopírá následující nemožnost. Uvažujme kartézský seznam celých racionálních buněk \(C_1,\ldots,C_n\in W\) a pouze tyto přechody:

- libovolné existující \(U_z\) na jedné celé buňce;
- výměnu dvou celých buněk;
- podmíněný výběr takových přechodů, při němž se nepřidává jiná změna jejich racionálních vektorů.

Definujme

\[
Q_L(C)=C^{\mathsf T}LC.
\]

Každé \(U_z\) zachovává \(Q_L\) jednotlivé buňky a výměna pouze přehodí jeho hodnoty. Proto každé konečné slovo zachovává celý multiset

\[
\boxed{\{Q_L(C_1),\ldots,Q_L(C_n)\}.} \tag{9}
\]

Totéž platí pro celočíselné buňky při \(Q_L(X,D)=X^{\mathsf T}LX/D^2\), neboť \(\widehat U_z\) přesně zdvihá příslušnou racionální izometrii. Podmíněné řízení závěr nemění: každá skutečně provedená větev má tutéž vlastnost.

Zvláště pro libovolnou funkci \(h:\mathbb Q_{\ge0}\to\mathbb R\) je invariantní

\[
\sum_i h\bigl(Q_L(C_i)\bigr).
\]

Volba \(h(t)=t^2\) dává nezáporný účet čtvrtého stupně, který se sčítá přes celé buňky. Samotné lokální izometrie a výměny proto jeho použití nevylučují.

Z (9) plyne také nemožnost realizovat na **dvou celých buňkách** univerzální přechod

\[
(C,D)\longmapsto
\left(\frac{-3C+4D}{5},\frac{4C+3D}{5}\right) \tag{10}
\]

pouze uvedenou abecedou.

Je-li \(D=0\), \(Q_L(C)=t>0\), mají dvě cílové buňky normové hodnoty \(9t/25\) a \(16t/25\), zatímco vstup měl \(t\) a nulu. Pokud se pomocné buňky obnovují, lze jejich nezměněný multiset z obou stran (9) zrušit. Zbylé multisety jsou různé, což je spor.

Ani konečně mnoho pevných počátečních pomocných buněk, které se obnovovat nemusí, neumožní (10) pro všechny vstupy. Nechť jejich počáteční normové hodnoty jsou \(c_1,\ldots,c_m\). Zvolme \(C=\lambda C_0\) pro pevné \(C_0\ne0\) a nenulové racionální \(\lambda\). Hodnota \(t=\lambda^2Q_L(C_0)\) může nabývat nekonečně mnoha hodnot, takže ji lze zvolit mimo konečný seznam \(25c_i/9\) a \(25c_i/16\). Potom ani jedna požadovaná cílová hodnota není ve vstupním multisetu: není rovna \(0\), \(t\) ani žádnému \(c_i\). To odporuje (9).

Tento důkaz je tvrzením o kartézských vektorech buněk a jejich racionálním čtení. Nelze jej beze změny použít na obecný provázaný stav v tenzorovém součinu, kde jednotlivým buňkám nemusí být přiřazen čistý amplitudový vektor \(C_i\).

## 7. Proč prokládané kódování překážku obchází

V kódování (4) neleží \(x\) v první celé buňce a \(y\) ve druhé. Oba logické kanály mají jednu souřadnici v každé ze čtyř buněk. Pro každé \(j\) platí

\[
Q_L(C_j)=32(x_j^2+y_j^2).
\]

Přechod (6) tuto hodnotu zachovává pro každé \(j\) zvlášť. Multiset (9) se tedy vůbec nemění. Přesto se oba celé logické vektory promíchají.

Protipříklad čtvrtého stupně z oddílu 6 na této kódované rodině čte

\[
\sum_{j=0}^3Q_L(C_j)^2
=1024\sum_{j=0}^3(x_j^2+y_j^2)^2.
\]

Tento účet obsahuje smíšené členy

\[
2048\sum_{j=0}^3x_j^2y_j^2
\]

a nelze jej vyjádřit jako \(f(x)+g(y)\) s \(f(0)=g(0)=0\). Dosazení \(y=0\) a \(x=0\) by totiž muselo určit

\[
f(x)=1024\sum_jx_j^4,\qquad g(y)=1024\sum_jy_j^4,
\]

což uvedené smíšené členy neobsahuje. Například pro \(x=y=(1,0,0,0)\) je společný účet \(4096\), zatímco takto určený součet oddělených účtů je \(2048\).

Stejná překážka oddělenosti platí v hlavní pětibuněčné rodině (B): nahradíme \(x_j,y_j\) souřadnicemi \(c_i(x),c_i(y)\) a sčítáme přes pět buněk. Při \(x=y\ne0\) je společný účet čtyřnásobkem \(1024\sum_i c_i(x)^4\), zatímco oddělený součet vynucený vstupy \((x,0)\) a \((0,x)\) je pouze dvojnásobkem. Nulový součet pěti souřadnic tento rozpor neodstraňuje.

Existující zdroj tedy již obsahuje potřebné přesné promíchání na celé racionální dvojici v pevné kódované rodině. Pětibuněčná verze navíc na stejném nosiči realizuje afinní působení a má omezené celočíselné provedení s pevným jmenovatelem a zachovaným buněčným účtem (D). Otevřená identifikace je užší: zda sledované fyzikální čtení právě na této rodině splňuje oddělenost a samostatné zachování z oddílu 5. Tato otázka se nesmí zaměnit s již dokázanou vratností zdroje, s uchováním jeho celkového bankovního účtu ani s dynamikou původního \(U\).
