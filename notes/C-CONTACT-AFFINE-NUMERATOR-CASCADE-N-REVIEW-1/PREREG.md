# Nezávislý slepý posudek PR #1865 — zmrazený seznam kontrol (fáze 1)

Status tohoto dokumentu: vlastní PREREG posudku, sepsáno PŘED prvním spuštěním
vlastního ověřovače `review.py`. Žádný autorův kód, data ani výstup nebyl otevřen
(`verify.py`, `blindbreak.py`, `EXPECTED.txt`, `BREAK-EXPECTED.txt`,
`COMPARISON.json`, `SHA256SUMS` jsou skryté a nečtou se). Podklad jsou jen texty PR
v `notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/` (dále jen cesta PR) a kánon.
Kandidát PR je v textech značen NON-CANONICAL / L1,
`C-CONTACT-AFFINE-NUMERATOR-CASCADE-N` (PR/PREREG.md:3). Tento posudek žádný
status v kánonu nezvyšuje a hypotézu nenazývá dokázanou.
Kánonová autorita kontaktu citovaná jen jménem: řádek
`RELATIVE-CONTACT-INTEGRAL-LAW` se statusem `[T]` v /canon/REGISTRY.tsv:595
(definice totálního kontaktu na O=Z[j], rho=j^2); PR odkazuje na „public Canon
v107“ jako autoritu kontaktu (PR/README.md:107). KONTAKT zde ověřuji z rovnic
v textu PR, ne převzetím kánonového statusu.

## Zmrazené vlastní konvence (k převodu při pozdějším porovnání s autorem)

K1 Báze: prvek O zapisuji jako čtveřici celých čísel `(a0,a1,a2,a3)` =
   `a0 + a1*j + a2*j^2 + a3*j^3`, `1+j+j^2+j^3+j^4=0` (PR/PREREG.md:11).
   Tedy `rho=j^2=(0,0,1,0)`, `J=1+rho=(1,0,1,0)`, `u=1-rho=(1,0,-1,0)`.
K2 Pořadí slotů: core sloty `0..15`; zdroj na `0,1,2`; čerstvé nuly `3..15`;
   volitelné archivy `16,17` (PR/PREREG.md:26-28). Kaskádní port `s`
   (1<=s<=13) je slot `2+s`, tj. sloty `3..15` v tomto pořadí.
K3 Číslování kontaktů: chronologický seznam hran
   `(0,1),(0,2),(0,3),...,(0,15)`, celkem 15; „C01“ znamená hranu `(0,1)`,
   „C02“ hranu `(0,2)` (PR/PREREG.md:39-44). Odmítnutý kontakt = identita.
K4 Můj fingerprint (záměrně NE autorova serializace z PR/PREREG.md:106-109,
   s autorem se zatím neporovnává): pro korpus q=3 řádky v rostoucím lichém n,
   každý řádek je text
   `n=<n>|<slot0>;<slot1>;...;<slot15>` kde slot je `a0,a1,a2,a3` v desítkové
   soustavě, sloty oddělené `;`, řádky oddělené `\n`, za posledním řádkem je
   `\n`, kódování UTF-8. Hranový otisk: text `0>1;0>2;...;0>15` bez
   závěrečného `\n`, UTF-8. Oba SHA-256 tisknu jako POZOROVANÉ hodnoty mé
   konvence, nikdy jako PASS proti číslu z textu PR.
K5 Čtečka dostává jako jediné argumenty `(slot0, tuple(slot3..slot15))`.
   Nic jiného (n, q, slot1, slot2, archivy) do ní nevstupuje.

## Nezávislé cesty (proti čemu se srovnává)

- Násobení v O implementuji dvakrát: (A) polynomiální redukce modulo
  `1+j+j^2+j^3+j^4`, (B) cyklická konvoluce délky 5 modulo `j^5-1` s odečtem
  páté složky. Shoda A/B se kontroluje na deterministickém výčtu.
- Q implementuji dvakrát: (Q1) uzavřený tvar `(5*sum(zi^2)-(sum zi)^2)/2`
  (PR/PREREG.md:14), (Q2) `Tr(z*bar(z))/2`, kde bar je automorfismus
  `j -> j^4` a `Tr(1)=4`, `Tr(j^k)=-1` pro k nedělitelné 5.
- Obecné (symbolické) kontroly dělám přes sympy s volnými symboly q, n
  (koeficienty čtveřic jsou polynomy v q, n); tam výsledek platí obecně,
  ne jen na korpusu. Vše ostatní je konečný výpočet na uvedeném korpusu.
- `v2` a lichý díl `m` počítám z celého čísla `qn+1` obyčejným integer
  dělením dvěma, nezávisle na kontaktech.

## Kontroly (PASS právě když platí kritérium; jinak FAIL a exit != 0)

R01 Prstenec. Krit.: `rho^5=1`, `rho^k != 1` pro 1<=k<=4,
    `1+rho+rho^2+rho^3+rho^4=0`, `J+u=2`, `J-u=2*rho`,
    `J * (-rho-rho^3) = 1` (tedy `J^{-1}=-rho-rho^3`, PR/PREREG.md:73),
    násobení A == B na všech dvojicích z deterministické množiny čtveřic
    s koeficienty v {-2,-1,0,1,2} tvaru (a,b,c,0) a (0,b,c,d).
    Rozsah: obecné identity v O (konečná množina jen pro kříž A/B).
R02 Q-hodnoty. Krit.: Q1==Q2 na téže množině i na všech stavech korpusů;
    `Q(u)=5`, `Q(J)=3`, `Q(2J)=12`, `Q(1)=2`, `Q(0)=0`,
    `Q(m*u)=5*m^2` pro m z korpusů (účet normalizovaného výstupu čtečky
    `r=u*m`, PR/PROOF.md:198; homogenita Q). Gramova matice Q1
    `(5I - 11^T)/2` má podle sympy vlastní čísla {1/2, 5/2}, tedy Q>=0 a
    Q(z)=0 <=> z=0. Rozsah: obecně (vlastní čísla), hodnoty bodově.
R03 Norma. Krit.: determinant matice násobení prvkem u v bázi K1 (sympy,
    přesně) je 5; determinant pro J je jednotka (±1). Tedy u není jednotka
    v O, J ano (PR/PROOF.md sekce 1). Rozsah: obecně.
R04 Kontakt z definice. Definice (PR/PREREG.md:12-13): odmítni, není-li
    `a-b` v `2O`; jinak `s=(a+b)/2`, `t=(a-b)/2`,
    `C(a,b)=(s+rho*t, s-rho*t)`. Krit.: na každém rozlišeném primitivním
    páru vyskytnuvším se v bězích níže: součet páru stejný, Q(a)+Q(b)
    stejný, epsilon=sum(zi) mod 5 každého ze dvou slotů stejné,
    `C^5 = id`, `C^4` je inverze; odmítnutý pár je identita a připuštěný
    je právě když rozdíl je sudý po složkách. Navíc tvar
    `C(a,b)=((J*a+u*b)/2,(u*a+J*b)/2)` (PR/PROOF.md:21-22) souhlasí na
    připuštěných párech z množiny R01 (dělení dvěma přesné).
    Rozsah: konečný — vyskytnuvší se páry + množina R01.
R05 Symbolický prefix (obecně). Se symboly q,n a definicí kontaktu
    (dělení dvěma je na těchto výrazech přesné polynomiálně) krit.:
    po C01: `slot0=2*q*u*n`, `slot1=2*(q-(q-2)*rho)*n`;
    po C02: `slot0=u*J*(q*n+1)`, `slot2=q*u^2*n+J^2`, slot1 beze změny
    (PR/PREREG.md:46-52). Rozdíl `a-b=-4n` u prvního kontaktu symbolicky.
    Rozsah: obecně pro každé q,n (algebraická identita, sympy simplify==0).
R06 Symbolický zdroj (obecně). Krit.: ze zdroje
    `E_q(n)=(2(q-1)u*n, 2((q-1)u+2)*n, 2J)` (PR/PREREG.md:18) symbolicky
    `Q_total=[40*q*(q-1)+32]*n^2+12` a
    `S_total=4*(q-(q-1)*rho)*n+2J` (PR/PREREG.md:31-33); pro q=3:
    `272*n^2+12`. Rozsah: obecně.
R07 Symbolický jeden kaskádní krok (obecně). Pro volnou čtveřici symbolů Y
    a `x=2Y` krit.: `C(x,0)=(J*x/2, u*x/2)=(J*Y, u*Y)`.
    Rozsah: obecně.
R08 Slovo. Krit.: seznam hran je přesně 15 hran K3, žádná hrana nezávisí
    na vstupu (jeden konstantní seznam v kódu), počet core slotů 16.
    Tiskne se můj hranový otisk dle K4 (pozorovaná hodnota, ne PASS krit.).
R09 Korpus A: q=3, lichá n=1..4095 (2048 případů). Korpus B: q=1..9,
    lichá n=1..127 (576). Pro každý případ krit. současně:
    (a) po prefixu platí tvary R05 číselně;
    (b) `v=v2(qn+1) <= 12`, `m=(qn+1)/2^v` liché;
    (c) finální `slot0 = u*J^(v+1)*m` (PR/PREREG.md:56);
    (d) pro 1<=s<=v: `slot(2+s)=u^2*J^s*(qn+1)/2^s` a je nenulový;
        pro v<s<=13: `slot(2+s)=0` (PR/PREREG.md:57-58);
    (e) slot1, slot2 = zbytky z R05 (staré zbytky zůstávají);
    (f) sled připuštění: první dva kontakty připuštěny, z kaskády právě
        prvních v připuštěno, ostatní odmítnuty;
    (g) celkový součet, celkové Q a epsilon každého slotu na konci ==
        na začátku; celkové Q sedí na vzorec R06;
    (h) čtečka (K5) vrátí právě (m,v); `r=J^(-(v+1))*slot0=(m,0,-m,0)`;
        účet normalizovaného r je `5*m^2`;
    (i) aritmetická inverze `n'=(2^v*m-1)/q` je celá a `n'==n`.
    Rozsah: konečný korpus, přesně tyto počty; program počty přepočítá
    a vyžaduje 2048 a 576.
R10 Pokrytí hloubek. Krit.: v korpusu A se vyskytne každá hloubka 1..12
    (PR/PREREG.md:86-87) a rozdělení hloubek z kontaktů == rozdělení
    spočtené nezávisle z v2(3n+1); v korpusu B je případů s v=0 právě 256
    (4 sudá q × 64 lichých n; sudé q dává qn+1 liché) a rozdělení opět ==
    nezávislé z v2. Rozsah: konečné korpusy.
R11 Plná inverze. Krit.: pro každý případ korpusů A, B, C i svědka R13:
    obrácené pořadí hran, 4 kontakty na hranu (PR/PREREG.md:80), vrátí
    úplný počáteční stav včetně archivů. Celkový počet plných inverzí
    program vyžaduje 2850 = 2048+576+225+1.
R12 Korpus C archivy: q=3, n v {1,3,5,7,15,27,85,1365,4095}, všech 25
    uspořádaných dvojic z {0,1,j,u,J} na slotech 16,17 (PR/PREREG.md:91-94),
    celkem 225. Krit.: core finální stav == případ bez archivů, oba archivy
    beze změny, úplný účet = core účet + Q archivů, plná inverze (R11).
R13 Svědek mimo hloubku: q=3, n=5461, `qn+1=2^14` (PR/PREREG.md:95-98).
    Krit.: všech 13 kaskádních slotů nenulových, `slot0=2*u*J^14`
    (PR/PROOF.md:250-253) a je sudý po složkách, čtečka vrátí právě
    `DEPTH_LIMIT` (ne pár (m,v)), zachování součtu/Q/epsilon, plná inverze.
    Tento případ se nepočítá jako kladný aritmetický úspěch.
R14 Determinismus a mez čtečky. Krit.: (a) pro vzorek případů: záměna
    slot1/slot2/archivů za jiné hodnoty (nejsou argumentem) nemění výstup
    čtečky; (b) syntetické vstupy: mezera v nenulovém prefixu (nenulový
    port za nulou) -> FAIL-čtečky (vyjímka/odmítnutí), `r` jiného tvaru než
    `(m,0,-m,0)` -> odmítnutí, všech 13 nenulových -> `DEPTH_LIMIT`;
    (c) stejný (aktivní, kaskáda) vstup dává vždy stejný výstup (opakovaný
    běh čtečky na stejném vstupu).
R15 Výstup není nový zdroj. Krit.: pro každý případ korpusů A,B: finální
    16-slotový core stav != `E_q(m)` doplněné nulami; `slot0 != (m,0,0,0)`
    (výstup není čisté m); slot1 a slot2 jsou přesně netriviální zbytky R05
    a pro n>0 je slot1 != 0. Navíc reziduální překážka na příkladu
    q=3,n=3 (m=5): epsilon(slot1 počáteční)=`4n mod 5` se liší od
    epsilon(slot1 z E_3(m))=`4m mod 5` (PR/PROOF.md sekce 7), tj. tentýž
    slot nelze kontakty přestavět na E_3(5) — kontroluji jen tuto nutnou
    podmínku, ne obecné tvrzení o všech kódováních.
R16 Mez obnovy zdroje (jen nutnost, bez dosažení). Krit. aritmetiky:
    `Q(E_3(n))=272*n^2+12` (R06), tedy rozdíl účtů je `272*(m^2-n^2)`;
    pro n=3,m=5: účty 2460 a 6812, rozdíl 4352 (PR/REVIEW.md:190);
    pro n ≡ 3 (mod 4) symbolicky `272*(m^2-n^2)=68*(5n^2+6n+1)` při
    `m=(3n+1)/2` (PR/PROOF.md:294). Nutnost odvozuji jen ze zachování Q
    (R04) a Q>=0 (R02): pokud by finální systém obsahoval E_3(m) plus
    cokoli dalšího s Q>=0, musí dodaný účet B splňovat
    `272*(m^2-n^2) <= B` (PR/PROOF.md:287). Program ŽÁDNOU konstrukci
    dosahující mez nehledá ani netvrdí; „ostrost/dosažení“ je NEOVĚŘENO.
R17 Můj fingerprint korpusu A dle K4: spočte se a vytiskne (SHA-256 +
    délka payloadu). PASS kritérium je jen: payload má 2048 řádků,
    každý se 16 sloty po 4 celých číslech a n rostoucí lichá 1..4095;
    hodnota hashe se s ničím z PR nesrovnává.

## Rozsah běhu a přepínač

Výchozí `--scope full` = korpusy výše kompletně včetně R04 na všech
vyskytnuvších se primitivních párech a R11 na všech 2850 případech.
`--scope sample` zkracuje korpusy A/B/C na předem dané podvýběry
(A: lichá n<=255, B: q=1..9 lichá n<=31, C: n v {1,3,27} a dvojice z
{0,J}) a je určen jen k ladění; hlášený výsledek posudku smí být jen
z `full`. Pokud by `full` na stroji nedoběhl, výsledek se označí
NEOVĚŘENO v nedoběhlé části — nesmí se vydávat sample za full.

## Negativní sonda (mimo složku posudku)

Kopie ověřovače v `/tmp` s jedinou změnou: poslední hrana slova
`(0,15)` nahrazena za `(0,14)`. Krit.: sonda skončí s nenulovým kódem
a vytiskne FAILURE/FAIL. Pokud by prošla, je ověřovač neplatný.

## Co tento posudek výslovně netvrdí

Žádné tvrzení o nekonečném provozu, opakovaném Collatz kroku, obnově
zdroje, volbě q=3 silou J, fyzikální realizaci, energii/čase ani o postupu
v kánonu. Symbolické kontroly R05–R07 jsou algebraické identity nad
deklarovanými definicemi; konečné korpusy nejsou důkaz obecné věty PR.
