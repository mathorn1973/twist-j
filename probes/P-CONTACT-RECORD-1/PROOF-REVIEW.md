# P-CONTACT-RECORD-1 — samostatná dispozice důkazního přezkumu

**NON-CANONICAL, L1. Samostatný statický matematický přezkum, 2026-10-06.**

**Dispozice: důkaz je přijatelný v přesně deklarovaném podmíněném L1 rozsahu.** Nenalezena blokující matematická chyba v úplném K_i, čtečce, inverzi, složení dvou záznamů, minimální referenci ani prefixové ochraně. Toto je doporučení k přijetí konkrétního důkazu, nikoli tvrzení, že veřejná autorita již důkaz přijala. Není to výsledek běhu ani veřejné PASS.

Přezkum proběhl odděleným přezkumným čtením a vlastním odvozením v téže agentní pracovní relaci. Nejde o externí institucionální nebo jinak externě nezávislý posudek. Hodnocené soubory nebyly měněny. Nebyl spuštěn ani importován verifier, jeho matematické funkce ani starší audity. Jediné úkony mimo čtení byly výpočet obsahových otisků a porovnání Git blobů; nejde o vědecké kontroly identity.

Tento záznam se týká pouze existujícího P-CONTACT-RECORD-1. Nezavádí čtvrtou definiční předlohu, nepřebírá Pi_alg/CW-ALG-1 a nepřezkoumává spojovací větu V=A_y T_alg A_x. Kontaktní kontrakt zůstává samostatný.

## Přesné přezkoumávané bajty a veřejný základ

Předmětem jsou celé [PROOF.md](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PROOF.md), [PREREG.md](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PREREG.md) a [verify.py](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/verify.py). Byly přečteny také podpůrné README, SOURCES a veřejný přezkumný obal, ale jejich starší výpočetní výsledky nejsou premisou níže uvedené dispozice.

| Soubor | SHA-256 přezkoumávaných bajtů |
|---|---|
| candidate/PROOF.md | `805137842d66894b36cc5cef17b45bf1c67b81570bf9eb8a4c77c9394d40abf5` |
| candidate/PREREG.md | `24a24ee5b055fec4b6a1cd6ebb5b4a3ffcec2e0e078b5f5937111e8a253ba4cd` |
| candidate/verify.py | `99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134` |

Pomocí surového `git hash-object --no-filters` byla ověřena shoda každé kopie s příslušným blobem veřejného notes commitu `8128286127f1a48b01ebda1a5c1e7a0d88d46095` v [PR #1388](https://github.com/mathorn1973/twist-j/pull/1388). Neměnné odkazy: [PROOF](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PROOF.md), [PREREG](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PREREG.md), [verifier](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/verify.py). Toto určuje předmět přezkumu, nikoli veřejný pin nebo přijetí věty.

Úplné původní mapy b,d,e byly porovnány s [veřejnými checkpointovými mapami Canonu v99](https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md#L577-L584), přečtenými z neměnného Git objektu tohoto commitu. Pořadí pístů a význam determinantového čtení odpovídají [pístovému reshapu](https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md#L2920-L2966). Normativní historický zdroj není tvrzením o aktuálním main; aktuální veřejnou autoritu a podmínky dalšího kroku ověřuje samostatná procedurální kontrola.

W_b, Ucal_i, jednorázová příprava a koncové čtení jsou **výslovné předpoklady přezkoumávaného rozšířeného přístroje**. Jejich slovo „přijaté“ v definici architektury není v tomto posudku změněno na tvrzení o odvození z původní abecedy, fyzické dostupnosti nebo již provedeném veřejném přijetí.

## Zkontrolovaný úplný kontaktní krok

Pro p=(p1,p2,p3,p4) označme R p=(p3,p4,p1,p2) a k=(2,1,3,4). Ze zdrojových map plyne b(p,q,r)=(-Rp,-q,-r), zatímco d,e mají shodnou pístovou a r část a liší se konstantou v q. Dvojí použití každé z b,d,e je identita na všech šesti souřadnicích; přímo e d vrací p,r a mění q na q+1. Inverze d e odečítá 1. Tyto identity nevyžadují připravené q ani r.

Přímé přepsání bilineárního h po B=b_x b_y zamění koeficienty3 a2, a tedy h(Bp)=-h(p). B je involuce na **celých obou buňkách**. Pro nenulové h platí sigma(-h)=1-sigma(h). Z toho je správná uvedená involutivita W_b na obou bitech: při nevybrané větvi je stav pevný; při vybrané větvi se další W_b vybere znovu a vrátí B i bit. Nulová větev je přesně identita.

Vlastním dosazením do obou větví jsem ověřil

\[
E_b=W_bBW_b=
\begin{cases}(Bp,Bq,Br,\eta),&h=0,\\
(p,q,r,1-\eta),&h\ne0.
\end{cases}
\]

Zápis Bq a Br zde znamená negaci obou komponent. E_b vrací h a je involuce. Pro tau_i=e_i d_i a pravostranné skládání má K_i=E_b tau_i E_b^-1 tau_i^-1 na h=0 q_i sled x→x−1→−x+1→−x+2→x−2. Ostatní q projde dvěma negacemi. Písty i r projdou B dvakrát; bit se vrátí. Na h≠0 E_b pouze přepíná bit, a proto s tau_i komutuje. Dostáváme na celém X

\[
K_i(f,q)=(f,q+3\delta v_i),\qquad
K_i^{-1}(f,q)=(f,q-3\delta v_i),\qquad K_i^5=I.
\]

Zkontrolováno bylo i pořadí všech dvanácti listů v PROOF a `contact_word`: pravý tau^-1, E_b^-1, tau, E_b se skutečně provedou v tomto pořadí. Jediná použitá změna pořadí je záměna disjunktních b_x,b_y, které komutují na úplném nosiči. Reverze vypsaného seznamu je úplnou inverzí, protože každý jeho list je involuce. Délka12 je doložená délka tohoto slova, nikoli minimum.

## Čtečka, obsazené reference a skutečná inverze

Každý řádek P_q je explicitní involuce; hodnoty3,4 fixuje. Vlastním dosazením všech pěti vstupních q jsem ověřil P_(q+3)P_q(0)=1 a P_qP_q(0)=0. Úplné aktivní řádky na r=0,1,2 jsou podle q buď cyklus `(0 1 2)`, nebo záměna `(0 1)`; přesně odpovídají tabulce PROOF. Není tedy dovoleno nahrazovat obecnou čtečku prostým nastavením r na delta.

Protože Ucal mění pouze r a h na r nezávisí, kontakt uvnitř dostává správnou původní delta. Jeho již dokázaný kontrakt platí pro **každou** dočasnou hodnotu r vytvořenou prvním Ucal. Pro s=3epsilon delta tím na celém původním nosiči přímo plyne

\[
(q_i,r_i)\longmapsto(q_i+s,P_{q_i+s}P_{q_i}(r_i)).
\]

Z výstupu (y,r') je inverze (y−s,P_(y−s)P_y(r')). Po sobě se ruší stejné involuce P_y a P_(y−s). Písty na konci zůstávají, takže delta lze při inverzi určit z výstupu. Listově jde o Ucal_i K_i^-1 Ucal_i, nikoli o druhé stejné použití čtečky. Při epsilon=0 nebo delta=0 je celá mapa skutečně identita, včetně obsazených r.

Význam r'=epsilon delta je přesný až na ready vrstvě r=0 a platí bodově pro libovolné neznámé q. Není předpokládáno rovnoměrné rozdělení q. Hodnoty3,4 během nativního kontaktu jsou přípustné: uvedený příklad q_i=2,r_i=0 dává po prvním Ucal r=2 a po následujícím e_i r=4. Vložená reference se proto po celou dobu správně účtuje jako původní F5 souřadnice.

## Dva záznamy a prefixová ochrana

Po úplném R_x jsou původní písty a eta obnoveny. R_y tedy používá stejnou delta, dostává skutečné obsazené r_x a jeho úplná koncová mapa mění jen q_y,r_y. Nebylo použito nahrazení r_x nulou ani příprava mezi kroky. Současné použití předchozí úplné mapy pro oba indexy dává Bcal=R_y R_x a inverzi R_x^-1 R_y^-1 na všech stavech. Pouze pro dva garantované výsledky se na začátku požaduje r_x=r_y=0. **Tato původní kontaktní věta nevyžaduje eta=0**; platí pro oba vstupní bity. Samostatné identity epsilon=0 stále obsahují oba listy Ucal.

Prefixový argument jsem zkontroloval zvlášť od koncové mapy. V celé druhé čtečce mohou r_x měnit pouze b_x a vybraná větev W_b; obě změny jsou negace. Ucal_y,d_y,e_y,b_y r_x fixují. Proto každý povolený list zachovává r_x² na libovolném úplném vstupu a indukce dává invarianci pro každý prefix včetně prázdného. Stejná množina involutivních listů dokazuje tvrzení i pro každý prefix inverzního seznamu.

Po prvním dokončeném ready zápisu tedy první čtení zůstává epsilon_x delta po každé diskrétní hranici druhé čtečky. Syrové r_x může kolísat: nulový svědek po R_x dává q=(3,0),r=(1,0); pátý list druhé čtečky b_x dává4, dvanáctý b_x vrací1. Jejich čtverce jsou vždy1. Toto jsem zkontroloval přímo v pořadí listů. Obecný obor r_x² je `{0,1,4}`, nikoli pouze bit.

Prefixové tvrzení nekontroluje vnitřek fyzické realizace W_b a nevytváří nový dynamický list „umocni r“. Stejně tak nevytváří invariant pod d_x,e_x,Ucal_x. Ochrana prvního záznamu a vznik druhého záznamu jsou rozdílné vlastnosti; původní důkaz je nezaměňuje.

## Minimum a negativní hranice

Dolní mez tří samostatných referenčních stavů je platná přesně v deklarované jednovolací klasické vratné třídě. Po libovolném společném vratném kodéru má S velikost25. Výsledky identity a translace +3 vyžadují S∩T(S)=∅, jinak by tentýž dekodér musel jeden úplný vstup rozlišit dvěma výsledky reference. Na Q×A je5m disjunktních pěticyklů; z každého lze vybrat nejvýše dva nesousední body. Tedy25≤10m a m≥3. Krok+3 je po přeznačení právě pěticyklus, takže použití C5 ve verifieru je správné. Výslovná tabulka P_q poskytuje horní mez m=3. Argument nijak nepředstírá minimum pro jinou paměť, více volání, jiný nosič nebo fyzický přístroj.

Z Ucal²=I přímo plyne R_1^n=Ucal K_i^n Ucal a R_1^5=I. Uvedené smazání při druhém aktivním použití z `(q,r)=(0,0)` přes `(3,1)` do `(1,0)` je správné. Holý K_i má jiný koncový účinek na referenci než opakovaný celý reader.

R_0=I na úplném stavu znamená přesnou nerozlišitelnost nepoužití a dokončeného nulového experimentu bez dalšího údaje o dokončení. Reset neznámého výsledku0/1 do0 při zachování ostatních dostupných údajů by sloučil50 stavů do25; není bijekcí. Inverze skutečného experimentu obnovuje také q a odstraňuje záznam, takže není restartem se zachovaným archivem. Tvrzení o nedostatečnosti jediného čtení pouze před/po kontaktu platí v téže třídě s libovolným q a pevnou referencí. Žádná z těchto hranic není použita jako nevymezený zákaz jiných architektur.

## Statické posouzení verifieru a evidenční hranice

Celý `verify.py` byl čten, nikoli spuštěn. Zkontrolovány byly přímé mapy, datové pořadí, větvení z aktuálního h/eta, pořadí slov, skutečné reverzní inverze, nezávislá implementace P přes záměny a skládání ze skutečného mezivýstupu.

Redukce na malé kontrakty je oprávněná: explicitní afinní identitu buňky určuje nula a šest bází; bilineární identitu h(Bp) určuje16 dvojic bází. Parita B sleduje plný pístový účinek a čtyři afinní dvojice koeficientů sledují obě q i obě r. Nejde o pouhou kontrolu K na reprezentativním q=0. Žádná kontrola původního autonomního U nebo entropie není importována.

Rozsahy ve zdroji a preregistraci jsem ověřil odvozením počtů:35 afinních řádků;16 bilineárních párů;13 úplných afinních bázových řádků pro komutaci;20 větvových řádků W/E a40 symbolických K;60/100 řádků tritové/vložené čtečky;5000 úplných q/r vstupů dvou čteček. Pět pevných pístových párů dává25000 doslovných kompozic,225000 hranic druhé čtečky včetně prázdného prefixu a1000 ready případů. Tyto počty jsou přezkoumané meze kódu, **nikoli výsledky jeho provedení**. Velký původní nosič není vydáván za enumerovaný.

Přijatelný matematický důkaz se neopírá o budoucí PASS těchto tabulek. Naopak budoucí výpočetní evidence musí nést vlastní pin, skutečné výstupy, průchod obou veřejných architektur a aktuální procedurální schválení. Doporučení autora přijmout určité verifiery není automaticky veřejným přijetím této písemné věty.

## Konečná dispozice

Pro tento přesný podmíněný L1 kontrakt doporučuji **přijmout důkaz bez změny jeho rozsahu**. Nezůstává nalezená matematická překážka vyžadující opravu původního PROOF. Doporučení zahrnuje úplnost map/inverzí na X, oba vstupní bity, neznámé q, obsazené r, jednorázový význam ready záznamů, přesnou třídu minimální reference a omezenou listovou ochranu.

Nadále se samostatně dokládá veřejné přijetí, piny a formální C evidence podle aktuálního repozitáře. Tento posudek nemění Canon, status vlastníků, přijatou architekturu ani rozsah jiných sond; nedokazuje fyzický kontakt, detektor, energii, teplotu, křivost nebo Landauerův vztah. Případné pozdější společné začlenění v100 nesmí zpětně rozšířit tuto kontaktní preregistraci.
