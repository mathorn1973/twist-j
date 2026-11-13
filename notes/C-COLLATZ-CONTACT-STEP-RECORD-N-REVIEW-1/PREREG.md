# PREREG — nezávislý slepý posudek PR #1862 (fáze 1), zmrazeno před spuštěním review.py

Autor posudku: Emmy (Muse Wonder Full), jiná rodina modelů než autor PR.
Zdroj kontraktu: pouze texty v checkoutu
`notes/C-COLLATZ-CONTACT-STEP-RECORD-N/{PREREG,PROOF,README,BREAK-SCOPE,RUN,REVIEW,PROMO*}.md`
(repo na 85255b14f40a7a853d261ffcc19dc96fa850be44, bez historie gitu).
Autorův `verify.py`/`break.py`, `EXPECTED*`, `COMPARISON.json`, `SHA256SUMS`
jsem neotevřela (jsou skryté) a do konce fáze 1 neotevřu.
Tento soubor je sepsán a zmrazen před prvním spuštěním mého `review.py`.

## 1. Kontrakt odvozený z textu (rovnice, ne očekávání)

- Prstenec `O=Z[j]`, `1+j+j^2+j^3+j^4=0`, `rho=j^2`, `u=1-rho`, `w=1+rho`
  (PREREG.md:10, PROOF.md:15-17).
- Kontakt `C(a,b)`: je-li `a-b in 2O`, polož `s=(a+b)/2`, `t=(a-b)/2` a vrať
  `(s+rho*t, s-rho*t)`; jinak vrať `(a,b)` (PREREG.md:11-12, PROOF.md:19-22).
- Účet `Q(z)=(5*sum(z_i^2)-(sum z_i)^2)/2`, báze `(1,j,j^2,j^3)`;
  epsilon `eps(z)=sum z_i mod 5` (PREREG.md:13, PROOF.md:30-43).
- Bit `b`: `(u,0)` pro `b=0`, `(0,u)` pro `b=1`, little-endian
  (PREREG.md:17-18, PROOF.md:113).
- Sloty: X 0..11 (6 bitů), Y 12..23, archiv A 24..29 (3 bity), archiv B 30..35,
  scratch 36..44 (9 nul), selektor 45,46,47 (jeden token u), pomocník 48=w;
  počáteční selektor A; celkem 49 slotů, součet `19u+w`, `Q=98`
  (PREREG.md:22-26, PROOF.md:148-166).
- Doména `D={1,3,5,7,9,11,13,15,17,23}`, vstupy `I={1,3,5,7,9,11,13,15}`;
  `v=v2(3n+1)`, `m=(3n+1)/2^v` (PREREG.md:28-31). Tabulku (m,v) do kompilátoru
  **nezadávám z textu**; počítám ji z definice `3n+1` a s tabulkou
  PROOF.md:174-185 ji jen srovnávám jako kontrolu K3.
- Makra, chronologicky zleva doprava (PREREG.md:40-46, PROOF.md:51-87):
  `D(h;c,d)=C(h,c)^3 C(h,d)^3 C(h,c) C(h,d) C(h,c)` (9 kontaktů),
  `V(g;c,d)=C(g,h) D(h;c,d) C(g,h)^4 D(h;c,d)` (23 kontaktů).
  V má vyměnit c,d právě když `g=u`, a obnovit g,h (tabulky PROOF.md:61-68,95-102).
- Mintermový XOR: vypůjčení tokenů řetězem
  `V(c0;c1,s0), V(s0;c2,s1), ...`, poslední scratch = konjunkce řídicích slotů;
  s ním V-výměny cílových kolejí, pak vypůjčení V-makra v opačném pořadí;
  jeden řídicí slot bez scratche; nepravdivá hodnota bitu používá nulovou kolej;
  více výstupů sdílí jeden řetěz (PREREG.md:48-54, PROOF.md:111-144).
- Modul vybrané banky (PREREG.md:56-63, PROOF.md:194-219):
  (1) pro n vzestupně z D, řízeno selektorem a 6 kolejemi X-mintermu pro n,
      XOR bitů `m(n)` do Y a `v(n)` do archivu (překlápí se jen jedničkové bity);
  (2) pro n vzestupně z D, řízeno selektorem, 6 kolejemi Y-mintermu pro `m(n)`
      a 3 kolejemi archivního mintermu pro `v(n)`, XOR bitů `n` do X;
  (3) po bitech: XOR Y do X řízený selektorem a jedničkovou kolejí Y, pak
      XOR X do Y řízený selektorem a jedničkovou kolejí (nového) X.
- Slovo `W` = modul A, modul B, pak nepodmíněné D-výměny selektoru (B,S) a (A,B),
  cyklus A->B->S->A (PREREG.md:65-66, PROOF.md:232-235). W je jedno pevné slovo,
  nezávislé na vstupu (PREREG.md:69). Běh: 3 táž W (PREREG.md:73-80).

## 2. Mé zmrazené konvence (kam text nedosáhne; při porovnání převést)

K1. Reprezentace: prvek O je u mě polynom nad Z v proměnné t (=j) mod
    `1+t+t^2+t^3+t^4`, uložený jako čtveřice koeficientů stupňů 0..3.
    Násobení je obecná konvoluce s redukcí `t^5=1`, `t^4=-1-t-t^2-t^3`
    (ne ručně psaná tabulka násobení rho). `a-b in 2O` testuji jako
    „všechny 4 koeficienty rozdílu sudé“.
K2. Pár kolejí bitu k registru se základnou B jsou sloty `(B+2k, B+2k+1)`;
    první je nulová kolej, druhý jedničková. Selektor: 45=A, 46=B, 47=S.
K3. Pořadí řízení mintermu: selektor první (PROOF.md:195), pak bity vzestupně;
    ve fázi (2) po Y-bitech archivních bitů vzestupně. Scratch řetězu
    s0=36, s1=37, ... v pořadí vypůjčení.
K4. Cílové překlápění sdíleného mintermu: bity cílového registru vzestupně;
    fáze (1) nejdřív Y, pak archiv (BREAK-SCOPE.md:33-34). V zápisu
    `V(g; c, d)` je c první kolej cíle dle výše (u kolejí bitu: nulová, pak
    jedničková; u vypůjčení: `V(c0; c1, s0)` doslova dle PROOF.md:120).
K5. Fáze (3) je prokládaná po bitech: pro k=0..5 nejdřív Y->X, pak X->Y
    (BREAK-SCOPE.md:35-36). Hrana je uspořádaná dvojice (první, druhý) argument C.
K6. Můj edge-fingerprint: SHA-256 binárního proudu, kde každá chronologická
    hrana jsou právě 2 bajty `(první, druhý)`; bez oddělovačů a bez nového řádku.
    NENÍ to serializace `i,j\n` z BREAK-SCOPE.md:39-40 — při porovnání převést.
K7. Můj fingerprint hranic: pro každé n z I vzestupně a hranici po W1,W2,W3 jeden
    ASCII řádek `n|k|slot0;slot1;...;slot48\n`, slot = `a,b,c,d` (mé koeficienty
    1,t,t^2,t^3); SHA-256 zřetězení těchto 24 řádků. Není to JSON tvar autora
    ani breakera (REVIEW.md:88-96) — při porovnání převést. Fingerprinty K6/K7
    jsou jen tištěné výstupy; PASS/FAIL na nich nezávisí (žádné EXPECTED nečtu).
K8. Memoizace: `C(a,b)` se při prvním výskytu uspořádané dvojice spočítá mou
    aritmetikou a ověří dle K-pravidla pro dvojice (kontrola C2 níže), pak se
    výsledek smí znovu použít; hraniční replay celého slova tím není nahrazen
    (srov. BREAK-SCOPE.md:67-68 jako popis techniky, ne jako můj kód).

Odvozený počet (mou rukou z §1, před spuštěním): fáze (1) na řádek 6+popcount
maker výpůjček/cílů dle §1 dává na modul
`10*(12+18) + sum popcount(m)+popcount(v) + sum popcount(n) + 36` V-maker;
ze spočtené tabulky je to 397 V na modul, tj. 794 V + 2 D celkem a
`794*23+2*9 = 18280` kontaktů. Kontroluji proti tvrzení README.md:6.

## 3. Zmrazené kontroly (každá tiskne PASS/FAIL; exit 0 jen při úplném PASS)

C0  Aritmetika prstence z definic: `1+t+t^2+t^3+t^4=0`, `rho^5=1`, `rho!=1`,
    `Q(u)=5`, `Q(w)=3`, `eps(rho)=1`, `eps(u)=0`.
    Nezávislá cesta: mé polynomiální násobení. PASS = všechny rovnosti přesně.
C1  Lokální tabulky doslova kontakty: všech 6 řádků D (h in {w, 1+rho^2} × cíl
    (0,0),(u,0),(0,u); PROOF.md:61-68) a 6 řádků V (g in {0,u} × týž cíl;
    PROOF.md:95-102), včetně obnovy g,h; každé makro navíc plným nativním
    inversem (hrany pozpátku, 4 kontakty na hranu) vrátí počáteční trojici.
    PASS = přesná rovnost čtveřic ve všech 12 dopředných i 12 zpětných případech.
C2  Každá odlišná uspořádaná primitivní dvojice, která se v jakémkoli mém
    primitivním replay (včetně inversů) vyskytne: `C^5=id`, `C^4∘C=id`,
    zachování součtu dvojice, součtu Q a eps každého ze dvou slotů.
    PASS = platí pro 100 % vyskytnuvších se dvojic; jejich počet se tiskne.
C3  Aritmetická tabulka z definice: pro n v D spočítám (m,v) z `3n+1`; musí
    souhlasit s PROOF.md:174-185, všechny dvojice (m,v) jsou různé a
    `n=(2^v*m-1)/3` přesně (bezezbytkové dělení). PASS = všech 10 řádků.
C4  Slovo: W se sestaví jednou, před jakýmkoli stavem, jen z D a definic.
    PASS = počet V-maker 794, D-maker 2, hran 18280, všechny hrany mají
    oba indexy v 0..48, různé; tiskne se můj edge-fingerprint (K6).
C5  Příprava: pro každé n v I má počáteční 49slotový stav součet `19u+w`
    a celkové Q=98, Y=A=B=0, scratch nulový, selektor A, pomocník w.
    PASS = pro všech 8 vstupů přesně.
C6  Osm plných tříslovových trajektorií primitivními kontakty (n v I):
    po W1: X=m(n), A=v(n), B=0, selektor B; po W2: X=m(m(n)), A beze změny,
    B=v(m(n)), selektor S; po W3: X,A,B beze změny, selektor A. Na každé
    z 24 hranic: Y a scratch prázdné, pomocník w, součet 19u+w, Q=98,
    všechny registry dekódovatelné jako binární koleje. Vstupy obou aktivních
    slov musí být v D (druhý výstup v D být nemusí). PASS = všech 8×3 hranic
    a všechny dekódované hodnoty; tiskne se můj fingerprint hranic (K7)
    a tabulka výsledků ke srovnání s PROOF.md:245-254 / README.md:23-32.
C7  Plný primitivní invers 3W (hrany pozpátku, C^4 na hranu) obnoví pro
    každé n v I přesně počáteční 49slotový stav z C5. PASS = 8/8 přesně.
C8  Obsazená pokračování: 80 případů (n v D × předchozí A v 0..7, selektor B,
    B,Y,scratch připravené), plnými primitivními kontakty: po jednom W
    X=m(n), B=v(n), A přesně zachováno, selektor S, Y/scratch prázdné,
    pomocník w, součet 19u+w, Q=98; plus plný invers obnoví start.
    PASS = 80/80 dopředu i zpět (PREREG.md:85-87, PROOF.md:266-270).
C9  Skip na úrovni maker (výslovně NE primitivní replay): 4096 stavů
    (selektor S, X v 0..63, A,B v 0..7, práce připravena) pustím přes
    abstraktní sémantiku V/D ověřenou v C1 (V mění c,d jen při řídicím u;
    D mění vždy). Během běhu hlídám předpoklady maker (řízení v {0,u},
    cílová dvojice nejvýš jeden token, pomocník nedotčen). PASS = 4096/4096
    beze změny registrů, selektor na konci A, žádný předpoklad porušen.
    Rozsah je označen jako makro-úroveň (PREREG.md:88-90).
C10 Zpětné získání vstupu: z finálního X a uspořádaných hloubek (A,B) z C6
    aplikací `x -> (2^v*x-1)/3` dvakrát v opačném pořadí archivů (nejdřív B,
    pak A) vyjde přesně původní n, obě dělení bezezbytková. PASS = 8/8.
C11 Stejný první výstup, různé hloubky: v mých trajektoriích existují
    dva různé vstupy se stejným m a různým v; konkrétně kontroluji tvrzení
    PROOF.md:280-282 (1 a 5 → výstup 1, hloubky 2 a 4; 3 a 13 → výstup 5,
    hloubky 1 a 3). PASS = obě dvojice z mého výpočtu přesně tak.
C12 Oddělené lemma o půlení (PROOF.md:364-396), jen konečné instance:
    `J^{-1}=-rho-rho^3` mým násobením (J=w); pro x=3n+1 (n v D) jako holé
    celé číslo v O a kaskádu s D=4 nulovými sloty: neprázdný prefix uložených
    slotů má délku v(n) a `J^{-v} * aktivní = m(n)`; pro liché x=z D je
    C(x,0)=(x,0). PASS = všechny instance. Netvrdím tím obecný důkaz lemmatu.

Mimo strojový rozsah tohoto posudku (označuji NEOVĚŘENO, neodvozuji z textu):
obecné důkazy PROOF.md §7 (obstrukce) a obecné znění §8 nad rámec instancí C12;
shoda s autorovým slovem/hranicemi a jeho výstupy (fáze 2); dvoarchitekturová
brána. Žádné tvrzení o původu pravidla 3n+1 z J, neohraničeném algoritmu,
konvergenci ani statusech v kánonu.

## 4. Prah selhání

Jakékoli FAIL výše, výjimka nebo nedekódovatelná hranice = celkový FAIL
(exit != 0), výsledek se zachová tak, jak je. Prahy po spuštění neměním;
oprava mého kódu smí měnit jen implementaci, ne kritéria ani konvence §2.
