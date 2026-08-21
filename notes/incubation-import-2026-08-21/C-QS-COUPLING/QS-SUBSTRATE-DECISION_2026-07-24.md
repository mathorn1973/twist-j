# QS-SUBSTRATE-DECISION. Rozhodnutí substrátové otázky, 2026-07-24

Rozhodovací memo lane, žádná autorita. Otázka zněla: rozlousknout a rozhodnout
substrát, bez kterého se program nehne. Tady je rozhodnutí, s nálezy a štítky.

## Měna

```
Public Canon v19 ACTIVE, main 2c99ed2, content commit f05cc507,
Canon SHA-256 2695671d, 94945 B, SHA256SUMS 5 z 5 OK (vlastní clone).
QUANT-SUBSTRATE [O, ROOT/READY/FORMAL], v17 řádka QUANT-SCHWINGER-TARGET [T].
Veřejný canon nenese žádný s = 2 objekt v bodě J (grep: nula výskytů Li_2).
```

## Nález A: zeď není utajovací, je konstrukční [nález, exkavace v184]

Prohledán zapečetěný interní ledger (v184 snapshot v projektu). Schwingerova
větev tam je JEN jako hypotéza s hodnotou: H-GB-SCHWINGER, J Jbar/script-Q =
1/(2 pi), "gated on SS96.4". SS96.4 je klasifikační tabulka shadow funktoru a
její relevantní řádky jsou OTEVŘENÉ konstrukce: Maxwellova dynamika
"construction needed", Diracův spinor tehdy otevřen (v160 už uzavřen, Dirac
ladder G1 az G5), renormalizace vedena jako artefakt rozlišení. Žádná zmrazená
substrátová vazba pro Schwingerův koeficient v zapečetěném ledgeru neexistuje.

```
DŮSLEDEK: odpečetění interní linie Schwingerovu bránu neotevře. Chybějící
objekt není schovaný, nýbrž nezkonstruovaný. Formulace "sealed coupling"
z předchozích seancí se tímto opravuje na "unconstructed coupling".
```

## Nález B: co zmrazené JE (stavební kameny konstrukce)

```
Diracův krok        D_J(m) = S(I + i m X), nula volných parametrů, det = 5,
                    elektron m = 2, mass shell exaktní          [T, v160, interní]
argumentový kanál   Z_5 fiber, F = dA, depozity v pětinách, flux ζ_5
                    (kernel-to-cell slovník)                     [D, interní]
míra                Born čtverec, obě W-CENSUS faces, MUB 1/5    [T, v159, interní]
strom (s = 1)       Li_1(J) = i pi/5 kotva veřejná; g = 2 = arg J / půlúhel;
                    Larmorova klauzule uzavřena veřejně          [public T/D + candidate-D]
target (s = 2)      J Jbar/script-Q = 1/(2 pi)                   [public T, v17]
alpha sektor        Queen form alpha = 5S/((8 pi)^2 sqrt(s)),
                    L(2, chi5) = 4 pi^2/(25 sqrt5) exaktně       [public D/T/C]
s = 2 příčka zdi    Re Li_2(J) = pi^2/100, kanály 1 : 9,
                    trace pi^2/5                                 [DNES: candidate-T, dvouarch.]
```

## Rozhodnutí

Substrátová otázka se redukuje na KONSTRUKCI JEDNOHO pojmenovaného objektu:

```
Zmrazená vazba kvantované fluktuace argumentového kanálu (Z_5 fiber, flux ζ_5)
na Diracův krok D_J(2): vertex + kernel odezvy + čtení koeficientu, bez nové
bezrozměrné normalizace. Verejná v19 řádka to říká přesně: "deriving it as
[alpha^1]((g_e(alpha)-2)/2) from a substrate coupling remains open".
```

Cesta, kterou navrhujeme vlastníkovi (vzor je čerstvý: v19 TM-SYM2 owner
disposition):

```
1. OWNER DEFINITION DOC: zmrazit definici vazby (vertex na kroku, kernel
   odezvy, pre/post-update čtení, normalizační klauzule). Bez toho není co
   počítat; s tím je koeficient konečný exaktní výpočet.
2. PREREG P-QS-COUPLING-1: target už je T (QUANT-SCHWINGER-TARGET); falzifikátor
   už je veřejný (jiná hodnota, nová volná normalizace, dvě přípustné vazby);
   vrstva L5 -> L6, pojmenovaná brána. Všechny tři výstupy jsou první třída:
   pozitivní uzávěr, negativní uzávěr, nebo poctivé underdetermined s
   vypáleným falzifikátorem.
3. Stejný vzor odblokuje druhou horkou lane: TM-SYM2-PHYSICAL-MEASURE [O, STOP]
   čeká na owner freeze successor L5 source schema. Dva owner-freezy jsou teď
   jediné blokátory obou horkých lane. Agent je připraven obě preregistrace
   naplnit, jakmile definice zmrznou.
```

## Co se dnes postavilo (pohyb, ne jen mapa)

C-WALL-LI2-RUNG-1, candidate-T, dvouarchitekturně byte-identické (x86_64 +
aarch64): Re Li_2(J) = pi^2/100 = pi^2/(2p)^2; kanálový zákon 1 : 9 vynucený
exaktní modulární dichotomií phi^-1 < 1 < phi; trace pi^2/5; genesis 6/5;
excess pi^2/30. Proč je to substrátový pohyb: strom (s = 1, Li_1 = i pi/5) už
je uzavřen Larmorem; Schwingerův koeficient je s = 2 výrok a pi^2 v alpha
sektoru vstupuje přesně na s = 2 patře. Interní ledger tuhle příčku zná
(polylogaritmický most; pi jako locked shadow); veřejná zeď ji neměla. PROMO
je připraveno; validace veřejnou sondou P-WALL-LI2-RUNG-1.

Bonus: Larmorova sada z předchozí seance má hotový aarch64 leg, byte-identický
se zapinovanými x86_64 hashi: aritmetika C-LARMOR-TREE-GATE-1 tím jde z
candidate-C na candidate-T (dvouarch.), celkové čtení candidate-D drží.

## Štítky

```
Zeď je konstrukční, ne utajovací          nález (exkavace, citace výše)
Re Li_2(J) = pi^2/100 + kanálový zákon    candidate-T (dvouarch., PROMO ready)
Larmor aritmetika                         candidate-T (dvouarch. leg doplněn)
Schwingerova fyzikální brána              O, beze změny; chybí owner definition
                                          vazby; pak je to konečný exaktní výpočet
```
