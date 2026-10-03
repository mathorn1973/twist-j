# Konečná reference, uchovaná historie a dva J kontakty

**NON-CANONICAL — L1, candidate-T; analytický návrh, 2026-10-03.**
Následující důkazy platí v přijatém komplexním amplitudovém modelu.
Neodvozují tento nosič, přípravu reference ani jednotlivé výskyty z nativního U.
Neověřují implementaci nedodaného balíku ani jeho hlášené vědecké běhy.
Veřejnou autoritu nadále určuje [STATUS.md](../../STATUS.md).

<a id="p01"></a>

## P01 — Nosič a úplné energetické bloky

Nechť $\mathcal H_F=\mathbb C^5$, $P|q\rangle=|q+1\pmod5\rangle$,
$K_\pm=(I\pm P^2)/2$. Platí $\sum_bK_b^\dagger K_b=I$.
Projektivní kontext $d$ má úplnou rodinu ortogonálních projektorů
$\{\Pi_{d,m}\}_m$. Energie pole je

$$
H_F=2I-P-P^\dagger=aE_a+bE_b,\qquad
a=(5-\sqrt5)/2,\quad b=(5+\sqrt5)/2.
$$

Projektory $E_0,E_a,E_b$ mají hodnosti $1,2,2$, součet $I$
a indexy $v_0=(0,0),v_a=(1,0),v_b=(0,1)$.
Reference má bázi $|i,j\rangle$, $0\le i,j\le2N$, a energii
$H_R|i,j\rangle=(ai+bj)|i,j\rangle$. Všechny další registry shrnuje
$\mathcal H_C$ s účtem $H_C$. Ideální unitární hradla $W$ působí
na $F,C$ a musí splňovat $[W,H_C]=0$; nemusejí komutovat s $H_F$.

Pro $t\in\{1,\ldots,2N\}^2$ definujme izometrii

$$
J_t\psi=\sum_{s\in\{0,a,b\}}(E_s\otimes I_C)\psi
                \otimes|t-v_s\rangle_R.
$$

Její obraz je úplný blok: obsahuje všechny sektory pole při stejném
$H_F+H_R=at_1+bt_2$. Obrazy různých $t$ jsou ortogonální.
Položme $P_{\rm full}=\sum_tJ_tJ_t^\dagger$. Na tomto prostoru je
lineární lift libovolného operátoru $A$ definován jako

$$
\mathcal L_0(A)=\sum_tJ_tAJ_t^\dagger.
$$

Z $J_t^\dagger J_u=\delta_{tu}I$ bezprostředně plyne
$\mathcal L_0(A_2)\mathcal L_0(A_1)=\mathcal L_0(A_2A_1)$.
Pro unitární hradlo použijeme úplné rozšíření

$$
\widehat W=\mathcal L_0(W)+(I-P_{\rm full}).
$$

Tento operátor je unitární, zachovává $H_F+H_R+H_C$ a splňuje
$\widehat W_2\widehat W_1=\widehat{W_2W_1}$.
Případné další degenerace celkové energie nevadí: konstrukce zachovává
jemnější rozklad na uvedené bloky i účet $H_C$ zvlášť.

Počáteční podpora reference $1\le i,j\le2N-1$ zajistí, že každý
vstup pole leží v $P_{\rm full}$. Všechna hradla jej tam zachovají.
Nulový větvový operátor má proto nulovou amplitudu na dosažitelných stavech;
nesmí se zaměnit s identitním doplněním unitárních hradel na okraji.

<a id="p02"></a>

## P02 — Trojúhelníkový profil a jeho překryv

Pro $N\ge1$ položme $c_i=\min(i,2N-i)$ pro $1\le i<2N$
a $c_i=0$ mimo tuto podporu. Potom

$$
S_N=\sum_i c_i^2=N^2+2\sum_{i=1}^{N-1}i^2
    =\frac{N(2N^2+1)}3,\qquad
\chi_N=\frac1{\sqrt{S_N}}\sum_i c_i|i\rangle,
\quad\eta_N=\chi_N\otimes\chi_N.
$$

Právě $2N$ sousedních rozdílů $c_i-c_{i-1}$ má čtverec jedna.
Rozvinutí součtu jejich čtverců dává
$2N=2S_N-2\sum_i c_ic_{i-1}$. Překryv s jednotkovým posunem je tedy

$$
r_N=\langle\chi_N,S_1\chi_N\rangle
   =1-\frac{N}{S_N}=1-\frac3{2N^2+1}.
$$

Součinový profil má překryv $r_N$ při posunu v jedné ose a $r_N^2$
při posunu $(1,-1)$. Symetrie kolem $N$ dává
$\langle H_R\rangle=(a+b)N=5N$; rozměr reference je $(2N+1)^2$.
Rovnoměrný profil na téže podpoře má stejný rozměr i střední energii, ale

$$
r_{\rm flat}=1-\frac1{2N-1},\qquad
r_N-r_{\rm flat}=
\frac{2(N-1)(N-2)}{(2N^2+1)(2N-1)}.
$$

Zlepšení je přísné pro $N\ge3$. Rovnost těchto dvou účtů neznamená
stejnou cenu přípravy koherence ani optimálnost trojúhelníku.
Jeho lokální rovnice $2c_i-c_{i-1}-c_{i+1}=2\delta_{i,N}$
s nulovými krajními hodnotami sama neudává přípravný mechanismus.

**Rozsah racionality:** dvouosé amplitudy $c_ic_j/S_N$, překryv $r_N$
a níže uvedené speciální váhy jsou racionální. Z toho neplyne racionalita
všech amplitud celého přístroje: například maticový prvek $E_a$ obsahuje
$(\sqrt5-1)/10$, jiné kontexty mohou obsahovat kořeny jednotky.
Přesná aritmetika může vyžadovat algebraická čísla; konkrétní implementace
musí svůj číselný obor a přesnost doložit samostatně.

<a id="p03"></a>

## P03 — Chyba celého výstupu bez násobení délkou historie

Pouze pro důkaz vložme konečnou referenci do $\ell^2(\mathbb Z^2)$
s unitárními posuny $S_v$ a definujme
$D=\sum_sE_s\otimes I_C\otimes S_{v_s}$.
Na dosažitelných stavech platí
$\widehat W=D^\dagger(W\otimes I_R)D$; všechny výsledné indexy stále
leží v konečné fyzické referenci. Žádná nekonečná reference se nepřipravuje.

Pro normalizované $\psi$, včetně korelací s nedotčeným spektátorem,
ortogonalita $E_s$ dává

$$
\|(D-I)(\psi\otimes\eta_N)\|^2
=\sum_s\|E_s\psi\|^2\|S_{v_s}\eta_N-\eta_N\|^2
\le2(1-r_N).
$$

Stejná mez platí pro $D^\dagger-I$. Rozklad rozdílu na dva členy,

$$
\begin{aligned}
\widehat W(\psi\eta_N)-(W\psi)\eta_N
={}&D^\dagger(W\otimes I)(D-I)(\psi\eta_N)\\
 &+(D^\dagger-I)((W\psi)\eta_N),
\end{aligned}
$$

dává trojúhelníkovou nerovností a normováním obou výstupů

$$
\boxed{\|\Psi_{\rm actual}-\Psi_{\rm ideal}\otimes\eta_N\|^2
\le\min\left(4,8(1-r_N)\right)
=\min\left(4,\frac{24}{2N^2+1}\right).}
$$

Za $W$ lze vzít celý konečný ideální program. Díky násobivosti jeho
liftu se mez nenásobí počtem měření. Je to mez pro celý koherentní výstup,
včetně reference a archivů, nikoli pouze pro jeho vybrané pravděpodobnosti.
Předpokládá počáteční součin s $\eta_N$; během programu se reference
neodpojuje ani neobnovuje. Nevztahuje se automaticky na proud nových polí.

<a id="p04"></a>

## P04 — Účinný vstup pro archivované pravděpodobnosti

Nechť $M_h$ je ideální větvový operátor úplné historie a $\psi$ počáteční
stav pole. Skutečný nenormovaný stav pole a reference v této větvi je

$$
\Phi_h=\sum_{s,t}E_sM_hE_t\psi\otimes S_{v_t-v_s}\eta_N.
$$

Při výpočtu normy jsou různé konečné sektory $s$ ortogonální.
Společný posun $-v_s$ se z překryvu bra a ket vyruší. Proto

$$
\Gamma_N(\rho)=\sum_{s,t}g_{st}E_s\rho E_t,\qquad
g=\begin{pmatrix}1&r_N&r_N\\r_N&1&r_N^2\\r_N&r_N^2&1\end{pmatrix},
\qquad
p(h)=\operatorname{Tr}[M_h\Gamma_N(\rho)M_h^\dagger].
$$

Matice $g$ je Gramova matice posunutých referencí; $\Gamma_N$ je tedy
úplně pozitivní a zachovává stopu. U smíšeného vstupu důkaz plyne linearitou.
Mapa se použije jednou na vstup celé ideální historie. Neudává skutečný
stav pole před prvním měřením a neopravňuje k jejímu vložení po každém kroku.
Skutečná konečná reference pro čistý vstup je výslovně

$$
\rho_R^{\rm out}=\sum_h\operatorname{Tr}_F|\Phi_h\rangle\langle\Phi_h|.
$$

Tento výraz netvrdí návrat do $|\eta_N\rangle\langle\eta_N|$.
$\rho_R^{\rm out}$ je pouze redukovaný stav reference; sám neobsahuje
její korelace s polem a archivy. Ty zachovává úplný stav
$\sum_h\Phi_h\otimes|h\rangle_A$ a právě z něj musí pokračovat další krok.

<a id="p05"></a>

## P05 — Úplný placený zápis a skutečné dva J kontakty

Následující konstrukce je samostatná analytická dilatace. Nepředstírá
rekonstrukci nedodaných pracovních ukazatelů nebo jejich hodinového programu.
Pro libovolnou úplnou rodinu $\{D_\ell\}$,
$\sum_\ell D_\ell^\dagger D_\ell=I$, vezměme čerstvý archiv $A$
s prázdným stavem $\bot$ o energii 0 a výsledky $\ell$ o energii 1.
Baterie má hladiny $0,\ldots,B_{\max}$ s energií rovnou hladině. Položme

$$
V=\sum_{b=1}^{B_{\max}}\sum_\ell
D_\ell\otimes|\ell\rangle\langle\bot|_A
       \otimes|b-1\rangle\langle b|_B,
\quad P_{\rm in}=V^\dagger V,\quad Q=VV^\dagger.
$$

Úplnost rodiny dává
$P_{\rm in}=I_F\otimes|\bot\rangle\langle\bot|
\otimes\sum_{b=1}^{B_{\max}}|b\rangle\langle b|$.
Operátor $V$ je částečná izometrie, $Q$ je projektor a
$P_{\rm in}Q=0$, protože obrazy mají archiv obsazený. Tedy

$$
U_D=V+V^\dagger+I-P_{\rm in}-Q,\qquad
U_D^\dagger=U_D,\quad U_D^2=I.
$$

Přechod sníží baterii o jednu a zvýší obsazenost archivu o jednu; adjungovaný
přechod provede opak. Celý $U_D$ zachovává $H_C=B+\operatorname{occ}A$,
včetně hranice baterie a komplementu obrazu. Jeho lift z P01 navíc
vyrovná změnu energie pole referencí. Prázdný archiv je od výsledku 0 odlišný.

Pro dva úplné J kontakty použijme čtyři čerstvé archivy a baterii
$B_{\max}=5$, zpočátku na hladině 5. Postupně proveďme uvedený zápis pro
rodiny $\{K_{b_1}\}$, $\{\Pi_{d_1,m_1}\}$, $\{K_{b_2}\}$,
$\{\Pi_{d_2,m_2}\}$. Příslušná ideální historie má operátor

$$
M_h=\Pi_{d_2,m_2}K_{b_2}\Pi_{d_1,m_1}K_{b_1},\qquad
\Psi_{\rm ideal}=\sum_hM_h\psi\otimes|b_1,m_1,b_2,m_2\rangle_A\otimes|1\rangle_B.
$$

Po prvních dvou zápisech je baterie na 3, po všech čtyřech na 1. Čtyři
obsazené archivy nesou dohromady energii 4, takže účet je přesně $5=4+1$.
Poslední dvě hradla jsou identitou na první dvojici archivů. Zachovají proto
celou její redukovanou matici hustoty, nejen diagonální četnosti záznamů.
Skutečný stav reference a jeho korelace pokračují podle $\Phi_h$ z P04;
mezi kontakty se neprovádí reset. Na součin všech čtyř unitárů platí beze změny
mez z P03 a pro úplnou historii platí jediná vstupní $\Gamma_N$.

Úplný skutečný výstup této realizace je tedy

$$
\Psi_{\rm actual}=\sum_h\Phi_h\otimes
|b_1,m_1,b_2,m_2\rangle_A\otimes|1\rangle_B,
$$

s $\Phi_h$ z P04 a právě zde uvedeným $M_h$. Jeho norma je jedna;
vyplývá to z úplnosti čtyř instrumentů a unitárnosti jejich liftů.

Pro ideální vstup $|0\rangle$ a oba polohové kontexty jsou přípustné
$b_1,b_2\in\{+,-\}$, $m_1\in\{0,2\}$ a
$m_2\in\{m_1,m_1+2\pmod5\}$. Každá z těchto 16 historií má amplitudu
o absolutní hodnotě $1/4$, tedy váhu $1/16$. To je ideální srovnávací
případ, nikoli tvrzení o přesných vahách konečné reference. Vložené druhé J
rovněž znamená, že tento protokol není zkouškou opakovatelnosti z P07.

Stejný abstraktní zápis uskuteční jeden J kontakt a $K$ následných měření
s $K+1$ archivy a počáteční baterií $K+2$, konečná baterie je opět 1.
Přibývá paměť a energie obsazenosti; nevzniká bezplatné neomezené opakování.
Inverze celého unitáru záznamy smaže, dopředné pokračování je uchovává.
Tento důkaz neudává počet lokálních hradel původní konstrukce ani její
periodu $6K+10$. Doložení takového programu, fyzického přípravného
mechanismu, role energie jako generátoru času a jednotlivých událostí
zůstává samostatným úkolem.

<a id="p06"></a>

## P06 — Sedmá nula a její konečná odchylka

Pro vstup $|0\rangle$ je skutečný stav po prvním J rozdělení přesný,
neboť $K_b$ komutují s $H_F$. Minusová větev před dalším měřením má
nenormovaný stav $v=(|0\rangle-|2\rangle)/2$, $E_0v=0$.
Proto se v jejích archivovaných vahách uplatní pouze překryv $r_N^2$.

Zachování prvních šesti nul má samostatný důvod. Pro standardní šestici
přímkových projektorů přes $u=(1,0)$ použijme jejich identitu
$\sum_{L\ni u}\Pi_L=I+A_u$, kde $A_u|q\rangle=|2-q\pmod5\rangle$.
Z $A_uPA_u=P^\dagger$ plyne $[A_u,H_F]=0$, a tedy i
$[A_u,E_s]=0$. Proto všechny $E_sv$ zůstávají v záporném prostoru
$A_u$, kterým je $\operatorname{span}\{|0\rangle-|2\rangle,
|3\rangle-|4\rangle\}$. Kladnost projektorů a uvedená součtová identita
ztotožní tento prostor s jejich společným jádrem. Účinný minusový stav
$\Gamma_N(vv^\dagger)$ má podporu v témže jádře, takže šest vah zůstává
přesně nulových. Sedmá podmínka na $q=3$ už tuto celou podporu neanuluje.

Použijme $(E_a)_{xy}=(2/5)\cos(2\pi(x-y)/5)$. V souřadnici 3 je
$(E_av)_3=-\sqrt5/10$ a $(E_bv)_3=+\sqrt5/10$.
Z předchozí formule tedy přímo plyne

$$
\boxed{x_N=\Pr(-,q=3)=2\frac1{20}(1-r_N^2)
=\frac{12N^2-3}{10(2N^2+1)^2}>0.}
$$

Stejné dosazení pro pět souřadnic dává společné minusové rozdělení
$(1/4-x_N,0,1/4-x_N,x_N,x_N)$. Jeho součet je $1/2$, takže
$\Pr(q=3\mid-)=2x_N$. Pro $N=2$ je $x_N=1/18$; dvě opakovaná
polohová měření mají minusové váhy $7/36,7/36,1/18,1/18$ na dvojicích
$(0,0),(2,2),(3,3),(4,4)$, všechny neshodné dvojice mají váhu nula.

Chyba tohoto svědka je $O(N^{-2})$, ale přesný sedminulový cíl tato
rodina nesplňuje pro žádné konečné $N$. Konečně podporovaný nenulový
normovaný stav nemůže mít jednotkový překryv s nenulovým posunem: rovnost
v Cauchyově–Schwarzově nerovnosti by vynutila shodu jeho podpory s posunem.
To omezuje uvedenou realizaci; nejde o zákaz všech možných přístrojů.

<a id="p07"></a>

## P07 — Přesná opakovatelnost a zahození korelací

Pro jeden J kontakt a $K$ následných měření je
$M_{b,h}=\Pi_{d_K,m_K}\cdots\Pi_{d_1,m_1}K_b$.
Dvě totožná měření bez vloženého J nebo jiného zásahu do pole mají při
$m_2\ne m_1$ nulový operátor $\Pi_{m_2}\Pi_{m_1}K_b$, a proto
$\Pr(m_2\ne m_1)=0$ přesně i pro konečné $N$.
Opakovatelnost patří celému systému pole–reference; nevynucuje ideální
vlastní stav samotného pole po prvním měření.

Naproti tomu vložení nové $\Gamma_N$ po ideálním polohovém výsledku
používá sektorové váhy $(1,2,2)/5$, a proto dává neshodu

$$
1-\frac{9+8r_N+8r_N^2}{25}
=\frac{8(1-r_N)(2+r_N)}{25}.
$$

Pro $N=2$ je to $64/225$. Jde o celkovou váhu přes oba porty,
nikoli o společnou váhu pouze minusové větve.

<a id="p08"></a>

## P08 — Podmíněný důkaz konečného hodinového programu

Nechť celý dopředný program tvoří úplná unitární hradla
$F_0,\ldots,F_{m-1}$, zachovávající tentýž energetický účet.
V pořadí provedení sestavme seznam
$G=(F_0,\ldots,F_{m-1},I,I,F_{m-1}^\dagger,\ldots,F_0^\dagger)$
délky $L=2m+2$. Dva prostřední kroky jsou pasivní čtecí okno, bez
nového neúčtovaného zápisu. Na hodinách $c\in\mathbb Z_L$ definujme

$$
T=\sum_{c=0}^{L-1}|c+1\pmod L\rangle\langle c|\otimes G_c.
$$

Operátor T je unitární. Pro počáteční hodiny 0 se po L krocích použije
$G_{L-1}\cdots G_0=I$. Pro jiné počáteční hodiny jde o cyklickou
permutaci tohoto součinu, tedy o jeho unitární konjugaci, opět I.
Proto $T^L=I$ na celém nosiči. Při zvoleném degenerovaném Hamiltoniánu
hodin $H_{\rm clock}=0$ zachovává T také společný energetický účet.
Tím není odvozen fyzikální generátor času ani cena přípravy řízení.

Pokud nedodaný program opravdu poskytuje uvedená úplná hradla s
$m=4+3K$, dostáváme $L=6K+10$, při $K=2$ hodnotu 22.
Samotný počet hlášených kroků tyto předpoklady neověřuje. Abstraktní zápis
z P05 má jinou granularitu hradel a není jeho implementační náhradou.
Dopředná fáze uchovává starší záznamy, zatímco úplná inverze je smaže.
