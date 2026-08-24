# RECON: w4 struktura a změna metody po nákladovém readoutu

Status: NON-CANONICAL recon, gates nothing, no prereg. Nabídka do K4 lane;
tato session K4 lane NEVLASTNÍ a nic v ní nemrazí. Datum 2026-08-12.
Podnět: twisterový HOLD readout (skeleton 34094, nejméně 2 621 435 805 696
kandidátních párů, stále INCOMPLETE; 29 478 patternů, 54 399 signed
skeletonů) a rozhodnutí vlastníka Q2 census nespouštět. To rozhodnutí je
správné a níže je důvod silnější než cena.

Skripty (na uzlu pi, ~/jam/claude_scratch): recon_k4_w4_deltak_gate.py,
recon_k4_w4_weyl_sharp.py, recon_k4_chord.py, recon_k4_w4_sampler.py.
Vše exaktní celočíselná aritmetika, žádné numerické vlastní číslo; inercie
dvěma cestami (congruence a Berkowitz), profily frozen dvoucestnou rutinou.
Solver ani substrát jsem neupravoval, importuji frozen modul.

## 1. Nová strukturní věta: K je AFINNÍ ve znaménkovém vektoru

```
A1  K(u) = K_0 + sum_j u_j M_j,  u_j = (-1)^(v_j) v {+1, -1}
    Ověřeno exaktně: predikce z 65 jednobitových diferencí se rovná
    přímému kflat na 40 náhodných tabulkách, bit po bitu, 256 z 256
    složek. To je přesně důvod, proč je Delta K mask-only: pozorování
    K4 agenta z w2 je stín linearity a platí i na w4 (ověřeno).
```

Důsledek, který mění geometrii úlohy: fiber pár NENÍ dvojice bodů, je to
TĚTIVA hyperkrychle uvnitř lineární rodiny symetrických matic. Segment
K + t Delta, t v [0,1], je rovný. Přechod (7,0,9) -> (9,0,7) tedy znamená,
že tětiva protne determinantální nadplochu (symetroid) tak, aby dvě vlastní
čísla přešla nulou. K4 mašinérie na to už má nástroje (count_open01,
mobius01, poly_sign_at: počítání kořenů v otevřeném (0,1)).

## 2. Ostrá Weylova brána, spočítaná na všech 29 478 skeletonech

Nutná podmínka je ostřejší než rank: n_+(K + D) >= n_+(K) - n_-(D) a zpět,
takže přechod vyžaduje min(n_-(D), n_+(D)) >= 2.

```
rank D histogram   2:57  4:797  5:178  6:2770  7:580  8:5389  9:838
                   10:4861  11:820  12:10002  13:450  14:2656  15:80
inercie D          27 různých typů; jediný s min <= 1 je (1,14,1)
ZAVŘENO ZDARMA     57 z 29 478 skeletonů, bez jakéhokoli hledání
NOVÉ               3128 skeletonů má n_- != n_+ (liché ranky). Na w2 byla
                   každá perturbace vyvážená; na w4 vyváženost PADÁ. To je
                   strukturní rozdíl w2 proti w4, který nikde zapsán nebyl.
```

Poctivě: brána je na w4 slabá (57 z 29 478). Ale je exaktní, stála 90 sekund
a těch 57 už nikdo hledat nemusí.

## 3. Tětivový argument PADL, a to je informace

Weyl dává: aby dvě vlastní čísla přešla nulou, musí K nést aspoň dvě kladná
vlastní čísla pod ||Delta||_2. Změřeno exaktně (počty vlastních čísel v okně
přes inercii K - cI, žádná numerika):

```
ceil ||Delta||_2 přes 29 478 skeletonů:   min 3, medián 16, max 27
kladná vlastní čísla K v (0, c] na 400 náhodných tabulkách:
    c = 3    aspoň dvě u 275 ze 400
    c = 16   aspoň dvě u 400 ze 400 (typicky čtyři)
    c = 27   aspoň dvě u 400 ze 400 (typicky šest)
```

Závěr: ŽÁDNÁ NORMOVÁ PŘEKÁŽKA NEEXISTUJE. Tětiva je pohodlně dost dlouhá,
aby dvě vlastní čísla přenesla přes nulu. Pokud T-A na váze 4 platí, důvod
je aritmetický nebo strukturní, nikdy ne velikostní. Jedny jednoduché dveře
zavřené, poctivě, jako F.

Vedlejší nález téhož běhu, důležitý pro odhady: na náhodných tabulkách je
n_+(K) = 8 u 399 ze 400. Generický profil je (8,0,8); (7,0,9) je už sám o
sobě vzácný stratum (řádově 10^-3). To vysvětluje, proč dřívější solver
vyjmenovával (8,0,8), a je to vstup do počtu níže.

## 4. Změna metody, hlavní bod

Nákladový readout neříká jen, že census je drahý. Říká, že fibery jsou
astronomicky HOJNÉ. Z toho plyne obojí:

```
1  Vyčerpání je mrtvé v OBOU směrech. Nenajde svědka (moc velké) a
   nedokáže T-A (moc velké). Důkaz T-A na váze 4 tedy MUSÍ být
   strukturní. Twisterovo rozhodnutí Q2 nespouštět je správné a tohle
   je jeho silnější důvod.
2  Falsifikace se naopak stává LEVNOU. Jeden svědek stačí. Buď opačné
   páry na váze 4 existují a padnou při vzorkování, nebo je hustota
   profilů na fiber varietě silně nenáhodná, a to je přesně ta
   překážka, kterou musí budoucí no-go věta vysvětlit. Obě odpovědi
   jsou cenné a obě jsou levné.
```

Sampler proto NEENUMERUJE: používá frozen solve01 beze změny a randomizuje
ho jen náhodným napinováním podmnožiny bitů před voláním, bere první řešení
a měří sdruženou distribuci profilů (px, py).

## 5. Výsledek vzorkovacího běhu: mechanismus je DIAGONÁLNÍ KONCENTRACE

Protokol: seed 20260812, budget 40000 uzlů na pokus, náhodné piny 8 až 30
bitů, náhodný skeleton na každý pokus, 780 s na jednom jádru.
46 948 pokusů, 8 418 navzorkovaných fiber párů, 38 530 infeasible (přepnuté
piny), 0 undecided.

```
sdružený histogram profilů (neuspořádané páry)
   ((8,0,8), (8,0,8))    8083
   ((7,0,9), (7,0,9))     273
   ((7,0,9), (8,0,8))      41
   ((9,0,7), (9,0,7))      15
   ((8,0,8), (9,0,7))       4
   ((9,0,7), (10,0,6))      2
   ((7,0,9), (9,0,7))       0     <- hledaný opačný pár
```

Statistika, poctivě označená. Marginály přes 16 836 konců: (7,0,9) 587krát,
(9,0,7) 36krát, tedy p1 = 0.0349, p2 = 0.00214.

```
diagonála {(7,0,9),(7,0,9)}   nezávislost čeká 10.2, pozorováno 273
                              OBOHACENÍ 26.7 krát
antidiagonála {(7,0,9),(9,0,7)}
                              nezávislost čeká 1.26, pozorováno 0
                              samotná nula ZDE NIC NEDOKAZUJE (Poisson)
                              ale při stejném obohacení by čekala 33.5,
                              a nula proti 33.5 má p = 2.9e-15
```

To je věcné jádro běhu. Fiber podmínka konce NEROZPOJUJE, ona je SVÁZÁVÁ,
a sváže je specificky na SHODNÝ profil: koreluje diagonálu 27krát a
antidiagonálu neobohacuje vůbec. Slabá w4 verze toho, co je na w2 rovnost
spekter přes S_4 obraz. Známý w4 náhodný pár, oba konce (7,0,9), tedy není
výjimka: je typickým členem diagonální třídy, která má v této míře hustotu
kolem 3 procent. Tím se přeformuluje i jeho status: vysvětlit je třeba
diagonální koncentraci, ne jeden pár.

Dvě poctivé mezery, obě povinné pro produkční verzi:

```
M1  Vzorkovací míra je zkreslená konvencí. Znaménkový vzorec masky je
    fixní (+1,-1,+1,-1) a piny orientaci fixují taky, což se projevuje
    asymetrií 587 proti 36 mezi (7,0,9) a (9,0,7). Produkční sampler
    musí randomizovat znaménkový vzorec i orientaci, jinak je jakékoli
    tvrzení o hustotě artefakt.
M2  8 418 vzorků NEROZHODUJE existenci. Rozhoduje až rozsah, kde by
    nula byla nemožná i pod nezávislostí.
```

## 6. Doporučení do K4 lane, k rozhodnutí vlastníka

```
1  Dávku na Q2 census nerozbalovat. Vyčerpání je mrtvé, ne drahé.
2  Váha 4 falsifikačně: pustit produkční sampler s opravou M1 na 80
    jádrech. Jedno jádro dalo 8 418 vzorků za 780 s, takže 80 jader za
    hodinu dá řádově 3 miliony vzorků. Při nezávislosti by antidiagonála
    čekala kolem 450 zásahů, při diagonálním obohacení kolem 12 000.
    Nula na tom rozsahu je tvrdý strukturní signál; jeden zásah zabije
    T-A na váze 4 okamžitě. Tohle je správné využití noci místo censu.
3  Strukturní linka: tětiva proti symetroidu, s existující mašinérií na
    počítání kořenů v (0,1). Přechod = dva kořeny pencilu det(K + t D)
    v otevřeném intervalu. Konečný algebraický objekt, ne prohledávání.
4  Volný readout, který teď dává největší smysl: kolik z těch 273
    diagonálních (7,0,9) párů je S_4 obrazem? Rozdělí to diagonální
    koncentraci na symetrickou a genuinní část a je to hodina práce.
5  Zapsat linearitu K ve znaménkovém vektoru jako samostatný floor.
    Jednořádková věta, unese ji celá lane a dosud nebyla vyslovena.
6  Weight-2 vidlice ze včerejška beze změny: rozhoduje úplnost censu
    1512, ne mechanismus. Tímto reconem nedotčeno.
```
