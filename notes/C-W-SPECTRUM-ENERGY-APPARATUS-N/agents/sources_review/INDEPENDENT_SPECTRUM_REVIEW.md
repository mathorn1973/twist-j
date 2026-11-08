# Nezávislá analytická kontrola spektra a energetického přístroje

Datum: 2026-10-20. Autor kontroly: samostatný spolupracující agent.
Status: analytická kontrola; žádné vědecké numerické či symbolické spuštění.
Kontrola vychází z definice kontaktního W, nikoli ze zastaralých příloh.

## 1. Globální spektrální mezera: námitky prověřeny

Položme C=(I+2iX)/sqrt(5), g=2pi/5 a W_f=SG. Po změně souřadnic
k1=(P+q)/2, k2=(P-q)/2 je symbol W_f součinem dvou jednorozměrných
symbolů diag(exp(ik),exp(-ik)) C. Jejich vlastní hodnoty jsou
exp(+-i theta(k)), kde cos(theta(k))=cos(k)/sqrt(5). Proto

    theta(k) in [a,pi-a], a=atan(2).

Součet dvou takových úhlů leží v [2a,2pi-2a], rozdíl v
[-(pi-2a),pi-2a]. Celé spektrum volného W_f tudíž leží ve dvou
kruhových obloucích se středy 0,pi a poloviční šířkou

    b=pi-2a=2 atan(1/2).

Pro důkaz mezery postačí tato inkluze. Změna (P,q)->(k1,k2) pokrývá
polovinu dvourozměrného toru, což není překážka: společný posun obou k
o pi změní obě jednorozměrné matice znaménkem, jejich součin zachová.
Nesmí se bez kontroly používat nezávislá plná k-torusová parametrizace
pro jedno konkrétní pevné P; zde se skutečně bere sjednocení všech P,q.

Kontaktní projekce V může mít v plném prostoru nekonečnou hodnost.
To následující normový argument neomezuje. Pro Gamma=exp(-igV),

    ||exp(ig/2) W-W_f||
      = ||exp(ig/2) Gamma-I|| = 2 sin(g/4).

Normální resolventa W_f splňuje ||(z-W_f)^(-1)||=1/dist(z,spec W_f).
Neumannova řada proto umístí spektrum exp(ig/2)W do uzavřeného
chordového okolí spec W_f o poloměru 2sin(g/4). Obě spektra leží na
jednotkové kružnici; toto okolí znamená úhlové rozšíření nejvýše g/2.

Šířka původní mezery je delta=pi-2b. Platí

    cos(delta)=7/25,
    cos(g)=(sqrt(5)-1)/4 > 7/25,

protože poslední nerovnost je ekvivalentní 3125>2809. Jelikož oba úhly
leží v (0,pi), delta>g. Zbývající mezera má tedy zaručenou kladnou
šířku delta-g. Dva středy bezpečných řezů v ARGUMENTU vlastní hodnoty
lambda jsou

    alpha=3pi/10,  alpha-pi=-7pi/10.

To je globální výsledek pro celé W, včetně kontaktních větví. Není
odvozen pouze z lokální mezery vázané větve u P=0. Není to přesný popis
všech okrajů kontaktních pásem; jde o prokázané společné mezery.

## 2. Znaménko logaritmu a nulová hladina

Zvolíme-li Arg lambda in (alpha-2pi,alpha), pak

    H0=i Log(W),  exp(-i H0)=W,
    spec H0 subset (-3pi/10,17pi/10).

Vázaná větev má energii Omega(P), včetně Omega(0)=g. Tento přesný
generátor nemusí být nezáporný. Posun K=H0+3pi/10 I je nezáporná
energetická souřadnice pro konstrukci baterie; konzervace K+HA a H0+HA
je totožná. Nesmí se však psát exp(-iK)=W: skutečně se objeví konstantní
globální fáze exp(-i3pi/10). Pokud je vyžadován zároveň nezáporný
generátor i přesná matice W, vyhoví H0+2pi I; energie klidové větve se
pak změní na g+2pi. Žádná z těchto konstant nemění změnu energie D.

Analytická funkce log je definována na okolí celého spektra. Konečný
dosah W a resolventový výpočet dovolují exponenciální prostorový útlum
H0 a konečné komutátory s polohami. To není tvrzení o striktně konečném
dosahu H0. Předchozí zákaz přesného konečně dosahujícího generátoru
tak zůstává beze změny.

## 3. Konečná kapacita spojité baterie

Nechť po odečtení konstanty 0<=H<=h a V je libovolná cílová unita.
Baterie je L2([0,A],da), HA násobí energií a, A=L+2h. Toto je omezená
energetická kapacita, nikoli konečný počet stavů.

Spektrální rozklad H a změna proměnných t=E+a dávají přímý integrál
vláken

    H_t = ran 1_[max(0,t-A),min(h,t)](H).

Tvrzení platí i při spojitém či smíšeném spektru H: po změně proměnné
se integruje původní spektrální míra dmu(E) a Lebesgueova míra dt.
Pro t in [h,A] je H_t celým systémovým Hilbertovým prostorem. Zde
definujeme U_t=V; na ostatních vláknech U_t=I_Ht. Jde o měřitelný
unitární přímý integrál a přesně platí [U,H+HA]=0.

Baterii připravíme do reálného normalizovaného stavu

    b(a)=sqrt(2/L) sin(pi(a-h)/L), a in [h,h+L],
    b(a)=0 jinak.

Každá vstupní systémová energie E in [0,h] pak vede do t in [h,A].
Všechna výstupní E' in [0,h] zanechají a'=t-E' in [0,A]. Žádná
amplituda nenaráží na dolní ani horní konec baterie. Střední počáteční
energie je h+L/2, kapacita je A, norma derivace b je pi/L.

## 4. Nezávislá kontrola chybových konstant

Po nulovém prodloužení b na reálnou osu je na nominovaném vstupu
ekvivalentní popis Fourierovou proměnnou tau:

    V_tau=exp(i tau H) V exp(-i tau H),
    p(tau)=|bhat(tau)|^2.

p je sudá, integrál p je 1 a integrál tau^2 p je pi^2/L^2. Položme
D=V^*HV-H. Duhamelův vzorec dává ||V_tau-V||<=|tau| ||D||; proto
společná stavová chyba (i s libovolným pasivním referenčním systémem)
nepřevyšuje pi||D||/L.

Pro F(tau)=Ad(V_tau), L_H=i[H,.], platí

    ||L_H||_diamond <= h,
    F' = F o i[D_tau,.],  ||F'||_diamond <= osc(D),
    F''=[L_H,F'],         ||F''||_diamond <= 2h osc(D).

Sudost p odstraní lineární Taylorův člen. Pro polovinu diamantové
vzdálenosti redukovaného kanálu od Ad(V) dostáváme

    d_half_diamond <= pi^2 h osc(D)/(2L^2).

Pro samotnou práci je lepší použít přímo pozorovatelnou V^*HV=H+D.
Její dvojitý komutátor s H má normu nejvýše h^2 osc(D)/2. Proto

    |work_actual-work_ideal| <= pi^2 h^2 osc(D)/(4L^2).

Jsou-li díky analytickému logaritmu ||D_eta||,osc(D_eta)=O(|eta|),
stačí eta~1/q a L=q: společná chyba je O(q^-2)=o(eta) a chyba práce
O(q^-3)=o(eta^2). Nepotřebujeme chybný krok skalární Lipschitz =>
operatorová Lipschitz ani uniformní malost ||exp(i eta R)-I||.

## 5. Místní působení přístroje vyžaduje vlastní důkaz

Exponenciální útlum H neznamená automaticky uniformní prostorový útlum
celého U na všech bateriových stavech. I omezený interval energií má
neomezenou sdruženou Fourierovu proměnnou tau. Podmíněné operace
exp(i tau H)Vexp(-i tau H) mohou mít libovolně dlouhý efektivní čas.
Ostré hranice celkové energie rovněž nelze prohlásit za místní operace.

Na určeném vstupu b je naproti tomu dokázána malá prostorová odchylka:
jestliže V je diagonální v poloze a vstup leží v podprostoru poloh Q,
má výstupní amplituda mimo Q normu nejvýše pi||D||/L. Jemnější útlum
se vzdáleností lze získat rozdělením integrálu podle |tau|: pro krátké
casy použít exponenciální šíření H, pro dlouhé Chebyshevovu mez
int_|tau|>T p <= pi^2/(L^2 T^2). To je tvrzení o dané připravené
baterii, nikoli globální operátorový zákaz dalekého působení.

## 6. Co nebylo uzavřeno

- Příprava reálného spojitého koherentního stavu b je dodaný zdroj.
- Konečná energetická kapacita není konečný celočíselný nosič.
- Přesný energetický lift sám neposkytuje místní autonomní hodiny ani
  přepínač, který po požadovaném čase interakci zastaví.
- Opačné posuny dvou skutečných kopií W zachovají společnou translaci;
  rozklad podle jejich součtové energie zachová tuto symetrii. Přesná
  dynamika vnitřního řízení ani energetická cena přípravy tím nevznikají.
- Výběr hladké větve logaritmu je explicitní volba; nesmí se tvrdit,
  že globální mezera sama ruší všechny dřívější větvové nejednoznačnosti.

Závěr kontroly: globální mezera, konečná spojitá baterie a uvedené
chybové meze jsou analyticky slučitelné a skutečně zahrnují celé
spektrum W. Uvedená omezení zůstávají explicitní.
