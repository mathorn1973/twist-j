# Fixed-Delta lokalizace, a proč je lichý rank teorém

Status: NON-CANONICAL analýza, gates nothing. 2026-08-12.

## 1. Co fixed-Delta test uzavřel

Na 177 přesně identických Delta: plus 0 protnutí ze 197 záznamů, minus 72
ze 189, tedy 38.10 %. Po skeletonech 65 ku 0 ve prospěch minusu a 112
oboustranných nul, přičemž ani jednou plus neprotíná víc a ani jednou
neprotínají obě strany. To vylučuje každý mechanismus závislý výhradně na
masce nebo na Delta, a vylučuje ho párováním, ne standardizací, což je
silnější. Rankový bound to potvrzuje z druhé strany: TV vzdálenost 0.0843
připouští nejvýš 8.43 bodu z pozorovaných 34.38, a po přerovnání na pooled
rozdělení rozdíl neklesne, ale vzroste na 36.04 bodu.

Bezpečná lokalizace je vlastníkova: asymetrie sídlí v M, přesněji ve
vzájemné poloze M a pevného Delta. Nelze říct „v M samotném", protože
relevantní může být zarovnání.

Nemonotonie pooled protnutí (2.4 až 3.8 % na rancích 6 až 11, skok na
9.78 % při ranku 12, pak pokles) je při side-conditioned pohledu vysvětlená:
plus zůstává pod 0.86 % v každém ranku, minus roste z 15 až 26 % na 49 až
67 %. Pooled křivka je tedy směs dvou monotónních, ne vlastní jev.

## 2. Lichý rank: 0 ze 496 není datum, je to teorém

Oprava „nízký SUDÝ rank" je správná a má triviální důvod, který ji celou
vysvětluje:

```
deg det(A + t Delta) = rank(Delta) genericky (u vlastníka 44 ze 46).
Reálný polynom LICHÉHO stupně má vždy aspoň jeden reálný kořen.
Tedy při lichém ranku je bezkořenovost NEMOŽNÁ, ne vzácná.
```

Nula ze 496 na lichých rancích do 10 tedy není měření, je to důsledek. A
tím se deflace 46 dokončuje bez zbytku: paritní část je triviální a nízká
část je stupňový ocas, přesně jak tabulka ukazuje. Po odečtení obojího na
těch 46 nezbývá žádné reziduum, které by volalo po vysvětlení. Jediná
výhrada: stupeň může být menší než rank (dva případy deg 4 při ranku 6),
takže lichý rank vylučuje bezkořenovost jen genericky, ne absolutně.

## 3. Dva kroky, které lokalizaci posunou z binární na spojitou

Binární „protíná nebo ne" zahazuje informaci, kterou už máte spočítanou.

```
N1  PÁROVANÝ SPOJITÝ READOUT na 177 sdílených Delta: pro každý pár
    záznamů (plus, minus) při TÉMŽE Delta vypsat nejmenší |kořen|
    polynomu. Delta je identické, takže se polynomy liší jedině přes
    A = 2M, a rozdíl je čistě efekt M. Dá to velikost efektu, ne jen
    znaménko: je plus jen o kousek dál od stěny, nebo o řády? To
    rozhodne, jestli je jev spojitý posun nebo strukturní zeď.
N2  CENSUS BLÍZKOSTI NULY u M podle strany, exaktně a bez numeriky:
    počet vlastních čísel A = 2M v (-c, c) přes žebřík racionálních c,
    spočtený inercií A - cI a A + cI. Hypotéza k otestování: minusová M
    nesou systematicky víc vlastních čísel blízko nuly, tedy stratum
    (9,0,7) je tenčí a leží blíž ke stěnám. Sedí to s tím, že (9,0,7) je
    v korpusu 4.71 krát méně obsazené a na náhodných tabulkách 1.69 krát;
    menší míra a větší blízkost ke stěnám je jedno tvrzení dvakrát.
    Falzifikace je přímá: kdyby se rozdělení blízkosti nuly nelišila,
    padá i tohle a asymetrie je v zarovnání M vůči Delta, ne v M.
```

N2 je jediná zbylá hypotéza, kterou v této lane ještě umím nabídnout, a
píšu ji s vědomím, že šest předchozích padlo. Je aspoň levná a přímo
falzifikovatelná.

T-A zůstává H.
