# Přístroj pro celé spektrum kontaktního W

Stav: analytický důkaz. Při jeho psaní nebyl spuštěn nový vědecký výpočet.
Dokončené balíky `mass_sharp` a `mass_construction` nejsou měněny.

## 1. Vstupní operátory a větev energie

Nechť `H` je omezený samosdružený operátor na libovolném separabilním
prostoru `S`, po deklarovaném přičtení skalární konstanty splňující

    0 <= H <= h I,        h > 0.                                      (1)

Nechť `V` je požadovaný unitární zásah na celém `S`. Nikde jej
neomezujeme na vlastní vektory, izolovanou větev nebo konečný počet
energetických hladin. Píšeme

    D = V* H V - H,       C_V = ||D|| = ||[H,V]||,
    a_D = sup spec D - inf spec D.                                   (2)

Pro původní kontaktní `W` lze použít analytický logaritmus s řezem
v globální mezeře na fázi `alpha=3 pi/10`. Příslušný mechanický
operátor `H_W` má `exp(-i H_W)=W`, fázi kontaktní větve `Omega(0)=g`
a energii v intervalu `(-alpha,2 pi-alpha)`. V bateriovém výpočtu
použijeme `H=H_W+alpha I`, tedy bezpečně `h=2 pi`. Tento posun se
započítá v celkovém skalárním časovém faktoru; nemění `D`, práci,
komutátory ani rychlost. Nejde o výměnu přesného logaritmu za
kalibrovaný polynom ve `W`.

Důkaz globální mezery, existence analytického logaritmu a odhadu
pro jeho prostorové komutátory náleží samostatné spektrální části.
Pro použití zde stačí její výsledek

    ||[H_W,R]|| <= C_H,
    ||V_eta* H_W V_eta-H_W||
        <= 2 C_H |sin(eta/2)| <= C_H |eta|,
    V_eta = exp(i eta R).                                          (3)

Jedna explicitní, konzervativní konstanta je

    omega = (arccos(7/25)-g)/2 > 0,
    C_H = csc^2(omega/2).                                          (4)

U dvojice skutečných procházek `W_R tensor W_Y` vezmeme součet obou
energií, `h=4 pi`, a zásah `V_eta=exp(i eta(R-Y))`. Pak
`C_V <= 2 C_H |eta|`. Dvojice, včetně pohyblivé reference, je v této
větě celým systémem `S`; baterie nezastupuje nezapočtenou referenci.

## 2. Kladná baterie s konečnou energetickou kapacitou

Zvolme `L>0` a definujme

    A = L+2h,
    B = L^2([0,A], de),
    (H_B b)(e) = e b(e).                                           (5)

Baterie je nekonečně rozměrný kontinuální registr s omezenou kladnou
energií `0 <= H_B <= A`. Není to konečný seznam vzájemně souměřitelných
hladin. Proto může přesně pojmout všechny rozdíly energií původního
spojitého spektra.

Její pevný počáteční stav, nezávislý na neznámém vstupu systému, je

    b_L(e) = sqrt(2/L) sin(pi(e-h)/L),       h <= e <= h+L,
             0,                            otherwise.             (6)

Platí přesně

    ||b_L||_2 = 1,
    ||b_L'||_2^2 = pi^2/L^2,
    <H_B> = h+L/2 = A/2,
    Var(H_B) = L^2(1/12-1/(2 pi^2)).                               (7)

Derivace v (7) je slabá derivace nulového prodloužení na reálnou osu.
Stav je v `H^1(R)`: na obou koncích svého intervalu je nulový.

## 3. Přesný unitární zásah v souřadnici celkové energie

Prostor `S tensor B` má přímointegrální rozklad podle celkové energie

    H_0 = H tensor I + I tensor H_B.

V celkové energii `t` je vlákno izometrické prostoru

    S_t = 1_[max(0,t-A), min(h,t)](H) S.                            (8)

Prázdné intervaly dávají nulové vlákno. V celém intervalu

    h <= t <= A                                                   (9)

je `S_t=S`, protože každý systémový energetický příspěvek `E` z
`[0,h]` ponechává baterii `e=t-E` v `[0,A]`.

Přesné odvození: spektrální věta zapíše
`S = integral^oplus K_E dmu(E)`. Vektor celého systému má souřadnice
`Psi(E,e)`. Substituce `t=E+e` definuje unitární převod `T`, jehož
vlákna jsou (8); Fubiniho věta zachovává normu. Operátor `T H_0 T*`
je násobení číslem `t`. Případ bodového, absolutně spojitého i
singulárně spojitého spektra je zahrnut stejným rozkladem.

Definujme na celém prostoru

    (T U T*)_t = V,         h <= t <= A,
                  I_(S_t), otherwise.                             (10)

Rodina je měřitelná a každé vlákno je unitární. Proto je `U` unitární
a silně komutuje s `H_0`. Zejména platí přesná operátorová rovnost

    U* H_0 U = H_0.                                               (11)

Pro libovolný vstup `psi tensor b_L` leží celková energie v (9),
neboť `E in [0,h]` a `e in [h,h+L]`. Zásah tedy vždy používá plné
vlákno `V`, nikoli hraniční identitu. Po zásahu stále zbývá
`e'=t-E' in [0,A]`. Není potřeba vyhodit, změřit nebo renormalizovat
žádný hraniční výsledek.

## 4. Fourierův zápis slouží důkazu, nikoli falešnému časovému operátoru

Nulově vložme baterii do `L^2(R)`. Na tomto větším pomocném prostoru
existuje kanonický posun s Fourierovou proměnnou `tau`. Ideální
celkové energetické souřadnice mají převod

    C = exp(-i H tensor P),
    U_infty = C* (V tensor I) C,
    U_infty(tau) = exp(i tau H) V exp(-i tau H) = K_tau.             (12)

Znaménko lze ověřit na vlastních energiích: přechod `E -> E'`
posune energii baterie o `E-E'`. Na všech vstupech s bateriovou
podporou v `[h,h+L]` je skutečné `U` z (10) přesně toto omezení
`U_infty`; jeho výstup zůstává v `[0,A]`.

Tím se netvrdí existence kanonického samosdruženého operátoru času
na konečném intervalu energie. Fourierova osa a `P` v (12) jsou
pouze pomocný analytický rozklad skutečného, již definovaného `U`.

Položme `p_L(tau)=|bhat_L(tau)|^2`. Parsevalova rovnost dává

    integral p_L(tau) dtau = 1,
    integral tau^2 p_L(tau) dtau = pi^2/L^2.                       (13)

Protože `b_L` je reálné, `p_L` je sudé. Posunutí bateriové vlny
o `h` tento fakt nemění.

Překryv dvou energeticky posunutých bateriových stavů má dokonce
uzavřený tvar. Pro `s in R` označme `x=|s|/L`. Pak

    F_L(s) = integral b_L(e) b_L(e-s) de
           = (1-x) cos(pi x) + sin(pi x)/pi,     0<=x<=1,
             0,                                 x>=1.              (13a)

Jde zároveň o charakteristickou funkci hustoty `p_L`. Platí
`0 <= 1-F_L(s) <= pi^2 s^2/(2L^2)`; pravá mez plyne přímo
z `||b_L(. - s)-b_L|| <= |s| ||b_L'||`. Ve spektrálním zápisu
kanálu proto každý dvojitý přechod `E_c -> E_a`, `E_d -> E_b`
nese přesný faktor `F_L(E_a-E_c-E_b+E_d)`. Tato funkce je definovaná
pro všechny reálné energetické rozdíly; žádná společná mřížka
hladin se v ní neobjevuje.

## 5. Rovnoměrná chyba společného stavu

Pro každý normalizovaný systémový vektor, také s libovolnou
pomocnou kvantovou referencí, platí

    ||U(psi tensor b_L) - (V psi) tensor b_L||
       <= pi C_V/L.                                              (14)

Důkaz: Duhamelova rovnost pro omezené `H` dává

    ||exp(i tau H) V exp(-i tau H)-V||
        <= |tau| ||[H,V]||.

Čtverec normy v (14) je po Fourierově převodu přesně

    integral p_L(tau) ||(K_tau-V)psi||^2 dtau.

Použijeme (13). Toto je důkaz přes Parsevalovu a Duhamelovu rovnost;
nepoužívá neplatný přechod od skalární Lipschitzovy vlastnosti k
operátorové Lipschitzově vlastnosti.

Označíme-li nejhorší infidelitu včetně propletených vstupů `epsilon`,
pak následně

    epsilon <= min(1, pi^2 C_V^2/L^2).                             (15)

Neznamená to přesný návrat baterie: oba systémy si ponechávají malé
korelace a baterie přesně dodává skutečně odebranou energii.

## 6. Redukovaný kanál má ještě menší chybu

Skutečný kanál po zapomenutí baterie je přesně

    E_L(rho) = integral p_L(tau) K_tau rho K_tau* dtau.             (16)

Pišme `F_tau = Ad_(K_tau)`, `F_0=Ad_V` a
`mathcal L(X)=i[H,X]`. Na stopové třídě i po přidání libovolné
pomocné reference platí

    F_tau = exp(tau mathcal L) F_0 exp(-tau mathcal L),
    ||mathcal L||_diamond <= h,
    ||[mathcal L,F_0]||_diamond <= a_D,
    ||F_tau''||_diamond <= 2h a_D.                                (17)

Druhá nerovnost pro komutátor plyne z
`F_0^(-1) mathcal L F_0 - mathcal L = i[D,.]` a z odečtení středu
spektrálního intervalu `D`. Všechny konjugace v (17) zachovávají
diamantovou normu.

Taylorův odhad s integrálním zbytkem a sudost `p_L` odstraní celý
první člen. Pro půldiamantovou vzdálenost
`d_L=(1/2)||E_L-Ad_V||_diamond` vychází

    d_L <= min(1, pi^2 h a_D/(2L^2))
        <= min(1, pi^2 h^2/L^2).                                  (18)

Je-li `C_V=O(|eta|)`, je první horní mez v (18) řádu
`|eta|/L^2`, nejen `1/L`.

Tato horní mez je slučitelná s předchozí nutnou kapacitní mezí.
Spektrální šířky celého systému a baterie jsou nanejvýš `h` a `A`,
takže přesná univerzální implementace při `a_D>0` stále není možná:

    epsilon >= a_D^2/[4(L+3h)^2].                                 (19)

Konstrukce neposkytuje zakázaný přesný kanál; poskytuje přesné
zachování energie a kvantifikovanou malou odchylku kanálu.

## 7. Přesné účtování skutečné práce

Požadovaná práce na vstupu `rho` je `Tr(D rho)`. Skutečná práce
na systému je

    W_actual = Tr(H E_L(rho))-Tr(H rho).

Rovnost (11) dává pro každý vstup přesně

    Delta <H_B> = - W_actual.                                     (20)

Z (16) a komutace `H` s jeho vlastními exponenciálami plyne

    E_L^*(H) = H + integral p_L(tau)
                          exp(i tau H) D exp(-i tau H) dtau.

Sudost a druhý Taylorův zbytek proto dávají ostřejší odhad

    |W_actual-Tr(D rho)|
        <= pi^2 ||[H,[H,D]]||/(2L^2)
        <= pi^2 h^2 a_D/(4L^2).                                  (21)

Tento odhad platí pro každou smíšenou přípravu, bez konečnorozměrného
předpokladu a bez změny spektrální energie na numerickou mřížku.

U kontaktní větve se musí použít skutečné `D_eta`. Holý kop mění
momentum, ale nepřenáší automaticky vektor `chi_P` do `chi_(P+eta)`.
Například v klidu a paralelním kalibru

    <chi_0,H_W''(0)chi_0>
       = kappa + 2<chi_0',(H_W(0)-g)chi_0'>.                       (22)

Koeficient práce je tedy obecně koeficient skutečné změny energie,
včetně složky mimo kontaktní větev. Rovnice (22) plyne dvojím
derivováním `H_W(P)chi_P=Omega(P)chi_P`, nikoli novým modelem.
Výběr logaritmické větve zůstává fyzikální specifikací.

## 8. Přímé navázání na původní konečné přípravy

Vezměme stejnou posloupnost impulsů jako v celočíselné konstrukci,

    q=5^ell,       eta_q=2 arctan(1/q),
    N=q^4,         T=q,
    L=q.                                                           (23)

Pro celé spektrum jednoho `W` i dvojice s pohyblivou referencí
platí díky (3)

    C_V=O(q^-1),          a_D=O(q^-1),
    delta_joint=O(q^-2)=o(eta_q),
    epsilon=O(q^-4),
    d_L=O(q^-3),
    |W_actual-Tr(D_eta_q rho)|=O(q^-3)=o(eta_q^2),
    A=q+2h,              <H_B>=h+q/2.                              (24)

Konstanty jsou dané skutečným globálním spektrálním odstupem, nikoli
fitem na konečné matici. Odhady jsou asymptotické se zobrazenými
konstantami; velká konzervativní hodnota `C_H` sama neopravňuje
prohlásit malé konkrétní `q` za přesný praktický přístroj.

Protože kanál je odhadnut na všech stavech, lze bez dodatečné
projekce vložit právě původní konečné binomické přípravy, včetně
jejich skutečné příměsi mimo vázanou větev. Následné použití `W^T`
chybu kanálu nezvětší. Očekávání libovolného omezeného rychlostního
operátoru normy nejvýše jedna se změní nanejvýš o `2d_L`.

Přístroj může během zásahu mírně změnit také polohu, ačkoli ideální
kop s polohou komutuje. Je-li `X` taková poloha, `[X,V]=0` a
`||[H,X]||<=C_X`, potom na vstupních vektorech z domény `X`
(zejména na původních vektorech s konečnou podporou)

    |Delta <X>_during_U| <= 2 pi C_X/L.                            (25)

Důkaz používá (12),
`||[X,K_tau]||<=2|tau| C_X` a Parsevalovu rovnost. Zároveň dokládá
zachování potřebné operátorové domény na připravených vstupech.
Při `T=q`, `L=q` má tento dodatečný posun v původním podílu
`Delta X/(T eta_q)` velikost `O(q^-1)`. Ani při měření polohy
od okamžiku před zásahem tedy nezničí již dokázaný limit odezvy.

## 9. Autonomní Hamiltonián s přiznanou interakční energií

K (10) lze přidat explicitní časově nezávislý Hamiltonián.
Zvolme kladný omezený Borelův logaritmus `K_0` jednotky `V`,

    0 <= K_0 <= 2 pi,
    exp(-i K_0)=V.

U kopu je to diagonální funkce polohy
`K_0(x)=(-eta x) mod 2 pi`; u relativního kopu se dosadí `x=R-Y`.
V celkových energetických vláknech položme

    K_t = K_0,       h<=t<=A,
          0,         otherwise,
    H_tot = H_0+K.                                               (26)

Potom

    0 <= H_tot <= (A+h+2 pi) I,
    [H_0,K]=0,
    exp(-i H_tot)=exp(-i H_0) U.                                 (27)

V jednotkách jednoho taktu tedy získáme přesný volný krok původního
`W` společně s energeticky konzervativním zásahem. Ideální srovnávací
výstup je `(W V psi) tensor exp(-i H_B)b_L`, až známý skalární
faktor kvůli posunu `H_W` v (1). Pro dvojici je volný krok
`W_R tensor W_Y`. Platí stejné chyby (14)--(24), protože společný
volný vývoj je unitární.

Interakční energie `K` není vynechána. `H_0`, `K` i jejich součet
se zachovávají samostatně, takže skutečnou práci v (20) platí
baterie, nikoli neoznačený úbytek interakční energie.

Rovnice (27) určuje autonomní vývoj a čtení v předem určeném čase.
Nedodává vnitřní zastavovací hodiny. Ponecháme-li interakci zapnutou,
další celá období opakují také `U`; nejsou to další čisté kroky
volného `W` po jediném kopu. Výběr doby zásahu a vypnutí zůstávají
samostatnou konstrukční otázkou.

## 10. Přesný rozsah výsledku

Přístroj pokrývá celý spektrální prostor skutečného `W`, zachovává
jeho zvolenou přesnou energii a má konečnou, kladnou kapacitu.
Nepotřebuje souměřitelné hladiny, energetické zaokrouhlování,
postselekci ani projekci na vázanou větev. Rovnice (24) zachovává
původní odezvový limit a současně odděluje chybu práce od jejího
vedoucího kvadratického členu.

Kontinuální baterie je nekonečně rozměrný přídavný registr. Její
stav (6) je dodaná energetická koherence. Jednotka (10) je definována
spektrálně; z její existence samotné neplyne prostorově konečný
dosah ani sestavení z původní pevné celočíselné abecedy bran.
Analytický logaritmus původního `W` má exponenciální prostorové
chvosty, ale tvrdé energetické hranice přístroje se nesmějí bez
dalšího důkazu prohlásit za stejně místní. Tyto vlastnosti jsou
oddělené od již přesně dokázaného energetického spojení se spektrem.
