# Řetěz v96: zákon, první práce a místní záznam

LOCAL RESEARCH, NON-CANONICAL souhrn existujících veřejných vět [T].
2. října 2026. Tento text není nový stroj ani změna Canonu.

Autoritou je Public Canon v96 na main/tagu `44423153eee6259c7277eec5f5adbed9679f9146`.
Přesným zdrojem jsou [společné důkazy 1–9](https://github.com/mathorn1973/twist-j/blob/44423153eee6259c7277eec5f5adbed9679f9146/canon/CANON.md#L7632)
a řádky `FIELD-CONSERVATIVE-CHAIN-LAW`, `FIELD-CHAIN-FIRST-WORK`,
`FIELD-LOCAL-WORK-RECORD` v [registru v96](https://github.com/mathorn1973/twist-j/blob/44423153eee6259c7277eec5f5adbed9679f9146/canon/REGISTRY.tsv#L486).
Živou kontrolu autority a případné nové běhy eviduje nadřazený výsledkový záznam;
tento text žádné vědecké programy nespouští.

## Úplný zákon [T]

Pro každé konečné `N>=2` má buňka `c_i=(m_i,b_i,z_i,r_i)` tři reagující
a tři divácké čtyřvektory, syrové pole `z_i=(E_i,M_i) in Z^4 x Z^2`
a nezáporný zdroj `r_i`. Mezi sousedy je uložen nezáporný kanál `q_j`.
Úplný nosič má `32N-1` souřadnic; rovnost zahrnuje jejich skutečné pořadí
a veškerý starý obsah. Není ztotožněn s nativním checkpointem `F_5^6`.

Zákon je `T_N=F B A G`, tedy chronologie `G; A; B; F`. Přesně definovaná
místní reakce `G` páruje jen doslovné uspořádané látkové stavy R a AM.
Přijímá výhradně integrální rozklad pole, správný obraz L a financovanou
větev; každé odmítnutí ponechá celý vstup. Kontakty A a B prohazují celý
uložený obsah zdrojů a kanálů, včetně obsazených. F je celočíselný vratný
krok pole. Tyto konkrétní operace mají úplné inverze; jejich obrácené pořadí
dává inverzi makrokroku na celém přijatém nosiči.

Úplná energie je součet kladně definitních kvadratických energií látky,
diváků a pole plus všech `r_i` a `q_j`. Každá primitivní operace zachovává
energii, každého diváka, součty reagujících vektorů a jednotlivé skutečné
náboje, divergence i Gaussovy defekty, také mimo Gaussovu podmnožinu.
Oba směry mají hloubku čtyři a závislost nejvýše přes dvě hrany deklarované
cesty uložených bloků. Pevný řez vypouští oba kontakty jedné hrany a uchová
její starý kanál. Stejné závěry platí pro tento přesně určený řez.

Pro pevné N a energii je úplná slupka konečná. Zachovávající bijekce je na
ní permutací: každý úplný stav je periodický od začátku. Na pevné slupce
existuje společný násobek period; věta neurčuje jednu periodu nezávislou
na N a energii, směšování, rovnoměrnou míru ani zákon výskytu.

## První příchod, práce a návrat [T]

Pro každé celočíselné `w` s `H(w)=1` je předepsaná čistá příprava:
zdroj `(R,0,PLw,0)`, mezilehlé buňky `(ZM,0,0,0)`, přijímač
`(R,0,0,0)` a nulové kanály. Její celková energie je 41, nezávisle na N.
Platí přesně:

| Událost na této přípravě | První hranice/krok |
|---|---|
| Dvě jednotky zdroje u přijímače | Hranice `N-1` |
| Financovaná přijímačová reakce R → AM | Krok `N` |
| Návrat původní celé 31souřadnicové buňky do připravenosti | Hranice `N+1`; dvě jednotky jsou v posledním kanálu |

Důkaz je indukce pro všechna N a tato w, nikoli extrapolace časových vzorků.
Rovněž dva přesné negativní rozsahy platí pro všechny nezáporné časy:
rovnoenergetický mimobrazový zdroj `y_minus=(0,0,1,-2)` a každý jednotlivý
pevný řez udržují připravený přijímač beze změny. Tvrzení nepokrývá libovolný
předem excitovaný přijímač a neurčuje optimální možnou latenci.

## Místní uchovaný záznam [T]

Rozšíření přidává přijímači `p in C5` s definovanou konstantní energií 1.
Úplný nosič má `32N` souřadnic a čistá příprava energii 42. Predikát
`e(c)=1` právě při skutečně přijaté místní větvi R → AM dává

```text
Ghat(c,p) = (G c, p+e(c) mod 5),
Ghat^-1(c',p') = (G c', p'-e(G c') mod 5).
```

Inverze nejprve obnoví původní vstup. Dopředné uvolnění AM → R samo předchozí
zápis nemaže. Všechny vrstvy i inverze po projekci přesně dávají původní
řetěz. Čtečka dostává pouze místní p a čte BLANK pro nulu, HIT jinak.

Při `p=0` a prvním přijatém zápisu v kroku j je HIT zaručen na hranicích
`j,...,j+7`: osm hranic, sedm uplynulých makrokroků. Důvodem je nejméně
jeden mezilehlý krok mezi dvěma inkrementy. Není dokázán reset právě v j+8,
trvalá paměť ani stejná garance pro libovolný počáteční p. V čisté kladné
rodině je `j=N`; oba negativní případy zůstávají BLANK navždy.

## Přesná hranice této uzavřené matematiky

Metrika, graf, látkové koncové stavy, příprava, rozvrh, zdrojové váhy,
pětistavový ukazatel a čtečka jsou zvolené definice. Věta neodvozuje jejich
výběr z J nebo U, fyzikální hodiny, fyzikální přenos, cenu v SI ani výskytový
či Bornův zákon. HIT dokládá přijatou místní událost v daném modelu; sám
neprokazuje původ od konkrétního zdroje.

**Věta nepřechází mezi stroji.** Rozměr, energie 41/42, Gaussovy invarianty,
čtyřvrstvá lokálnost i osmihraniční retence náleží tomuto nosiči a zákonu.
Pro packetový stroj #1328, komplexní přístroj #1330–#1334 nebo nativní U
je lze použít pouze po zvlášť doloženém zobrazení zachovávajícím příslušné
operace, doménu a pozorované údaje. Shodná jména registrů takové zobrazení
nenahrazují.
