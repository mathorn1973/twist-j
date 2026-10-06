# P-RESIDUAL-RECORD-COMPOSITION-1 — formální preregistrace

NON-CANONICAL, L1. V100-JOIN-1, přijetí existujícího rozsahu 2026-10-06.
Vlastník `v100-composition-review-20261006`, rezervace #1387, předloha #1390.

## Rovnice

Přesně PROOF.md (4)–(12): V=A_y T_alg A_x na úplném X,
A_i=Ucal_i K_i Ucal_i, jeho úplná inverze, jedna příprava
S_0={r_x=r_y=eta=0}, přesný obraz S_1, invariantní Omega_alg a jednorázové
záznamy delta(g),delta(Mg). G'=Mg, D_C'=L5 D_C na S_0 a pokračování
čtené dynamiky na Omega_alg bez další přípravy. První syrový záznam se
obnovuje na konci T_alg a jeho čtverec se zachová po každém listu A_y.
Nejde o tvrzení ochrany uvnitř T_alg nebo čerstvých záznamů při opakování V.

## Kód a přijetí

Přijímá se nezměněný [PREREG-DRAFT.md](PREREG-DRAFT.md), SHA-256
`021a18883fa4c1dc0918f723aa7debc5d1c410ad42bb4c3a4f9893f8aa374515`,
v celém matematickém rozsahu, nulovém prahu a architekturních podmínkách.
Jeho historické označení návrhu nyní doplňuje ACCEPTANCE.md; žádná rovnice
nebo kontrola se nemění. Přesný přijatý verifier z notes commitu
`e4eaf10360dd758278a8e9c25cec2edcb7f5312a` má SHA-256
`bf693e33d5652141bf2367c6892e9c54d76a2f3a383aee19849747d1f17bae9f`.
Všechny runtime soubory, původní reporty a nové obaly váže PACKAGE.json.

Před tímto pinem jsou samostatně přijaty písemné důkazy i omezené verifiery
CONTACT a CW-ALG-1. Jejich přesné veřejné piny, přijetí, formální výsledky
a nezměněné dependency hashe určuje PUBLIC-DEPENDENCIES.json.
VERIFIER-PINS.json zůstává původním notes manifestem a nemění se.
Jeho historický stav není současnou přijímací dispozicí.

## Nosič, data a přesné množiny

X=F5^12×{0,1}, libovolné písty, q, obě r a bit. Nezměněný CHECK-MAP.md
určuje claim→funkci→množinu→důkaz. Skutečné konečné průchody jsou
25 položek P, 2500 úplných čtečkových řádků, 12000 bodů GL2/q,
125 Gramů, 1282 reduced slotů včetně dvou celých nulových větví,
32050 slotů s obsazenými r a 2400 prefixových hranic.
Symbolický přenos přes pojmenované invertibilní H klíče prochází čtyři
páry delta a osm oboustranných inverzních identit. Není to enumerace
všech q nebo nativní výpočet H_T; obecné tvrzení plyne z písemného důkazu.

S_1 se ověřuje jako deklarovaná množina právě tehdy, když úplná inverze
vrátí S_0, včetně obsazených výstupních referencí a neaktivního doplňku.
Skutečné mezifaktory obsahují změněné r_x. Stejné symbolické H se ruší
pouze při shodě celého klíče; žádné H se nenahrazuje identitou.
Konkrétní H_T je určeno přesnou syntaxí přijatého CW-ALG-1; obecný audit
invertibilního q-vlákna není jeho numerickým výpočtem.

## Systematiky, selhání a vrstva

Pouze přesná aritmetika F5 a pojmenované symbolické identity. Práh nula;
jediný protipříklad mapy, inverze, S_1, Omega, ochrany, počtu nebo vazby
zdroje znamená selhání. Bez oprav po pinu, reinterpretace počtů, nových
primitiv/registrů/resetů nebo obrovské expanze. Falsifikátor se zachová.
Pouze podmíněný L1 rozsah deklarované architektury, žádný fyzický lift.

## Běhový kontrakt

Před každým během obnovit aktuální STATUS/POLICY/AGENTS/CORE/FRONTIER,
autoritu a kolize. Zveřejnit celý pin na probe/P-RESIDUAL-RECORD-COMPOSITION-1
a přečíst všechny jeho bajty, až po doloženém přijetí obou závislostí.
Příkaz z kořene: **python3 probes/P-RESIDUAL-RECORD-COMPOSITION-1/verify.py**.
První místní běh na Linux CPython 3.12 má limit 600 s. Přesný raw stdout
poskytne jediný EXPECTED.txt; RUN.md obsahuje pin, prostředí, exit, počty
a otisky, RESULT.md rozsah a případný první falsifikátor.
Následují GitHub x86_64/aarch64 na témže PR headu, Python 3.12, shodné
runtime bajty, exit 0, prázdný stderr, byte-identical stdout a agregát check.
Nenulový exit nebo timeout se disponuje podle POLICY; frozen obsah se
neopravuje ani znovu nepoužije pod týmž identifikátorem.

Přijetí není během ani společným v100. Žádný původní report, kontaktní
kontrakt, Canon nebo vědecký status vlastníka se touto preregistrací nemění.
