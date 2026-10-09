# Společný reziduální krok a dva jednorázové záznamy

NON-CANONICAL, L1. Návrh samostatného přezkumu
P-RESIDUAL-RECORD-COMPOSITION-1 pro případné pozdější veřejné v100.
Tento dokument není Canon fold, přijetí závislostí ani výsledek formálního běhu.
Verze spojovacího kontraktu: V100-JOIN-1.

## 1. Závislosti a deklarované vstupy

Veřejný základ je Public Canon v99, commit
68080edc12faf029de48181f0a384f66e42dbc04. Z něj se přebírají původní mapy,
pístové čtení C a pevné matice M, B_read, L5. K přezkumu se předkládají
dvě samostatné kandidátní závislosti:

1. P-CONTACT-RECORD-1, beze změny jejího vlastního rozsahu: úplný K_i,
   čtečka Ucal_i, její inverze, jednorázová reference a listová ochrana r_x².
2. P-ALG-CONTACT-REALIZATION-1, verze CW-ALG-1: přesná gramatika s předností
   maker, algebraická Pi_alg, její konečný překlad a úplné q-zvednutí.

Jejich veřejné návrhy a obsahové piny uvádí README.md. Odkaz na návrh
neznamená jeho přijetí. Přijetí obou závislostí a tohoto spojení musí být
zaznamenáno odděleně před společným foldem.

Výslovně se dodávají W_a,W_b, vazby Ucal_x,Ucal_y, počáteční příprava
r_x=r_y=eta=0 a pevná matematická čtení. To je deklarované rozšíření
architektury, nikoli odvození těchto rozhraní z původního autonomního U.
V tomto dokumentu se žádná nová brána, buňka, registr, reset, čítač ani
fyzická implementace těchto vstupů nezavádí. Pomocné symboly ve formulích
jsou označení existujících souřadnic nebo konstrukce pevného slova.

## 2. Úplný nosič a cílová rovnost

Všechny pětistavové souřadnice leží v F5, eta v {0,1}. Úplný nosič je

    X = F5^12 × {0,1}; z=(p_x,q_x,r_x; p_y,q_y,r_y; eta).

Každý píst p_i je čtveřice, jako matice 2×2 se čte po řádcích.
Nosič má 488281250 stavů. Pišme f=(p_x,p_y,r_x,r_y,eta), q=(q_x,q_y)^T.
Faktor rho zapomíná právě q; žádná z povolených bran kompilátoru nečte q
do tohoto faktoru. Čtečky Ucal_i toto rozhraní rozšiřují výslovně.

\[
G(p)=(\alpha,\beta,\gamma)
=(\det X_p,\tfrac12[\det(X_p+Y_p)-\det X_p-\det Y_p],\det Y_p),
\quad \delta(g)=1-\beta^4.
\]
\[
M=\begin{pmatrix}0&3&0\\4&4&4\\0&3&3\end{pmatrix},\quad
B_{\rm read}=\begin{pmatrix}1&4&2\\4&0&1\\3&4&4\end{pmatrix},\quad
L_5=\begin{pmatrix}3&3&2\\3&4&2\\3&2&0\end{pmatrix}.
\]

Pevné čtení je D_C=B_read G a B_read M=L5 B_read. Cílem není volba nové
matice podle výstupu, nýbrž uskutečnění tohoto již pevného reziduálního kroku.

## 3. Převzaté úplné mapy a přesně zvolený překlad

P-CONTACT-RECORD-1 dává dvanáctilistý K_i:

\[
K_i(f,q)=(f,q+3\delta(Gf)e_i).
\]

Její pevná tabulka P_q na r=0,1,2,3,4 je

| q | Obrazy r=0,1,2,3,4 |
|---|---|
| 0 | 0,2,1,3,4 |
| 1 | 0,1,2,3,4 |
| 2 | 2,1,0,3,4 |
| 3 | 1,0,2,3,4 |
| 4 | 1,0,2,3,4 |

Ucal_i provádí jen r_i↦P_(q_i)(r_i). Z involutivity P_q plyne na celém X

\[
\mathcal A_i=\mathcal U_iK_i\mathcal U_i:
\quad q_i'=q_i+3d,\quad r_i'=P_{q_i+3d}P_{q_i}(r_i),\quad d=\delta(Gf).
\tag{1}
\]

Na konci jsou ostatní souřadnice totožné. Pro každý q a d=0,1 platí
P_(q+3d)P_q(0)=d. Žádné rozdělení pravděpodobnosti na q se nepředpokládá.

Použije se právě algebraická Pi_alg z CW-ALG-1, ne původní lexikografická Pi.
Její pístová/bitová část R je nezávislá na r a na celém faktoru platí

\[
\Pi_{\rm alg}(p,r,\eta)=(R(p,\eta),r).
\]

Slovo je pevně

\[
T_{\rm alg}=\operatorname{Expand}(\operatorname{CW\!\text{-}\!ALG\!\text{-}\!1}
(\Pi_{\rm alg})).
\tag{2}
\]

Rozhoduje explicitní přednost maker a syntaktické konvence verze CW-ALG-1.
Faktorově ekvivalentní náhrady, zkrácené zapisovače a samostatná kompilace
inverzní faktorové permutace se za totéž úplné slovo nepokládají.
Příslušné úplné zvednutí má tvar

\[
T_{\rm alg}(f,q)=(\Pi_{\rm alg}f,H_fq),\qquad H_f\in GL_2(F5).
\tag{3}
\]

H_f je určeno gramatikou a skutečnou faktorovou trajektorií; není novým
volitelným vstupem a netvrdí se H_f=I. Inverze je ReverseInvert téhož slova.
Referenční implementace Pi_alg ani kontrola jejích souřadnic toto slovo
nevykonávají. Jeho obrovská expanze není součástí navrženého ověřování.

## 4. Spojovací věta na celém nosiči

Definujme pevné slovo V=A_y T_alg A_x. Následující popis je úplná mapa,
včetně obsazených r a obou vstupních bitů:

\[
\begin{aligned}
d_0&=\delta(Gp),&u&=q+3d_0e_x,&\widehat r_x&=P_{u_x}P_{q_x}(r_x),\\
f_x&=(p,\widehat r_x,r_y,\eta),&f_2&=\Pi_{\rm alg}f_x,&v&=H_{f_x}u,\\
d_1&=\delta(Gf_2),&q'&=v+3d_1e_y,&r_y'&=P_{v_y+3d_1}P_{v_y}(r_y).
\end{aligned}
\tag{4}
\]

Výstup má písty a bit z f_2 a r_x'=rhat_x. Druhá čtečka dostává celý
skutečný výstup T_alg. V (4) se žádný mezistav nenahrazuje čistou referencí.

Pro jedinou počáteční množinu

\[
S_0=\{r_x=r_y=\eta=0\},\qquad |S_0|=5^{10}=9765625
\]

platí pro libovolné písty a q hlavní věta

\[
\boxed{G(Vz)=MG(z),\quad D_C(Vz)=L_5D_C(z),\quad
(r_x',r_y')=(\delta(g),\delta(Mg)).}
\tag{5}
\]

Důkaz: první použití tabulkové identity z (1) dá rx=delta(g), ry=0.
Eta zůstala 0, takže zaručená doména Pi_alg obsahuje tento skutečný stav.
Krok (2) změní G na MG a vrátí obě r podle globálního kontraktu (3).
Poslední použití tabulkové identity platí pro každou hodnotu v_y, kterou
slovo skutečně předalo, a dává ry=delta(Mg). Rovnost D_C plyne z pevné
maticové identity. Konkrétně delta(Mg)=1-(alpha+beta+gamma)^4.

Úplná inverze, nikoli druhé stejné použití, je

\[
V^{-1}=\mathcal A_x^{-1}T_{\rm alg}^{-1}\mathcal A_y^{-1},\quad
\mathcal A_i^{-1}=\mathcal U_iK_i^{-1}\mathcal U_i.
\tag{6}
\]

Čtečka se invertuje pomocí d z nezměněných pístů:

\[
q_i=q_i'-3d,\qquad r_i=P_{q_i'-3d}P_{q_i'}(r_i').
\]

Pro prostřední slovo z f',q' nejprve obnovíme f=Pi_alg^-1(f') a potom
q=H_f^-1 q'. V (6) se tak nejprve vrátí druhá čtečka, poté totožné
kompilované slovo v opačném pořadí a nakonec první čtečka. Obnoví se
všechny původní souřadnice, nejen čtení nebo počáteční nuly.

## 5. Přesný obraz přípravy a doména pokračování

Veřejně přezkoumávaný atlas CW-ALG-1 pro g≠0 užívá

\[
\kappa(g)=\beta^2-\alpha\gamma,\quad
m(0)=5,\quad m(1)=m(4)=6,\quad m(2)=m(3)=4,
\quad\ell=j+m(\kappa(g))\eta.
\]

Maximální šířka orbity m_*(g) je 5 pro g=s(2,1,3), s≠0, jinak 6.
Přesný T_alg-dosah celé vrstvy eta=0 s libovolnými r,q je

\[
\Omega_{\rm alg}=\{g=0,\eta=0\}\cup
\{g\ne0,\ell<m_*(g)\},\qquad |\Omega_{\rm alg}|=281640625.
\tag{7}
\]

Každý aktivní cyklus navštíví vlákno maximální šířky a tam leží jeho slot
v bitu 0. To dokazuje přesnou dosažitelnost (7) pro T_alg. S libovolnými q
na počátku zůstávají příslušná q-vlákna úplná díky jejich bijektivitě.
Ze S_0 má samotné T_alg dosah Omega_alg∩{rx=ry=0}, velikosti 11265625.

Čtečky zachovávají písty a bit na konci; Pi_alg zachovává (7) v obou směrech.
Proto V(Omega_alg)=Omega_alg a na této doméně pro každé n≥0 platí

\[
G(V^nz)=M^nG(z),\qquad D_C(V^nz)=L_5^nD_C(z).
\tag{8}
\]

Toto je invariantní doména pokračování čtené dynamiky, bez resetu eta.
Není to tvrzení o nových připravených záznamech při každém opakování.

Přesný jednoprůchodový obraz S_1=V(S_0) má libovolné q' a

\[
r_x'=\delta(M^{-1}g'),\qquad r_y'=\delta(g'),\qquad g'=G(p').
\tag{9}
\]

Pro g'=0 je eta'=0 (a oba záznamy 1). Pro g'≠0 platí přesně

\[
\ell'=j'+m(\kappa(g'))\eta'<m(\kappa(M^{-1}g')).
\tag{10}
\]

Podmínka (10) je na nenulovém vláknu ekvivalentní eta(R^-1(p',eta'))=0.
Spolu se záznamovými podmínkami (9) a uvedeným pravidlem pro nulové vlákno
jsou tyto podmínky nutné i postačující, aby inverze (6) obnovila stav S_0.
Libovolné q' má jediný
předobraz, protože (3) a translace q jsou bijekce na celém q-vlákně.
Proto |S_1|=|S_0|=9765625.

Po A_x(S_0) je rx=delta(g), ry=0, eta=0 a q libovolné. Po T_alg A_x(S_0)
platí stejné pístové/bitové podmínky (10), rx z (9), ale ry=0; q je stále
libovolné. To jsou přesné rozhraní tří částí, nikoli vybrané ukázky.

Skutečný opakovaný dosah V ze S_0 je union_{n≥0} V^n(S_0). Netvrdíme jeho
rovnost s (7): dokončené makrokroky zachovávají rx,ry∈{0,1,2}, zatímco
(7) připouští i 3,4. Uvnitř skutečných slov se stále používá celý nosič X.
Pevnost doplňku Pi_alg se nepřenáší na V, protože tam mohou působit čtečky.

## 6. Obnova prvního záznamu a jednorázový význam

Globální rovnost r_i T_alg=r_i platí také pro obsazené r. Proto po
dokončení prostředního slova pro z∈S_0 přesně

\[
r_x(T_{\rm alg}\mathcal A_xz)=\delta(g),\quad
r_x^2(T_{\rm alg}\mathcal A_xz)=\delta(g).
\tag{11}
\]

To je obnova syrového registru na rozhraní slova. Invariance r_x² po každém
vnitřním listu T_alg se netvrdí. Písty/r mohou uvnitř sloužit jako obsazené
vratné pracovní souřadnice; konstrukční důkaz jejich čistotu nepotřebuje.

P-CONTACT-RECORD-1 samostatně dokazuje, že každý list A_y mění rx pouze
znaménkem nebo jej ponechá. Pro každý prefix V_k tohoto konkrétního
druhého slova a z∈S_0 tedy

\[
r_x^2(V_kT_{\rm alg}\mathcal A_xz)=\delta(g).
\tag{12}
\]

Dvojice v (5) má výslovně jednorázový význam při jedné přípravě S_0.
Opakování V může přepisovat již obsazené reference; (8) mu nepřiděluje
čerstvou dvojici delta(g),delta(Mg). Nezavádí se archiv ani mezilehlý reset.
Samotná nulová hodnota záznamu nepotvrzuje dokončení: zachovává se původní
hranice nerozlišitelnosti nepoužitého a dokončeného nulového experimentu.
Není dokázán fyzický detektor, autonomní U ani nový status otevřeného vlastníka.

## 7. Přezkumná a veřejná hranice

Přezkum musí samostatně přijmout úplný kontrakt (1), přesnou verzi gramatiky
(2) včetně přednosti maker a zvednutí (3), a teprve potom spojení (4)–(12).
Kompilátorová univerzalita působí na faktoru; nepředstírá alternující grupu
celého X. Žádná kontrola referenční mapy není označena za provedení (2).

Veřejný formální pin, vlastní běh a přezkum každé potřebné sondy zůstávají
samostatné povinnosti. Tento návrh nemění Canon, registr, FRONTIER,
QUADRATIC-MEMORY-NATIVE-CONTACT ani fyzické vlastníky. Společné v100 je
možné až po doloženém přijetí obou důkazních závislostí a spojovacího
kontraktu v přesném rozsahu potřebném zde. Podmíněný architekturní důkaz
sám fyzický status otevřených vlastníků nezvyšuje ani nevyžaduje jejich
uzavření jako podmínku této podmíněné L1 věty.
