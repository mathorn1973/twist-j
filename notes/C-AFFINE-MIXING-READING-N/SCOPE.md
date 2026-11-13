# Rozsah a návaznost na Public Canon v104

Stav: NON-CANONICAL, L1, candidate-T. Datum: 21. října 2026.

## Uzavřený matematický řetězec

1. Zachování odděleného účtu při jednom univerzálním racionálním promíchání vynutí kvadratické čtení; nezápornost vynutí shodu dvou předem různých čtení.
2. Potřebná matice je restrikcí již zadaného U_z₀ z JM-RETAINED-RATIONAL-PAIR-SOURCE, kde z₀=(1,0,0,0,0,0,0,0) má q(z₀)=4. Platí na celé invariantní rovině, nejen na připraveném vstupu.
3. Pět prokládaných buněk kóduje dvojici x,y∈K=Q(ζ₅). Všechny racionální vstupy této dvojice jsou pokryty. Celá afinní akce na témže kódu vzniká permutacemi pěti buněk.
4. Proto v úplné třídě nezáporných, v nule nulových, oddělených a při těchto operacích zachovávaných čtení platí f=g=c q₊. Nenulovost dává c>0, kalibrace určuje c.
5. Explicitní invariantní celočíselný podnosič s pevným společným jmenovatelem zachovává součet zadaných buněčných účtů bez zásobníku.
6. Stejná zdrojová involuce obsahuje i pevný referenční směr k₀=4e+t, kolmý k oběma promíchávaným směrům a se stejnou normou. Konstantní reference v pěti buňkách je pevná také při všech potřebných permutacích.
7. Oddělenost lze vyslovit jako nezávislost poměrů signál/reference na druhém signálu. S normalizací a zachováním referenční váhy pak bez předpokladu polynomiálnosti plyne právě trojice (1,cq₊(x),cq₊(y))/(1+c(q₊(x)+q₊(y))). Podmínky čtení jsou zde výslovné, nikoli odvozené ze samotné dynamiky.

Věta klasifikuje čtení slučitelná s již deklarovaným modelem a se skládáním jeho buněčných operací. Konstrukce zdroje JM už obsahuje metriku L. Není tvrzeno odvození veškeré kvadratické geometrie bez vstupních struktur. Realizace libovolného slova řadičem původního autonomního zdroje není automatickým důsledkem možnosti matematicky skládat jeho jednotlivé operace.

## Předpoklady výběrové věty

| Předpoklad | Úloha |
|---|---|
| Celý K×K nad Q | Smíšené rozdíly pokrývají všechny směry; žádné omezení na jedinou připravenou dráhu. |
| Čtení sestupuje na racionální amplitudy | Různé celočíselné zápisy stejného x,y nesmějí měnit f,g. |
| Účet má na daném kódu tvar f(x)+g(y) | Jde o dva logické kanály prokládané uvnitř buněk, nikoli o dvě celé JM buňky. |
| f,g≥0 a f(0)=g(0)=0 | Odstraní lineární a konstantní volnost a následně vynutí shodu čtení. |
| Zachování při všech vstupech promíchání | Vynutí druhý stupeň. Samotná existence operace neukládá libovolnému čtení, aby ji zachovávalo. |
| Zachování při současné afinní akci na obou kanálech | Dosazením jednoho nulového kanálu získáme afinní invarianci každého čtení; ta určí jedinou kvadratickou přímku. |
| Nenulovost a kalibrace | Vyberou kladné a případně číselně určené měřítko. |

Oddělenost účtu je skutečná podmínka. Součet čtvrtých mocnin norem celých JM buněk je také nezáporný a zachovává se při lokálních zdrojových involucích a výměnách buněk. Na novém kódu však obsahuje smíšené členy mezi x a y a nemá požadovaný oddělený tvar. Tím je přesně doloženo, co nová věta vylučuje a na základě čeho.

## Dvě výslovné podmínky pro normalizované čtení

`OPERATIONAL-READING.md` nahrazuje předem napsaný oddělený účet podmínkami na tři výsledkové váhy. Základní jsou P₀>0, nezápornost, normalizace a nulová váha nepřítomného signálu. Rozhodující jsou nezávislost P₁/P₀ na y a P₂/P₀ na x a zachování P₀ při operacích na signálech. Z nich se sčítavý účet odvodí jako 1/P₀−1. Jde o přesné převedení zbývajícího požadavku na čtení, ne o odstranění všech fyzikálních předpokladů.

Stejná dynamika připouští i jiná přiřazení výsledků, pokud se některá z těchto podmínek vypustí. Jednoznačnost normalizovaných vah navíc neodstraňuje libovolný společný kladný násobek nenormalizovaných vah. Hodnota c=2/25 používá kalibraci metrikou původního zdroje a konkrétní referenční amplitudu; obecná výběrová věta takovou hodnotu bez kalibrace neukládá.

`RATIONAL-EFFECTS.md` uvádí alternativní silnější předpoklad: jedinou nezápornou normalizovanou váhu pro každý racionální efekt, nezávislou na jeho vložení do různých konečných měření, se sčítáním při sloučení výlučných výsledků. Jistota přípravy pak vynutí obvyklý poměr kvadratických forem. Efekty jsou všechny příslušné Q-lineární operátory; jejich fyzikální realizace neplyne z konečné abecedy zdrojových operací. Pouhá normalizace binárních měření ani racionálních projektorových rámců není stejnou hypotézou.

V Public Canon v104 již existující pasivní tříatomové QDD záznamy skládají předem zadané kvadratické váhy. Jejich správné slučování samo neprokazuje jedinečnost těchto vah mezi všemi čteními. Racionální rámcová nejedinečnost známá z `A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS [T]` je důvodem rozlišovat projektory a všechny efekty.

## Celočíselné nosiče se nesmějí zaměnit

Univerzální JM-INTEGER-PAIR-INVOLUTION zachovává obsah gcd(X,D), může však měnit jmenovatel a nezachovává vždy samotný účet XᵀLX+D². Fundovaný zdroj rozdíl dorovnává zásobníkem.

Nový explicitní podnosič používá pevný program z₀, souřadnice (u,v) s v≡2u mod 5 a neměnný kladný jmenovatel D. Racionálně působí stejným U_z₀, ale jeho úplný celočíselný přechod je jiný: nevyžaduje zachování gcd. Na tomto nosiči se XᵀLX+D² zachovává přímo. Obě tvrzení jsou slučitelná a žádné z nich neopravuje ani nenahrazuje původní větu.

Všechna racionální x,y lze zakódovat výběrem vhodného společného D před přechodem. Jeden pevný číselný jmenovatel nepokrývá všechny racionální vstupy. Cena přípravy či řadiče není odvozena. Dokázána je úplná zadaná involuce a její buněčný účet; celé původní zařízení navíc obsahuje měnící se n,p a jejich ceny n²+p².

Pětice celočíselných buněk je kartézský nosič. Není automaticky obecným kvantovým stavem pěti tenzorových buněk. Samostatné tenzorové provedení s pomocným K má jiný, výslovně pojmenovaný nosič.

## Vztah k veřejným zdrojům

Při zveřejnění poznámky STATUS uvádí aktivní Public Canon v104, obsahový commit 4a50e527d20018839f006ed312454b710e6486b4. Původně prohlédnutý kandidát na commitu 957b27ce26edbc13600b17c89b9ba870ed472716 má totožné bajty CANON.md; otisk i velikost byly při zveřejnění ověřeny. Připnuté zdrojové práce #1681 a #1699 zůstávají dohledatelnými podklady vzorců. Status a rozsah převzatých tvrzení určuje aktivní kánon; tato nová poznámka zůstává nekanonická.

Nová práce používá jejich přesné vzorce, nyní obsažené i v aktivní v104. Dodává návaznost mezi již zadanou zdrojovou involucí a dříve dokázanou afinní jedinečností. Shoda se znaménkově upravenou maticí D=A₁ΣA₁ z DRIFT-IS-THE-READ je algebraické srovnání; operátor driftu tím není prohlášen za nativní bránu.

Žádný závěr nezvyšuje status zdroje, nemění vydání v104, registr, původní U ani existující vlastníky otevřených fyzikálních otázek. Není odvozena Bornova četnost, fyzikální energie v SI, měřicí přístroj ani Riemannova hypotéza.

## Přesná zbývající otázka

Existence promíchání i pevné reference už v deklarovaném JM modelu doložena je. Zbývá nezávisle fyzikálně zdůvodnit, že příslušné čtení světa patří právě do uvedené třídy: závisí jen na racionálních amplitudách, má nezávislé poměry k referenci a při uvedených operacích zachovává referenční váhu. Alternativou je zdůvodnit celou efektovou doménu a její kontextově nezávislé skládání. Bez takového určení třídy by tvrzení o globální jedinečnosti čtení bylo silnější než důkaz. Žádná z těchto podmíněných vět sama nekonstruuje fyzikální generátor výsledků.
