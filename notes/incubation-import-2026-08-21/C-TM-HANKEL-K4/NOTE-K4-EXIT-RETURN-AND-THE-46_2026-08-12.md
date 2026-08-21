# Rozklad 63x na dva jevy, a co je na 46 doopravdy vzácné

Status: NON-CANONICAL analýza, gates nothing, počítáno jen z vlastníkových
čísel a z mého dřívějšího inercního censu Delta. 2026-08-12.

## 1. Trace: vyvráceno pořádně, přijímám

AUC 0.6729 a balanced accuracy 63.30 % na 8093 diagonálách, přičemž žádný
práh neporazí triviální „vždy plus" (82.491 proti 82.516 při libovolné
klasifikaci podle přesné hodnoty). Asociace je slabá ale nenulová, což je
víc než nic; jako mechanismus je to mrtvé. Můj test na 35 vzácných
náhodných tabulkách byl podceněný a tohle je ta správná verze. Zapsáno.

## 2. Test smíšených párů rozkládá 63x na dva různé jevy

Vlastníkova čísla umožňují rozklad, který jsem předtím neudělal a který
mění čtení. Pro každou stranu vezmi VŠECHNY páry s aspoň jedním vzácným
koncem, tedy diagonální plus smíšené, a rozděl je podle osudu tětivy:

```
konce (7,0,9)   8132 párů   nikdy neopustí 6639 (81.6 %)
                            opustí a vrátí se   37 ( 0.45 %)
                            opustí a zůstane  1456 (17.9 %)
konce (9,0,7)   2113 párů   nikdy neopustí  922 (43.6 %)
                            opustí a vrátí se  495 (23.43 %)
                            opustí a zůstane   696 (32.9 %)
```

Odtud dvě zcela různé pravděpodobnosti:

```
P(opustí)             0.1836  proti  0.5637     poměr   3.07 x
P(vrátí se | opustí)  0.0248  proti  0.4156     poměr  16.77 x
součin                                                 51.5 x
```

To je věcná oprava mého tloušťkového čtení. Menší část asymetrie je o tom,
JESTLI tětiva komoru opustí, tedy o tloušťce. Větší část, skoro
sedmnáctinásobek, je o tom, JESTLI SE VRÁTÍ, když už opustila. A to není
tloušťka výchozí komory, to je tloušťka toho, čím prochází: na záporné
straně tětiva sousední komoru typicky jen prořízne a vrátí se, na kladné
straně odejde a zůstane.

Vlastníkovo upozornění, že 63x je vlastnost vzorkované tětivy a ne holé
geometrie, tím platí ještě víc: rozklad ukazuje, že se tam mísí dva jevy
s opačnou interpretací. Poměr 2.005x ze smíšeného testu je přesně ta
tloušťková složka, a je řádově menší než 63x, což sedí.

## 3. Na těch 46 není vzácná vyváženost. Je to RANK

Vlastník uvádí, že každé Delta mezi 46 má vyváženou inercii, typy
(1,14,1), (2,12,2), (3,10,3), (4,8,4), (5,6,5). Z mého dřívějšího censu
inercií Delta přes všech 29478 weight-4 skeletonů plyne, co je na tom
opravdu neobvyklé:

```
vyvážených Delta celkem              26350 z 29478 = 89.39 %
takže „všech 46 vyvážených"          P = 0.894^46 = 0.0057
                                     významné, ale ne dramatické

mezi vyváženými má rank <= 10        13760 z 26350 = 52.22 %
takže „všech 46 má rank <= 10"       P = 0.522^46 = 1.05e-13
```

Vyváženost je tedy z velké části základní stav, kdežto omezení na rank
nejvýše 10 je astronomicky nepravděpodobné. A hlavně: dva NEJČASTĚJŠÍ
vyvážené typy, (6,4,6) s 9934 výskyty a (7,2,7) s 2656, mezi 46 nejsou
vůbec, ačkoli (6,4,6) je vůbec nejběžnější typ v celém censu.

A dává to mechanický smysl, což je dobré znamení, ne špatné: stupeň D se
rovná ranku Delta (u vlastníka 44 ze 46), a polynom malého sudého stupně
bez reálného kořene je snadný, kdežto stupně 12 nebo 14 bez reálného
kořene je vzácný. Rootlessness tedy silně preferuje nízký rank.

TESTOVATELNÁ PREDIKCE, zadarmo na korpusu: podíl bezkořenových záznamů
jako funkce rank(Delta) má strmě klesat. Když klesá zhruba tak, jak by
klesal pro polynomy daného stupně, jsou ta 46 jen nízkostupňový ocas a
žádná hlubší struktura tam není. Když některý rank vyčnívá, tam je
struktura. Tohle rozhodne, jestli je ta podtřída cíl, nebo artefakt.

## 4. Ke „kdy je -det(A + t Delta) striktně kladný na R"

Formulace nejmenšího algebraického cíle je správná a má dvě klasické
adresy, obě exaktní a obě levné, takže bych je zkusil dřív než cokoli
vlastního:

```
1  Reálný univariátní polynom je striktně kladný na R právě tehdy, když
   je součtem dvou čtverců reálných polynomů; nad Q je kladný polynom
   součtem nejvýše pěti čtverců v Q[t] (Pourchet). SOS rozklad těch 46
   je tedy exaktní certifikát a je vypočítatelný. Otázka, která z toho
   vypadne: mají ty čtverce aritmetický smysl v termínech M a Delta?
   Kdyby ano, je to hledaná charakterizace.
2  Klasický kontext je teorie DEFINITNÍCH pencilů. Pro dvojici reálných
   symetrických matic platí, že existuje-li reálná lineární kombinace,
   která je pozitivně definitní, jsou obě současně diagonalizovatelné
   kongruencí a všechna zobecněná vlastní čísla jsou REÁLNÁ. Absence
   reálného kořene tedy implikuje, že ŽÁDNÁ reálná lineární kombinace
   A a Delta není definitní. Těch 46 jsou v tomto smyslu maximálně
   indefinitní pencily, a klasická míra vzdálenosti k definitnosti,
   Crawfordovo číslo, je pro ně nulová.
```

Bod 2 dává okamžitou a levnou nutnou podmínku, kterou lze testovat na
celém korpusu, ne jen na 46, a která nepotřebuje kořeny: existuje reálná
kombinace alpha A + beta Delta pozitivně definitní? Jestli ano, pencil má
reálná vlastní čísla a bezkořenový být nemůže. To je rychlejší filtr než
Sturm a je to standardní věta, ne moje hypotéza.

Ireducibilita všech 46 nad Q, kterou vlastník změřil, k tomu sedí: kdyby
byl pencil rozložitelný na menší bloky, byla by definitnost snadnější a
polynom by se rozpadl. Ireducibilita je tedy konzistentní s maximální
indefinitností a je to hezký nezávislý indicií.

## 5. Bilance

```
moje, vyvráceno na správném korpusu   trace jako rozhodovač strany
moje, opraveno tímto rozkladem        tloušťkové čtení 63x; větší část
                                      té asymetrie je návrat, ne tloušťka
moje, přidáno                         rank <= 10 je pravý signál u 46,
                                      vyváženost je z 89 % základní stav
ukazatel do klasiky                   SOS certifikát a definitní pencily
                                      s Crawfordovým číslem
```

T-A zůstává H.
