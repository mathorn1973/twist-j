# Afinní součinové přípravy: úplný zákaz tří místních dvojic

**NON-CANONICAL, candidate-T, L1. Analytická příloha.**

Tato příloha používá ruční důkaz. Není dalším konečným výčtem ani
rozšířením vědeckých tvrzení ověřovaných programy tohoto balíčku.
K tomuto odvození nebyl spuštěn nový vědecký program.

## 1. Přesné tvrzení

Jednu původní buňku F5⁶ rozdělíme do tří pevných surových dvojic
X,Y,A, zdroje, přijímače a reference. Rozdělení má přesně velikosti
2+2+2. Každá má předem zvolený
afinní kód

    E_X(x)=v_X x+w_X, E_Y(y)=v_Y y+w_Y, E_A(a)=v_A a+w_A,

kde v_X,v_Y,v_A jsou nenulové dvouvektory nad F5.
Všech 125 součinových příprav x,y,a∈F5 je přípustných.
Žádná souřadnice jednoho bloku nesmí záviset na hodnotě jiného bloku.

Předem zvolené stejné místní čtečky čtou před vývojem x,y,a.
Smějí být libovolně nelineární, ale používají pouze svou surovou dvojici.
Vývoj začíná v původním čase 0 a pro celou přípravu se použije jeden
pevný počet m≥0 skutečných tiků U. Není přidána jiná operace, pomocný
nosič, datově závislé zastavení ani časově měněná čtečka.

**Tvrzení.** Pro žádné κ≠0 a žádné takové rozdělení, kódy, čtečky a m
nelze na všech 125 přípravách splnit

    x_out=x, a_out=a, y_out=y+κ(x−a).

Celková počáteční stopa zde nemusí být konstantní.
Její afinní tvar je

    L(x,y,a)=αx+βy+γa+δ.

Při proměnné stopě mohou mít jiné návrhy velikosti bloků 1+1+4 nebo
1+2+3; tato příloha je neklasifikuje.

Předpoklad afinních kódů je podstatný. Tato příloha neklasifikuje
obecné nelineární součinové přípravy na všech rozděleních.
Místní čtečky naproti tomu afinní předpokládány nejsou; v některých
případech si důkaz jejich afinní tvar teprve vynutí.

## 2. Použité přesné původní mapy

Stejně jako ve VARIABLE-TRACE.md píšeme
(p1,p2,p3,p4,q,r)=(p₁,p₄,p₁′,p₄′,q,r).

Označme

    A=(12)(34), B=(13)(24), c_*=(1,3,4,2).

Původní generátor a působí na písty permutací A, generátor b jako −B.
Generátory d,e mají totožný pístový odraz

    p -> (2,1,3,4)−p,

a totožné r -> 1−r; liší se jen q -> 1−q, respektive 2−q.
První skutečné bity jsou 011.

Úplné surové mapy jsou zapsány a odvozeny v
[VARIABLE-TRACE.md, částech 2 a 6](VARIABLE-TRACE.md).
Pro tento důkaz potřebujeme:

- U² je identita buněčných souřadnic na počáteční H₁ i H₂.
- U³ na počáteční H₀ dává
  (p4,p3−r,p2+1,p1+r+3,q+1,r+1).
- Písty U³ na H₁,H₂ mají stejný odraz −Id kolem c_*.
- Písty U³ na H₃,H₄ mají stejný tvar −B kolem c_*.
- r po U³ je 1−r na H₁,H₂ a 2−r na H₃,H₄.

Všechny přípravy jsou od času 3 na stejné synchronizované vrstvě.
Pro každý pevný m≥3 má jejich společné skutečné pokračování tvar

    p -> c_*+ε B^e(p−c_*), r -> εr+η,

kde ε∈{1,−1}, e∈{0,1} a η jsou společné, na datech nezávislé
hodnoty určené skutečným časovým úsekem. Konkrétně ε=(−1)^(m−3).

Proto se úplné koncové mapy původních větví 1,2 liší pouze v q.
Totéž platí pro větve 3,4. Jejich pístové permutace jsou v pořadí
obou dvojic B^e a B^(e+1); společné znaménko je −ε.
V každé dvojici je také r mapa totožná.

## 3. Dvě stopové vrstvy nedovolují skrytou závislost na stopě

**Lemma.** Nechť L je nekonstantní afinní funkce na F5³,
u≠v a F(t)=Mt+b je jedna společná afinní surová mapa.
Jestliže nějaká čtečka R obnovuje afinní cílovou veličinu
τ(t)=ℓt+c ze stejného F(t) na celé dvojici vrstev L=u a L=v,
pak ℓ patří do řádkového prostoru M.

**Důkaz.** Vezměme w∈ker M. Jestliže lineární část L má na w nulu,
body t,t+w v libovolné jedné vrstvě mají stejný surový obraz, a tedy
ℓw=0. Pokud L_lin(w)≠0, položme λ=(v−u)/L_lin(w)≠0.
Pro t ve vrstvě u leží t+λw ve vrstvě v a má tentýž surový obraz.
Znovu ℓw=0. Tedy ker M⊆ker ℓ, což je uvedená řádková podmínka. □

Čtečka v lemmatu nemusí být lineární. Zvláště když surový obraz
závisí pouze na y, nemůže na dvou různých vrstvách obnovovat
y+κ(x−a): jeho lineární část má nenulové koeficienty u x a a.

Použijeme také tento jednoduchý důsledek: pokud na jedné vrstvě
s volnými x,y surový výstup nějakého bloku bijektivně pokryje celou
F5² afinní funkcí x,y a požadovaný odečet je afinní funkcí x,y,
je pevná čtečka na celé F5² nuceně afinní. To plyne složením
požadovaného odečtu s inverzí této afinní bijekce.

## 4. Předem uzavřené případy

Je-li L konstantní, použije se úplný důkaz
[PROOF.md, část 8](PROOF.md): společné vybrané slovo má omezené
surové závislosti a nemůže dát tři potřebné místní účinky.
Tento důkaz dovoluje i neafinní kódy a čtečky.

Je-li přijímač přesně (q,r), použije se širší důkaz pro všechny pevné časy
[VARIABLE-TRACE.md](VARIABLE-TRACE.md), který dovoluje i
neafinní součinové přípravy a proměnnou stopu.

Pro m=0 se přijímač vůbec nezmění, takže nenulová κ nemůže fungovat.

Pro m=2 je na dvou počátečních vrstvách L=1,L=2 celé U² identitou
buněčných souřadnic. Přijímač má na obou stejný obraz E_Y(y).
Při nekonstantním L jej lemma z části 3 vylučuje pro každou polohu
přijímače.

Dále proto stačí nekonstantní L, m=1 nebo m≥3 a přijímače odlišné
od (q,r).

## 5. Každý přijímač, který neobsahuje q

Tato část výslovně zahrnuje jak libovolnou dvojici pístů,
tak smíšenou dvojici (r,p_i).

Pro m=1 mají počáteční větve 3,4 generátory d,e. Jejich účinek na
každou takovou přijímačovou dvojici je totožný a závisí jen na jejím
vlastním vstupním kódu E_Y(y). Lemma z části 3 dává spor.

Pro m≥3 zvolíme dvojici počátečních větví 1,2 při e=0, nebo 3,4
při e=1. Podle části 2 má vybraná dvojice totožnou koncovou mapu
na všech souřadnicích kromě q a její celková pístová permutace je Id.
Píst přijímače proto závisí jen na svém vlastním původním pístu.
Je-li v přijímači r, jeho mapa je rovněž stejnou afinní funkcí
původního r. Žádný člen s jiným vstupním pístem ani s cizím r zde
nevzniká.

Surový přijímačový obraz na obou vrstvách opět závisí pouze na y.
Lemma jej vylučuje. Tím jsou pokryty všechny přijímače bez q.

## 6. Smíšený přijímač (q,p_i), jeden skutečný krok

Zbývající čtyři souřadnice tvoří jeden dárcovský blok K=(r,p_j)
a jednu čistě pístovou dvojici D. Výměnou označení zdroje a reference,
doprovázenou κ -> −κ, můžeme D označit jako referenci a K jako zdroj.
Nulovost κ se tím nezmění.

Afinní souřadnice zapíšeme

    p_j=T x+t₀, r=R x+r₀,
    p_i=W y+w₀, q=V y+q₀.

Pak α=T+R a β=W+V. Referenční stopový koeficient je γ.

### 6.1 Větev d vynutí tvar donorové stopy

Na celé počáteční větvi L=3 působí d na přijímač pouze jeho
vlastním kódem E_Y(y). Při pevném y tedy musí být x−a konstantní
na přímce αx+γa=3−βy−δ.

Pokud (α,γ) není nenulovým násobkem (1,−1), je to nemožné:
buď se x−a po této přímce mění, nebo α=γ=0 a v některé neprázdné
vrstvě jsou x,a úplně volné. Nekonstantnost L v posledním případě
zajišťuje β≠0 a takovou vrstvu.

Proto nutně

    α=λ, γ=−λ, λ≠0,
    L=λ(x−a)+βy+δ.

### 6.2 Jedna skutečná výměna vynutí afinní referenční čtení

Alespoň jedna z permutací A=(12)(34), B=(13)(24) přehodí celou
pístovou dvojici D na její komplement {p_i,p_j}.
Pokud D není B-pár, použijeme původní b při L=1.
Je-li D B-pár, použijeme původní a při L=0.

Na této jediné původní větvi L=z_* platí

    a=x+(β/λ)y+(δ−z_*)/λ.

Hodnoty x,y jsou volné. Surový referenční výstup je až na pořadí
a společné znaménko právě dvojice (T x+t₀,W y+w₀).

Závislost požadovaného a na x vynutí T≠0. Kdyby W=0, injektivita
přijímačového kódu by dala V≠0, a tedy β=V≠0. Požadované a by
se měnilo s y při stejném surovém referenčním výstupu. To je spor.
Proto také W≠0.

Referenční výstup této větve afinně a bijektivně pokrývá celou F5².
Pevná čtečka R_A je proto podle části 3 na celé F5² afinní.

### 6.3 Stejné afinní čtení nesnese původní odraz

Na vstupním kódu čte R_A(E_A(a))=a. Větev L=3 je dostupná pro
každé a vhodnou volbou x, protože λ≠0. Původní d na referenci
působí odrazem c_D−E_A(a), kde c_D je pevná dvojice konstant.

Každá afinní R_A proto na tomto výstupu dává −a plus konstantu.
To nemůže být rovno a pro všech pět hodnot a. Tím je vyloučen m=1.

## 7. Smíšený přijímač (q,p_i), všechna m≥3

Ponechme označení K=(r,p_j) pro zdroj, D pro pístovou referenci
a koeficienty z části 6. Tvar α=−γ se zde nepředpokládá.

### 7.1 Referenční dvojice musí být B-pár

Jestliže D není B-pár, B ji přehazuje na její pístový komplement.
Z dvojic počátečních větví 1,2 a 3,4 vybereme tu, jejíž celková
pístová permutace je B.

Na obou těchto vrstvách je surová referenční mapa totožná, nezávisí
na r a vůbec neobsahuje vlastní referenční hodnotu a: všechny její
vstupní písty leží mimo D. Řádkové lemma z části 3 proto vylučuje
obnovu a. Nutně je D jeden z párů 13 nebo 24, a tedy j=B(i).

### 7.2 Závislosti ve větvi 0 vynutí γ≠0 a W≠0

Na H₀ má U³ pro D=13 pístový výstup (p4,p2+1);
pro D=24 je to (p3−r,p1+r+3). V obou případech jde o funkci pouze
x,y, bez vlastní referenční hodnoty a. Následné B^e ponechá dvojici D
na témže místě a tuto chybějící závislost nepřidá.

Kdyby γ=0, v každé neprázdné větvi L=0 by bylo možno měnit a při
stejných x,y i stejném surovém referenčním konci. Proto γ≠0.

Kdyby W=0, tato surová referenční mapa by závisela jen na x.
Injektivita E_Y však dává V≠0 a β=V≠0. Při pevném x a změně y
lze zvolit

    a=−(αx+βy+δ)/γ

tak, aby L=0. Referenční hodnota by se měnila při stejném surovém
výstupu. Proto W≠0.

### 7.3 Výměnná dvojice vynutí čtení zdroje pouze z r

Vyberme z dvojic 1,2 nebo 3,4 tu, jejíž celková pístová permutace
je B. Protože j=B(i), zdrojový píst p_j na konci závisí jen na
přijímačovém vstupním p_i=W y+w₀. Zdrojové r závisí jen na
R x+r₀. Pokud R=0, celá surová zdrojová mapa v této dvojici
neobsahuje x, což vylučuje lemma z části 3. Proto R≠0.

V jedné vybrané větvi jsou díky γ≠0 hodnoty x,y volné a a je určeno
stopovou rovnicí. Zdrojový výstup, jehož dvě souřadnice mají nenulové
koeficienty u y a x zvlášť, pokrývá celou F5².

Zachování x proto určuje pevnou zdrojovou čtečku na celém prostoru:
musí být afinní funkcí samotného r, s nenulovým koeficientem.
Na pístové souřadnici nemůže záviset, protože ta při pevném x
proběhne všech pět hodnot.

### 7.4 Dvě původní r-konstanty si odporují

Ponechme x,y stejné. Díky γ≠0 lze vybrat příslušné reference pro
počáteční stopu 1 a pro počáteční stopu 3. V čase 3 je jejich
zdrojové r podle části 2 rovno 1−r, respektive 2−r.

Společné další pokračování změní jejich rozdíl přesně na ε≠0.
Čtečka vynucená v části 7.3 je globálně afinní pouze v r a má
nenulový koeficient. Oba konce proto přečte odlišně, přestože oba
mají vrátit stejné x. To je spor.

Tím jsou vyloučena všechna m≥3 i pro poslední smíšené přijímače.

## 8. Rozsah úplného závěru

Předchozí části pokrývají konstantní i nekonstantní stopu, m=0,1,2
a všechna m≥3, přijímač (q,r), každou dvojici bez q včetně (r,p_i)
a každou dvojici (q,p_i). Nezůstává tedy žádné rozdělení do tří
pevných surových dvojic s afinní součinovou přípravou v uvedené třídě.

Využití libovolné nelineární místní čtečky proti důkazu nepomůže.
Všude se používá buď přesná kolize surových stavů, řádková nutnost,
nebo se afinní čtečka vynutí pokrytím celého místního prostoru.

Předpoklady se však nesmějí rozšířit: obecné nelineární přípravy
na ostatních polohách přijímače, jiné velikosti bloků včetně 1+1+4
a 1+2+3, společné čtení, jiný počátek, doba podle dat, pomocníci
a nové interakce
zůstávají mimo tento výsledek. Jednorázové kladné zápisy v rozdělení
2+4 z PROOF.md mu neodporují.

Důkaz nemění původní U, Canon ani fyzikální status modelu.
Nedokazuje obecnou nemožnost fyzikálního kontaktu a neurčuje energii.

Autor: A. M. Thorn. Původní důkaz Apache-2.0.
