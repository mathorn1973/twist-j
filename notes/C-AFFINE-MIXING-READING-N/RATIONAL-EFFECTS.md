# Racionální efekty: alternativní silnější podmínky čtení

**Stav:** NON-CANONICAL, L1, candidate-T; podmíněný matematický dodatek.

Tento dodatek podává konečněrozměrnou racionální verzi známé efektové Gleasonovy–Buschovy věty. Obecná věta ani přechod od efektů k hustotnímu operátoru nejsou novým objevem tohoto balíčku. Zde je důkaz přizpůsoben racionálnímu nosiči a jeho neortonormálnímu Gramu. Hlavní referenční cesta balíčku je v `OPERATIONAL-READING.md`; zde se předpokládá podstatně bohatší doména měření.

## 1. Výslovná dodatečná hypotéza

Nechť \(V=\mathbb Q^n\), \(G=G^\top\in M_n(\mathbb Q)\), \(G>0\), a

\[
\mathcal S_G=\{E\in M_n(\mathbb Q):E^\top G=GE\},\qquad
\mathcal E_G=\{E\in\mathcal S_G:0\le E\le I\}.
\]

Uspořádání je určeno Gramem: \(E\ge0\) znamená \(GE\ge0\) jako symetrickou kvadratickou formu. Pro každou pevnou nenulovou přípravu \(\psi\in V\) předpokládáme funkci

\[
w_\psi:\mathcal E_G\longrightarrow[0,1]
\]

na **všech** těchto racionálních efektech, splňující:

1. \(w_\psi(I)=1\).
2. \(w_\psi(E+F)=w_\psi(E)+w_\psi(F)\), kdykoli \(E,F\ge0\) a \(E+F\le I\).
3. \(w_\psi(P_\psi)=1\), kde
   \[
   P_\psi=\frac{\psi\psi^\top G}{\psi^\top G\psi}.
   \]

Operační obsah druhého bodu zahrnuje totožnost váhy stejného efektu v různých kontextech a slučování výlučných výsledků. Pro \(E+F\le I\) jde o racionální POVM \((E,F,I-E-F)\) a jeho sloučení \((E+F,I-E-F)\). Nevyžaduje se, aby \(E,F\) komutovaly.

Dostupnost celé této domény ani její nekontextové čtení nejsou v tomto dodatku odvozeny z existujících bran \(U_z\) a permutací. Jsou to dodatečné předpoklady. Spojitost, měřitelnost a aditivita nad reálnými skaláry se nepředpokládají.

## 2. Kladné racionálně lineární rozšíření

Přípravu nyní držíme pevnou a píšeme \(w\). Z aditivity plyne \(w(0)=0\) a

\[
w(E/k)=w(E)/k\qquad(k\in\mathbb Z_{>0}).
\]

Pro libovolné \(A\in\mathcal S_G\), \(A\ge0\), zvolme celé \(m>0\) tak velké, že \(A\le mI\), a definujme

\[
\Phi(A)=m\,w(A/m).
\]

Takové \(m\) existuje bez odmocniny \(G\): racionální Gram–Schmidt poskytne racionální ortogonální základ s kladnými racionálními diagonálními normami a odhad \(2|ab|\le a^2+b^2\) dá potřebnou horní mez. Nezávislost na volbě \(m\) plyne z

\[
m\,w(A/m)=mn\,w(A/(mn))=n\,w(A/n).
\]

Společným dostatečně velkým jmenovatelem dostaneme aditivitu \(\Phi\) na pozitivním kuželu, odtud jeho racionální homogenitu. Každý \(H\in\mathcal S_G\) je rozdíl pozitivních prvků. Položíme

\[
\Phi(A-B)=\Phi(A)-\Phi(B).
\]

Je-li \(A-B=A'-B'\), pak \(A+B'=A'+B\), takže hodnota nezávisí na rozkladu. Vznikne kladný \(\mathbb Q\)-lineární funkcionál na celé \(\mathcal S_G\), shodný s \(w\) na efektech, s \(\Phi(I)=1\).

Pro úplnost, jeho stopový tvar v daném Gramu je

\[
\Phi(E)=\operatorname{Tr}(BGE)=\operatorname{Tr}(\rho E),
\qquad B=B^\top,\quad \rho=BG.
\]

Existence a jednoznačnost reálné symetrické matice \(B\) je konečněrozměrná dualita symetrických matic: \(E\mapsto GE\) identifikuje \(\mathcal S_G\) s racionálními symetrickými maticemi. Pro \(u\in\mathbb Q^n\) je \(G^{-1}uu^\top\) pozitivní racionální operátor, a proto

\[
u^\top Bu=\Phi(G^{-1}uu^\top)\ge0.
\]

Tedy \(B\ge0\), ekvivalentně \(G\rho=GBG\ge0\), dále \(\rho^\top G=G\rho\) a \(\operatorname{Tr}\rho=1\). Nezápornost reálné kvadratické formy na všech racionálních vektorech implikuje její nezápornost: záporná hodnota by přetrvala při dostatečně přesné racionální aproximaci souřadnic. Jde o vlastnost konečné kvadratické formy, nikoli o předpoklad spojitosti \(w\). Následující čistý případ ani tento aproximační argument nepotřebuje. Obecná \(\rho\) může mít reálné koeficienty.

## 3. Jistota přípravy vynutí Bornovo čtení

Racionálním Gram–Schmidtem doplňme \(u_1=\psi\) na \(G\)-ortogonální racionální základ. Pišme

\[
d_i=u_i^\top Gu_i>0,\qquad P_i=u_i u_i^\top G/d_i.
\]

Z \(\sum_iP_i=I\), pozitivity a jistoty \(\Phi(P_1)=1\) plyne \(\Phi(P_i)=0\) pro \(i>1\). Pro \(i<j\) položme

\[
H_{ij}=u_i u_j^\top G+u_j u_i^\top G.
\]

Kladnost na rank-one operátorech dává pro každé \(t\in\mathbb Q\)

\[
0\le\Phi\bigl((u_i+t u_j)(u_i+t u_j)^\top G\bigr)
=d_i\Phi(P_i)+t\Phi(H_{ij})+t^2d_j\Phi(P_j).
\]

Je-li \(i=1<j\), pravá strana je \(d_1+t\Phi(H_{1j})\); nezápornost pro všechna racionální \(t\) vynutí \(\Phi(H_{1j})=0\). Pro \(1<i<j\) dostáváme totéž z \(t\Phi(H_{ij})\ge0\).

Prvky \(P_i,H_{ij}\) tvoří racionální základ \(\mathcal S_G\). Tím je funkcionál úplně určen a

\[
\boxed{\displaystyle
w_\psi(E)=\frac{\psi^\top GE\psi}{\psi^\top G\psi}
=\operatorname{Tr}(P_\psi E).}
\]

Zvláště \(\rho_\psi=P_\psi\). Důkaz platí v každé konečné dimenzi; nemá výjimku pro dimenzi dvě. Čistý závěr byl získán pouze racionální algebrou a nezáporností, bez limit a bez normalizace základových vektorů iracionálními odmocninami.

## 4. Proč nestačí binární konzistence ani pouhý rámcový test

Nechť

\[
b_\psi(E)=\frac{\psi^\top GE\psi}{\psi^\top G\psi},\qquad
h(t)=\frac{t^2}{t^2+(1-t)^2},\qquad \widetilde w(E)=h(b_\psi(E)).
\]

Toto přiřazení je definováno na všech efektech, leží v \([0,1]\), zachovává jistotu přípravy a pro každý binární test splňuje

\[
\widetilde w(E)+\widetilde w(I-E)=1,
\]

protože \(h(t)+h(1-t)=1\). Přesto není aditivní. Racionální třívýsledkové POVM \((I/3,I/3,I/3)\) by mělo součet vah

\[
3h(1/3)=3/5\ne1.
\]

Opakované stejné efekty jsou zde tři odlišně označené výlučné výsledky. Samotná konzistence doplňkových dvojic tedy nestačí, ani když je přiřazení globálně definované a nekontextové.

Projektorové či omezené racionální rámcové podmínky nejsou uvedenou efektovou smlouvou. Klíčový krok \(E\mapsto E/k\) opouští projektory; shoda součtu na vybraných projektorových rámcích jej neopravňuje. Nekvadratický rámcový protipříklad se tudíž nemůže automaticky přenést na všechny POVM. Netvrdíme tím neplatnost klasické Gleasonovy věty na její úplné reálné či komplexní doméně a v příslušných dimenzích.

## 5. Použití a přesná hranice

Pro \(V=K\oplus K\), \(K=\mathbb Q(\zeta_5)\), s Gramem \(q_+\oplus q_+\), přípravou \(\psi=(x,y)\ne0\) a dvěma kanálovými projektory dostaneme

\[
\Pr(X\mid x,y)=\frac{q_+(x)}{q_+(x)+q_+(y)},\qquad
\Pr(Y\mid x,y)=\frac{q_+(y)}{q_+(x)+q_+(y)}.
\]

Společná škála Gramu se vykrátí. Jde o \(\mathbb Q\)-prostor dimenze osm: doména obsahuje všechny příslušné efekty v \(\operatorname{End}_{\mathbb Q}(K^2)\). Rank-one \(P_\psi\) obecně není \(K\)-lineární; nahrazení domény pouze \(K\)-lineárními efekty by bylo jinou větou.

Zde se určuje normalizovaná pravděpodobnost výsledku při daném Gramu. Neodvozuje se tím dostupnost všech efektů z původního \(U\), libovolné nenormalizované zdrojové čtení ani mechanismus skutečného vzorkování na L6. Výběr Gramu, jeho realizace v JM nosiči a operační referenční cesta mají v balíčku vlastní důkazy a vlastní předpoklady.

## 6. Známé primární zdroje

- P. Busch, *Quantum states and generalized observables: a simple proof of Gleason's theorem*, Phys. Rev. Lett. **91**, 120403 (2003), [arXiv:quant-ph/9909073v3](https://arxiv.org/abs/quant-ph/9909073v3). Charakterizace vah na všech efektech pomocí hustotního operátoru; rozšíření na pozitivní kužel a lineární funkcionál.
- C. M. Caves, C. A. Fuchs, K. Manne, J. M. Renes, *Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements*, Found. Phys. **34**, 193 (2004), [arXiv:quant-ph/0306179v1](https://arxiv.org/abs/quant-ph/0306179v1). Efektová formulace zahrnuje dvourozměrné systémy i racionální pole; nekontextovost je výslovným předpokladem.

Zdejší samostatný důkaz zpřesňuje použití těchto známých principů pro konkrétní racionální Gram, přípravu a typy nosiče v tomto balíčku. Neoznačuje obecný Gleasonův–Buschův výsledek za nový.
