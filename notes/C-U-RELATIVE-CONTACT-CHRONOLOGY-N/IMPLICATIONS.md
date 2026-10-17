# Důsledky: pomocné buňky, přesný dvoutakt a zbývající fyzikální závazek

**C-U-RELATIVE-CONTACT-CHRONOLOGY-N — NON-CANONICAL, candidate-T, L1.**

Tento text navazuje na samostatný [PROOF.md](PROOF.md). Všechny zde nové
matematické závěry mají níže ruční důkaz. Nebyl spuštěn nový vědecký
program. Původní výsledky a jejich status odděluje [SOURCES.md](SOURCES.md).

Hlavní posun má dvě strany. Pomocná buňka může převzít chybu, ale v přesně
vymezené třídě oprav ji nelze odstranit a současně obnovit všechny
pomocníky. Zároveň lze referenční kontakt přesně provést ve dvou ticích,
pokud připustíme dvě konkrétní nové brány zachovávající společnou stopu.
Takový dvoutakt existuje pro každou hodnotu vazby v F₅. Samotná časová
slučitelnost tedy nevylučuje relativní kontakt ani nevybírá jeho vazbu.

## 1. Nutná podmínka pro další úplný návrh

Označme X=(x,y,a) úplný trojstav zdroje, přijímače a reference.
Pro C(X)=(x,y+x−a,a) platí C(x,y,x)=(x,y,x).
Jestliže má úplný návrh M_{n,m}, včetně přístroje v deklarovaném stavu
ready, realizovat tento kontakt a m skutečných nativních tiků, musí na
celém svém přiznaném nulovém oboru splnit

\[
\pi_{\rm data}M_{n,m}(x,y,x;\mathrm{ready})
 =D_{n+m-1}\cdots D_n(x,y,x).
\tag{1}
\]

D_n je skutečný společný nativní krok v čase n, nikoli libovolně zvolený
bit. Pravá strana obsahuje volný vývoj: nulový kontakt nezastavuje čas.
Přípustná příprava a souřadnicový význam projekce musí být určeny předem.
Rovnice (1) je nutná podmínka na data, nikoli postačující důkaz správného
stavu celého přístroje.

Při slabším cíli, rovnosti pouze dostupného pozorování R, je třeba
deklarovat R a prokázat příslušnou rovnost jeho hodnot. Má-li být takto
získaný model použitelný v dalších kontaktech, musí stejná pozorovací
rovnost přetrvat při všech připuštěných pokračováních. Rovnost jednoho
koncového čísla sama takovou možnost skládání neposkytuje.

Invariant I z PROOF.md zaručuje rozlišení pro každé R, pro něž na daném
oboru existuje h s I=h∘R. Když R hodnotu I zahodí, tento konkrétní důkaz
sám o shodě čtení nerozhodne. Zahození I ještě není konstrukcí správné
čtečky a jejího dalšího vývoje.

## 2. Přesná mez oprav pomocí dalších buněk

### 2.1 Obor a povolené kroky

Buňka má nosič V=F₅⁶. Pro v∈V položme

\[
S(v)=p_1+p_4+p'_1+p'_4,\qquad
I(v)=\bigl(S(v)-{\bf1}_{z(v)=0}\bigr)^2\in\{0,1,4\}.
\]

PROOF.md dokazuje I(f₀v)=I(f₁v)=I(v) na celém V, tedy i mimo
synchronizované vrstvy.

Uvažujme pevný konečný počet N buněk. Během opravy dovolujeme:

1. Vybrané nativní kroky f₀ nebo f₁ na jednotlivých buňkách, případně
   jejich souběžné provedení.
2. Libovolné permutace celých buněk.
3. Pomocné řízení, které nemění buněčná data jiným způsobem.

Volba kroku a konečné zastavení smějí záviset na celém dosavadním stavu
a historii. Tato třída je pro nativní řízení záměrně velkorysá: nezávislá
volba f₀,f₁ nemusí být fyzicky k dispozici. Záporný závěr pro tuto větší
třídu platí i pro její část s jedinými skutečnými hodinami.

Během této opravy nejsou povoleny CSUM, R_i, L_i, jiné mezibuněčné
sčítání, libovolně volené jednotlivé generátory a,b,c,d,e mimo jejich
skutečný výběr, další zápis řadiče do buňky ani přidání, odložení či
výměna buněk. Přičítací brány, které vytvořily původní chybu, nejsou
součástí tohoto opravného kroku.

Toto není tvrzení o všech starých operacích repozitáře. Zvláště
[KERNEL-CONNECT-ALL-K](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/probes/P-KERNEL-CONNECT-ALL-K-1/PREREG.md)
výslovně připouští R_i,L_i a jiný výběr generátorů. Jeho širší
dosažitelnost se nesmí zaměnit s právě definovanou nativní opravou.

### 2.2 Zachovaný histogram

Nechť b₀,b₁,b₄ označují jednotkové vektory tří kategorií histogramu.
Nejsou to buněčné stavy ani generátory. Pro X=(v₁,…,v_N) definujme

\[
H_k(X)=\#\{i:I(v_i)=k\},\qquad k\in\{0,1,4\}.
\tag{2}
\]

Počty H_k jsou obyčejná nezáporná celá čísla. Neprovádíme jejich redukci
modulo 5.

**Tvrzení.** Každý konečný povolený opravný postup zachovává všechny
tři H_k, i při adaptivní volbě kroků.

**Důkaz.** Vybraný f_t zachová kategorii každé zasažené buňky. Permutace
změní pouze její pozici. Řadič žádnou další změnu buněčných dat podle
předpokladu nedělá. Každý skutečně provedený krok tedy zachová (2).
Indukce po délce konkrétní větve dokazuje výsledek i tehdy, když volba
větve a její konečná délka závisí na datech. □

### 2.3 Oprava dat musí zanechat stopu v pomocnících

Tři datové pozice na začátku a na konci opravy jsou pevně určeny;
uvnitř opravy se buňky smějí přehazovat. Ideální nulové svědky z
PROOF.md mají datový histogram 3b₀, včetně obou dárců.

Po pětitaktu je datový histogram 2b₀+b₄. Po rozkladu s jednou mezerou
je 2b₀+b₁. Označme typ chyby ℓ∈{1,4} a počáteční pomocný histogram
h_in, měřený bezprostředně před opravou.

Jestliže oprava vrátí všechny tři datové buňky do přesných ideálních
stavů, musí z (2) platit

\[
(2b_0+b_\ell)+h_{\rm in}=3b_0+h_{\rm out},
\qquad
h_{\rm out}=h_{\rm in}-b_0+b_\ell.
\tag{3}
\]

Stejná rovnice platí, dovolíme-li na ideální straně další čistě nativní
vývoj: všechny její datové kategorie zůstávají nulové.

Z (3) plynou dvě nutné meze. Pomocníci se nemohou všichni vrátit do
původního stavu; nemůže se vrátit ani jejich původní histogram.
A před opravou musí existovat alespoň jedna pomocná buňka s I=0.
Ani čistě nativní pokračování pomocníků ideální strany tento rozpor
neodstraní, protože rovněž zachovává histogram.

Jde pouze o nutné podmínky. Rovnice (3) netvrdí, že každá banka s
jednou takovou buňkou dovede obnovit všechny konkrétní souřadnice dat.
Zároveň nevylučuje obnovu dat za cenu změněných pomocníků.

### 2.4 Podmíněná mez opakovaných oprav

Předpokládejme navíc, že jiný, samostatně doložený zdroj postupně dodá
r₁ chybných trojic typu 1 a r₄ typu 4 a každá z nich se opraví do
ideální datové kategorie 3b₀. Používá se stále stejná konečná banka
pomocníků. Mezi opravami banka nepřijímá ani neodkládá buňky a
nepodstupuje další kroky měnící její histogram.

Opakované použití (3) pak dává

\[
h_{\rm out}
 =h_{\rm in}-(r_1+r_4)b_0+r_1b_1+r_4b_4,
\qquad
r_1+r_4\le h_{{\rm in},0}.
\tag{4}
\]

Poslední nerovnost je nezápornost koncového počtu pomocníků s I=0.
Takový postup proto při těchto předpokladech neobnovuje opravnou
banku pro neomezené další použití.

Předpoklad dodávání této posloupnosti vadných vstupů nebyl odvozen:
ani jednotlivý nulový svědek, ani samotný výsledek issue 1001 jej
neposkytují. (4) je podmíněná mez, nikoli nová nativní konstrukce
opakovaného zdroje.

Histogram a I nejsou fyzikální energie, teplo ani entropie.
Rovnice (3) a (4) neurčují energetickou cenu obnovy nebo Landauerovu
mez. Nová histogram měnící interakce opouští tuto přesně popsanou
třídu oprav.

## 3. Kladný výsledek: dvě brány, které dovolují skutečné mezitiky

### 3.1 Konkrétní kontakt C₁

Nyní jako nové brány na V³ zadejme

\[
P(x,y,a)=(x,3y+3x,a),\qquad
Q(x,y,a)=(x,2y+4a,a).
\tag{5}
\]

Veškeré koeficienty v této části patří do F₅. Obě brány jsou na V³
bijekce, neboť jejich koeficient přijímače je nenulový a dárci
zůstávají zachováni. Přímé dosazení dává

\[
QP(x,y,a)=(x,6y+6x+4a,a)=(x,y+x-a,a)=C_1(x,y,a).
\tag{6}
\]

Součty přijímačových koeficientů jsou 3+3=1 a 2+4=1 v F₅.
Proto každá brána zvlášť zachovává každou společnou vrstvu H_s³,
včetně s mimo {1,4}.

Pro společně vybraný nativní generátor g(v)=Lv+b a c+d=1 platí

\[
g(cu+dv)=c\,g(u)+d\,g(v).
\tag{7}
\]

Díky zachování společné stopy před i po bráně se skutečně použije
tentýž generátor na všech třech buňkách. Z (7) plyne, že P i Q
komutují se souběžným vybraným nativním krokem na každém H_s³.
To je podmínka, kterou holé přičtení zdroje v PROOF.md nesplnilo.

Při skutečných časech n,n+1 a nativním tiku po každé bráně tedy na
každé společné vrstvě přesně platí

\[
D_{n+1}Q D_nP
   =D_{n+1}D_nQP
   =D_{n+1}D_n C_1.
\tag{8}
\]

Rovnice platí pro každé n≥0 a s∈F₅. Pro jednu vnitřní mezeru navíc
Q D_nP=D_n C₁. Zdroj i reference v obou rovnostech normálně stárnou;
není vložen jejich HOLD.

Lze to zapsat jako úplný podmíněný dvoustavový řadič. Pro j∈{0,1}
položme B₀=P, B₁=Q a

\[
\widetilde W(n,X,j)
 =(n+1,D_nB_jX,j+1\bmod2).
\tag{9}
\]

Ze j=0 se po dvou krocích vrátí j=0 a data splní (8).
Brány, řadič a jeho výběrové pravidlo jsou zde explicitně přidané
předpoklady. Globální bijektivita celého autonomního vývoje na
sjednocení všech stopových vrstev se netvrdí: samotné f_t na tomto
sjednocení bijekce nejsou. Bijektivní jsou P,Q a jednotlivé nativní
přechody mezi určenými společnými vrstvami.

### 3.2 Stejná možnost pro všech pět hodnot vazby

Pro κ≠−1 v F₅ definujme

\[
P_\kappa(x,y,a)
 =\left(x,\frac{y+\kappa x}{1+\kappa},a\right),
\qquad
Q_\kappa(x,y,a)
 =(x,(1+\kappa)y-\kappa a,a).
\tag{10}
\]

Dělení je inverze nenulového prvku F₅. Součet koeficientů každé
přijímačové kombinace je 1 a koeficient y je nenulový. Stejný důkaz
tedy dává globální bijektivitu bran, zachování každého H_s³,
komutaci s vybraným nativním krokem a

\[
Q_\kappa P_\kappa=C_\kappa,\qquad
D_{n+1}Q_\kappa D_nP_\kappa
   =D_{n+1}D_n C_\kappa.
\tag{11}
\]

Pro κ=0 jsou obě brány identity. Zdánlivě vynechaný případ κ=−1=4
získáme výměnou role zdroje a reference ve faktorech pro κ=1:

\[
P_-(x,y,a)=(x,3y+3a,a),\qquad
Q_-(x,y,a)=(x,2y+4x,a).
\tag{12}
\]

Pak Q₋P₋=(x,y−x+a,a)=C₋₁, znovu při všech vlastnostech výše.
Tím je pokryto všech pět κ∈F₅, nikoli pouze čtyřčlenná podrodina.

Tento výsledek současně brání příliš širokému zápornému závěru a
příliš rychlému výběru zákona. Vložené tiky samy relativní kontakt
nevylučují. Slučitelnost s těmito tiky ale ponechává celou rodinu.
Jednotková kalibrace, která vybírá κ=1, zůstává dalším předpokladem
původní [klasifikace v issue 990](https://github.com/mathorn1973/twist-j/issues/990#issuecomment-5654429916).

### 3.3 Co je již odvozeno a co je stále zadáno

Rovnice (8) až (12) jsou úplné matematické důkazy účinku uvedeného
podmíněného zákona. Nejsou odvozením fyzické dostupnosti bran P,Q
ze samotného původního U. V přezkoumaných zdrojích taková realizace,
její spouštění a úplný energetický účet dodány nebyly.

Jestliže se P nebo Q dále rozloží na jiné podkroky, musí se znovu
prokázat jejich skutečná chronologie. Algebraický vzorec složené
brány její vnitřní tiky nenahrazuje. Tento požadavek nelze obejít
tím, že se nové faktory pouze přejmenují na nativní operaci.

Kladný dvoutakt rovněž neodporuje části 2: nové brány P,Q do tamního
opravného jazyka nepatří. Zde se s nimi správný kontakt provede
rovnou; tam se zkoumá oprava již vzniklé chyby pomocí omezených
následných kroků.

## 4. Jak zapadají skutečně odvozené kladné nativní zákony

[Issue 994](https://github.com/mathorn1973/twist-j/issues/994#issuecomment-5655607857)
odvozuje uvnitř jedné původní buňky, pro dva pevné pístové bloky
ve vystředěných souřadnicích, skutečný zákon

\[
(u',v')=-\operatorname{Swap}^{\,\eta\mathbin{\mathrm{xor}}\theta}(u,v),
\qquad \eta={\bf1}_{z=1}.
\]

Po synchronizaci je η_n=θ_{n−1}. Nativní čas výměny je tedy odvozen.
Zákon přesouvá dva počáteční obsahy mezi pevnými souřadnicovými
místy; sám nevytváří nové nezávislé zprávy nebo rostoucí archiv.
Nejde o dvě původní šestirozměrné buňky s dodatečnou mezibuněčnou
bránou.

[Issue 1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909)
odvozuje skutečný tříkrok na celé počáteční vrstvě H₀. Při skutečných
počátečních bitech 011 se vybere slovo a,c,e. Pro

\[
X(s,t,\alpha,\beta)
 =(t,\alpha,-t-\alpha-\beta,\beta,-s,s)
\]

a pevné místní výstupní souřadnice je účinek
(s,t,α,β)↦(s,t+s,α,β). To je kladný nativní výsledek. Vstupní a
výstupní souřadnicové popisy se však liší.

Zde lze navíc přímo uzavřít jednu přesnou cestu obnovy. Výstup tohoto
skutečného U³ patří do H₁ a pro s∈{1,4} platí

\[
\tau_0(s)=4,\qquad \tau_1(s)=1.
\]

H₁∪H₄ je uzavřeno pod oběma vybranými f₀,f₁. Tentýž nosič se tedy
nemůže pouhým dalším nativním čekáním vrátit do původní přípravné
vrstvy H₀. Abstraktní opakování výstupního výrazu není obnovení této
surové vstupní přípravy. Jiná příprava, jiné rozhraní, nový nosič či
skutečná interakce tím vyloučeny nejsou.

[Issue 998](https://github.com/mathorn1973/twist-j/issues/998#issuecomment-5662316457)
má kladné globálně přenášené matematické čtení a současně záporný
výsledek pro přesně vymezených padesát aktuátorů při zachování
deklarovaného nativního rozhraní. Dostupný vzorec čtečky a fyzicky
provedená změna tak zůstávají odlišnými závazky.

Tyto předchůdce zde znovu numericky neověřujeme a jejich staré počty
testů nepřebíráme jako nové běhy této poznámky.

## 5. Přesné místo zbývajícího fyzikálního mostu

### Dostupný zákon a příprava

Počet dostupných stavů a existence algebraického kontaktu řeší různé
podmínky. Dostatečná kapacita sama nedokazuje přípravu, spouštění
interakce ani její úplné provedení. Tato poznámka nepřidává nový
nezávislý důkaz předchozích kapacitních konstrukcí T₁₂.

Nový dvoutakt již dává konkrétní správný časový předpis při
explicitních branách. Zbývá doložit ze zdroje právě tyto brány,
nebo jinou kompletní realizaci stejného účinku, a zahrnout řízení,
pole, zásoby, obsazené či odmítnuté větve a přípustné přípravy.
Dostupnost přípravy je fyzikální tvrzení nad rámec množinového
obrazu H_s³.

### Dostupné čtení a kontext kontaktu

[PR 1424, SOURCE_SELECTION.md v commitu c404723](https://github.com/mathorn1973/twist-j/blob/c404723bbda3a65dd39c86ae4fc1152b587977c3/notes/C-PHYSICAL-READOUT-CLOSURE-SYNTHESIS-N/SOURCE_SELECTION.md)
dokazuje, že dvě dokončené kontaktní historie mohou mít totožný
úplný zaznamenaný konec a odlišný poslední energetický přenos.
Jejich společná čtečka proto musí splňovat vláknové kritérium i
napříč kontaktními kontexty; samostatná správná čtečka pro každý
známý zákon nestačí.

Případný uchovaný štítek kontextu musí mít zdrojově doloženou
přípravu a fyzickou realizaci. Nativní invariant I této poznámky
není tímto štítkem a není energetickou změnou přijímače. Jde o
odlišné veličiny na odlišně deklarovaných nosičích.

### Nezávislý energetický test

Pro předem danou, na parametru c nezávislou rodinu úplných přechodů
a pevné funkce H₁,Π je v témže zdroji úplně dokázáno kritérium

\[
H_c=H_1+(c-1)\Pi,\qquad
a_q=\Delta_qH_1,\quad b_q=\Delta_q\Pi,\qquad
a_q+(c-1)b_q=0\quad\text{pro každý }q.
\tag{13}
\]

Tady jde o původní číselné energetické veličiny a přípustný doménový
parametr c, nikoli o aritmetiku modulo 5 ani o vazbu κ.

Pokud všechny b_q=0 a a_q=0, přežije celá přípustná rodina.
Nenulové b_q navrhne jedinou hodnotu c=1−a_q/b_q. Ta musí patřit
do předem určeného přípustného oboru a splnit rovnice všech ostatních
přechodů. Jinak je přípustná množina prázdná;
záporný výsledek má svědka s nejvýše dvěma přechody. Na nekonečném
oboru kladný výsledek vyžaduje obecný důkaz.

Účet musí zahrnovat přístroj, pomocníky a případnou interakční
energii při přesně té časové jemnosti, pro kterou se zachování
tvrdí. Vyrovnání pouze po celém dvoutaktu neprokazuje zachování při
každém jeho vnitřním kroku. A energetické dorovnání kontaktu,
definované z předem vybrané ceny, není nezávislý zdroj téže ceny.

Uvedený nový dvoutakt nemá dodanou takovou energetickou realizaci.
Jeho časová správnost tento zbývající závazek neplní.

## 6. Kam nás výsledek posouvá

| Otázka | Doložený výsledek | Přesná hranice |
|---|---|---|
| Lze holé podsoučty přesunout přes skutečné tiky? | Čtyři případy jedné mezery a všech šestnáct kontextů daného pětitaktu selhávají jako celé mapy. | Jde o uvedené rozklady. |
| Pomůže po nulovém svědku libovolně dlouhé čekání? | Rozdílné I se nikdy nesjednotí při vybraných nativních krocích. | Jiné interakce a čtení zahazující I vyžadují jiný důkaz. |
| Mohou při omezené opravě pomoci další buňky bez vlastní změny? | Přesná obnova dat vynutí změnu pomocného histogramu (3). | Nutná podmínka v pevné třídě; není to energetická cena ani konstrukce opravy. |
| Existuje vůbec rozklad slučitelný s mezitiky? | Ano: (5) až (12) dávají přesný podmíněný dvoutakt pro všech pět κ. | Brány a řadič jsou nové výslovné předpoklady. |
| Vybral tento dvoutakt konkrétní fyzikální zákon? | Zachovává celou rodinu C_κ, včetně identity. | Kalibrace κ, vznik kontaktu a zdrojová dostupnost jsou další závazky. |
| Je dokončeno opakované fyzické čtení s energií? | Ne. Je určeno, co musí úplný zdrojový zákon a přístroj navíc splnit. | Příprava, čtení kontextu a nezávislý úplný energetický účet zůstávají otevřené. |

Za užitečný další konkrétní cíl proto považujeme zdrojovou realizaci
jednoho úplného kroku s dostupnou přípravou, pevným rozhraním a
přiznaným stavem přístroje. Rovnice (8) je přesný pozitivní vzor pro
časování; (1) a (3) jsou nutné překážky, které musí respektovat
příslušné další návrhy. Kritérium (13) se použije až na skutečně
dodaný úplný zákon nezávislý na testovaném c.

Touto poznámkou se nemění Canon ani status předchůdců. Fyzikální
uzávěr, Hilbertova koherence nebo fotonová fáze úplného modelu z ní
neplynou.

Autor: A. M. Thorn. Původní text a důkazy: Apache-2.0. Oddělený
asistentský přezkum je popsán v REVIEW.md.
