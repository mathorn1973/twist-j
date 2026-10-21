# Spojení energetického přístroje s celým spektrem W

**Výsledek:** skutečné kontaktní W má společnou spektrální mezeru.
Existuje jeho přesný samosdružený logaritmus s exponenciálně slábnoucími
prostorovými vazbami. K této energii lze připojit spojitou baterii
s konečnou kladnou energetickou kapacitou, která přesně zachovává
celkovou energii a provede původní impulz s řízenou chybou. Konstrukce
zahrnuje celý spektrální prostor W, skutečné konečné přípravy a
pohyblivou referenci nesoucí druhou kopii stejného W.

Současně je prokázáno, že ani exponenciální útlum vazeb spolu s energií
vázané větve nevybere jediný logaritmus. Různé přípustné energie mění
práci impulzu již v jeho hlavním kvadratickém členu.

Status: LOCAL / NON-CANONICAL / NEW_DECLARED / L1. Jde o matematickou
konstrukci pro přesně deklarovaný kontakt, nikoli odvození přístroje
z původního nativního U nebo identifikaci známé fyzikální částice.
Zastaralé přílohy se v tomto pokračování nepoužívají. Jednotky mají
jeden tik a hbar rovné jedné; fyzikální kalibrace není nově odvozena.

## 1. Pevné W

Na prostoru \(\ell^2(\mathbb Z_R\times\mathbb Z_r)\otimes\mathbb C^4\)
platí

\[
W=\Gamma SG,\qquad
G=\frac{(I+2iX)\otimes(I+2iX)}5,\qquad
\Gamma=e^{-igP_0},\qquad g=\frac{2\pi}{5}.
\]

\(P_0\) je projekce na relativní souřadnici \(r=0\). Kontakt působí
po proudění. Ve Fourierově konvenci původního důkazu má volný krok symbol

\[
W_f(P,q)=\operatorname{diag}(e^{iP},e^{iq},e^{-iq},e^{-iP})G.
\]

Původní jednoduchá vázaná větev u klidu splňuje

\[
W(P)\chi_P=e^{-i\Omega(P)}\chi_P,\qquad
\Omega(0)=g,\qquad
\Omega''(0)=\kappa=\frac{\sqrt{16\phi+7}}{20},
\quad \phi=\frac{1+\sqrt5}{2}.
\]

To jsou stejné operátory a stejná větev jako v předchozí konstrukci.
Nově se řeší jejich celé spektrum a skutečné energetické napojení.

## 2. Globální mezera opravdu existuje

Jednočásticový volný krok má fáze \(\pm\theta(k)\), kde

\[
\cos\theta(k)=\frac{\cos k}{\sqrt5},\qquad
\theta(k)\in[\arctan2,\pi-\arctan2].
\]

Zde arctan2 znamená \(\arctan(2)\). Součty a rozdíly těchto úhlů dávají
přesné volné spektrum

\[
\sigma(W_f)=
\{e^{i\varphi}:\varphi\in[-b,b]\cup[\pi-b,\pi+b]\},
\qquad b=2\arctan(1/2).
\tag{1}
\]

Proměnné \(k_1=(P+q)/2,\ k_2=(P-q)/2\) pokrývají potřebné produkty:
společný posun obou \(k_j\) o \(\pi\) obrátí obě jednočásticové matice
znaménkem a jejich součin zachová.

Rozhodující odhad kontaktu je

\[
\|e^{ig/2}W-W_f\|=2\sin(g/4).
\tag{2}
\]

Vyplývá přímo ze dvou vlastních hodnot kontaktní projekce. Resolventa
normálního \(W_f\) potom umístí spektrum \(e^{ig/2}W\) do chordového
okolí volných oblouků; na kružnici jde o úhlové rozšíření nejvýše
\(g/2\). Po otočení zpět:

\[
\boxed{\quad
\sigma(W)\subseteq
\{e^{i\varphi}:\varphi\in[-b-g,b]\cup[\pi-b-g,\pi+b]\}.
\quad}
\tag{3}
\]

Je to inkluze celého nekonečného kontaktního operátoru. Není nutná
konečná matice, odhad z několika hybností ani předpoklad o pokračování
vázané větve. Rovnost s oběma obalovými oblouky se netvrdí.

Mezi oblouky zůstávají dvě mezery, každá o zaručené šířce

\[
\Delta_{\rm gap}=\arccos(7/25)-\frac{2\pi}{5}>0.
\tag{4}
\]

Kladnost je přesná:

\[
\cos(2\pi/5)=\frac{\sqrt5-1}{4}>\frac7{25},
\qquad
5-\left(\frac{53}{25}\right)^2=\frac{316}{625}>0.
\]

Středy bezpečných řezů v argumentu vlastní hodnoty jsou
\(3\pi/10\) a \(-7\pi/10\).

## 3. Energie celého spektra a její prostorové vazby

Zvolíme \(\alpha=3\pi/10\) a argument logaritmu v intervalu
\((\alpha-2\pi,\alpha)\). Definice

\[
\boxed{H=i\operatorname{Log}_{\alpha}W,\qquad e^{-iH}=W}
\tag{5}
\]

je přesná na celém prostoru. Na vázané větvi dává energii \(\Omega(P)\),
včetně \(g\) v klidu. Spektrum \(H\) leží uvnitř
\((-3\pi/10,17\pi/10)\).

Analytický funkční počet a konečný dosah W dávají exponenciální
prostorový útlum H v obou původních souřadnicích:

\[
\|1_{d(x,F)\ge \ell}H\psi\|
\le C_0e^{-\mu\ell}\|\psi\|,
\qquad \operatorname{supp}\psi\subset F.
\tag{6}
\]

V přiloženém důkazu jsou explicitní kontura a konstanty \(C_0,\mu>0\).
Zachovává se dřívější zákaz přesně konečného dosahu generátoru.
Exponenciálně slábnoucí vazby zůstávají přítomné i na velké vzdálenosti.

Pro skutečný impulz \(V_\eta=e^{i\eta R}\) navíc platí globální odhad

\[
\|V_\eta^\dagger HV_\eta-H\|
\le 2C_H|\sin(\eta/2)|\le C_H|\eta|,
\tag{7}
\]

\[
C_H=\csc^2(\omega/2),\qquad
\omega=\frac{\arccos(7/25)-2\pi/5}{2}>0.
\]

Konstanta je konzervativní. Důkaz používá Cayleyův převod a přímo
dokázanou operátorovou mez pro arctan. Neopírá se o nesprávnou domněnku,
že \(\|e^{i\eta R}-I\|\) je na celém nekonečném prostoru malá.

## 4. Reference dostává vlastní W a vlastní energii

Systém rozšíříme o druhou kopii stejného kontaktu, se souřadnicemi \(Y,s\):

\[
W_{\rm pair}=W_R\otimes W_Y,\qquad
H_{\rm pair}=H_R\otimes I+I\otimes H_Y.
\]

Zásah je nyní

\[
V_\eta=e^{i\eta(R-Y)}.
\tag{8}
\]

Posune první hybnost o \(+\eta\) a druhou o \(-\eta\), přesně modulo
\(2\pi\). S celkovou translací obou těžišť komutují H i V; stejnou
symetrii zachová energetický přístroj níže.

Pro bateriovou souřadnici pouze posuneme počátek energie:

\[
H_S=H_{\rm pair}+2\alpha I,\qquad 0\le H_S\le hI,\qquad h=4\pi.
\tag{9}
\]

Konstantní posun nemění práci, komutátory ani zákon zachování.
Při exponentiaci vznikne známá globální fáze \(e^{-2i\alpha}\);
přesnou rovnost s \(W_{\rm pair}\) má původní \(H_{\rm pair}\).

Pohyblivá reference tedy není nezapočtená značka s nulovou energií.
Samotné předepsání opačných impulzů ovšem neodvozuje zákon vzájemné
síly mezi tělesy.

## 5. Přístroj přijímá přesně všechny energetické rozdíly

Obecně předpokládejme \(0\le H_S\le h\) a požadovaný unitární zásah V.
Baterie šířky L má prostor a energii

\[
\mathcal H_B=L^2([0,A],de),\qquad
(H_Bb)(e)=e\,b(e),\qquad A=L+2h.
\tag{10}
\]

Její kapacita je konečná a energie nezáporná. Její Hilbertův prostor
má nekonečný rozměr a její spektrum je spojité. Tento přídavný zdroj
umožňuje přijímat nesouměřitelné rozdíly původních energií bez jejich
zaokrouhlení.

V souřadnici celkové energie \(t=E+e\) je systémové vlákno

\[
\mathcal H_t=
1_{[\max(0,t-A),\,\min(h,t)]}(H_S)\mathcal H_S.
\]

Pro \(h\le t\le A\) obsahuje všechny systémové energie, tedy celý
\(\mathcal H_S\). Zde použijeme V, na zbývajících vláknech identitu:

\[
\mathcal U_t=
\begin{cases}
V,&h\le t\le A,\\
I_{\mathcal H_t},&\text{jinak}.
\end{cases}
\tag{11}
\]

To definuje unitární operátor na celém společném prostoru a přesně
splňuje

\[
\boxed{
\mathcal U^\dagger(H_S+H_B)\mathcal U=H_S+H_B.
}
\tag{12}
\]

Při spektrálním přechodu \(E\to E'\) změní baterie svou energii
o \(E-E'\). Obecný důkaz je přímointegrální a zahrnuje bodové,
absolutně spojité i singulárně spojité spektrum. Symbolické vlastní
energie v této větě nepředpokládají normalizovatelné ostré vlastní stavy.

Počáteční baterie, stejná pro všechny neznámé vstupy, je

\[
b_L(e)=
\sqrt{\frac2L}\sin\frac{\pi(e-h)}L
\quad(h\le e\le h+L),
\qquad b_L(e)=0\ \text{jinde}.
\tag{13}
\]

Má normu jedna, střední energii \(h+L/2\) a
\(\|b_L'\|_2=\pi/L\). Všechny její připravené vstupy mají
\(t\in[h,A]\), takže operace vždy působí v plném vlákně. Po zásahu
zůstává baterie uvnitř \([0,A]\). Žádný hraniční výsledek se nevyhazuje.

Obecná myšlenka operace po sektorech celkové energie a široké
koherentní baterie je známá. Konstrukce Chiribelly, Yanga a Rennera
pracuje ve své explicitní horní mezi s konečně mnoha stejně vzdálenými
hladinami. Přechod k celému spojitému spektru zde dokazuje oddělený
přímointegrální argument:
https://arxiv.org/html/1908.10884v3 .

## 6. Přesné zachování energie, kontrolovaná chyba zásahu

Definujme skutečnou změnu systémové energie

\[
D=V^\dagger H_SV-H_S,\qquad a_D=\operatorname{osc}(D).
\]

Pro každý normalizovaný vstup, také propletený s pomocnou testovací
referencí, je chyba společného stavu omezena

\[
\|\mathcal U(\psi\otimes b_L)-(V\psi)\otimes b_L\|
\le\frac{\pi\|D\|}{L}.
\tag{14}
\]

Baterie se nemusí přesně vrátit do původního stavu. Skutečné malé
korelace nesou energetickou výměnu. Její účet je přesně

\[
\Delta\langle H_B\rangle=-\Delta\langle H_S\rangle.
\tag{15}
\]

Reálnost bateriové vlny ruší první člen chyby redukované operace.
Pro půldiamantovou vzdálenost d, která kontroluje i propletené vstupy,
a nejhorší infidelitu \(\varepsilon\) platí

\[
d\le\frac{\pi^2h\,a_D}{2L^2},
\qquad
\varepsilon\le\frac{\pi^2\|D\|^2}{L^2}.
\tag{16}
\]

Hodnoty lze vždy omezit také jedničkou. Pro práci je důležitý zvláštní
odhad

\[
\left|\mathcal W_{\rm skutečná}-\operatorname{Tr}(D\rho)\right|
\le\frac{\pi^2h^2a_D}{4L^2}.
\tag{17}
\]

Tyto meze vyplývají z Fourierova rozkladu baterie a druhého Taylorova
zbytku. Dokázána je přibližná realizace V s přesnou konzervací energie.
Přesná univerzální nekomutující operace s normalizovanou baterií by
odporovala známé WAY větě:
https://arxiv.org/html/2208.13494v3 .

## 7. Napojení na původní odezvu

Ponecháme původní posloupnost

\[
q=5^\ell,\qquad \eta_q=2\arctan(1/q),\qquad N=q^4,\qquad T=q,
\]

a přidáme \(L=q\). Vstupy obou kopií jsou původní konečné binomické
vektory

\[
\psi_N(R,r)=
\frac{\binom{2N}{N+R}\delta_{r0}}
{\sqrt{2\binom{4N}{2N}}}(1,0,0,-1).
\]

Nikde se nepromítají na ideální vázanou větev. Globální odhad (7)
dává pro dvojici \(\|D_{\eta_q}\|=O(q^{-1})\), a tudíž:

| Veličina | Dokázaný řád |
|---|---|
| Chyba společného stavu | \(O(q^{-2})=o(\eta_q)\) |
| Nejhorší infidelita | \(O(q^{-4})\) |
| Chyba redukované operace | \(O(q^{-3})\) |
| Chyba práce proti skutečnému cílovému D | \(O(q^{-3})=o(\eta_q^2)\) |
| Kapacita baterie | \(q+8\pi\) |
| Počáteční střední energie baterie | \(q/2+4\pi\) |

Konstanty jsou explicitní, ale konzervativní. Z těchto asymptotických
mezí neplyne, že malé konkrétní q již poskytuje prakticky přesný přístroj.

Následný volný vývoj chybu stavu nezvětšuje. Průměrný proud má normu
nejvýše jedna, takže jeho očekávání se změní nanejvýš o \(2d\).
Případný polohový posun během přístroje má navíc samostatný odhad
\(2\pi C_H/L\); po dělení \(T\eta_q\) mizí. Tím zůstává skutečný limit

\[
\boxed{
\frac{v_R}{\eta_q}\longrightarrow\kappa,\qquad
\frac{v_Y}{\eta_q}\longrightarrow-\kappa,\qquad
\frac{v_R-v_Y}{\eta_q}\longrightarrow2\kappa.
}
\tag{18}
\]

V lokální hybnostní souřadnici kolem klidu při \(P+Q=0\) je
\(p=(P-Q)/2\) sdružené s \(R-Y\). Relativní odezva proto dává

\[
\mu_{\rm rel}=\frac1{2\kappa}
=\frac{10}{\sqrt{16\phi+7}},
\]

zatímco jednotlivé těžiště má koeficient hmotnosti \(1/\kappa\).
Globální půlení hlavních úhlů na hybnostním toru se netvrdí.

## 8. Skutečná práce stále vyžaduje volbu energie

Holý impulz zachová původní vnitřní vektor, takže obecně nedává
nový vlastní vektor \(\chi_{P+\eta}\). Správná práce je tedy
\(\operatorname{Tr}(D_\eta\rho)\), včetně složky mimo vázanou větev.
Již u klidu platí

\[
\langle\chi_0,H''(0)\chi_0\rangle
=\kappa+
2\langle\chi'_0,(H(0)-g)\chi'_0\rangle.
\tag{19}
\]

Ještě silnější výsledek poskytují dvě globální spektrální mezery.
Položme

\[
A_W=\Re(e^{ig/2}W),\qquad P_-=1_{(-\infty,0)}(A_W).
\]

Projekce \(P_-\) na druhý spektrální shluk má sama exponenciální
prostorové chvosty. Pro každý pevný celý m je

\[
H_m=H+2\pi mP_-
\tag{20}
\]

přesný samosdružený logaritmus W s exponenciálně slábnoucími vazbami.
Všechny H_m mají stejnou energii blízké vázané větve i stejnou křivost.
Přesto mění práci stejného impulzu na jednom tělese o

\[
\mathcal W_m-\mathcal W_0
=2\pi m\beta_-\eta^2+o(\eta^2),
\qquad
\boxed{\beta_-\ge\frac{3(1+\sqrt5)}{80}>0.}
\tag{21}
\]

Dolní mez plyne z přesného očekávání
\(\langle s_0,A_W(0)s_0\rangle=-3\cos(g/2)/5\) a z resolventy
na druhém shluku. Platí také pro původní konečné binomické přípravy;
u dvou stejných opačně kopnutých těles se vedoucí rozdíl zdvojnásobí.

V tomto přístroji je výslovně zvoleno m=0. Samotné W, jeho odezvová
hmotnost ani exponenciální útlum vazeb tuto volbu nevynucují.

## 9. Co má a nemá vyřešenou prostorovou realizaci

Pro H je exponenciální útlum operátorová věta na celém prostoru.
Pro celý bateriový přístroj máme na určeném koherentním vstupu
malou odchylku od polohově diagonálního V a také prostorový odhad

\[
\|1_{d(x,F)\ge\ell}\mathcal U(\psi\otimes b_L)\|
\le e^{-\mu\ell/2}+\frac{4\pi K_\mu}{L\mu\ell}
\]

pro jedno těleso, s odpovídajícím součtem konstant pro dvě kopie.
Nevyplývá z toho uniformní konečný dosah celé \(\mathcal U\) na všech
bateriových stavech. Její ostré celkové energetické okraje a neomezená
Fourierova proměnná potřebují vlastní fyzickou realizaci.

Je možné dodat časově nezávislý generátor. Kladný omezený logaritmus
cílového V vložený do stejných plných vláken dává interakci K s
\([K,H_S+H_B]=0\) a

\[
H_{\rm tot}=H_S+H_B+K\ge0,\qquad
e^{-iH_{\rm tot}}=e^{-i(H_S+H_B)}\mathcal U.
\]

Interakční energie je explicitní a zachovává se samostatně. Po jednom
taktu vznikne zásah spolu s volným krokem W. Při dalším autonomním
vývoji se však zásah opakuje. Jednorázový protokol následovaný
volným W stále předpokládá vypnutí; vnitřní místní zastavovací hodiny
nejsou touto větou sestrojeny.

Dodané zdroje tedy zůstávají konkrétní: spojitý nekonečně rozměrný
bateriový registr, jeho koherentní příprava, spektrálně definovaná
interakce a volba energetické větve. Spojení se spektrem W je
provedeno přesně; sestavení celého aparátu z původní konečné
celočíselné abecedy nebylo prokázáno.

## 10. Ověření a čtení balíčku

Univerzální spektrální a energetické věty jsou dokázány analyticky a
nezávisle přezkoumány. Algebraické vstupy navíc prošly dvěma různými
přesnými programy: celý charakteristický Laurentův polynom byl
vypočten Leibnizovým determinantem a nezávisle Newtonovými identitami
ze stop mocnin. Obě první spuštění prošla; žádný vědecký neúspěšný
pokus nebyl odstraněn a nebyla potřebná oprava programu.

Certifikáty jsou shodné po bytech: 656 bytů, SHA-256
7bbf0e0e6546a79961f52fbc9de448b349c6d66fb79ef12b9a64c64f72579c48.
Oba běhy proběhly na Linux x86_64 s Pythonem 3.12.14.
Jiná architektura, veřejné CI ani přijetí do Canonu se netvrdí.
Samotná přesná algebraická kontrola nenahrazuje nekonečně rozměrné
důkazy.

Hlavní důkazy:

- agents/spectrum_locality/PROOF_GLOBAL_SPECTRUM_AND_LOCALITY.md
- agents/spectral_lift/SPECTRAL_APPARATUS.md
- PROOF_MOVING_REFERENCE_v2.md

Poslední v2 pouze výslovně zpřesňuje lokální souřadnici relativní
hybnosti; původní zmrazená verze i poznámka o upřesnění zůstávají
zachované. Podrobné nezávislé přezkumy, zadání kontroly, zdrojové
otisky a nezměněné první běhy jsou součástí téhož balíčku.
