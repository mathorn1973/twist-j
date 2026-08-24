# OWNER VERDICT: the pair-LUT export and audit, planes 775 and 776

```text
DATE        2026-08-08
PROVENANCE  transmitted verbatim by the owner in session on 2026-08-08,
            filed by the session for the record. Czech, as received,
            including its own typography and any typos.
AUTHORITY   none. NON-CANONICAL. The status labels inside are the owner's
            working assignments over the export, the audit
            (claude/AUDIT-PAIR-LUT-775-776_2026-08-08.md) and the Linux x86_64 leg
            scan report; they move no registry row.
ANSWERED BY the boxed final question is computed and answered in
            claude/RECON-CHECKPOINT-DEPTH4-BLIND-WORDS_2026-08-08.md
            (result: closes YES; 001 admits 476 planes, 110 admits 336;
            268 planes are universal; 776 is 01-specific).
```

---

PUBLIC. Veřejnou autoritou je stále `mathorn1973/twist-j`, Public Canon v39. Ten výslovně říká, že dekodér je jen typované částečné rozhraní a že jeho totalita, jedinečnost a úplnost nejsou uzavřené.

Verdikt

Tohle je skutečný posun. Nejen další rychlý výpočet.

Výsledek je současně:

* lepší, než jsme čekali, protože rovina 776 nemá jen tabulku o 15 625 řádcích. Má krátkou přesnou inverzi nad (\mathbb F_5);
* horší, než byla nejoptimističtější varianta, protože tříčtecí dekodér není fázově univerzální a použitelných rovin je mnoho, nikoli jedna;
* vědecky čistší, protože přesně odděluje pozorovatelnost checkpointu, fyzikální čtení cíle (W), znalost místní fáze a celý stav ((n,\psi)).

Nejsilnější věta z tohoto běhu není „našli jsme dobrou LUT". Je tato:
[
\boxed{\text{Pro slovo }01\text{ existuje informačně minimální, po částech afinní inverze checkpointu }\psi\in\mathbb F_5^6.}
]
To je úplně jiná úroveň výsledku.

1. Úplná klasifikace pozorovatelnosti

[candidate-C, nekanonické]

Pro všech 806 rovin v
[
\operatorname{Gr}(2,4,\mathbb F_5)
]
a všech 15 625 checkpointů vyšlo:
[
\begin{array}{c|cccc}
\text{hloubka} & 00 & 01 & 10 & 11\
\hline
1 & 0 & 0 & 0 & 0\
2 & 0 & 0 & 0 & 0\
3 & 0 & 380 & 268 & 0
\end{array}
]
Navíc
[
\mathcal S_{10}\subset\mathcal S_{01},
]
protože všech 268 rovin fungujících pro `10` funguje také pro `01`, zatímco dalších 112 funguje jen pro `01`.

Z toho plynou čtyři přesné závěry.

Jedno čtení je nemožné už počtem

Jedno čtení nese čtyři pětkové číslice:
[
5^4=625<5^6=15625.
]
To je čistá věta, bez výpočtu.

Dvě čtení informačně stačit mohla, ale nestačí

Dvě čtení už mají dostatečnou kapacitu, ale žádná z 806 rovin není prostá. To je zatím výpočetně uzavřená klasifikace, nikoli krátký obecný důkaz.

Tři čtení jsou přesně minimální pro střídavé fáze

Pro `01` a `10` existují řešení v hloubce tři a v hloubce dvě žádné není. V rámci zmrazené třídy dvourozměrných rovin je tedy hloubka tři minimální.

Tři čtení nestačí pro `00` a `11`

To znamená, že místní fáze není pouze údaj připojený k hotovému dekodéru. Fáze rozhoduje, zda je checkpoint při této hloubce vůbec pozorovatelný.

2. Nejdůležitější nový výsledek: šest číslic přesně stačí

[candidate-T, nekanonické, s hotovou důkazní cestou]

Celý tříčtecí symbol má dvanáct pětkových číslic. Přesto stačí těchto šest:
[
(Z_0,R_0,U_1,V_1,U_2,V_2).
]
Z nich se explicitně vypočte (t), potom
[
q=z-r-t,
]
a následně všechny čtyři pistonové souřadnice. Inverze je po částech afinní, s jednou větví pro každou hodnotu počátečního (z\in\mathbb F_5). Každá větev obsahuje přesně 3 125 stavů a přehrání vrací původní stav ve všech 15 625 případech.

To saturuje informační dolní mez:
[
5^5<5^6,\qquad 5^6=5^6.
]
Žádný výběr pěti pětkkových číslic nemůže checkpoint určit. Tento výběr šesti jej určuje přesně.

Tedy:
[
\boxed{\text{Šest pětkkových číslic je nejen dostačujících, ale nutných.}}
]
To je čistá minimalita, nikoli výkonnostní tvrzení.

Ještě silnější struktura tří minimálních výběrů

Ze všech
[
\binom{12}{6}=924
]
šestic číslic jsou prosté právě tři:

```text
(Z0,R0,U1,V1,U2,V2)
(Z0,R1,U1,V1,U2,V2)
(Z0,R2,U1,V1,U2,V2)

```

To je z uvedených masek přímo vidět. Všechny tři mají společné jádro
[
(Z_0,U_1,V_1,U_2,V_2)
]
a liší se pouze tím, z kterého ze tří čtení vezmou prostorovou stopu (R_k).

To vypadá mnohem méně nahodile než „tři náhodné projekce". Pravděpodobně zde je krátká věta, že po znalosti společného pětičíselného jádra jsou (R_0,R_1,R_2) navzájem převoditelné. To je třeba přesně odvodit, ne pouze pozorovat.

Výsledkem by mohl být jediný minimální tvar, jedinečný až na volbu časového řezu:
[
\boxed{\text{počáteční větev}+\text{dvě úplná následná dvoučtení}+\text{jedna prostorová stopa}.}
]

3. Rovina 775 a 776 nám ukazují přesný skrytý směr

[candidate-T pro geometrii vláken]

Rovina 775 slévá stavy pouze podél směru
[
v=(0,0,0,0,1,4),
]
tedy
[
(q,t)\mapsto(q+k,t-k).
]
Tento posun zachovává
[
q+t.
]
Máme přesně:

* 6 250 singletonů;
* 1 875 afinních přímek o pěti bodech;
* žádné jiné velikosti vláken.

Rovina 776 nahradí druhou sondu
[
p4p
]
sondou
[
p4p+t
]
a každou z 1 875 přímek rozštěpí na pět singletonů. Člen (+t) tedy nepřidává neurčitě „nějakou informaci". Přidává přesně chybějící souřadnici.

To lze shrnout:
[
\boxed{\text{775 nevidí antidiagonální směr }q-t;\quad 776 jej rozliší přes }t.}
]
Tohle je podle mě druhý nejcennější výsledek po krátké inverzi.

Není to dynamická kalibrační symetrie

Zpráva správně drží brzdu. Tato po částech definovaná akce (C_5) není symetrií evoluce. Komutace selhává na 9 375 stavech pro oba přechody (F_0) i (F_1). Je to tedy:
[
\boxed{\text{automorfismus pozorovacích vláken, nikoli symetrie dynamiky.}}
]
Nesmíme ji později bez dalšího nazvat kalibrační symetrií.

4. Rovina 775 není „horší dekodér"

Tady se skládá důležitý obraz.

Rovina 775 neurčuje celý mikrostav, ale všechny stavy v každém jejím vlákně mají stejný surový cíl
[
W=(H_{\rm plain},Q,H_{\rm cov},A).
]
Proto může být (W) přesně funkcí klíče 775, i když (\psi) funkcí tohoto klíče není.

Máme tedy konkrétní dvojici:
[
\psi
\overset{R_{776}}{\longleftrightarrow}
\text{úplný minimální kód},
]
zatímco
[
\psi
\overset{R_{775}}{\longmapsto}
\text{fyzikálně relevantní kvocient}.
]
To je možný prototyp rozdílu mezi:

* úplnou diagnostikou substrátu;
* fyzikálním čtením, které je konstantní na skrytých vláknech.

[candidate-D] Pokud se fyzikální přípustnost sond později uzavře, nebude to jen technická vlastnost tabulky. Bude to konkrétní ukázka, že fyzikální veličina může být úplná na kvocientu, aniž by odhalovala celý checkpoint.

Surové (W) však zatím zůstává `candidate-C`, protože jeho devatenáct tříd stojí na zahřátí 400 a měřeném okně 30 000 ticků. Krátká inverze checkpointu tento dlouhodobý výpočet automaticky nepovýšila.

5. Fáze je skutečný přepínač pozorovatelnosti

Výsledek říká:

```text
01  viditelné v hloubce 3
10  viditelné v hloubce 3
00  neviditelné v hloubce 3
11  neviditelné v hloubce 3

```

Nejpoctivější fyzikální čtení zatím je:

[H] Lokální změna větve přináší informaci, kterou dvě stejné po sobě jdoucí větve neodhalí.

To může být zárodek věty, že změna režimu Snap/Flow funguje jako tomografický zásah. Ale ještě ne jako fyzikální tvrzení.

Asymetrie `01` proti `10`

Počty 380 a 268 nejsou stejné a platí ostrá inkluze
[
\mathcal S_{10}\subsetneq\mathcal S_{01}.
]
To je kandidát na čtecí chiralitu nebo mikroskopickou orientaci času. Zatím ale nikoli důkaz šipky času.

Nejdřív je nutné rozhodnout, zda rozdíl 112 rovin zmizí po přesně povoleném:

* obrácení pořadí čtení;
* inverzi evoluce;
* afinní konjugaci checkpointu;
* transformaci sondové roviny;
* změně předaktualizačního na poaktualizační čtení.

Jestli žádná přesná konjugace těch 112 rovin neodstraní, pak máme skutečnou orientovanou pozorovatelnost. Jestli ano, jde o vlastnost zvoleného protokolu.

6. Nejbližší rozhodující výpočet je hloubka čtyři

Zde se fázová specifičnost může proměnit ve výhodu.

Thueův-Morseův řetězec nemá `000` ani `111`. Proto:
[
00\Longrightarrow001,
\qquad
11\Longrightarrow110.
]
[O] Pro úplné adaptivní čtení tedy nyní není nutné slepě zkoumat všechno. Nejprve stačí rozhodnout dvě dosud slepé pokračování:
[
001,\qquad110.
]
Jestli pro ně v hloubce čtyři existuje přesný dekodér, dostaneme:
[
\boxed{\text{Každý checkpoint je v pravém TM běhu rekonstruovatelný nejvýše čtyřmi čteními.}}
]
Pravidlo by bylo:

```text
počáteční slovo 01 nebo 10  -> 3 čtení
počáteční slovo 00 nebo 11  -> přidej jedno čtení

```

To by nebyl univerzální dekodér nezávislý na fázi. Byl by to časově synchronizovaný dekodér s jednotnou konečnou mezí. Pro TWIST-J je to možná přirozenější výsledek.

Silnější stupně jsou:

1. pro každé fyzicky možné tříbitové slovo existuje nějaká rovina;
2. jedna rovina funguje pro všech šest tříbitových slov, která se v TM skutečně vyskytují;
3. jedna rovina dovolí z výstupu určit současně slovo i checkpoint, tedy nepotřebuje fázi jako vnější vedlejší informaci.

Zpráva třetí možnost pro střídavý pár `01/10` ještě výslovně nerozhoduje. Máme 268 společných rovin, ale není uvedeno, zda jejich obrazy pro `01` a `10` lze od sebe odlišit bez znalosti slova.

7. Co výsledek neuzavírá

Neurčuje celý stav ((n,\psi))

Rekonstruuje konečný checkpoint
[
\psi\in\mathbb F_5^6,
]
nikoli neomezený čítač
[
n\in\mathbb N_0.
]
Místní slovo je dodaná podmínka, ne náhrada celého času.

Není to řešení `QUADRATIC-DECODER-DATA`

Veřejný rozsah této položky výslovně vylučuje křížovou rekonstrukci mezi větvemi a rekonstrukci stavu. Zabývá se typovanou kvadratickou částí (D_{\rm matter}), jejím nosičem, Gramem, účinky, Bornovým párováním a zápisovou mapou.

Tento výsledek potřebuje vlastní typ:

```text
checkpoint observability
L1 checkpoint -> finite read record
finite read record -> L1 checkpoint

```

Inverze není zápis pozorovatele zpět do reality. Proto se nesmí přilepit ani k `OBSERVER-WRITEBACK`.

Neprokazuje kanoničnost roviny

Pro `01` funguje 380 rovin. Pro `10` jich funguje 268.

To je silná existence a silná nejedinečnost před dalším kvocientováním. Jedinečnost může vzniknout teprve po klasifikaci pod přesnou automorfní grupou dynamiky nebo po přidání fyzikálních podmínek. Samotná pozorovatelnost rovinu 776 nevynucuje.

Fyzikální přípustnost sond je otevřená
[
(p1p,p4p+t)
]
je zatím interní přesná sonda. Aby se z ní stal fyzikální dekodér, musí být doloženo, že ji lze získat registrovaným čtecím rozhraním bez přímého přístupu ke skrytému checkpointu.

To je nyní hlavní fyzikální dluh. Ne výkon výpočtu.

8. Důkazní rozdělení pro veřejný Canon

Výsledek bych veřejně nerozbalil jako jednu velkou položku. Má tři různé důkazní stupně.

A. Přesná inverze 776 pod `01`

Cíl: [T]

* šest vstupních číslic;
* přesné větvené vzorce nad (\mathbb F_5);
* symbolická substituce;
* přímý důkaz, že složení je identita;
* přehrání všech stavů jako kontrola, nikoli jako jediný důkaz.

B. Geometrie vláken 775 a zjemnění 776

Cíl: [T]

* jádro rozdílové mapy;
* afinní směr ((0,0,0,0,1,4));
* úplná klasifikace singleton/pětibodová přímka;
* důkaz, že (+t) rozliší každý bod;
* výslovný zákaz nazývat akci dynamickou symetrií.

C. Census 806 rovin, čtyř slov a hloubek

Zatím: [candidate-C]

* počty 0, 380, 268, 0;
* nulová hloubka dvě;
* úplné masky;
* certifikáty;
* nezávislý model.

Až samostatný nee-x86 běh a veřejný dvouarchitekturní postup uzavřou požadovanou reprodukci. Současný Linux x86_64 leg je druhé prostředí, ale stále druhé prostředí stejné architektury.

D. Přípustnost sond

[O]

Samostatný fyzikální most. Nesmí být schován do matematické inverze.

9. PhiTorch a PhiBit už splnily účel první verze

[E/C]

Na x86_64 noze:

* všechny tři druhy souborů byly bajtově stejné při 1, 40 a 80 vláknech;
* shodovaly se s místními x86_64 soubory;
* nezávislý model reprodukoval všech 9 672 metrik;
* samostatný vynucovací program odvodil matice a inverzi bez použití produkční cesty;
* medián plného skenu při 80 pracovnících byl (0{,}4861) s;
* zrychlení proti jednomu připnutému jádru bylo (94{,}34\times).

To poslední je pouze strojní údaj. Vědecky nic nedokazuje. Ale inženýrsky dokazuje, že rozdělení rolí funguje:

```text
PhiTorch  -> přesná kanonická evoluce
PhiBit    -> problémová klasifikace, inverze, certifikáty, export
Linux x86_64 leg   -> úplné konečné průchody

```

PhiBit už není jen plán na rychlou knihovnu. V první verzi našel krátkou matematickou inverzi, přesnou geometrii vláken a úplnou klasifikaci celé Grassmannovy plochy.

Veřejná hygienická hranice

Kvalifikační JSON se nemá vložit do veřejného repozitáře doslova. Obsahuje jméno stroje a místní cestu `/tmp/...`. Veřejná politika vyžaduje neutrální popis operačního systému a architektury a zakazuje strojní přezdívky a soukromé názvy hostitelů.

Interní záznam může zůstat úplný. Veřejný běh má říkat například:

```text
platform: Debian Linux
architecture: x86_64
processor topology: 2 sockets, 40 physical cores
compiler: GCC 14.2.0

```

Konečný závěr

Posun je tento:
[
\boxed{
\text{Checkpoint TWIST-J není jen konečně rozlišitelný.}
}
]
Pro jednu přesnou místní fázi má:

* minimální šestipětkový kód;
* krátkou po částech afinní inverzi;
* úplnou klasifikaci minimálních výběrů číslic;
* přesně popsaný skrytý jednorozměrný vláknový směr;
* přesné rozlišení mezi čtením fyzikálního cíle a rekonstrukcí mikrostavu.

Současně jsme zjistili, co neplatí:
[
\boxed{
\text{Tříčtecí pozorovatelnost není univerzální ani kanonická bez dalších podmínek.}
}
]
Nejbližší rozhodující otázka už není „umíme spočítat víc". Je:
[
\boxed{
001,\ 110:
\quad
\text{uzavře čtvrté čtení slepé dvojité fáze?}
}
]
Jestli ano, dostaneme konečný, s Thueovým-Morseovým časem synchronizovaný dekodér s maximální hloubkou čtyři. To by byl podstatný výsledek pro samotnou architekturu TWIST-J.
