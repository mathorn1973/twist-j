# V2 jedna volba: odometr, kvadratické čtení a čtyřfázový můstek

**Status:** NON-CANONICAL pracovní nadhled. Tento text nemění Canon,
nepovyšuje žádný výrok, neotevírá formální probe a není preregistrací.
Autoritou je Public Canon v32, content commit
`b007a9df39e672a7ad30afc6e6c88e13551ab280`, tag `canon-v32`. Při tomto
auditu měl veřejný `main` hlavu
`f8c4cc64ba4fc21723fc3e715b5a40036ef7b404`.

## 0. Zadání a mapování tabule

Vstupní tabule a její řádky v registru:

```text
VYNUCENO
[T] J^n: pětiperiodická fáze, neperiodická škála      J-PROJECTIONS
[T] J je jednotka; čistý J-krok je grupová orbita     J-UNIT, J-STEP
[T] čtyřfázový ramifikovaný lift, carry koeficient 2  RAMIFIED-TM-LIFT
[T] čtyřfáze není funkcí checkpointu                  CARRY-J-CHECKPOINT
[T] žádný konečný autonomní nosič nereprodukuje
    checkpointovou řadu                               viz oddíl 3 níže

ZVOLENO
[D] nekonečný nosič je 2-adický odometr               ODOMETER-INTERNALIZED
[D] místo v_2 čteno jako quadratic read side          TWO-PLACE-PHYSICS

OTEVŘENO
[O] přesný L1/L5-to-L6 bridge                         ENTROPY-LAYER-BRIDGE,
                                                      TM-SYM2-PHYSICAL-MEASURE
[H] oba [D] řádky jsou jedna místní volba v_2         zde oddíl 5

PŘEDCHOZÍ VÝSLEDEK
[F] frozen UNIQUE selektor neexistuje                 TM-SYM2-MEASURE
[T] orbitová klasifikace 48 = 4 x 12                  TM-SYM2-PROJECTIVE-FOURFOLD
```

Cílem poznámky je posunout oba otevřené řádky: zaostřit hypotézu jedné
místní volby do falzifikovatelného tvaru a dodat pro entropy-layer bridge
přesnou nutnou podmínku plus zúžený prostor kandidátů. Nic zde není
uzávěr; obě položky zůstávají otevřené.

## 1. Falzifikace a hranice tvrzení

Matematické jádro padá na jediném přesném protipříkladu k identitám
v oddílech 2 až 4. Přiložený svědek `verify_v2_jedna_volba.py` používá
jen celá čísla, přesné zlomky a standardní knihovnu; při kterémkoli
`FAIL` končí nenulovým návratovým kódem. Jde o neformální audit bez
veřejné preregistrace, ne o nový důkazní status.

Není zde tvrzeno:

- že `ENTROPY-LAYER-BRIDGE` je uzavřen kterýmkoli směrem;
- že hypotéza jedné místní volby je dokázána;
- že čtyřfázová míra (oddíl 4) konstruuje prvek třídy `A_A`;
- žádné fyzikální čtení nad rámec registrovaných [D] řádků;
- žádná identifikace číselné shody 2/15 (oddíl 8) s mapou nebo faktorem.

## 2. Lemma A: čtyřfáze je přesný odečet v_2 modulo 4

`RAMIFIED-TM-LIFT [T]` dává `Theta_n = J_lambda^s_2(n)` s
`J_lambda = J mod (1 - zeta_5) = 2` a chronologický krok

```text
Theta_(n+1) = Theta_n . 2^(1 - c_n) mod 5,    c_n = v_2(n + 1).
```

**Lemma A.** Zobrazení `c mod 4 -> 2^(1-c) mod 5` je bijekce
`Z/4 -> F_5^x` (tabulka `0->2, 1->1, 2->3, 3->4`). Přírůstek čtyřfáze
tedy závisí jen na `v_2(n+1) mod 4` a zpětně jej přesně určuje.

*Důkaz.* `ord(2 mod 5) = 4`, takže `2^(1-c)` probíhá při `c = 0..3`
čtyři různé hodnoty a závisí jen na `c mod 4`. Bijekce se invertuje
diskrétním logaritmem při základu 2. QED.

Důsledek pro `CARRY-J-CHECKPOINT [T]`: informace, která podle tohoto
theorému nemůže být funkcí checkpointu, je přesně kvantifikována — je to
proud `v_2(n+1) mod 4`, tj. čistě lokální data hodin v místě 2,
překódovaná ramifikovaným obrazem `J_lambda = 2`. Chybějící obsah
čtyřfáze nad rámec parity `theta` je druhý bit `s_2(n) mod 4`.

## 3. Lemma B: neperiodicita a konečné nosiče

**Lemma B.** Proud přírůstků `iota_n = 2^(1 - v_2(n+1)) mod 5` není
eventuálně periodický.

*Důkaz.* Nechť `iota_(n+p) = iota_n` pro všechna `n >= N` a nějaké
`p >= 1`; polož `a = v_2(p)`. Pro každé `m > a` s `2^m > N` vezmi
`n + 1 = 2^m`: pak `v_2(n+1) = m` a `v_2(n+1+p) = v_2(2^m + p) = a`.
Rovnost přírůstků vynucuje přes Lemma A `m ≡ a (mod 4)` pro všechna
velká `m`, spor. QED.

Výstup každého konečného autonomního stroje bez vstupu je eventuálně
periodický. Lemma B je tedy přesný aritmetický obsah řádku tabule
„žádný konečný autonomní nosič nereprodukuje checkpointovou řadu" na
úrovni fázového proudu: nosič musí nést neomezenou 2-adickou hloubku.
Minimální kompaktní zúplnění nesoucí `+1` se všemi `v_2`-daty je právě
projektivní limita `Z_2 = lim Z/2^k`, tedy volba
`ODOMETER-INTERNALIZED [D]`.

## 4. Přesný zákon míry na čtyřfázovém kanálu

**Tvrzení (hustota, vrstva L1/L5).** Pro `j = 0..3` má množina
`{n in N_0 : v_2(n+1) ≡ j mod 4}` přirozenou hustotu `2^(3-j)/15`;
na dyadickém okně `[0, 2^M)` jsou počty přesně

```text
count_j(M) = sum_(c<M, c≡j mod 4) 2^(M-1-c) + [M ≡ j mod 4],
|count_j(M)/2^M - 2^(3-j)/15| <= 2^(1-M).
```

**Tvrzení (Haar, vrstva L6).** Na `Z_2` s normalizovanou Haarovou
mírou je `Haar{x : v_2(x+1) = c} = 2^-(c+1)` (cylindr
`x ≡ 2^c - 1 mod 2^(c+1)`), `v_2(x+1)` je definováno mimo nulovou
množinu `{-1}`, a pushforward čtyřfázového odečtu je

```text
mass(j) = sum_(c≡j) 2^-(c+1) = 2^-(j+1) . 16/15 = 2^(3-j)/15,
(mass(0..3)) = (8/15, 4/15, 2/15, 1/15),  součet 1.
```

Obě čtení dávají tutéž čtveřici: Cesàrovo čtení na dopředné orbitě
(registrovaný nosič `N_0`) souhlasí s Haarovým čtením na zúplnění. To
je malý přesný L1-to-L6 přechod na straně hodin — netýká se ještě
checkpointové složky `F_5^6`, a proto neuzavírá `ENTROPY-LAYER-BRIDGE`.

Jmenovatel má algebraický původ: nejmenší `f` s `5 | 2^f - 1` je
`f = 4`, prvočíslo 2 je v `Q(zeta_5)` inertní se zbytkovým tělesem
`F_16` a `15 = 2^4 - 1 = |F_16^x|`. Řád čtyřfáze, zbytkový stupeň
místa 2 nad `Q(zeta_5)` a jmenovatel mas jsou jedno číslo 4, resp.
jeho `2^4 - 1`.

## 5. Zaostřená hypotéza jedné místní volby

**V2-JEDNA-VOLBA [H, jen poznámka].** Existuje jeden typovaný lokální
údaj v prvočísle 2,

```text
D_2 = (zúplnění hodin v místě v_2, redukce J -> J_lambda = 2
       generující obraz řádu 4 = f(2 | Q(zeta_5))),
```

takový, že `ODOMETER-INTERNALIZED [D]` i klauzule „v_2 jako read side"
v `TWO-PLACE-PHYSICS [D]` jsou dvě registrovaná čtení téhož `D_2`, a
žádná další nezávislá volba v obou řádcích není obsažena.

Doložené styčné body (vše přesné, svědek G01-G08):

1. přírůstková formule `Theta_(n+1) = Theta_n . J_lambda^(1 - v_2(n+1))`
   používá prvek 2 v obou rolích najednou: jako hodnotu (ramifikovaný
   obraz `J`) i jako místo (valuace `v_2` v exponentu);
2. carry koeficient binární sčítačky je totéž 2 (`RAMIFIED-TM-LIFT`);
3. řád čtyřfáze 4 = zbytkový stupeň místa 2 v `Q(zeta_5)`;
4. masy `(8,4,2,1)/15` mají jmenovatel `2^4 - 1`;
5. na pětkové straně je `M_J^(5^k) = i_5 I` s `i_5 ≡ 2 mod 5` a
   periodou přesně `4 . 5^k` (`TIME-QUANTUM-TOWER [C]`, zde nezávisle
   auditováno pro `k = 1, 2`): tentýž faktor C4 = <2> ⊂ F_5^x.

Falzifikátor hypotézy: přesná registrovaná konstrukce, která obě volby
oddělí — nosič zúplněný v místě 2, jehož vynucené čtení není
kvadratická/Bornova noha; nebo odvození kvadratického čtení z jiného
místa než 2; nebo protipříklad k Lemmatu A. Pouhé pojmenování jiné
preference hypotézu nefalzifikuje.

## 6. Co z toho plyne pro ENTROPY-LAYER-BRIDGE [O]

`ENTROPY-CYLINDER-NOGO-CURSOR [T]` vylučuje každý čistě slovní
konečně-cylindrický systém na všech kurzorech a oknech `L = 4..32`
s přenosem do každé lambda-hloubky; `ENTROPY-COMPONENT-NOGO [C]`
vylučuje 900 zmrazených komponentových případů. Zbylý prostor pro
`P_5` jsou měřitelné mapy, které nejsou konečně-cylindrické.

Odečet `v_2` je kanonický příklad přesně této třídy: závisí na
neomezeně mnoha binárních cifrách, je definovaný mimo nulovou množinu,
měřitelný, s geometrickým chvostem — a přitom má přesnou aritmetiku
(oddíl 4). Posun této poznámky je proto dvojí:

1. **Nutná podmínka (přesná, odvozená).** Faktor mu na straně hodin je
   Haar na `Z_2`; pushforward čtyřfázového odečtu je vynucen jako
   `(8,4,2,1)/15`. Každý kandidát `P_5`, jehož konstrukce čte
   čtyřfázový kanál, musí být s touto marginálou kompatibilní; není co
   volit.
2. **Zúžený prostor kandidátů.** Hledat `P_5` jako šikmý součin přes
   `v_2`-věž (konečná hloubka odečtu roste, nikoli pevné okno), ne
   jako cylindr. Okno `W = [512, 2048) = [2^9, 2^11)` registrované
   v `Law_W` je samo dyadické, takže věžový odečet je s ním typově
   kompatibilní.

Styčný bod s pětkovou stranou už v evidenci je: zmrazená afinní tabulka
`P-ENTROPY-BRIDGE-4` (řádek `ENTROPY-AFFINE-COCYCLE [C]`) se opakuje
v blokové škále `k` s periodou čtyři a translační množina je funkcí
`2^k mod 5` (svědek G07); jediná netriviální multiplikativní část je
`a = -1` na úrovni `k = 0`. Tatáž perioda čtyři se objevuje v
`TIME-QUANTUM-TOWER` jako faktor `4` v periodě `4 . 5^k`. To je přesně
stopa C4 = <2> na straně `O_lambda`, zatím jen v pevné kalibraci.

## 7. Návrh dalšího kroku (jen náčrt, žádná preregistrace)

Případný `P-ENTROPY-BRIDGE-5` by měl tři brány:

```text
B5-G1  kalibračně nezávislá identifikace pentagonové věže s akcí
       násobení J na O/lambda^k (uzavření mezery vyznačené v
       ENTROPY-AFFINE-COCYCLE: „no gauge-independent identification");
       rozhodnutí: přesný izomorfismus věží, nebo přesná obstrukce.
B5-G2  typovaná nutná podmínka fázové marginály (8,4,2,1)/15 pro
       každý kandidát P_5 čtoucí čtyřfázový kanál; odvozená, ne
       předpokládaná.
B5-G3  konkrétní necylindrický kandidát: šikmý součin, v němž konečná
       v_2-hloubka hodin vybírá pentagonovou buňku checkpointové věže;
       test přesné ekvivariance a Law_W na dyadickém okně při
       konečných hloubkách.
```

Selhání jednoho kandidáta je podle registrovaného rozhodovacího pole
STOP, ne negativní uzávěr; `A_A = empty` vyžaduje úplnou větu.

## 8. Číselné pozorování, výslovně bez mapy

Třetí fázová masa `2/15` je číselně shodná s koeficientem u `P5`
v registrovaném `M_TM = (1/3) P1 + (2/15) P5`
(`TM-SYM2-PROJECTIVE-FOURFOLD [T]`); dále `8/15 = 1/3 + 1/5` a
`(1/3) + (2/15).5 = 1`. Jsou to přesné racionální identity čísel
(svědek G09), ale žádná mapa mezi čtyřfázovým kanálem a šesticí zlatých
přímek zde není sestrojena ani tvrzena. `TM-SYM2-PHYSICAL-MEASURE [O]`
navíc výslovně zakazuje uzávěr, který by `M_TM` předpokládal; toto
pozorování smí nanejvýš motivovat typ mostu, ne jeho hodnoty.

## 9. Stav svědka

```text
soubor              verify_v2_jedna_volba.py
brány               G01-G09, 9/9 ALL PASS
platform            Linux aarch64, CPython 3.11.15
exit / stderr       0 / prázdný
verifier sha256     86a8dab1a5a483cfca38d9a6fa0c8458512c0ac08912ea2394547aa6b1936117
verifier bytes      8235
stdout sha256       ff606917602eaad7d140622941562ff8fe7ce0a4b7add4480efcb01fe900b48f
stdout bytes/lines  1203 / 11
negativní test      zkažená tabulka v G02 dává 8/9 SOME FAIL, exit 1
```

Svědek čte zmrazenou veřejnou tabulku `EXPECTED_AFFINE` z
`probes/P-ENTROPY-BRIDGE-4/verify.py` jako statická data; žádný formální
probe se nespouští a žádný registr, frontier ani Canon se nemění.
