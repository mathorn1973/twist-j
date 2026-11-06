# NOTE: šipka času sedí v modulu, ne ve fázi

```text
status      NON-CANONICAL. Poznámka. Žádný kandidát, žádná sonda, žádný pohyb
            registru, žádná změna statusu.
date        2026-10-23
basis       Public Canon v104, main e6240e2689bb22aab5f02bad90b75d3692bb96d9,
            tag canon-v104, content commit
            4a50e527d20018839f006ed312454b710e6486b4, canon/SHA256SUMS 5 z 5 OK
origin      vlastníkova otázka: proč je vratnost důležitá a není šipka času
            její opak; vlastník označil čtení „šipka je v modulu“ za důležité
            a zadal je domyslet
predecessor notes/C-J-U-D-ARROW-LOCALITY-N (issue #1288, nesloučená větev):
            jeho U1, U2, R2 a odmítnutá tvrzení 1 a 5 se tu citují, nic z nich
            se znovu nezískává ani nemění
label       [T] na aritmetice v Z[zeta_5] (ověřeno exaktně, jedna noha),
            [T] a [C] na registrovaných řádcích, na které se odkazuje,
            [H] na čtení v §5 s falzifikátory v §6, [O] na druhém místě
platform    jedna noha, x86_64, Linux, Python 3 standardní knihovna, exaktní
            celočíselná aritmetika, žádný float. Žádná dvouarchitekturní brána.
verifier    check_arrow_in_modulus.py
            sha256 c84092f536f94016b02b7e7084ce8f21bd94322a4d4f75ad37968bc559b47fa5
stdout      check_arrow_in_modulus.stdout
            sha256 9f8c6010c06d484e149d92e3b68c0b600bbad4c4efb1f59ceca0420ba8ea75b4
language    český text; anglické shrnutí níže; kód a stdout anglicky
```

## Summary (EN)

```text
[T]  O_K^x = mu_10 x <phi> (J-UNIT-STRIP-NORMAL-FORM, J-HARMONIC-SEAM). Only
     the free coordinate of a unit is ordered: J^n = j^n phi^(-n) carries n in
     the modulus and only n mod 5 in the phase. An arrow can sit in the
     modulus and nowhere else inside a unit.
[T]  J^-1 = -j - j^2 = phi conj(j) = phi^2 conj(J) = zeta_10^-1 sigma_2(J)
     = zeta_10^-3 sigma_3(J). Inversion up to torsion holds exactly for the
     two place-swapping Galois elements and fails for 1 and sigma_4 (B2).
     Tr M_J = 3, Tr M_J^-1 = 2, so no linear conjugacy at all (#1288, U2).
[T]  Entropy is symmetric, h(T_J) = h(T_J^-1) = 2 log phi (J-TORAL-ENTROPY).
     The step moves the place ratio A/B by phi^-4 (J-UNIT-STRIP-NORMAL-FORM):
     the registered monotone orbit coordinate.
[T]  Closed world: ord_m(J) = lcm(5, ord_m phi) (J-RESIDUE-PERIOD); the
     kernel step is a permutation of every finite residue ring.
[H]  Reading: the direction is fixed by the marked J; what the direction
     means in the modulus (contract or expand) is fixed by the archimedean
     place, since the place swap carries J to J^-1 up to a tenth of a turn.
     Inside Z[zeta_5]/(m) there is no place, no modulus and no arrow; the
     arrow in the modulus is a property of the reading, not of the plenum.
     Falsifiers F1 to F3 in section 6.
```

## 0. Co si mainstream od vratnosti kupuje, a co z toho twist bere

Vratnost slévá dvě různé věci. První: nic se neztrácí, dva stavy nikdy
nesplynou, každý stav má právě jednoho předchůdce (obsah Liouvilleovy věty
a unitarity). Druhá: zákon vypadá stejně dopředu i dozadu, T-symetrie. Druhá
je navíc a právě ona vyrábí Loschmidtův paradox: symetrický zákon, nesymetrický
svět, šipka se musí nacpat do počátečních podmínek.

Twist bere první a druhou ne. N(J) = 1, det M_J = 1, bijekce na Z^4 (J-UNIT
[T]). Inverzní prvek existuje, ale nic v plenu ho neaplikuje (čítač jen
přičítá) a žádná symetrie ho ze zákona vpřed nedělá (§2). „Vratnost neplatí“
je tedy přesné jako věta o symetrii a nepřesné jako věta o bijekci. Obě půlky
stojí vedle sebe.

## 1. Kde šipka vůbec může sedět [T]

Dirichlet: jednotky Z[zeta_5] jsou mu_10 x <phi>, hodnost 1, a J generuje
touž volnou část (J phi = j, J-GOLDEN-BRIDGE [T]; struktura grupy jednotek je
v J-HARMONIC-SEAM [T] a J-UNIT-STRIP-NORMAL-FORM [T]). Torze je cyklická,
volná část je Z. Jen Z je uspořádané.

$$
J^n = j^{\,n}\,\varphi^{-n}
$$

Fáze J^n je n mod 5, modul J^n je phi^{-n}. Fáze zná jen zbytek po pěti,
modul zná n celé. Šipka může být jen v modulu, protože nic jiného v jednotce
není uspořádané. To není čtení, to je struktura grupy jednotek.

## 2. Co je „zpět“ [T, ověřeno A1 až B8]

$$
J^{-1} \;=\; -j - j^2 \;=\; \varphi\,\bar j \;=\; \varphi^2\,\bar J
\;=\; \zeta_{10}^{-1}\,\sigma_2(J) \;=\; \zeta_{10}^{-3}\,\sigma_3(J)
$$

Tři čtení téhož prvku:

```text
sdružení + phi^2   fázi otočí automorfismus zadarmo; modul phi^2 nikdo neodnese
žádné sigma_a(J) = J^-1   a silněji Tr M_J = 3, Tr M_J^-1 = 2: žádná lineární
                   symetrie mřížky nepřevede krok na inverzi (#1288, U2, B8)
prohození míst     sigma_2 a sigma_3 dávají J^-1 až na desetinu otáčky;
                   1 a sigma_4 ne. Inverze až na torzi <=> prohození
                   archimédovských míst (B2). To je to, co tahle poznámka
                   přidává k #1288.
```

Zpět je tedy jiný prvek a směr je dán už označením J jako kroku, ne vnějším
vnořením (#1288, odmítnuté tvrzení 1). Co ale směr znamená v modulu, je dáno
místem: týž označený krok J má u sigma_1 modul 1/phi a u sigma_2 modul phi,
a prohození míst ho převede na J^{-1} až na torzi. Šipka je v axiomu; její
modulové znaménko (zkracuje, nebo prodlužuje) je v místě. Volba místa je
znaménko sqrt5, tedy volba, že phi je ta větší z dvojice phi, 1 - phi.

Jediný prvek řádu 2 v Galoisově grupě, sigma_4 (Z2-PLACES-SPLIT [T]),
J neinvertuje ani až na torzi (B5, B7). Involutivní obrácení času proto
nemůže být symetrie okruhu. Musí mít kus mimo okruh: buď modul phi^{+-2},
nebo dekodér. Veřejný slovník čte T z obrácení Thue-Morse, ne z Galoise
(TWO-PLACE-PHYSICS [D]); tohle je aritmetický důvod, proč jinak nemůže.

## 3. Entropie šipku nenese [T]

h(T_J) = h(T_J^{-1}) = 2 log phi, Lyapunov +-log phi symetricky
(J-TORAL-ENTROPY [T], J-MAHLER-MEASURE [T], probes/P-TWOLOGPHI-INVARIANTS-1).
Součin modulů přes archimédovská místa je 1 (N(J) = 1, součinový vzorec).
Krok vpřed nic netvoří: přenese měřítko phi z jednoho místa na druhé. Vzad ho
přenese zpátky. Množství je symetrické, směr přenosu je šipka.

Registrovaná podoba téhož: pro A = |sigma_1(alpha)|^2, B = |sigma_2(alpha)|^2
posílá násobení J poměr A/B na phi^{-4} A/B a exponent n orbity se čte
z tohoto poměru exaktně v Q(sqrt5) (J-UNIT-STRIP-NORMAL-FORM [T]). Poměr
míst je jediná souřadnice orbity, která jde monotónně. To je šipková
souřadnice, už v registru.

Otázka, kterou tohle čtení otevírá [O]: co je fyzikálně druhé místo, tedy kam
odchází to, co se u nás zkrátí. AXIOM-PROJECTION-DICTIONARY [D] čte modul
jako gravitaci a měřítko a o místě neříká nic; žádný veřejný řádek nečte obě
místa fyzikálně. Tady se to nerozhoduje.

## 4. Uzavřený svět [T a C, registrováno, nezávisle přepočteno C1]

Modulo racionální m má J konečný řád, ord_m(J) = lcm(5, ord_m phi)
(J-RESIDUE-PERIOD [T]; na Z/5^k je perioda 4 x 5^k, TIME-QUANTUM-TOWER [C]):
15, 40, 30, 20, 80, 10, 140 pro m = 2, 3, 4, 5, 7, 11, 13. V uzavřeném
celočíselném plenu je krok jádra permutace a je periodický. Ve stavu žádná
šipka není, všechno se přesně vrátí.

Co ve stavu zbývá: nebijektivní část složeného stroje (rekurentní jádro
6250 z 15625 hlav, 313 komponent, U-NATIVE-INVARIANT-AND-NOWRITE [T];
blokové mapy dvě ku jedné na jádře, ENTROPY-BLOCK-HALVING [C]; zpětný strom
šířky dvě, ENTROPY-UNIQUE-PAST [C]) a čítač, který není stavová proměnná
a v nativním nosiči začíná v nule bez oboustranného rozšíření (#1288, R2).
To je jediné místo, kde by šipka ve stavu mohla sedět. Že tam sedí, z toho
neplyne: slučování hlav samo o sobě disipaci nedokazuje (#1288, odmítnuté
tvrzení 5).

Ani velikost celých čísel šipku nedává (D1): |J^n|_inf = F_{n+1},
|J^{-n}|_inf = F_n, obě strany utíkají rychlostí phi.

## 5. Kde šipka v modulu doopravdy je, v tomhle čtení [H]

V setkání celých čísel s reálnými. V konečném okruhu Z[zeta_5]/(m) není žádné
archimédovské místo, tudíž ani modul, tudíž ani šipka v modulu. Místo vznikne
až vnořením do C, a vnoření je čtení (L6). Směr kroku je v axiomu (§2);
šipka v modulu je vlastnost čtení, ne plena. Souzní to s veřejným čtením, že
čas je čítač a jeho identifikace s fyzikálním časem je slovník, ne
konstrukce (CANON.md A0 Reading, TIME-CUT-READING [D]); tady je vidět proč:
bez čtení není modul.

## 6. Falzifikátory čtení

```text
F1  pozorovatelná veličina programu, která nese šipku a je invariantní vůči
    prohození míst (racionální, nebo symetrická funkce obou míst). Entropie,
    regulátor, stopa, norma jsou slepé, jak čtení žádá. Re Li_2 rozlišuje:
    pi^2/100 u a in {1,4} proti 9 pi^2/100 u a in {2,3}, poměr 9
    (WALL-LI2-RUNG [T], reálné části). Polylogaritmický most je tedy jediná
    registrovaná veličina, která místo, a v tomhle čtení šipku v modulu,
    vidí. Jedna šipková veličina symetrická v místech čtení shodí.
F2  vidlička T^2. Kdyby fyzikální T bylo sigma_2 až na torzi, pak
    T^2 = sigma_4, tedy involuce v zeta_5, ze které TWO-PLACE-PHYSICS [D]
    čte CP, a CPT by bylo T^-1 != 1. Standardní QM má T^2 = +-1 a CPT = 1.
    Buď T není sigma_2 (a je v Thue-Morse, jak slovník říká), nebo je
    špatně čtení CP ze zeta_5 involuce. Tady se nerozhoduje; je to
    vlastníkova vidlička.
F3  kdyby se našel automorfismus Z[zeta_5] posílající J na J^-1, padá §2
    celé. Galoisova grupa je vyčerpána (B1), okruh je komutativní, jiný
    není; stopa to uzavírá i pro GL_4(Q) (B8).
```

## 7. Co tato poznámka nedělá

Nepohybuje registrem, nemění žádný status, nezakládá kandidáta a nezasahuje
do notes/C-J-U-D-ARROW-LOCALITY-N. Věty §1 až §4 jsou aritmetika
a registrované řádky; §5 je čtení s falzifikátory v §6. Pokud by z toho měl
být kandidát, půjde veřejným protokolem sond podle POLICY.md, s vlastním
claimem a vlastní preregistrací.
