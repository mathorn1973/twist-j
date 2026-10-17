# Výsledek: přesné místo chybějícího uzavření

PUBLIC / NON-CANONICAL / L1. Autorský analytický candidate-T.
Autor: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Veřejná rezervace: https://github.com/mathorn1973/twist-j/issues/1603

Úplné spojení fáze, energie a setrvačnosti zatím odvozeno není. Dvě přesné
podmíněné analýzy určují, co už funguje a kde se čtení rozcházejí.
Nejde o výsledek pokusu, novou fyzikální konstantu ani změnu Canonu.

## 1. Plošná fáze není automaticky časovým kmitočtem energie

V úplném stroji #1585 je skutečný přírůstek zaznamenané plochy
a=q Delta p=Delta u. Při návratu celého stavu je součet a přesně nula.
Čtyřkrokové úplné oběhy s celkovou energií nula a jedna dokazují:

    a=kappa E+beta+chi(Ts)-chi(s) modulo 5

nemůže na celém nosiči platit s nenulovým kappa nebo beta. Jediné řešení
koeficientů je kappa=beta=0; potenciál chi=u je poskytne na všech stavech.
Obecné kritérium součtů po úplných obězích je nutné i postačující a dává
přesný test pro budoucí nosiče. PROOF.md obsahuje jeho konstrukční důkaz.

Tento výsledek neruší netriviální fázi prostorové smyčky: ta může vrátit
q,p, ale změnit záznam u,v. Také není zákazem všech spojitých časových fází
nebo jiných fyzikálních energetických čteček. Testuje konkrétní plošný
přírůstek a úplný účet energie modulo pět.

## 2. U Diracova kroku souhlasí slupka a pohyb, frekvence ještě ne

Pro výslovně zvolenou porovnávací normalizaci W_m=D_m/sqrt(1+m^2)
platí na hlavní kladné větvi

    omega(0)=atan(m),    omega''(0)=1/m.

Zde m označuje bezrozměrný parametr kroku, nikoli již změřenou fyzikální
hmotnost. Při společném lineárním čtení E=A omega, p=B k a rychlosti
c=A/B vychází

    M_curv c^2/E(0)=m/atan(m)>1,  m>0.

M_curv je definována křivostí disperze. Není zde dokázanou odezvou
původního stroje na sílu. Výsledek vylučuje rovnost dvou čtení v této
přesné třídě, ne fyzikální vztah E0=M c^2. Společné jednotky poměr nezmění.

Kladný výsledek je rovněž přesný:

    Ehat=sqrt(m^2+sin(k)^2),    phat=sin(k),
    Ehat^2-phat^2=m^2,
    omega'(k)=phat/Ehat=dEhat/dphat.

Algebraická hmotnostní slupka tedy souhlasí se skupinovým posunem fáze.
Její energie a hybnost ale nejsou přímo časovým a prostorovým kmitočtem.
Globální čtení navíc zaměňuje k a pi-k; místní omezení větve tuto konkrétní
nejednoznačnost odstraní, nikoli rozdíl klidových čtení.

## 3. Konkrétní kladná cesta a otevřený úkol

V dodané rodině slabých kroků m=epsilon M platí přesná mez

    0 < M-atan(epsilon M)/epsilon <= epsilon^2 M^3/3.

PROOF.md uvádí i ostřejší dolní mez. Klidová frekvence se tedy v této
limitě přibližuje M. To je podmíněná cesta ke shodě; dosud není odvozena
taková rodina ani její hodiny z původního stroje a neřeší pevný parametr 2.

Další věcný cíl: dodat jeden přijatý dynamický děj a jedny hodiny, pro něž
frekvence, energetická čtečka a odezva pohybu dají tutéž hmotnost. Při zde
testovaném lineárním čtení musí už místně platit omega(0) omega''(0)=1
v jednotkách rychlosti bezhmotné větve. Nynější porovnávací krok dává
atan(m)/m<1. Tato podmínka určuje konkrétní požadavek na uzavření.

Obecná souvislost diskrétní Diracovy disperze a limit malých parametrů má
známou literaturu, např. A. Bibeau-Delisle et al.,
[Doubly-Special Relativity from Quantum Cellular Automata](https://arxiv.org/abs/1310.6760),
EPL 109, 50003 (2015). Novost této poznámky není tvrzena pro obecné vzorce;
jde o vyhodnocení přesně uvedených TWIST-J konstrukcí. Žádný externí kód
ani datová sada nejsou převzaty.

## Stav ověření a zveřejnění

Analytický důkaz a oddělená oponentura jsou rozlišeny v REVIEW.md.
Připravený konečný audit audit.py nebyl spuštěn: předběhový veřejný commit
se správnou autorskou identitou dosud nebylo možné publikovat. Není zde
žádný výpočetní PASS, EXPECTED.txt ani dvouarchitekturní vědecká reprodukce.
Podrobnosti a skutečné kontroly správy repozitáře uvádí CHECKS.md.
Všechny závěry zůstávají NON-CANONICAL; žádný fyzikální nebo nativní krok
není přijat tímto textem.
