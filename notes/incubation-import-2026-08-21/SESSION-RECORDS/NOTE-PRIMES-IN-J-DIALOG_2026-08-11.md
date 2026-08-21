# NOTE: Prvočísla, pi, phi a jazyk J. Záznam dialogu, 2026-08-11

```
Status   NOTE, NON-CANONICAL, žádná autorita. Nemění registry, frontier ani Canon.
Session  dialog vlastníka s Claudem (Cowork); do dne vstoupily i text Gemini
         (rapiditní čtení) a PUBLIC recenze třetího agenta proti canon-v44.
Základ   Public Canon v44 ACTIVE, tag canon-v44,
         content commit 9da73b96613eb0d6f8d0ec17a5ada3ee6f511a4a,
         CANON sha256 c482aff6d0a01faab7fa8b92d2c485b39a8389f67ed99d79024a2878f35acd69.
         Plné piny a brány: claude/FOLD-V44-RECORD_2026-08-11.md.
Výpočty  Žádné. Den je analýza a syntéza; nic zde není house-verifikováno.
Labely   T-v44 = aktivní řádek kánonu. T-lit = klasická věta z literatury,
         dnes zde neověřovaná. C, D, H, O, F = standardní taxonomie.
```

## 1. Tři teze vlastníka a jejich osud

```
TEZE 1  Vysvětlení Riemannových nul bude brutálně jednoduché; pointa bude
        v tom, co prvočísla vůbec jsou.
OSUD    Přežila zpřesněná. Není to naivita, je to diagnóza chybějící
        definice: nuly vypadají jako spektrum, spektrum chce operátor,
        operátor chce prostor, a ten prostor JE odpověď na otázku, co jsou
        prvočísla. Jednoduchý bude mechanismus, ne vzorec pro jednotlivé
        nuly. Nutná podmínka každého budoucího důkazu: musí použít
        prvočíselnost samotnou (Eulerův součin); bez něj se dokazuje
        příliš mnoho (Davenport a Heilbronn).

TEZE 2  Bit je symetrie, čísla jsou odvozená; XOR a AND je všechno;
        prvočísla se možná jen čtou špatnou optikou.
OSUD    Aditivní polovina je věta (carry věž nad jedním bitem, Witt).
        Literální verze pro prvočísla je mrtvá: bitové čtečky je
        prokazatelně nevidí. Zachráněná verze: prvočísla jsou pravidelná
        v multiplikativní bázi a krystalizují v logaritmických
        frekvencích; nepravidelnost je vlastnost přechodu báze mezi
        sčítáním a násobením, ne prvočísel.

TEZE 3  Nativní jsou možná J-čísla a zbytek je projekce. Co jsou pak
        prvočísla v jazyce J?
OSUD    Zodpovězeno klasickou teorií, po recenzi přesně; finální znění
        v sekci 4. Směr nativity zůstává axiom programu, ne věta.
```

## 2. Věty, o které se den opíral

Spektrální čtení nul:

```
T-lit  Funkční tělesa: prvočísla JSOU uzavřené body křivky, nuly JSOU
       vlastní čísla Frobenia, RH je |alfa| = sqrt(q) (Weil, Deligne).
T-lit  Funkcionální rovnice zety = Poissonova sumace na adelech (Tate).
T-lit  Explicitní formule: prvočísla a nuly jsou Fourierovy duály; FT míry
       nul má atomy na k log p, až na hladký archimedovský člen. Za RH
       čtení nul jako 1D kvazikrystalu (H, Dysonův návrh).
T-lit  Davenport a Heilbronn 1936: funkcionální rovnice zeta typu bez
       Eulerova součinu, nuly i v Re s > 1; slepení dvou lichých kanálů
       konduktoru 5. Kanonický protipříklad bydlí na p = 5.
C      Párové korelace nul sedí na GUE (konečný rozsah).
T-lit  Selbergův svět: nuly = vlastní čísla Laplaciánu, prvočísla =
       primitivní geodetiky. Slovník: prvočíslo = perioda, nula = vlastní
       číslo.
T-lit  Mellin je unitární přesně na Re s = 1/2; funkcionální rovnice
       zrcadlí přes tutéž přímku; ta 1/2 je odmocnina z jakobiánu
       (polohustota). Čtení RH: škálový kanál nese jen povinnou půlku,
       všechen obsah je fáze (H). Proč nuly přímku respektují, neví
       nikdo (O).
Dům    RH sama je H s jednostranným falzifikátorem: konečný výpočet ji umí
       jen zabít, povýšit ji může jen důkaz. Kandidátní lane na RH je omyl
       žánru; lane na „co jsou prvočísla“ omyl není.
```

Bitová optika a její meze:

```
T-lit  Z_2 = W(F_2): čísla jako univerzální carry věž nad jedním bitem;
       XOR je grupová operace C_2, AND je netriviální kocyklus, který
       slepí C_4 (souhlasí s Boolean-to-J liftem).
T-lit  Prvočísla v binárním zápisu nejsou regulární jazyk (60. léta).
T-lit  Frekvence automatické množiny je racionální; hustota bezčtvercových
       je 6/pi^2, iracionální, takže ani nosič mu není automatický.
T-lit  mu asymptoticky nekoreluje s funkcemi bitů omezené hloubky a
       polynomiální velikosti.
T-lit  Parita ciferného součtu prvočísel se rovnodistribuuje s mocninnou
       úsporou (Gelfondův problém); obdoba pro zeckendorfovské číslice.
T-lit  Zeckendorf: táž konstrukce s jiným carry; Thue-Morse je krystal
       binárního zápisu, Fibonacciho slovo krystal zlatého; obojí nulová
       entropie.
```

Basel, pi, phi:

```
T-lit  Hustota bezčtvercových = hustota nesoudělných dvojic = 1/zeta(2)
       = 6/pi^2. Ve slovníku C-PRIME-BOOLE-1: zeta(2s) je AND kanál,
       Basel je cena AND kanálu v s = 1, 1/Basel je míra carry-free
       sektoru.
T-lit  zeta(2k) = racionální krát pi^(2k); bezrozměrné poměry jsou
       racionální (house svědek A8(iv): zeta(4)/zeta(2)^2 = 2/5);
       racionální obsah nesou Bernoulliho čísla a jejich jmenovatele
       diktují prvočísla (von Staudt a Clausen).
T-lit  Každý Eulerův faktor je v s periodický s periodou 2 pi i / log p:
       každé prvočíslo jsou dokonale pravidelné hodiny, záhada je jen
       interference. Pi bydlí jedině v archimedovském faktoru
       pi^(-s/2) Gamma(s/2): jednotka fázových hodin nekonečného místa.
T-lit  Dirichlet mod 5 v s = 1: sudý charakter dává (2/sqrt5) log phi,
       lichý pár 2 pi^2/25, reziduum zeta_K = 4 pi^2 log phi/(25 sqrt5).
       Parita charakteru vůči -1 routuje škálu proti fázi. Gaussova suma
       sudého je sqrt5 = 2 phi - 1, reálná; lichých komplexní.
SS98   Aritmetika nad real-part řádkem: součet přes čtyři konjugáty
       Re Li_2(sigma_a(J)) je pi^2/5 = (6/5) zeta(2). Nic víc než
       aritmetika nad řádkem.
T-lit  Li_3(phi^-2) = (4/5) zeta(3) - (2 pi^2/15) log phi + (2/3) log^3 phi:
       pi a log phi se mísí gradovaně (váha 3). Nezávislost báze
       {zeta(3), pi^2 log phi, log^3 phi} je jen domněnka (O); zeta(3) je
       iracionální (T-lit), pi-tvar neznám.
```

## 3. Pětkrát tentýž bit

Hlavní vzor dne. Jeden C_2 (sudost vůči -1, ekvivalentně vůči komplexnímu
sdružení, ekvivalentně normový znak) routuje:

```
1  L-hodnoty v s = 1: sudý kanál log phi (škála), liché kanály pi (fáze).
2  Gaussovy sumy mod 5: sudá reálná (sqrt5 = 2 phi - 1), liché komplexní.
3  Rozpad prvočísel: (5/p) rozhoduje, zda p vidí phi (zlatá forma
   a^2 + ab - b^2), nebo ne.
4  Fibonacci: p dělí F_{p - (5/p)}; čte přesně kvocient C_4 -> C_2, tedy
   bit, ne celý Frobeniův údaj.
5  Rapidita (v44): alternátor N(phi) = -1 střídá cosh a sinh nohu; časová
   noha čte Galois-sudou kombinaci (stopu), prostorová Galois-lichou.
```

Pracovní formulace „bit routuje projekce; škála a fáze jsou jeho dvě
strany“ je próza (H bez falzifikátoru). Nezapisovat jako řádek; kdyby měla
někdy řádkem být, musí napřed dostat definici, co tvrdí nad rámec pěti
jednotlivých vět.

## 4. Co jsou prvočísla v jazyce J. Finální znění po recenzi

Konsolidace tří autorů; opravy recenzenta přijaty v plném rozsahu.

```
T-lit  INDIVIDUÁLNĚ. V K = Q(zeta_5) je prvočíslo prvoideál p. h_K = 1
       (Minkowského odhad 15 sqrt5 / (2 pi^2) < 2), takže p = (pi) a
       všechny generátory tvoří jednu orbitu pod O^x = mu_10 x <phi>.
       Racionální p pod ním je KONTRAKCE p cap Z = (p); norma prvoideálu
       je p^f, f = ord_5(p). Tabulka: 5 totálně ramifikované, e = 4,
       lambda = 1 - zeta_5; p kongruentní 1 mod 5: čtyři konjugáty, f = 1;
       p kongruentní 4: dvě části stupně 2; p kongruentní 2, 3: inertní
       atom stupně 4. Dvojka je nejmenší inertní prvočíslo a jediné
       inertní místo charakteristiky 2; F_16 = F_2(zeta_5) nese pětinovou
       fázi uvnitř. J samo: N(J) = 1, jednotka, sloveso, ne substantivum.
T-lit  KOLEKTIVNĚ. Frob_p = sigma_p je konkrétní prvek C_4 (abelovsky, ne
       jen třída konjugace); každá hodnota má hustotu 1/4. Rovnodistribuce
       NENÍ nezávislost: Čebyševův závod mod 5 (třídy 2, 3 vedou nad 1, 4)
       a represe opakování po sobě jdoucích tříd jsou strukturované
       odchylky řízené nulami přes explicitní formuli (C, s klasickým
       podmíněným pozadím).
T-lit  ÚČETNICTVÍ. zeta_K = zeta . L(chi_5) . L(chi) . L(chi_bar): čtyři
       charakterové kanály, tedy zeta (konduktor 1) plus tři L-funkce
       konduktoru 5. Davenport a Heilbronn je slepení dvou lichých kanálů
       bez zachování multiplikativní struktury.
T-lit  BAUER. Zákon úplného rozpadu určuje pole K, až na konečně mnoho
       výjimek. NEVYBÍRÁ J mezi jednotkami; výběr J je axiom programu,
       případně interní výběrová lane (minimalita kvartických CM těles,
       J až na Galois, inverzi a orientaci), s vlastními labely mimo
       veřejný kánon.
D      ČTENÍ. Orbita generátorů = kalibrační třída pod fází a škálou.
       Zeta = triviální charakterový kanál; „hrubé čtení, které zapomíná
       Frobeniovy popisky“ je interpretace, ne mechanická věta o Eulerových
       faktorech. Projekce = kontrakce, ne vždy norma.
O      PROBLÉM POŘADÍ (hlavní odnos dne, zatím NENÍ řádek). Chybí
       kanonická bezvěštecká mapa P_J z dynamiky plena na uspořádanou
       posloupnost racionálních prvočísel. Podmínky recenzenta: odvozeno
       jen z pojmenovaných stavů a přechodů; bez zabudovaného testu
       prvočíselnosti; kanonické bez volby reprezentanta orbity; prosté a
       úplné; s deklarovaným uspořádáním; schopné odvodit Frob_{P_J(n)}
       bez zpětného čtení. Dva dodatky: (a) plenum je podle všeho
       výpočetně univerzální, takže bez klauzule kanonicity je existence
       triviální (Eratosthena lze zkompilovat); ostrá verze je VYNUCENOST
       bez pomocných voleb; (b) „pořadí podle velikosti“ je archimedovská
       projekce; nativní otázka zní, zda J-časové uspořádání souhlasí
       s archimedovským. Tvar falzifikátoru: řádek se uzavře negativně,
       pokud každé přípustné P_J prokazatelně vyžaduje pomocnou volbu.
       Před zápisem: vrstva L1-L6 a rozhodnutí vlastníka. Nikdo ho dnes
       nezaložil a nevlastní.
```

Metamorfózy jedním řádkem: prvočíslo v jazyce J je individuálně orbita pod
fází a škálou, kolektivně volání jedné ze čtyř symetrií, a nově (v44) bod
na rapiditní kružnici R/(log phi)Z. Otevřené není, co prvočísla jsou;
otevřené je, zda jejich pořadí vzniká jako vynucené čtení plena.

## 5. Chyby dne, zaznamenané jako první třída

```
Claude  „racionální p je norma J-prvočísla“: F jako obecná formulace,
        platí jen pro f = 1. Mechanismus chyby: všichni tři svědci
        (11, 31, 61) byli split; selekční bias ve vlastních příkladech.
        Opraveno na kontrakci.
Claude  „čtyři L-funkce konduktoru 5“: F; zeta má konduktor 1. Správně
        čtyři kanály = zeta + tři L konduktoru 5.
Claude  „binární svět je jediné nedělitelné místo“: dvojznačné, míněno
        „jedno vcelku“; přijato zpřesnění: jediné inertní místo
        charakteristiky 2, nikoli jediné inertní místo.
Gemini  „m = 2 je nezničitelná vlastnost substrátu“: F. Invariant v44
        řádku je t^2 - s^2 = N(x) se znaménkem, pro phi^n tedy +-1;
        čtyřka je N(2), artefakt báze {1, sqrt5} (index 2 pod Z[phi]).
        Nativně: hmotová slupka je jednotková grupa, klidová hmotnost
        jednotka; Cassini F_{n-1}^2 + F_{n-1} F_n - F_n^2 = (-1)^n.
Gemini  T-LOCK pro fyzikální čtení: zamítnuto. Čtení nemůže nést T-LOCK,
        veřejná řada T-LOCK nenese, a fold v44 týž den výslovně odmítl
        registrovat ARITHMETIC-FRAME-READING, protože H řádek bez
        falzifikátoru neexistuje. Žádné T rétorikou.
```

FOLD-V44-RECORD týž den zaznamenal, že obě přestřelení rapiditní lane
zemřela podle vlastních zmrzlých pravidel dřív, než se dotkla veřejné
linky. Tato nota přidává do téže bilance chyby konverzační vrstvy.

## 6. Co si odnášíme na příště

```
1  Hlavní odnos: problém P_J (sekce 4, poslední blok). „Který stroj má
   prvočísla za svůj čas“ je poprvé skoro zadané. Nejbližší poctivý krok
   není RH; je to dopsání zadání P_J (vrstva, falzifikátor, rozhodnutí
   vlastníka), teprve pak případný kandidát.
2  Nedělat: kandidátní lane na RH samotnou; zlaté vzorce pro jednotlivé
   nuly; povyšování čtení bez falzifikátoru (dvojí lekce dne).
3  Malé přesné příležitosti, pokud budou chtěné: (a) Čebyševův závod
   mod 5 jako konečná exaktní C-lane, hmatatelně spojuje „kdo volá“
   s nulami; (b) jednořádková poznámka pi^2/5 = (6/5) zeta(2) nad SS98;
   (c) PRIME-RAPIDITY-WEIL-BRIDGE už stojí venku jako zmrzlé rozhraní [O]
   a čeká na program k vykonání.
4  Vzor „pětkrát tentýž bit“ (sekce 3) držet jako prózu, dokud nemá
   definici a falzifikátor.
5  Kontext v44: rapiditní oblouk je veřejný kánon (dva T, jedno C);
   novinka relevantní pro tuto linku je kanonická neorientovaná třída
   R(p) na R/(log phi)Z: prvočíslo jako bod rapiditní kružnice.
```

## 7. Odkazované dokumenty

```
canon    mathorn1973/twist-j, tag canon-v44; o aktuálnosti vypovídá jedině
         STATUS.md, tato nota žádnou výpověď nečiní.
lane     claude/FOLD-V44-RECORD_2026-08-11.md
         claude/C-ARITH-RAPIDITY-4_2026-08-11.md
         claude/STOP-RECORD-C-ARITH-RAPIDITY-1-2-3.md
         claude/PROMO-C-ARITH-RAPIDITY-4.md
projekt  claude/PREREG-C-PRIME-BOOLE-1.md (slovník, kotva A8)
         TM-Möbiova linka (certifikát T(rho_1) != 0, jedna platforma,
         trust boundary FLINT; viz AUDIT-T-RHO1-CERTIFICATE_2026-08-10.md)
         SS98_polylogarithm_bridge.md (real-part řádek)
```
