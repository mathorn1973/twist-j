# Koncový účet kandidáta E/R

**NON-CANONICAL / ZMRAZENÝ KONTRAKT / RESULT-EXPOSED.**
Veřejná rezervace: #854. Počet vědeckých běhů při pinu: nula. Podpůrný matematický kontrakt
sondy `P-QDD-STABILIZER-APPARATUS-1`. Není to fyzický zákon vzniku události,
přijatý reset podle #539 ani výsledek formálního běhu. Formální program před
veřejným pinem neběžel. Veřejná věta `DECODER-RESERVOIR-RECORD-ACCOUNTING`
už obsahuje obecnou zásobníkovou bilanci a prahové účty; ty zde netvrdíme
jako nově objevené. Novou kontrolovanou kompozicí je konkrétní obvod E/R,
jeho úplný koncový výstup a tento přesně určený stavový protokol.

## 1. Hranice kompozice a úplný typ

Všechny následné systémové analyzátory stojí **před** koncovým zásobníkem.
Přímé rozhraní `terminal(k, variant, v)` vrací pro E dvojici pětirozměrných
vektorů `(Pv,Qv)` a pro R čtveřici `(K0v,K1v,K2v,K3v)`, odvozenou přímým
obvodem. Každý vektor má nulový součet souřadnic. Rovnost celého výstupu
znamená uspořádanou rovnost podepsaných vektorů; rovnost jejich energií
je slabší relace. Nula je přípustný vstup a vrací všechny nulové větve.

Kontext je neměnná trojice `(setup, channels, epsilon)`: přesné předem
zvolené zapojení, uspořádané různé názvy výstupů a racionální práh
`epsilon>0`. Samotný textový identifikátor nedokládá fyzickou realizaci.
V auditované kompozici jsou `setup=stabilizer-E-k0` atd. a kanály E
`(LOW,HIGH)`, kanály R `(r0,r1,r2,r3)`. Čtení HIGH u R sčítá značky
kanálů r1,r2,r3 až po jejich samostatném prahování.

Úplný stav tvoří kontext, neměnný archiv dokončených běhů a jeden aktuální
běh. Běh nese své pořadové číslo, počáteční životní počty jednotlivých
kanálů, úplný seznam dávek a příznak `closed`. Každá dávka nese:

- číslo běhu a pořadí impulsu bez mezer, včetně nulových impulsů;
- všechny podepsané výstupní vektory a samostatně předanou vstupní energii;
- intervaly nových životních pořadových čísel v označených kanálech;
- aktuální počty a zbytky každého kanálu v tomto běhu.

Podepsané vektory zůstávají fyzikálně pouze **modelovými amplitudami**.
Digitální kopie těchto čísel není experimentálním důkazem uchování pole.
Pole, z něhož by vznikly skutečné značky, zde není identifikováno.

## 2. Přesné operace

`ready` připraví běh 0, žádnou dávku a nulové počty. `deposit` nejprve
ověří celý stav a úplnost výstupů. Pro vstupní energii e a výstupy x_r
požaduje přesnou rovnost `e=sum_r ||x_r||^2`. Chybějící větev či ztráta se
nesmí dodatečně normalizovat. Případné ztrátové kanály potřebují nový
předem pojmenovaný kontext; současná sonda je bezeztrátová.

Modelový koncový krok je ortogonální výměna `(x_r,0)->(0,x_r)` s čerstvým
nulovým místem zásobníku. Energie se uloží jednou. Dosavadní dávky se
zachovají a připojí se nová. Pro kumulativní energii aktuálního běhu

\[
 H_r(n)=\sum_{t<n}\|x_{t,r}\|^2
\]

jsou nové účty

\[
 N_r(n)=\lfloor H_r(n)/\epsilon\rfloor,\qquad
 c_r(n)=H_r(n)-\epsilon N_r(n),\quad 0\le c_r(n)<\epsilon.
\]

Je-li životní počet na začátku běhu l_r, dávka vydá právě čísla
`l_r+N_r(n-1)+1,...,l_r+N_r(n)`. Rozsah může být prázdný. Pořadí kanálů
v serializaci není tvrzením o fyzickém časovém pořadí současné dávky.

`read` vrací totožný úplný stav. `end` uzavře aktuální běh; opakované END
je idempotentní, DEPOSIT po END je odmítnut. END je administrativní hranice,
nikoli důkaz fyzické terminality. `reset` archivuje celý aktuální běh
včetně amplitud, zbytků a počtů a připraví nový běh s nulovými **lokálními**
počty. Životní pořadová čísla navážou. Kontext zůstane stejný. Archivovaná
energie se nevymaže, nevrací se zdroji a nepřipočítá se k novému běhu.

RESET sám nezavádí další impuls ani nedodává energii. Každá nová příprava
je samostatný externí vstup s přiznanou energií. Toto rozhraní není resetem
zbytkové dekodérové vlny a nenahrazuje nynější `REJECTED_RESET_DISABLED`
v TRC1. Odvození resetu fyzického přístroje zůstává u #539.

## 3. Univerzální invariant konečných historií

Pro každou konečnou posloupnost těchto operací platí

\[
 E_{\rm supplied}
 =E_{\rm signed\ store}
 =\sum_{\text{archivované i aktivní běhy }j}\sum_r
       (\epsilon N_{j,r}+c_{j,r}).
\]

Důkaz je indukcí podle operací. READY dává nuly. Ortogonální obvod a
výměna při DEPOSIT přidají na obou stranách stejnou přesnou energii;
jednoznačný celočíselný podíl a zbytek ji pouze jinak zapíší. READ a END
energii ani dávky nemění. RESET přesune celý jeden účet do archivu,
nikoli mimo součet. Nulový impuls přidá nulovou energii a žádnou značku,
ale zůstane jako výslovně zaznamenaný vstup. Z indukce také plyne, že každé
životní pořadové číslo je vydáno právě jednou a staré dávky jsou prefixem
nové historie včetně přechodu do archivu.

Při uchování kontextu a úplného podpisového zásobníku lze terminální
výměnu obrátit. Pouhé počty/zbytky podepsané amplitudy neobnovují. Rovnost
koncových energií proto neopravňuje ztotožnit úplné přístrojové stavy.

## 4. Rozhodnutelné důsledky paměti

Pro shodné opakované vstupy s energiemi e_r a E=sum e_r>0, bez resetu,

\[
 N_r(n)=\lfloor ne_r/\epsilon\rfloor,\qquad
 N_r(n)/\sum_sN_s(n)\longrightarrow e_r/E.
\]

Jde o n nových příprav s celkovou dodanou energií nE. Tento limit nelze
získat neomezeným pokračováním jedné přípravy s konečným rozpočtem.
Pro m výstupů a nE/epsilon>m je absolutní chyba každého podílu nejvýše
`m/(nE/epsilon-m)`: pišme N_r=ne_r/epsilon-delta_r, 0<=delta_r<1,
a odečtěme e_r/E. V čitateli je rozdíl `(e_r/E)sum(delta_s)-delta_r`
s absolutní hodnotou nejvýše m. Při nulovém součtu počtů podíl není
definován. Při měnících se vstupech se váží energie, nikoli počet pokusů.

Je-li e_r/epsilon=a/b v základním tvaru, přírůstky mají periodu b.
Perioda je přesně b: při periodě d musí být součet přírůstků za d kroků
roven da/b, tedy celočíselný, a proto b dělí d. Nulový tok má b=1.
Současný vícekanálový tok má periodu nejmenšího společného násobku těchto
b. Tento přesný deterministický model má tedy konkrétní testovatelný
časový vzor; náhodné fáze nebo jiný rozptyl by byly novými předpoklady.

Pro e_a=e_b=epsilon/2 dává každý lichý impuls nula značek a každý sudý
impuls dvě značky, po jedné v obou kanálech. Reset po každém impulsu
nedá žádnou značku, ačkoli veškerá dodaná energie zůstává v archivu.
Tím se odděluje poměr intenzit, poměr počtů a výlučný výsledek přípravy.

Rovněž obecně platí

\[
 0\le\left\lfloor\sum_{r\in H}H_r/\epsilon\right\rfloor
          -\sum_{r\in H}\lfloor H_r/\epsilon\rfloor\le |H|-1.
\]

Plyne to rozkladem každého H_r/epsilon na celé číslo a zlomek v [0,1).
Sloučení energií před prahem je jiný detektor. Ve zmrazeném R se nejprve
prahuje po cestách a potom sčítají HIGH značky.

## 5. Nejistota a hranice důkazu

Pro nezávisle dodaný interval kumulativní energie [h-,h+] je počet určen
právě tehdy, když oba krajní body mají stejný celočíselný podíl prahem.
Jinak `threshold_interval` vrací `AMBIGUOUS` a celý rozsah možností;
uzavřený interval končící na prahu už obsahuje vyšší počet. Tato funkce
neodhaduje fyzické chyby a žádný interval nefitujeme daty.

Podpůrný auditor kontroluje všechny k a oba obvody na nule, všech pěti
simplexových vstupech a deseti rozdílech, v obou pořadích impulsů,
s uchovanými starými stavy a resetem mezi běhy. Nezávislá kumulativní
rekonstrukce z celého seznamu amplitud ověřuje účty i všechna vydaná
pořadová čísla. Další pevné kontroly pokrývají periodicitu 2/3,
dvojici půlkvant, archivaci, čtení, END, chybný kontext, chybějící kanál,
záměnu energie a poškození minulých dávek. Konečný audit nenahrazuje
výše uvedený indukční důkaz pro všechny konečné historie.

Tato sonda zůstává podmíněným matematickým modelem přístroje. Nevydává
modelovou dávku za uskutečněnou událost L5 a nevytváří míru L6.
`feeds_U=false`; průchod od Omega,U, nezávislá fyzická realizace, vlastnictví
fází a zákon jednotlivého výsledku vyžadují vlastní veřejné podklady.
