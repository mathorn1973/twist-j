# Základní manifest fyzikálního popisu

**Stav dokumentu:** `NON-CANONICAL / PROGRAM NOTE / NO CLAIM / NO STATUS`

**Datum:** 2026-09-01

**Účel:** podklad pro veřejné posouzení před případným rámcovým foldem v75

## Autorita při sepsání

```text
STATE:           ACTIVE
CANON:           Public Canon v74
AUTHORITY:       mathorn1973/twist-j main
TAG:             canon-v74
TAG_OBJECT:      796b09aef958a9021b93cff0df7f300ef95f5337
TAG_TARGET:      05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT:  2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:    2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:     389246
BASE_MAIN:       8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
REGISTRY_ROWS:   352
SHA256SUMS:      5/5 OK
```

Tento soubor není Canon, axiom, věta, slovník, hypotéza ani otevřená
povinnost. Nevytváří identifikátor v `NORMATIVE.tsv`, řádek v
`REGISTRY.tsv`, závislost, gate, evidenci ani povolení k sondě. Veřejný stav
všech existujících položek zůstává přesně stavem v74.

## 1. Manifest

> Fyzická skutečnost je jeden uzavřený celek. Uvnitř tohoto celku existuje
> rozlišení a dění. Měření, záznamy i jejich posuzování jsou rovněž fyzikální
> děje uvnitř celku. Popis podléhá výslovným logickým pravidlům a rozlišuje
> skutečnost, tvrzení, pravdivost a ověření.

Jde o metodické vymezení předmětu fyzikálního popisu, nikoli o hotový
matematický model.

### 1.1 Jeden uzavřený celek

Fyzikální popis má jediný fyzický předmět. Systém, přístroj, záznam, paměť a
posouzení výsledku nemají být v rozhodujícím kroku přesunuty k fyzicky
účinnému pozorovateli stojícímu mimo popisovaný celek.

Slovo „uzavřený“ zde samo o sobě neznamená topologicky uzavřenou množinu,
konkrétní zákon zachování, determinismus, vratnost, diskrétnost ani absenci
užitečného řezu mezi systémem a přístrojem.

### 1.2 Vnitřní rozlišení a dění

Uvnitř celku musejí být dobře typovaným způsobem rozlišitelné alespoň některé
stavy, události, vztahy nebo záznamy. Musí být také určeno, co v dané
realizaci znamená následnost nebo změna. Manifest nevybírá množiny, algebry,
kategorie, historii, globální čas ani konkrétní zákon kroku.

### 1.3 Vnitřní měření

Měřený systém, přístroj, vazba, vznik záznamu, jeho uchování a případné
porovnání mají být objekty nebo procesy uvnitř stejné realizace. Pouhé
připojení vnější funkce, která po skončení přečte stav, ještě tento požadavek
neplní.

Řez „systém versus přístroj“ může být legitimní. Musí však být buď odvozen z
vnitřní struktury, nebo přiznán jako další přesně typované datum.

### 1.4 Skutečnost, tvrzení, pravdivost a ověření

| Rovina | Význam | Nesmí se ztotožnit s |
| --- | --- | --- |
| skutečnost | co se fyzicky děje | zápisem nebo modelem tohoto dění |
| tvrzení | formální nebo jazykový výrok | samotným děním |
| pravdivost | sémantický vztah tvrzení k jeho předmětu | pouhým důkazním zápisem nebo výsledkem přístroje |
| ověření | vnitřní postup tvorby a posouzení záznamu podle pravidel | pravdivostí samotnou |

Z manifestu neplyne úplnost, rozhodnutelnost ani neomylnost záznamu. Jazyk,
logika, sémantika a přípustné kroky ověření musejí být přiznané. Přechod mezi
jazykem objektů a jazykem, v němž se posuzují tvrzení o nich, nesmí být
skrytý.

## 2. Tři oddělená patra programu

### 2.1 Metodický rámec

Manifest stanoví, jaký druh popisu program hledá. Nevybírá číslo, těleso,
generátor, dimenzi, architekturu, dekodér, přístroj ani fyzikální míru. Stojí
mimo registr vědeckých tvrzení.

### 2.2 Konkrétní matematická konstrukce

Současný TWIST-J deklaruje konstrukci založenou na

\[
J=1+\zeta_5^2.
\]

Uvnitř této deklarované konstrukce zůstává `AXIOM-J` primitivním algebraickým
axiomem na vrstvě `FOUNDATION`. Žádná věta TWIST-J jej neodvozuje ani
neospravedlňuje. Architektura, čtení a přístroj nejsou automatickými důsledky
samotného zápisu pro \(J\).

Přesný budoucí nárok, že jedna úplně typovaná konstrukce založená na \(J\)
realizuje určené části manifestu, by byl samostatným fyzikálním tvrzením.
Nevzniká tímto dokumentem. Před případným cílem `H` musí mít alespoň:

1. formální realizační predikát;
2. přesný stavový nebo historický nosič a zákon dění;
3. složení systému, přístroje a záznamu;
4. pevné čtení a jeho obor i kodoménu;
5. fyzikální míru nebo četnostní pravidlo, pokud se tvrdí pravděpodobnosti;
6. měřitelný výstup a skutečný falsifikátor.

Bez těchto položek je „\(J\) realizuje manifest“ programový směr, nikoli
veřejná hypotéza.

### 2.3 Měření

Matematická bezespornost konstrukce sama nerozhodne, zda konstrukce odpovídá
našemu vesmíru. Měřicí patro musí předem určit veličiny, jednotky, přípravu,
výběr pokusů, vznik a uchování záznamu, chybový model, předpověď a podmínku
neúspěchu.

Měření může podpořit nebo vyvrátit konkrétní realizaci a její čtení. Nemění
manifest v matematickou větu.

## 3. Přímá axiomatická cesta

V rámci současného programu je legitimní tento postup:

1. přiznat \(J\) jako primitivní vstup deklarované konstrukce;
2. zmrazit architekturu a čtení před nahlédnutím do cílového výsledku;
3. odvodit přesné důsledky;
4. porovnat fyzikálně typované důsledky s měřením.

Tato cesta nepotřebuje dokazovat, proč bylo \(J\) vybráno, aby mohla přesně
zkoumat, co z deklarovaných vstupů plyne. Důsledek axiomu však nesmí být
vydáván za důvod axiomu.

## 4. Silnější selekční program

Samostatně lze zkoumat, zda nezávislá formalizace jednoty, vnitřního
rozlišení, dění a měření spolu s předem zvoleným principem jednoduchosti
vynutí třídu realizací obsahující \(J\).

Dobře typovaná úloha by měla tvar

\[
\operatorname*{Argmin}_{A\in\mathfrak A,\;P(A)}c(A)\big/\!\sim
=\{[A_J]\}.
\]

Zde musejí být před výpočtem zmrazeny:

- \(\mathfrak A\), úplná přípustná třída realizací;
- \(P\), formální překlad požadavků manifestu;
- \(c\), přesné pořadí nebo míra jednoduchosti;
- \(\sim\), relace stejnosti;
- \(A_J\), přesně typovaná cílová realizace.

Tento dokument žádnou takovou veřejnou povinnost nevytváří. Případný budoucí
cíl `O` smí vzniknout až po zmrazení uvedených položek, vlastní rozhodovací
podmínky a falsifikátoru. Neúspěch selekční větve by sám o sobě nevyvrátil
přímou axiomatickou větev.

## 5. STOP před slovem „vynuceno“

Nárok na minimalitu, jednoznačnost nebo vynucení se zastaví, pokud:

1. přípustná třída není přesně určena;
2. podmínky skrytě jmenují pětku, \(J\), cílovou dimenzi nebo cílový invariant;
3. není zmrazena ekvivalence, zejména Galoisova akce, orientace a inverze;
4. jednoduchost nemá předem dané přesné pořadí;
5. průzkum není úplný v deklarované třídě;
6. výsledek vybírá jen těleso či okruh, ale nárokuje architekturu nebo čtení;
7. čtení, přístroj nebo míra mohou být vybrány po spatření výsledku;
8. existují dva neekvivalentní minimizéry;
9. matematická selekce je vydávána za empirickou pravdu.

Úzké charakterizační věty o pěti mohou zůstat legitimní ve svých zmrazených
třídách. Podle veřejné poznámky `notes/AXIOM-NOT-DERIVED-2026-08-26.md` však
nejsou evidencí pro axiom. Axiom jedné konstrukce se smí stát větou silnější
metateorie pouze v nové, úplně typované úloze. Nesmí se tak stát přepsáním
významu již registrovaných vět.

## 6. Přesná hráz vůči v74

Současný `canon/CANON.md` říká v A0 „Reality is the closed integer J-Cayley
plenum“ a `canon/CORE.md` říká, že \(J\) je primitivní axiom. Manifest nelze k
těmto větám pouze připojit. Případný v75 fold musí:

- zúžit A0 na axiom deklarovaného kandidátního modelu;
- ponechat `AXIOM-J` jako primitivní algebraický základ konstrukce;
- nepředstírat, že fyzická adekvátnost nebo vynucení \(J\) už byly dokázány;
- neměnit stav, rozsah, evidenci ani falsifikátor žádného registrovaného
  tvrzení.

Přesný návrh tohoto slovního rozdělení je v
`notes/canon/PROMO-FOUNDATIONAL-SPLIT-V75.md`. Samotný tento manifest nic do
Canonu nevkládá.

## 7. Co manifest netvrdí

Manifest netvrdí:

- že vesmír je \(J\);
- že \(J\) je minimální, jediné nebo vynucené;
- že současná architektura byla odvozena z \(J\);
- že vnitřní měření, přístroj, kompozice či fyzikální míra jsou hotové;
- že matematický reversor je fyzikální časová symetrie;
- že invariantní míra je míra pokusů;
- že formální ověření je totéž jako pravdivost;
- že jedna matematická selekce sama určuje náš vesmír.

## Dispozice

Tento text patří pod `notes/` jako trvalý nekanonický programový rámec. Do
Canonu lze případně převzít jen krátké rámcové rozdělení po samostatném
review a release foldu. Konkrétní realizační a selekční tvrzení musí dostat
vlastní identifikátory, obory, falsifikátory a brány. Tento soubor jim
nepředjímá stav.
