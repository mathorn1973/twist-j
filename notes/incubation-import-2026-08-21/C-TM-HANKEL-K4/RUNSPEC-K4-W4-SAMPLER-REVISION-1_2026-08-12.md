# RUNSPEC revize 1: tři opravy přijaty, jeden cíl přidán

Status: NON-CANONICAL, gates nothing. Revize
claude/RUNSPEC-K4-W4-SAMPLER-X86-64_2026-08-12.md po připomínkách
vlastníka. Původní runspec se nemaže, tohle je jeho oprava. 2026-08-12.

## 1. Tři opravy, všechny PŘIJATY

```
O1  M1 zajišťuje ÚPLNÝ SCOPE, ne rovnost marginálů. Moje formulace
    "symetrizuje marginály" byla domněnka vydávaná za důsledek. Nový
    probe přes obě orientace a komplementární involuci dává 289 proti 62,
    tedy 4.7:1 místo pilotních 16:1. Zbytková asymetrie je po opravě
    scope MĚŘENÝ FAKT o fiber míře, ne artefakt konvence, a patří do
    readoutů jako první třída, ne jako nuisance.
O2  "Uniformní" je nutné definovat. Sampler NENÍ uniformní na fiber
    párech: je to uniformní volba signed skeletonu krát solverem
    indukovaná míra na řešeních toho skeletonu, plus konkrétní
    XOR-gauge sampler. Skeleton s 10^12 řešeními má stejnou váhu jako
    skeleton s 10^3. Každý výrok o hustotě musí míru jmenovat.
O3  Pravidlo tří. Při nule zásahů v N pokusech je 95procentní horní mez
    3/N, ne 1/N. Při 3.1 milionu vzorků tedy 9.7e-7, ne 3e-7. Moje
    číslo byla bodová škála vydávaná za mez. Chyba, opraveno.
```

Důsledek O1 na sílu testu: můj odhad "oprava zesílí test 4.6krát" vycházel
z p1 = p2. Při 4.7:1 a zachovaném součtu je zesílení 2.66krát. A i tohle
číslo je predikce; skutečné zesílení se vyčte z marginálů produkčního běhu,
nepředpovídá se.

Důsledek O2, který stojí za vyslovení, protože zjednodušuje čtení:
otázka míry se týká VÝHRADNĚ negativní větve. Svědek je svědek v každé
míře; jediný nalezený opačný pár zabíjí T-A bez ohledu na to, jak byl
nalezen. Zkreslení sampleru je tedy problém jen tehdy, když běh skončí
nulou. To je taky důvod, proč se fáze B nesmí míchat do agregátu fáze A.

## 2. Opravená tabulka, v jednotkách vlastníkových tranchí

Pilotní akceptace 0.179, takže tranche 100k pokusů dává kolem 17 900
vzorků. Sazby na vzorek: pilotní marginály 2 p1 p2 = 1.49e-4, při 4.7:1
se zachovaným součtem 3.96e-4 (predikce, ne měření).

```
tranche  vzorků      exp(indep, pilot)  exp(4.7:1)   95% mez při nule
1        17 900              2.7             7.1        1.7e-4
10       179 000            26.7            70.9        1.7e-5
174 (1h) 3 110 000         463.7          1232.1        9.7e-7
```

Čtení: jedna tranche nerozhoduje nic. Deset tranchí (asi 6 minut na 80
jádrech) už při generické hustotě čeká desítky zásahů, takže kladná
odpověď spadne brzy. Hodina dává mez kolem 1e-6 na sazbu v POJMENOVANÉ
míře, a to je nejsilnější výrok, který lze z běhu vytáhnout.

## 3. Přidaný cíl: hledat KAŽDÝ obrat znaménka, ne jen (7,0,9) proti (9,0,7)

Pilotní histogram unese obecnější tvrzení, kterého si runspec nevšiml.
Se signaturou s = POS - NEG:

```
((8,0,8),(8,0,8))  8083   s = 0, 0
((7,0,9),(7,0,9))   273   s = +2, +2
((7,0,9),(8,0,8))    41   s = +2, 0
((9,0,7),(9,0,7))    15   s = -2, -2
((8,0,8),(9,0,7))     4   s = 0, -2
((9,0,7),(10,0,6))    2   s = -2, -4
```

V žádném z 8 418 párů nemají konce OPAČNÁ znaménka signatury. Nula výjimek
na celém vzorku, ne jen na 290 vzácných párech. Pracovní tvrzení tedy je

```
SIGN-INVARIANCE  na fiber páru se znaménko signatury nikdy neobrátí
                 (může přejít do nuly a zpět, nikdy z + na -)
```

a T-A je jeho speciální případ +2 proti -2. Proč to chci logovat:

```
1  Je to čistší tvrzení a je to to, co by dokazovala strukturní věta.
   "Nepřekročí bod rovnováhy" je geometrická věta o tětivě proti
   symetroidu; "nespojí zrovna tyhle dva profily" je věta o dvou buňkách.
2  Je to VĚTŠÍ terč za stejnou cenu. Falsifikace se tím zlevňuje: stačí
   jakýkoli pár s opačnými znaménky, ne zrovna ten jeden.
3  Testuje se na CELÉM vzorku, ne na jeho vzácné části. Pilot dal 8 418
   testů obecného tvrzení proti 290 testům vzácné verze.
```

Poctivě, aby to nevypadalo lépe než to je: statistická síla proti
nezávislosti se skoro nezvedne (1.57e-4 proti 1.49e-4, tedy 1.06krát),
protože doplňkové buňky jsou drobné. Zisk je konceptuální a falsifikační,
ne statistický.

## 4. Doporučený primární readout: podmíněné rozdělení partnera

Nejrobustnější statistika, kterou pilot nabízí, není hustota, ale podmíněné
rozdělení, protože z něj vypadává marginální asymetrie z O1 i velká část
obav z O2:

```
podmíněno tím, že jeden konec je (7,0,9)  [587 konců]
    partner (7,0,9)  546   93 %
    partner (8,0,8)   41    7 %
    partner (9,0,7)    0    0 %
podmíněno tím, že jeden konec je (9,0,7)  [36 konců]
    partner (9,0,7)   30   83 %
    partner (8,0,8)    4
    partner (7,0,9)    0
oba konce mimo (8,0,8)  [290 párů]
    zarovnané          288
    obě strany rovnováhy 0
```

Toto je věcné jádro pilotu v podobě, která nezávisí na tom, jak přesně je
míra definována: vzácný konec si vybírá partnera se STEJNÝM profilem v 83
až 93 procentech a se zrcadlovým nikdy. Doporučuji to jako hlavní tabulku
běhu; hustotní mez s pravidlem tří ať je vedle ní, ne místo ní.

## 5. Co se v runspecu nemění

Dvoufázový návrh, oddělený seed a doména pro fázi B, oddělený agregát,
deterministické ukončení po celé tranchi při svědku, per-skeleton počty,
S_4 obraz a shoda charakteristických polynomů u každého páru s vzácným
koncem, seed a stream na jádro. A pořadí: falsifikace před strukturou.
