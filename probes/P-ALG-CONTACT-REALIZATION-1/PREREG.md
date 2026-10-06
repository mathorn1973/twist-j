# P-ALG-CONTACT-REALIZATION-1 — formální preregistrace

NON-CANONICAL, L1. Přijetí existující předregistrace, 2026-10-06.
Vlastník `v100-algebra-review-20261006`, veřejná rezervace #1386, předloha #1389.

## Rovnice a přesný předmět

Předmět je výhradně původní SPEC.md / CW-ALG-1: konečné slovo
T_alg=Expand(CW-ALG-1(Pi_alg)), rho T_alg=Pi_alg rho a úplné
T_alg(f,q)=(Pi_alg f,H_T(f)q), H_T(f) v GL_2(F5), se syntaktickou úplnou
inverzí, zachováním obou r na konci a přesnou Omega_alg.
Pi_alg není původní lexikografická Pi. Složení A_y T_alg A_x není cílem této sondy.

## Kód a neměnné přijetí

Přijímá se [původní PREREG-DRAFT.md](PREREG-DRAFT.md) v celém rozsahu A–D,
architekturním kontraktu a nulových prahech, SHA-256
`fe924d5074700aeaabf427e3071844a65a407de37ed8e4335f115932a4eb587c`.
Její historické věty o budoucím verifieru a nepřijatém návrhu popisují stav
před přijetím; nynější dispozice je [ACCEPTANCE.md](ACCEPTANCE.md).
Žádná vědecká definice, konečná množina ani kritérium se tím nemění.

Přesné zdroje z notes commitu `a7c5d72a0ff0ab0af0b1de18ae3f18af134529d3`:
verify.py SHA-256 `115f6cae93934792a31178bd5b2ea630336ac7e43cf2abbeca8e2db0823222b0`;
compiler_identity_checks.py `54bb787eb9a222a5a7fe764863002b4490826c099ac3e599992a7d28ccbe04b7`;
SPEC.md `bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656`.
PACKAGE.json váže všechny soubory i jejich původ. SPEC, PREREG-DRAFT a pomocník
zůstávají sourozenci verifieru pod původními názvy potřebnými za běhu.

## Nosič, skutečné průchody a důkazní závislosti

X=F5^12×{0,1}; faktor F zapomíná právě q_x,q_y. Přesné konečné průchody,
symbolické identity a obecné důkazní závislosti rozlišuje nezměněný
[CHECK-MAP.md](CHECK-MAP.md). Závazné meze jsou jeho tabulky a původní
PREREG-DRAFT A–C, včetně 390625 pístových dvojic, 781250 pístových/bitových
stavů, 1280 nenulových redukovaných stavů a malých B3–B6 množin.
Odvozené počty dosažitelnosti nejsou počty enumerovaných stavů X.
Obecnou konstrukci pro celý konečný nosič nese SPEC a samostatný
PROOF-REVIEW, nikoli extrapolace malých tabulek.

## Systematiky a práh selhání

Přesná aritmetika F5, žádná statistika nebo náhodný výběr. Platí původní
priority, terminální homogenizace, A4, A18 a doslovné syntaktické inverze.
Jakákoli neshoda deklarované kontroly, počtu, podpory, orientace, atlasu,
inverze, domény nebo zdrojového otisku je selhání s prvním svědkem.
Tolerance je nula. Žádný audit nesmí být vydán za nativní provedení T_alg,
numerické určení H_T nebo identitu na q. Obrovská expanze a nové prostředky
jsou zakázány. Po pinu se kód, vstupy, rozsah ani prahy nemění.

## Vrstva a přesný běhový kontrakt

Pouze L1, podmíněně deklarovanou abecedou. Před každým během obnovit aktuální
STATUS/POLICY/AGENTS/CORE/FRONTIER, autoritu a kolize. Po přijetí zveřejnit
celý neměnný pin na probe/P-ALG-CONTACT-REALIZATION-1 a bajtově jej přečíst.
Příkaz z kořene je **python3 probes/P-ALG-CONTACT-REALIZATION-1/verify.py**;
historický adresářový příklad v CHECK-MAP není formálním RUN příkazem.
Místní Linux CPython 3.12, limit 600 sekund podle stávajícího runneru.
Jediný dokončený první běh poskytne surový EXPECTED.txt; RUN.md zachytí pin,
prostředí, exit, počty a otisky bez normalizace bajtů.
Následně tentýž PR head na GitHub x86_64 a aarch64, Python 3.12, shodné
runtime bajty, exit 0, prázdný stderr, shodný stdout a úspěšný agregát check.
Nenulový exit/timeout se řeší podle aktuálního POLICY bez opravy zmrazeného
balíku nebo opětovného použití identifikátoru. Výsledek nelze přejmenovat.

V okamžiku tohoto pinu nejsou tvrzeny provedené kontroly, PASS ani společné
v100. Původní reporty a vědecké statusy zůstávají zachovány.
