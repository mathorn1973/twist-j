# Trojlístek: co dokáže kontakt a jak správně označit meridiány

**Výzkumná návaznost, 17. října 2026. NON-CANONICAL, matematická vrstva L1.**

Tato poznámka navazuje na dříve ověřený přechod od značené binární
ikosaedrické grupy ke Kleinovým invariantům a trojlístkové větvi.
Zkoumá konkrétní současné operace TWIST-J a přesné geometrické značení.
Hlavní nové doplnění je dvojí: univerzální překážka pro věrné 2I po
přidání již deklarované čtecí vazby a výslovná oprava kladných meridiánů
skutečného Kleinova pokrytí.

## 1. Hlavní výsledky

| Přesně zkoumaný objekt | Výsledek | Význam |
|---|---|---|
| Celé hotové čtečky A_x, A_y | Grupa C5 × C5; čtečky komutují | Právě tato dvojice netvoří necyklický meridiánový obraz |
| M=Ucal, N=e Ucal e na jedné celé buňce | Přesná grupa S3, meridiány řádu 2 | Dodaná čtecí vazba dovoluje necyklickou trojlístkovou reprezentaci |
| Všechna pevná slova z a,b,c,d,e,Ucal | Každá akce 2I zabije centrální −I | V této celé třídě neexistuje věrné binární ikosaedrické působení |
| Skutečné původní U a přesně vymezené řízení faktorem χ=(z,r) | Neumí přesnou úplnou Ucal | Dodané čtení q do r není odvozené z tohoto původního vývoje |
| C=A², D=B³ ve značené komplexní grupě | Grupa 2I, (CD)³=−I | Správné determinantově jednotkové složky kladné geometrické dvojice |
| R1=j³C, R2=j³D | Kladná geometrická monodromie G16, řád 600 | Výslovná vazba na skutečné pětičetné Kleinovo větvení |

První a čtvrtý bod jsou přímé analytické důsledky stávajících definic;
nepřejmenovávají dřívější kontaktní výsledky na nové objevy. Základní
grupa 2I řádu 120, její Kleinovy invarianty a původní maticové součtové
styky jsou převzaté z dřívější práce. Nové jsou zde konkrétní kontaktní
dvojice, univerzální centrální mez a opravené geometrické značení.

## 2. Přesná kontaktní konstrukce

Jedna úplná buňka má stav

\[
x=(p,q,r)\in\mathbb F_5^4\times\mathbb F_5\times\mathbb F_5.
\]

Původní e působí jako

\[
e(p,q,r)=((2,1,3,4)-p,\,2-q,\,1-r).
\]

Již deklarovaná dodatečná vazba Ucal mění pouze r, podle pevné tabulky
P_q. Nejde o autonomní U. Pro

\[
M=\mathcal U,\qquad N=e\mathcal U e
\]

obě operace přesně obnoví p a q. Na r mají tabulku:

| q | M | N |
|---|---|---|
| 0 | (1 2) | (1 4) |
| 1 | I | I |
| 2 | (0 2) | (0 4) |
| 3 | (0 1) | (0 1) |
| 4 | (0 1) | (0 1) |

Zápis (1 2) znamená transpozici hodnot 1 a 2; ostatní hodnoty zůstávají
pevné. Na q=0 jsou to dvě transpozice se společným bodem. Na celé buňce
proto platí

\[
M^2=N^2=I,\qquad MNM=NMN,\qquad (MN)^3=I,
\qquad\langle M,N\rangle\cong S_3.
\]

Platnost zahrnuje všechny obsazené hodnoty r. Tato reprezentace je
přesná, avšak její existence neidentifikuje žádnou souřadnici s fyzikální
prostorovou křivkou. Obrazy meridiánů mají řád dva.

## 3. Proč tento přídavek stále nedává věrné 2I

Označme

\[
\Gamma_+=\langle a,b,c,d,e,\mathcal U\rangle.
\]

Z původních definic plyne pro každé pevné slovo, bez omezení délky,

\[
q'=\varepsilon q+c,\qquad r'=\pi_q(r),\qquad
p'=Lp+t(q,r),\qquad L\in C_2^3.
\]

Tento tvar je uzavřený na skládání i inverzi. Akce na q je dihedrální
grupa řádu deset. Po jejím odstranění zbývá pět permutačních akcí na
pětiprvkovém r. Jádro akce na q,r a L tvoří posuny p závislé na q,r;
je podgrupou elementární abelovské 5-grupy o řádu nejvýše 5^100.

Grupa 2I=SL2(F5) je dokonalá. Každá její akce v abelovské pístové
lineární grupě nebo v dihedrální grupě q je tedy triviální. Každá akce
2I na pěti bodech navíc zabije centrální −I: případný netriviální obraz
by byl dvojitou transpozicí v A5, jejíž centralizátor je abelovská
čtyřgrupa. Dokonalý obraz v ní nemůže přežít.

Obraz −I tudíž musí ležet v pístovém 5-jádře. Současně má řád dělící
dvě. Musí být identitou:

\[
\boxed{\rho(-I)=I\quad
\text{pro každé }\rho:\mathrm{SL}_2(\mathbb F_5)\to\Gamma_+.}
\]

Jde o překážku pro všechna pevná slova této přesné třídy. Není to
neúspěšné hledání do konečné délky a nepředpokládá se řešitelnost celé
Gamma_plus. Tatáž mez platí pro oddělené buňky s pouhými slotovými
operacemi, protože jejich grupa leží v přímém součinu těchto grup.

Úplné společné součty, W_b, nové stavové řízení či nové permutace adres
nejsou v této třídě. Jejich připuštění vyžaduje vlastní odůvodnění.

## 4. Konkrétní oprava geometrického značení

Ponecháváme původní komplexní vložení

\[
j=e^{2\pi i/5},\quad a=j+j^4,\quad s=j^2-j^3,
\quad a^2+a=1.
\]

Původní abstraktní meridiánová dvojice je

\[
A=\begin{pmatrix}j&1\\0&j^4\end{pmatrix},\qquad
B=\begin{pmatrix}j^4&0\\-1&j\end{pmatrix}.
\]

Kladný lokální oběh větvení řádu pět musí mít normálovou vlastní
hodnotu j a tečnou vlastní hodnotu 1. Původní A tento požadavek po
nutném skaláru j³ nesplní:

\[
\det(j^3A-I)=2+2j+j^3\ne0.
\]

Matice jA je odraz, ale s netriviální vlastní hodnotou j², tedy druhou
mocninou lokální monodromie. Upřesnění se týká tohoto geometrického
značení; původní abstraktní reprezentace zůstává platná.

Předepsaná oprava je

\[
C=A^2=\begin{pmatrix}j^2&a\\0&j^3\end{pmatrix},\qquad
D=B^3=\begin{pmatrix}j^2&0\\a&j^3\end{pmatrix}.
\]

Platí CDC=DCD, C^5=D^5=I a (CD)^3=−I. Z rovností C³=A, D²=B se
obnoví původní grupa H=2I, řád 120. Kladné odrazy jsou

\[
R_1=j^3C=\begin{pmatrix}1&j^3a\\0&j\end{pmatrix},\qquad
R_2=j^3D=\begin{pmatrix}1&0\\j^3a&j\end{pmatrix}.
\]

Oba mají spektrum {1,j}. Jejich centra dávají

\[
(R_1R_2)^3=-j^3I,\qquad (R_1R_2)^6=jI.
\]

Obnoví se tedy celý skalární C5 i H. Výsledná grupa je

\[
\langle R_1,R_2\rangle=G_{16}\cong 2I\times C_5,
\qquad |G_{16}|=600.
\]

Výslovný Galoisův vztah ke starému značení poskytuje jednotková
integrální matice

\[
Q=\begin{pmatrix}a&0\\-s&1\end{pmatrix},\qquad
Q^{-1}=\begin{pmatrix}a+1&0\\s(a+1)&1\end{pmatrix},
\]

pro niž Q sigma3(A) Q^{-1}=C a Q sigma3(B) Q^{-1}=D, kde
sigma3(j)=j³. J, metrika ani fyzikální čtení se tím nepřepisují.

## 5. Jde o skutečné Kleinovo pokrytí

Přijaté invarianty stupňů 12, 20, 30 splňují

\[
w^2+h^3=1728f^5.
\]

Skalární C5 zachovává h,w a působí netriviálně na f. Proto

\[
\mathbb C[V]^{G_{16}}=\mathbb C[h,w].
\]

Kvocient v↦(h(v),w(v)) má diskriminant w²+h³=0. Link tohoto
komplexního hrotu je trojlístek T(2,3). Mezilehlý kvocient přes 2I
je pětičetné pokrytí s lokálním působením f↦jf. Přesně tento
charakter mají R1,R2.

Samotný charakter f ještě nefixuje společné přístupové cesty.
Soubor geometry/PROOF.md proto doplňuje skutečnou geometrickou
prezentaci komplementu, samostatný důkaz jednoznačnosti ireducibilní
dvourozměrné dvojice a normalizátor 2I. Z jejich spojení plyne
existence kladné geometrické generující dvojice s obrazy právě R1,R2,
po společné volbě základního listu. Není předepsána jediná
parametrizace cest. Dřívější bod v0 na f=0 není základním bodem
komplementu.

## 6. Opravená dvojice na úplných součtových stycích

Redukce modulo lambda=1−j dává

\[
C_0=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
D_0=\begin{pmatrix}1&0\\2&1\end{pmatrix}.
\]

Pro původní A0=[[1,1],[0,1]], B0=[[1,0],[-1,1]] jde o
C0=A0² a D0=B0³; současné sdružení provádí diag(2,1).

Ve skutečné dodané abecedě úplných dvoubuněčných součtů
P(x,y)=(x,y+x), Q_cs(x,y)=(x+y,y) tedy opravené operace jsou

\[
\mathcal C=Q_{\rm cs}^2:(x,y)\mapsto(x+2y,y),\qquad
\mathcal D=P^2:(x,y)\mapsto(x,y+2x).
\]

Zde x,y jsou celé šestice nad F5. Matice působí stejně na každou
odpovídající dvojici souřadnic, takže maticové identity jsou doslovné
identity na všech dvanácti souřadnicích. Zejména

\[
\mathcal C\mathcal D\mathcal C=\mathcal D\mathcal C\mathcal D,
\qquad
(\mathcal C\mathcal D)^3(x,y)=(-x,-y).
\]

Tento poslední prvek je netriviální na úplném nosiči. Právě jeho
zachování odlišuje binární působení od faktorů, v nichž centrum zmizí.
Tato část je komponentový důsledek zmrazených maticových identit F6,
ne další hledání kandidáta nebo nové připuštění úplných součtů.

## 7. Co je ještě otevřené pro protonový výklad

Matematický trojlístek je zde přesný objekt geometrie větvení.
Prostorový nosič v původním autonomním vývoji, nezávisle připuštěný
fyzikální kontakt, stabilita, energie a čtení hmotnosti zůstávají
samostatné úkoly. Samotné S3, samotné 2I ani přítomnost −I nejsou
odvozením protonu nebo jeho fyzikálního spinu.

Konkrétní výsledek této práce určuje užší další otázku: jakou skutečně
připuštěnou interakcí lze na úplném nosiči uskutečnit uvedenou
geometricky označenou dvojici a zachovat její centrální operaci.
Pouhé prodlužování pevných jednobuňkových slov ze šesti zkoumaných
map tuto otázku nevyřeší — vylučuje je obecná věta.

## 8. Součásti balíčku a opakování

- PREREG.md a FREEZE.json: přesné cíle a hashe před prvním novým během.
- contact/PROOF.md, contact/CONTRACTS.md: kontaktní důkazy a kontrolní cíle.
- geometry/PROOF.md, geometry/PREREG_CONTRACT_DRAFT.md: geometrické důkazy,
  zdroje a cíle přijaté společným PREREG.
- contact/verify.py a geometry/verify.py: dvě autorské části.
- independent/verify.py a independent/REVIEW.md: oddělená implementace
  a analytická kontrola vytvořené bez nových autorských kódů a výstupů.
- IMPLEMENTATIONS.json: zdrojové hashe všech ověřovačů před spuštěním.
- runs/: zachované první stdout, stderr a provozní záznamy.
- EVIDENCE.md: skutečné výsledky běhů, jejich rozsah a případné námitky.
- SOURCES.md: připnuté veřejné a primární matematické zdroje.

Skripty vyžadují Python 3.8 nebo novější a standardní knihovnu. Lze je spustit
přímo, například `python3 geometry/verify.py`. Pro nové zachycení
výstupů použijte `python3 run_check.py geometry --run-id replay01`;
analogicky pro contact a independent. Zadaný adresář běhu nesmí
existovat, aby se první záznamy nemohly přepsat.

Počty úspěšných kontrol jsou konečné certifikáty podpírající důkazy.
Jde o místní kontrolu a oddělenou implementaci v rámci téže relace,
nikoli o veřejné dvouarchitekturní přijetí nebo vnější vědeckou recenzi.
