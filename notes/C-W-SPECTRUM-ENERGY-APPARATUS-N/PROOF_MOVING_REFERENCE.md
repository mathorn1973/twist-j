# Pohyblivá reference a původní odezva

Status: vlastní analytický dodatek k uvedené spektrální konstrukci.
Všechny prostory a operace jsou dodané konstrukční údaje. Nejde o
odvození kontaktu či fyzikálního přístroje z původního nativního U.

## 1. Dvě skutečné kopie stejného W

Označme prostor jedné kontaktní dvojice S_W a její dvě souřadnice R,r.
Referenci dáme druhou kopii S_W se souřadnicemi Y,s. Volný krok a
energie celé dvojice jsou

    W_pair = W_R tensor W_Y,
    H_pair = H_R tensor I + I tensor H_Y,
    exp(-i H_pair) = W_pair.

Zde H=i Log_alpha W je přesný analytický logaritmus z důkazu globální
mezery, alpha=3pi/10. V konstrukci baterie použijeme

    H_S = H_pair+2alpha I,       0 <= H_S <= h I,       h=4pi.

Tato konstantní změna počátku energie nemění práci ani konzervaci.
Při exponentiaci dodává přesně známou globální fázi exp(-2i alpha).
Referenční těleso má vlastní pohyb, vnitřní kontakt i energii. Není
to pouhá neměnná značka Y s nulovým Hamiltoniánem.

Požadovaný zásah je

    V_eta = exp[i eta(R-Y)].                                      (1)

Na plné hybnostní kružnici posouvá P na P+eta a Q na Q-eta. Jeho
inverze je V_-eta. Pro společnou translaci obou těžišť T_a platí
[T_a,H_S]=[T_a,V_eta]=0. Spektrální převod do celkové energie i
hraniční projekce baterie s T_a komutují, a proto

    [U_eta,L, T_a tensor I_B] = 0.                                (2)

Nový aparát tedy zachovává přesně součet quazihybností modulo 2pi,
současně s přesnou aditivní energií H_pair+H_B. Nezaměňujeme to za
globální operátorovou konzervaci součtu dvou hlavních úhlových větví.

Na připravené baterii je jeho redukovaný kanál směsí

    K_tau = exp(i tau H_pair) V_eta exp(-i tau H_pair).

Každé K_tau stále posouvá první hybnost o +eta a druhou o -eta:
H_pair je v obou hybnostech vláknový operátor. Hybnostní hustoty se
proto posunou přesně i po zapomenutí baterie. Pro reálné funkce
hybnosti jde o operátorovou identitu K_tau* f(P,Q) K_tau
=f(P+eta,Q-eta). Počáteční konečná příprava má stejné malé obtočení
hlavní větve hybnosti jako v původním důkazu; aparát je nezvětšuje.

Tato symetrie a předepsané opačné impulzy nejsou odvozením zákona
vzájemné síly mezi dvěma tělesy. Globální cílové V_eta se samo
rozkládá na dva faktorové impulzy. Společný energetický aparát
započítává energii obou a může je korelovat s baterií.

## 2. Konečné původní stavy zůstávají skutečnými vstupy

Pro N>=1 definujme

    b_N(R)=binom(2N,N+R),  |R|<=N,
    Z_N=binom(4N,2N),
    psi_N(R,r)=b_N(R) delta_r0 (1,0,0,-1)/sqrt(2 Z_N).

Připravíme psi_N tensor psi_N, obě s nulovou střední hybností.
Jde o přesně tutéž binomickou přípravu, která byla dříve přezkoumána.
Není nahrazena ideálním pásovým vlastním vektorem. Pokud byl starý
impulz omezen oknem |R-Y|<=B, volba B>=2N zaručuje stejný cílový
výstup na tomto vstupu jako (1). Mimo tuto podporu zde definujeme
globální (1), protože nový spektrální aparát má být unitární na
celém prostoru.

Položme

    q=5^ell, eta=2atan(1/q), N=q^4, T=q, L=q.                     (3)

Pro tento aparát je A=q+8pi a počáteční průměr energie baterie
4pi+q/2. Jde o konečné hodnoty při každém q. Rozměr spojitého
bateriového prostoru přitom zůstává nekonečný při každém q.

Z globálního spektrálního odhadu platí pro D_eta=V_eta*H_SV_eta-H_S

    ||D_eta|| <= 4 C_H |sin(eta/2)| <= 2 C_H |eta|,
    osc(D_eta) <= 2||D_eta||,
    C_H=csc^2[(arccos(7/25)-2pi/5)/4].                            (4)

Věta o spektrálním přístroji tedy dává společnou chybu O(q^-2),
infidelitu O(q^-4), půldiamantovou chybu d_L=O(q^-3) a chybu
skutečné práce oproti Tr(D_eta rho) řádu O(q^-3)=o(eta^2).
Všechny odhady platí i pro neznámé propletené vstupy.

## 3. Zachování původního limitu skutečného pohybu

Nechť D_R=W_pair* R W_pair-R je jedno-tikový posun prvního těžiště.
Původní kontaktní důkaz ukazuje ||D_R||=1 a totéž pro D_Y.
Průměrný proud po T volných krocích je

    D_R,T=(1/T) sum_(t=0)^(T-1) W_pair^(-t) D_R W_pair^t,
    ||D_R,T||<=1.

Kanálová mez tedy pro každý skutečný vstup dává

    |v_R,T(actual)-v_R,T(ideal kick)|<=2d_L.                      (5)

Původní nepromítnutý binomický důkaz, se všemi přípravnými a
mezipásovými členy ponechanými, dává

    v_R,T(ideal kick)/eta -> kappa,
    v_Y,T(ideal kick)/eta -> -kappa,
    kappa=sqrt(16phi+7)/20, phi=(1+sqrt5)/2.

Protože d_L/eta=O(q^-2), stejný limit platí s novým energetickým
aparátem. Pokud se poloha počítá už od okamžiku před zásahem,
přičte se možný posun během U. Pro první těžiště platí

    |Delta<R>_during_U|<=2pi C_H/L,

a obdobně pro Y. Po dělení T eta je tato korekce O(q^-1) a mizí.
Pro odvození domény polohy se používá druhý Fourierův moment
baterie, nikoli jen malá stopová vzdálenost. Samotná blízkost stavů
by pro neomezený operátor polohy nestačila.

Výsledkem je skutečný relativní pohyb dvou pohyblivých kopií:

    v_R,T/eta -> kappa,
    v_Y,T/eta -> -kappa,
    (v_R,T-v_Y,T)/eta -> 2kappa.                                 (6)

Při součtové hybnosti nula je kanonická relativní hybnost
p=(P-Q)/2, sdružená s X=R-Y. Cílový impulz ji mění o eta.
Odpovídající redukovaná hmotnost v těchto pevně zadaných jednotkách je

    mu_rel = 1/(2kappa) = 10/sqrt(16phi+7),

zatímco koeficient jednotlivého těžiště zůstává m=1/kappa.
To je odezvová hmotnost tohoto deklarovaného modelu, nikoli
identifikace fyzického elektronu, protonu nebo dvojice pozitivně
energetických fotonů.

## 4. Skutečná práce a její nejednoznačnost

Přístroj přesně splňuje

    Delta<H_B> = -Delta<H_pair>.

Pro skutečný bare kick se práce neurčuje pouze rozdílem hodnot
Omega. Jeho stav po posunu obsahuje mimo-větvovou složku a správná
veličina je Tr(D_eta rho). Na ideálním klidovém vlákně platí

    <chi0,H_W(P)chi0>-g
      = (P^2/2)[kappa+2<chi0',(H_W(0)-g)chi0'>]+O(P^3).

Tyto členy aparát ponechává a účtuje. Neprovádí skrytou projekci.
Spektrální důkaz navíc konstruuje exponenciálně místní H_m
=H+2pi mP_- se stejnou blízkou pásovou energií Omega a stejným W.
Již na jednom tělese mění práci o

    2pi m beta_- eta^2+o(eta^2),
    beta_- >= 3(1+sqrt5)/80 > 0.

U dvou symetricky kopnutých kopií se vedoucí rozdíl zdvojnásobí.
V tomto balíčku je zvolen m=0. Jde o explicitní energetickou volbu,
kterou samotný krok W, odezvová hmotnost ani exponenciální útlum
vazeb neurčují.

## 5. Jednorázový protokol a autonomní varianta

Výroky (5)-(6) se týkají jedné aplikace přesné U a poté T kroků
volného W_pair. Časově nezávislý H_tot ze spektrálního důkazu
realizuje za jedno období U současně s jedním volným krokem,
se započtenou interakční energií. Další autonomní období by
opakovala také U. Samočinné vypnutí po jednom zásahu nebylo
odvozeno. Důkaz proto netvrdí, že jednorázový protokol už má
vnitřní místní hodiny nebo hotový prostorový obvod.
