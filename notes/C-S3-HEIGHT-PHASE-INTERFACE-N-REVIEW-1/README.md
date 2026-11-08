# Slepý nezávislý posudek PR #1961 — fáze 1 (zmrazení)

## Co složka je

Nezávislý posudek podle protokolu posudků #1862/#1865/#1879 pro
`C-S3-HEIGHT-PHASE-INTERFACE-N` a jeho `CONSTRUCTIVE-3`
([PR #1961](https://github.com/mathorn1973/twist-j/pull/1961), hlava
`73f3cb4946b05f5d63aba1c279642f77c699caef`), psaný slepě z textů PR
(CONTRACT, PROOF, PREREG, README, SOURCES, REVIEW v obou složkách) a z
veřejných předchůdců v `main` (kontrakt stopek a fixture `WORD535.txt`
z `P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1`, důkaz a preregistrace
kopírovače a cyklu z `P-RELATIVE-CONTACT-WORKBANK-REUSE-1`).

- `PREREG.md` — zmrazený seznam kontrol R01–R15 s kritérii PASS/FAIL,
  konvence K1–K8, prohlášení o slepém režimu a expozici, plán fáze 2.
  Commitnuto samostatně jako `4f729be8eb372053d931ce1eb4a044f70fb8c3d6`
  před prvním spuštěním ověřovače.
- `review.py` — vlastní implementace od nuly: čistý stdlib, exaktní
  celočíselná aritmetika, dvě reprezentace násobení v `O = Z[j]`,
  `h` ze součinu, kontakt z definice s párovými invarianty na každém
  rozlišném přechodu, vlastní sestavení 95kontaktového slova z PROOF §2–§5,
  vlastní složení slova `S` z bloků (porovnáno kontakt po kontaktu s
  `WORD535.txt`), kopírovač `K` z `W6`, cyklus `A U_i A^-1` se SWAPy na
  nosiči `39+25k`, úplné invarianty stavu na hranicích, dekodér jen z
  archivů, úplná literální inverze, dva mutanty, vlastní BFS předchůdce.
  Čte jediný soubor, veřejný fixture `WORD535.txt` v `main`.
- `README.md` — tento popis.

## Slepý režim

Autorovy `search.py`, `verify.py`, `audit.py`, `assembly.py`, všechny
`*EXPECTED*.txt`, oba `SHA256SUMS`, oba `RESULT.md` a oba `RUN.md` nebyly
otevřeny, spuštěny ani použity jako očekávané hodnoty. Čísla uvedená v těle
PR a ve zprávě zadavatele (95, 15, 80, 19 cyklů, 2 597 775, 50, 114, 3790)
jsem znal; jsou proto kritérii, ne slepými predikcemi (PREREG §0).

## Jak se to pouští

```sh
env LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/review.py
```

Z kořene repozitáře. Exit 0 jen při úplném PASS R01–R14 (R15 je
pozorování), jinak 1. Výstup nemá cesty, časy ani platformu.

## Výsledek zaznamenaných běhů (fáze 1)

První spuštění skončilo `RESULT FAILURE` (R08, R10, R11, R12). Příčinou byly
dvě chyby mého kódu, ne vlastnost cíle: (1) konstanta ovládání starého
aparátu `u_old` byla zadána jako `1-j` místo `1-rho` (CONTRACT §1 PR
výslovně říká, že staré `u` je naše `B`); (2) čítač kontaktů R11 započítával
i kontakty použité při konstrukci stavů `Y_n` uvnitř běhu (o 102 více).
Obě opravy jsou čistě implementační; PREREG.md, kritéria ani fixtures se
neměnily. Druhé spuštění po opravě: exit 0, stderr prázdný, R01–R14 PASS,
`RESULT PASS`. Klíčová čísla, vše vlastním přepočtem:

```
R07 |A|=95 endpoints exact t=-2..2, cuts=2375, admitted_per_t=[30,36,37,38,44]
R09 S from blocks == WORD535.txt (535), |W|=5350 |W^-1|=21400 |K|=60 |U|=26870, K: 41/60 admitted
R10 W on all 10 ready cores == closed form; W^-1 restores
R11 14 cases, 19 cycles, boundaries=147, contacts=2597775, swaps=50, decode==input, inverse restores
R12 fresh archive pairs k,k-1,...,0
R15 OBSERVED bfs_result=INCONCLUSIVE reason=depth cap visited=12853 max_depth=6
FP_WORD      bfd48f0b8befb7c64f1b8a1b0f6589fc71a2120c87e63c9ba0ca21add2fe7b8d
FP_TRACES    075ca8281d2cb629f800e5e2ea3e9e49452159db915bbe2c76c09ffcae71863a
FP_ENDPOINTS 46b86040ef87c325d1417beb27546494c80b5d5706cb3e0e09c56bf7f023e549
FP_S         12f7a12e3969a2984dc5549cf42833512b906cc487ad45b96d705b278e842b6e
FP_FINALS    ba66ebc699ec5f0bfd9133597d920a9b2cb0a84bde4e8707737fa31612e4e954
```

Fingerprinty jsou hodnoty mé serializace (K6). `FP_S` se shoduje s
otiskem `Fingerprint[S]` nezávislého posudku #1879 v `main`
(`notes/C-RELATIVE-CONTACT-WORKBANK-REUSE-REVIEW-1/README.md`), který
používá tutéž serializaci slova; je to shoda dvou nezávislých složení
slova `S` z bloků, ne hodnota od autora PR.

## Rozsah a meze

Ověřeno strojem: celý 95kontaktový kompilátor na pěti deklarovaných
výškách včetně všech značek a zapisovačů, skutečné stopky `W=S^10` na
všech deseti připravených jádrech, kopírovač, všech 14 případů sestavy
(19 cyklů) s doslovným dopředným programem i doslovnou inverzí, dekodér,
formule zdrojů pro `k=1,2,3` z vlastních stavů. Obecný důkaz pro všechna
konečná `k` (indukce) a dyadické no-go kořenového PROOF §3 jsou ověřeny
jen čtením a konečnými instancemi, ne strojově. BFS předchůdce je
pozorování; autorův výsledek se porovná ve fázi 2. Nic se netvrdí o
přípravě vstupů, autonomním provozu, nativním U, fyzikální energii ani
o statusu v kánonu; kandidát zůstává NON-CANONICAL / L1, jak sám deklaruje.
