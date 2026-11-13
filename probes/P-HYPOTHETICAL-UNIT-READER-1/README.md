# Pracovní čtečka jednotkového přenosu

**Máme jeden konkrétní zákon, úplný stav a spustitelný model.**
Fyzikální status je pracovní hypotéza H. Podmíněné matematické výsledky jsou
candidate-T, L1, NON-CANONICAL. [Rezervace #1431](https://github.com/mathorn1973/twist-j/issues/1431).

Dva zdroje střídavě předávají jednotku společnému přijímači. Jeho skutečná
zásoba se mění; ukazatel se posune o stejnou hodnotu. Prázdný dárce obrátí
směr spojení. Přístroj si uchová kontext, podle kterého pozná, zda naposledy
proběhl přenos, zpětný přenos, nebo pouhý odraz.

Nově předpokládáme fyzickou dostupnost právě této vazby. Odvození z původního
U/J ani hotový laboratorní přístroj tento balíček nepředstírá.
[MODEL.md](MODEL.md) obsahuje celý zákon, důkazy, hypotézy a přesné meze.

## Zkusit model

Samostatný [model.py](model.py) potřebuje jen Python 3.10 nebo novější;
můžeš jej stáhnout a spustit přímo. Pro celý balíček použij větev
probe/P-HYPOTHETICAL-UNIT-READER-1. Následující příkazy platí z kořene
této větve veřejného repozitáře:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/model.py
~~~

Výchozí příprava má zdroje 2 a 1, přijímač 1, správné příznaky a ukazatel 1.
Výpis ukáže všech dvanáct souřadnic, poslední dopředný přenos a chyby
příznaků. Po dvanácti krocích se vrátí celý stav.

Změna přípravy a počtu kroků:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/model.py --sources 1 1 --receiver 2 --steps 4
~~~

Odpojení prvního přívodu:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/model.py --sources 3 1 --receiver 1 --enabled 0 1 --steps 12
~~~

Zpětný vývoj a úplný strojově čitelný výpis:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/model.py --backward --steps 12 --json
~~~

Záměrně vadný příznak prázdného prvního zdroje:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/model.py --state 0 0 1 1 1 0 1 0 1 0 1 1 --steps 1
~~~

Ve vadném příkladu je skutečný přenos nula a čtečka hlásí minus jedna.
Zákon chybu uchová. Správnost příznaků je proto součástí kalibrace.
Volba vlastního ukazatele pomocí přepínače --pointer dovoluje samostatně
zkoumat jeho počáteční odchylku.

## Co přesně zkoumáme

| Otázka | Předpověď hypotézy |
|---|---|
| Naváže druhý přenos na skutečný první výstup? | Ano: pro binární zdroje \(t\to t+a\to t+a+b\). |
| Funguje obsazený přijímač? | Ano, i při nezávisle zvoleném počátečním \(t\). |
| Co ukazuje pětihodnotový ukazatel? | Při \(p_0=y_0\bmod5\) vždy \(y\bmod5\); na \(N\le4\) přesnou celou zásobu po celý vývoj. |
| Určuje samotný konečný ukazatel poslední přenos? | Ne. Konkrétní vstupy 10 a 01 dají stejný ukazatel 2, ale poslední změny 0 a 1. Směry spojení je rozliší. |
| Co se stane na prázdném konci? | Směr se obrátí, zásoba i ukazatel zůstanou stejné. |
| Je proces úplně vratný? | Ano, včetně chybných příznaků a odpojených přívodů. |
| Může přístroj zaznamenávat navždy bez dalších zdrojů? | Má konečné periodické slupky; trvalý nevratný archiv tento model neslibuje. |

Čtečka posledního jednotlivého přenosu používá současný stav spojení,
fáze a příznaků, nikoli historii nebo vstupní štítek. Je při správných příznacích přesná i na větších
zásobách; tam už samotný ukazatel neukazuje celou zásobu.

## Nejsilnější posun: cena energie se testuje až po určení přenosu

Stejný zákon na stejné slupce \(N=6\) dává

\[
(3,2,1)\mapsto(2,2,2),\qquad
(2,3,1)\mapsto(1,3,2).
\]

Počáteční i konečný stav všech konečných přístrojových registrů je
v obou případech shodný.
V dosavadní rodině
\(f_c(n)=2\lfloor n/2\rfloor+c(n\bmod2)\)
jsou změny zásobní energie \(2-2c\) a \(0\).
Zachování obou přechodů tedy vynutí \(c=1\), i když připustíme libovolnou
společnou energii všech uvedených přístrojových registrů.

Pro celý neomezený obor a všechny nezávislé příznaky je výsledek silnější:
v oddělené třídě \(f(r_1)+f(r_2)+f(y)+A(h)\), při \(f(0)=0\), musí být
\(f(n)=\varepsilon n\). Při zapnutých obou kontaktech je úplná energie této
třídy \(\varepsilon N+C\). Jednotka \(\varepsilon\) ani její cena v joulech
nejsou odvozené.

Když požadujeme zachování jen na správně připravených příznacích, zbývá
ještě cena obsazenosti \(b[n>0]\), kterou může vyrovnat energie příznaků.
Tuto mez důkaz výslovně zachovává.

## Přesné ověření

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/verify.py
~~~

Zmrazená zkouška obsahuje všechny úplné stavy s \(N\le8\):
211 200 stavů včetně všech směrů, příznaků, ukazatelů, fází a vypínačů.
Z toho 26 400 má správné tři příznaky; ukazatel může mít nenulovou odchylku.

Hlavní a samostatně napsaný cyklický výpočet musejí vytvořit totožné přesné
výstupy včetně otisku celé tabulky přechodů. Dále se zkoušejí dva zápisy,
kontextová kolize, porucha, odpojení, energetické svědky a úplný návrat.
Obecné věty na nekonečném oboru stojí na důkazech v MODEL.md.

[PREREG.md](PREREG.md) vymezuje vstupy a falsifikátory;
[REVIEW.md](REVIEW.md) popisuje oddělený asistentský přezkum.
Po prvním dokončeném běhu budou EXPECTED.txt, RUN.md a RESULT.md obsahovat
skutečný výstup, záznam prostředí a výsledkový rozsah.
