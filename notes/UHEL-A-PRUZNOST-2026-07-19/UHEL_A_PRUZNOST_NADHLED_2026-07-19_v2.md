# Úhel, pružnost a přenos: kde se potkávají dvě čtení J

**Status:** NON-CANONICAL pracovní nadhled, opravená verze 2. Tento text
nemění Canon, nepovyšuje žádný výrok a není důkazem fyzikálního slovníku.
Autoritou je Public Canon v10, content commit
`817275c4ef460d2d500a947db34c975baa651c40`. Při tomto auditu měl veřejný
`main` hlavu `633b6f220fddd5882b73b156ca12161fc6d97938`. Veřejný probe
`P-RAMIFIED-TM-LIFT-1` je
sloučený do `main`, ale jeho případný zápis do registru a Canonu vyžaduje
samostatný fold.

## 0. Falzifikace a hranice tvrzení

Matematické jádro padá na jediném přesném protipříkladu k některé z níže
uvedených identit. Přiložený svědek používá jen celá čísla a standardní
knihovnu. Při kterémkoli `FAIL` končí nenulovým návratovým kódem.

Fyzikální čtení je jiná vrstva. Není zde dokázáno:

- že polární rozklad a rozklad sčítačky jsou izomorfní rozklady;
- že XOR je elektromagnetismus nebo že přenos je gravitace;
- že existují právě dvě základní síly;
- že fyzikální přenos, fáze, šipka času nebo princip ekvivalence jsou
  vynuceny aritmetikou L1;
- nulová hmotnost fotonu, hodnota `r_T` ani polarizační čtení.

Přesný výsledek je užší: archimédovské a ramifikované čtení mají společný
zdroj `J`. Ramifikované čtení se navíc přesně stýká s binární sčítačkou v
jedinečném celočíselném koeficientu `2`. To je aritmetická souhlasnost, ne
hotové fyzikální ztotožnění.

## 1. Polární rozklad axiomu [T]

V hlavním komplexním vnoření platí

```text
J phi = j,
J = phi^-1 j,
|J|^2 = 2 - phi = phi^-2,
arg(J) = 2 pi / 5,
Log(J) = -ln(phi) + i 2 pi / 5,
J^5 = phi^-5.
```

Každý krok tedy v hlavním vnoření otočí fázi o `2 pi / 5` a zmenší modul
faktorem `phi^-1`. Logaritmický krok měřítka je `-ln(phi)`, nikoli
`+ln(phi)`. V reciprokých Galoisových vnořeních se objeví roztažení
faktorem `phi`; úplná čtveřice modulů je

```text
(phi^-1, phi, phi, phi^-1),
```

a jejich součin je přesně `N(J) = 1`.

To je algebraická věta. Algebraická norma jedna znamená zachování součinu
Galoisových měřítek. Sama o sobě neznamená zachování fyzikální energie ani
definici elastického média. Hodnota `2 ln(phi)` je topologická entropie
hyperbolického nosiče; její čtení jako energie je další slovníkový krok.

## 2. Ramifikované čtení [veřejný probe, navržený status T]

Položme `lambda = 1 - j`. Redukce modulo jediný prvoideál nad pěti dává

```text
J_lambda = J mod lambda = 2 in F_5^x,
2^2 = -1,
2^4 = 1.
```

To není archimédovský úhel `2 pi / 5`. Jde o jiné místo téhož algebraického
prvku. Archimédovská fáze má řád pět, ramifikovaný obraz `2` má řád čtyři.

Probe `P-RAMIFIED-TM-LIFT-1` dokazuje na vrstvě L1 přesný řetězec

```text
J
  -> J_lambda = 2 in F_5^x
  -> four phases 1, 2, -1, -2
  -> sign quotient F_5^x/{+-1} ~= F_2
  -> Thue-Morse bit.
```

Pro `s_2(n)` rovné součtu binárních cifer a `t_n = s_2(n) mod 2` je

```text
Theta_n = 2^s_2(n) mod 5,
q(Theta_n) = t_n,
Theta_n^2 = (-1)^t_n.
```

Chronologický krok není stálá čtvrtotáčka. Pro
`c_n = nu_2(n + 1)`, počet koncových jedniček v binárním zápisu `n`, platí

```text
s_2(n + 1) = s_2(n) + 1 - c_n,
Theta_(n + 1) = Theta_n 2^(1-c_n) mod 5,
t_(n + 1) = t_n XOR 1 XOR (c_n mod 2).
```

To je přesný přenosový kokyklus. Čtyřfáze patří cifernému přechodu, ne
prostému časovému pořadí `n -> n + 1`.

## 3. Sčítačka [T pro identitu, konečný audit ve svědku]

Pro všechna nezáporná celá čísla platí

```text
x + y = (x XOR y) + 2 (x AND y).
```

XOR obsahuje bity přítomné právě v jednom vstupu. AND obsahuje bity
přítomné v obou vstupech a násobení dvěma je posune o jeden binární řád.
To je úplný důkaz identity po jednotlivých řádech. Koeficient `2` je
jedinečný, protože už případ `x = y = 1` nutí `2 = mu`.

V pětkové soustavě analogicky platí

```text
a + b = digit_sum_mod_5 + 5 carry.
```

Zde je přenos mezi pětkovými řády násoben pěti. Ramifikace říká, že pět je
ve `Z[j]` čtvrtou mocninou uniformizéru až na jednotku. Přiložený svědek
kontroluje normu `N(1-j)=5`, ale netvrdí fyzikální význam této filtrace.

## 4. Přesný svár obou řečí

Správné společné schéma je

```text
archimédovské místo:  J -> (phi^-1, 2 pi/5)
ramifikované místo:   J -> 2 in F_5^x -> C4 -> C2
binární sčítačka:     + -> XOR + 2 AND
```

První dvě řádky jsou dvě přesná čtení téhož `J`. Druhá a třetí řádka se
stýkají v jedinečném násobiteli `2` a v přenosovém kokyklu. Dosud ale není
sestrojena komponentová mapa

```text
(modul, úhel) <-> (carry, XOR).
```

Proto je nepřípustná věta „nejde o analogii, ale o totožný rozklad“.
Přípustný silný tvar je:

> Úhel a modul jsou dvě archimédovská čtení `J`. Čtyřfáze, Thue-Morse a
> přenosový kokyklus jsou jeho ramifikované čtení přes `J_lambda = 2`.
> Společný původ je věta; jejich fyzikální ztotožnění je slovník.

## 5. Fyzikální slovník [D, bez tvrzení jedinečnosti]

Public Canon čte modul jako gravitaci a měřítko, argument jako
elektromagnetismus a fázi. Přesný konečný Weylův komutátor

```text
Z X Z^-1 X^-1 = j I
```

má řád pět. Jeho čtení jako křivosti síly a následné přiřazení dvou
projekcí patří do `FORCE-AS-CURVATURE [D]` a
`AXIOM-PROJECTION-DICTIONARY [D]`.

Z polárního rozkladu lze proto poctivě mluvit o dvou abelovských kanálech
jednoho komplexního generátoru. Nelze z něj odvodit, že fyzika má právě dvě
síly nebo že neabelovský kanál nemůže existovat. Canon sám nese oddělené
neabelovské barevné dveře.

Úhlový kanál je kompaktní a konjugace obrací orientaci, zatímco modul
zachová. To podpírá dvouznaménkové čtení náboje a jednoznaménkové čtení
hmoty [D]. Kvantování náboje, univerzální přitažlivost a princip
ekvivalence však nejsou samotným polárním rozkladem dokázány.

Stejně tak pravidlo přenosu je stejné na každém ciferném řádu, ale vznik
přenosu závisí na obsahu cifer. Přesnější formulace tedy je „přenos používá
univerzální žebřík“, nikoli „přenos je slepý k obsahu“.

## 6. Historická kotva [komentář]

Weylova konstrukce z roku 1918 použila lokální změnu měřítka a pokusila se
z ní číst elektromagnetismus. Einsteinova námitka proti historii závislým
měřítkům hodin a spektrálních čar tuto fyzikální interpretaci vyřadila.
Weyl roku 1929 přenesl kalibrační princip na komplexní fázi kvantové vlnové
funkce, čímž vznikl moderní `U(1)` tvar elektromagnetismu.

TWIST-J drží obě archimédovské složky `Log(J)`, ale jejich fyzikální jména
zůstávají slovníkem [D], nikoli důsledkem samotné algebraické identity.

## 7. Stav důkazů a svědka

- Public Canon v10: `J-PROJECTIONS`, `J-MODULUS-CHORD`, `J-GOLDEN-BRIDGE`,
  `J-UNIT`, `LOG-AXES-INDEPENDENCE` [T].
- Public Canon v10: `AXIOM-PROJECTION-DICTIONARY`, `FORCE-AS-CURVATURE`,
  `FORCE-POLAR-SIGN`, `COULOMB-PROJECTION`, `MAXWELL-CLOSED` [D].
- `P-RAMIFIED-TM-LIFT-1`: veřejně sloučený, dvouarchitekturně reprodukovaný
  probe s navrženým theoremovým výsledkem na L1; Canon fold je samostatný
  krok.
- `verify_dve_projekce_v2.py`: neformální souhrnný audit přesných identit.
  Nedává nový status a nenahrazuje veřejné reprodukční balíky.

Neformální dvouarchitekturní audit verze 2:

```text
platform 1        Linux x86_64, Python 3.12.13
platform 2        Darwin arm64, Python 3.9.6
result             18/18 ALL PASS on both platforms
exit code          0 on both platforms
negative test      17/18 SOME FAIL, exit 1 on both platforms
stderr             empty on passing runs
stdout equality    byte-identical
verifier bytes     6980
stdout bytes       779
stdout lines       19
verifier sha256    861eefca9a91da114021fe5ddb99f81e04cf759f20fad55617c6463c513bb9bb
stdout sha256      dbef0696a60bb2c9d06bdbca0a715dafd3c9e42dedb227e9356bb0109408f9f4
```

Jde o neformální audit bez veřejné preregistrace, ne o nový důkazní status.
Piny původního svědka `22dc1e79...` a jeho výstupu `8278cfec...` zůstávají
historickým záznamem verze 1 a nepřepisují se.
