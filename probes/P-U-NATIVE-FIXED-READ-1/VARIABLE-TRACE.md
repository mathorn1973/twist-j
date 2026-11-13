# Proměnná stopa: zákaz úplného kontaktu do vláknové dvojice

**NON-CANONICAL, candidate-T, L1. Analytická příloha.**

Tato příloha dává ruční důkaz pro libovolný pevný počet původních tiků.
Není založena na konečném výčtu a není rozšířením počtu tvrzení ověřovaných
konečným auditem ostatních částí balíčku. K tomuto důkazu nebyl spuštěn
nový vědecký program.

## 1. Přesná třída a tvrzení

Jedna původní buňka má šest souřadnic nad F5. Pro přehlednost zde píšeme

    (p1,p2,p3,p4,q,r) = (p₁,p₄,p₁′,p₄′,q,r).

Přijímač je pevná surová dvojice Y=(q,r). Čtyři písty se rozdělí do
dvou pevných dvojic X,A, zdroje a reference. Existují právě tři taková
neuspořádaná párování: 12|34, 13|24 a 14|23.

Předem zvolené místní přípravy jsou

    E_X:F5 -> F5², E_Y:F5 -> F5², E_A:F5 -> F5².

Všech 125 součinových příprav E(x,y,a), x,y,a∈F5, je přípustných.
Každý blok závisí jen na své hodnotě. Celková počáteční stopa smí být
libovolně proměnná.

Předem zvolené stejné místní čtečky R_X,R_Y,R_A závisejí pouze na
příslušné surové dvojici. Na vstupu čtou x,y,a. Nesmějí používat ostatní
bloky, zvláštní větev čtení podle hodin, nový pomocný registr ani
výběr doby odečtu podle dat. Kódy a čtečky smějí být nelineární;
žádný afinní předpoklad o nich se nepoužívá.

Vývoj začíná v původním čase 0. Pro jedno pevné m≥0 se použije
přesně U^m se skutečnými bity θ_n=popcount(n) mod 2.

**Tvrzení.** Pro žádné κ≠0 v F5 nelze na celém tomto součinu splnit

    R_X(π_X U^m E(x,y,a)) = x,
    R_A(π_A U^m E(x,y,a)) = a,
    R_Y(π_Y U^m E(x,y,a)) = y+κ(x−a),

se stejnými místními čtečkami jako na vstupu.

Jde výlučně o uvedenou polohu přijímače (q,r), původní počátek a
pevné společné m. Tvrzení neklasifikuje ostatní polohy přijímače,
společné čtení více bloků, pomocné nosiče, změny přípravy či čtení
v čase, řízení délky podle dat nebo novou interakci.

## 2. Přesné původní zákony a stopové větvení

Generátory v právě zavedeném pořadí souřadnic jsou:

    a(p1,p2,p3,p4,q,r)
      = (p2,p1,p4,p3,q,r)

    b(p1,p2,p3,p4,q,r)
      = (−p3,−p4,−p1,−p2,−q,−r)

    c(p1,p2,p3,p4,q,r)
      = (2−p3,1−p4+r,2−p1,1−p2−r,1−q,−r)

    d(p1,p2,p3,p4,q,r)
      = (2−p1,1−p2,3−p3,4−p4,1−q,1−r)

    e(p1,p2,p3,p4,q,r)
      = (2−p1,1−p2,3−p3,4−p4,2−q,1−r).

Při řídicím bitu t se skutečně vybere písmeno s indexem z+2t mod 5
v pořadí a,b,c,d,e. Stopové mapy pro z=0,1,2,3,4 jsou

    τ₀=(0,4,0,4,4),     τ₁=(2,1,1,3,1).

Stopa se vyvíjí jen podle své předchozí hodnoty a skutečného bitu.
Souřadnice q,r se v každém generátoru mění pouze podle q,r a
vybraného písmene. Proto je jejich celý vývoj určen počátečním
(q,r), počáteční stopou a původními hodinami.

První skutečné bity jsou 011. Po třech krocích všechny počáteční
stopy skončí v H₁:

    {0,1,2,3,4} -> {0,4} -> {1,2} -> {1}.

Tato fakta a původní zdrojový tříkrok jsou veřejně doloženy v
[PROOF.md PR 1428](https://github.com/mathorn1973/twist-j/blob/9de862afafd02ea3e49daf6e4567127dc2a01f2c/notes/C-U-RELATIVE-CONTACT-CHRONOLOGY-N/PROOF.md)
a v [úplném výsledku 1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909).
Následující konkrétní větve jsou jejich přímé ruční složení.

## 3. Nutná bijektivita obou dárcovských stop

Označme součet dvou souřadnic zdrojového kódu jako f(x),
referenčního kódu jako g(a) a přijímačového kódu jako h(y).
Počáteční stopa je

    z=f(x)+g(a)+h(y).

Jestliže f(x)=f(x′) pro x≠x′, pak při stejných a,y dostaneme
stejnou počáteční stopu i stejné počáteční q,r. Celý přijímačový
vývoj je podle části 2 totožný. Požadované koncové hodnoty se však
liší o κ(x−x′)≠0. To je spor.

Stejně musí být injektivní g. Na pětiprvkovém oboru jsou tedy f,g
bijekce F5 -> F5. Pro libovolné pevné a,y a libovolnou z lze
jednoznačně vybrat zdroj x s touto stopou. Různé z dávají různé x.

Tento nutný závěr platí pro libovolné nelineární přípravy. Ani h
zatím není předpokládáno konstantní či afinní.

Pro m=0 se přijímač vůbec nemění a požadavek je okamžitě nemožný.
Dále rozlišíme m=1, m=2 a všechny m≥3.

## 4. Jeden skutečný krok

### 4.1 Větev z=0 vynutí konstantní přijímačovou stopu

Při z=0 se vybere a, které q,r vůbec nezmění. Stejná přijímačová
čtečka proto vrátí y. Požadovaný zákon vynutí x=a.

Pro libovolné a,y existuje díky bijektivitě f přesně jedno x
v počáteční větvi z=0. Musí to být x=a. Proto pro všechna a,y platí

    f(a)+g(a)+h(y)=0.

Odtud h(y)=γ je konstantní a f(a)+g(a)=−γ.

Přijímačový kód je injektivní, protože jeho vstupní čtečka rozlišuje
všech pět y. Pět kódových bodů s q+r=γ je tedy celou přímkou tohoto
součtu. Souřadnice r při změně y proběhne všech pět hodnot.

### 4.2 Párování 12|34 a 14|23

Bez újmy obecnosti nazveme zdrojem dvojici obsahující p1. Výměna
rolí x,a pouze nahradí κ za −κ, které je rovněž nenulové.

Při z=2 působí c. Pro pevnou referenci a zvolíme jednoznačný zdroj

    x_c(a)=f⁻¹(2−γ−g(a))=f⁻¹(f(a)+2).

Toto je bijekce hodnot a na zdrojové hodnoty x. Zdrojový výstup má
první souřadnici 2−p3(a), zatímco jeho druhá souřadnice proběhne
s r všech pět hodnot: u páru 12 se r přičítá, u páru 14 odečítá.

Pro každou referenci tak získáme celý svislý sloupec surového
zdrojového prostoru. Dvě různé reference vyžadují různé zdrojové
odečty x_c(a), takže tyto sloupce nesmějí splývat. Je jich pět,
a proto pokryjí celou F5². Pevná zdrojová čtečka nutně má tvar

    R_X(v1,v2)=ρ(v1),

kde ρ je bijekce F5 -> F5.

Ze vstupního čtení plyne ρ(p1(x))=x, tedy p1(x) probíhá všech pět
hodnot. Větev z=3 je dostupná pro každý x vhodnou volbou reference.
Generátor d dává první zdrojovou souřadnici 2−p1(x). Zachování
zdroje vyžaduje

    ρ(2−p1(x))=ρ(p1(x))=x.

Injektivita ρ vynutí p1(x)=1 pro každé x. To je spor s pěti hodnotami.

### 4.3 Párování 13|24

Zdroj lze opět označit jako 13 a referenci jako 24.
Při z=2 působí c na referenci takto:

    (p2,p4) -> (1−p4+r, 1−p2−r).

Pro každou referenční hodnotu a a všechna y jde o celou přímku
součtu 2−g(a). Protože g je bijekce, těchto pět přímek pokryje
celý referenční prostor. R_A musí být funkcí samotného součtu.

Stejná čtečka na vstupních kódech dává a. Je proto na celé F5²
přesně R_A(v1,v2)=g⁻¹(v1+v2). Po c by muselo platit

    g⁻¹(2−g(a))=a,

a tedy g(a)=1 pro všechna a. To odporuje bijektivitě g.

Tím je vyloučen m=1 pro všechna tři párování.

## 5. Dva skutečné kroky

Na počáteční vrstvě z=1 vyberou bity 01 slovo b,b.
Na vrstvě z=2 vyberou c,c. Oba generátory jsou involuce, takže

    U² = Id na počáteční H₁,
    U² = Id na počáteční H₂

ve všech šesti buněčných souřadnicích; čas samozřejmě pokročí o dva.

Pro stejná a,y vyberme pomocí f dvě různá x₁,x₂ s počátečními
stopami 1,2. Oba koncové přijímače jsou totožný vstupní kód E_Y(y).
Požadované hodnoty y+κ(x₁−a), y+κ(x₂−a) jsou odlišné. Spor.

## 6. Úplné původní tříkroky

Nechť F_s označuje buněčný účinek U³ na počáteční H_s.
Přímé složení skutečně vybraných písmen dává:

    F₀ = e c a:
      (p4, p3−r, p2+1, p1+r+3, q+1, r+1)

    F₁ = d b b = d:
      (2−p1, 1−p2, 3−p3, 4−p4, 1−q, 1−r)

    F₂ = e c c = e:
      (2−p1, 1−p2, 3−p3, 4−p4, 2−q, 1−r)

    F₃ = d b d:
      (−p3, −p4, −p1, −p2, 2−q, 2−r)

    F₄ = d b e:
      (−p3, −p4, −p1, −p2, 3−q, 2−r).

Skládání na pravé straně působí zprava doleva; například první
chronologické slovo je a,c,e. Všech pět výstupů patří do H₁.

Zvláště pístové části F₁,F₂ jsou totožné, stejně jako pístové části
F₃,F₄. Rozdíly v každé této dvojici jsou pouze ve vláknové souřadnici q.

## 7. Přesný tvar libovolně dlouhého dalšího vývoje

Po čase 3 mají všechny přípravy tutéž stopu a dále vybírají ve
stejných časech stejná písmena z b,d,e. Jejich čtyři písty mají
společný střed

    c_*=(1,3,4,2).

Nechť B zamění p1 s p3 a p2 s p4. Vystředěné písty se při b
mění jako −B, při d,e jako −Id. Proto pro každý pevný m≥3 existují
ε∈{1,−1}, e∈{0,1} tak, že skutečný společný úsek od času 3 do m
působí na všechny přípravy jako

    p -> c_*+ε B^e(p−c_*).

Přesně ε=(−1)^(m−3); pro důkaz není třeba vypočítat e z hodin.
Souřadnice q,r mají ve stejném úseku tvary εq+α_m, εr+β_m,
kde α_m,β_m jsou společné konstanty. Rovnost koncových q,r v čase 3
proto přetrvá do času m.

Tento popis je skutečný původní vývoj, nikoli volný výběr slova.
Pístový normální tvar je rovněž odvozen v
[primárním výsledku 994](https://github.com/mathorn1973/twist-j/issues/994#issuecomment-5655607857)
a souvisí s kanonickým chráněným záznamem v
[MEMORY-PROOF.md](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md).
Předkládaná aplikace neprohlašuje jeho klasifikaci 313 tříd za nový výsledek.

## 8. Všechna m≥3: párování 12|34 a 14|23

V obou párováních B přehazuje celé dárcovské bloky.

Pokud e=0, zvolíme dvojici počátečních stop 3,4. Pístové části
F₃,F₄ jsou totožné a po společném pokračování mají permutační
část B. Pokud e=1, zvolíme dvojici stop 1,2; jejich totožná pístová
část po pokračování má opět permutační část B.

V obou případech závisí úplný koncový surový zdrojový blok pouze
na počátečním referenčním bloku a společných konstantách.
Žádný člen s r se v těchto dvojicích nevyskytuje.

Ponechme a,y stejné a bijekcí f vyberme dvě různá x odpovídající
oběma zvoleným stopám. Zdrojové konce jsou totožné, ale zdrojová
čtečka má vrátit dvě různá x. Spor. Tento krok dokonce nepotřebuje
rovnost vstupního a výstupního čtecího vzorce.

## 9. Všechna m≥3: párování 13|24

Označme zdroj jako 13 a referenci jako 24. Následné B oba bloky
zachovává a pouze uvnitř nich přehazuje souřadnice.

### 9.1 Zachování zdroje vynutí h(y)=γ

V počáteční větvi z=0 má F₀ zdrojový výstup

    (p1,p3) -> (p4,p2+1).

Závisí pouze na referenčním kódu. Ani společné další pokračování
nepřidá závislost na q,r nebo původním zdroji.

Pro pevné a a každé y vyberme x=f⁻¹(−g(a)−h(y)), aby počáteční
stopa byla 0. Všechny tyto zdrojové konce jsou stejné. Zachování
zdroje a injektivita f proto nutí h(y)=γ konstantně.

Stejně jako v části 4 přijímačový kód pokryje celou přímku
q+r=γ a r(y) proběhne všech pět hodnot.

### 9.2 Referenční čtečka je nuceně funkcí součtu

Ve větvi z=0 platí f(x)=−g(a)−γ. Referenční výstup F₀ je

    (p2,p4) -> (p3−r,p1+r+3).

Pro každé a a všechna y je to celá přímka součtu

    f(x)+3 = −g(a)−γ+3.

Společný střed má na dvojicích 13 i 24 součet 0. Pokračování z
části 7 tedy změní referenční součet přesně na

    ε(−g(a)−γ+3),

bez další konstanty. Celou přímku převede bijektivně na celou přímku.
Protože g je bijekce, takto získané přímky opět pokryjí celou F5².

Pevná R_A proto závisí pouze na součtu. Vstupní rovnost
R_A(E_A(a))=a a bijektivita g pak určují na celém prostoru

    R_A(v1,v2)=g⁻¹(v1+v2).

### 9.3 Další větve vynutí ε=−1 a γ=3

Ve větvích F₁,F₂ je referenční pístový součet −g(a). Po společném
pokračování je −εg(a). Zachování reference vyžaduje

    g⁻¹(−εg(a))=a

pro všechna a. Proto −ε=1, tedy ε=−1. Pro ε=1 již máme spor.

Pro ε=−1 má větev z=0 konečný referenční součet g(a)+γ−3.
Stejné čtení a zachování reference tedy vynutí γ=3.

### 9.4 Při γ=3 nastane neodstranitelná přijímačová kolize

Kód q+r=3 obsahuje přesně jeden přijímačový vstup s

    (q,r)=(3,0).

Ponechme jeho hodnotu y a referenci a stejné. Bijekcí f vyberme
různé x₀,x₂ s počátečními stopami 0,2. Podle části 6 mají obě
historie v čase 3 totožný přijímač:

    F₀:(q,r)=(3,0) -> (4,1),
    F₂:(q,r)=(3,0) -> (4,1).

V čase 3 mají obě celé buňky stopu 1. Jejich další společné
vybrané kroky proto zachovají totožnost q,r až do stejného času m.

Požadované koncové hodnoty se přitom liší o κ(x₀−x₂)≠0.
Stejná přijímačová čtečka z totožné surové dvojice je nemůže vrátit.
To je poslední spor.

## 10. Co je uzavřeno a co zůstává mimo důkaz

Případy m=0,1,2 a všechny m≥3 pokrývají libovolný pevný počet
skutečných původních tiků. Důkaz tedy uzavírá proměnnou počáteční
stopu pro přijímač (q,r) a všechna tři párování pístových dárců,
včetně libovolných nelineárních součinových kódů a místních čteček
v uvedené třídě.

Výsledek neříká, že původní buňka nikdy nepřenáší informaci.
Jednorázové kladné zápisy z vláknového zdroje do čtyřpístového
přijímače mají opačný směr a jiné rozdělení 2+4. Tento důkaz je
nezahrnuje. Rovněž neklasifikuje smíšený přijímač (q,p_i) nebo
(r,p_i), jiné přípravné rodiny, společné čtení, časově závislé
rozhraní, pomocné banky či skutečnou mezibuněčnou interakci.

Není ztotožněn žádný konečný buněčný invariant s energií, teplem
nebo fyzikální událostí. Canon ani status předchozích výsledků se
touto analytickou přílohou nemění.

Autor: A. M. Thorn. Původní důkaz Apache-2.0.
