# Kontaktní přenos a ochrana dvou záznamů

NON-CANONICAL. Návrh jedné podmíněné L1 věty k veřejnému přezkumu.
Veškerá aritmetika níže probíhá v F5, kromě bitu eta a počtů stavů.
Skládání map se čte zprava doleva; vypsané prováděcí seznamy zleva doprava.

## Výslovné vstupy architektury

Úplný nosič je X = F5^12 × {0,1}. Stav je

    z = (p_x,q_x,r_x; p_y,q_y,r_y; eta),   p_i = (p1,p4,p1p,p4p).

Každá buňka má šest pětistavových souřadnic. Celkem |X| = 488281250.
Definujeme

\[
h(p_x,p_y)=3(p_{x1}p_{y4}+p_{x4}p_{y1})
            +2(p_{x2}p_{y3}+p_{x3}p_{y2}),\qquad
\delta=1_{\{h=0\}}=1-h^4.
\]

V tomto vzorci indexy 1 až 4 označují pozice v právě uvedené čtveřici,
nikoli přeznačení původního nativního pořadí.

Z původních jednobuněčných písmen používáme právě tyto mapy:

\[
\begin{aligned}
b(p,q,r)&=(-p_3,-p_4,-p_1,-p_2,-q,-r),\\
d(p,q,r)&=(2-p_1,1-p_2,3-p_3,4-p_4,1-q,1-r),\\
e(p,q,r)&=(2-p_1,1-p_2,3-p_3,4-p_4,2-q,1-r).
\end{aligned}
\]

Písmeno na jedné buňce nechává druhou buňku a eta beze změny. Každá z
těchto tří map je involuce. Označme B=b_x b_y. Potom B²=I a h(Bp)=-h(p).
Poslední identita plyne z prohození dvou bilineárních závorek a z 3=-2 v F5.

**W_b je přijatý vstup rozšířené architektury.** Položme
sigma(1)=sigma(2)=0, sigma(3)=sigma(4)=1. Jeho úplná definice je

\[
W_b(z)=
\begin{cases}
z,&h=0,\\
(B^{\,\sigma(h)\mathbin\oplus\eta}(p_x,q_x,r_x;p_y,q_y,r_y),\sigma(h)),&h\ne0.
\end{cases}
\]

Hodnota h v této definici se vyhodnotí na vstupu daného listu.
W_b není vydáván za slovo původní abecedy ani za odvozený fyzikální kontakt.
Čtecí vazby Ucal_i definované níže, jednorázová příprava a koncové čtení
jsou další výslovné vstupy téže architektury. Nevkládáme žádnou jinou bránu,
žádný mezilehlý reset, hodiny ani registr dokončení.

## Úplný kontaktní kontrakt

W_b je involuce. Je-li h nenulové a eta=sigma(h), je příslušný stav pevný.
Jinak první použití vykoná B, změní h na -h a nastaví eta na sigma(h).
Protože sigma(-h)=1-sigma(h), druhé použití opět vykoná B a obnoví původní
eta. Případ h=0 je identita.

Pro E_b=W_b B W_b a tau_i=e_i d_i dostáváme úplné mapy

\[
E_b(z)=\begin{cases}(B(p,q,r),\eta),&h=0,\\(p,q,r,1-\eta),&h\ne0,
\end{cases}
\qquad
\tau_i:(p,q,r,\eta)\mapsto(p,q+v_i,r,\eta).
\]

Zde v_i je jednotkový vektor v q=(q_x,q_y). E_b je involuce a zachovává h.
Tau_i má inverzi q_i↦q_i-1 a ostatní souřadnice nemění.
Položme f=(p_x,p_y,r_x,r_y,eta). Komutátor

\[
K_i=[E_b,\tau_i]=E_b\tau_i E_b^{-1}\tau_i^{-1}
\]

má na úplném nosiči přesný účinek

\[
\boxed{K_i(f,q)=(f,q-2\delta v_i)=(f,q+3\delta v_i).}
\tag{1}
\]

Na h=0 se skládá negace q, translace +1, negace q a translace -1;
výsledkem je q_i-2. Na h≠0 mění E_b pouze eta a s tau_i komutuje.
Tím jsou dokázány obě větve, včetně návratu všech pístů, obou r a bitu.
Inverze (1) je q_i↦q_i-3delta, ostatní souřadnice identické. Platí K_i^5=I.

Skutečné prováděcí slovo K_i je

    e_i,d_i,W_b,b_x,b_y,W_b,d_i,e_i,W_b,b_y,b_x,W_b.

Je to tau_i^{-1}, E_b^{-1}, tau_i, E_b v prováděcím pořadí.
Inverze provede přesně obrácený seznam. Všechny listy jsou involuce;
nejde o nahrazení skutečného slova novou makrobranou. Délka dvanácti listů
není tvrzena jako minimální.

## Jednorázová reference a úplná čtečka

Nejprve lze použít samostatnou referenci A={0,1,2}, kterou kontakt nemění.
Pro vložené provedení má r_i nadále všech pět hodnot F5. Na ně definujeme
permutace P_q tabulkou; poslední dva sloupce jsou fixovány.

| q | P_q(0) | P_q(1) | P_q(2) | P_q(3) | P_q(4) |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 1 | 3 | 4 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 2 | 1 | 0 | 3 | 4 |
| 3 | 1 | 0 | 2 | 3 | 4 |
| 4 | 1 | 0 | 2 | 3 | 4 |

Ucal_i ponechá všechny souřadnice kromě r_i a provede r_i↦P_(q_i)(r_i).
Je to involuce. V samostatné variantě provede stejnou tabulku na A a
původní r_i nemění. Čte právě q_i; nečte h, volbu experimentu ani jeho
mezistavy. Zápis Ucal_i (matematicky \(\mathcal U_i\)) se nezaměňuje s
původním autonomním U, jehož úplný stav obsahuje nativní čítač.
Dosavadní jednosměrný faktorový kontrakt takové čtení q zpět do faktoru
neposkytoval. Ucal_i právě toto rozhraní výslovně dodává. Kalibrace P_q
je pevná; přeznačení q by vyžadovalo odpovídající přeznačení celé tabulky.

Vyberme experiment O_i=I pro epsilon_i=0, O_i=K_i pro epsilon_i=1.
Epsilon_i je označení zvoleného experimentu, nikoli skrytý řídicí vstup
přístupný čtečce. Oba experimenty používají stejné pevné rozhraní

\[
\mathcal R_i=\mathcal U_i O_i\mathcal U_i.
\]

Pro s_i=3epsilon_i delta je její **úplná** mapa, i pro obsazený registr,

\[
q_i'=q_i+s_i,\qquad r_i'=P_{q_i+s_i}P_{q_i}(r_i),
\tag{2}
\]

s ostatními souřadnicemi identickými na konci. Z výstupního y_i=q_i'
se vstup obnoví přesně

\[
q_i=y_i-s_i,\qquad r_i=P_{y_i-s_i}P_{y_i}(r_i').
\tag{3}
\]

Písty se vracejí, proto se delta v inverzi vyhodnotí také z výstupu.
Inverzní listové slovo je obrácené slovo čtečky. Nelze je nahradit druhým
stejným použitím čtečky.

Při epsilon_i delta=0 je (2) identita na úplném nosiči. Při epsilon_i
delta=1 mají složené permutace r následující úplné řádky:

| vstupní q_i | výstupní q_i | obrazy r_i=0,1,2,3,4 |
|---:|---:|---|
| 0 | 3 | 1,2,0,3,4 |
| 1 | 4 | 1,0,2,3,4 |
| 2 | 0 | 1,2,0,3,4 |
| 3 | 1 | 1,0,2,3,4 |
| 4 | 2 | 1,2,0,3,4 |

Na jednou připravené vrstvě r_i=0 tedy r_i'=epsilon_i delta, bodově pro
každé neznámé q, bez předpokladu pravděpodobnosti. Aktivní h=0 dává
výsledky 0 a 1. Na h≠0 je samotný kontakt K_i=I, takže jej od identity
nelze rozlišit.

## Přesná třída minimální reference

Minimum tří stavů platí v této třídě: klasická konečná deterministická
vratná diskriminace jednoho volání I proti známé translaci
T:q_i↦q_i+3 na Q=F5². Vstup q je libovolný z celé Q, pevný aktivní
faktor je pouze divák. Jediná připravená reference je A v jedné společné
hodnotě 0; není vypůjčena jiná paměť. Před i po volání se smějí použít
libovolné, ale pro oba experimenty stejné vratné mapy na Q×A. Výsledek
se čte pouze z A. Není dostupná volba experimentu, h ani vnitřek volání.
Kodér a dekodér se nemusejí rovnat a smějí měnit q.

Nechť m=|A| a S je obraz Q×{0} po kodéru. Vratnost dává |S|=25.
Dokonalé rozlišení vyžaduje S∩T(S)=prázdná množina: společný bod by
stejný dekodér musel označit současně jako oba různé výsledky.
Translace na Q×A má 5m disjunktních pěticyklů. Na každém z nich může S
obsadit nejvýše dva ne-sousední body. Proto

\[
25\le 2\cdot5m,\qquad m\ge3.
\]

Tabulka P_q mez dosahuje s A={0,1,2} a přesnými koncovými hodnotami 0,1.
Nejde o minimum fyzických přístrojů, afinní syntaxe nad F5, délky slova
nebo vícevolacích protokolů. Povolení jiné paměti mění třídu.
Tři pracovní hodnoty jsou nutné na rozhraní testované operace; nejsou to
tři nově přidané stavy vloženého stroje.

| Rozlišení prostředků | Přesný význam |
|---|---|
| Samostatná reference A | má právě tři stavy; celý nosič zvětšuje třikrát |
| Vložený registr r_i | zůstává pětistavovou souřadnicí F5; nosič nezvětšuje |
| Pracovní hodnoty | 0,1,2 na vstupu a výstupu oracle při ready protokolu |
| Konečné výsledky | 0,1 po dokončení jednoho připraveného testu |

Uvnitř doslovného K_i může vložené r_i nabýt i 3 nebo 4. Kontakt vrací
r_i teprve na svém konci. Samostatné A se naproti tomu prodlužuje identitou
přes každý původní list. Konstrukce je kalibrovaná na I versus +3;
stejný význam pro každý jiný nenulový posun není garantován.
Například z q_i=2,r_i=0 dá první Ucal_i hodnotu r_i=2 a následující
první list e_i uvnitř K_i hodnotu r_i=4. Vložený přístroj se tedy
nesmí v mezikrocích omezit na nosič se třemi hodnotami r_i.

## Dva záznamy bez nové přípravy

Provedeme Bcal=R_y R_x a pouze na počátku připravíme r_x=r_y=0.
Druhá čtečka dostane **úplný skutečný výstup** první. Žádná souřadnice se
mezi čtečkami nevymaže, nezahodí ani znovu nepřipraví.

Pro libovolný vstup, včetně obou již obsazených registrů, je úplná mapa
Bcal dána rovnicí (2) současně pro i=x,y. Obě pístové čtveřice a eta se
vracejí; proto obě s_i používají tutéž počáteční delta. Rovnice (3) pro
oba indexy dává úplnou inverzi. Skutečná inverze nejprve vrací druhou a
potom první čtečku v opačném listovém pořadí.

Na připravené vrstvě dostáváme hlavní řetězec

\[
\boxed{
K_i\longrightarrow\mathcal U_iK_i\mathcal U_i
\longrightarrow(r_x,r_y)=(\epsilon_x\delta,\epsilon_y\delta)
\longrightarrow m_x=r_x^2.
}
\tag{4}
\]

Obě nulové čtečky se skutečně vykonávají jako Ucal_i,Ucal_i. Celkové
počty listů pro volby 00,10,01,11 jsou 4,16,16,28. Na neaktivní vrstvě
je úplná složená mapa identita i pro libovolná obsazená r.

## Ochrana po každém listu druhé čtečky

Druhé prováděcí slovo je buď Ucal_y,Ucal_y, nebo

    Ucal_y,e_y,d_y,W_b,b_x,b_y,W_b,d_y,e_y,W_b,b_y,b_x,W_b,Ucal_y.

Předem pevně volíme koncové matematické čtení m_x(z)=r_x(z)². Jeho
hodnota je určena také na každé diskrétní hranici listu. Jednotlivé listy
mají tento přesný účinek na libovolný úplný stav:

| List druhé čtečky | Účinek na r_x | Účinek na m_x |
|---|---|---|
| Ucal_y, e_y, d_y, b_y | r_x | r_x² |
| b_x | -r_x | r_x² |
| W_b | r_x nebo -r_x podle aktuální větve | r_x² |

Indukce přes skutečné listy dává pro každý prefix V_k, včetně k=0,

\[
\boxed{m_x(V_k z)=m_x(z)\quad\text{pro všechna }z\in X.}
\tag{5}
\]

Jde o obecnou invarianci, která nepotřebuje ready vrstvu, rovnoměrné q,
h=0 ani zvláštní eta. Proto po dokončeném prvním připraveném zápisu

\[
m_x(V_k\mathcal R_x z_0)=\epsilon_x\delta(z_0)
\]

na každé hranici druhé čtečky. Samotná ochrana nevyžaduje r_y=0; tato
příprava je potřebná k garantovanému významu druhého výsledku.
Protože listy jsou involuce, (5) platí i pro každý prefix obráceného slova.

Syrové r_x přitom invariantní není: z úplného nulového vstupu při
epsilon_x=epsilon_y=1 dává první čtečka q=(3,0), r=(1,0), p=0, eta=0.
Po pátém listu druhé čtečky b_x je r_x=4; po dvanáctém b_x je opět 1.
Na všech mezilehlých hranicích je m_x=1.

Obecný obor hodnot m_x je {0,1,4}: třídy jsou {0}, {1,4}, {2,3}.
Binární význam 0/1 má teprve po dokončeném prvním ready zápisu.
Hodnota 4 není obecně chyba. Ochrana prvního výsledku není ochranou
právě vznikajícího druhého výsledku.

## Zachované negativní hranice

Opakování celé aktivní čtečky na stejném registru splňuje

\[
\mathcal R_1^n=\mathcal U_iK_i^n\mathcal U_i,\qquad
r_i^{(n)}=P_{q_i+3n}P_{q_i}(r_i^{(0)}),\qquad \mathcal R_1^5=I.
\]

Z q_i=0,r_i=0 dostaneme po prvním testu (3,1) a po druhém (1,0).
Záznam se tedy může vymazat už při druhém použití. Další holý K_i
ponechává r_i na konci beze změny; to je jiná operace než celá čtečka.
Nejde o neomezený archiv, čítač, automatickou obnovu ani nezávislé opakované
měření s novou čistou referencí.

Nepoužitý vstup a dokončený nulový experiment jsou nerozlišitelné i
úplným stavem, neboť R_0=Ucal_i²=I. Bez samostatně dodané informace o
dokončení nelze r_i=0 ani m_i=0 vydávat za příznak uskutečněné události.
Do této sondy se taková informace ani její nosič nepřidává.

Univerzální reset neznámých výsledků 0 a 1 na ready0 při zachování všech
ostatních souřadnic není injektivní: při pevných aktivních pístech, bitu
a druhém registru r by slučoval 50 stavů Q×{0,1} do 25 stavů Q×{0}.
Inverze konkrétní čtečky vrací i q
a odstraňuje záznam; není restartem se zachovaným archivem.

Ochrana (5) není globální. Například d_x a e_x mění r_x=0 na 1; Ucal_x
při q_x=3 také mění 0 na 1. Samostatná reference zachovaná prodloužením
V×I_A má jiný kontrakt než vložený r_x vystavený těmto písmenům.
Jednorázové přiložení vazby pouze před kontaktem či pouze po něm při
plně neznámém q neposkytuje toto rozlišení: v prvním případě se reference
kontaktem nemění, ve druhém jsou možné vstupy čtení v obou větvích stejné.

Rovnice (5) se týká diskrétních hranic vypsaných listů, kde W_b je
výslovně přijatý list. Neříká nic o neznámé fyzické implementaci uvnitř
W_b ani o nerušivosti připojeného detektoru. Mapa r_x↦r_x² není nová
dynamická brána a do žádného pomocného registru se zde nezapisuje.
Kódování P_q a volba tohoto čtení nejsou odvozeny z J ani z autonomního U.
K_i je uzavřený faktorový kontakt s q translací, nikoli výměna bloků;
samotný tento konečný přenos nevybírá geometrický transport nebo fyzickou
křivost. Rovněž se nepřidává rozhraní pro čtení libovolného jiného posunu.
Žádný fyzikální, energetický, pravděpodobnostní či termodynamický předpoklad
se nepřijímá a žádný přechod L1 do jiné vrstvy se neuzavírá.

Entropická bilance původního autonomního U je samostatný výsledek jiného
kontraktu a není premisou (1) až (5). Tato sonda neodvozuje teplotu,
tepelnou cenu ani Landauerův vztah a nezavádí nový fyzikální zákon TWIST-J.
