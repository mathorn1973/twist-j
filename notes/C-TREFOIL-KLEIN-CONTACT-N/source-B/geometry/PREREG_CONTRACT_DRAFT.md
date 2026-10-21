# Návrh konečného kontraktu: kladné geometrické meridiány

**Stav:** návrh předregistrace, dosud nezmrazený kořenem úlohy. Žádný nový vědecký běh v této analytické větvi zatím nebyl proveden. Před spuštěním musí být přesný přijatý obsah a obě implementace připnuty společným protokolem.

## Nosič a konvence

- Přesná aritmetika v \(K=\mathbb Q[j]/(1+j+j^2+j^3+j^4)\); hlavní matice mají koeficienty v \(\mathbb Z[j]\).
- Kladné geometrické vložení \(j=\exp(2\pi i/5)\); žádná plovoucí aproximace nerozhoduje rovnost ani kladnost.
- Sloupcové vektory, matice působí zleva. Lokální kladný zdvih mapy \(z\mapsto z^5\) končí v \(jz\).
- \(a=j+j^4\), \(s=j^2-j^3\), \(\lambda=1-j\), \(\sigma_3(j)=j^3\).
- \(S=[[0,-1],[1,0]]\), \(A=[[j,1],[0,j^4]]\), \(B=SAS^{-1}\).
- Zmrazené kandidáty: \(C=A^2\), \(D=B^3\), \(Q=[[a,0],[-s,1]]\), \(R_1=j^3C\), \(R_2=j^3D\).
- Dříve ověřený řád \(|\langle A,B\rangle|=120\) je přijatý vstup, nikoli nový výsledek. Nové generování se kontroluje konečnými slovními certifikáty; nové vyčerpávající hledání matice nebo dvojice není součástí kontraktu.

## F0 — základní přesné identity

Ověřit \(a^2+a=1\), \(s^2=a-2\), \(a(a+1)=1\), \(j^2+j^3=-a-1\). Ověřit explicitní tvar \(B=[[j^4,0],[-1,j]]\).

## F1 — záporný svědek původního geometrického značení

Ověřit

\[
\det(j^3A-I)=2+2j+j^3\ne0,
\qquad\operatorname{tr}(A)=a,
\qquad\operatorname{tr}(C)=-a-1\ne a.
\]

Ověřit charakteristický polynom \(jA\): \((X-1)(X-j^2)\), tedy determinant \(j^2\). Tato kontrola musí projít jako **očekávané vyvrácení** možnosti použít \(j^3A\) coby kladný odraz. Selhání původního kandidáta není označeno jako neúspěch opravené dvojice.

## F2 — explicitní determinantově jednotková dvojice

Ověřit

\[
C=\begin{pmatrix}j^2&a\\0&j^3\end{pmatrix},
\quad
D=\begin{pmatrix}j^2&0\\a&j^3\end{pmatrix},
\]

\[
CDC=DCD,\quad C\ne D,\quad C^5=D^5=I,
\quad\det C=\det D=1,
\]

\[
\operatorname{tr}(CD)=1,\quad (CD)^2-CD+I=0,
\quad(CD)^3=-I.
\]

Ověřit \(C^3=A\), \(D^2=B\). Tyto rovnosti spolu s definicí C,D certifikují rovnost generovaných podgrup a převzetí řádu 120.

Ověřit

\[
CD-DC=\begin{pmatrix}a^2&-as\\-as&-a^2\end{pmatrix},
\qquad\det(CD-DC)=a^2\ne0.
\]

Tento determinant je certifikát ireducibility, nikoli náhrada obecné klasifikační věty.

## F3 — kladné odrazy a celé centrum

Ověřit explicitní matice

\[
R_1=\begin{pmatrix}1&j^3a\\0&j\end{pmatrix},
\quad
R_2=\begin{pmatrix}1&0\\j^3a&j\end{pmatrix}.
\]

Pro každou ověřit \(\chi_{R_i}(X)=(X-1)(X-j)\), \(R_i\ne I\), \(\det(R_i-I)=0\), \(\det R_i=j\), \(R_i^5=I\). Tím je certifikována hodnost jedna a přesný řád pět.

Ověřit

\[
R_1R_2R_1=R_2R_1R_2,
\quad (R_1R_2)^3=-j^3I,
\quad (R_1R_2)^6=jI,
\]

\[
C=j^2R_1,\qquad D=j^2R_2.
\]

Poslední tři rovnosti jsou generující certifikát pro celou \(G=\mu_5H\). Řád 600 následuje důkazem z \(|H|=120\) a triviálního průniku \(H\cap\mu_5\), nikoli z nezmrazeného hledání či z numerické tolerance.

## F4 — integrální Galoisův převod

Ověřit

\[
Q^{-1}=\begin{pmatrix}a+1&0\\s(a+1)&1\end{pmatrix},
\quad QQ^{-1}=Q^{-1}Q=I,
\quad\det Q=a.
\]

Ověřit po koeficientech \(\sigma_3(j)=j^3\), \(\sigma_3^4=\operatorname{id}\), a rovnosti

\[
Q\sigma_3(A)Q^{-1}=C,\qquad Q\sigma_3(B)Q^{-1}=D,
\]

\[
Q\sigma_3(jA)Q^{-1}=R_1,\qquad Q\sigma_3(jB)Q^{-1}=R_2.
\]

Koeficienty Q i předepsané inverze musejí být celočíselné v bázi \(1,j,j^2,j^3\). Invertibilita a jednotkovost determinantu jsou dány výslovnou inverzí.

## F5 — charakter konkrétní formy stupně dvanáct

Zmrazit polynom

\[
f_0(x,y)=xy(x^{10}+11x^5y^5-y^{10}),
\quad f(u,v)=f_0(su+av,v).
\]

Ověřit koeficientově \(f\ne0\), homogenitu stupně 12 a

\[
f(Cv)=f(v),\quad f(Dv)=f(v),
\quad f(R_1v)=jf(v),\quad f(R_2v)=jf(v),
\]

\[
f(jAv)=j^2f(v).
\]

Ověřit váhy vyšších stupňů \((j^3)^{20}=(j^3)^{30}=1\) a \((j^3)^{12}=j\). Plné opakované vytváření forem stupňů 20 a 30 a nové přepočítávání Kleinovy rovnice nejsou součástí tohoto úzkého testu; přebírají se z předchozí ověřené souřadnicové práce. Nový charakter f musí být ověřen na konkrétním polynomu, nejen na číslech stupňů.

## F6 — přesná redukce u lambda

Použít jediné předepsané zobrazení \(\mathcal O\to\mathbb F_5\), \(j\mapsto1\). Neslučovat \(\mathcal O/(5)\) se zbytkovým tělesem \(\mathcal O/(1-j)\).

Ověřit

\[
\bar a=2,\quad\bar s=0,\quad
\bar Q=K_0=\operatorname{diag}(2,1),\quad
\overline{Q^{-1}}=\operatorname{diag}(3,1).
\]

Pro \(A_0=[[1,1],[0,1]]\), \(B_0=[[1,0],[-1,1]]\) ověřit

\[
\bar C=\bar R_1=A_0^2=K_0A_0K_0^{-1}
=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\]

\[
\bar D=\bar R_2=B_0^3=K_0B_0K_0^{-1}
=\begin{pmatrix}1&0\\2&1\end{pmatrix}.
\]

Ověřit jejich braid relaci a \((\bar C\bar D)^3=-I\). Tyto konečné identity samy neudělují fyzikální přípustnost \(K_0\).

## Co se rozhoduje důkazem a kontrolou zdrojů

Následující části nejsou vydávány za závěr strojového vyčerpání:

1. \(\mathbb C[V]^G=\mathbb C[h,w]\) a identifikace skutečného Kleinova pokrytí — plyne z přijatého invariantního okruhu a charakteru μ5.
2. Identifikace \(G\) s \(G_{16}\), geometrická prezentace komplementu a význam kladného odrazu — primární Chavli a Broué.
3. Jednoznačnost ireducibilní dvojice rozměru dva — samostatný trace důkaz v PROOF.md, opora Tuba–Wenzl 2.9(a).
4. Vnitřní povaha sdružení dvou geometrických dvojic — normalizátor \(2I\), Kollár příklad 7.
5. Existence kladných geometrických generátorů s obrazy přesně R1,R2 — kombinace bodů 1–4. Není tvrzena konkrétní předem předepsaná parametrizace cest a bod na větvení není základním bodem komplementu.

## Pravidlo ukončení a změn

Každá nepravdivá předepsaná rovnost nebo nesplněná nenulovost ukončí příslušnou kontrolu jako FAIL; hodnoty se po běhu nedolaďují. Změna kandidátů, mocnin, základního kořene nebo konvence vyžaduje novou verzi kontraktu s výslovně zaznamenaným důvodem. Kontroly popisují konečné algebraické rovnosti; žádný počet PASS se nevydává za důkaz nativní nebo fyzikální přípustnosti.
