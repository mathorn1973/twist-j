# Obecný přenosový obvod pro násobení J

2026-10-28. NON-CANONICAL. Vlastní důkazy pro všechna konečná N a přesný
rozsah následné konečné kontroly. Bez změny kánonu či registru. Používá se
Public Canon v106 s piny v SOURCE_MANIFEST.json, nikoli vnitřní v184.

## 1. Cíl a dodané prostředky

O=Z[ζ₅], λ=1−ζ₅, J=1+ζ₅², A_N=O/(λ^N). Každá třída má jednoznačné
číslice b_0,...,b_(N−1) v {0,1,2,3,4}. Chceme přesný vratný obvod
pro f_J(b)=digits_N(J Σ b_i λ^i) s vrácenou pracovní pamětí.

Zdrojové QDD-AFFINE-CONTROL-REALIZATION poskytuje podmíněný model
pětihladinových systémů: místní Fourier F, místní unitární ovládání,
párový H_ij=−ℏg N_i⊗N_j, N|j>=j|j>, g>0, a kompilaci mod5 přičtení.
Zde výslovně rozšiřujeme počet systémů a dostupnost adresovaných vazeb
na dvojice požadované obvodem. Prostorové přepojování se neúčtuje.
Řídicí pole, čisté počáteční buňky a zdroj práce jsou dodané prostředky.
Nenahrazují se za odvození z původního autonomního U.

Násobení v A_N a digitové sčítání ve F₅^N jsou různé operace. Obvod
používá druhou operaci uvnitř cílových registrů k realizaci první.

## 2. Všechny přenosy v jedné přesné identitě

Z Φ₅(1−λ)=λ⁴−5λ³+10λ²−10λ+5=0 plyne

    5 H(λ)=−λ⁴,  H(t)=1−2t+2t²−t³.

Polynomiální identita

    H(t)(1+2t+2t²+t³)=1−t⁶

dává formální řadu 1/H(t) s periodickými koeficienty

    α=(1,2,2,1,0,0,1,2,2,1,0,0,...).

Proto v A_N přesně

    5 = − Σ_(j≥0, j+4<N) α_j λ^(j+4).

Jde o konečnou kongruenci a λ-adický rozvoj. Není to tvrzení o konvergenci
komplexní mocninné řady při dosazení archimédovské hodnoty λ.

Při normalizaci koeficientu na pozici i napišme c_i=a_i+5q_i,
a_i∈{0,...,4}, q_i=floor(c_i/5). Pak přenos do každé vyšší dostupné
pozice i+4+j je −q_i α_j. Tato operace zachovává třídu a nezasahuje
již hotové nižší číslice. Poskytuje obecný normalizátor.

Pětiznaková formule 5=−λ⁴ už pro A₆ nestačí:

    5=−λ⁴−2λ⁵ modulo λ⁶.

Konkrétně x=3λ má po násobení J číslice (0,1,4,3,0,4). Zachování pouze
předchozího jediného přenosu z A₅ by dalo (0,1,4,3,0,0).

## 3. Automat s konečným stavem přenosu

Pro u∈{J,J^(-1)} zaveďme C_0=0 a postup po vstupních číslicích b_i:

    a_i = residue_λ(C_i+u b_i), zvolený v {0,1,2,3,4},
    C_(i+1) = (C_i+u b_i−a_i)/λ.

Inverzní jednotka je J^(-1)=−ζ−ζ²=−2+3λ−λ², neboť JJ^(-1)=1.
Dělení λ je přesné v O. V ζ-bázi t=C+ub, s=Σ_j t_j,
a=s mod5 a q=(s−a)/5 dává

    C'=(t_0−a−q, t_0+t_1−a−2q,
        t_0+t_1+t_2−a−3q, q).

Tedy pouze celočíselné operace. Pro každý prefix platí invariant

    u Σ_(i<n)b_i λ^i = Σ_(i<n)a_i λ^i + λ^n C_n.

Důkaz je součet přechodových identit po vynásobení λ^i; vnitřní
přenosy se vyruší. Po N krocích proto výstup udává přesně násobení u
v A_N. Koncový přenos C_N obecně není nula a fyzicky se nesmí zahodit
pod záminkou jeho automatického zániku.

### Konečnost pro všechny délky, před jakýmkoli výčtem

V ζ-bázi definujeme kladnou celočíselnou formu

    Q(C)=Tr(C Cbar)=5Σ c_j²−(Σ c_j)².

Pro a,b∈{0,...,4}:

    Q(Jb−a)=6b²−6ab+4a²≤96,
    Q(J^(-1)b−a)=6b²−4ab+4a²≤96.

Nejmenší modul konjugátu λ je sqrt((5−sqrt5)/2)>47/40. Tuto ostrou
racionální dolní mez potvrzuje 1791²>5·800². Norma odmocniny Q je
eukleidovská norma všech čtyř vložení, takže

    sqrt(Q(C')) ≤ (40/47)(sqrt(Q(C))+sqrt96).

Geometrická řada od C_0=0 pak dává

    Q(C_n)<153600/49, tedy Q(C_n)≤3134.

Pro každou souřadnici dále Q(C)≥(5/2)c_j². Lze to ukázat minimalizací
ostatních tří souřadnic při pevném c_j, nebo dokončením čtverců. Proto

    |c_j|≤35 pro všechny dosažitelné přenosy a všechny délky.

Příslušné dosažitelné množiny jsou konečné: nejvýše 71⁴<5¹¹ bodů.
Netvrdíme, že celá souřadnicová krabice je uzavřená pod přechodem;
mez je dokázána pro stavy dosažené od nuly.

Úplný výčet začíná v nule a prochází všech pět vstupů každého nového
stavu až do prázdné fronty. Žádná maximální délka se nepředpokládá.
Časový či paměťový limit před vyčerpáním fronty znamená pouze
nedokončený výčet. Analytický důkaz konečnosti na výčtu nezávisí.

## 4. Oba automaty jsou přesně propojeny

Z hrany λC'+a=Jb+C po vynásobení −J^(-1) plyne

    λ(−J^(-1)C')+b=J^(-1)a−J^(-1)C.

Transformace C→−J^(-1)C tedy převádí dopřednou hranu b/a na inverzní
hranu a/b. Pro dané C je b→a permutací pěti číslic, se směrnicí 2.
Tím pokrývá všechna inverzní vstupní slova a přesně celý dosah od nuly.

Obě minimální dosažitelné množiny proto mají stejnou velikost M.
Oba nezávislé úplné výčty musí souhlasit i na této korespondenci všech
hran, nikoli pouze na kardinalitě.

Každá tabulka má vlastní označení: nula má identifikátor 0, zbytek je
lexikograficky seřazen podle čtyř ζ-koeficientů. Identifikátor se ukládá
do q=ceil(log_5 M) pětihladinových buněk, nejnižší číslice první.
Význam jiného identifikátoru nemusí být v obou tabulkách stejný.
Nevyužité identifikátory mají v tabulkovém rozhraní s nulovými
příznakovými pomocníky nulovou akci na cíle.

## 5. Z pevné tabulky do dovolených pulzů

Následující rozklady odstraňují potřebu předpokládat obecnou univerzalitu
nebo neanalyzovanou vícenásobně řízenou bránu. Používají pouze zdrojové
párové interakce a místní operace. Všechny výsledné výpočetní brány jsou
bázové permutace s koeficienty +1, bez skrytých relativních fází.

### 5.1 Rovnostní přičtení y <- y+k[x=a]

Nejprve posuňme x tak, aby a přešlo na 4. Nechť S=(0 3)(1 2),
Nhat=diag(0,1,2,3,4), X je cyklický posun. Potom

    Nhat+S Nhat S = 3I+5|4><4|.

Dvě párové interakce D(θ)=exp(iθ Nhat_c Nhat_t), proložené S,
s θ=2πk/25 vytvoří požadovanou podmíněnou fázi a navíc místní fázi
exp(i3θ Nhat_t). K jejímu přesnému odstranění zvolme

    β=2π(25−3k)/250>0, k=1,2,3,4.

Pět opakování D(β) a následného posunu X na řídicím registru vrátí
řízení a přidá fázi exp(i10β Nhat_t)=exp(−i3θ Nhat_t), protože
celkový součet pěti navštívených hladin je 10. Celý zbytek je
exp(2πik[x=4]Nhat_t/5). Obalení F na začátku a F* na konci přičítá
k[x=4] do cíle. Nakonec vrátíme počáteční posun řízení.

Tato realizace má sedm kladných párových pulzů a nejvýše jedenáct
místních operací. Nepotřebuje pomocnou buňku ani neúčtovanou skalární
fázi. Posuny X a dvojitá transpozice S mají determinant +1. Párové
Fourierovy operace jsou skutečné vzájemné inverze, takže se jejich
případné konvenční globální fáze ruší.

### 5.2 Násobivé přičtení t <- t+xy

V F₅ platí přesně

    xyz=(x+y+z)³−(x+y)³−(x+z)³−(y+z)³+x³+y³+z³,

protože celočíselný koeficient 6 je modulo pět roven jedné. Místní
kubická fáze R₃|z>=ω^(z³)|z>, ω=exp(2πi/5), má determinant jedna.
Potřebné lineární součty vytvoříme přičteními do jednoho ze zúčastněných
registrů, aplikujeme fázi a součty zrušíme. Trojitý člen potřebuje čtyři
přičtení, každý ze tří dvojitých dva, jednoduché žádné.

Celkem deset zdrojových SUM bran a sedm místních kubických fází tedy
dává přesně diag(ω^(xyz)). Fourierova konjugace cílového z dává
t <- t+xy. Se zápornými fázemi dostaneme t <- t−xy. Cena je deset
párových a 29 místních operací, bez pomocné buňky. Platí na všech
5³ bázových vstupech, ne jen na bitech 0 a 1.

### 5.3 Jeden řádek libovolné tabulky

Pro r řídicích číslic a s cílových číslic použijeme 2r−1 čistých
pomocných buněk. Do prvních r spočteme indikátory rovnosti s daným
řádkem. Řetězcem r−1 násobivých přičtení do čistých buněk spočteme
jejich součin. Ten je jedna právě pro tento řádek. Podle něj přičteme
požadované výstupní hodnoty a všechny součiny a příznaky obráceně vrátíme
do nuly. Řídicí číslice zůstávají zachované; cíle mohou být neprázdné.

Na řádek jsou horní meze

    párové pulzy: 34r−20+s,
    místní brány: 80r−58+2s.

Nulové řádky i nulové cílové příspěvky smí překladač vynechat. Pro
tabulku přenosů stačí 5M řádků, protože ostatní identifikátory mají
definovanou nulovou akci na připraveném rozhraní. Vzniká úplná unitární
operace na celé bázi, včetně nevyužitých kódů. Tabulková interpretace
vyžaduje nulové příznakové buňky; ty se po každém řádku obnoví. Při
špinavých příznacích se nedeklaruje nulový účinek nevyužitého kódu.

## 6. Přenosy se skutečně vracejí do nuly

Pro jeden násobitel u sestavíme operaci

    E_u(X,Y,0)=(X,Y ⊕ f_u(X),0),

kde ⊕ je souřadnicový součet modulo pět, nikoli součet v A_N.

Pracovní paměť obsahuje C_0,...,C_N, každý o q buňkách, zpočátku samé
nuly. C_0 se nikdy nepřepisuje. Dopředný průchod pro i=0,...,N−1
podle (C_i,b_i) přičte kód C_(i+1) do jeho čistých buněk a výstupní
číslici do Y_i. Po dopředném průchodu jdeme i=N−1,...,0 a podle týchž
ještě dostupných (C_i,b_i) odečteme pouze kód C_(i+1). Všechny přenosy
se vrátí do nuly a Y zůstane.

Použitím záporného výstupního přičtení dostaneme E_u^(-1). Celý
obvod je unitární i na špinavých pracovních stavech; uvedená aritmetická
interpretace používá výslovnou počáteční nulu pracovní paměti.

Na místě realizujeme násobení následující úplnou posloupností:

    (X,0) --E_J--> (X,f_J(X))
          --SWAP--> (f_J(X),X)
          --E_(J^-1)^(-1)--> (f_J(X),0).

Poslední rovnost používá f_(J^-1)(f_J(X))=X, přesnou jednotkovou
identitu v A_N. Buffery se vymažou vratně, žádným resetem nebo odhozením.
Výměna dvojice pětic používá tři SUM brány a jednu místní negaci.

## 7. Cena jednoho násobení a celého slova

Označme R=5(M_J+M_(J^-1))=10M. Jeden dopředný řádek má r=q+1,
s=q+1; jeden zpětný r=q+1,s=q. Pro E_u tedy na jednu vstupní číslici
připadají horní meze (70q+29)·5M_u párových a (164q+46)·5M_u místních
operací. Dvě vyhodnocení a výměna bank dávají

    P_mul(N) ≤ K N,  K=(70q+29)R+3,
    L_mul(N) ≤ L N,  L=(164q+46)R+7.

Velikost dat a pracovního prostoru je

    N data + N buffer + q(N+1) přenosy + (2q+1) příznaky
      = (q+2)N+3q+1 pětihladinových systémů.

Pracovní buňky lze mezi násobeními opakovaně používat. Cena je O(N),
s konstantou stanovenou konečným automatem. Tabulkové rozklady jsou
záměrně konzervativní; nevydávají se za praktické optimum.

Pro N čtení d_n(J^n x), každé před příslušným násobením, přidáme N
nulových archivních buněk a N kopií SUM. Pak

    P_word(N) ≤ K N²+N,
    paměť dat, práce a archivu = (q+3)N+3q+1.

Příprava F^⊗N přidá N místních operací. Celkový počet místních a
párových instrukcí celého experimentu má proto horní mez

    T(N) ≤ [(234q+75)R+10]N²+4N.

Jedno násobení je tedy lineární, celá dosavadní konstrukce slova
kvadratická. Samostatná přípravná cena s čistými lázněmi z předchozí
poznámky není touto aritmetickou cenou nahrazena.

Pro samotné M_J je v tomto modelu nutná alespoň lineární cena: každý
výstupní digit k≥1 závisí netriviálně na vstupu k−1, s koeficientem −2
modulo pět. Přenosy z nižších pozic tuto závislost nezruší. Graf párových
interakcí proto musí spojit všech N datových registrů. Z produktově
čistých pomocníků je potřeba alespoň N−1 párových interakcí. Horní mez
má správný asymptotický řád; optimální konstanta ani prostorová cena
z toho neplynou.

## 8. Pevná sada pulzů a účtování řízení

Rovnostní brány používají θ/(2π)=k/25 a β/(2π)=(25−3k)/250;
obyčejné SUM používají k/5. Kubické fáze, Fourier, posuny a místní
permutace tvoří další pevnou konečnou sadu. Vše je nezávislé na N.
Není potřeba dodávat nominální úhly 2π/5^N při každém rozšíření paměti.

To neznamená konstantní požadavek na přesnost reálného přístroje:
chyby skutečných pulzů se mohou s délkou skládání hromadit. Tento
výsledek předpokládá přesné brány; toleranci ani opravu chyb neodvozuje.

Předchozí paměťová formule nezahrnuje hodiny a fyzické řízení. Je-li
plně rozvinutý program G_0,...,G_(T−1) dodán jako pevný word, přidáme
čítač o T stavech a úplnou matematickou unitární mapu

    V_N = Σ_(t<T) |t+1 modT><t| ⊗ G_t.

Je unitární, protože každý G_t je unitární a hodinové větve jsou
ortogonální. Od hodin nula provede přesně daný program a po T krocích
vrátí hodiny do nuly. Lze jej uložit do ceil(log_5 T) dalších pětic;
nepoužité hodinové kódy definujeme jako pevné body. Není to samočinné
zastavení ani záruka nového čistého archivu pro další oběh.

Toto výslovně určuje úplný diskrétní program s hodinami. Fyzické
vazby, které mají tento řadič uskutečnit, nejsou odvozeny z původního U
ani automaticky z dvoutělesových H_ij. Zadaný program a adresovatelné
ovládání jsou stále přiznané zdroje. Párové počty výše neobsahují
přepojování na omezeném prostorovém grafu.

## 9. Důsledek pro zdroj slov všech konečných délek

Z přesné přípravy F^⊗N|0>^⊗N, nulového archivu a čisté práce vzniká

    5^(-N/2) Σ_(y∈A_N) |J^N y>_data |Ψ_N(y)>_archive |0>_work.

Ψ_N je bijekce: jeho n-tá číslice závisí na novém b_n s nenulovým
koeficientem 2^n modulo pět a na nižším prefixu. Proto je redukovaný
stav celého archivu přesně I_(5^N)/5^N. Každý prefix má stav
(I_5/5)^⊗k. Žádné dodatečné dephasování není potřeba; úplný stav dat
a archivu přesto zůstává koherentní a provázaný.

Formální váha nulového součtu v O je tedy přesně

    N! / ((N/5)!^5 5^N), pokud 5|N; jinak nula.

Její asymptotika podél násobků pěti je sqrt(3125)/(2πN)². Nyní má
každý konečný člen této rodiny vlastní popsaný obvod s konečnou cenou.
Nevznikl jeden konečný aparát pro nekonečný proud, odvozená klasická
selekce jednoho výsledku ani nativní realizace v šestici F₅^6.

## 10. Co dokazuje výpočet a co důkaz

All-N závěr nese invariant, analytická konečnost, úplná kompilace
pevných tabulek a vratné vyčištění. Vyčerpání malých A_N ani dlouhé
příklady nejsou extrapolovány do obecné věty.

Konečný výpočet samostatně zkontroluje oba úplné přenosové uzávěry,
každou hranu a jejich vzájemnou korespondenci; všechny vstupy délek
1 až 7; předem určené delší vzory; návrat pomocníků; fyzické matice
primitivních bran; a skládání archivních slov. Nezávislý program
používá jinou celočíselnou bázi a žádný import hlavního enginu.

Obrovské úplné pulzní rozvinutí každé tabulky se při této kontrole
nesimuluje. Překladač jej umí vydat; jeho správnost je složením
ověřených přesných primitiv, dokázaného řádkového rozkladu a ověřené
aritmetiky. Spuštěná simulace velkého obvodu probíhá na úrovni těchto
doložených bloků. Žádný laboratorní pokus se netvrdí.
