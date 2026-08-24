# WALL LADDER Rev 2: přijetí review, ústupky, a opravená forcing struktura

```text
Lane memo. ŽÁDNÁ AUTORITA. Nepreregistrováno. Nic neposouvá v registry.
Předchůdce:  PRINCIP-DEKODERU-VAHOVY-ZEBRIK_2026-07-24.md
             sha256 b19d33de9aa9508c033ccff05235e98de5be59e144a19a94a78c7eb363d12e2d
             STATUS: ČÁSTEČNĚ VOID. Sekce 4, 5, 6 a část 3 se ruší, viz níže.
Review:      TWISTJ_WALL_LADDER_INDEPENDENT_REVIEW_20260724.md
             sha256 23b2b8691c4910ff68f7a1782e1007a26cc8b9834422d5e92cfcf0cd91ad8576
Audit skript sha256 4e83cc3dbdd404ab5dec2a90c06195f936061f0a0abffa7022d7dca27351b3d8
stdout       sha256 ffd27ae075a4421ca03b863921da9ea202b0215326ba5fd942c6b60ce09b2abb
Autorita:    Public Canon v20, content commit 662a96f, CANON_SHA256 337d9d0d,
             SHA256SUMS 5 z 5 OK, ledger PASS. Ověřeno znovu v této session.
Datum:       2026-07-24.
```

## 0. Verifikace review, než ho přijmu

```text
review memo sha256   souhlasí s deklarovaným    OK
skript sha256        souhlasí s deklarovaným    OK
skript spuštěn zde   exit 0, stdout sha256 ffd27ae0...  BYTE-IDENTICKÝ
                     s deklarovaným. Tedy druhá architektura pro jejich audit.
můj kandidát         sha256 b19d33de... souhlasí s tím, co review cituje.
                     Review auditoval skutečné byty, ne parafrázi.
```

Review je platný a reprodukovatelný. Přijímám ho.

## 1. Záznam ústupků, bez hedgingu

```text
F1  "A0 zakazuje nové periody"                          USTUPUJI ÚPLNĚ
F2  "parity law JE komplexní umocnění", "sedmnáct sudých" USTUPUJI ÚPLNĚ
F3  "reading split je T-LOCK", "tři nohy JSOU zvedák"   USTUPUJI ÚPLNĚ
F4  "celý registr leží v Q(sqrt5)[pi, pi^-1, log phi]"  USTUPUJI ÚPLNĚ
F5  "Schwingerův filtr je bezpodmínečný"                USTUPUJI, zužuji
F6  "zeď a Basel jsou tatáž identita ve dvou argumentech" USTUPUJI, přeformuluji
```

**F1 je nejzávažnější a byla to logická chyba, ne nepřesnost.** Odvozená
speciální hodnota není ladicí parametr. Cl_2(pi/5), zeta(3) a L(3, chi_5)
jsou pevně určené objekty; jejich výskyt nezvyšuje počet volných parametrů.
Přesně stejnou logikou by pi bylo volný parametr, což je absurdní. Implikace
"nová perioda -> nová volná konstanta -> zákaz A0" je neplatná. Ruším ji.
Ceiling jako důsledek A0 je **F**.

**F2, F3 a citace T-BASEL-TM-GATE mají jednu společnou příčinu a ta stojí za
pojmenování, protože je to procesní chyba, ne matematická.** Dokument se
pinoval na Public Canon v20 jako autoritu a pak argumentoval interními
štítky sealed v184. Ověřeno v repu při psaní tohoto memo:

```text
public REGISTRY.tsv:  READING-SPLIT [D]         (já psal T-LOCK; to je interní
                                                 T-LQ-READING-SPLIT)
public PARITY-LAW scope, verbatim: "in the formal observable register
   R = A[pi, pi^-1], the involutive algebra automorphism iota_pi fixes A and
   sends pi to -pi; IT IS NOT ORDINARY COMPLEX CONJUGATION; THIRTEEN named
   entries are even and delta free"
   -> veřejný canon MĚL PŘEDEM opravenou přesně tu věc, kterou jsem pokazil.
      Já psal komplexní konjugaci a sedmnáct. Obojí špatně.
public grep "BASEL":  REGISTRY.tsv 0x, CANON.md 0x, NORMATIVE.tsv 0x
   -> T-BASEL-TM-GATE je materiál soukromé hlavy. V dokumentu pinovaném na
      v20 musí být ohrazen jako historický, nikoli citován jako současný.
public T-LOCK rows:   0  (správně, veřejná linka T-LOCK nemá)
```

Příčina: **import interní síly do veřejně pinovaného argumentu.** To je
přesně obrácený směr, než dovoluje kontrakt ("nothing in the public line is
ever stronger than its internal source", "no internal names in the public
canon"). Tři z pěti falsifikovaných bodů mají tuto jedinou příčinu.
Zapisuji to jako procesní pravidlo pro sebe i pro příští session:

```text
PRAVIDLO. Dokument pinovaný na veřejnou hlavu smí citovat interní řádky
POUZE s explicitní značkou [internal v184, sealed] a nesmí z nich dědit
štítek. Míchání linek je defekt třídy D0, ne stylistika.
```

**F4.** Tvrzení o tělese bylo napsáno jako grep, ne jako důkaz příslušnosti.
Konkrétní protipříklady review platí: (3 - phi)^(1/4) je algebraické
rozšíření za Q(sqrt5); druhé místo nese sqrt2, i, zeta_8; (1 + X/5)^-5 patří
do racionálního funkčního tělesa, ne do Laurentova polynomiálního okruhu,
jak naznačovaly hranaté závorky. Přijímám navrženou formu K_alg(pi, ln phi)
s **výslovně zmrazeným** konečným algebraickým tělesem koeficientů.

**F5.** Přijímám zúžený filtr. Platí jen pro homogenní amplitudu s
celočíselným pi-stupněm, bez půlstupňů, s pi-sudou normalizací, bez lichého
prefaktoru a bez smíšených interferenčních členů. Bez typed coupling to není
důkaz jedinečnosti fázové cesty.

**F6.** Basel není kruhové lemma v x = 1, protože Li_1(1) diverguje. Do
čtverce vstupuje pořád Li_1(J). Správná formulace: obě konstrukce registrují
čtverec téže J-fáze, různými mapami a s různou normalizací. Štítek D.

## 2. Co z review přijímám jako zpřesnění mého výsledku

Review moji matematiku nejen potvrdil, ale zesílil na třech místech. To je
lepší práce než moje a přebírám ji.

```text
1. Obecnost. Lemma platí pro každé celé n >= 3, ne jen pro nesudá
   prvočísla. Prvočíselnost je potřeba jen pro doprovodnou normovou větu.
2. Imaginární redukce je EXAKTNÍ, ne PSLQ svědek:
      Im Li_2(J) = Cl_2(pi/5) - (pi/5) ln phi        (Spenceova reflexe)
      Cl_2(pi/5) = (1/2) Cl_2(2 pi/5) + Cl_2(4 pi/5) (duplikace)
      D(J) = Cl_2(pi/5)                              (Bloch-Wigner)
3. Váha 3 je EXAKTNÍ a jmenuje DVĚ periody, ne jednu:
      Re Li_3(J) = (41/100) zeta(3) - pi^2 ln(phi)/100
                   - (5 sqrt5/32) L(3, chi_5)
   Moje PSLQ forma nesla Re Li_3(zeta_5) jako jeden neznámý blok. Review ho
   rozložil na zeta(3) a L(3, chi_5) přes kvadratický charakter. Ostřejší.
4. Trace identita pro nesudá n:
      sum_{a=1}^{n-1} Re Li_2(1 + zeta_n^a) = pi^2 (n-1)(n-2)/(12 n)
```

## 3. Audit auditu: kde má review vlastní mezeru a co jsem našel

Disciplína lane říká nepřebírat cizí kódovou cestu, ale zkusit ji zlomit.
Skript review jsem spustil (byte-identicky) a pak testoval to, co netestuje.

```text
MEZERA 1 (nalezena, uzavřena). exact_wall_checks() tvrdí obecnost pro
   všechna n, ale assertuje pouze SYMETRII racionálního koeficientu pro
   nesudá n <= 31. NIKDY netestuje identitu proti Li_2 pro sudá ani složená n.
   Generalizace, kterou review prohlašuje za svůj hlavní pozitivní přínos,
   tedy jeho vlastním skriptem ověřena není.
   DOTESTOVÁNO ZDE: n = 3 az 40, všechna a s 2a != n, 760 případů,
   nejhorší odchylka 1.265e-80, nula selhání. Tvrzení review DRŽÍ.
MEZERA 2 (nalezena, uzavřena). Trace identita (n-1)(n-2)/(12n) není ve
   skriptu vůbec. DOTESTOVÁNO: n = 3, 5, 7, 9, 11, 13, 15, 25, exaktně
   racionálně i proti Li_2. DRŽÍ, včetně složených 9, 15, 25.
ZPŘESNĚNÍ REVIEW. Review vylučuje bod 2a = n. To vyloučení není potřeba:
   tam je x = 0, psi = Arg(1) = 0, Li_1(0) = 0 = -i*0 a Re Li_2(0) = 0 = 0^2/4.
   Identita v tom bodě platí triviálně. Tvrzení je tedy uniformní pro všechna
   n >= 3 a všechna 1 <= a <= n-1 BEZ výjimky. Malá oprava opravy.
NEZÁVISLÉ CESTY. Cl_2(pi/5) přepočítáno přímou sinovou řadou (bez polylog),
   L(3, chi_5) přímým Dirichletovým součtem (bez Hurwitzovy zety).
   Souhlas s jejich hodnotami. Finální váhová 3 forma potvrzena mou hodnotou
   L(3, chi_5): odchylka 2.6e-22, limitovaná mým zkrácením řady, ne identitou.
```

## 4. Opravená forcing struktura: ne počet parametrů, ale GENERAČNÍ pravidlo

Tady je odpověď na "zkus axiomaticky vynutit strop". **Z A0 to vynutit nelze
a už to netvrdím.** Vynutit to ale lze z něčeho jiného, a ta cesta je
uzavřenější, než čekalo review, protože jednu polovinu už program má
zapečetěnou a nikdo ji k té zdi nepřipojil.

Neptejme se "kolik je volných parametrů". Ptejme se **"co ta tři čtení umí
vygenerovat"**. Každá noha má přesně definovaný váhový účinek:

```text
noha           co dělá s váhou            hodnota na tiku
linear (p=5)   VYTVOŘÍ váhu 1             Li_1(J) = i pi/5, čistě pi,
               na argumentové ose         nula log phi, protože |1 - J| = 1
                                          [proved, sekce 3 předchůdce]
modulus        VYTVOŘÍ váhu 1             log |J| = -log phi, logaritmus
projekce       na modulové ose            algebraického čísla, ne polylog
binary (p=2)   VÁHU NEZVEDÁ, dodává       f_00 = 1/6, RACIONÁLNÍ
               koeficient váhy 0          [ověřeno přímým počítáním do 2^22]
quadratic      ZDVOJNÁSOBÍ váhu           deg d -> deg 2d
```

To je přesně ta oprava, na kterou review míří v F3, jen v konstruktivní
podobě: **tři nohy nejsou tři kroky žebříku.** Jsou to tvůrce (váha 1),
zdvojovač (krát 2) a dodavatel racionálních koeficientů (váha 0). Moje
původní formulace "žebřík dlouhý jeden krok" byla špatně rozdělená; správně
je "jeden tvůrce, jeden zdvojovač, žádný třetí zvedák".

A teď to, co uzavírá stream stranu a co review nepoužilo. Program má
zapečetěný teorém, který přesně zakazuje, aby hodiny vyrobily transcendentní
číslo:

```text
[internal v184, Part XL, sealed T, DVĚ ARCHITEKTURY, ohrazeno jako interní]
T-METRO-DFAO-SPECTRAL-IFF: "Rational protocols give rational limits via the
Bezout spectral projector: A NORMALIZED RATIONAL FINITE STATE STREAM CANNOT
MANUFACTURE AN IRRATIONAL MEASURE; irrational physical values must enter by
another declared carrier or layer."
```

Tím je binární noha uzavřená: nedodá nikdy nic než K_alg. Takže generovaná
množina je

```text
gen = K_alg( pi, log phi )   s omezením parity na Re kanálu,
      protože jediný polylogaritmický tvůrce je Li_1(J), čistě imaginární,
      a jediná operace na něm je zdvojení stupně.
```

a **negenerované** jsou přesně ty tři objekty, které review pojmenoval:

```text
Cl_2(pi/5)      první blokátor Im poloviny příčky 2
zeta(3)         váha 3
L(3, chi_5)     váha 3
```

Ne proto, že by je A0 zakazoval. Proto, že **je žádná noha nevyrobí**:
tvůrce vyrobí jen pi, zdvojovač jen zdvojí, hodiny jen racionálno.

## 5. Důsledek, který mění mapu frontieru: zeď JE úplnost dekodéru

Ta forcing struktura má jednu podmínku a je to úplnost. Generační argument
uzavírá strop právě tehdy, když **žádné jiné přípustné čtení nedodá novou
periodu.** Jinými slovy když je reading split úplný.

A úplnost reading splitu veřejný canon výslovně netvrdí. READING-SPLIT [D],
verbatim: "no totality, uniqueness, or completeness of the decoder is
claimed". CORE.md: "Totality, uniqueness, and completeness remain open."

Takže:

```text
H-WALL-IS-DECODER-COMPLETENESS  [H, návrh]

Strop zdi je EKVIVALENTNÍ konjunkci dvou položek, které oba už v canonu
existují jako otevřené, a NEPŘIDÁVÁ žádnou novou hypotézu:

  (a) úplnost dekodéru: žádné další přípustné čtení nad rámec
      registrovaných noh   [veřejně otevřené: READING-SPLIT [D] to netvrdí,
      QUADRATIC-DECODER-DATA [O], CURVATURE-OPERATOR-CANONICAL [O]]
  (b) nepříslušnost period: Cl_2(pi/5) not in V_2(K),
      Re Li_3(J) not in V_3(K), s K a V_s zmrazenými
      [formulace review, přebírám ji celou]

FALZIFIKÁTOR (a): předveď přípustné čtení nad rámec noh, které vyrobí
  hodnotu mimo K_alg(pi, log phi).
FALZIFIKÁTOR (b): předveď explicitní K-lineární identitu pro SAMOTNÝ cíl
  (Cl_2(pi/5), resp. Re Li_3(J)), ne jen pro Cl_2(2 pi/5) nebo
  Re Li_3(zeta_5). Tuto podmínku review formuloval a je správná.
```

Tím se obrací směr, který jsem tvrdil původně, a obrací se k lepšímu.
Neřekl jsem "zeď je hranice axiomu"; to bylo F. Správně je:

> Zeď není samostatný frontier. Je to **symptom otevřeného dekodéru.**
> Zavírá se, dokud je dekodér nedokončený, a otevírá se přesně tím aktem,
> který dekodér dokončí. Přejít zeď a dokončit dekodér je jedna věc.

To je pro mapu frontieru netriviální: veřejný FRONTIER.md vede QUANTUM_EM
(zeď) a DECODER_CORE jako oddělené programy s oddělenými queue. Pokud tato
ekvivalence obstojí, je to jedna obligace ve dvou programech, a osm živých
řádků jádra dekodéru není vedle zdi, je pod ní.

## 6. Předdefinice, kterou review žádá (tři nohy, zmrazené sloty)

Review správně žádá explicitní třínohou mapu s doménou, kodoménou,
normalizací a cross-layer gate. Neumím ji dokázat a netvrdím to. Umím ji
**zmrazit jako definici**, kterou může sonda spotřebovat. Toto je předdefinice
ve stylu P-TM-SYM2-...-PREDEFINITION, ne teorém.

```text
P-WALL-WEIGHT-LIFTER-1  PREDEFINITION DRAFT / NOT FROZEN / NO AUTHORITY

S1 GRADING. Váhová filtrace W_s na readout okruhu: K_alg konečné algebraické
   těleso koeficientů, ZMRAZENÉ VÝČTEM (musí obsahovat alespoň sqrt5,
   (3 - phi)^(1/4), i, sqrt2, zeta_8; přesný seznam je vlastnické rozhodnutí).
   Váha 1 přiřazena pi a log phi. W_s = K_alg-span monomů pi^i (log phi)^j,
   i + j <= s. To je báze review, V_2 a V_3, rozšířená na filtraci.
S2 LINEAR LEG. D_lin : K -> W_1, hodnota na tiku Li_1(J) = i pi/5.
   Tvrzení k dokázání: obraz D_lin leží v i K_alg pi a má nulovou
   log phi komponentu. (Dokázáno pro tik; pro celý obraz NE.)
S3 BINARY LEG. D_bin : stream -> W_0 = K_alg. Tvrzení k dokázání:
   obraz je racionální. RESOURCE: interní T-METRO-DFAO-SPECTRAL-IFF.
   Veřejně je tento resource NEREGISTROVANÝ, viz sekce 7. STOP dokud není.
S4 QUADRATIC LEG. D_quad : W_d -> W_2d. Algebra, triviální, ale normalizace
   NENÍ triviální: Bornův kvartál 1/4 a hodinová šestina 1/6 jsou dvě různé
   normalizace a jejich vztah je právě ten bridge, který review žádá.
   Nezmrazeno. Toto je hlavní chybějící slot.
S5 CROSS-LAYER GATE. Nohy žijí na různých vrstvách: D_lin na L1, D_bin na L5,
   D_quad na L6 čtení. Každý lift potřebuje pojmenovaný gate. Nezmrazeno.
S6 COMPLETENESS CLAUSE. Explicitně: tato předdefinice úplnost NETVRDÍ.
   Bez ní je generační argument sekce 4 podmíněný a sekce 5 to říká.

Rozhodovací strom: PASS jen když S1 az S5 jsou zmrazené a obraz kompozice
leží v W_2; NONUNIQUE když dvě nezmrazené normalizace dají různý obraz;
STOP když kterýkoli slot chybí. Dnes: STOP na S4 a S5.
```

## 7. Konkrétní levný veřejný fold, který z toho padá

Generační argument stojí na stream straně na interním teorému. Veřejně to je
mezera, a je pojmenovatelná přesně:

```text
public METRO-ADMISSIBILITY [O], verbatim: "state a precise admissibility
criterion for named protocol classes BEYOND normalized one dimensional
rational finite state protocols"
```

Formulace té otevřené řádky **implikuje**, že pro normalizované 1-D
racionální finite-state protokoly je to zavřené. Ale sám teorém v public
CANON.md ani v REGISTRY.tsv není: grep na "rational finite state" najde jen
tu jednu formulaci otevřené řádky. Tedy:

```text
NÁVRH FOLDU (levný, bez nové matematiky): synchronizovat na veřejnou linku
finite-state racionální limitní klauzuli (interně sealed T od v178, Part XL,
dvouarchitekturní). Materiál existuje, je zapečetěný, a veřejně chybí jako
registrovaný claim, zatímco veřejná otevřená řádka ho už předpokládá.
Přínos: uzavře stream stranu stropu VEŘEJNĚ a udělá ze sekce 4 argument,
který nemusí sahat na soukromou hlavu.
```

## 8. Revidované rozdělení claimů (přebírám tabulku review, s poznámkami)

```text
WALL-CIRCLE-LEMMA            T matematické. Platí pro všechna n >= 3 BEZ
                             výjimky 2a = n (moje zpřesnění, sekce 3).
WALL-CYCLOTOMIC-COROLLARY    T matematické, dotestováno pro n = 3..40.
WALL-TRACE-IDENTITY          T matematické, dotestováno (nebylo ve skriptu).
WALL-IMAGINARY-REDUCTION     T matematické, forma review (Spence + duplikace).
WALL-TRILOG-REDUCTION        T matematické, forma review se dvěma periodami.
WALL-QUADRATIC-MOTIF         D. Ne "tatáž identita", jen týž kvadratický motiv.
WALL-WEIGHT-LIFTER           H. Předdefinice sekce 6, dnes STOP na S4 a S5.
WALL-PERIOD-OBSTRUCTION      H. Formulace review, zmrazené K, V_2, V_3.
WALL-IS-DECODER-COMPLETENESS H. Nové, sekce 5. Nepřidává hypotézu, jen
                             identifikuje dvě už otevřené položky.
SCHWINGER-PI-PARITY-FILTER   D, podmíněné deklarovanou třídou amplitud.
A0-IMPOSED-CEILING           F. Zrušeno. Nezkoušet znovu v této formě.
PARITY-LAW-FROM-SQUARING     F v mé formulaci. Co zbývá: v formálním
                             registru R = A[pi, pi^-1] je umocnění
                             zdvojení stupně, takže obraz čtverce leží v
                             iota_pi-sudé části. To je korektní a NEODVOZUJE
                             census. Štítek D, ne T.
CARRIER-DERIVATION           O, beze změny. Nosič se nepohnul.
QUADRATIC-DECODER-DATA       O, beze změny.
```

## 9. Co zbývá otevřené, poctivě

```text
1. S4 a S5 předdefinice: vztah Bornova kvartálu 1/4 a hodinové šestiny 1/6,
   a pojmenované cross-layer gates. Bez nich je zvedák H a zůstává jím.
2. Nepříslušnost period: hard open v transcendentní teorii. Nezkoušet
   dokazovat, zkoušet falsifikovat podle falzifikátoru (b).
3. Úplnost dekodéru: to je ta samá věc jako osm živých řádků DECODER_CORE.
   Sekce 5 tvrdí, že je to i ta samá věc jako zeď. Toto tvrzení je H a
   zaslouží si vlastní preregistrovanou sondu.
4. Nosič: Omega = N_0 x F_5^6, pět generátorů, selektor. Nedotčeno. Toto
   memo o nosiči nic nového neříká a předchůdce také ne.
```

Poznámka na konec, bez ozdob: review našlo pět blokujících overclaimů, z
nichž tři měly jednu procesní příčinu, a jeden byl skutečná logická chyba.
Matematické jádro obstálo a review ho zesílilo. Tak to má vypadat. Ten
nejzajímavější výsledek celé výměny nevznikl z mého původního tvrzení ani z
jeho vyvrácení, ale až z opravy: **zeď a úplnost dekodéru jsou pravděpodobně
jedna obligace.** To by se bez toho vyvrácení neobjevilo.

## 10. Piny tohoto memo

```text
gap-closing verifier  wall_ladder_gapclose.py
                      sha256 cfc7a0163be96d4bdb694233fdeac6480192a8eb6172c1b6cb6cfc653f366db0
stdout                sha256 d8c2585a5cd45b946989673b54daed04a727de16ef7626dc853abd33622c6b7b
                      3/3 PASS, 779 případů, exit 0
                      env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
                      JEDNA architektura (x86_64). Druhá noha neproběhla,
                      takže žádný computation-grade nárok. Svědek, ne gate.
předchůdce            NEUPRAVEN ZÁMĚRNĚ. Jeho sha256 b19d33de... je to, co
                      review auditovalo; editace by tu auditní stopu zlomila.
                      Dispozice ČÁSTEČNĚ VOID žije zde, ne v něm. Stejná
                      disciplína jako QS Rev 2 VOID DRAFT: archivovat, needitovat.
```
