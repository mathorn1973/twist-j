# Rekonstrukce a oprava výzkumné větve: trojlístkový proton

Datum: 17. října 2026. Jazyk: čeština; jména tvrzení, stavů a matematická notace podle veřejného TWIST-J.

**Režim:** PUBLIC comparison with Public Canon v103, plus NON-CANONICAL local incubation.
**Status nových matematických výsledků:** authored `candidate-T` s místní nezávisle napsanou kontrolou; historické konečné běhy `candidate-C`. Žádná veřejná propagace.
**Status fyzikální interpretace:** bez statusu. Hypotéza „proton je trojlístek“ nebyla odvozena.

## I. Co se rozpadlo, co ne

1. Obě dokončené větve skončily samostatným odevzdáním do osobní knihovny.
   Poslední odpověď zůstala nedokončená, odkaz ke druhému balíčku se nedostal
   do závěrečné zprávy. Proto nebylo jasné, na jaký konkrétní vědecký výsledek
   a na který kód navázat.
2. První archiv A má 21 připnutých souborů, druhý B má 25. U všech souhlasí
   SHA-256 v jejich vlastních manifestních souborech a původní archivy jsou
   nyní znovu přístupné.
3. Tato rekonstrukce původní archivy ani první výstupy nemění. Opravuje
   přenos, společné účetnictví a konkrétní formulaci příští vědecké úlohy.
4. Původní A měla v auditní historii po prvním úspěšném běhu pozdější
   odstranění časového pole z pomocného nezávislého reportu. Tato okolnost
   zůstává zaznamenána; neprohlašujeme historický pin za bezezměnný.
   Balíček B má zdroje všech tří běhů připnuté před spuštěním a první výstupy
   zachované samostatně.

## II. Připnutá veřejná autorita

`mathorn1973/twist-j`, `main`, Public Canon v103 ACTIVE:

- HEAD a cíl anotovaného tagu `canon-v103`: `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`.
- CONTENT_COMMIT: `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`.
- SHA-256 `canon/CANON.md` deklarovaný v `STATUS.md` a `canon/SHA256SUMS`:
  `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`.
- Délka: 1 052 518 bajtů. Archivovaný publikační běh `39022927713` má
  stav SUCCESS, x86_64 i aarch64 základní kontrola prošla.
- `POLICY.md`, `AGENTS.md`, `canon/CORE.md` a `canon/FRONTIER.md` byly znovu
  přečteny při rekonstrukci. `STATUS.md`, `POLICY.md` a `AGENTS.md` mají
  přednost před historickými soubory a tímto zápisem.

Aktivní veřejná otevřená tvrzení zahrnují `QUADRATIC-MEMORY-NATIVE-CONTACT [O]`,
`COLOR-MEASURE-SELECTION [O]` a `PROTON-RESIDUAL-IS-QCD [O]`. Neuzavíráme je.

## III. Řetězec A: Kleinova plocha, trojlístek a ramifikace

Přijatý klasický základ je binární ikosaedrická grupa
`2I ~= SL_2(F_5)` řádu 120 a Kleinovy invarianty `f,H,W`
stupňů 12, 20, 30, s rovnicí

    W^2 + H^3 = 1728 f^5.

Projekce invariantní plochy na `(W,H)` má obecně pět listů.
Místo větvení `W^2 + H^3 = 0` má jako link trojlístek `T(2,3)`.
Jde o přesnou algebraickou/topologickou konstrukci. Samotný uzel
**není** automaticky ztotožněn s fyzickým prostorem protonu.

Se značenými maticemi

    S = [[0,-1],[1,0]],   T = [[j,1],[0,j^4]],

kde `j^5=1`, `j!=1`, `J=1+j^2`, byla analyticky a dvojmo numericky
v přesné aritmetice ověřena změna báze

    a = j+j^4,  s=j^2-j^3,
    P = [[1,-a],[0,s]].

`P^-1 T P=diag(j,j^4)` a `P^-1 S P` odpovídá standardnímu
unitárnímu značení. **P není integrálně invertibilní u lambda=1-j**.
Modulo `lambda` přechází diagonalizované T na identitu, zatímco
původní T na nenulovou unipotentní matici, takže tuto mez nelze
odstranit integrálním sdružením.

Přesná primitivní normalizace invariantů po substituci `B=s P^-1`
dává koeficientové valuace `(10,20,25)` a rovnici

    W_prim^2 + s^10 H_prim^3 = 1728 F_prim^5.

Modulo `lambda` se člen `H_prim^3` ztratí. Tato ramifikovaná změna
**není** důkazem nativního prostorového uzlu v charakteristice pět.

Předem zadaný bod s `J` na nulové formě `F` má přesné jednotkové
Hermitovo čtení. Tato jednotka je matematická normalizace, ne fyzikální
hmotnost ani délka.

Všechny přesné koeficienty a důkaz jsou v `source-A/author/PROOF.md`.

## IV. Řetězec B: kontaktní operace a oprava meridiánů

### B1. Dvě již hotové kontaktní čtečky nestačí

Z původního `CONTACT-RECORD` plyne pro úplné kontakty `A_x,A_y`,
včetně obsazené paměti,

    <A_x,A_y> ~= C_5 x C_5.

Komutují a jejich braidový vztah `A_x A_y A_x = A_y A_x A_y`
by v komutativní grupě vynucoval `A_x=A_y`, což není pravda.
**Falsifikována je přesně tato dvojice, nikoli trojlístek obecně.**

### B2. Dodaná vazba umožňuje S3, ale ne věrné 2I

Pro úplnou jednu buňku, původní generátor `e` a dodané rozhraní
`Ucal`, položme

    M=Ucal,  N=e Ucal e.

Obě obnovují písty a `q`, působí na `r` permutacemi. Přesně platí

    M^2=N^2=(MN)^3=I,   MNM=NMN,   <M,N> ~= S_3.

Je to neabelovský obraz abstraktní trojlístkové grupy, ale jeho
meridiány mají řád 2 a nevytvářejí `2I`. `Ucal` je **dodaný předpoklad**.

Pro celou grupu **pevných slov**

    Gamma_plus=<a,b,c,d,e,Ucal>

byl odvozen úplný tvar stavové akce a centrální překážka:

    rho(-I)=I

pro každý homomorfismus `rho:SL_2(F_5)->Gamma_plus`.
Důkaz používá dokonalost `SL_2(F_5)`, akci na `q` ve `D_10`,
pět r-permutačních vláken `S_5` a pístové jádro exponentu 5.
**Nevylučuje** další `W_b`, úplné mezibuněčné součty ani stavově
řízené programy v jiném úplném nosiči.

Samotné původní `U` zachovává faktor `chi=(sum(x),r)` a nemůže na
celém nosiči realizovat dodanou `Ucal` pouhým společným počtem
svých dopředných kroků. Tato záporná věta má přesný faktorový
rozsah, ne obecnou nemožnost styku.

### B3. Správné kladné geometrické značení

Staré abstraktní meridiány `A=T`, `B=STS^-1` byly grupově správné,
ale bez dalšího nevyjadřovaly **jednoduché kladné monodromie**
skutečného komplexního pětičetného větvení.
Opravený předem zvolený pár je

    C=A^2,  D=B^3,  R1=j^3 C,  R2=j^3 D.

`R1,R2` mají vlastní hodnoty `{1,j}`. Vygenerují komplexní
reflexní grupu `G16 ~= 2I x C5` řádu 600. Pětice

    (W,H,f) -> (W,H,j f)

je algebraická akce nad větvením. Původní souřadnicový bod na `f=0`
není bodem komplementu pro základní listy monodromie.

### B4. Kladný vzor na mezibuněčných součtech

Po redukci modulo `1-j`:

    C0 = [[1,2],[0,1]],   D0 = [[1,0],[2,1]].

Tyto matice jsou realizovatelné jako **deklarovaná algebraická operace**
ze součtových map na dvou úplných šestiregistrových buňkách:

    Ccal: (x,y) -> (x+2y,y)
    Dcal: (x,y) -> (x,y+2x).

Platí na celém F5^12

    Ccal Dcal Ccal = Dcal Ccal Dcal,
    (Ccal Dcal)^3 = -I.

Tím předepsaný centrální prvek přežívá na úplném nosiči.
**Není** tím dodán autonomní řadič, fyzikální připuštění celobuněčných
součtů, prostorový invariant ani zachování energie.

Všechny výpočty, současně pozitivní a negativní, jsou v
`source-B/contact/PROOF.md` a `source-B/geometry/PROOF.md`.

## V. Současné veřejné větve, které se nesmějí převzít dvakrát

Stav ověřený 17.10.2026, všechny otevřené a nesloučené:

- PR #1577: původní port nerozlišuje `j` proti `j^-1` za uvedené
  stejné faktorové historie.
- PR #1579: deklarovaný dodaný kontakt skutečně tuto dvojici rozliší
  a přenese ji do záznamů. `W_b`, `Ucal`, energie předpony a autonomní
  řízení zůstávají vstupem.
- PR #1581: tři pevné reference nesou všech pět fází do původního
  placeného záznamového aparátu pro 25 dvojic. Opět jde o
  `NON-CANONICAL` podmíněné L1 výsledky a ne o fyzikální měření.

Čisté algebraické kontaktní dvojice se nesmějí zaměnit za přijatý
aktuální fyzikální mechanismus. Tyto PR se při rekonstrukci
nezměnily ani neuzavřely.

## VI. Co se z těchto výsledků opravdu nesmí tvrdit

- Neexistuje nyní odvození, že proton je `T(2,3)`.
- Kleinovo větvení v komplexní geometrii a fyzicky pozorovaný
  prostor tvoří dvě různé úrovně; jejich spojení potřebuje vlastní gate.
- `S3` je neabelovský, ale není binární ikosaedrická grupa.
- Pěticyklická fáze, pět listů pokrytí a pět barev nepředstavují
  automaticky stejný fyzikální objekt.
- Vratná algebraická kontaktní operace není automaticky dovolená
  fyzikální operace původního `U`.
- Navržený vztah `m_p/m_e = 6 pi^5 + 5 alpha(1-(1-alpha)/(6 pi))`
  zůstává číselnou hypotézou. Odvodit její koeficienty nebo zbytek
  ze stabilního uzlového nosiče se dosud nepodařilo.
- Stabilita uzlu, baryonové číslo, spin, náboj, energie i čtení
  experimentální hmotnosti nejsou uzavřené.

## VII. Nejbližší praktické rozhodnutí

První samostatnou otázkou musí být nativní admissibility/compilation
`C-TREFOIL-NATIVE-CONTACT-N` (pracovní jméno, NON-CANONICAL; nejde o
existující veřejnou sondu). Její rámec je v `NAVAZUJICI_ULOHA.md`.

Vstupem nemůže být další pěkný vzorec na poměr hmotností. Vstupem
musí být stejný úplný nosič, konkrétní opakovatelná operace a skutečný
falsifikátor na celé deklarované třídě. Teprve až je L1 uzavřeno, má
smysl zkoušet pojmenovaný přechod k prostorovému uzlu L2/L3,
prostorovému nosiči L4, streamu L5 a měření L6.

## VIII. Reprodukce a kontrola dat

- B: všechny tři zdroje kontakt, geometrie a oponent znovu spuštěny
  při této opravě na Pythonu 3.13.5 x86_64. Exit 0, stderr prázdné;
  zachycený stdout se **bajt po bajtu shoduje** s prvními výstupy.
- A: autorův zdroj i oddělený zdroj oponenta znovu spuštěny na
  Pythonu 3.13.5 x86_64. Autor: 59/59 PASS, oponent: 94/94 PASS;
  přesná množina výsledků kontrol je shodná s prvními výsledky.
  Autorův celý stdout není bajtově stejný pouze proto, že obsahuje
  skutečnou verzi Pythonu (dříve 3.12.14); kód nebyl změněn.
- Oba archivní SHA-256 manifesty jsou úplné a jejich všech 46
  záznamů souhlasí. Tento obnovovací běh je **reprodukce**,
  ne nové nezávislé vědecké potvrzení a ne dvouarchitekturní gate.

## IX. Odkazy

- [Public Canon v103](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md)
- [POLICY](https://github.com/mathorn1973/twist-j/blob/main/POLICY.md)
- [CORE](https://github.com/mathorn1973/twist-j/blob/main/canon/CORE.md)
- [FRONTIER](https://github.com/mathorn1973/twist-j/blob/main/canon/FRONTIER.md)
- [Kleinovy invarianty, Nash](https://doi.org/10.1016/j.exmath.2013.09.003)
- [G16 a braidová grupa: Chavli](https://arxiv.org/abs/1504.02279)
- [PR #1577](https://github.com/mathorn1973/twist-j/pull/1577)
- [PR #1579](https://github.com/mathorn1973/twist-j/pull/1579)
- [PR #1581](https://github.com/mathorn1973/twist-j/pull/1581)

Vybrané úplné původní důkazy, zmrazené vstupy a zdrojové programy jsou v podsložkách `source-A/` a `source-B/`; originální archivy jsou doloženy otisky v `ORIGINS.md`. Tento
text není substitutem za jejich konkrétní číselné a grupové certifikáty.
