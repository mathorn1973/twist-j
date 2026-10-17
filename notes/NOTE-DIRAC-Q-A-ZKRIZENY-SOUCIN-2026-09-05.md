# Diracova q-čísla, zkřížený součin, a co v TWIST-J skutečně drží

```text
STATUS   NON-CANONICAL. Terminologická brzda a jedno přesné umístění algebry.
         Nezakládá claim, nemění registr, frontier, status ani žádnou bránu.
         Není to sonda a není pinovaná.
BASIS    Public Canon v77. Doslovné znění registrových řádků čteno z
         canon/REGISTRY.tsv na commitu 8ea01cd.
OVĚŘENO  12 z 12 kontrol, exaktně (Fraction), žádný float v žádném tvrzení.
         Skript notes/NOTE-DIRAC-Q-A-ZKRIZENY-SOUCIN-2026-09-05.check.py,
         sha256 souboru
           7624d22523cc64ed6fc0ca5008dadcc2d7f624bca27137f16d467c9f7ec23b90,
         sha256 stdout
           affc6235ce8d5f07bcfcf258ac5b79a45616064c5ae49fedda18908b4a36868d,
         dva běhy s byte-identickým stdout, x86_64 CPython 3.11.15 a
         arm64 CPython 3.9.6. Pin před prvním spuštěním nebyl, takže je to
         auditní vstup, ne veřejná evidence, a nepovyšuje to nic.
DATUM    2026-09-05
PŮVOD    inkubační relace plus vlastnická oponentura, dvě kola. Osm tvrzení
         první verze bylo staženo jako F, jsou vypsána v oddílu 9.
```

## 0. Závěr napřed

```text
Registrovaná dvojice P, S na kruhovém kvocientu generuje reprezentaci
O_K x| C_4; po racionalizaci jde o End_Q(K).

Násobicí podalgebra je maximální komutativní podalgebra operátorů.
Diracovu c-stranu tvoří skaláry.

Normálnost násobení platí vůči výslovně určenému konjugačnímu adjungování.

Ztotožnění této konstrukce s úplnou fyzikální q-vrstvou zůstává
samostatnou hypotézou.
```

Celá poznámka je o jediné disciplíně: **které struktury držíš pevně.** Tři z jejích
oprav jsou tentýž typ chyby, jen na třech místech. Prvek versus operátor. Komutant
podalgebry versus střed algebry. Unitární třída operátoru versus operátor
i s aritmetikou, kterou zachovává.

## 1. Dvě různá q

```text
Diracovo q-číslo      nekomutující dynamická veličina, 1925 až 1926.
                      Protějšek c-čísla. c-číslo = skalární násobek identity.
Kvantové číslo [n]_q  deformační parametr, [2]_q = q + q^-1.
```

Společné mají jen písmeno. Naše j a m jsou hodnoty toho druhého q, ne příklady
prvního. Záměna těch dvou je nejsnazší chyba v celé oblasti.

Historicky navíc: *On Quantum Algebra* má víc axiomů než komutační pravidlo a
c-čísla tam vystupují jako podtřída q-čísel; naivní zobrazení Poissonovy závorky
na komutátor naráží na Groenewoldovu a van Hoveovu překážku; ket je stavový
vektor, ne q-číslo; a Hilbertův prostor algebru nenahradil, dal jí prostor, na
kterém se reprezentuje.

## 2. c-strana jsou skaláry, ne maximální komutativní podalgebra

Nosič `K = Q(j)`, báze `(1, j, j^2, j^3)`, `A = { M_x : x v K }`.

```text
A' = A                                komutant A je A, tedy A je MASA
Z(End_Q(K)) = Q . I                   střed, tedy Diracova c-strana
```

Důkaz první rovnosti je jednořádkový: komutuje-li T se všemi násobeními, pak
`T(x) = T(M_x 1) = M_x T(1) = x T(1)`.

Komutant podalgebry a střed celé algebry jsou různé objekty. Označit `A` za
c-vrstvu je táž chyba jako označit za c-číslo prvek J: prvek v okruhu komutuje,
operátor `M_J` skalární není (kontrola 1).

Ani „úplný soubor komutujících pozorovatelných je doslova okruh" neplatí, protože
obecné `M_x` není samoadjungované. Po komplexifikaci a pevném adjungování lze
z komutující normální rodiny udělat společný spektrální popis; skalární hodnoty
pak dávají vložení `sigma_a : K -> C`, a ta nejsou totožná s operátory `M_x`.

```text
skaláry         Q . I                       c-strana
komutativní rám A = {M_x}, MASA             ne c-strana
skalární data   vložení sigma_a : K -> C    spektrum rodiny, ne operátory
```

## 3. Umístění: co registrovaná dvojice generuje

Obecně, pro Galoisovo `K/Q` s grupou `G`:

```text
K x| G  ---> End_Q(K),   sum_gamma a_gamma [gamma]  |-->  sum_gamma M_(a_gamma) gamma
izomorfismus; pro K = Q(j), G = C_4 je to End_Q(K) = M_4(Q)
```

Na registrovaném modelu kruhového kvocientu, `I = (1 + delta)^-1 O_K`,
`P = M_delta`, `S = M_(delta^4) gamma_3`:

```text
gamma_3 = P^-4 S            Z[delta] = O_K
Z<P, S> = rho_I(O_K x| C_4)
```

To je přesné umístění algebry generované touto dvojicí, nic víc. `S` je
semilineární, tedy je to doslova prvek zkříženého součinu; nekomutativita
nepřišla ze slabšího předpokladu, přišla z druhého generátoru jiného typu.

Pozor na nosič: komutant samotného `M_J` je na `K` komutativní, protože
`Q[J] = K`. Na `K^r` s diagonálním působením je komutant `M_r(K)`, pro `r > 1`
nekomutativní. Samo slovo ekvivariance abelovost nezaručuje.

Pro případnou celočíselnou sondu je podstatné, že inkluze je vlastní, a je
změřená (kontroly 9 a 10):

```text
O_K x| C_4  je vlastní podokruh  End_Z(O_K)
index 5^6 = 15625
souřadnicová projekce E(a_0 + a_1 j + a_2 j^2 + a_3 j^3) = a_0
leží mimo, v křížové bázi má jmenovatele právě 5
```

Mezera tedy sedí přesně na rozvětveném prvočísle. To je celočíselné a levné
téma na samostatnou sondu, pokud ho někdo bude chtít.

## 4. Normálnost je vlastnost dvojice, ne operátoru

Normálnost bez určeného adjungování není tvrzení. Na témže nosiči, v téže bázi:

```text
eukleidovská forma (Gram = I)     M_J M_J^T != M_J^T M_J,  vstup 11 je 3 proti 2
h(x,y) = (1/5) Tr(x ybar)         M_J^*h = M_Jbar,  [M_J, M_J^*h] = 0
```

(kontroly 2, 3, 4). Rozhoduje kombinace komutativity okruhu a stability vůči
konjugačnímu adjungování, ne komutativita sama. Pro každé `a` v `K` platí
`h(M_a x, y) = h(x, M_abar y)`, tedy `M_a^*h = M_abar`.

```text
M_J M_J^*h = M_(2 - phi) = M_(phi^-2)          kontrola 5
```

## 5. Polární rozklad opouští racionalitu

Nové v tomto kole, plyne z oddílu 4 a je exaktně ověřené (kontrola 6).

Při pevném `h` polární faktory `M_J = U B` komutují s `M_J` i mezi sebou,
protože `A` je komutativní a `B` leží v jejím reálném uzávěru. Konkrétně:

```text
B = (1 / sqrt5) (3 I - M_phi)          1/sqrt5 je reálný skalár, ne prvek K
(3 I - M_phi)^2 = 5 (2 I - M_phi)      exaktně, v celých číslech
B^2 = M_J M_J^*h                       tedy B je kladný polární faktor
U = M_J B^-1                           U U^*h = M_J M_J^*h B^-2 = I
```

Podstatné je tohle: `B^2` leží v `A`, ale `B` neleží ani v `End_Q(K)`. Zapsat
`B` jako `M_x` by vyžadovalo `x` v `K` s `sigma_1(x) = phi^-1` a
`sigma_2(x) = phi`, jenže na `K^+ = Q(sqrt5)` je `sigma_2` právě záměna
`sqrt5 -> -sqrt5`, takže druhá hodnota vyjde `-phi`. Kladný polární faktor tedy
v okruhu neexistuje.

```text
M_J je celočíselný.  Rozdělení na fázi a škálu není.
1/sqrt5 v zaznamenaném U_5 a B není artefakt modelu, je vynucené.
```

To je algebraický důvod, proč vidlice mezi surovým `J` a jeho unitární částí není
jen otázka vkusu: druhá větev stojí peníze v podobě iracionality, kterou první
větev nemá. Fyzikální volbu to nerozhoduje.

## 6. Zlaté q je 1 - J, podmíněně

```text
delta = 1 - J = -j^2,   rad 10
[2]_delta = delta + delta^-1 = -j^2 - j^3 = phi        přesně definice phi
Tr(delta^n), n = 0..9 = (4, 1, -1, 1, -1, -4, -1, 1, -1, 1)
```

(kontroly 11 a 12). Ta stopová řada je doslova charakter registrovaného řádku
`J-GALOIS-CIRCULAR-ODD-CHARACTER`. Zlaté `q` tedy není importovaná konvence,
je to `1 - J`.

Podmínka, která k tomu patří: identifikace `delta` jako determinantového
charakteru je vázaná na zmrazený chirální ribbon lift z `P-J-FIBONACCI-BRAID-1`.
Registrovaný scope vylučuje opačnou chiralitu a jiné normalizace. Podmíněnost je
součástí tvrzení.

Pozor také na to, že `[2]_j = j + j^-1 = phi^-1`, nikoli `phi`. Přechod mezi
parametrem `j` v pleteních a `delta` v symetrickém kvantovém čísle se musí psát.

## 7. Permutační unitarita a co znamená slepá

Pro jednotku `u` nekonečného řádu je `V_u |x> = |u x>` unitární na `l^2(O_K)`.
Všechny nenulové orbity jsou nekonečné a orbit je spočetně nekonečně mnoho
(násobení jednotkou zachovává absolutní normu a kladná celá čísla `n` mají
navzájem různé normy `n^4`). Proto

```text
V_u  =  1_C  (+)  (+)_{k=1..nekonecno} W          W oboustranny posun
```

pro každou takovou jednotku, tedy unitární ekvivalenční třída samotného `V_u`
tyto jednotky nerozlišuje. To není „nula bitů" o `J`: se zachovanou aritmetickou
strukturou rozdíl zůstává. Pro označené translace `T_a |x> = |x + a>` platí

```text
V_u T_a V_u^-1 = T_(u a)
```

a `u` je z té konjugační akce plně čitelné. Zase totéž pravidlo: záleží na tom,
co držíš pevně.

## 8. Falzifikátory jako kontrolní tvrzení

Každý fixuje nosič, formu a zachovávanou strukturu. Bez nich se předpoklady mezi
tvrzeními posouvají a test nic netestuje.

```text
F1  NOSIČ K = Q(j), báze (1,j,j^2,j^3); FORMA h = (1/5)Tr(x ybar);
    ADJUNGOVÁNÍ M -> H^-1 M^T H.
    Tvrzení: M_x^* = M_xbar a [M_x, M_x^*] = 0 pro každé x v K.
    Padne: jediné x v K s nenulovým komutátorem při TOMTO adjungování.
    Nepadne jinou formou; při eukleidovské Gram = I je nenormálnost doložená
    (oddíl 4) a je součástí tvrzení, ne jeho vyvrácením.

F2  NOSIČ a FORMA jako F1; ZACHOVÁVANÁ STRUKTURA racionalita.
    Tvrzení: kladný polární faktor M_J neleží v End_Q(K).
    Padne: racionální kladně definitní B~ s B~^2 = M_J M_J^* a [B~, M_J] = 0.

F3  NOSIČ registrovaný kruhový kvocient I = (1+delta)^-1 O_K s P, S.
    Tvrzení: Z<P,S> = rho_I(O_K x| C_4), po tenzorování Q je to End_Q(K).
    Padne: prvek Z<P,S> mimo rho_I(O_K x| C_4), prvek rho_I(O_K x| C_4) mimo
    Z<P,S>, selhání gamma_3 = P^-4 S, nebo Z[delta] != O_K.

F4  NOSIČ O_K jako Z-modul; ZACHOVÁVANÁ STRUKTURA celočíselnost.
    Tvrzení: index [End_Z(O_K) : O_K x| C_4] je 5^6 a souřadnicová projekce E
    má v křížové bázi jmenovatele právě 5.
    Padne: jiný index, jiná množina jmenovatelů, nebo E uvnitř.

F5  NOSIČ l^2(O_K); ZACHOVÁVANÁ STRUKTURA translace {T_a}.
    Tvrzení: samotná unitární třída V_u jednotky nekonečného řádu nerozlišuje,
    dvojice (V_u, {T_a}) je rozlišuje skrze V_u T_a V_u^-1 = T_(u a).
    Padne: unitární invariant samotného V_u rozlišující dvě takové jednotky,
    nebo dvě různé jednotky se shodnou konjugační akcí na všech T_a.

F6  NOSIČ zmrazený chirální ribbon lift z P-J-FIBONACCI-BRAID-1.
    Tvrzení: při zmrazeném liftu je delta = 1 - J determinantový charakter
    a [2]_delta = phi.
    Padne: stejně přípustný zmrazený lift v registrované třídě, jehož
    determinantový charakter není delta ani delta^-1.
    NENÍ to test rovnice q^2 - phi q + 1 = 0: ta má právě dvojici {q, q^-1}
    a nemůže vystřelit nikdy.
```

## 9. Co bylo staženo, a co zůstává hypotézou

Stažené jako F v průběhu dvou kol oponentury: „Z[J] je c-strana a sloveso je
c-číslo"; „kruhový kvocient je abelovský" bez rozlišení determinantového kanálu;
připsání obecného zákazu dekodéru sondě `P-J-FIBONACCI-BRAID-1`, jejíž
registrovaný scope surové `M_J` výslovně vylučuje; „jeden operátor nestačí
k interferenci"; záměna samoadjungovanosti za unitaritu; MASA jako c-vrstva;
normálnost bez určeného adjungování; a falzifikátor postavený na Jonesově
mezeře, jejíž důkaz kladnost předpokládá, takže ji nemůže dodat.

Zůstává hypotézou, a tato poznámka na to nesahá: ztotožnění zkříženého součinu
s úplnou fyzikální q-vrstvou; příprava, aparát a zákon uskutečněných výsledků;
a jakýkoli lift z L1 výš. Registrované řádky samy říkají, že žádná Bornova škála
ani interpretace brány se netvrdí, a `S` transportuje vlastní přímky, není to
Hadamardovská superpozice.

## Příloha: seznam kontrol

```text
 1  M_J není skalární matice                                            PASS
 2  eukleidovská forma: M_J není normální, vstup 11 je 3 proti 2        PASS
 3  h = (1/5)Tr(x ybar): adjungovaný M_J je M_Jbar, det H = 1/5         PASS
 4  h-normálnost: [M_J, M_J^*] = 0                                      PASS
 5  M_J M_J^* = M_(2-phi) = M_(2 + j^2 + j^3)                           PASS
 6  (3I - M_phi)^2 = 5(2I - M_phi), B^2 = M_J M_J^*                     PASS
 7  gamma_3 má řád 4 a nekomutuje s M_J                                 PASS
 8  gamma M_x gamma^-1 = M_gamma(x)                                     PASS
 9  [End_Z(O_K) : O_K x| C_4] = 5^6 = 15625                             PASS
10  projekce E leží mimo, jmenovatelé právě {1, 5}                      PASS
11  delta = 1 - J = -j^2, delta + delta^-1 = phi                        PASS
12  Tr(delta^n) = (4,1,-1,1,-1,-4,-1,1,-1,1)                            PASS
```

Skript je `notes/NOTE-DIRAC-Q-A-ZKRIZENY-SOUCIN-2026-09-05.check.py`. Standardní
knihovna, exaktní aritmetika. Není to pinovaný verifikátor: pin před prvním
spuštěním nebyl, takže shoda dvou architektur je tady auditní vstup, ne
protokolární brána. Pro povýšení čehokoli odtud by musela vzniknout řádná sonda
s prereg, pinem a veřejným během.
