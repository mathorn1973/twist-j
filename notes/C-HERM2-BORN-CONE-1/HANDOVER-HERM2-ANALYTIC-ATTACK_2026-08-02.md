# HANDOVER, konsolidace přímého analytického útoku na Herm2(C)

Datum 2026-08-02. Status: NON-CANONICAL, kandidátní lane, kontejnerový běh mimo protokol na výslovný pokyn autora. Žádný zápis do repozitářů, žádná autorita. Nic níže nenese silnější štítek než candidate-T.

Poznámka o kontextu: pracovní tahy předchozí části session už nejsou v kontextu modelu. Tento dokument není opis ztracených tahů, je to rekonsolidace: celá páteř byla znovu ověřena jedním během.

Ověřovací běh (kontejner, python3 stdlib, deterministické seedy):

```
skript  herm2_consolidation_verify.py
        sha256 6e0bd75b3ec062e0c295fa571913ee265ef1cc52c99123561b84a145f54d8f0b, 15944 B
stdout  herm2_consolidation_verify_stdout.txt
        sha256 576f744d1b0a736d5428ef937d7ffaba921005d3e702729e4dbe72fbc6d6b220, 3706 B
výsledek 47/47 PASS, exit 0
```

Exaktní aritmetika (Fraction, $\mathbb Z[\zeta_5]$, $\mathbb Q(\sqrt5)$, komplexní racionály). Řádky označené "numeric witness" jsou svědci s uvedenou tolerancí, ne důkazy; každý takový svědek stojí na exaktní páteři uvedené vedle něj.

## Teze útoku

Kvadratické čtení rozdělené jedničky je $\operatorname{Herm}_2(\mathbb C)$, jeho kladný kužel je současně Bornův a kauzální, a $J$ na něm působí jako multiplikátor jednoho loxodromického Lorentzova kroku.

## Exaktně ověřená páteř (candidate-T)

1. Algebra $J$ v $\mathbb Z[\zeta_5]$: $J\bar J = 2-\varphi = \varphi^{-2}$ a současně $J+\bar J = J\bar J$, z čehož $\cos\arg J = (\varphi-1)/2$, tedy $\arg J = 2\pi/5$ exaktně, bez numeriky. Dále $J\varphi = j$, $(J-1)^3 = j$, $\operatorname{Tr} J = 3$, $N(J) = 1$. Moduly konjugátů: $\varphi^{-1}$ pro $a\in\{1,4\}$, $\varphi$ pro $a\in\{2,3\}$; dělení nese $\chi_5$. (Z1 až Z13)

2. $J^5 = 5\varphi-8 = \varphi^{-5}$, reálné a kladné, rozhodnuto celočíselně ($125>121$). Rotační část $J/|J|$ má proto přesný řád 5: pátá mocnina loxodromického kroku je čistý boost. Pět tiků čítače = jeden čistý boost. (Z7, Z8, Z11, L3)

3. $\det X = t^2-x^2-y^2-z^2$, dokázáno exaktně interpolační mřížkou $3^4$ (stupeň nejvýše 2 v každé proměnné). PSD kritérium pro $2\times2$: $X\succeq0 \iff t\ge0 \wedge \det X\ge0$; ekvivalence s minorovým kritériem ověřena exaktně, Bornova forma $v^\dagger X v$ je reálná a uvnitř kužele nikdy záporná. Bornův kužel = budoucí kauzální kužel; hranice $\det = 0$ jsou čisté stavy a nulové směry. (M1 až M3)

4. Boostová data J-kroku, celá v $\mathbb Q(\sqrt5)$: $\cosh\eta = \sqrt5/2$, $\sinh\eta = 1/2$, $\eta = \ln\varphi$, tedy $\beta^2 = 1/5$ a $\gamma = \sqrt5/2$. Rychlost J-kroku je $c/\sqrt5$. (B1 až B5)

5. Rigidita: $A_5$-invariantní symetrická forma na $1\oplus W$ má právě dva parametry, $a\,t^2 + b\,|\mathbf x|^2$ (charaktery, exaktně, A4). Invariance vůči jedinému J-boostu vynucuje $b = -a$, protože páka $\cosh\eta\sinh\eta = \sqrt5/4 \ne 0$; eukleidovská volba $b = a$ invariantní není. Minkowski je vynucen, ne vybrán. (B6 až B8, A4)

6. $\Lambda^2 W \cong W$ znak po znaku ve zlaté aritmetice a $\dim\operatorname{Hom}_{A_5}(\Lambda^2W, W) = 1$: jediná ekvivariantní závorka, vektorový součin. Věta o jedinečnosti pro "space is a commutator". (A1 až A3)

7. Zolotarev $p = 5$: $\det(m_a|_{W_5}) = \chi_5(a)$ exaktně, bit je orientace trojprostoru. Táž $\chi_5$ dělí moduly konjugátů $J$ (bod 1) a nese $L(1,\chi_5) = 2\ln\varphi/\sqrt5$ (numerický svědek, odchylka pod 1e-8, klasická formule třídového čísla). Trojrole bitu drží. (O1, O2, D1, Z12, Z13)

8. Cauchy a Binet: $\det\bigl(\sum_i w_i\psi_i\psi_i^\dagger\bigr) = \sum_{i<j} w_i w_j\,|\det(\psi_i,\psi_j)|^2$ exaktně; jedna větev dává $\det = 0$ (čistá = nulová, světelný okraj), nekolineární směs dává časupodobný vnitřek. Identita je přesná; čtení "hmota = nekolinearita" zůstává [H]. (CB1, CB2)

9. Loxodromický krok: $g_J = \operatorname{diag}(\sqrt J, 1/\sqrt J)$ působí $(u,v,w)\mapsto(|J|u,\ |J|^{-1}v,\ (J/|J|)\,w)$ a zachovává determinant (svědek na exaktní páteři bodů 1 a 2). (L1, L2)

10. Cesta A nad $\mathbb Q$ degeneruje: s triviální involucí je $vv^\dagger = vv^{T}$ identicky, fáze se nemá kde vzít. Oprava přes CM typ $\Phi = \{\sigma_1,\sigma_2\}$, $\Psi = (\sigma_1(\alpha), \sigma_2(\alpha))$, dělá $\Psi\Psi^\dagger$ a $\Psi\Psi^{T}$ genericky různé. (RA1, RA2)

## Tři nálezy k přenosu

### A. Aritmetická C4 nese pár, ne samotný Herm [candidate-T]

Galoisův generátor na CM spinoru je $\phi_g(z_1,z_2) = (z_2, \bar z_1)$: řád 4, smíšeně lineární (ani $\mathbb C$-lineární, ani antilineární; $\phi_g^2$ je globální konjugace). Indukovaná akce na kvadratických datech: $t$ pevné, $z\mapsto -z$, a na koherencích

$$ (w, s)\ \mapsto\ (s, \bar w), \qquad w = z_1\bar z_2\ \text{(Herm offdiag)},\quad s = z_1 z_2\ \text{(Sym offdiag)}, $$

čtyřcyklus $w\to s\to\bar w\to\bar s$. Herm sám o sobě Galois-stabilní není; stabilní je až pár $(\Psi\Psi^\dagger, \Psi\Psi^{T})$. Dvouslotový dekodér tedy není dodatečná oprava cesty A, je vynucen samotnou Galoisovou akcí. (G1, G2)

Korekce syntézy, sekce 4: rotoreflexe $S(t,z,w) = (t,-z,iw)$ je JINÁ realizace C4. Je geometrická: $S(X) = U X^{T} U^\dagger$ s $U \propto \begin{pmatrix}0&i\\1&0\end{pmatrix}$, spinorový zdvih $\psi\mapsto U\bar\psi$ je antiunitární a na spinorech má řád 8; $S^2 = R_z(\pi)$. Obě realizace mají regulární charakter $(4,0,0,0)$, ale jako strukturované akce se liší: $S$ zachovává Herm a je nevlastní prostorová, $\phi_g$ Herm nezachovává a cyklí jej se Sym. Ztotožnění "Galois = $S$ na Herm" v syntéze bylo nedokázané a je nesprávné. (C1 až C5 vs G1, G2)

### B. CM typ $\mathbb Q(\zeta_5)$ je jediný až na Galois [candidate-T]

Přesně 4 CM typy, všechny primitivní (jediné kvadratické podtěleso je reálné $\mathbb Q(\sqrt5)$, takže žádný typ není indukovaný), a $\operatorname{Gal}(K/\mathbb Q)$ na nich působí tranzitivně. Volba $\Phi = \{\sigma_1,\sigma_2\}$ není volný modul, jen Galoisův reprezentant. Tvrdý bod 2 je uzavřen na úrovni klasifikace. (K1)

### C. Galoisova čtvrtotáčka překlápí loxodromii na čistý boost [candidate-T, svědek]

$$ \phi_g\, g_J\, \phi_g^{-1} \;=\; \operatorname{diag}\!\bigl(1/\sqrt J,\ \overline{\sqrt J}\bigr), $$

multiplikátor $\varphi$, reálný: čistý expanzní boost, rotace je pohlcena smíšenou linearitou čtvrtotáčky. Reálné spektrum $\{s, \bar s, s^{-1}, \bar s^{-1}\}$ je zachováno; jde o konjugaci v $GL(4,\mathbb R)$, ne v konformní grupě, a přesně to je pointa: co je "rotace" a co "boost" rozhoduje komplexní struktura, a bit s ní hýbe. Souhlasí s $\chi_5$ dělením modulů konjugátů (kontrakce $\varphi^{-1}$ vs expanze $\varphi$). (L4, Z12, Z13)

## Stav čtyř tvrdých bodů

1. Společný nosič: zúženo, otevřeno. Kanonický kandidát je $K\otimes\mathbb R \cong \mathbb C^2$ s CM strukturou; Galoisova C4 na něm žije kanonicky (nález A). Zbývá realizovat veřejné $A_5$ a $g_J$ na TÉMŽ nosiči bez dalších voleb. Návrh: ikosianová cesta, binární ikosaedrická $2I$ je grupa jednotek zlatých kvaternionů nad $\mathbb Z[\varphi]$ a J-boost škáluje jednotkou $\varphi$, takže $\mathbb Z[\varphi]$-mřížka je přirozený společný domov. [O; falzifikátor: neexistence kompatibilního uložení $2I$ a $g_J$ na jednom $\mathbb Z[\varphi]$-modulu slučitelná s kvadratickým čtením shodí celý řetěz.]

2. CM typ: uzavřeno až na Galois (nález B).

3. Kladnost: redukováno na tvar dekodéru. Je-li registrovaný výstup tvaru $\sum_i w_i\psi_i\psi_i^\dagger$ s celočíselnými $w_i\ge0$, je kladnost věta (a hranice kužele jsou přesně čisté větve, CB2). [Falzifikátor: registrovaný výstup censusu mimo tento tvar.]

4. Prostorová vs vnitřní fáze: zpřesněno, nevyřešeno. V $\operatorname{Herm}_2$ je $\arg J$ prostorová rotace kolem osy boostu (malá grupa), ne vnitřní U(1). Vnitřní čtení míří na symetrický slot $\Psi\Psi^{T}$, který nese fázově citlivé párování a který Galois cyklí s Herm koherencí (nález A). Zůstává [H]; slovník je samostatná sonda.

## Návrh dalších sond (názvy pro claim)

```
P-COMMON-CARRIER-ICOSIAN-1   A5 (pres 2I v ikosianech) a g_J na jednom
                             Z[phi]-nosici; falzifikator: neexistence
                             kompatibilniho ulozeni.
P-DECODER-SOS-FORM-1         censusovy vystup D_matter je soucet vazenych
                             ctvercu sum w psi psi†; falzifikator:
                             registrovane pole mimo tento tvar.
P-U1-DICTIONARY-1            presny slovnik arg J: prostorova mala grupa vs
                             vnitrni U(1) na symetrickem slotu; falzifikator:
                             predikce vazby, ktera selze na registrovanych
                             datech.
```

## Co vzít s sebou

Teze žije a je po konsolidaci ostřejší: nosičem kvadratického čtení je pár $(\Psi\Psi^\dagger, \Psi\Psi^{T})$, kužel je jeden (Bornův = kauzální), a $J$ je jeden loxodromický krok, jehož pátá mocnina je čistý boost rychlosti $c/\sqrt5$. Soubory k přenosu: tento dokument, verifikační skript, stdout. Tato session nemůže zapisovat do /mnt/project; přenos do claude/ lane proveď ručně nebo v další session. Verifikátor je samonosný, poběží kdekoli na python3 stdlib.
