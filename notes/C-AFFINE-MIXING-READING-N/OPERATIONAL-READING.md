# Čtvercové čtení z měření vůči pevnému referenčnímu kanálu

**Stav:** NON-CANONICAL, L1, candidate-T. Analytická věta za přesně uvedených podmínek čtení. Bez vědecké exekuce, bez odvození skutečných četností nebo měřicího přístroje z původního pravidla \(U\).

Cílem je nahradit předpoklad nepozorovaného součtu \(f(x)+g(y)\) podmínkami pro tři vzájemně výlučné výsledky jednoho čtení: referenci, první kanál a druhý kanál. Rozhodující podmínkou bude shoda poměrů výsledkových vah při vyřazení třetího výsledku a při samostatné kalibraci. Samotná binárnost, normalizace a slučování výsledků nestačí.

## 1. Reference již má pevný kanál v téže matici JM

Použijme značení a pevný program \(z_0\) z `EXISTING-SOURCE.md`:

\[
e=e_0\otimes e_0,\quad
t=\eta\otimes\eta,\quad
\ell=e_0\otimes\eta+\eta\otimes e_0,
\quad r=4e-t,\quad s=2\ell.
\]

Definujme navíc

\[
\boxed{k_0=4e+t.}
\]

Protože \(e,t,\ell\) jsou navzájem kolmé s kvadráty norem \(1,16,8\), platí

\[
\langle k_0,k_0\rangle_L
=\langle r,r\rangle_L
=\langle s,s\rangle_L=32,
\]

\[
\langle k_0,r\rangle_L
=\langle k_0,s\rangle_L
=\langle r,s\rangle_L=0.
\]

Normála zdrojového odrazu je \(v=r-s/2\). Je kolmá ke \(k_0\), takže přesně

\[
U_{z_0}k_0=k_0,
\qquad
U_{z_0}|_{\operatorname{span}(r,s)}
=\frac15\begin{pmatrix}-3&4\\4&3\end{pmatrix}. \tag{1}
\]

Třetí nedotčený kanál tedy není přidán změnou dynamiky. Je už součástí téhož \(U_{z_0}\). Z totožnosti amplitudového kanálu však ještě neplyne žádná pravděpodobnostní četnost výsledku.

## 2. Pět buněk se společnou referencí

Nechť \(K=\mathbb Q(\zeta_5)\), \(F=\mathbb Q(\sqrt5)\) a

\[
q_+(x)=\operatorname{Tr}_{F/\mathbb Q}(x\bar x).
\]

Pro \(x=\sum_{j=0}^3a_j\zeta_5^j\), \(\sigma_x=\sum_ja_j\), použijme nulově součtové souřadnice

\[
c(x)=\left(a_0-\frac{\sigma_x}{5},\ldots,
a_3-\frac{\sigma_x}{5},-\frac{\sigma_x}{5}\right),
\]

\[
\sum_i c_i(x)=0,
\qquad x=\sum_i c_i(x)\zeta_5^i,
\qquad \sum_i c_i(x)^2=\frac25q_+(x).
\]

Kódovaná rodina s referencí je

\[
\boxed{C_i=k_0+r\,c_i(x)+s\,c_i(y),\qquad 0\le i<5.} \tag{2}
\]

Reference má ve všech pěti buňkách stále koeficient jedna. Každý zdrojový přechod ji zachová podle (1); každá výměna buněk zachová společný referenční vektor \((k_0,\ldots,k_0)\). Oba signálové kanály přitom mají nulový součet souřadnic.

Pět aplikací \(U_{z_0}\) realizuje

\[
S(x,y)=\left(\frac{-3x+4y}{5},\frac{4x+3y}{5}\right),
\qquad S^2=I.
\]

Přesuny indexů \(i\mapsto i+2\) a \(i\mapsto2i\) realizují současně na obou kanálech generátory

\[
D_Jx=\zeta_5^2x,
\qquad u(\zeta_5)=\zeta_5^2,
\qquad\mathcal G=\langle D_J,u\rangle
\simeq\operatorname{AGL}_1(\mathbb F_5).
\]

### Přesné celočíselné provedení

Označme

\[
A_4=\{p\in\mathbb Z^5:\sum_i p_i=0\}.
\]

Úplný nosič této omezené konstrukce tvoří \(p,\kappa\in A_4\), \(D\in\mathbb Z_{>0}\). Položme

\[
q=2p+5\kappa,\qquad
X_i=Dk_0+rp_i+sq_i.
\]

Racionálně se čte \(C_i=X_i/D\), tedy \(c_i(x)=p_i/D\) a \(c_i(y)=q_i/D\). Z toho

\[
x=\sum_i(p_i/D)\zeta_5^i,
\qquad y=\sum_i(q_i/D)\zeta_5^i.
\]

V souřadnicích \((0,0),(0,1),(1,0),(1,1)\) je

\[
(X_i)_{00}=4(D+p_i),\quad
(X_i)_{01}=(X_i)_{10}=2q_i,\quad
(X_i)_{11}=D-p_i,
\]

takže kódování je při uloženém \(D\) přesně vratné. Pět zdrojových matic má na tomto nosiči prostý celočíselný zápis

\[
\boxed{(p,\kappa,D)\longmapsto(p+4\kappa,-\kappa,D).} \tag{3}
\]

Skutečně

\[
p'=(-3p+4q)/5=p+4\kappa,
\quad q'=(4p+3q)/5=2p+3\kappa
=2p'+5(-\kappa).
\]

Vratnost a zachování obou nulových součtů jsou okamžité. Afinní přechody pouze permutují současně souřadnice \(p,\kappa\). Každou racionální dvojici \((x,y)\) lze zakódovat: zvolíme \(D\) jako pětinásobek společného jmenovatele všech \(c_i(x),c_i(y)\), čímž jsou \(p_i,q_i\) dělitelné pěti a \(\kappa_i=(q_i-2p_i)/5\) celá.

Jde o omezené provedení s pevným jmenovatelem, nikoli o totožnost s úplným \(\widehat U_z\), které na celém původním nosiči zachovává obsah. Příslušná rozdílnost nosičů je podrobně vymezena v `EXISTING-SOURCE.md`.

Pro již zadaný buněčný účet dostáváme

\[
\sum_iE_{\rm cell}(X_i,D)
=\sum_i(X_i^{\mathsf T}LX_i+D^2)
=165D^2+32\sum_i(p_i^2+q_i^2),
\]

\[
\boxed{
\sum_iE_{\rm cell}(X_i,D)
=165D^2+\frac{64}{5}D^2
\bigl(q_+(x)+q_+(y)\bigr).
} \tag{4}
\]

Tento účet zachovávají (3) i permutace. Výrok se týká buněk; není tvrzením o bezplatném běhu celého autonomního zdroje včetně jeho řadiče a hodin.

## 3. Podmínky přímo pro výsledky čtení

Pro každý \((x,y)\in K^2\) nechť jsou dána tři čísla

\[
P_0(x,y),\quad P_1(x,y),\quad P_2(x,y).
\]

Mají představovat tři vzájemně výlučné a společně úplné výsledky na kódované rodině: reference, první kanál, druhý kanál. Jde o společné rozdělení, nikoli o tři libovolné binární experimenty, jejichž pravděpodobnosti by se směly bez dalšího sečíst.

Předpoklady jsou:

**P1. Kladná reference a nepřítomnost signálu.** Pro všechny vstupy

\[
P_i\ge0,\qquad P_0+P_1+P_2=1,\qquad P_0>0,
\]

\[
P_1(0,y)=0,\qquad P_2(x,0)=0.
\]

V experimentu \((x,0)\) tedy zbývají pouze výsledky 0 a 1; v experimentu \((0,y)\) pouze 0 a 2. Kladnost reference zaručuje konečné kalibrační poměry i při nenulových signálech.

**P2. Shoda vyřazených záznamů se samostatnou kalibrací.** Jestliže v experimentu \((x,y)\) vyřadíme záznamy výsledku 2, poměr zbývajících výsledků 0 a 1 souhlasí s experimentem \((x,0)\). Obdobně po vyřazení výsledku 1 souhlasí zbylý poměr s experimentem \((0,y)\). Přesně:

\[
\frac{P_1(x,y)}{P_0(x,y)+P_1(x,y)}=P_1(x,0),
\]

\[
\frac{P_2(x,y)}{P_0(x,y)+P_2(x,y)}=P_2(0,y). \tag{5}
\]

Při P1 jsou to ekvivalentně vztahy

\[
\frac{P_1(x,y)}{P_0(x,y)}
=\frac{P_1(x,0)}{P_0(x,0)},\qquad
\frac{P_2(x,y)}{P_0(x,y)}
=\frac{P_2(0,y)}{P_0(0,y)}. \tag{6}
\]

Podmínka není důsledkem pouhého vyřazení záznamů: to určuje pouze levou stranu (5). Rovnost s jiným, samostatně připraveným experimentem je dodatečná podmínka slučitelnosti čtení. Právě ona zakazuje, aby druhý kanál měnil poměr prvního kanálu vůči stejné referenci.

**P3. Reference nerozlišuje připuštěné promíchání a afinní permutace.** Platí

\[
P_0(S(x,y))=P_0(x,y),
\]

\[
P_0(D_Jx,D_Jy)=P_0(x,y),\qquad
P_0(ux,uy)=P_0(x,y). \tag{7}
\]

Příslušné amplitudové přechody a jejich pevný referenční kanál již byly výše sestrojeny. Tvrzení (7) o jejich výsledném čtení však zůstává výslovným předpokladem. Samotná lineární algebra nepředepisuje všechny přípustné funkce výsledků.

## 4. Věta: společný čtvercový zákon je určen až na kalibraci

**Věta.** Každé čtení splňující P1–P3 má pro jedno \(c\ge0\) přesně tvar

\[
\boxed{
(P_0,P_1,P_2)(x,y)
=\frac{(1,cq_+(x),cq_+(y))}
{1+c(q_+(x)+q_+(y))}.
} \tag{8}
\]

Pokud je alespoň jeden signál někdy zaznamenán s kladnou pravděpodobností, je \(c>0\). Jedna samostatná kalibrace určí zbývající \(c\). Nevyžaduje se spojitost, měřitelnost ani předpoklad mnohočlenného stupně.

**Důkaz.** Definujme přímo z binárních kalibrací

\[
f(x)=\frac{P_1(x,0)}{P_0(x,0)},\qquad
g(y)=\frac{P_2(0,y)}{P_0(0,y)}.
\]

Z P1 plyne \(f,g\ge0\), \(f(0)=g(0)=0\). Z P2 máme \(P_1=f(x)P_0\), \(P_2=g(y)P_0\). Normalizace tedy sama určí

\[
P_0=\frac1{1+f(x)+g(y)},\quad
P_1=\frac{f(x)}{1+f(x)+g(y)},\quad
P_2=\frac{g(y)}{1+f(x)+g(y)}. \tag{9}
\]

Oddělený součet zde není předem daným nepozorovaným účtem. Vznikl z kalibračních poměrů a ze společné normalizace tří výsledků.

První rovnost P3 a (9) dávají

\[
f\left(\frac{-3x+4y}{5}\right)
+g\left(\frac{4x+3y}{5}\right)=f(x)+g(y).
\]

Zesílená věta z `PROOF.md`, oddíl 2, nutí \(f=g\) a tuto společnou funkci nutí být kvadratickou formou. Její důkaz používá nezávislost smíšených druhých rozdílů na počátečním bodu; nezápornost odstraní lineární části. Žádná pravidelnost funkce se nedoplňuje.

Z afinních rovností P3 získáme po dosazení \(y=0\) invarianci \(f\) vůči \(D_J,u\); dosazení \(x=0\) dává totéž pro \(g\). Již dokázaná afinní jedinečnost proto určí \(f=g=cq_+\), \(c\ge0\). Dosazení do (9) dává (8). Naopak (8) splňuje P1–P3, protože \(q_+\) je kladně definitní, afinně invariantní a \(S\) zachovává součet dvou jeho hodnot. Tím je klasifikace úplná. □

## 5. Přesné testy pomocí součinů četností

Podmínka P2 nevyžaduje dělení malou pravděpodobností při samotném testování. Při P1 je ekvivalentní vymizení dvou výrazů

\[
\Delta_1(x,y)=
P_1(x,y)P_0(x,0)-P_0(x,y)P_1(x,0)=0,
\]

\[
\Delta_2(x,y)=
P_2(x,y)P_0(0,y)-P_0(x,y)P_2(0,y)=0. \tag{10}
\]

K nim patří přímo rozdílové testy (7), nulové signály z P1 a společná normalizace. Každá rovnost porovnává konkrétní přípravy a označené výsledky. Jediný přesný nenulový rozdíl vyvrací příslušnou podmínku modelu.

Při skutečném měření lze pravděpodobnosti nahradit odhady četností. Například čitatel odhadu \(\Delta_1\), po vynásobení oběma počty pokusů, je

\[
n_1(x,y)n_0(x,0)-n_0(x,y)n_1(x,0).
\]

Konečný naměřený čitatel nemusí být nulový ani při platném pravděpodobnostním zákonu. Výběr souboru příprav, počty pokusů a statistický práh by musely být určeny před měřením. Tento text žádná taková měření ani jejich výsledek nepředkládá. Konečný úspěšný seznam zkoušek také nenahrazuje předpoklad všech racionálních vstupů použitý ve větě.

## 6. Binárnost a slučování výsledků čtvrtý stupeň nevylučují

Položme \(a=q_+(x)\), \(b=q_+(y)\), \(Q=a+b\). Pro \(Q>0\) definujme

\[
P_0=\frac1{1+Q^2},\qquad
P_1=\frac{aQ}{1+Q^2},\qquad
P_2=\frac{bQ}{1+Q^2},
\]

a při \(Q=0\) položme \((P_0,P_1,P_2)=(1,0,0)\).

To je platné nezáporné rozdělení tří výlučných výsledků. Prázdný signál má nulovou pravděpodobnost. Všechny obyčejné operace slučování výsledků jsou dány součtem jejich pravděpodobností. Reference je invariantní při \(S\) i při afinním působení, protože oba přechody zachovávají \(Q\).

Samostatná binární kalibrace však dává

\[
\frac{P_1(x,0)}{P_0(x,0)}=q_+(x)^2.
\]

Podmínka P2 selže: pro nenulová \(x,y\)

\[
\Delta_1(x,y)
=\frac{ab}{(1+(a+b)^2)(1+a^2)}>0.
\]

Stačí konečný přesný příklad \(x=y=1\), kde \(q_+(1)=2\):

\[
(P_0,P_1,P_2)(1,1)=\frac{(1,8,8)}{17},
\qquad (P_0,P_1)(1,0)=\frac{(1,4)}5,
\]

\[
\Delta_1(1,1)=\frac4{85}.
\]

Tento příklad splňuje P1 a P3, ale nikoli P2. Dokazuje, že shoda s vyřazenou kalibrací je skutečným omezením navíc, nikoli jiným názvem pro binárnost nebo běžná pravidla pravděpodobnosti.

Platí i opačné oddělení podmínek. Rozdělení

\[
(P_0,P_1,P_2)(x,y)=\frac{(1,a^2,b^2)}{1+a^2+b^2}
\]

splňuje P1, P2 i afinní část P3, protože jeho kalibrační poměry jsou kontextově nezávislé \(a^2\) a \(b^2\). Nezachovává však referenční pravděpodobnost při \(S\). Pro \(y=0\) a \(x\ne0\) je před promícháním \(a^2+b^2=a^2\), kdežto po promíchání

\[
q_+(-3x/5)^2+q_+(4x/5)^2
=\left(\frac{81}{625}+\frac{256}{625}\right)a^2
=\frac{337}{625}a^2.
\]

Proto se \(P_0\) změní. Podmínka P2 a dynamická část P3 jsou tedy dvě nezávislá omezení; ani jedna nenahrazuje druhou.

Obecně lze v jednom kontextu rozdělit libovolnou celkovou nezápornou váhu \(H(Q)\) mezi disjunktní události jako \(H(Q)a_i/Q\). Uvnitř tohoto kontextu se váhy přesně sčítají a zachovávají všechna zpřesnění s týmž \(Q\). Teprve srovnání téže události napříč přípravami s jiným \(Q\) odhalí závislost na ostatních kanálech. Samotné zpřesňování výsledků v jediném experimentu tuto volnost neodstraní.

## 7. Co normalizované výsledky stále neurčují

Věta určuje referenčně kalibrované poměry \(f,g\). Neurčuje každou možnou nenormalizovanou fyzikální intenzitu nebo energii.

Pro libovolnou kladnou funkci \(\lambda(x,y)\) mají totiž váhy

\[
\bigl(\lambda(x,y),
\lambda(x,y)cq_+(x),
\lambda(x,y)cq_+(y)\bigr)
\]

po normalizaci přesně stejné pravděpodobnosti (8). Volba \(\lambda=H(q_+(x)+q_+(y))>0\) může navíc zachovávat obě skupiny přechodů. Ani P1–P3 tuto společnou násobnou volnost nenormalizovaných vah nerozliší.

Konstantní referenční amplituda \(k_0\) ještě sama neprokazuje, že každý myslitelný absolutní měřič má konstantní odezvu referenčního kanálu nezávisle na zbytku přípravy. Takové ztotožnění by vyžadovalo další přístrojovou nebo absolutně kalibrační podmínku. Nelze je získat jen z normalizovaných poměrů.

Jiná situace by nastala, kdyby bylo již nezávisle dáno, že každému kanálu přísluší stejná kontextově nezávislá surová odezva \(h(q_+(x))\). Shoda všech jejích normalizovaných poměrů s Bornovým poměrem by pak vůči jednomu pevnému nenulovému referenčnímu vstupu přímo vynutila \(h(t)=ct\) na všech dosažitelných hodnotách. Právě nezávislost této surové odezvy na ostatních kanálech je však dodatečným předpokladem, který se v obecné násobné rodině výše neuplatňuje.

## 8. Kalibrace poskytovaná existující metrikou

Pokud se navíc přijme čtení pomocí tří navzájem kolmých projektorů pro přímý součet pěti kopií metriky \(L\), mají na celočíselném kódu referenční složka a oba signálové bloky váhy

\[
160D^2,\qquad
\frac{64}{5}D^2q_+(x),\qquad
\frac{64}{5}D^2q_+(y).
\]

Po vydělení referenční vahou je tedy

\[
\boxed{c=\frac{2}{25}.}
\]

Tato hodnota není vložena do důkazu výběrové věty. Je to zvláštní kalibrace nabízená projektorovým rozkladem přesně dané metriky, nikoli normalizací celého buněčného účtu. Bez přijetí této vazby zůstává \(c\) určeno samostatnou kalibrací. Rozdíl mezi referenční normovou vahou \(160D^2\) a pevným členem buněčného účtu \(165D^2\) je záměrný: zbývajících \(5D^2\) účtuje zápis pěti jmenovatelů a není automaticky vahou žádného detekčního výsledku.

Nový uzavřený výsledek je tedy přesný: **slučitelné vyřazování výsledků vůči společné referenci, její invariance při již dostupných přechodech a nezápornost určují společné čtvercové poměry bez předpokladu čtvercového stupně.** Který skutečný přístroj tuto slučitelnost a tyto četnosti realizuje, tím ještě odvozeno není.
