# RUNSPEC: co má twister dnes večer počítat, a co ne

Status: NON-CANONICAL runspec, recon, gates nothing, no prereg. Návrh do
K4 lane, rozhodnutí vlastníka. 2026-08-12.
Podklad: claude/RECON-K4-W4-STRUCTURE-AND-METHOD_2026-08-12.md (pilotní běh
8418 vzorků na jednom jádru).

## 0. Krátká odpověď: jedna věc, ne pět

```
BĚŽÍ     w4 sampler, produkční verze s opravou M1. To je jediná úloha,
         která dnes potřebuje 80 jader.
NEBĚŽÍ   Q2 census. Vyčerpání je mrtvé v obou směrech, nerozbalovat.
NEBĚŽÍ   PROP-2C, PROP-2D, PROP-1. Jsou to důkazy a citace klasické věty.
         Nepotřebují ani jádro. Twister jim nemá co dát.
NEBĚŽÍ   Weilova věž. Čeká na ANO-7 a její nejbližší krok je minutová
         kontrola hodnosti proti seznamu nul, ne noční běh. Klidně na
         notebooku.
NEBĚŽÍ   k6. Potřebuje re-gate, což je administrativa, ne výpočet;
         přepočet není třeba, artefakty jsou pinované.
```

Jinými slovy: poslední tři hodiny přinesly hodně, ale skoro nic z toho
nepotřebuje cluster. Twister má dnes jednu jasnou úlohu.

## 1. Oprava M1 je POVINNÁ, jinak je nulový výsledek nečitelný

Pilot fixoval znaménkový vzorec masky na (+1,-1,+1,-1) a piny na
{a:0, b:1, c:0, d:1}. Důsledek byl měřitelný: marginály (7,0,9) 587 proti
(9,0,7) 36, tedy faktor 16. To znamená, že pilot vzorkoval jen jednu
stranu. Bez opravy by nulový výsledek nešel odlišit od "sampler tam
nedosáhl".

```
M1  Na každý pokus vylosuj znaménkový vzorec masky rovnoměrně mezi
    přípustnými (v každé orbitě musí maskované buňky být vyvážené) a
    piny nastav podle něj. Tím se marginály symetrizují.
```

Vedlejší efekt, který stojí za vyslovení: oprava test ZESILUJE. Očekávaný
počet antidiagonálních zásahů při nezávislosti je N krát 2 p1 p2, a to je
při pevném součtu p1 + p2 maximální právě když p1 = p2. Symetrizace
marginálů na p = 0.0185 zvedne 2 p1 p2 z 1.49e-4 na 6.85e-4, tedy zhruba
4.6krát více očekávaných zásahů na stejný počet vzorků.

## 2. Dimenzování a co běh rozhodne

Pilot: 8 418 vzorků za 780 s na jednom jádru, tedy 10.8 vzorku za sekundu.
80 jader po hodině dá řádově 3.1 milionu vzorků.

```
při 100 tisících vzorcích (asi 2 minuty na 80 jádrech)
    nezávislost čeká kolem 70 antidiagonálních zásahů
    -> pokud je T-A na váze 4 nepravdivá při generické hustotě,
       VÍ SE TO ZA PÁR MINUT, ne za noc
při 3.1 milionu vzorcích (hodina)
    nezávislost čeká kolem 2 100
    profilově slepá korelace (obohacení 27x) čeká kolem 57 000
    -> nula na tomto rozsahu ohraničuje hustotu pod 3e-7 a zabíjí
       model slepé korelace s odstupem, který se nedá přehlédnout
```

Běh je tedy sebeukončující, když je odpověď kladná, a teprve hodina dělá
silný negativní výrok. Rozumné je pustit hodinu a číst průběžně.

## 3. Dvoufázový návrh, pokud má běh dostat víc než hodinu

Uniformní vzorkování utratí kolem 96 procent rozpočtu na páry
((8,0,8),(8,0,8)), které nikoho nezajímají.

```
Fáze A  uniformně, s M1, prvních zhruba 15 minut. Dává nezkreslený
        odhad hustoty a marginálů. Tohle je ta čísla, která se citují.
Fáze B  podmíněně: dál vzorkovat jen skeletony, které ve fázi A daly
        aspoň jeden konec v (7,0,9) nebo (9,0,7), a v nich hustěji.
        Zvyšuje výtěžnost ve vzácném stratu řádově, ALE je to zkreslená
        míra a smí sloužit jen k HLEDÁNÍ SVĚDKA, nikdy k odhadu hustoty.
        Ta dvě čísla se nesmí smíchat do jednoho readoutu.
```

## 4. Co logovat, readouty bez prahů

```
1  plný sdružený histogram profilů, ne jen vzácné buňky
2  per-skeleton počty, aby bylo vidět, jestli je diagonální koncentrace
   rovnoměrná, nebo ji táhne pár skeletonů
3  u KAŽDÉHO páru dotýkajícího se (7,0,9) nebo (9,0,7): je druhý konec
   S_4 obrazem prvního? shodují se charakteristické polynomy? To je ten
   levný readout, který rozdělí diagonální koncentraci na symetrickou a
   genuinní část, a je to nejdůležitější vedlejší produkt běhu
4  akceptační poměr a rozdělení počtu pinů, jako detektor zkreslení
5  seed a stream na jádro, aby byl běh reprodukovatelný
6  první opačný pár: uložit svědka, vytisknout, a skončit. Jeden svědek
   stačí a další hledání je plýtvání
```

## 5. Jak číst výsledek, předem

```
NALEZEN SVĚDEK   T-A na váze 4 je F. Okamžitě, jedním párem. Weight-2
                 věta tím není dotčena a zůstává tím, čím je.
NULA na 3e6      hustota opačných párů pod 3e-7 v uniformní míře, a
                 model profilově slepé korelace padá. NENÍ to důkaz T-A;
                 je to změřená překážka a zadání pro strukturní důkaz,
                 který půjde cestou tětiva proti symetroidu.
NULA na málo     nerozhoduje nic. Pod zhruba 100 tisíci vzorky se nic
                 netvrdí.
```

## 6. Jedna poznámka k pořadí

Pokud by se mělo volit mezi během a hodinou algebry, volil bych běh, a to
z jediného důvodu: falsifikace je levná a rychlá, a dokud není vyloučená,
je každá hodina strávená důkazem T-A hodinou, která může být zbytečná.
Strukturní linka má smysl začít až po nulovém výsledku na rozsahu.
