# Přenos bez tabulky: malé vratné sčítačky

2026-10-29. NON-CANONICAL. Analytický návrh navazující na zmrazený
balíček `twist_general_carry_2026-10-28`. Původní balíček zůstává beze
změny. Tento text je předběhové odvození. Přesný veřejný rozsah kontrol určuje
PREREG.md; výsledky následného běhu budou v RESULT.md a RUN.md.

## Výsledek odvození

Tabulku 8245 řádků lze v každém kroku nahradit sčítačkami modulo
125 a 625. Dostáváme konkrétní horní meze pro násobení J v A_N:

    párové pulzy <= 136917 N,
    místní operace <= 255187 N + 32,
    paměť pro data a práci = 14N+22 pětihladinových buněk,
    s archivem = 15N+22.

Pro celé N-písmenové čtení:

    párové pulzy <= 136917 N²+N,
    všechny instrukce včetně přímé Fourierovy přípravy
        <= 392104 N²+36N.

Párová horní mez je více než 45krát menší než původní obecná mez
6249713 N. Cenou je větší pracovní paměť. Ani nový návrh netvrdí
optimální konstantu. Všechny následující počty jsou odvozené z
konkrétních operací; nový výpočet je musí zkontrolovat před označením
za výpočetně potvrzený výsledek.

Používáme přesně stejné dodané fyzické prostředky: místní operace,
SUM, sedmipulzní equality-add a desetipulzní multiply-add. Nepřidáváme
reset, nové čisté buňky během běhu, nové nominální úhly ani neodvozenou
univerzální bránu. Prostorové přepojování, fyzický řadič a skutečná
přesnost zůstávají samostatnými podmínkami.

## 1. Malý přenos při pětkovém sčítání

Pro x,y v {0,1,2,3,4} definujme h(x,y)=floor((x+y)/5). V F_5 platí

    h(x,y) = sum_(k=1..4) binom(x,k) binom(y,5-k).

Důkaz: Vandermondova identita dává pravou stranu jako binom(x+y,5),
protože binom(x,5)=binom(y,5)=0. Pro x+y=0..4 je nula; pro hodnoty
5,6,7,8 jsou celá čísla 1,6,21,56, tedy všechna jedna modulo pět.

Tabulky pomocných funkcí modulo pět jsou

    B2=(0,0,1,3,1), B3=(0,0,0,1,4), B4=(0,0,0,0,1).

H(x,y;e): e <- e+h(x,y) lze sestavit ze čtyř členů

    x B4(y), B2(x) B3(y), B3(x) B2(y), B4(x) y.

Každá jednoargumentová funkce B_k se vypočítá do čisté pomocné buňky
součtem equality-addů za její nenulové hodnoty. Po multiply-add se
pomocníci přesně odpočtou. Používají se dvě opakovaně využívané čisté
pomocné buňky. Přesná horní cena H je

    párové pulzy: 24+80+80+24 = 208,
    místní operace: 51+139+139+51 = 380.

Záporná varianta používá záporná cílová přičtení; cena je stejná.
Všechny stavební operace jsou přesné bázové permutace bez zbývající
relativní fáze.

## 2. Vratná sčítačka modulo 5^L

Vstupní A a cílové B jsou libovolná L-ciferná pětková čísla. Chceme

    (A,B,0) -> (A,B+A mod5^L,0).

Použijeme L-1 čistých přenosových buněk c_1,...,c_(L-1), c_0=0.
Dopředně pro i=0,...,L-2:

    c_(i+1) += h(A_i,B_i)
    B_i += A_i mod5
    c_(i+1) += c_i [B_i=4]
    B_i += c_i mod5.

Na nejvyšší číslici pouze přičteme A_(L-1) a c_(L-1). Člen
c_i[B_i=4] se provede equality-addem do příznaku, multiply-addem
a zrušením příznaku, za 24 párových a 51 místních operací. Přenos
zůstává bit: jestliže h(A_i,B_i)=1, mezisoučet po odečtu pěti je
nejvýše tři, a druhý přenos tak nemůže nastat současně.

Přenosy smažeme odzadu, aniž bychom změnili výsledné B. Pro výslednou
číslici z=B_i platí

    c_(i+1) = [z<A_i] + c_i[z=A_i]
             = h(A_i,4-z) + c_i[z=A_i].

První člen se odečte H po místním dočasném zrcadlení z -> 4-z.
Druhý člen se odečte po dočasném B_i -= A_i, spočtení příznaku
[B_i=0], multiply-add a obrácení obou příprav. Zpětné pořadí zajišťuje,
že potřebné c_i ještě existuje. Na konci jsou všechny pomocníci nula.

Bez vynechávání operací s c_0=0 stačí pro L>=2 horní meze

    A_L <= 468(L-1)+2 párových pulzů,
    B_L <= 872(L-1)+4 místních operací,
    L-1 přenosů + 2 pomocníci pro H.

Tedy A_3=938, A_4=1406, B_3=1748, B_4=2620 jako zvolené horní meze.
Pro L=1 je to obyčejný SUM. Inverse se provádí obráceným slovem bran
a odečítá A při stejné ceně. Sčítačka platí pro všechny vstupy A,B,
nejen pro přenosové stavy z původního automatu. Čistota pracovní paměti
je výslovná počáteční podmínka; celý obvod je unitární i mimo ni.

## 3. Koeficienty přenosu místo identifikátoru

Z předchozího důkazu pro všechny dosažitelné stavy víme |c_j|<=35.
Uložíme d_j=c_j+35 v {0,...,70}, každé d_j do tří pětkových buněk.
J má ζ-koeficienty u=(1,0,1,0), J^(-1) má u=(0,-1,-1,0).

Ve čtyřciferné pomocné bance S spočteme

    S = 35 + d_0+d_1+d_2+d_3 + (sum_j u_j)b.

Pro všechny přípustné přenosy a b=0..4 je 27<=S<=323<625. Proto

    a=S_0=S mod5, Q=(S_1,S_2,S_3)=floor(S/5)

jsou skutečný zbytek a podíl, nikoli podíl neznámého zabaleného čísla.
Původní celočíselný podíl q=(sum(c+ub)-a)/5 je Q-35. Dosazení do
starého přesného dělení λ dává

    d'_0 = 35+d_0+u_0 b-a-Q,
    d'_1 = 35+d_0+d_1+(u_0+u_1)b-a-2Q,
    d'_2 = 35+d_0+d_1+d_2+(u_0+u_1+u_2)b-a-3Q,
    d'_3 = Q.

Každý výsledek leží v 0..70 díky již dokázané obecné mezi dosažených
přenosů. Výpočet modulo 125 tedy vrátí přesný požadovaný kód. Přechod
nemusí mít uvedenou aritmetickou interpretaci pro libovolný nezasažený
12-ciferný kód, ale fyzické slovo je všude úplná permutace.

## 4. Přesný postup a účet jednoho kroku

Nová banka C_(i+1) i S začíná nulová. C_i je zachovaná vstupní banka.

1. Nastav S=35 dvěma místními posuny; přičti čtyři d_j a dvakrát
   přičti nebo odečti b. Celkem 6 sčítaček délky čtyři.
2. Nastav první tři výstupní koeficienty d'_0,d'_1,d'_2 na 35
   šesti místními posuny. Potom použij výše uvedené sčítání modulo125.
   Počty tříciferných sčítaček jsou pro J 4+6+9=19, pro J^(-1)
   3+6+9=18. Překopíruj Q do d'_3 třemi SUM branami.
3. Přičti a do příslušné výstupní číslice Y_i jedním SUM.
4. Zruš S obrácením bodu1. Všechny vnitřní sčítačky vracejí své
   pomocníky do nuly po každém použití.

Nový carry-kód se tvoří pouze do nulové banky. Místní počáteční posun
35 proto nepašuje předpoklad o přičítání konstanty do libovolného čísla.
Zpětný průchod provede tytéž přípravy S, obrácení bodu2 a zrušení S.
Obrácení bodu2 vrací C_(i+1) přesně do nuly. Výstup Y_i zachová.

Jeden dopředný krok má cenu

    J:       12 A_4+19 A_3+4 = 34698 párových,
             12 B_4+19 B_3+18 = 64670 místních;
    J^(-1): 12 A_4+18 A_3+4 = 33760 párových,
             12 B_4+18 B_3+18 = 62922 místních.

Zpětný krok má o jeden SUM méně. C_0 představuje sémantickou nulu,
tedy čtyři kódy35. Jeho počáteční nastavení a konečné vrácení stojí
16 místních operací na každé celé E_u. Dostáváme

    E_J:      <=69395 N párových, <=129338 N+16 místních;
    E_Jinv:   <=67519 N párových, <=125842 N+16 místních.

Stejné spojení E_J, skutečné SWAP, E_Jinv se záporným výstupem jako
v původním důkazu dává deklarované násobení na místě. SWAP stojí
3N párových a 7N místních operací. Odtud výsledek v úvodu.

## 5. Paměť a celá slova

Paměť se skládá z N datových buněk, N výstupních pomocných buněk,
12(N+1) přenosových buněk, čtyř buněk S, nejvýše pěti vnitřních
pomocníků sčítačky a jedné trvale nulové buňky pro rozšíření vstupů.
Celkem 14N+22. Nulová rozšiřující buňka se pouze čte; lze ji používat
pro více různých vyšších nulových číslic stejného vstupu.

N archivních buněk dává 15N+22. Každé násobení vrací celou pracovní
paměť do nuly. N násobení plus N zápisů dává P_word<=136917 N²+N.
Místní operace tvoří 255187 N²+32N z násobení, 2N ze zápisu a N
Fourierových příprav, tedy 255187 N²+35N. Součet je392104 N²+36N.

Hodiny, řídicí vazby, prostorové směrování, přípravné lázně a případná
ochrana proti skutečným chybám se účtují samostatně jako dříve.

## 6. Navržené povinnosti před prvním novým během

Před spuštěním nového enginu zmrazit tento důkaz, přesný kontrakt,
programy a piny původních tabulek. První výstupy zachovat bez přepisu.

1. Všech25 dvojic pro h, oba cílové směry a všech5 počátečních stavů cíle.
   Ověřit také návrat obou pomocníků a úplný rozklad do starých
   fázově ověřených primitiv.
2. Celá sčítačka pro L=1,2,3 na všech A,B (25,625,15625 dvojic),
   pro L=4 na všech390625 dvojicích, v obou směrech nebo s ověřením
   přesné inverze. Kontrola všech carry a pomocníků po každém příkladu.
3. Všech16490 hran obou původních uzavřených automatů: nový přechod
   ve ζ-koeficientech musí dát přesně stejné a,C'. Zkontrolovat rozsahy
   S i výsledných d' a úplné obrácení nového kódování.
4. Všech97655 slov délek1..7 přes úplnou nově vyhodnocenou přenosovou
   tabulku, přímá celookruhová identita v O a stejné mapové otisky.
   Celý vygenerovaný program, čistota práce a obě E_u s neprázdným
   cílem se ověří pro všechna slova doN3 a všechny dlouhé příklady.
5. Přesně stejných25 předem definovaných slov pro každé N=8,9,12,16,
   32,64,128 jako v původním kontraktu; žádný dodatečný výběr výsledků.
6. Celá archivní slova doN5, všechny3125 slov a120 nulových konců;
   stejné předem určené mapové hashe jako původní balíček.
7. Z vygenerovaného programu spočítat párové a místní instrukce
   bez rozvinutí všech matic; nesmí překročit odvozené horní meze.
8. Samostatný checker nesmí importovat nový aritmetický engine.
   Konečné kontroly oddělit od obecného důkazu a netvrdit druhou
   architekturu, pokud všechny běhy proběhnou na stejném stroji.

Samotné opakování starých testů novým matematickým vzorcem nestačí:
nová rizika jsou vrácení ripple-carry pomocníků, nechtěné zabalení S,
zaměnění digitového a celočíselného sčítání, a chybný pořadník mazání.
