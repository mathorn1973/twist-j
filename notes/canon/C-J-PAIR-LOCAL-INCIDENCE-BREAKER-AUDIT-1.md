# C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1 (NON-CANONICAL)

Datum: 2026-09-04. **Předání inkubačního auditu, L1; žádná veřejná formální
sonda, registrace výsledku ani uzavření fyzikálního čtení.** Veřejný základ:
`fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e`, Public Canon v75.
`COINCIDENCE-RECORD-FREQUENCY` zůstává `candidate-H / UNTESTED / STOP`;
`QDD-INSTRUMENT-APPARATUS` zůstává `O / STOP`.

**Výsledek:** numerické svědky B1–B4 jsme reprodukovali druhou implementační
cestou. Vyvracejí neznaménkovou autonomní dynamiku, banku nad surovými
příchody a tvrzení, že A je automorfismus celé pevné celočíselné mřížky.
Zmrazená banka má ale jiný vstup: nejprve spočítá znaménkové koeficienty,
potom z nich vytvoří redukovaná vlákna. V tmavé buňce breakeru skutečně
vrátila 0. Podmíněný census tím drží; fyzické provedení redukce stále chybí.

## 1. Co přesně bylo předáno a ověřeno

Přiložený [původní kandidátní text](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/source/C-J-PAIR-LOCAL-INCIDENCE-CENSUS-N.md)
a [původní model](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/source/candidate_model.py)
jsou bajtově nezměněné snímky před tímto auditem. Jejich tehdejší formulace
„unexecuted“ popisuje stav při zmrazení; model byl následně vykonán v níže
uvedeném místním inkubačním běhu. Veřejná formální sonda vykonána nebyla.

Vstupem oponentury byl uživatelem předaný text B1–B4. Původní skript
externího breakeru jsme nedostali. Dva jím jmenované české dokumenty
`NAVRH-APARATU-RETEZ-AXIOM-BORN_2026-09-04_CZ.md` a
`NOTE-KUDY-K-BORNOVU-CTENI_2026-09-04_CZ.md` nebyly v tomto workspace
dostupné. Jejich úplný obsah tedy tento audit neposuzuje. Posuzuje přiložený
konkrétní model a výslovně uvedené námitky, nikoli domnělou totožnost balíků.

[Verifier](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/verify_incubation.py)
nejprve počítá vlastní konvoluci rozesíláním zdrojových sloupců a determinant
Gaussovou eliminací nad `Fraction`. Teprve poté importuje nezměněný model,
který používá řádkové posuny, a porovnává výsledky. Jde o druhou kódovou
cestu se známými svědky, nikoli slepý test nebo nezávislé objevení nálezů.
Dřívější statické kontroly více agentů nebyly nezávislé exekuční reprodukce.

## 2. B1: absolutní populace není úplný dynamický stav

Používáme `A=1+g²−g³−g⁴`, `g e_k=e_(k+1 mod 5)`. Pro předané vstupy vychází:

```text
d  = (-3, 0,-1, 1, 3)     A d  = (-1,3,-8, 1,5)
d' = (-3, 0, 1,-1, 3)     A d' = (-5,3,-4,-1,7)
```

Stejné `|d|`, různé `|Ad|`: žádná mapa G pouze nad absolutními populacemi
nemůže na všech těchto stavech splňovat `G(|d|)=|Ad|`.
Původní dvojice není v našem nosiči
`L_D={d∈Z⁵: Σd_k=0, d_i≡d_j (mod 5)}`. Námitku to neodstraňuje:
vynásobení obou vstupů pěti dává svědky uvnitř L_D:

```text
D  = (-15,0,-5, 5,15)     A D  = ( -5,15,-40, 5,25)
D' = (-15,0, 5,-5,15)     A D' = (-25,15,-20,-5,35)
```

Model uchovává znaménkovou přípravu i znaménkové koeficienty řezu. Záznamový
census nenahrazuje tento stav a nesmí se použít jako jediný vstup dalšího
kroku A. B1 je platný zákaz takového rozšíření.

## 3. B2 a B3: přesná poloha interference

Ze semene `a₀=(4,−1,−1,−1,−1)` dostáváme následující exaktní hodnoty.
„Příchody“ v každém řádku vycházejí z již redukovaného předchozího stavu;
nejde o celý strom dosud nevyrušených historií ze semene.

| Krok | Nový znaménkový stav | Čtverce surových počtů příchodů, součet | Čtverce redukovaných koeficientů, součet | Poměr |
|---|---|---:|---:|---:|
| 0→1 | (5,0,5,−5,−5) | 212 | 100 | 53/25 |
| 1→2 | (−5,−5,20,−5,−5) | 1300 | 500 | 13/5 |
| 2→3 | (−25,−25,25,0,25) | 5300 | 2500 | 53/25 |
| 3→4 | (−25,−25,−25,−25,100) | 32500 | 12500 | 13/5 |

Obecně položme `C=|A|=N−g`, kde N je matice samých jedniček,
`q(a)=Σa_k²` a `L(a)=Σ|a_k|`. Pak `CᵀC=I+3N`, tedy

```text
q(C|a|)=q(a)+3L(a)²,          q(Aa)=5q(a) pro Σa_k=0.
```

V buňce 1 prvního kroku jsou příspěvky `(-1,-1,+1,+1)`:

| Co se počítá | Hodnota |
|---|---:|
| Surové nezáporné páry | (2+2)² = 16 |
| Znaménkový součet párů | (2−2)² = 0 |
| Skutečný výstup přiloženého modelu v buňce 1 | 0 |

Přiložený model provádí právě toto pořadí:

```text
znaménkové d → znaménková aritmetika A^n d
             → nová redukovaná vlákna velikosti |(A^n d)_k|
             → úplná dvourolová banka párů
             → jediné XOR porovnání buněk → census.
```

XOR interference neprovádí. Její algebraické vyhodnocení je před ním.
Proto přijímáme `candidate-F` pro **rozšíření na surové nezáporné příchody**
a odmítáme tvrzení, že tato banka sama fyzicky odvodila interferenci.
Svědek B3 však nedává `candidate-F` doslovnému modelu s redukovaným vstupem:
ten nevytváří oněch šestnáct adres ve tmavé buňce. Hradlo nečte numerický
Bornův cíl; přesto celý census závisí na silném předpokladu přípravy vláken.
Absence čtení cílového poměru sama o sobě není fyzikálním odvozením.

## 4. Obecná překážka pro kladnou banku surových párů

Uvažujme pravidlo konečných nezáporných záznamů, odděleně aditivní vůči
disjunktnímu přidávání surových jednotek v každé ze dvou rolí. Elementární
odpovědi podle znamének označme nezápornými celými čísly
`w₊₊, w₊₋, w₋₊, w₋₋`. Na dvou stejných vstupech s p kladnými a m zápornými
jednotkami dává rozklad na singletony

```text
R(p,m)=w₊₊ p²+(w₊₋+w₋₊)pm+w₋₋ m².
```

Jednotková odezva čistých znamének vyžaduje `w₊₊=w₋₋=1`.
Pokud má výstup záviset na redukovaném koeficientu prostřednictvím jeho
čtverce, musí platit `R(p,m)=(p−m)²`. Avšak

```text
R(1,1)=2+w₊₋+w₋₊ ≥ 2,          (1−1)²=0.
```

Zde `p=m=1` označuje lokální nulový vstup v uvedené rozšířené třídě surových
portů, nikoli nenulovou globální přípravu modelu. Pro skutečnou buňku B3
s `p=m=2` stejná argumentace dává alespoň 8 proti nule; úplná neznaménková
incidence dává 16. Fyzická dostupnost singleton kalibrací je předpoklad
tohoto no-go, nikoli jeho závěr.

To je spor. **Nezápornost, surová oddělená aditivita, jednotková kalibrace
a nulový výstup po vyrušení nemohou platit současně.** Jde o podmíněnou
konečně množinovou větu (`candidate-T` na úrovni důkazu), nikoli o výsledek
registrace nebo vyvrácení všech možných fyzikálních aparátů.

Znaménkový součet sám je lineární. Převedení na nezáporné redukované počty
`|p−m|` ale není aditivní vůči surovému disjunktnímu sjednocení. Součinová
věta přiloženého kandidáta tedy platí **po redukci**; její aditivitu nelze
přenést přes vyrušení. Znaménkové váhy poskytují algebraický rozdíl, nikoli
kladnou kardinalitu fyzických událostí. Jiná kladná konstrukce by musela
změnit předpoklady, například připustit rušení či kontextovou selekci.

## 5. B4: tři odlišné otázky vratnosti

Na kořenové mřížce `A₄={d∈Z⁵:Σd_k=0}`, v bázi `e_i−e_4`, má A matici

```text
 1 -1 -1  1
-1  0 -2 -2
 2  1  2  0
 0  2  1  2
```

a determinant 25. Obraz má index 25; A není automorfismus celé této pevné
mřížky. Totéž platí na invariantní plnorozměrné podmřížce L_D.
Na sektoru se součtem nula ale `AᵀA=5I`, takže A je injektivní a
`A⁻¹=Aᵀ/5`. Na obrazu existuje jednoznačný celočíselný předchůdce.
Pro obecný cíl tomu tak není: předobraz `e₀−e₄` je
`(2/5,0,−2/5,1/5,−1/5)`.

To není důkaz mnohoznačného slévání znaménkových stavů. Mnohoznačná je jiná
mapa: z libovolně označených surových příchodů na jejich výsledný koeficient;
ta zapomíná jejich prezentaci a původ. Fyzická vratnost takové realizace by
vyžadovala jejich uchování v úplném stavu nebo prostředí.

Tvrzená involuce banky drží koeficient a pevný a mění pouze b:
`(a,b)↦(a,b XOR h_a)`. Neprovádí krok A. B4 ji nevyvrací a ona naopak
nedokazuje vratnost celé přípravy či autonomní dynamiky. Například
`(a,z)↦(a,z+Aa)` má celočíselnou inverzi `(a,z)↦(a,z−Aa)` při uchování a.
Je to výpočetní rozšíření s pamětí, nikoli dodaný fyzikální mechanismus.
Z determinantu samotného tedy neplyne nutnost fyzické anihilace.

## 6. Co drží a co je další přesná povinnost

Oddělená aditivita za předpokladů původního textu dává součin vláken.
**Výběr stejné buňky je další předpoklad.** Ve vícebarevné verzi vzniká
`F(X,Y) ≅ ⨿ᵢⱼ X_i×Y_j×W_ij`; diagonálu určuje teprve kalibrace jednoho
záznamu pro stejnou buňku a žádného pro různé buňky. Součinová věta sama
tuto kalibraci ani její fyzikální oprávnění nedodává.

Další krok musí dodat fyzický nosič znaménka a redukce, nezávisle na cílovém
poměru. Musí přesně určit:

1. úplný stav a znaménkový krok, přičemž census nenahrazuje dynamický stav;
2. proč různé surové prezentace téhož koeficientu vytvářejí stejný čitelný
   výstup a proč se zrušené příspěvky nepočítají jako samostatné záznamy;
3. kde je případná paměť prezentace, pokud se požaduje fyzická vratnost;
4. vznik redukovaných vláken, dva vstupní porty, kapacitu, prázdnou přípravu,
   jedno sepnutí a uchování záznamů při pevném řezu;
5. nezávislé oprávnění diagonální odezvy a samostatnou hranici mezi censusem
   celé populace a sebelokací jednoho čtenáře.

Matematická definice jednotky již existuje v
[C-J-RESIDUAL-INTEGER-UNIT-1-N](https://github.com/mathorn1973/twist-j/blob/fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e/notes/canon/C-J-RESIDUAL-INTEGER-UNIT-1-N.md).
To neřeší její fyzickou realizaci. Proto nelze na aktuální balík bez dalšího
přenést tvrzení, že vůbec nemá definici jednotky. Rovněž platí
[přijaté rozdělení A/U5 a otevřeného B](https://github.com/mathorn1973/twist-j/blob/fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e/notes/canon/C-J-A-U5-COINCIDENCE-OWNER-FREEZE.md);
breaker toto rozhodnutí sám neruší a nepovoluje přivést raw J či B do
celočíselného count portu. [PR #803](https://github.com/mathorn1973/twist-j/pull/803)
bylo sloučeno jako `a7ef8ba676a7a26ebac4b0d5a0b31c47bc41cc9c`.

## 7. Inkubační protokol a přenositelnost

Původní obecný požadavek veřejného zámku před jakýmkoli místním ověřením byl
příliš silný. Pro tento uživatelem schválený inkubační audit jsme nejprve
zmrazili [PREREG se šesti poli](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PREREG.md)
a SHA-256. Ještě před spuštěním vzniklo samostatně zapečetěné
[erratum](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PREREG-ADDENDUM-1.md):
jedna věta měla přehozené číslo buňky a počet nula. Vstupy, kód a práh se
nezměnily. Veřejný protokol formálních sond tím není nahrazen.

Lokální běh 2026-09-04 v 16:35:12 UTC: Python 3.12.10, Windows AMD64,
`LC_ALL=C`, `PYTHONHASHSEED=0`, `TZ=UTC`, `PYTHONDONTWRITEBYTECODE=1`.
Návratový kód 0; stdout 3138 bajtů; stderr 0 bajtů. Exaktně prošly
znaménkové stavy a census pro n=0…4, svědci B1–B4 i involuce při pevném
vstupu. Obecné závěry výše nesou důkazy, nikoli velikost tohoto vzorku.

Veřejný handoff obsahuje minimální přenosnou specifikaci, kód, PREREG,
erratum a [provenienci s SHA-256](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PROVENANCE.json).
Původní místní organizační README, spouštěcí obálka a surové provozní výstupy
nejsou součástí tohoto výběru; jejich relevantní hashe jsou zaznamenány.
Nejde tedy o bajtově totožný přenos celé místní složky. Oba vědecké zdrojové
snímky, verifier, PREREG a erratum jsou přeneseny beze změny.

Pro nové inkubační přehrání stačí v adresáři této poznámky spustit
`python C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/verify_incubation.py`
se stejným prostředím. Verifier používá jen standardní knihovnu a soubory
z tohoto handoff. Nový běh je vlastní reprodukce příjemce; není původním
zmrazeným během ani automaticky veřejnou formální sondou.

Tento identifikátor označuje audit, nerezervuje veřejný claim ani nepřebírá
`C-J-COINCIDENCE-RECORD-1` jiné linky. Externí
`BREAKER-RECORD-C-J-COINCIDENCE-RECORD-1` má smysl zabalit již nyní, s přesným
kódem, vstupy, výstupem a verzí napadeného textu; na fyzickou realizaci
jednotky čekat nemusí. Jeho původní skript tento handoff nenahrazuje.
