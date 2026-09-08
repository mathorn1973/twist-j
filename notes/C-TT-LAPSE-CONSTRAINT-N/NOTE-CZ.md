# C-TT-LAPSE-CONSTRAINT-N: co vyšlo, česky pro vlastníka

**NON-CANONICAL. Žádný status, žádné uzavření O/H, žádná změna kánonu.**
Základ v81, `main` c6d90f1. Prereg zmrazen před výpočtem
(`e0bb6984…f0af8`), verifier 24 z 24 přesných kontrol (po opravě jedné
fixtury, obojí zachováno). Podrobnosti v README.md a RESULT.md.

## Stavba

Diskrétní linearizovaná ADM akce s lapsem a nulovým shiftem na planárním
nosiči `Z/5` (osa slotů K1) s veřejným stencilem `L`, indefinitní DeWittova
forma, prefaktor `1/(2 lambda)`, `lambda = 216 pi` z FRW-CANONICAL-FORM.
Planární pravidlo: součin dvou prvních diferencí je `<f, L g>`, druhá
diference je `-L`. Nic jiného se nezavádí. Dvě čtení K1 zmrazena: zdrojové
(K1 jako předepsané napětí, kovektorová energie s lapsem, tj. předchůdce
plus lapse) a dekodérové (`h_+ = v^2 = iota` je přímo strain, žádná hmota,
skalár ze druhého řádu vazby).

## Sektorový rozklad [candidate-T]

```text
kinetika   (1/2)[(Dh_+)^2 + (Dh_x)^2 + (Dh_13)^2 + (Dh_23)^2 - (Dtau)^2] - Dtau Dell
gradient   (1/2)<tau,L tau> - (1/2)<h_+,L h_+> - (1/2)<h_x,L h_x>
lapse      n . 2 L tau
```

`ell` (podélná) a vektor nemají žádnou gradientní energii: kalibrační
směry. Lapse násobí jen `tau`. TT pár má fyzikální znaménko vlny, `tau` má
opačné gradientní znaménko a kinetiku jen přes vazbu na `ell`. To je
konformní faktor Einsteinovy akce na mřížce; přesně to, co pozitivně
definitní `B+` smazalo.

## Rovnice (přesnou variací explicitní akce, dvě hodnoty lambda)

```text
(a) lapse     (1/lambda) L tau = iota/2
(b) podélná   (1/(2 lambda)) Delta^2 tau = iota/4
(c) stopa     Delta^2 tau + Delta^2 ell + L tau + 2 L n = 0
(d) TT        Delta^2 h_+ + L h_+ = lambda iota,  Delta^2 h_x + L h_x = 0
(e) vektor    Delta^2 h_13 = Delta^2 h_23 = 0
```

Lapse je v akci lineárně, bez `n^2` a bez `Delta n`: F2 nestřílí. Při
`ell = 0` určí (a) `tau` okamžitě ze zdroje, (c) určí `n`, (b) je
konzistence. Žádný volný skalární mód: F3 nestřílí. Relativní koeficient
zdroj/geometrie, který předchůdce nastavil ručně (`rho = 1`), je tu
`lambda`, vynucený C1: F5 nestřílí.

## Homogenní limita

`H = 2 Phi I`: na místo vychází `-(3/lambda)(Delta Phi)^2`, znaménko i
koeficient FRW-CANONICAL-FORM. Předchůdce dával `+24`. F1 nestřílí
(v linearizovaném rozsahu; nelineární homogenní sektor je FRW deklarací).

## Nulový mód: plochý statický nosič K1 neunese [candidate-T]

`L` zabíjí konstanty, takže `k = 0` složka (a) zní `0 = iota_hat_0/2`,
a `sum_r iota = a^2 > 0` pro každé slovo a řez. Hamiltonovská vazba nemá na
statickém plochém kompaktním nosiči řešení pro žádné slovo K1, v obou
čteních (v dekodérovém je nulový mód zdroje `53/864`, `161/864`, `269/864`
podle třídy `u_0 = u_1`, sousední, protilehlé; shodně pro obě mřížkové
transkripce).

`k = 0` složka vazby je Friedmannova rovnice `3H^2 = lambda rho` při nulové
expanzi. Energie K1 musí jít do dynamického homogenního sektoru. C1 tedy
není limita ke kontrole, je vynucena C2 na kompaktním nosiči. To je přesný
smysl, v jakém je skalární jmenovatel TT programu ohraničen FRW-INHOM:
nulový mód každého vázaného skalárního sektoru na tomhle nosiči je
homogenní FRW sektor. Podporuje to tvoje BOUNDED_BY, ne REQUIRES:
nenulové módy tu stojí na plochém pozadí podmíněně.

## Zdrojové čtení: zachování, F6 střílí

(a) a (b) dohromady dávají na nenulových módech `Delta^2 iota = L iota`:
linearizované zachování předepsaného napětí. Pokračování, které zákon
vyžaduje z obou řezů,

```text
iota_-1 = 2 iota_0 - iota_1 + L iota_0,   iota_2 = 2 iota_1 - iota_0 + L iota_1,
```

není tvaru K1 (dvě sousední místa s `a^2/2`) pro žádné z deseti slov,
20 z 20. Čtyři statická slova padají také, protože statické podélné napětí
závislé na ose má `partial_3 T_33 != 0`. Spolu s nulovým módem: pevná K1
nemůže být předepsaným zdrojem vázané dynamiky bez změny. **F6 střílí pro
zdrojové čtení.** Uzavírá to na úrovni kandidáta cestu, kterou jsi už
odkázal pod TT-SOURCE: emisní mapa ano, vázaný gravitační zdroj ne, dokud
K1 nemá vlastní zákon zachování (dluh zpětné reakce předchůdce).

## Dekodérové čtení: vázaný skalár [candidate-T pro přesná pole]

`h_+ = iota`, žádná hmota. Vazba ve druhém řádu s transkripcí (i):

```text
L tau = sigma = (1/4)[(Delta h_+)^2 + g(h_+)] = lambda eps_GW,   lambda se krátí,
tau = L^+ (sigma - mean sigma),   L^+ racionální symetrický cirkulant.
```

Skalár je zdrojován diskrétní energií TT pole, tou samou formou, kterou
předchůdce dokázal nezápornou. Pro deset slov vyšla přesná racionální pole
`tau` (jmenovatel `1715360 = 32 . 5 . 71 . 151`), řádu `a^4` proti
`h_+ = O(a^2)`, translačně kovariantní v `u`. `sigma` je kvadratická
v `h = v^2`, tedy skalár spotřebovává přesně čtvrté momenty dubletu, ty,
které TT-VECTOR-MOMENT-UNDERDETERMINATION žádá zmrazit a K1 dodává.

Transkripce (ii), doslovné `(3/2) h'^2 + 2 h h''`, dává stejný nulový mód a
jiná pole na všech nenulových módech. Vidlice je reálná a deklarovaná: je to
mřížkový zbytek chybějícího produktového pravidla.

**Co ten skalár není:** kosmologická porucha křivosti, `P_S(k)`, ani
poměr. Žádný poměr se netvoří. K1 se nehnula; strain za dvěma řezy se
prodlužuje volnou TT rovnicí (d) bez zdroje, což je dynamika, ne změna K1.
**F6 v dekodérovém čtení nestřílí.**

## Spin (C4)

Na plochém stupni sektory nešíří jeden operátor: TT `Delta^2 + L`, skalár
eliptická vazba `L`, lapse algebraický, podélná a vektor bez gradientní
energie. F4 nestřílí. Registrované `c = 1 - s^2` (`-3` při `s = 2`) je
Reggeův-Wheelerův koeficient na hmotném pozadí, kubický řád; kvadratická
plochá akce ho ukázat nemůže. C4 splněno jen ve slabé podobě, silná
otevřená, nepředstírá se.

## Účet

```text
                     zdrojové čtení          dekodérové čtení
F1 ne FRW            nestřílí                nestřílí
F2 lapse propaguje   nestřílí                nestřílí
F3 zbylá stopa       nestřílí                nestřílí
F4 spinově slepé     nestřílí (RW otevřeno)  nestřílí (RW otevřeno)
F5 nový koeficient   nestřílí                nestřílí
F6 změna K1          STŘÍLÍ                  nestřílí

Uzavřených O/H:      0
Posunů statusu:      0
```

Otevřené položky, pojmenované, aby další krok byl úzký: (1) diskrétní
Bianchiho identita ve druhém řádu, rozhodne, jestli je mřížková vázaná
teorie konzistentní, nebo se `ell` musí zmrazit další volbou; (2) výběr
mezi transkripcemi (i) a (ii); (3) rovnice nenulových módů na FRW pozadí,
které nulový mód vynucuje; (4) 3D nosič, diskrétní gradient slučitelný
s `L`; (5) RW koeficient na hmotném pozadí.

Krátce: třída s lapsem přežila všech šest falsifikátorů v dekodérovém
čtení a vydala první skalár ve stejném kontextu, který není ani radiační
stopa, ani přejmenovaný čtverec. Nulový mód říká, kdo je jeho rodič: FRW.
Zdrojové čtení je pod vazbami mrtvé. To je, myslím, přesně ten užší
problém, který jsi chtěl.
