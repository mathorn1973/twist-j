# Posudek PR #1961 (C-S3-HEIGHT-PHASE-INTERFACE-N / CONSTRUCTIVE-3) — fáze 2

## Rozhodnutí: PASS S POZNÁMKOU

Mezi mým slepě napsaným a zmrazeným ověřovačem a autorovými čtyřmi
programy nebyl nalezen žádný skutečný rozpor (DIFF-REAL: 0). Všechny
autorovy hashe, které lze z mých vlastních stavů přepočítat v autorově
formátu, sedí: JSON slova (po normalizaci orientace), všech 14 finálních
stavů sestavy a pořadí navštívených uzlů BFS. Čtení důkazů (kořenový PROOF,
CONSTRUCTIVE-3/PROOF) nenašlo matematickou chybu.

Kandidát zůstává **NON-CANONICAL / L1**, jak sám deklaruje: konstruktivní
analytický kandidát s exaktními audity na jedné architektuře. Tento posudek
žádný status v kánonu nemění, není dvouarchitekturovou vědeckou bránou a
nerozhoduje o v110. Přijetí je rozhodnutí vlastníka kánonu.

## Zmrazení a druhý běh

Zmrazení ověřeno z GitHubu (contents API při commitu
`df5b02081a46b7dcfb3bef942d7811285ecc49bb`): blob id a velikosti
`PREREG.md` 2fa530c3… 16875 B, `README.md` 451974c5… 4970 B, `review.py`
ed52007b… 34395 B se rovnají lokálním `git hash-object`. SHA-256:

```
266a80bb99fb2d4f3349ee50077bc6e9bd80abfddfd1fbd2c8d26afed9f1b245  PREREG.md
91431ffa4268fa739e8637c8bfb23af2861cf34f403be666d86bfd16a6274a00  README.md
c196e23ef7fb969b1b3704f9de4e5f195df321d82af694748d7e10ee407b9cbf  review.py
```

PREREG.md byla commitnuta samostatně jako
`4f729be8eb372053d931ce1eb4a044f70fb8c3d6` před prvním spuštěním
ověřovače a před otevřením jakéhokoli autorova spustitelného souboru či
výstupu. Druhý běh `review.py` (Linux x86_64, CPython 3.13.18, prostředí
dle README): exit 0, `RESULT PASS`, R01–R14 PASS, R15 INCONCLUSIVE,
stdout 2328 B bajtově shodný s během fáze 1 (sha256 `5e246b69…0237`),
stderr prázdný (`RUN-REVIEW.txt`, `RUN-REVIEW-STDERR.txt`). Teprve potom
byly spuštěny a otevřeny autorovy programy.

## Autorovy programy na tomto stroji

Spuštěno beze změny z kořene čistého checkoutu hlavy PR `73f3cb49…caef`
(strom po bězích beze změn), v pořadí dle PREREG PR:

| Program | Exit | stderr | stdout | `cmp` proti očekávanému |
| --- | ---: | ---: | ---: | --- |
| `CONSTRUCTIVE-3/verify.py` | 0 | 0 B | 4165 B, sha256 `72432979…c2203` | EXPECTED.txt: **IDENTICKÝ** |
| `CONSTRUCTIVE-3/audit.py RUN-VERIFY.txt` | 0 | 0 B | 3707 B, sha256 `163342bd…2e9db` | AUDIT_EXPECTED.txt: **IDENTICKÝ** |
| `CONSTRUCTIVE-3/assembly.py` | 0 | 0 B | 2906 B, sha256 `fcc72a21…ae74f` | ASSEMBLY_EXPECTED.txt: **IDENTICKÝ** |
| `search.py` | 0 | 0 B | 449 B, sha256 `b7dcf988…4378a` | EXPECTED.txt: **IDENTICKÝ** |

`sha256sum -c`: kořen 10/10, `CONSTRUCTIVE-3` 12/12 OK. Šest souborů
zmrazených v `5a925ab` a šest v `7406c14` je na hlavě blob-identických;
výsledky přibyly až v `4f84c75` a `73f3cb4`; autor i committer všech čtyř
commitů A. M. Thorn. Časy commitů (pin 11:40:18Z, běh 11:41:06Z, výsledek
11:47:50Z) jsou s pořadím pin → běh konzistentní; jsou to však autorem
nastavená metadata, ne vnější svědek.

## Porovnání R01–R15 (jednostranné vyřízení)

Podrobnosti a formáty jsou v `COMPARISON.json` a `COMPARE-OUTPUT.txt`
(skript `compare_after_run.py` je pomocník fáze 2 mimo zmrazený kód;
používá jen primitiva zmrazeného `review.py`).

- **R01–R03 (prstenec, kontakt, stock):** MATCH; sedm hodnot stocku, `Q=80`,
  `H=33+14phi`, `Sigma`, hodnoty `x_t` i počáteční účty `119+10t^2`.
- **R04–R06 (separátor, značky, zapisovač):** MATCH, stejné stopy
  `AA/RR` a `A R^(5-p) A^4 A^p` / `R A^(5-p) R^4 A^p`. `audit.py` odvozuje
  hodnotu po značce jiným vzorcem (`2 rho x_s/J`) — skutečně odlišná cesta.
- **R07 (kompilátor):** koncové body stav po stavu a stopy znak po znaku
  MATCH; připuštěno na vstup `[30,36,37,38,44]`. Slovo: 95 neuspořádaných
  párů ve stejném pořadí; 20 kontaktů značek má u mne orientaci `C(d_s,g)`
  doslova podle PROOF §3, autor kanonizuje `a<b` (jeho REVIEW.md to uvádí).
  Kontaktní zobrazení je na orientaci nezávislé (můj R02), stopy i stavy
  shodné: DIFF-CONVENTION. Po normalizaci orientace dává mé slovo přesně
  autorův `word_json_sha256`.
- **R08 (formule):** MATCH z mých vlastních sestavených stavů pro `k=1,2,3`.
- **R09–R10 (`S`, `W`, `K`):** moje `S` složené z bloků se rovná
  `WORD535.txt` kontakt po kontaktu; autor fixture parsuje. Můj otisk `S`
  se navíc shoduje s otiskem nezávislého posudku #1879. Uzavřený tvar `W`
  na všech deseti jádrech a kopírovač pro všech pět `r` ověřuji jen já
  (autor je má uvnitř cyklu).
- **R11–R12 (sestava):** všech 14 autorových `final_state_sha256`
  reprodukováno z mých stavů v jeho JSON formátu; počty
  2 597 775 / 864 540 / 1 733 235 / 50 shodné; dekodér, archivy,
  inverze, čerstvost `k,…,0`. Hranice: já 147, autor 114 — jiné počítání
  (DIFF-CONVENTION). Autor navíc chrání dokončené archivy adresou na
  každém primitivu (442 510 kontrol), já jen na hranicích.
- **R13 (analytika):** konečné instance potvrzeny; obecné věty čtením.
- **R14 (citlivost):** oba mutanty detekovány; autor obdobu nemá.
- **R15 (BFS):** můj BFS pod zmrazenou sémantikou K7 dává totéž
  `visited=12853`, `generated=92120`, `unchanged=66022`,
  `duplicate=13246`, `expanded=3290` a **stejný otisk pořadí uzlů**
  `0158b2b9…`. Autorův závěr „žádné společné slovo délky ≤ 6 v této
  osmislotové třídě“ je korektní důsledek úplné expanze hloubek 0–5 a
  testu cíle každého vloženého uzlu hloubky 6; celková klasifikace
  INCONCLUSIVE je správná.

## Poznámky (žádná není věcná neshoda)

1. **Nezávislost autorových programů je vnitřní.** `verify.py` a `audit.py`
   sdílejí seznamy případů a strukturu, liší se reprezentací a odvozením;
   `assembly.py` importuje skalární rutiny z `verify.py` (deklarováno).
   Vše v jedné autorské relaci; RESULT.md PR to říká. Tento posudek je
   první strukturálně oddělená implementace, psaná slepě.
2. **Provenience je zde veřejně ověřitelná** na úrovni blobů: piny
   `7406c14` a `5a925ab` předcházejí výsledkům a zmrazené soubory se
   nezměnily. „Nula běhů před pinem“ zůstává autorovým záznamem.
3. **Jedna architektura.** Můj replay přidává druhé x86_64 prostředí
   (Linux, CPython 3.13), ne druhou architekturu; CI noty nespouští.
4. **Konvence počítání** (3790/4075 řezů, 114 hranic, orientace slova)
   se liší; žádná společná veličina se neliší.
5. **Drobnost v `assembly.py`:** `source(n)` má `Y_1` zapsané jako
   konstantu `(B,J,0)` místo výpočtu `F(Y_0)`; hodnota je správná
   (`u_1=B`, `w_1=J`) a rodina má jen `n∈{0,1}`. `Y_(n+10)` se počítá
   jedním krokem `F`, což je správné díky periodě 9.
6. **Moje fáze 1 měla dva vlastní omyly** před zmrazením (konstanta
   `u_old`, znečištění čítače); jsou popsány v README.md a nezměnily
   kritéria.

## Co ověřil čí kód a v jakém rozsahu

Můj `review.py`: R01–R15 dle PREREG — kompilátor a jeho součásti,
stopky na všech deseti jádrech, kopírovač pro všech pět značek, 14 případů
sestavy s doslovným dopředným programem i inverzí, formule pro `k=1,2,3`,
F16 fakta, oddělení stop, mutanty, BFS. Autorův `verify.py`/`audit.py`:
kompilátor, značky, zapisovače ve dvou reprezentacích; `assembly.py`:
14 případů s doslovným fixture a ochranou archivů na každém primitivu;
`search.py`: BFS s digestem pořadí. Indukci pro všechna konečná `k`
(PROOF §6, WORKBANK PROOF §7) a dyadické no-go (kořenový PROOF §3)
ani jedna strana strojově nedokazuje.

## Co CI

Workflow `policy.yml` na hlavě PR: `check_policy`, unit testy,
`check_canon`, `check_ledger`, `check_gate_contract` prošly;
`check_verifier.py --base` a `check_reproduce.py --base` skončily
`NOT APPLICABLE` (log běhu 42477317656). Lokálně na stromu PR:
`POLICY PASS`, `CANON PASS v109 claims=609`, `LEDGER PASS`,
`GATE CONTRACT PASS`. Diff PR obsahuje jen `notes/`, bez soukromých cest,
adres či CRLF.

## Co zůstalo neověřeno

Příprava `G_t` starým 322kontaktovým loaderem (zde jen premisa);
nezávisle dodávaný zdroj `Y_n`; obecné `k` nad `k=3`; aarch64 replay;
fyzikální interpretace, autonomní provoz, nativní U, S0–S1 (PR je
výslovně netvrdí); minimalita slova či stocku (netvrzena).

## Co nezávislost je a co ne

Je: PREREG i `review.py` psané bez četby autorova kódu a výstupů, vlastní
design, zmrazení přečtené zpět z GitHubu, autorovy soubory otevřené až po
druhém běhu. Není: nezávislost na specifikaci — rovnice, stock, slovo,
případy sestavy i sémantika BFS jsou převzaty z textu PR a z veřejných
předchůdců, takže všechny programy ověřují týž deklarovaný kontrakt; čísla
z těla PR jsem znal předem (PREREG §0).
