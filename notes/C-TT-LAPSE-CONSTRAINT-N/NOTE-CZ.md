# C-TT-LAPSE-CONSTRAINT-N: co vyšlo, česky pro vlastníka

**NON-CANONICAL. Žádný status, žádné uzavření O/H, žádná změna kánonu.**
Základ v81, `main` c6d90f1. Prereg zmrazen před výpočtem
(`e0bb6984…f0af8`), dva zmrazené verifiery beze změny (24 z 24 po opravě
jedné fixtury, obojí zachováno), po recenzi 2026-09-08 přidán třetí,
zmrazený addendum certifikát (10 z 10, obě architektury bajtově shodně).
Závěry přepsány do doloženého rozsahu. Podrobnosti v README.md a RESULT.md.

## Stavba

Diskrétní linearizovaná ADM akce s lapsem na planárním nosiči `Z/5`
(osa slotů K1) s veřejným stencilem `L`, indefinitní DeWittova forma,
prefaktor `1/(2 lambda)`, `lambda = 216 pi` z FRW-CANONICAL-FORM. Shift
nastaven na nulu před variací: deklarované omezení s důsledkem níže.
Planární pravidlo: součin dvou prvních diferencí je `<f, L g>`, druhá
diference je `-L`. Dvě čtení K1 zmrazena: zdrojové (K1 jako předepsané
napětí, předchůdce plus lapse) a dekodérové (`h_+ = v^2 = iota` je přímo
strain, skalár ve druhém řádu z deklarované transkripce, ne z variace
kvadratické akce).

## Sektorový rozklad [candidate-T]

```text
kinetika   (1/2)[(Dh_+)^2 + (Dh_x)^2 + (Dh_13)^2 + (Dh_23)^2 - (Dtau)^2] - Dtau Dell
gradient   (1/2)<tau,L tau> - (1/2)<h_+,L h_+> - (1/2)<h_x,L h_x>
lapse      n . 2 L tau
```

`ell` a vektor bez gradientní energie, lapse násobí jen `tau`, TT pár má
fyzikální znaménko vlny, `tau` opačné gradientní znaménko a kinetiku jen
přes vazbu na `ell`. Konformní faktor Einsteinovy akce na mřížce; přesně
to, co pozitivně definitní `B+` smazalo. Chybějící gradientní energie sama
nedokazuje, že `ell` a vektor jsou kalibrace; viz níže.

## Rovnice [candidate-T jako polynomiální identity]

Sedm sektorových rovnic je certifikováno jako polynomiální identity ve
všech 105 polních, 15 zdrojových proměnných a v `1/lambda` (addendum A4),
ne jen na náhodných konfiguracích:

```text
(a) lapse     (1/lambda) L tau = iota/2
(b) podélná   (1/(2 lambda)) Delta^2 tau = iota/4
(c) stopa     Delta^2 tau + Delta^2 ell + L tau + 2 L n = 0
(d) TT        Delta^2 h_+ + L h_+ = lambda iota,  Delta^2 h_x + L h_x = 0
(e) vektor    Delta^2 h_13 = Delta^2 h_23 = 0
```

Lapse je v akci jen lineárně a jeho rovnice žádný lapse neobsahuje (A5): v
uvedené kvadratické akci nepropaguje. To je celý obsah záznamu F2.

Při `ell = 0` určí (a) nenulové módy `tau` okamžitě, (c) určí `n`, (b) je
konzistence. Žádný čistě stopový radiační mód. Ale soustava nemá hybnostní
vazby, protože shift byl vynulován před variací. Bezzdrojová konfigurace
`h_13(n,r) = n f(r)`, `f` nekonstantní s nulovým průměrem, splňuje všechny
uvedené rovnice (A7). Hybnostní vazba by nehomogenní vektorovou rychlost
vyloučila; tahle soustava ne. Vektorový sektor tedy není doložen jako
kalibrace a „TT je jediný radiační sektor“ není doloženo. Zmrazit `ell` po
nevyšlé konzistenci by byl nový kandidát, ne oprava tohoto.

Soupis koeficientů je spočítaný (A6): 370 monomů, každý koeficient
racionální násobek `lambda^0` nebo `lambda^-1`. Relativní koeficient
zdroj/geometrie, který předchůdce nastavil ručně, je tu `lambda` volbou
společného prefaktoru. Záznam normalizace zvolené akce, ne fyzikální
normalizace skalárního srovnání.

## Homogenní limita

`H = 2 Phi I`: na místo `-(3/lambda)(Delta Phi)^2`, znaménko i koeficient
FRW-CANONICAL-FORM; předchůdce `+24`. Záznam F1: kvadratický homogenní
koeficient souhlasí; úplná nelineární diskrétní FRW redukce (`e^(3 Phi)`,
plná závislost na lapse, Friedmannovy identity) je deklarace, ne výsledek
tohoto běhu.

## Nulový mód: statický plochý nosič je s K1 neslučitelný [candidate-T]

`1^T L = 0`, takže `k = 0` složka (a) zní `0 = iota_hat_0/2`, a
`sum iota = a^2 > 0` pro každé slovo. Úplná rovnice `L tau = sigma` nemá na
statickém plochém kompaktním nosiči řešení pro žádné slovo, v obou čteních
(dekodérové nulové módy `53/864`, `161/864`, `269/864` podle třídy, shodně
pro obě transkripce).

Užší a správná formulace místo „C1 plyne z C2“: zvolený statický plochý
podklad je neslučitelný s kladným zdrojem vazby; v FRW pokračování se
homogenní příspěvek musí zahrnout a vyřešit, ne odstranit projekcí.
Spočítaná pole řeší projektovanou rovnici a mají vůči úplné vazbě
zbytek `L tau - sigma = -mean(sigma) 1 != 0` (A3). Nejsou to počáteční
data na dynamickém pozadí; to pozadí ani jeho rovnice nenulových módů
dodány nejsou. Samotný lapse a nulový mód neodvozují nelineární FRW větev.
Překážka je ale přesná: nulový mód skalárního jmenovatele patří
homogennímu sektoru, který vlastní FRW-INHOM.

## Zdrojové čtení: zachování, F6 střílí v testovaném rozsahu

(a) a (b) dávají na nenulových módech `Delta^2 iota = L iota`. Pokračování,
které to žádá z obou řezů, není tvaru K1 pro žádné z deseti slov, 20 z 20;
i čtyři statická slova padají. Spolu s nulovým módem: pevná K1 nemůže být
předepsaným zdrojem této ploché vázané soustavy bez změny. **F6 střílí pro
zdrojové čtení v tomto rozsahu.** Není to věta o každém zachovávaném
zdroji ani o FRW rozšíření. Emisní mapa pod TT-SOURCE ano, vázaný zdroj
ne, dokud K1 nemá vlastní zákon zachování.

## Dekodérové čtení: projektovaný vázaný skalár [candidate-T pro přesná pole]

V bezzdrojové kvadratické akci dá variace lapse jen `L tau = 0`. Zdroj
kvadratický v `h` potřebuje kubické členy (lapse krát kvadratické
tenzorové výrazy), které uvedená akce nemá. Druhý řád je proto dodán
deklarovanou transkripcí, dvěma:

```text
(i)  L tau = (1/4)(Delta h)^2 + (1/4) g(h)
(ii) L tau = (1/4)(Delta h)^2 - (3/4) g(h) + h L h
```

**Přesný vztah obou transkripcí** (tvůj nález, certifikován jako A1, A2):
pro tento `L` a `g` platí polynomiální identita

```text
L(h^2) = 2 h (L h) - 2 g(h),
```

tedy `sigma_ii - sigma_i = (1/2) L(h^2)` a `tau_ii - tau_i = (1/2) Pi(h^2)`.
Nulové módy shodné, rozdíl nenulových módů v uzavřeném tvaru: v řezu 0
`+3/40` na obsazeném a `-1/20` na prázdném místě, pro každé slovo. Vidlice
je zúžena na jeden místní člen, ne rozhodnuta: při proměnném lapse
`<nu, sigma_ii - sigma_i> = (1/2)<L nu, h^2>` obecně nemizí, takže člen s
nulovým součtem nelze zahodit před variací lapse.

**Časové umístění.** Součet `Z_n = sum sigma_i = (1/4)(||h_(n+1) - h_n||^2
+ <h_n, L h_n>)` se volnou TT rovnicí nezachovává: pro `h_0 = h_1 = f`,
`Lf != 0`, je `Z_1 - Z_0 = (1/4)||L f||^2 > 0` (A8; slovo `0101`:
`14189/279936`). Zachovaný tvar má mezikrokový člen `<h_n, L h_(n+1)>`,
jako v energetické větě předchůdce. `sigma_i` tedy není „táž zachovaná
diskrétní energie“; časové umístění musí určit odvození vazby, ne převzatý
spojitý výraz.

S těmito mezemi jsou projektovaná pole přesná: `tau = L^+ (sigma_i - mean)`,
racionální pro deset slov (jmenovatel `1715360 = 32 . 5 . 71 . 151`),
translačně kovariantní v `u`, škálování `a^4`.

**Momenty a amplituda.** `h = Q(v)` je kvadratické v dubletu, `sigma`
kvadratická v `h`, `tau` lineární v `sigma`: `tau` je čtvrtého stupně v
dubletu. Obecně `E[tau]` potřebuje společné momenty do 4. stupně,
`Cov(tau,tau)` do 8., `Cov(h,tau)` do 6. Úplný desetislovný zákon K1 je
na svém dvouokenním oboru všechny určuje, nový zákon není třeba; obecná
specifikace čtvrtých momentů ale výkon veličiny kvadratické v `h` neurčí.
`h ~ a^2`, `tau ~ a^4`, `Cov(tau,tau) ~ a^8`; formální poměr by šel jako
`a^-4`. Vykrácení `lambda` není vykrácení amplitudy. Žádný poměr se
netvoří; `tau` není kosmologická porucha ani `P_S(k)`.

Dvě okna K1 se nehnula. Strain za nimi se prodlužuje volnou rovnicí (d),
deklarované prodloužení; existence úplného vázaného pokračování
slučitelného s ním prokázaná není. Záznam F6 pro dekodérové čtení: okna
zachována, dokončení otevřené.

## Spin (C4)

Na plochém stupni sektory nešíří jeden operátor; to je popis plochého
rozkladu. Registrované `c = 1 - s^2` na hmotném pozadí zůstává neotestované,
silná podmínka otevřená.

## Doložený rozsah a otevřené povinnosti

```text
F1  kvadratický homogenní koeficient souhlasí; úplná nelineární FRW redukce deklarace
F2  v uvedené kvadratické akci lapse nepropaguje (polynomiálně)
F3  projektované tau určeno podmíněně; úplná vazbová redukce (shift, hybnost,
    globální řešitelnost) nedoložena
F4  plochý rozklad popsán; koeficient na hmotném pozadí neotestován
F5  koeficienty zvolené akce spočteny; fyzikální normalizace otevřená
F6  zdrojové čtení: testované pokračování opouští třídu K1 (střílí v rozsahu);
    dekodérové čtení: okna zachována, úplné vázané pokračování neprokázáno

Uzavřených O/H:      0
Posunů statusu:      0
```

„Nestřílí v provedené kontrole“ není „podmínka splněna“. Žádná z C1 až C5
se nehlásí jako splněná.

Otevřené povinnosti v pořadí, v jakém je musí příští konstrukce splnit:
(1) hybnostní vazby, shift až do variace nebo doplnění a důkaz ekvivalence;
(2) jedna společná variační soustava v potřebném řádu, z níž vypadne
Hamiltonova vazba, hybnostní vazby, podélná rovnice, časové umístění
zdroje druhého řádu a jejich zachování, transkripce (i)/(ii) nahrazeny tím,
co ta akce dá, sporný člen je lokalizován rozdílem `(1/2) L(h^2)` a jeho
lapsovou vahou `(1/2)<L nu, h^2>`; (3) homogenní složka jako součást
počátečních dat, ne projekce, rovnice nenulových módů na témže pozadí;
(4) 3D gradient slučitelný s `L`; (5) RW koeficient.

Přijímací objekt dalšího kroku: úplná kompatibilní konstrukce počátečních
dat a propagace vazeb, nebo přesný protipříklad. Ne další tabulka
kovariancí, ne přejmenovaný skalární jmenovatel.
