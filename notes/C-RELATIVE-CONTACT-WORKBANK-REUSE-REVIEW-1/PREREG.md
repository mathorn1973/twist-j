# Nezávislý slepý posudek PR #1879 (P-RELATIVE-CONTACT-WORKBANK-REUSE-1), fáze 1
## Zmrazená preregistrace vlastního ověřovače — sepsáno PŘED prvním spuštěním review.py

Stav: NON-CANONICAL posudek. Nic zde nemění status v kánonu a nic netvrdí
o nekonečném provozu ani o fyzikální realizaci.

## 0. Nezávislost a zdroje

Jediné vstupy posudku (cizí text, ne závazné pokyny):
- `probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/PREREG.md` (dále A-PREREG),
- `probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/PROOF.md` (dále A-PROOF),
- `probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/README.md`,
  `RUN.md` (jen pin/hash metadata; autorův výsledek se NEPŘEJÍMÁ),
  `PROVENANCE.md` (jen expozice) — vše v checkoutu PR #1879,
- kánon ke čtení: řádek RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T]
  v `/canon/CORE.md` (v108 předchůdce na O^56, účet 156); status se nemění.

NEČTENO a nepoužito (skryto v slepém režimu): autorův `verify.py`,
`EXPECTED.txt`, `WORD535.txt`, `RESULT.md`, `SOURCES.tsv`, historie gitu.
Slovo S se proto neskládá ze souboru WORD535.txt, ale z blokových definic
A-PROOF ř. 245–265 (PROOF sám říká ř. 208–211, že definice souhlasí
s deklarovaným WORD535; shoda mého S s bytovým obsahem WORD535.txt
a s jeho SHA-256 z A-PREREG ř. 48–49 je v této fázi NEOVĚŘENA).

Každá kontrola níže srovnává proti mé NEZÁVISLÉ cestě: vlastní výpočet
z definic (A-PREREG ř. 31–43, A-PROOF §1–§8), uzavřené formule pro
koncové body, druhá aritmetická reprezentace, nebo statická podpora slova.
Nikdy proti autorovu souboru či výstupu.

## 1. Zmrazené konvence posudku (moje volby; při porovnání s autorem je třeba je převést)

V1. Prstenec: prvek O=Z[j] jako čtveřice celých čísel (a0,a1,a2,a3)
    v bázi (1,j,j^2,j^3), 1+j+j^2+j^3+j^4=0.
V2. Kontakt C(i,k) bere za první argument slot i, za druhý slot k;
    (+rho*d) dostane první slot. Slova běží chronologicky zleva doprava,
    adresy nulové (A-PREREG ř. 45–46, A-PROOF ř. 15–16).
V3. Slovo S skládám POUZE z bloků A-PROOF ř. 247–261 (O1, A0, Bc=C(c,9),
    O2=C(9,10), E_c, E_c^-1 doslovně jak psáno, L_p, SCAN_q s p rostoucím,
    W_A, W_B, D včetně posledního C(9,c), V, R, F, F^-1, T). F=C(0,1)C(1,2).
    Literální inverze slova: obrátím pořadí a každý kontakt nahradím čtyřmi
    týmiž kontakty (A-PREREG ř. 50–52); SWAP zůstává SWAP.
V4. Kopírovač: W6 je jednoznačně (one-based) řetězec z A-PREREG ř. 56 /
    A-PROOF ř. 99; místní místa 1..6 mapuji pro p=0..4, q=(p+1) mod 5 na
    (a+2p, a+2p+1, a+2q, a+2q+1, t+2p, t+2p+1) (A-PREREG ř. 58–60,
    A-PROOF ř. 143–144). K(a,t) řadí moduly p v rostoucím pořadí.
V5. Fáze h=0,1,2: archivy t_h=31+20h a t_h+10 (A-PREREG ř. 64);
    cyklus je W K(11,t_h) K(21,t_h+10) W^-1 (A-PREREG ř. 65–67).
    Po fázi h=0 a h=1 pět SWAPů (i, 91+5h+i), i=0..4 v rostoucím i
    (A-PREREG ř. 69; A-PROOF ř. 413–417 tutéž výměnu značí Pi_1, Pi_2).
    SWAPy v jednom bloku působí na disjunktní sloty, jejich vnitřní pořadí
    je tedy volba bez vlivu na výsledek; přesto ji zmrazuji takto.
V6. Indexy: Y modulo 9, X modulo 5, značky bank M[p] modulo 5;
    -r značí třídu mod 5; Delta_0=1, Delta_1=8, ve značkách tedy
    M[-r-Delta_1]=M[-r-3] (A-PREREG ř. 104, A-PROOF ř. 506–510).
    Po W je zdroj Y_(s+10) tedy Y_(s+1 mod 9), hodiny X_(r+10)=X_r
    (A-PREREG ř. 106 říká X_(r+10), A-PROOF ř. 356 totéž zjednodušeně X_r).
V7. Výčet vstupů a trojic: vstupy L=[(s,r) pro s=0,1 a uvnitř r=0..4],
    index vstupu = 5s+r. Trojice mají index (i0*10+i1)*10+i2 a běží
    v tomto přirozeném pořadí. Částečný běh s N<1000 běží prvních N trojic
    v tomto pořadí (tedy první vstup je v trojicích upevněn na (0,0);
    pokrytí všech 10 vstupů jako první fáze pak nese samostatný audit U,
    viz K4 — toto zkreslení částečného pokrytí výslovně přiznávám).
V8. Serializace (pouze moje): prvek = "a0,a1,a2,a3" (desítkově, znaménko `-`
    pro záporné); stav = jeho sloty v rostoucí adrese spojené znakem `;`,
    bez ukončovacího nového řádku; slovo = tokeny "C{i},{k}" resp.
    "S{i},{k}" chronologicky spojené `;`. Fingerprint = SHA-256 (hex,
    malá písmena) nad ASCII bajty serializace. Agregátní fingerprint
    koncových stavů = SHA-256 nad spojením serializací finálních
    (dopředných) stavů provedených trojic v pořadí V7, každá ukončená `\n`.

## 2. Kontroly (přesná PASS/FAIL; každá tiskne PASS/FAIL; tolerance 0)

### K1 — aritmetika prstence a funkcionál účtu z definic
Nezávislá cesta: (a) druhá reprezentace pěti koeficientů (cyklická konvoluce,
j^5=1) s vlastním kontaktím pravidlem; (b) maticový test kvadratické formy.
Def. z A-PREREG ř. 31–36 a A-PROOF ř. 20–35, 39–47, 49–58.
PASS: Q(u)=5, Q(w)=3, Q(b)=3; matice R násobení činitelem rho splňuje
R^T A R = A pro A formy Q (diag 2, mimo -1/2) a R^5=I (obecný, ne vzorkový
fakt o formě); na všech párech (a,c) z koeficientového boxu {-1,0,1,2}^4
(256 prvků, 65 536 párů) se obě reprezentace na kontaktu shodují přesně,
C^5=id, C^4 je inverze, diagonální a nepřijaté páry jsou pevné, a platí
Q(a)+Q(c) zachováno, součet zachován, epsilon každého slotu zachován;
na boxu {-2..2}^4 platí Q(rho z)=Q(z) a rho^5 z = z pro všech 625 z.
Dále: po hlavních bězích se každý ROZLIŠNÝ pár, který se v trajektoriích
skutečně vyskytl, přepočte literálně (včetně invariantů) — to pokrývá
použitou pár-množinu úplně, ale obecný primitivní invariant se hlásí jen
v rozsahu maticového faktu a těchto úplných enumerací, ne jako strojový
důkaz pro všechna O×O.
FAIL: kterákoli neshoda.

### K2 — nosič 101, příprava, účet 290 a zachování pod povolenými kroky
Z textu: A-PREREG ř. 77–91; A-PROOF ř. 213–243, 462–464, 472–492, 494–498.
PASS: příprava každého provedeného uspořádání má právě 101 slotů
(0..4 vstup, 5..10 ovládání (0,u,0,0,w,0) účet 8, 11..20/21..30 dvě pracovní
banky, 31..90 šest archivních, 91..95/96..100 dva zásobníky);
účet vstupu 14, prázdné banky 30 (každá z 8), jádra 82, pomocných 86 slotů
248, celkem E=290 a součet Sigma=(8,0,0,0), rezidua dle A-PROOF ř. 494–495.
Na každé kontrolní hranici provedených trajektorií (start, po W, po každém K,
po W^-1, po SWAP-bloku, finále, po plné inverzi) je E=290, Sigma stejný a
vektor označených reziduí stejný jako na startu; rezidua vyměňovaných dvojic
jsou těsně před každým SWAPem stejná. Zachování uvnitř kroků nesou K1-ověřené
použité páry a záměna celých slotů. FAIL: jakákoli odchylka.

### K3 — šest trvalých archivních bank, role, záznamy mimo pracovní banky
Z textu: A-PREREG ř. 64–73, 78–79, 98, 108–118; A-PROOF ř. 403–406, 431–432,
452–453, 503–516.
PASS: šest bank bází 31,41,51,61,71,81; staticky z (mého) slova: žádný
primitiv za dokončením vlastního K archivní banky se té banky nedotýká,
a žádná fáze se nedotýká archivů jiných fází ani zásobníků (jen SWAP-blok
svého zásobníku). V provedených trajektoriích: archivy dříve dokončené
jsou na všech pozdějších hranicích bajtově stejné (stejný obsah slotů),
finálně je každá archivní banka platná M[p] (nikoli prázdná), zatímco obě
PRACOVNÍ banky jsou finálně M_empty. Dekodér, který smí číst POUZE šest
archivních bank (přesná shoda s M[p] vzory; prázdná/neplatná = odmítnutí),
vrací u každé trojice právě (a-a') mod 5 v {1,3}, s=0 pro 1, s=1 pro 3,
r=-a, a obnovená trojice se rovná zadané. FAIL: dotek, změna, špatné umístění
záznamu, dekódovací chyba/kolize.

### K4 — tři navazující pokusy na týchž dvou pracovních bankách, správný výstup každý
Z textu: A-PREREG ř. 11–14, 100–107; A-PROOF ř. 342–361, 365–384, 446–450.
PASS: jeden fixní program pro všechny trojice (žádná volba podle vstupu;
ověří se, že slovo je jedno a totéž); u každé provedené trojice a každé fáze
se po W pracovní banky rovnají (M[-r], M[-r-Delta_s]) a zbytek jádra uzavřené
formuli A-PROOF ř. 355–356, po obou K archivy nesou tutéž dvojici a do
W^-1 vstupuje přesně celý stav po W. Samostatně totéž U pro všech
10 vstupů (nezávisle na počtu provedených trojic). Finální stav se po
složkách (celých 101) rovná uzavřené formuli A-PROOF ř. 446–450 pro k=3.
FAIL: kterákoli složka/fáze.

### K5 — obnova pracovních bank, zdroje, hodin i ovládání po zápisu a kopii
Z textu: A-PREREG ř. 93–98, 107, 112–113; A-PROOF ř. 169–173, 386–390,
429–436.
PASS: po každém pětimodulovém K i na všech pěti 12kontaktových hranicích
modulů se zdrojová (pracovní) banka rovná své podobě před K; po každém
W^-1 se všech prvních 31 slotů rovná připravenému jádru dané fáze (zdroj Y_s,
hodiny X_r, ovládání (0,u,0,0,w,0), obě pracovní banky M_empty) — tedy
počáteční, ne dopředu-vyvinuté hodnoty. Po SWAP-bloku je v jádře další vstup
v původní přípravě a právě vyprázdněný zásobník nese obnovený předchozí vstup.
U kopírovače se obnova tvrdí jen na hranicích modulů, ne uvnitř
(A-PREREG ř. 107–108). FAIL: jakákoli složka.

### K6 — plná inverze existuje a vrací úplný stav
Z textu: A-PREREG ř. 70–71, 109–110, 120–121; A-PROOF ř. 175–179, 360–361,
457–460.
PASS: literální inverze celého dopředného programu dle V3 má 322 440 kontaktů
a 10 SWAPů; použita na skutečný finální stav každé provedené trojice vrací
úplný 101slotový počáteční stav včetně pořadí vstupů a šesti prázdných
archivů; stejně inverze K (240 kontaktů) na 20slotech a inverze W (21 400).
Zároveň se nadále tvrdí jen to, co text říká: tato inverze záznamy maže,
není to reset se zachováním záznamů (A-PREREG ř. 120–124).
FAIL: jakákoli složka či délka.

### K7 — uznaná historie spotřebovává čerstvou archivní kapacitu (vyčíslit)
Z textu: A-PREREG ř. 122–124, 168–172; A-PROOF ř. 477–481, 518–537.
PASS: zásoba čerstvých archivních DVOJIC na dopředných hranicích
(po etapách U_0,U_1,U_2 včetně startu) je přesně 3,2,1,0. Každá uznaná
historie jednoho pokusu spotřebuje 2 čerstvé archivní banky = 20 slotů
o přípravném účtu 60; tři pokusy 6 bank = 60 slotů o účtu 180 (placeno
v přípravě 290, ne „spalováno" — účet se zachovává, K2). Obecné formule
z A-PROOF ř. 479–481 pro k: slotů 26+25k, E 68+74k, svěžích bank 2k —
ověřuji jen algebraickou dosazovací shodu pro k=3 (101, 290, 6) a
kapacitní aritmetiku 5^4=625 < 1000 <= 5^5, konstrukce dává 6 bank;
údaje pro obecné k nad rámec k=3 jsou v tomto posudku konečný výpočet
formulí, ne strojová trajektorie. FAIL: jiný počet/čas spotřeby.

### K8 — počty 1000/1000, 403 050 000 kontaktů, rozložení
Z textu: A-PREREG ř. 62, 70–71, 83, 136–147; A-PROOF ř. 157–159, 263–265,
353, 370–372, 457–468.
PASS (aritmetika z mých doslovně složených slov, ne z textu): |L_p|=10,
|SCAN|=80, |E_c|=10, |W_A|=|W_B|=105, |D|=9, |V|=23, |R|=261, |S|=535,
|W|=5 350, |K|=60 (přijatých 41 ze 60 na každém platném značkovém vstupu,
podle případu 6+5+3*10), 12kontaktový modul přijetí 10/6/5 se přijímacími
slovy z A-PROOF ř. 114–118, |W^-1|=21 400, |U|=5 350+60+60+21 400=26 870,
celý program 3*26 870=80 610 kontaktů + 10 SWAPů, inverze 322 440 + 10.
Množina trojic má 10^3=1000 prvků; hlavní inventář tedy představuje
1000 dopředných (80 610 000 kontaktů, 10 000 SWAPů) + 1000 inverzních
(322 440 000, 10 000) = 403 050 000 kontaktů a 20 000 SWAPů.
Trajektorově se z toho v této fázi skutečně projde objem podle
zmrazeného závazku v §3; samotná čísla se počítají i při částečném běhu.
FAIL: jakákoli délka či přijetí.

### K9 — fingerprinty slova a hranic podle MOJÍ serializace (konvence V8)
PASS: program tiskne SHA-256 pro S, W, K(11,31), celý dopředný program,
jeho literální inverzi, počáteční a dopřednou finální hranici trojice 0
a agregát provedených finálních stavů; dva nezávisle psané serializátory
mé konvence dávají na všech těchto objektech totožné bajty a hashe, a
znovu-sestavené slovo (nezávislé druhé složení bloků v kódu) dává tentýž
fingerprint jako hlavní složení. Hodnoty jsou nová vlastní čísla této
konvence; s autorovou EXPECTED.txt se v této fázi nesrovnávají (NEOVĚŘENO).
FAIL: neshoda serializátorů/složení.

## 3. Zmrazený rozsah strojového běhu a kontrakt programu

- review.py je čistě stdlib, exaktní celá čísla, běží z /work/posudek
  příkazem `python3 review.py [--triples N]`. Ve výchozím režimu N=1000.
- Exaktní zrychlení je povoleno jen za těchto podmínek, všechny se v běhu
  samy ověří: (i) cache rozlišných lokálních pár-přechodů; každý cache
  záznam se po běhu přepočte literálním opakováním kontaktu na prvcích
  (K1); (ii) běhy týmž hran za sebou (C^k) smí běžet jako jeden cache
  přechod, ale před prvním použitím se de-komprese běhově kódovaného slova
  musí rovnat literálně složenému slovu jako celek (i hranově, i počtem).
  To není koncov- bodový orákulum: žádný stav se nedosazuje z formule,
  formule slouží jen k porovnání.
- Závazek této fáze, zmrazený před během: kompletně (dopředu i inverzně,
  se všemi kontrolami K1–K9) ověřím NEJMÉNĚ prvních 100 trojic dle V7;
  cíl je všech 1000 v jednom běhu. Běh s N=1000 a všemi PASS končí
  návratem 0 a řádkou `RESULT: PASS (full)`. Běh s N<1000, i když všechny
  provedené kontroly passerují, tiskne `Scope: PARTIAL` a končí návratem 2:
  není to úplný PASS inventáře. Kterýkoli FAIL končí návratem 1.
- Pokud běh 1000 na tomto stroji nedoběhne v limitu, který sám použiji
  (600 s podle A-RUN), nahlásím dosažené N jako vzorek a zbytek jako
  NEOVĚŘENO; čas běhu sám program tiskne jako provozní údaj, ne jako
  kontrolu.

## 4. Rozsah platnosti (co PASS nebude znamenat ani při úspěchu)

- Konečné výpočty: menší než inventářově úplný běh neověří strojově
  všechny trojice; i úplný běh pokrývá jen deklarovaný k=3 nosič
  a desetivstupovou rodinu.
- Obecné: K1-ové maticové fakty (R^T A R=A, R^5=I) jsou obecné pro formu Q;
  indukce pro libovolný konečný horizont k (A-PROOF §7) je v tomto posudku
  NEOVĚŘENA strojem — ověřen je k=3 a dosazení formulí.
- Netvrdí se: provoz na neomezené historii na jednom konečném nosiči,
  regenerace obsazených archivů, surová syntéza vstupů, kontaktové
  vyjádření SWAPů, minimalita délek, fyzikální realizace, čas/energie.
- Status v kánonu se nemění; axiom J=1+zeta5^2 se nedokazuje ani se
  netvrdí, že by pětka byla vynucená.
