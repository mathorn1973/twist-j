# Slepý nezávislý posudek PR #1879 — fáze 1 (v109 jádro)

## Co složka je

Nezávislý posudek typu #1873 pro P-RELATIVE-CONTACT-WORKBANK-REUSE-1
(PR #1879, commit d6a5f77, slepý režim), psaný výhradně z textů PR:
PREREG.md, PROOF.md, README.md, RUN.md a PROVENANCE.md v
`probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/` a z řádku
RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T] v `/canon/CORE.md` (v108).

- `PREREG.md` — moje zmrazená preregistrace (kontroly K1–K9 s přesnými
  PASS/FAIL, vlastní konvence V1–V8, závazný rozsah běhu), sepsaná PŘED
  prvním spuštěním ověřovače.
- `review.py` — vlastní implementace od nuly (čistý stdlib, exaktní
  celočíselná aritmetika prstence O=Z[j] ve dvou reprezentacích, vlastní
  složení slova S z blokových definic PROOF.md §5, vlastní řízení stavu,
  cache přechodů POUZE s literálním přepočtem a povinnou dekompresí RLE,
  vlastní dekodér a fingerprinty dle mé serializace).
- `README.md` — tento popis.

## Nezávislost

Autorův `verify.py`, `EXPECTED.txt`, `WORD535.txt`, `RESULT.md`,
`SOURCES.tsv` ani historie gitu nebyly čteny, otevírány ani dohledávány;
v slepém checkoutu nejsou. Slovo S se neskládá z WORD535.txt, nýbrž
z bloků PROOF.md ř. 245–265. Shoda mého S s bytovým obsahem WORD535.txt
je proto v této fázi NEOVĚŘENA (bude předmětem porovnání po odhalení).
Program nic nečte ze souborů, nic nezapisuje a nepoužívá síť,
náhodu ani floaty.

## Jak se to pouští

```
cd /work/posudek
python3 review.py                # plný běh: 1000 trojic, dopředu i inverzně
python3 review.py --triples 100  # jen pro ladění: tiskne PARTIAL, končí 2
```

Návratové kódy: 0 jen při úplném PASS plného běhu, 2 při částečném
rozsahu (i když provedené kontroly projdou), 1 při FAIL.
Výstup tiskne status K1–K9, diagnostiky a fingerprinty.

## Výsledek zaznamenaného běhu (fáze 1)

Plný běh tady skutečně doběhl (zadání počítalo i s variantou,
že by byl drahý; nebyl):

```
K1..K9: PASS
executed_triples: 1000
RESULT: PASS (full), exit 0, stderr prázdný
Elapsed_seconds (operational only): 5.74  (opakovatelný běh 5.68)
Fingerprint[S]: 12f7a12e3969a2984dc5549cf42833512b906cc487ad45b96d705b278e842b6e
Fingerprint[forward]: 36b21644a315999b59fe9b917637779e190a14e2f5920ddbaf33eea90ebb5bdb
Fingerprint[aggregate_finals_first_1000]: a01988e7b7c61a37f40b8c6bc75588babe474b43eb1b83b8e581d95965f57b11
```

Fingerprinty jsou hodnoty MOJÍ serializace (konvence V8 v PREREG.md),
ne hodnoty autora; před porovnáním s autorem je třeba je převést.

## Rozsah a meze

Ověřeno strojem: deklarovaný k=3 nosič O^101, všech 1000 trojic
a jejich 1000 úplných inverzí (403 050 000 doslovných aplikací
kontaktu v inventáři; provedeno přes auditovanou RLE/cache cestu plus
literální bezcache průchod trojice 0), lokální identity kopírovače,
účty 290/8/248/42, svěží archivní dvojice 3,2,1,0, dekodér.
Konečný výpočet, ne obecná věta: trajektorie pokrývají jen k=3
a desetivstupovou rodinu. Obecné je jen maticové ověření formy Q
v K1 a dosazení formulí pro k; indukce pro libovolné konečné k
(PROOF §7) není mým během strojově ověřena a zůstává NEOVĚŘENA.
NEOVĚŘENO dále: shoda s autorovým WORD535.txt a s jakýmkoli
autorovým výstupem (slepý režim). Nic se netvrdí o nekonečném
provozu, fyzikální realizaci ani o statusu v kánonu.
