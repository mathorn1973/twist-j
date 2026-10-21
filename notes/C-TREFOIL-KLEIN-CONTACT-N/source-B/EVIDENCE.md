# Výsledky přesných kontrol a audit prvních běhů

**Celkový výsledek: PASS v deklarovaném rozsahu.**

Všechny tři nové implementace prošly při svém prvním vědeckém spuštění.
Nebyla potřeba změna cíle, oprava kódu nebo opakování. Zachovány jsou
první surové stdout, prázdné stderr a provozní záznamy jednotlivých
procesů. Výsledky jsou místní pomocné certifikáty analytické poznámky.

## 1. Pořadí zmrazení a běhů

| Událost | UTC, 17. října 2026 |
|---|---|
| Zmrazený společný kontrakt a čtyři přijaté podklady | 17:40:31.337548 |
| Připnuty všechny tři implementace, nezávislá analytická zpráva a spouštěč | 17:50:33.025980 |
| První spuštění geometrického autora | 17:50:37.123903 |
| První spuštění kontaktního autora | 17:50:37.142149 |
| První spuštění nezávislé implementace | 17:50:37.142223 |

Tři oddělené procesy proběhly souběžně teprve po připnutí všech zdrojů.
Nezávislý kontrolor při psaní svého programu nečetl nový autorský kód
ani jeho výstupy. Jeho analytický REVIEW.md byl rovněž připnut před
těmito běhy a zůstává beze změny; jeho označení NOT_RUN zaznamenává
právě tento dřívější okamžik.

Byly provedeny pouze předem popsané konečné kontroly. Vlastní univerzální
věty a geometrická existence zůstávají analytickými důkazy. Kontrola
syntaxe a výpočet hashů před zmrazením nebyly vědeckými běhy.

## 2. Skutečné výsledky

| Implementace | Výsledek | Splněné predikáty | Návratový kód | stderr |
|---|---|---:|---:|---:|
| Kontaktový autor, C0–C4 | PASS | 8 719 | 0 | 0 bajtů |
| Geometrický autor, F0–F6 | PASS | 83 | 0 | 0 bajtů |
| Oddělená implementace C0–C4/F0–F6 | PASS | 7 609 | 0 | 0 bajtů |

Počty predikátů závisí na rozdělení rovností v kódu a nejsou počtem
nezávislých experimentů. Některé kontroly se slučují do jedné rovnosti,
jiné testují jednotlivé části zvlášť. Rozhodující je shoda předepsaných
cílů a úplnost jejich analytického rozsahu.

### Kontaktní inventář

- 1 250 úplných řádků (delta,q_x,q_y,r_x,r_y) pro společnou konjugaci,
  páté mocniny a komutaci celých A_x,A_y.
- Dva celé záporné svědky, dohromady 84 doslovných listů, se skutečným
  W_b a všech 13 souřadnicemi. Výstupy přesně odpovídají zmrazeným
  (1,3,0,1) a (3,1,1,0) v souřadnicích q_x,q_y,r_x,r_y.
- 125 předepsaných pístových afinních řádků pro M a N, se všemi
  25 hodnotami q,r; přesně šest permutačních tabulek S3 a jejich
  uzavřenost. Všechny vstupní r jsou obsazenými plnými hodnotami.
- 750 řádků tvaru skutečných šesti generátorů, osm lineárních matic,
  deset zadaných unipotentních komutátorů a centralizátor jedné
  dvojité transpozice v A5.
- 35 afinních identit chi a dva pevné vstupy, které Ucal rozliší
  mimo tento faktor. Tvrzení pro libovolný čas se neodvozuje z
  konečné časové simulace.

### Geometrický inventář

Všechny části F0 až F6 prošly: základní identity, očekávaný záporný
determinant starého značení, C,D a jejich centra, kladné odrazy,
integrální Galoisův převod, koeficientové charaktery f a přesná
redukce modulo 1−j. Konkrétní forma f má 11 nenulových monomů.

Autor počítá v celočíselné bázi 1,j,j²,j³. Oddělený ověřovač používá
pětikoeficientový cyklický součin modulo součtový vztah. Polynomy
byly vytvořeny a dosazovány samostatně. Rovnosti se rozhodovaly
přesně, bez plovoucích tolerancí.

Přijatý řád H=120 se neopakoval novým vyčerpáním. Nové slovní
certifikáty C³=A, D²=B a (R1R2)^6=jI podporují analytický závěr
o celé G16 řádu 600. Vyšší Kleinovy formy a úplný invariantní okruh
zůstávají výslovně přijatým předchozím výsledkem.

## 3. Porovnání prvních výstupů

COMPARISON.json porovnává 19 společných položek zachycených výstupů.
Všech 19 se shoduje: celé kontaktní konce, M/N tabulky, S3 a řád
meridiánů, počty předem zadaných řádků, pístová lineární grupa,
centralizátor, chi svědci, záporný geometrický determinant, počet
monomů f a redukované C,D,Q.

Jde o porovnání už zachycených výstupů, nikoli o další vědecký běh.
Při převodu cyklotomických koeficientů se jen doplní nulová pátá
souřadnice; při převodu stavu se použije uvedené pevné pořadí
p_x,p_y,q_x,q_y,r_x,r_y,bit. Žádná fitovaná normalizace se nehledá.

## 4. Hashe zdrojů a prvních stdout

Společný PREREG:

`5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f`

FREEZE.json:

`7b6475aba1f5a4a48de043c7b7b6f7f6d6cb1432fee5389dd9620f5e6e521861`

IMPLEMENTATIONS.json:

`0c72e2ede19e9d60f836195eadd17ddfedd9161c3095db00d1d58fafd44f35ba`

| Část | SHA-256 kódu | SHA-256 prvního stdout |
|---|---|---|
| contact | f08be72c163003ae5cfbb9e48f1b9e907c3c4aa8febe25e33844d7cbd9063d14 | 67ffa8cd78c3dedfd53d06294e2bc825805fb8af0a88aae3e62ba8ad6fbc1d8f |
| geometry | 20c986a96c21cf46f9b17108514aa68ba13a33ac3c7c11a1ea912099eef30878 | a1de34c5ea1174a0d5a1a3229f6029153d327caf6c080160992ac94aefe102c9 |
| independent | dac53f0749d88900564c508fee3fe181dc1a4b82188e0211b411df8697c34468 | f14c67ac879142a3a3b83689d6e2380911dfb39be7bbd4cb4f83529a6f278111 |

stdout kontaktového autora obsahuje sedm řádků JSON objektů;
ostatní dva stdout tvoří vždy jeden JSON objekt. Surové soubory
zůstávají v původním formátu.

Prostředí všech tří běhů: Python 3.12.14, Linux x86_64. Přesné
příkazy, verze a časové údaje jsou v příslušných run.json.
Tato větev nebyla znovu spuštěna na aarch64 a nepředstavuje
veřejný dvouarchitekturní gate. Úspěšné veřejné běhy Canonu jsou
oddělený přijatý základ.

## 5. Dispozice důkazů

Předběžná nezávislá analytická zpráva nenašla blokující chybu a
nepožadovala změnu cíle. První přesné běhy i porovnání jejich
společných certifikátů následně prošly. Žádný první výstup, časový
údaj nebo autorský kód se po úspěchu nepřepisoval.

Výsledek poskytuje přesnou kontaktní konstrukci S3, univerzální
centrální mez pro vymezená úplná pevná slova a opravenou kladnou
geometrickou dvojici. Nativní připuštění dodané vazby nebo úplných
součtů a fyzikální protonový výklad nejsou závěrem těchto kontrol.
