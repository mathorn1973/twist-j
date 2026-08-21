# CENSUS v2: párování a klasifikace slotů completion manifestu

```text
STATUS   NON-CANONICAL. Audit a recon, mechanická práce bez matematiky,
         jedna platforma, deterministický výstup. Žádný claim, žádný
         posun statusu, žádná úprava normativního souboru. Zadáno
         vlastníkem 2026-08-05 ("udělej census v2"); navazuje na
         CENSUS-DMATTER-MANIFEST_v30_2026-08-01 (census v1).
BASIS    Public Canon v36 ACTIVE, main head 470d958 (merge PR #272),
         ověřeno fetch 2026-08-05. Skeleton
         notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json
         sha256 b19e073743fde8a71a18a9394c2c1bf71289ef515d626787ac290f6cfd57aa86
         18770 B, BEZE ZMĚNY od censu v1, deklarovaný pin stále v23.
         Nový vstup: notes/canon/P-DMATTER-TOTAL-1-EFFECT-SHADOW-
         MINIMAL-OWNER-FREEZE.md (vlastnický freeze 2026-08-04, PR #272,
         báze v36, issue 107).
SKRIPT   claude/census_dmatter_manifest_v2.py
         sha256 ccff30e9511764c4446406dde6cc8dd68a9bb993c68185a145f99e4ee05a0cb2
STDOUT   claude/census_dmatter_manifest_v2.stdout.txt
         sha256 5a04bb683bfe2343b4bccd2b85784d4a32c9483272c07d6a45ac6008b79c06ed
         exit 0, stderr prázdný; křížová kontrola v1 (242/38/204) sedí.
```

## Metoda

Census v1 spočítal sloty (242, z toho 38 nesených, 204 UNRESOLVED).
Census v2 každý ze 204 UNRESOLVED slotů (a) páruje s zobrazenou lokální
hodnotou z proposal_local_catalog, existuje-li, a (b) klasifikuje do
jedné z osmi tříd. Klasifikace je úsudek zapsaný jako explicitní
pravidla ve skriptu, každé netriviální přiřazení nese zdůvodnění;
stroj garantuje pokrytí 204 z 204 a aritmetiku, ne úsudek. Kdo chce
census vyvrátit, ukáže na konkrétní pravidlo a řádek, který mu
odporuje.

```text
S-BIND    vazba a publikace už zobrazeného lokálního objektu (včetně
          rebuildu stale typingu na v36)
S-NAME    čisté pojmenování (candidate_id)
S-MECH    vyřeší se mechanicky při pinu (public_pin_id)
S-EVAL    ohodnocení povinnosti po rebuildu balíku
S-AFTER   session derivace hradlovaná pojmenovanou závislostí
S-DERIVE  session derivace s reálně chybějícím obsahem
OWNER     skutečná vlastnická volba nebo freeze
O-FROZEN  vlastnická volba UŽ zmrazená poznámkou z 2026-08-04;
          zbývá vazba slotu na freeze
```

## Výsledek

```text
třída      slotů
O-FROZEN       2      účinky a Bornovo párování: EFFECT_SHADOW_MINIMAL
OWNER         13      viz rozklad na rozhodnutí níže
S-AFTER        6      metrologie (za METRO kalkulem), normalizace (za
                      mírou), fyzika za zdrojem, terminalita (za OWP
                      podstromem)
S-BIND       165      vazba a publikace; největší položka
S-DERIVE       1      factorization_map_id (nezávislost deklarovaná
                      False; režim určuje usnesené ruling 9.2)
S-EVAL        15      value_state 15 povinností po rebuildu
S-MECH         1      public_pin_id
S-NAME         1      candidate_id
CELKEM       204
```

Párování: 28 slotů nese přímo zobrazenou katalogovou hodnotu (X, K0,
Veff, V_lin, K_amp, QCarrier, CandidateQuadraticData, G, Q, dagger,
transpose, Qcan, iota_B0, beta, D_scoped, čtyři identitní hodnoty).
Dalších ~137 S-BIND slotů čerpá ze stale lokálního typingu vázaného na
rebuild (viz níže).

## Jedno číslo

**Mezi skeletonem a vyplnitelným manifestem stojí 13 vlastnických
slotů, které se skládají do PĚTI vlastnických rozhodnutí:**

```text
D1  typování vrstev a bran tří record mostů (beta, iota_B0,
    D_scoped_record): 9 slotů, jedna deklarace; reziduum OD2
    (layer_state, gate_state ponechány UNRESOLVED)
D2  measure_id: schválit nástupnický L5 zdroj (TM-SYM2-PHYSICAL-
    MEASURE, jediný vlastnický STOP frontieru)
D3  scheme_id: pojmenovat měřicí schéma (SCHEME-DICTIONARY)
D4  source_id: zvolit a definovat veřejný zdrojový objekt (TT-SOURCE;
    session může draftovat, volba je vlastníkova)
D5  detector_id: volba instrumentu (OD4: instrument UNRESOLVED,
    vyžaduje samostatnou predefinici)
```

Všechno ostatní z 204 je session práce: 165 vazby a publikace, 15
ohodnocení, 6 hradlovaných derivací, 1 skutečná derivační mezera, 2
mechanika. Poctivé čtení nálezu N3 censu v1 se potvrzuje a zpřesňuje:
**dluh D_matter rohu není chybějící matematika, je to z 81 procent
vazba a publikace, a volby v něm jsou spočítané: pět.**

Vztah k větě o modulech (v30): tohle je census-level horní odhad
volnosti v jádrovém rohu stage D_matter, leg D_quadratic. Zda každé z
pěti rozhodnutí je skutečný modul (NONUNIQUE), vynucené (UNIQUE), nebo
prázdné (EMPTY), rozhodnou až jednotlivé věty; census dává seznam,
věta o modulech dá klasifikaci.

## Delta od censu v1

```text
1  EFFECT_SHADOW_MINIMAL (2026-08-04, PR #272): vlastník zmrazil
   uspořádané výstupy LOW/HIGH, přesnou dvojici účinků
   E_low = (1/4)11^T, E_high = I - E_low, singleton přípustnost,
   úplnost, Bornovo stopové párování, hranici ZERO/NONZERO a
   source-forgetting jako typovaný kvocient. Tím jsou sloty
   effect_ids a born_pairing_id rozhodnuty na úrovni poznámky;
   skeleton je ještě nenese (O-FROZEN, zbývá vazba). QDD zůstává
   O / STOP beze změny, jak poznámka sama říká.
2  Skeleton se od v1 nezměnil (týž sha256): rebase z pinu v23 na
   v36 dál chybí, overlay factor_canonicity (přidán ve v24) dál
   chybí, a čtyři lokální binding artefakty jsou podle freeze
   poznámky STALE_BASE do rebuildů a reauditů na v36. Žádný S-EVAL
   slot nelze vyplnit před tím rebuildem.
```

## Pojmenované chybějící objekty MIMO 204 slotů

```text
D_direct_state UNRESOLVED       přímý zápis; režim určuje ruling 9.2
ledger edge QDD REQUIRES        DEF-DECODER-COMPLETION-CONTRACT:
                                ledger_state UNRESOLVED; fold akt
stream_extension,               otevřené hranice OD2 a OD3 mimo jádrový
hybrid_extension                rozsah, UNRESOLVED záměrně
```

## Doporučené pořadí konzumace (nikoho nezavazuje)

```text
1  Rebuild binding balíku na v36 + rebase skeletonu (S-BIND hromadně;
   levné dle N6 censu v1, schéma drift v23 až v36 je jen overlay).
2  Vazba O-FROZEN slotů na EFFECT_SHADOW_MINIMAL (2 sloty, hotový
   freeze).
3  D1 (typování vrstev): jedna vlastnická deklarace odemkne 9 slotů
   naráz; nejlevnější z pěti rozhodnutí.
4  S-EVAL průchod povinnostmi po rebuildu (15 slotů).
5  D2 až D5 podle vlastníkova pořadí; D4 může session předžvýkat
   draftem zdrojového objektu.
```

## Falzifikátor tohoto censu

Census je chybný, pokud opakovaný běh pinovaného skriptu dá jiné
počty; pokud kterýkoli citovaný pin nesouhlasí s hlavou; pokud se
ukáže, že některé klasifikační pravidlo odporuje textu vlastního
řádku (pak se opraví pravidlo a přepočítá, oprava se zaznamená, práh
se nehýbe); nebo pokud freeze poznámka z 2026-08-04 neříká to, co
delta 1 tvrdí.
