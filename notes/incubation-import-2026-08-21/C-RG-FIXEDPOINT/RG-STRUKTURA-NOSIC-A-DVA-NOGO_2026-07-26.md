# RG STRUKTURA: nosič je registrovaný, tok neexistuje

```text
Lane memo a odvození. ŽÁDNÁ AUTORITA. Nepreregistrováno, nespotřebováno,
nic neposouvá v registry. Není to kandidát: candidate-T vyžaduje prereg
PŘED výpočtem a ten neexistuje.
Autorita pin, ověřeno vlastním clonem v této session:
  Public Canon v23 ACTIVE, tag canon-v23,
  CONTENT_COMMIT 7830d852229ffc06c9d287d026c8ece290bf339b,
  CANON_SHA256 f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1,
  CANON_BYTES 116017, SHA256SUMS 5 z 5 OK,
  content commit je předek HEAD da3d9e53 (2026-07-26 19:09 +0200;
  commity po foldu jsou notes a predefinition, ne normativní fold).
Soukromá hlava twistj-jam: NEPOTVRZENA v této session [O].
Datum: 2026-07-26.
```

## 0. Falsifikace nejdřív

Otázka zněla: umíme odvodit RG strukturu, abychom to skutečně uměli tvrdit.

Odpověď má dvě části a obě jsou v rozporu s reconem.

**Za prvé: nosič nechybí.** Recon uzavírá větou "RG scale carrier chybí" a
registruje `O-RG-SCALE-CARRIER`. To je nepravda. Nosič škály je ve veřejném
Canonu v23 už teď, na štítku [C], a Canon pro něj používá doslova slovo
*renormalized*.

**Za druhé, a to je hlavní výsledek: tok na tom nosiči neexistuje.** Není to
otevřená obligace. Je to uzavřeno záporně, exaktně, na 6250 stavech: graf obou
větvových map nemá ani jednu mezikomponentní hranu, takže každá nerostoucí
funkce je na jádře invariantem a `Delta C = 0` identicky. c-teorémová linie
tedy nekončí jako "chybí nám ještě pět objektů", ale jako pojmenovaný
negativní výsledek. Podrobně v sekci 8.

## 1. Currency, a moje vlastní selhání hlášené první

```text
veřejná hlava v23     CONFIRMED [C]   vlastní clone, 5 z 5 SHA256SUMS OK
projektová instrukce v10   STALE
recon kotva v20            STALE
soukromá hlava             UNCONFIRMED [O]
```

Reportuji vlastní chybu, protože je to relevantní pro důvěru v nástroj: dvě
nezávislá čtení stránky `github.com/mathorn1973/twist-j/blob/main/STATUS.md`
přes fetch vrátila **zastaralou v2 kopii** (commit `7cfe2a62`, 54705 bytes) a
já na jejím základě prohlásil, že recon je vedle. Recon byl přesný a můj
nástroj lhal. Clone je autorita, fetch není. Toto platí i pro budoucí sessions:
veřejnou hlavu neověřovat přes rendrovanou stránku.

Druhá chyba v mém vlastním verifieru, opravená a hlášená: gate G6.2 tvrdil
`J^-1 = J^4`. To je nepravda, `J` není odmocnina z jedničky. Správně z
charakteristického polynomu `J^-1 = -J^3 + 3J^2 - 4J + 2`. Selhalo, opraveno,
zaznamenáno.

## 2. Co Canon v23 skutečně má a co recon přehlédl

`REGISTRY.tsv`, řádek 168:

```text
ENTROPY-BLOCK-HALVING [C]
  the renormalized block maps are exactly two-to-one on the recurrent core
  at every tested dyadic scale k = 0..10 for both letters: exactly one
  unresolved bit per scale
  scope 3. The kernel and the census | ev probes/P-ENTROPY-BRIDGE-2
  note  closed for k = 0..10 and both letters; an all-scale law requires
        a separate public proof
```

plus `ENTROPY-LIVING-SET [C]` (dva obrazy dělí jádro na poloviny po 3125,
všechny čtyři restrikce jsou bijekce) a `ENTROPY-UNIQUE-PAST [C]` (do hloubky
12 má každá word-prefix kompozice obraz 3125 a vlákna přesně dvě; zpětný strom
je housenka šířky dva s jednou smrtí na hladinu).

Inventura pěti povinných objektů monotónní věty:

```text
1  nosič škály, diskrétní index      JE      dyadické k, [C], k = 0..10
2  mapa toku                         JE      renormalized block map, [C]
3  neinvertibilita (pologrupa)       JE      přesně 2-do-1, [C]
4  funkce C(mu)                      NENÍ    existuje jen čítač k
5  fixed pointy a pozitivita         NENÍ    [O], nedeklarované
```

Bod 3 je ta těžká část a je hotová. RG je pologrupa právě proto, že
coarse graining je nevratný, a Canon má nevratnost registrovanou exaktně:
jeden nerozřešený bit na škálu.

## 3. Dva no-go, spočítané, ne tvrzené

Verifier `rg_carrier_nogo.py`, standardní knihovna, exaktní aritmetika,
žádný float v assertu, 34 gates, všechny PASS.

```text
file   sha256 c8959f54ffbf171bd278647e5c9b994c0abef5ac5fb55859b63f21470279ede0
stdout sha256 7ff80f6682e7459770e4bbadcae94ac96c19a5a58d8e8d8a05a690cebaaac0bf
env    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
       Linux x86_64, Python 3.11.15, runtime pod 4 s
platform  jedna platforma. Byte identita na druhé architektuře NEPROVEDENA,
          takže žádný computation-grade nárok se nedělá.
```

### NO-GO 1. Galoisova akce nemůže být tok

```text
Gal(Q(zeta_5)/Q) = (Z/5)^*, cyklická řádu 4, generátory 2 a 3.
orbita generátoru 2:            1 -> 2 -> 4 -> 3 -> 1
moduly podél orbity:            phi, phi^-1, phi, phi^-1
váhy podél orbity:              27/50, 3/50, 27/50, 3/50
generátor PŘEHAZUJE expandující a kontrahující kanál v každém kroku.
komplexní konjugace (r = 4) obě projekce fixuje, takže w klesá na
dvouprvkový kvocient kanálů, na kterém generátor působí jako involuce.
```

Vyčerpávající kontrola všech `4^4 = 256` funkcí na čtyřech vnořeních:
**neexistuje žádná nekonstantní slabě monotónní funkce podél kteréhokoli
generátoru, v žádné orientaci.** Důvod je telescope: čtyři přírůstky po
orbitě mají součet nula, takže jedno znaménko vynutí všechna nulová.

Důsledek: kdo navrhne "expandující -> kontrahující" jako trajektorii,
nenavrhl tok, navrhl involuci. To nezabíjí uspořádání `27/50 > 3/50`.
Zabíjí to jeho čtení jako RG toku.

### NO-GO 2. Tik nemůže nést monotónní veličinu

```text
char poly M_J = x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1)
N(J) = 1, Tr(J) = 3, det(M_J) = 1, tedy M_J v GL_4(Z)
mod 5 je M_J permutace (Z/5)^4 s délkami orbit přesně {1, 4, 20}
každý stav je periodický: každá orbita se vrací do sebe
```

Invertibilní zachovávající objem znamená rekurenci, a podél rekurentní
orbity je každá slabě monotónní veličina konstantní. Recon to tvrdil
správně slovy; tady je to spočítané. **Tik není renormalizační škála.**

Obě no-go dohromady dávají pozitivní obsah: monotónnost může žít jen na
neinvertibilní operaci, a Canon má registrovanou přesně jednu takovou.
Nosič tedy není věc volby, je vynucený.

## 4. Break round: zabil jsem si vlastní most

Lákadlo, kterému jsem podlehl a které jsem pak otestoval: rozdíl kanálů na
konjugovaný pár je `24/25 = 1 - 1/25`, což vypadá jako "jeden bit minus
`1/p^2`", tedy jako most na jednobitové půlení. Otestováno obecným `N`
pomocí `WALL-CIRCLE-LEMMA [T]`, nikoli na `p = 5`:

```text
BR-1  orbitální součet obecně          (N-1)(N-2)/(2N)      ověřeno N = 3..40
BR-2  excess nad 1 roven 1/N           JEN pro N = 5        N = 3..2000
      => tato koincidence p = 5 SKUTEČNĚ vybírá; nový přesný fakt,
         zpřesňuje BR-5 v notě PRINCIP DEKODERU (příčka je p-generická,
         ale excess = 1/p už ne)
BR-3  deficit 1 - pairdiff roven 1/N^2 pro N v {5, 7}, tedy NE jen pro 5
      => most 24/25 a 1/25 je KOINCIDENCE. ZABITO.
BR-4  poměr kanálů 9                   JEN pro N = 5        N = 3..2000
BR-5  9 není mocnina dvojky            => žádný celý počet dyadických kroků
      nereprodukuje poměr kanálů; bitové počítání ty dvě struktury nespojí
BR-6  6250 = 2 . 5^5, 3125 = 5^5       rekurentní jádro nese přesně jeden
      faktor dva nad čistou mocninou p, a ten jediný faktor JE to půlení
```

BR-3 je jediný výsledek tohoto dokumentu, který ubírá, a proto ho hlásím
uvnitř break roundu, ne v souhrnu.

## 5. Strukturální mezera, pojmenovaná jako jedna hrana

```text
grep DEPENDENCIES.tsv na hrany mezi entropickou a stěnovou stranou: PRÁZDNÉ
ENTROPY-BLOCK-HALVING  -> DEF-ARCHITECTURE            REQUIRES
ENTROPY-LAYER-BRIDGE   -> ENTROPY-BLOCK-HALVING       BOUNDED_BY
WALL-LI2-RUNG          -> J-PROJECTIONS, PI-FROM-J    REQUIRES
WALL-CIRCLE-LEMMA      -> J-PROJECTIONS, PI-FROM-J    REQUIRES
```

RG pologrupa žije v sekci 3 (kernel a census). Dilogaritmické váhy žijí v
sekci 16 (p = 5 and the wall). Mezi sekcemi neexistuje ani jedna hrana.
Otevřená otázka tedy není "chybí pět objektů". Je to **jedna chybějící
hrana**, a BR-5 už teď říká, že se nepostaví bitovým počítáním.

## 6. Poctivé oslabení proti vlastnímu nálezu

Toto je nejdůležitější odstavec dokumentu a jde proti tomu, co jsem právě
našel.

Bloková mapa je 2-do-1, ale obraz se stabilizuje na `3125 = 5^5` hned po
prvním kroku a dál už neklesá (`ENTROPY-LIVING-SET`, `ENTROPY-UNIQUE-PAST`:
každá word-prefix kompozice má obraz 3125 a vlákna přesně dvě do hloubky 12;
zpětná neurčitost se nekumuluje). Počet stavů tedy **není** přísně klesající
veličina. Klesne jednou a stojí.

Jediný přísně monotónní objekt na stole je čítač škály `k` sám. A čítač je
monotónní z definice. To není c-teorém. c-teorém tvrdí, že monotónní veličina
je **funkcí teorie**, je stacionární **právě** ve fixed pointech, a **počítá
stupně volnosti**. Nic z toho tady není. Recon měl pravdu v tom, že dvě
hodnoty nejsou monotónní funkce; stejná disciplína musí platit na jeden bit
a jeden čítač.

## 7. Verdikt, po uzavření

```text
[C]  nosič škály EXISTUJE a je veřejný: dyadické k, ENTROPY-BLOCK-HALVING
[C]  půlení je reálné: každé vlákno obou větvových map na jádře má velikost
     přesně dvě, 6250 -> 3125, jeden nerozřešený bit
[T]  Galoisova akce NEMŮŽE nést nekonstantní monotónní funkci
[T]  M_J NEMŮŽE nést monotónní veličinu (det 1, orbity 1, 4, 20)
[T]  NA JÁDŘE NEEXISTUJE ŽÁDNÝ TOK. Viz sekce 8. Toto uzavírá lane.
[F]  most 24/25 a 1/25 na jeden bit: koincidence, platí i pro N = 7, ZABITO
[F]  můj vlastní návrh O-RG-C-FUNCTION-1 ze sekce 8 první verze tohoto
     dokumentu: byl triviálně splnitelný a je nyní zodpovězen záporně.
     STAŽEN.
```

## 8. UZAVŘENÍ: bloková struktura nenese žádný tok

Toto je hlavní výsledek dokumentu a byl nalezen až poté, co jsem si v první
verzi napsal špatně formulovaný otevřený řádek. Hlásím to v tomto pořadí
schválně.

Veřejná sonda `P-ENTROPY-BRIDGE-3` to říká ve svém vlastním RESULT.md:

```text
"All irreversibility of a block sits in its first tick; past the first tick
 the driven dynamics on the living set is invertible."
```

Reprodukoval jsem tu sondu v této session byte identicky: stdout sha256
`a4600f241d499bef6eda8d1efa8fad082b054dcf7bbb5e10746c594401e4d32d`,
1612 bytes, 10 z 10 PASS, exit 0, prázdný stderr. To je třetí platforma
nad rámec dvou zaznamenaných.

Pak jsem na jejích vlastních objektech provedl analýzu toku, nový kód:

```text
graf toku    6250 uzlů, 12500 orientovaných hran x -> F_t(x), t v {0,1}
SCC census   313 komponent: 312 velikosti 20, jedna velikosti 10
             (přesně 313 atraktorů z G01)
mezikomponentní hrany   0 z 12500
transient    9375 stavů mimo jádro, všechny uvnitř po 3 ticích
```

**Lemma (elementární).** Leží-li hrana `x -> y` uvnitř silně souvislé
komponenty, pak pro každé `C` nerostoucí podél hran platí `C(x) = C(y)`:
existuje cesta `y -> ... -> x`, podél ní `C(x) >= C(y) >= ... >= C(x)`,
takže všechny nerovnosti jsou rovnosti.

**Důsledek, přesně ověřený.** Protože je uvnitř komponenty **každá** z 12500
hran, je každá funkce nerostoucí podél blokových map na rekurentním jádře
**invariantem** obou map. `Delta C = 0` identicky.

```text
T-RG-NO-FLOW-ON-CORE  (kandidát na veřejné znění, zatím bez prereg)
tvrzení   Na rekurentním jádře 6250 nemá orientovaný graf obou větvových map
          ani jednu mezikomponentní hranu. Každá funkce nerostoucí podél
          obou map je proto na jádře invariantem. Neexistuje c-funkce a
          bloková struktura nenese renormalizační tok.
falzifikátor  Předveď jednu mezikomponentní hranu, ekvivalentně stav x v
          jádře a nerostoucí C s C(F_t(x)) < C(x).
rozsah    Rekurentní jádro. NEtvrdí nic o transientu, o L5, L6, o CFT,
          o centrálním náboji, ani o soukromé linii.
```

Fyzikální čtení, přesně a bez nadsazení:

> Půlení je skutečné, ale slučuje dva stavy, které leží ve **stejné** silně
> souvislé komponentě. Ten jeden bit je zpětná neurčitost, nikoli dopředná
> monotónnost. Program má relaxaci do jádra dlouhou tři tiky a poté
> invertibilní dynamiku. Relaxace není tok se dvěma fixed pointy; je to
> jednorázový přechod.

Pins analýzy:

```text
file   rg_no_flow.py  sha256 e5888385da7503f4a7cbe9904d7b2bb331cdf25e2a76052f1d81c6cbf22914d1
stdout sha256 d6e8cf3ccc2bcd2073f0856b38ca58a708c8752e190d7cd7d97ba16a6fbe39e9  (1942 bytes)
env    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
       Linux x86_64, Python 3.11.15
nosič  definice generátorů, kódování, driver a census jsou zkopírovány
       doslova z pinnuté veřejné sondy P-ENTROPY-BRIDGE-3. Analýza toku
       je nový kód a je to ta část, která se tvrdí.
```

Poctivé přiznání k této části: první běh analýzy jsem pustil na
**vymyšlených** definicích generátorů, protože jsem je opsal z výpisu grepu,
ne ze zdroje. Carrier gates okamžitě spadly (jádro 15625 místo 6250, pět
komponent místo 313), fabrikace se odhalila sama a byla opravena čtením
zdroje. Zaznamenávám to, protože gate H7 na tom falešném nosiči "prošel",
a prošlý gate na špatném nosiči je přesně ten druh výsledku, který by se
neměl nikdy dostat dál.

## 9. Co s tím dál

Lane je uzavřená, ne otevřená. Pořadí podle hodnoty:

```text
1  P-RG-NO-FLOW-1        veřejná sonda, která uzavře c-teorémovou linii
                         záporně. Prereg musí být napsán PŘED novým
                         veřejným verifierem; můj běh je pouze odvozovací
                         svědek této lane a je jako takový přiznán.
2  P-RG-CARRIER-NOGO-1   dva elementární no-go (Galois, M_J). Levné,
                         aditivní, obojí T.
3  WALL-EXCESS-SELECTS-5 malý přesný přírůstek do sekce 16: excess
                         orbitálního součtu je roven 1/N právě pro N = 5.
4  oprava recon noty      aby se závěr "nosič chybí" nešířil dál.
```

Co se otevírat NEMÁ: `O-RG-SCALE-CARRIER` (nosič je registrovaný) ani
`O-RG-C-FUNCTION-1` (zodpovězeno záporně).

## 10. Co tento dokument NEDĚLÁ

```text
Nepromuje nic. Není preregistrován, není kandidát, není fold.
Nedělá dvouplatformní běh vlastní analýzy, takže žádný computation-grade
  nárok; reprodukce cizí sondy dvouplatformní je, moje analýza ne.
Netvrdí nic o transientu jako o toku. Relaxace do jádra existuje a je
  nevratná, ale je dlouhá tři tiky a nemá dva fixed pointy.
Netvrdí nic o soukromé linii; ta zůstává [O].
Neruší recon. Recon má pravdu v currency, v korekci neunitarity
  (M(4,5) je unitární), v Rogersově dvojici a v tom, že dvě hodnoty nejsou
  monotónní funkce. Mění se jeho závěr o nosiči a přibývá uzavření.
```
