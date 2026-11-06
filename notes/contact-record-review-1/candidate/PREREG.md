# Preregistrace kontaktního záznamu

NON-CANONICAL. **Návrh před veřejným pinem**, nikoli provedená či rezervovaná
sonda. Navržený identifikátor P-CONTACT-RECORD-1; jediná budoucí větev
`probe/P-CONTACT-RECORD-1`, jediná cílová složka `probes/P-CONTACT-RECORD-1/`.
Tento text, PROOF.md a verify.py se mají přijmout společně před formálním
během. Po veřejném pinem chráněném přijetí se rozsah ani prahy neposouvají.

## Rovnice

Předmět je jeden složený L1 kontrakt

\[
K_i\longrightarrow\mathcal U_iK_i\mathcal U_i
\longrightarrow(r_x,r_y)=(\epsilon_x\delta,\epsilon_y\delta)
\longrightarrow m_x=r_x^2,\qquad\delta=1_{\{h=0\}}.
\]

Úplné definice h, b,d,e,W_b,P_q a skutečných slov jsou pevně dány v
[PROOF.md](PROOF.md). Testují se:

1. K_i(f,q)=(f,q+3delta v_i), včetně úplného faktoru, inverze a délky
   skutečného dvanáctilistého slova. Délka není minimální tvrzení.
2. Úplná čtečka pro všech pět r_i má q_i'=q_i+s_i a
   r_i'=P_(q_i+s_i)P_(q_i)(r_i), s_i=3epsilon_i delta, a deklarovanou inverzi.
3. Samostatná reference má minimum tři stavy výhradně v přesné jednovolací
   klasické vratné třídě z PROOF.md. Vložené r_i má pět stavů, tři pracovní
   hodnoty na oracle rozhraní a dva výsledky dokončeného ready čtení.
4. Skutečné R_y R_x bez resetu, se společnou přípravou pouze na začátku,
   má úplnou produktovou mapu i pro obsazené reference a přesnou inverzi.
5. Každý list druhé čtečky zachovává m_x pro každý úplný vstup, takže
   každý její prefix zachovává první připravený výsledek. Syrové r_x
   se smí měnit a jeho konkrétní změna musí zůstat doložena.

Součástí kontraktu jsou negativní hranice: celá R_1 může podruhé smazat
první výsledek a R_1^5=I; R_0=I nedává příznak dokončení; neznámý binární
reset se zachováním všech ostatních souřadnic není injekce; ochrana není
globální invariant d_x,e_x,Ucal_x; na h≠0 je K_i=I.

## Kód

Jediný veřejný ověřovač je [verify.py](verify.py), Python 3.12, pouze
standardní knihovna, celočíselná aritmetika modulo 5, žádná náhodnost,
síť, externí soubory, binární přílohy nebo čtení měnitelného Canonu za běhu.
Před budoucím formálním během se připne jeho přesný commit a SHA-256,
spolu s SHA-256 preregistrace. Místní manifest návrhu není veřejným pinem.

Příkaz po veřejném přijetí a pinování, z kořene kanonického repozitáře:

    python3 probes/P-CONTACT-RECORD-1/verify.py

Program neimportuje staré audity. Ověřuje malé kontrakty odděleně a skládá
je. Následující počty jsou **předpovědi rozsahu**, nikoli výstup běhu:

| Kontrola | Rozsah |
|---|---:|
| Afinní buněčné identity přes nulu a šest bází | 35 řádků |
| Bilineární h(Bp)=-h | 16 dvojic bází |
| Komutace b_x,b_y přes afinní bázi úplného prostoru | 13 řádků |
| W_b,E_b na (h,eta,parita B) | 20 řádků |
| Symbolický úplný K_i pro oba indexy i=x,y | 40 řádků |
| Úplná P tabulka | 25 položek |
| Třístavová a vložená čtečka, mapy/inverze | 60 a 100 řádků |
| Nezávislé podmnožiny pěticyklu | 32 podmnožin |
| Dvě čtečky, všechna q_x,q_y,r_x,r_y, delta a volby | 5000 vstupů |
| Oba znaménkové listové účinky na každé r_x | 10 řádků |
| Negativní čtvercové kontroly b,d,e,Ucal | 100 řádků |
| Perioda celé čtečky a rovnost nepoužitý/dokončený0 | 50 a 25 řádků |

Afinní a bilineární identitě stačí uvedené báze právě kvůli explicitnímu
algebraickému typu map. Parita B sleduje celou mocninu b_x b_y, tedy i
písty; čtyři afinní vláknové mapy nesou obě q i obě r. Univerzalita se
neodvozuje z několika reprezentativních h ani z pouhé očekávané mapy K_i.
Program zvlášť ověří rozvoj komutátoru na zmrazený seznam listů.

Doplňková doslovná diagnostika má přesně pět pevných pístových párů

    p_x=(1,0,0,0), p_y=(0,0,0,2h), h=0,1,2,3,4.

Pro oba eta, všech 625 společných q/r a všechny čtyři volby jde o 25000
skutečných kompozic a 225000 hranic druhé čtečky včetně prázdného prefixu;
1000 případů začíná s oběma ready r. Provádí všechny listy a úplné inverze.
Samostatný úplný nulový svědek zachovává negativní stopu r_x:1→4→1.
To je kontrola implementace na uvedených svědcích, nikoli úplná enumerace
osmi pístů a bitu. Velké zmrazené místní audity se veřejným ověřovačem
znovu nespouštějí a jejich rozsah není novou veřejnou bránou.

## Nosič a data

Úplný vložený nosič X=F5^12×{0,1}; q=(q_x,q_y) je libovolné neznámé
q z celé F5². Pro dvě garantovaná čtení je jediná příprava r_x=r_y=0.
Inverze a ochrana m_x se týkají i obsazených registrů na celém X.
Samostatné minimum se vztahuje ke Q×A při pevně aktivním diváckém faktoru,
jedné oracle výzvě I/+3, společném vratném kodéru/dekodéru a výstupu jen z A.

W_b, Ucal_i, příprava a koncové čtení jsou explicitně přijaté vstupy
rozšířené architektury. Žádná dodatečná brána, registr, energie, teplota,
pravděpodobnost, occurrence law nebo fyzická realizace nejsou součástí dat.
Místní zdroje jsou označeny v README; veřejný důkaz a kód jsou samostatné.

## Systematiky a rovnost

Rovnost znamená přesnou shodu všech souřadnic na X, nikoli pouze q nebo h.
Rovnost čtení m_x je přesná shoda v F5. Kontext čtení tvoří pevná strana x,
stejný protokol a diskrétní hranice listů po dokončení prvního zápisu.
Nepřipouští se dodatečná volba čtení podle epsilon, h, výsledku nebo prefixu.
Nejde o tvrzení jedinečnosti všech čteček či fyzického výběru této čtečky.
Tabulka m_x má obecné tři hodnoty 0,1,4; po dokončeném ready zápisu jen0,1.

Při inverzi se vyhodnocuje původní experimentální slovo v opačném pořadí.
Epsilon nejsou registry; označují dvě předem stanovené experimentální volby.
Nulová čtečka stále obsahuje dva listy Ucal_i. Obsazený r_x se při druhém
čtení nesmí nahradit nulou. Znaménko W_b je stavově závislé a vždy se
vyhodnocuje z aktuálního vstupu listu. Ochrana je tvrzením o diskrétních
listech, nikoli o neznámé fyzické trajektorii uvnitř W_b nebo nerušivém měření.

## Prah selhání

Jediná přesná odchylka libovolné uvedené identity, inverze, připraveného
výsledku, minimálního kontraktu, listové ochrany nebo povinného negativního
svědka je selhání daného tvrzení. Nulová tolerance; žádný statistický test.
Nenulový exit, neprázdný stderr nebo odlišné stdout nejsou PASS.
Každý konkrétní falsifikátor se uchová a prahy se po pinování nemění.
Nesplněný požadavek fyzické realizace je mimo deklarovanou L1 třídu a
není záporným uzavřením otevřeného vlastníka.

Po prvním řádně připnutém dokončeném běhu se přidají EXPECTED.txt, RUN.md
a RESULT.md podle POLICY.md. Obě veřejné architektury musí na stejném
PR headu s Pythonem3.12 vrátit stejný hash ověřovače, exit0, prázdný stderr
a stdout shodné po bytech s jediným EXPECTED.txt; vyžaduje se úspěšný
agregát check. Místní staré PASS ani jejich Windows/AMD64 běhy tento
požadavek nenahrazují. Nezávislý přesný důkaz se posuzuje zvlášť od C evidence.

## Akční vrstva

Pouze L1. Žádný nový cross-layer gate, fyzikální zákon, Canon fold ani
změna statusu vlastníka. Zejména QUADRATIC-MEMORY-NATIVE-CONTACT,
QDD-INSTRUMENT-APPARATUS a jeho děti zůstávají otevřené podle veřejného
registru; fyzický HOLD druhého trace kontaktu se nedotýká této sondy.
ENTROPY-LAYER-BRIDGE zůstává samostatným negativním veřejným výsledkem.
Entropie původního autonomního U je jiný kontrakt; Landauerův vztah není
důsledkem této čtečky a tato sonda jej netestuje.
