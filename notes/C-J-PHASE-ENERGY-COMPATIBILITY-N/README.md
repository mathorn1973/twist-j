# Fáze, hodiny a energie: současný stav

PUBLIC / NON-CANONICAL / L1. Analytické závěry nejvýše candidate-T.
Autor: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Aktualizace: 2026-10-18 Europe/Prague.
Vlastník a diskuse: [#1603](https://github.com/mathorn1973/twist-j/issues/1603).
Návrh změn: [#1605](https://github.com/mathorn1973/twist-j/pull/1605).

**Společné fyzikální čtení fáze, energie a setrvačnosti zůstává otevřené.**
Přesné algebraické čtení pořadí kroků již existuje v Canonu. Doplněk níže
nově propojuje oba dodané návrhy přes přesné půlení klidové mince a rozvíjí
hlavní pokračování: zachovávaný operátor energie přímo ze stejného kroku.
Jeho fyzikální výběr ani původ v nativním U tím ještě odvozen není.
Současně zachováváme konečný poměr m/atan(m)>1 jako pracovní hypotézu
měřitelného rozdílu. Jeho odstranění limitou není povinným cílem.

| Část | Doložený rozsah | Hranice |
|---|---|---|
| Původní úplné oběhy | Důkaz a jediný audit: 9072 stavů, 252 oběhů; jen nulové univerzální afinní čtení plošného přírůstku jako energie modulo 5 | Konkrétní úplný nosič #1585; nejde o zákaz všech časových fází |
| Původní Diracovo porovnání | Přesná slupka a skupinový posun; pro doslovné fáze poměr hmotností m/atan(m)>1 | Parametr m není již změřená hmotnost |
| Diracova a alternátorová procházka | Přesná konjugace s Q=diag(1,-i), posunem vlnového čísla a časové fáze | Převést se musí i čtečky; původní P navíc obrací prostor |
| Galoisův a Lucasův řetězec | U_(phi^-n)(0)^2=U_(csch(n log phi))(0); pro liché n je druhý parametr 2/L_n | Přesná shoda v klidu; celé prostorové procházky nejsou totožné |
| Parita a kolmost žebříku | Kladná slupka vyžaduje opravu znaménka druhého kanálu; Galoisův krok má přesnou čtvrtotáčkovou reprezentaci a gamma(J)=(-j^3)J^-1 | Stopová kolmost energie a hybnosti není kolmostí klidové hmotnosti a hybnosti ani sama důkazem fyzikálního zákona |
| Hodiny z algebraického stavu | Kanonická celočíselná souřadnice k(J alpha)=k(alpha)+1, čitelná přesnými porovnáními | Fáze exp(i theta k) dovoluje každé zvolené theta |
| Torální návrh hodin | Existující kanonický Fourierův důkaz vylučuje netriviální stálý fázový přírůstek pro skalární Haarovu čtečku | Jiný nosič, míra, přidané hodiny či obecný kokyklus nejsou vyloučeny |
| Energie ze stejného kroku | Samoadjungovaný operátor H=r(U*-U)/(2i), H^2-P^2=m^2 I, přesná středová časová diference a zachování očekávání | Znaménko odpovídá fázi exp(-i omega t); H má obě znaménka spektra, zachování samo nevybírá fyzikální energii ani kontakt |
| Konečný algebraický krok | Za přesných předpokladů nelze současně ztotožnit doslovnou nenulovou fázi a hmotnost z křivosti při společné kalibraci | Algebraické musí být koeficienty celého kroku; nejde o zákaz všech konečných modelů |
| Konečná neekvivalence | Přesný kladný rozdíl A[m-atan(m)] zůstává předmětem fyzikální hypotézy | Vratný volný krok nedokazuje tření, spotřebu energie ani výrobu entropie |
| Více kontaktů v dosavadním rozvrhu | Přesný čtyřsložkový invariant vylučuje změnu q při libovolném konečném návratu do ker(F+I), kromě běžného volného znaménka | Jiný rozvrh a širší ponechaný nosič tím nejsou vyloučeny |

## Kde jsou důkazy

- [RESULT.md](RESULT.md), [PROOF.md](PROOF.md), [RUN.md](RUN.md): původní
  zmrazené závěry a skutečný první běh.
- [PROPOSALS.md](PROPOSALS.md): opravené návrhy, Lucasův řetězec a přesné
  půlení klidového kroku; rozlišení parity, Galoisovy konjugace, normy
  a stopové kolmosti včetně přesného účinku na fázi J.
- [CLOCKS.md](CLOCKS.md): existující kladné čtení hodin, torální hranice,
  zákaz prostého blokování a místní převod nelineární slupky.
- [ENERGY.md](ENERGY.md): hlavní pokračování, přesný operátor, hranice
  výběru energie, opravené lemma o transcendenci a hypotéza konečné
  neekvivalence včetně odlišení od tvrzené spotřeby za každý tik.
- [GUDERMANN-ADDITIVITY.md](GUDERMANN-ADDITIVITY.md): přesný zlatý
  násobitel poměru, komplementární Gudermannův úhel a podmínky, za nichž
  aditivita vybírá lineární fázi; oddělení prostorového dosahu a času.
- [CONTACT-KINEMATICS.md](CONTACT-KINEMATICS.md): přesný operátor posuvu,
  hranice kanonického čtení sin(k) a konkrétní místní kontakt, který
  propojí rezonanční módy s rozdílnou volnou sinusovou energií; pásmové
  průměrování, podmíněný výběr fáze a klasifikace společných zachování.
- [APPARATUS-BRIDGE.md](APPARATUS-BRIDGE.md): přímé porovnání s existujícím
  přístrojem; překážka pevného lineárního převodu klidových módů, přesný
  racionální Diracův krok s dělením pěti a meze společného účtu banky;
  konstrukce volného párového podprostoru s vlastním číslem -1 přímo
  v dosavadním F, důkazy jeho opuštění při uvedených kontaktech a zákaz
  netriviálního návratu přes libovolně mnoho skutečně rozvržených kontaktů.
- [FOLLOWUP_REVIEW.md](FOLLOWUP_REVIEW.md): oddělené posouzení doplňku,
  přesné otisky a rozsah kontroly.

## Autorita a skutečně provedené kontroly

Základ zůstává Public Canon v103, veřejný main a rozbalený tag
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, obsah
`01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`. Při pokračování byly ověřeny
všechny normativní otisky, návaznost obou commitů a úspěšné kontroly main
v běhu 39022927713. Prohlédnuto bylo všech 258 vzdálených větví a příslušné
otevřené úlohy. Staré přiložené interní verze nejsou současnou autoritou.

Původní veřejný předběhový pin je
`5389b000a6e5178ba99f45a611ebeb07e31051f8`; výsledek byl zveřejněn v
`14ce73995f376b295be6c18f296ac7d8ed2c2441`. Tento doplněk nemění žádný
z původních jedenácti souborů. Neopakuje audit, nezakládá novou formální
sondu a netvrdí dvouarchitekturní vědeckou reprodukci. Nové závěry jsou
analytické, s přiznaným předchozím seznámením s náměty. Běžné kontroly
repozitáře nejsou novým vědeckým během.

## Další konkrétní cíl

Hlavní větev je výběr energetického čtení H ze stejné úplné dynamiky.
Je třeba doložit přípustné předání energie při kontaktu, jeho úplný účet,
čtečku a odezvu na stejný prostorový posun a hodiny. Samotná komutace s U
nestačí: ENERGY.md uvádí celou rodinu jiných zachovávaných operátorů se
stejnou klidovou hodnotou a křivostí. Srovnání musí tuto volnost rozhodnout
nezávisle na požadované hmotnosti.

Vedle algebraické energie H zachováváme jako otevřenou fyzikální možnost
doslovné fázové čtení s konečným rozdílem mezi klidovou frekvencí a
setrvačnou odezvou. Rozhodnout je má stejný kontakt a čtení, nikoli
požadavek předem vynucené rovnosti. Výklad jako cenu za každý tik navíc
potřebuje skutečný účet měnícího se zásobníku; volný model ho neposkytuje.

Čtení k z existujícího normalizovaného skaláru je vhodný přesný vstup pro
budoucí konstrukci, s jeho již uvedenými předpoklady. Lucasovo číslo samo
nedokazuje návrat po L_n ticích. Větev se slabým krokem zůstává podmíněným
porovnáním, dokud nebude doložen její prostorový a časový převod z jednoho
úplného stroje. Vlastníci nativní přípustnosti #1586/#1589 a jejich kontrol
se nemění; denní souhrn má vlastní úlohu #1602.

Další směr je **kontakt respektující nativní krok**, s konkrétním zadáním
pro energetické čtení. [#1596](https://github.com/mathorn1973/twist-j/pull/1596)
na hlavě `a6d2b0d30b9d6703fffb15b187c58fa6ad71e229` již předává pod
#1589 výsledek STOP_UNTYPED: společný nosič, načtení, účet a úplná inverze
nejsou dodány. To není věta o nemožnosti a tento vlastník se nepřebírá.
Zdejší Hilbertův Diracův nosič a kontakt přidávají další výslovný typ.

Pro další porovnání potřebujeme od přijatého kontaktního modelu těchto
pět položek, určených před výběrem požadované energie:

1. Úplný stav a skutečný povolený krok, včetně nativního selektoru,
   obsazené paměti, odmítnutí a inverze; označení NATIVE nebo DECLARED-EXTENDED.
2. Jednu společnou přípravu přijímače, reference, banky a řadiče,
   nezávislou na zamýšleném výsledku.
3. Pojmenované čtení do porovnávacího nosiče, jeho obor a zachovanou
   informaci, stejný časový index a doloženou shodu skutečných kroků.
4. Úplný účet změn zdroje, přijímače, banky, reference a řadiče na
   téže historii; pouhá komutace s volným U0 ho nenahrazuje.
5. Rozhodnutí, zda povolený kontakt připouští zdejší kanál s celkovou
   fází pi a hodnotami 2m versus 2sqrt(1+m^2), a kdo případný rozdíl hradí.

Tyto položky zpřesňují rozlišovací otázku #1603; nejsou novou konstrukcí
nativního kontaktu ani převzetím #1398/#1498/#1589. Návratové hodiny
zůstávají vedlejší otázkou: čtení kroku již existuje a návrat konečného
checkpointu není návratem úplného stavu s rostoucím vnitřním čítačem.

## Přímé porovnání s hotovým kódem

Následné analytické porovnání již prošlo pod definice `F_step`,
`F_inverse` a `funded_contact_*` v
`probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py` na výše uvedeném
veřejném main. Volná matice a její inverze leží nad Z[1/6]. Klidové
Diracovy fáze pro m=2 a m=1/2 nesplňují nutnou spektrální podmínku.
Neexistuje proto pevný lineární převod zachovávající tyto módy, ani při
kladném celočíselném seskupování obou hodin. Zachování relativních fází
vylučuje i opravu společným skalárním násobitelem. Přesný rozsah včetně
pevných afinních kontaktních itinerářů je v APPARATUS-BRIDGE.md.

Kladná kontrolní konstrukce současně ukazuje, že racionální nosič stačí:
pro U=A/sqrt5 dává psi=x+sqrt5 y krok (x,y)->(A y,A x/5), s kladným
zachovávaným účtem ||x||^2+5||y||^2. Je to jiný výslovně zadaný krok,
ne odvození z dosavadního F či nativního U. Změna samotného typu banky
při nezměněném F proto věrný volný lineární převod neopraví.

Samotný párový kanál (0,pi)->(pi/2,pi/2) má na obou stranách vlastní
číslo -1, takže jej tato překážka **nevylučuje**. Následný důkaz jde dál:
v dosavadním F skutečně existuje čtyřrozměrný racionální podprostor
ker(F+I), popsaný vzorcem Z(q) v oddílu 9 APPARATUS-BRIDGE.md, se čtením
q=4A0. Je to přesné volné kódování; polohu, částicové energetické čtení
ani kontakt tím ještě neztotožňujeme.

Jediný nenulový přijatý kontakt funded_contact_* tento podprostor opustí
a samotné další volné kroky jej nevrátí. Jeho skutečná cena na Z(q) je
Delta=||a||^2/2-sigma*a^t*Pq/2.

**Netriviální návrat po více kontaktech je nyní pro skutečný rozvrh
vyloučen.** Dvě čtení R0=P^t*u+2(A0+B1) a R1=P^t*v+2(A1+B0)
si volný krok vymění; kontakt zachová R0. Řadič c proto vybírá přesný
invariant: R1 ve fázích 3 a 6, jinak R0. Na Z(q) je to až na znaménko
Mq, kde M=I+P^t*(2I+H_w)^(-1)*P je kladná a invertibilní. Libovolná
konečná historie s oběma konci v ker(F+I) tak má q_out=(-1)^N_F*q_in.
Při stejném řezu řadiče se q nemění vůbec, a to bez omezení počtu kontaktů,
volby původních štítků nebo banky. Při takovém návratu se obnoví i b a W;
mezilehlé výběry a splátky nejsou vyloučeny. Celý nativní stav se tím
nevrací: jeho čítač za každý úplný cyklus vzroste o pět.

Jeden úplný cyklus se do tohoto podprostoru vrátí právě tehdy, když jsou
oba skutečné vlnové impulsy nulové. Existence delších nenulových výletů
vracejících se do stejného bodu není rozhodnuta, ale jiný výsledný bod
v tomto pevném podprostoru už další opakování rozvrhu nepřinese.

Rozšířená racionální řídicí úloha s oběma paritami tiku má naproti tomu
dva dosažitelné směry uvnitř podprostoru. Tato přesná algebraická existence
nepředstavuje program sestavený z původních štítků a povolených kroků.
Další konstrukce musí ponechat i další vybuzené módy, nebo výslovně změnit
operaci či rozvrh chránící uvedený invariant. Oddíly 12–14 obsahují důkaz.

Také dosavadní bodový Hilbertův kontakt při g mimo 2pi Z opouští celý
volný sektor -1: ze vstupu (0,+;pi,+) do módu (pi/2,+;pi/2,-) s vlastním
číslem +1 přechází za jediný krok
s pravděpodobností sin^2(g/2)/L^2. Shoda volných fází proto nedává
uzavřený dvoustavový kontaktní stroj. Tato pravděpodobnost není tvrzením
o dlouhodobém rezonančním rozptylu. Převod polohy a kontaktu i úplný účet
zůstávají konkrétním otevřeným úkolem.

Dva požadované přírůstky 2phi^-3 a 2phi^-1 nelze vyrovnat jedinou
racionální bankou se společným lineárním měřítkem, pokud nic jiného
nekompenzuje změnu. Dvojice tvoří celočíselnou bázi účtu 2Z[phi]; to je
aritmetická možnost, nikoli povolení nového nativního přechodu.
