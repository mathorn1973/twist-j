# Vědecký stav po Public Canon v31 a plán posunu

**NON-CANONICAL.** Analytická poznámka, žádná autorita, žádná změna
Canonu, žádný dotčený soubor v `canon/`. Nezavádí žádný claim, gate,
status ani verifikátor; je to plánovací vstup pro vlastníka.

```text
base            Public Canon v31 ACTIVE
tag             canon-v31
content commit  7c8b57aac8df8460cb0ef928659fb07b2444f7ff
checkery        CANON PASS v31 claims=217; LEDGER PASS; POLICY PASS
ověřeno         2026-08-02, z čistého klonu public main
```

## 1. Souhrn stavu

Registr: 217 claimů; 115 T, 40 D, 24 C, 4 H, 24 O, 10 F; 28 živých
H/O řádků; 22 reprodukčních svědků. Frontier je rozdělena do osmi
programů; z 28 živých řádků je 6 READY, 13 STOP a 9 BLOCKED.

Delta v31 je jediný fold: `COLOR-CM-2I-SEMILINEAR-PAIR [T]` — L4
kostra kvadratické nohy na značeném celočíselném 2I reprezentantu
(stabilizátor {1,sigma}, Q-hodnotový párový charakter s kompletními
Hom daty, antidiagonální klasifikace semilineárních struktur s kocyklem
[-1] a minimálním řádem osm, Gramova F-přímka F·H0 s vyváženým
multiplikátorem phi^2). Obě inkubační vrstvy C-CM-2I-QCARRIER-1/2 tím
prošly do Canonu přes sondu `P-CM-2I-QCARRIER-1`; jejich obsah už není
čekající promoce, je to provenience.

Hybnost programu teď nesou tři shluky:

1. **CM/Herm2/ikosiánová lane** (kvadratická noha dekodéru) — v31 fold
   plus tři dosud nepromované kandidátní balíčky z 2026-08-02.
2. **Totalizace D_matter** — rozsáhlá owner-freeze příprava série
   `P-DMATTER-TOTAL-1` v `notes/canon/` a kontraktní manifest
   `DEF-DECODER-COMPLETION-CONTRACT`.
3. **Metrologická a měrová lane** — silně ohraničené no-go výsledky
   (ENTROPY-CYLINDER-NOGO-CURSOR, čtyři J-LI no-go, fired N2
   TM-SYM2-MEASURE), ale kladné směry stojí na STOP kvůli
   nezmrazeným schématům.

## 2. Uzavíratelné z existujícího materiálu (Tier 1)

Hotový, gate-ověřený materiál, kde chybí jen formální promoce
(dvouarchitekturní sonda podle POLICY §3–4 + fold):

- **P-CENTRAL-LIFT-PHASE-1** z `notes/C-CENTRAL-LIFT-PHASE-1`
  (16 exaktních gate; jádro externě auditované jako theorem-grade).
  Obsah: pinning větve J, projektivní pátá mocnina, kuželová věta
  bez samplování, tick bez odmocnin, centrální fáze zeta5^2, separace
  mu_5 vs mu_10, integrální tick-žebřík, split-unit projektory.
- **P-COMMON-CARRIER-ICOSIAN-1** z `notes/C-COMMON-CARRIER-ICOSIAN-1`
  (45 + 6 break gate). Obsah: ikosiánový řád jako společný nosič
  veřejného A5 (přes 2I) a J-kroku, volný rank-2 Z[zeta5]-modul,
  glue indexu 5 v ramifikovaném prvočísle, kritérium lepení a
  twistovaný sudý tick. Pozor: opora o Steinitze a h(K)=1 je
  [T, literatura] — v PREREGu explicitně oddělit.
- **Herm2 páteř** z `notes/C-HERM2-BORN-CONE-1` (47 gate): kužel
  Born = kauzální, vynucený Minkowski (rigidita b = -a), nález A
  (Galois vynucuje pár (Psi Psi^dagger, Psi Psi^T), tedy dvouslotový
  dekodér), jedinečnost CM typu až na Galois. Vzorkované M2/M3 jsou už
  překlopeny na mřížkový důkaz v CP5–CP6; sondu stavět na té verzi.

Tři sondy, tři samostatné PR (každý mění jeden probe adresář), fold do
v32. Očekávaný efekt: 3–5 nových T/D řádků na L4/D vrstvě. Žádný živý
O řádek se tím sám nezavře, ale STOP seznam QUADRATIC-DECODER-DATA se
věcně zkrátí (koeficientový okruh, efektivní nosič, Gram, dagger,
transpose, vynucení páru Q).

Poznámka ke statusu: v31 changelog ukazuje páku T vs C — bez
vlastníkova přijetí důkazu jako theorem-grade v PREREG §7 zůstane
každá promoce jen C. Přijetí je třeba naplánovat jako explicitní krok
u všech tří sond.

**Levný kredibilitní uzávěr navíc:** censusový shluk (CENSUS-313,
CENSUS-Z5-SHEET, CENSUS-PAIRING, CENSUS-HOSTING,
HYPERPLANE-BOUNDARY-REALIZATION) má falzifikátory znějící „zůstává C
bez nezávislé implementace nebo protokolové nezávislosti". Jedna sonda
s nezávislou reimplementací kernelu (jiný jazyk nebo nezávisle napsaný
enumerátor, byte-shoda transkriptů) zvedne pět C řádků najednou a je
čistě mechanická. Zapadá i do připravovaného Lean programu.

## 3. Co odblokuje owner freeze (Tier 2)

STOP řádky, kde rozhodovací podmínka je přesná a chybí jen veřejné
zmrazení schématu — žádná nová matematika před freezem:

- **QUADRATIC-DECODER-DATA [O, ROOT]** — pákový bod celého programu.
  Chybějící pole (MatterData schéma, orbit-to-amplitude most, write
  mapa, graf závislostí…) mají rozpracované owner-freeze podklady
  v sérii `P-DMATTER-TOTAL-1`; CM lane dodává kandidátní nosič, okruh,
  Gram, dagger i transpose a nález A dává kandidátní vynucení samotného
  páru Q. Po freezu je `P-DECODER-SOS-FORM-1` (návrh nesený Herm2
  lane) rozhodnutelná: kladnost je věta, pokud registrované výstupy
  censusu mají tvar sum w_i psi_i psi_i^dagger, s ostrým falzifikátorem
  (jediné registrované pole mimo tvar).
- **TM-SYM2-PHYSICAL-MEASURE [O, ROOT]** — N2 hranice je definitivní
  (gauge se nesmí zvětšovat); chybí zmrazení schématu nástupnického
  L5 zdroje se zachovanou orientací epsilon_read. Čistě vlastníkovo
  rozhodnutí o typu; do té doby řádek stojí legitimně.
- **SQRT-PHI-TIME-GRAVITY [O]** — STOP vyjmenovává přesně sedm polí
  k zmrazení (doména, ekvivalence/selektor větví, konvence
  pre/post-update, Y→D_clock mapa, kodoména, rovnost, závislosti).
- **OBSERVER-WRITE-PORT [H]** — potřebuje výstupní schéma a typ
  write-kanálu; kladné uzavření je pak typovaný graf závislostí,
  architektura („výstupy dekodéru nikdy nekrmí update") už je
  deklarovaná, takže jde o dokončení typování, ne o novou větu.
- **DE-CONFORMAL-WEIGHT [O]** — poddeterminovanost je od
  DE-TRACE-DENSITY-UNDERDETERMINATION [T] vyřízená; zbývá zmrazit
  registrovaný zdroj a typovaný slovník (a hlídat CIRCULAR výluky).
- **CURVATURE-OPERATOR-CANONICAL [O, ROOT]** — predefinice, kandidát
  definice i AUT-redukce už leží v `notes/canon/`; zbývá dotáhnout
  klasifikaci do exaktního rozhodnutí UNIQUE/NONUNIQUE/EMPTY. Zkušenost
  z CM lane (trichotomie nahrazená E1–E4 strukturou) je tu přenositelná
  lekce pro formulaci PREREGu.

Doporučení: jeden „freeze sprint" vlastníka nad QDD poli má největší
poměr dopad/úsilí v celém programu — QDD je ROOT DECODER_CORE a jeho
STOP blokuje i navazující SOS a U(1) sondy.

## 4. READY řádky — kde je potřeba nová věda

Formálně otevřené, sondovatelné hned, ale vyžadují nový výsledek:

- **QUANT-SUBSTRATE** — nejostřeji definovaný READY cíl: aritmetický
  terč J·Jbar/script-Q = 1/(2 pi) je už registrovaný [T]
  (QUANT-SCHWINGER-TARGET); otevřená je derivace jako
  [alpha^1]((g_e(alpha)-2)/2) ze substrátové vazby, plus Larmorova
  klauzule. Doporučený první úder po CM triu.
- **PHOTON-WINDOW-PROOF** — dvě přesné povinnosti: (i) F_occ >= kappa L
  pro uzavřené worldliny náboje 5 s 2^(4 kappa) > 2401,
  (ii) roughening certifikát pro deklarovaný Froehlich–Spencer import.
  Kombinatorická povinnost (i) je vhodná i pro čistě strojový útok.
- **TT-VECTOR-STATE-NORMALIZATION** — jediná brána k numerickému
  r_T(k); negativní uzávěr („každá normalizace porušuje TT identity
  nebo chce nový volný parametr") je také plnohodnotný výsledek.
- **GENERATIONS-L3** — binární rozhodnutí (počet generací = 3, jinak
  negativní uzávěr); bez rozpracovaného podkladu, vysoké riziko.
- **SCHEME-DICTIONARY** — slovník seed vs měřicí schéma; negativní
  falzifikátor (nový volný bezrozměrný parametr) je ostrý. Uzavření
  by odblokovalo ALPHA-S-RUNNING (BLOCKED).
- **LAMBDA-COCYCLE-ANGLES [H, ENRICHMENT]** — kocyklová forma je
  poslední přeživší trasa po čtyřech J-LI no-go; enrichment režim,
  nižší priorita, ale dobře ohraničená.

## 5. BLOCKED řádky — vědomě nechat ležet

NS-TILT čeká na CMB-S4 (empirický režim), QNM-LEAVER-MU na externí
shadow měření + preregistrované inferenční pravidlo. COIN-MINIMAL-READ
visí na MINIMAL-READ-DERIVATION, DRESS-CROSSCOUNT a METRO-EDGE-SCALE
na dekodérové a selektorové upstream práci, FRW-INHOM a TT-SOURCE na
tensorových zdrojích, NEUTRON-DELTA-EM na kompresním kanálu,
ALPHA-S-RUNNING na SCHEME-DICTIONARY. Žádný z nich nemá dnes levnou
akci; jediná průchozí cesta je přes upstream řádky výše.

Střední pásmo mezi Tier 2 a novou vědou je METRO-REDUCTION-CALCULUS:
povinnosti B (katalog zakázaných transformací s exaktními svědky),
D (společné q^k blokování s úplným transportem) a E (úplnost
approx_red) jsou konečně vymezené a navazují na uzavřené A a C
z METRO-REDUCTION-ARROWS [C]; je to pracná, ale definovaná agenda.

## 6. Změna axiomatiky — dopadová analýza

Ohlášená změna axiomatiky je za současné policy zvládnutelná bez
dopadu do hloubky, pokud se dodrží tři věci:

1. **Vlastní zapečetěný fold.** Jde o změnu obsahu `canon/`, tedy
   release procedura podle POLICY; nikdy nemíchat s vědeckými foldy.
   Ordinary-fix cesta je vyloučená.
2. **Scope-relativita chrání registr.** Každý registrovaný řádek je
   formulován vůči svému scope („relative to the displayed marking"
   apod.). Dokud nová axiomatika ponechává J = 1 + zeta_5^2
   definovatelné (ať už jako axiom, nebo jako odvozený objekt),
   žádný T řádek se nehýbe a checkery to vynutí.
3. **Reconciliation-style audit axiom-přilehlých řádků.** Slovně se
   axiomu dotýkají zejména: CORE.md (explicitní klauzule, že
   architektura NENÍ jednoznačně odvozena z J),
   AXIOM-PROJECTION-DICTIONARY [D], READING-SPLIT [D],
   FORCE-AS-CURVATURE [D], TWO-PLACE-PHYSICS [D]. Levná pojistka je
   projít těchto ~10–15 řádků mapou „starý výrok → výrok v nové
   axiomatice" před foldem, stejným stylem jako genesis reconciliation.

Pokud změna axiomatiku *posiluje* (více architektury odvozeno, méně
deklarováno), patří výsledky do nových T/D řádků, ne do editace
stávajících; přirozené cíle, které by z toho těžily, jsou
MINIMAL-READ-DERIVATION [O] a CURVATURE-OPERATOR-CANONICAL [O].

## 7. Doporučené pořadí

```text
1  (probe x3)   P-CENTRAL-LIFT-PHASE-1, P-COMMON-CARRIER-ICOSIAN-1,
                P-HERM2-BORN-CONE-1; owner theorem-grade přijetí
                v PREREG §7 u každé; fold v32
2  (paralelně)  owner freeze QDD polí ze série P-DMATTER-TOTAL-1
                (+ TM-SYM2 zdrojové schéma, pokud je rozhodnutí zralé)
3  (probe)      P-DECODER-SOS-FORM-1 po freezu; pak P-U1-DICTIONARY-1
4  (nová věda)  QUANT-SUBSTRATE (Schwingerova derivace) jako nezávislý
                úder; PHOTON-WINDOW-PROOF povinnost (i) jako strojově
                vhodný druhý cíl
5  (kredibilita) nezávislá reimplementace censusu -> pět C řádků;
                 vstupní bod pro Lean lane
6  (samostatně) axiomatický fold s reconciliačním auditem podle §6
```

Krok 1 a 2 jsou nezávislé a mohou běžet souběžně; krok 3 závisí na 2;
krok 6 je nezávislý na všem ostatním a měl by dostat vlastní verzi
Canonu bez příměsí.

## 8. Dodatek: posun k 2026-08-02 večer

Stav se od sepsání §1–§7 pohnul; tento dodatek nic výše nepřepisuje,
jen zaznamenává deltu a upřesňuje pořadí.

- **PR #252 merged: P-CENTRAL-LIFT-PHASE-1 proběhla formálně.**
  10/10 PASS, dvouarchitekturní gate splněn (lokální x86_64 +
  GitHub aarch64), post-CI ratifikace zapsána, owner přijal PREREG §7
  jako theorem-grade před pinem — T je dostupné přesně na E1–E3 scope.
  Pozor na zúžení: výsledek je jen L4 kvadratická opora (projektivní
  pátá mocnina, centrální znaménko, Herm/Sym skalární zákony,
  mu_5/mu_10 obstrukce). Kužel/rigidita (Herm2 páteř) a ikosiánový
  nosič v ní NEjsou — Tier 1 tedy pokračuje dvěma zbývajícími sondami.
  První položka kroku 1 je hotová a čeká na fold.
- **PR #249 (draft): policy vrstva „Supplemental Lean audits".**
  Dobře postavený firewall: audity jen pro už uzavřené T/T-LOCK řádky,
  žádný dopad na status/scope/gate, oddělený katalog `audits/INDEX.tsv`,
  EXACT vs PARTIAL pokrytí, immutabilní balíčky s append-only událostmi,
  CI validuje katalog, ale Lean nespouští — kernel acceptance zůstává na
  nezávislém reviewerovi s replay z čistého prostředí. Jde o závaznou
  změnu POLICY + nový checker (`check_audits.py` + testy) + zásah do
  AGENTS.md; potřebuje plnou revizi, ale koncepčně je to správná
  architektura pro kredibilitu.
- **PR #247 (draft): notes/lean-j-cyclotomic laboratoř.** NON-CANONICAL,
  na #249 nezávislá: pinnuté prostředí, kvartika J (symbolický důkaz
  anihilačního vztahu pro J = 1 + zeta^2), první abstraktní „CM floor"
  (involuce zabitá všemi ZMod-2 charaktery má odmocninu aditivního řádu
  čtyři — abstraktní echo C4/C8 bitu), a SELECTION-CONTRACT pro
  minimal-abelian-CM větu. Ten kontrakt je zjevně předpolí ohlášené
  změny axiomatiky (výběr Q(zeta_5) jako věta místo postulátu) a drží
  správný firewall aritmetika vs fyzikální čtení.

Upřesněné pořadí:

```text
1a  fold v32 = central lift phase (ratifikováno, fronta je čistá;
    kadence jedna položka na verzi drží)
1b  souběžně pin P-COMMON-CARRIER-ICOSIAN-1 (tik-tok: další sonda
    během foldu; v PREREG §7 oddělit [T, literatura] opory
    Steinitz/h(K)=1 a explicitně rozhodnout owner přijetí)
1c  potom Herm2 páteř (kužel, rigidita, nález A) jako třetí sonda
2   merge pořadí Lean: nejdřív #249 (policy, s nezávislým reviewer
    replay), #247 může jako notes kdykoli; první audit balíček pak
    přirozeně A-LEAN-* nad kvartikou J (scope J-UNIT, u J-PROJECTIONS
    nejspíš PARTIAL — archimedovská část výslovně vyjmenovat)
3   QDD freeze sprint (§3) běží nezávisle dál — pořád největší páka
```
