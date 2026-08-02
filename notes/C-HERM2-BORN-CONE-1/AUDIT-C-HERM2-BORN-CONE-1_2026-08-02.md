# AUDIT C-HERM2-BORN-CONE-1, 2026-08-02 (accepted)

NON-CANONICAL. Accepted external audit of the Herm2 consolidation
bundle, received from the author 2026-08-02, recorded verbatim below.
Where this audit and the bundle's earlier prose disagree, THIS AUDIT
SUPERSEDES the prose labels. Machine verification of the audit's exact
claims lives in two follow-up bundles:

```text
notes/C-CENTRAL-LIFT-PHASE-1     gates CP1-CP16
notes/C-CM-2I-QCARRIER-1         gates Q1-Q10
```

## Acceptance map

- Correction 1 (branch of arg J): ACCEPTED, machine-checked as CP1-CP2.
  The cosine data is branch-blind; the polarization J phi = zeta5 pins
  arg J = +2 pi/5. Gate Z2 of the bundle verifier is re-graded: its
  wording overstates; the exact content is Z2 + Z5 together.
- Correction 2 (five ticks projective): ACCEPTED, machine-checked as
  CP3-CP4 (zeta10^5 = -1 exactly). "Five ticks = one pure boost" holds
  in the projective Herm action; the spinor clears the central sign at
  ten. The physical-tick identification stays [candidate-D].
- Correction 3 (PSD cone proof): ACCEPTED, machine-checked as CP5-CP6.
  M2/M3 are re-graded from proof to audited witness; the equivalence
  X >= 0 iff (t >= 0 and det X >= 0) is theorem-grade via the char-poly
  grid identity plus the 2x2 sum/product sign lemma. Boundary
  refinement (rank one = pure = null ray; the origin is boundary but
  not a normalized state) accepted.
- Correction 4 (rigidity conditional): ACCEPTED, machine-checked as
  CP16. The b = -a forcing is a grid-proved polynomial identity; the
  common-carrier hypothesis is discharged at candidate level by
  notes/C-COMMON-CARRIER-ICOSIAN-1 (same quadratic coordinates carry
  the right 2I action and the glued J-boost).
- Correction 5 (unique bracket is not a curvature operator): ACCEPTED
  as scoping; CURVATURE-OPERATOR-CANONICAL remains open; fired
  dynamics is spatially abelian; no gate needed.
- Correction 6 (chi5 triple role; bit = quotient of C4): ACCEPTED.
  ker chi5 = {1, 4}; the bit distinguishes the contraction and
  expansion classes and forgets the position inside each conjugate
  pair. The follow-up gate Q10 sharpens this to a marking theorem on
  the registered integral lift.
- Findings A, B, C: ACCEPTED with the audit's refinements (A: the pair
  is the natural Galois closure of the Herm orbit, uniqueness of the
  decoder NOT claimed; B: classification closed, orientation open;
  C: projective phrasing).
- Hidden fourth finding (projective Herm slot, central Sym phase):
  ACCEPTED and machine-checked as CP7-CP12, with one extension: the
  unit-scalar central phase group is exactly mu_5, and the tenth-root
  phase 1 - J of the integral even tick escapes it by the central
  sign (mu_10 vs mu_5) -- the bit rides only the glued integral step.
- Common-carrier section: PARTIALLY SUPERSEDED by later work. The
  audit's "A_J = diag(J, 1) in GL2(O_K), existence essentially done"
  is correct for the free module with a chosen basis, but on the
  canonical h-split carrier NO unit rescaling of diag(J, 1) is
  integral (gate CP14; the ramified glue criterion of
  C-COMMON-CARRIER-ICOSIAN-1). The integral common-carrier statement
  is the icosian bundle; H0 = sum g-dagger g is computed exactly and
  its uniqueness up to an F-scalar is machine-checked there (Q7-Q9).
- Probe reordering: ADOPTED. C-CM-2I-QCARRIER-1 carries the first
  exact slice of P-CM-2I-QCARRIER-1 (the C4 descent dichotomy);
  C-CENTRAL-LIFT-PHASE-1 carries the theorem-grade central-phase
  content proposed for P-CENTRAL-LIFT-PHASE-1; P-DECODER-SOS-FORM-1
  stays deferred while QUADRATIC-DECODER-DATA is STOP.
- One refinement OF the audit (from the follow-up work): the
  compatibility trichotomy for the arithmetic C4 on the registered
  lift resolves neither to EMPTY nor to UNIQUE. Exactly: the chi5
  kernel descends with markings intact, the nontrivial coset descends
  only through the outer automorphism swapping the golden classes
  5a <-> 5b, and the branch pair 2a + 2b is fully C4-stable
  (Q-valued character). The Galois branches of the lift meet exactly
  in {+-I, +-S}, the geometric C4 (gates Q2-Q6, Q10).
- Reproduction status: ACCEPTED as [REPRODUCTION], same architecture,
  not a public computation gate; consistent with this bundle's README.

No falsifier fired by this audit. No threshold moved. PROMO deferred.

## Audit text (verbatim, as received; formatting preserved)

# Verdikt
**Status: PUBLIC basis, NON-CANONICAL audit. Bez propagace statusu a bez změny repozitáře.**
Interní `mathorn1973/twistj-jam` HEAD jsem v tomto prostředí neověřil, takže nečiním žádný výrok o interní aktuálnosti. Veřejná autorita je nyní **Public Canon v30**, tag `canon-v30`, content commit `857223fcd5e7bc8c8e68f1df768d6e8222b24ee0`. Veřejný Canon současně výslovně říká, že checkpoint, pět generátorů, selektor ani decoder nejsou zatím jednoznačně odvozeny z (J), a že totalita, jednoznačnost a úplnost decoderu zůstávají otevřené.
**Celkový vědecký verdikt:** páteř útoku žije. Nejsilnější nový výsledek není prosté „(\operatorname{Herm}_2) je decoder", ale toto:
[
\boxed{\text{Aritmetická }C_4\text{ neuzavírá samotný Herm slot. Uzavírá pár }
Q(\Psi)=\bigl(\Psi\Psi^\dagger,\Psi\Psi^T\bigr).}
]
To přesně zasahuje veřejný otevřený bod `QUADRATIC-DECODER-DATA`, který již tento pár uvádí jako požadovaný faktor. Handover však tento bod ještě nezavírá. Chybí veřejný společný totální obor, koeficientový okruh, Gram, orbit-to-amplitude bridge, effects, Born pairing, MatterData schema, přesná write mapa a úplný dependency graph. Řádek je stále `O / STOP`.
## Reprodukce artefaktu
Lokální opakovaný běh dopadl byte-identicky:
```text
handover SHA-256:
df657b3b8990a82bbae67fe6ef8da92b1b0ced51446210b5a32ff3fee82231b0
verifier SHA-256:
6e0bd75b3ec062e0c295fa571913ee265ef1cc52c99123561b84a145f54d8f0b
stdout SHA-256:
576f744d1b0a736d5428ef937d7ffaba921005d3e702729e4dbe72fbc6d6b220
result:
47/47 PASS
exit code 0
stderr empty
rerun stdout byte-identical
```
**Status: [REPRODUCTION].** Není to nezávislá konfirmace ani veřejná computation gate. Veřejná politika výslovně stanoví, že shoda na stejné architektuře je jen reprodukce a jednoarchitekturní konečný výsledek je nejvýše `C`, pokud nemá samostatný theorem-grade důkaz.
Navíc „47 exact PASS" neznamená 47 důkazů. Některé řádky používají exaktní aritmetiku na náhodně zvolených bodech. To je přesný svědek, nikoli důkaz univerzální identity. Dobrá zpráva je, že pro hlavní takové řádky existují krátké skutečné důkazy.
# Povinné opravy handoveru
## 1. Znaménko argumentu (J)
**Status: [candidate-T po opravě].**
Z identity
[
J+\bar J=J\bar J
]
dostaneme
[
\cos(\arg J)=\frac{\varphi-1}{2},
]
ale samotný kosinus určuje pouze
[
\arg J=\pm\frac{2\pi}{5}\pmod{2\pi}.
]
Kladkou hlavní větev určuje až další exaktní identita
[
J\varphi=j=\zeta_5,
\qquad \varphi>0,
]
případně přímo zvolená embeddingová orientace (\operatorname{Im}J>0). Správná důkazní věta je tedy:
[
J\bar J=J+\bar J=\varphi^{-2},
\qquad
J\varphi=j
\quad\Longrightarrow\quad
J=\varphi^{-1}j,
]
a proto
[
\arg J=\frac{2\pi}{5}.
]
Veřejný Canon používá právě přímou polarizaci (J=2\cos(2\pi/5)e^{2\pi i/5}), nikoli kosinus bez orientace.
## 2. Pět kroků: Lorentz ano, spinor pouze projektivně
**Status: [candidate-T].**
Je správně, že
[
J^5=5\varphi-8=\varphi^{-5}>0.
]
Je-li ale
[
g_J=\operatorname{diag}(s,s^{-1}),
\qquad s^2=J,
]
pak pro hlavní odmocninu (\arg s=\pi/5) platí
[
g_J^5 = -\operatorname{diag}!\left(\varphi^{-5/2},\varphi^{5/2}\right).
]
Tedy:
* na (\operatorname{Herm}_2), kde centrální (-I) působí triviálně, je pátá mocnina **čistý boost**;
* na spinoru zůstává po pěti krocích centrální znaménko (-I);
* na spinoru se znaménko odstraní až po deseti krocích.
Přesná věta tedy zní:
[
\boxed{g_J^5\text{ je čistý boost v projektivní Lorentzově akci, nikoli doslova kladný spinorový boost.}}
]
A věta „pět tiků čítače = jeden čistý boost" má status pouze `[candidate-D]`, dokud je výslovně deklarováno, že jeden fyzikální tick realizuje právě tuto Hermitovskou akci (g_J). Veřejný kernelový update není obecně pouhé násobení (g_J).
## 3. PSD kužel: tvrzení je věta, ale současný M2 není její důkaz
**Status: [candidate-T po nahrazení náhodného testu důkazem].**
Pro
[
X=
\begin{pmatrix}
t+z & x-iy\
x+iy & t-z
\end{pmatrix}
]
platí
[
\det X=t^2-x^2-y^2-z^2.
]
Jestliže (X\succeq0), pak (\operatorname{tr}X=2t\ge0) a (\det X\ge0).
Obráceně, jestliže
[
t\ge0,\qquad
t^2-x^2-y^2-z^2\ge0,
]
pak
[
t\ge\sqrt{x^2+y^2+z^2}\ge |z|,
]
tedy
[
t+z\ge0,\qquad t-z\ge0.
]
Oba diagonální minory i determinant jsou nezáporné, takže podle minorového kritéria pro Hermitovskou (2\times2) matici platí (X\succeq0).
Proto skutečně
[
\boxed{
X\succeq0
\iff
t\ge0\ \land\ t^2-x^2-y^2-z^2\ge0.
}
]
A následně
[
v^\dagger Xv\ge0
]
pro všechna (v) plyne přímo z definice pozitivní semidefinitnosti. Náhodné racionální testy M2 a M3 lze ponechat jako audit, ale ne jako důkaz.
Je třeba také zpřesnit hranici:
[
\det X=0,\quad X\neq0,\quad X\succeq0
]
znamená rank jedna, tedy čistý stav a nenulový budoucí nulový paprsek. Počátek (X=0) je rovněž na hranici, ale není normalizovaným čistým stavem.
## 4. Minkowskiho rigidita je podmíněná společným nosičem
**Status: [candidate-T, conditional].**
Z (A_5)-invariance na (1\oplus W) skutečně plyne dvouparametrická rodina
[
q(t,\mathbf x)=a,t^2+b,|\mathbf x|^2.
]
Pro jeden netriviální standardní boost
[
B=
\begin{pmatrix}
c&s\
s&c
\end{pmatrix},
\qquad cs\neq0,
]
je mimodiagonální člen v (B^T\operatorname{diag}(a,b)B)
[
cs(a+b).
]
Invariance proto vynucuje
[
b=-a.
]
To je čistý theorem-grade lemma:
[
\boxed{
A_5\text{-izotropie}+\text{jeden netriviální boost}
\Longrightarrow
q\sim t^2-|\mathbf x|^2.
}
]
Globální věta „Minkowski je v TWIST-J vynucen" však vyžaduje, aby veřejné (A_5) a konkrétní (J)-boost byly umístěny na témž označeném nosiči se stejným rozkladem (1\oplus W). Bez tohoto mostu je výrok podmíněný.
## 5. Jediná závorka neznamená jediný curvature operator
**Status: [candidate-T algebra, O fyzikální konstrukce].**
Platí
[
\Lambda^2W\cong W,
\qquad
\dim\operatorname{Hom}_{A_5}(\Lambda^2W,W)=1.
]
To přesně znamená:
[
\boxed{
\text{Každá }A_5\text{-ekvivariantní alternující bilineární mapa }
W\times W\to W
\text{ je násobkem vektorového součinu.}
}
]
Neurčuje to však:
* normalizaci závorky,
* nosič, na němž je realizována,
* projekci z kernelu,
* míru,
* ambientní versus intrinsický komutátor,
* konkrétní curvature operator.
Veřejný Canon navíc dokazuje, že skutečně firing generátory (b,d,e) mají komutátory pouze ve fiber translation plane, s nulovou pistonovou složkou. Fired dynamics je tedy prostorově abelovská. `CURVATURE-OPERATOR-CANONICAL` zůstává otevřený.
Výsledek o (\Lambda^2W) je velmi cenný, ale jeho přesný význam je:
> Jestliže prostorový komutátor existuje jako (A_5)-ekvivariantní alternující mapa na (W), jeho tvar je jediný až na skalár.
Není to ještě existence ani kanonická volba takové mapy z veřejného kernelu.
## 6. Trojrole (\chi_5) je shoda struktur, zatím ne jedna fyzikální identita
**Status: [candidate-T jednotlivé realizace, candidate-H jejich ztotožnění].**
Exaktně drží:
[
|\sigma_a(J)|=
\varphi^{-\chi_5(a)},
]
[
\det(m_a|_{W_5})=\chi_5(a),
]
a klasická formule
[
L(1,\chi_5)=\frac{2\ln\varphi}{\sqrt5}.
]
To jsou tři skutečné výskyty stejného kvadratického charakteru. Zatím však nejsou jedním operátorem na jednom veřejně typovaném nosiči.
Také je nutné držet rozdíl:
[
C_4=\operatorname{Gal}(K/\mathbb Q),
\qquad
\chi_5:C_4\to C_2.
]
Bit není celá Galoisova čtvrtotáčka. Je její znaménkový kvocient:
[
\ker\chi_5={1,4}=\langle\text{komplexní konjugace}\rangle.
]
Bit tedy rozlišuje kontrakční a expanzní třídu, ale zapomíná polohu uvnitř každého konjugovaného páru.
# Tři přenosové nálezy
## A. Galois nutí uzavření dvojice
**Status: [candidate-T].**
Pro
[
\phi_g(z_1,z_2)=(z_2,\bar z_1)
]
platí
[
\phi_g^2(z_1,z_2)=(\bar z_1,\bar z_2),
\qquad
\phi_g^4=1.
]
Definujme
[
w=z_1\bar z_2,\qquad s=z_1z_2.
]
Potom
[
w\mapsto s,\qquad s\mapsto\bar w,
]
tedy
[
w\to s\to\bar w\to\bar s\to w.
]
Z toho plyne přesně:
[
\boxed{\Psi\Psi^\dagger\text{ samo nestačí k rekonstrukci Galoisova obrazu.}}
]
Přidání (\Psi\Psi^T) uzavírá kvadratická data pod (C_4).
Silnější formulace „dvojice je jediný možný decoder" zatím prokázána není. Mohla by existovat ekvivalentní komprese nebo větší nosič. Přesné tvrzení je, že **Herm slot sám není uzavřen a dvojice je přirozené uzavření jeho Galoisovy orbity**.
To je přímá nová opora veřejného reading splitu, který má lineární, binární a kvadratický leg, ale výslovně netvrdí úplnost ani jednoznačnost.
## B. CM typ je klasifikačně uzavřen
**Status: [candidate-T].**
Pro (K=\mathbb Q(\zeta_5)) jsou konjugované páry embeddingů
[
{1,4},\qquad{2,3}.
]
CM typ vybírá po jednom embeddingu z každého páru, takže existují přesně čtyři typy. Jediné vlastní kvadratické podtěleso je reálné (\mathbb Q(\sqrt5)), nikoli CM podtěleso, takže žádný typ není indukovaný. Všechny jsou primitivní. Násobení exponentů prvkem (2\in(\mathbb Z/5\mathbb Z)^\times) je cyklicky permutuje, takže tvoří jedinou Galoisovu orbitu.
Tvrdý bod 2 je tedy skutečně uzavřen na úrovni:
[
\boxed{\text{CM typ existuje ve čtyřech reprezentantech a je jediný až na Galois.}}
]
Neuzavírá to ještě fyzikální orientaci, označený embedding ani kompatibilitu s veřejným spin liftem.
## C. Galois pohlcuje rotaci, ale formulace musí být projektivní
**Status: [candidate-T po zpřesnění].**
Pro (s^2=J) je
[
g_J=\operatorname{diag}(s,s^{-1})
]
a přímým výpočtem
[
\phi_g g_J\phi_g^{-1} = \operatorname{diag}(s^{-1},\bar s).
]
Tato komplexně lineární matice má determinant jednotkového modulu, nikoli nutně determinant (1). Její normalizovaná akce na (\operatorname{Herm}_2) je čistý boost:
[
u\mapsto\varphi u,\qquad
v\mapsto\varphi^{-1}v,\qquad
w\mapsto w.
]
Správná formulace tedy není „konjugace není v konformní grupě". Přesnější je:
> Konjugátor (\phi_g) je smíšeně reálně lineární a není prvkem komplexně lineární spin grupy. Výsledná komplexně lineární transformace však na Herm slotu indukuje čistou Lorentzovu boostovou akci.
# Skrytý čtvrtý nález: projektivní Herm slot a centrální symetrický slot
Tohle je podle mě nejdůležitější zpřesnění celého balíku.
**Status: [candidate-T].**
Pro (A\in GL_2(\mathbb C)) definujme normalizované akce
[
\mathcal H_A(X) = \frac{AXA^\dagger}{|\det A|},
]
[
\mathcal S_A(Y) = \frac{AYA^T}{|\det A|}.
]
Pro nenulový skalár (c\in\mathbb C) platí
[
\mathcal H_{cA}=\mathcal H_A,
]
ale
[
\mathcal S_{cA} = \frac{c^2}{|c|^2}\mathcal S_A.
]
Tedy:
[
\boxed{
\text{Herm slot je projektivní. Sym slot vidí centrální fázi.}
}
]
Nyní vezměme
[
A_J=\operatorname{diag}(J,1),
\qquad
g_J=\operatorname{diag}(s,s^{-1}),
\qquad
s^2=J.
]
Protože
[
A_J=s,g_J,
]
dostáváme
[
\mathcal H_{A_J}=\mathcal H_{g_J},
]
zatímco
[
\mathcal S_{A_J} = \frac{s^2}{|s|^2}\mathcal S_{g_J} = \frac{J}{|J|}\mathcal S_{g_J} = j,\mathcal S_{g_J}.
]
To dává přesný rozpad:
[
\boxed{
\begin{aligned}
\operatorname{Herm}_2 &: \text{Lorentzova geometrie, centrální fáze odstraněna},\
\operatorname{Sym}_2 &: \text{centrální fáze }j\text{ zůstává viditelná}.
\end{aligned}}
]
Ještě čistší je obejít odmocninu a pracovat přímo s (A_J). Pro
[
X=
\begin{pmatrix}
u&w\
\bar w&v
\end{pmatrix}
]
platí
[
\mathcal H_{A_J}(X) =
\begin{pmatrix}
\varphi^{-1}u&jw\
\bar j\bar w&\varphi v
\end{pmatrix}.
]
Proto
[
\mathcal H_{A_J}^5(u,v,w) = (\varphi^{-5}u,\varphi^5v,w).
]
To je exaktní formulace:
[
\boxed{\text{Jeden }J\text{-krok je loxodromický, pět projektivních kroků je čistý boost.}}
]
Tento lemma přesně vysvětluje, proč (\arg J) může být na Herm slotu prostorovou rotací a současně na Sym slotu zdrojem centrální fáze. Fyzikální identifikace této centrální fáze s elektromagnetickým (U(1)) stále zůstává `[candidate-H]`. Algebraický mechanismus už ale není hypotetický.
# Společný nosič
Původní hard point 1 je třeba rozdělit.
Veřejný Canon již obsahuje exaktní integrální lift
[
S=
\begin{pmatrix}
0&-1\
1&0
\end{pmatrix},
\qquad
T=
\begin{pmatrix}
\zeta_5&1\
0&\zeta_5^4
\end{pmatrix},
]
který nad (\mathcal O_K=\mathbb Z[\zeta_5]) uzavírá přesně 120 matic a redukuje se bijektivně na (SL_2(\mathbb F_5)=2I).
Proto lze položit
[
\Lambda=\mathcal O_K^2,
\qquad
G_{2I}=\langle S,T\rangle,
\qquad
A_J=\operatorname{diag}(J,1).
]
Protože (J) je jednotka, (A_J\in GL_2(\mathcal O_K)). Takže:
[
\boxed{\text{Existence společného integrálního lineárního nosiče pro }2I\text{ a }J\text{ je relativně k veřejnému liftu v zásadě hotová.}}
]
Navíc lze bez volby souřadnic vytvořit invariantní kladnou Hermitovskou formu
[
H_0=\sum_{g\in G_{2I}}g^\dagger g.
]
Pak
[
h^\dagger H_0h=H_0
\qquad
\forall h\in G_{2I}.
]
Na irreducibilním spinorovém nosiči je tato forma jediná až na kladný skalár. Její Hermitovské formy se rozloží na
[
1\oplus W,
]
kde (2I/{\pm I}=A_5) fixuje časovou osu a rotuje trojrozměrný traceless prostor.
Otevřené tedy není prosté „existuje nějaký společný nosič". Otevřeno je:
1. zda aritmetická smíšeně lineární (C_4) kompatibilně normalizuje nebo propojuje veřejně označený (2I) lift;
2. která ekvivalence se používá;
3. jak se vybere jedna z možných označených liftových tříd;
4. jak se checkpointová orbita mapuje na amplitudu v tomto nosiči;
5. jak se z (Q(\Psi)) zapisují přesná `MatterData`.
Veřejný audit už navíc falsifikoval jednoznačnost označeného spin liftu: existují čtyři inequivalentní třídy. Proto žádný nový common-carrier probe nesmí předpokládat jedinečný lift.
# Stav čtyř tvrdých bodů po auditu
| Tvrdý bod             | Přesný stav |
| --------------------- | ----------- |
| **1. Společný nosič** | `[candidate-T existence relative to fixed public lift]`; společné (\mathcal O_K^2) existuje. `[O]` zůstává CM/Galois kompatibilita, označená liftová třída, Gram normalizace a orbit-to-amplitude bridge. |
| **2. CM typ**         | `[candidate-T CLOSED]` na klasifikační úrovni: čtyři primitivní typy, jedna Galoisova orbita. |
| **3. Kladnost**       | `[candidate-T conditional]`: každý výstup (\sum_iw_i\psi_i\psi_i^\dagger), (w_i\ge0), je PSD. `[O]` je důkaz, že skutečný registrovaný (D_{\rm matter}) vždy tímto způsobem faktorizuje. |
| **4. Vnitřní fáze**   | `[candidate-T algebra]`: Herm projektivizuje centrální fázi, Sym ji uchovává. `[candidate-H]` zůstává identifikace se skutečným elektromagnetickým (U(1)). |
# Doporučené pořadí sond
Původní tři názvy bych neužil beze změny.
## 1. Nejprve klasifikace společného CM nosiče
Prozatímní název:
```text
P-CM-2I-QCARRIER-1
```
Nezkoumat pouhou existenci icosianového nosiče. Ta je vůči veřejnému integrálnímu liftu příliš slabá. Zmrazit:
[
(\mathcal O_K^2,\ S,\ T,\ A_J,\ \phi_g,\ H_0,\ Q)
]
a klasifikovat kompatibilní smíšeně lineární (C_4) struktury pod přesně deklarovanou ekvivalencí.
Rozhodnutí musí být nejméně trojhodnotové:
```text
UNIQUE       právě jedna kompatibilní třída
NONUNIQUE    nejméně dvě neekvivalentní třídy
EMPTY        žádná kompatibilní třída
```
To respektuje již odpálenou nejednoznačnost spin liftu.
## 2. Oddělit algebraickou fázi od fyzikálního slovníku
Místo jednoho `P-U1-DICTIONARY-1` nejprve:
```text
P-CENTRAL-LIFT-PHASE-1
```
s theorem-grade cílem
[
\mathcal H_{cA}=\mathcal H_A,
\qquad
\mathcal S_{cA}=\frac{c^2}{|c|^2}\mathcal S_A,
\qquad
\mathcal S_{A_J}=j\mathcal S_{g_J}.
]
Až poté samostatný dictionary probe, který zkusí fyzikální identifikaci centrálního slotu s (U(1)). Jinak by se algebraický theorem a fyzikální hypotéza smíchaly v jednom statusu.
## 3. SOS decoder až po orbit-to-amplitude bridge
`P-DECODER-SOS-FORM-1` nyní nemá být spuštěn jako veřejná formální sonda. `QUADRATIC-DECODER-DATA` je `STOP` právě proto, že nosič, společný totální obor, Gram a orbit-to-amplitude bridge nejsou veřejně zmrazené.
Pozdější probe nesmí pouze znovu dokazovat obecnou větu „součet čtverců je kladný". Musí testovat konkrétní veřejnou mapu:
[
\text{checkpoint/orbit}
\longrightarrow
\Psi
\longrightarrow
Q(\Psi)
\longrightarrow
\text{MatterData}.
]
Rozhodující falsifikátory mají být:
* dva checkpointy se stejným (Q), ale různým registrovaným (D_{\rm matter}) výstupem;
* registrované pole, které není konstantní na (Q)-fiberech;
* selhání normalizace;
* výstup vyžadující nezaregistrovaný vstup;
* censusový výstup mimo nezáporný Gram/SOS kužel.
# Ontologická věta po tomto útoku
Tvoje původní věta teď získává velmi přesný algebraický tvar.
Nechť (|\mathbf n|=1) a
[
P_\pm=\frac12(I\pm\mathbf n\cdot\boldsymbol\sigma).
]
Potom
[
P_\pm^2=P_\pm,
\qquad
P_+P_-=0,
\qquad
P_++P_-=I,
\qquad
\det P_\pm=0.
]
Jednička se tedy rozpadá na dva komplementární čisté nulové paprsky.
Jejich rozdíl
[
B=P_+-P_-=\mathbf n\cdot\boldsymbol\sigma
]
splňuje
[
\operatorname{tr}B=0,
\qquad
B^2=I.
]
To je přesná forma:
[
\boxed{
\text{Celek je jednička. Jeho podepsaný vnitřní rozdíl je nula v invariantu. Bit je orientace rozdělení.}
}
]
A Cauchyho-Binetova identita přidává další krok:
[
\det!\left(\sum_iw_i\psi_i\psi_i^\dagger\right) = \sum_{i<j}w_iw_j
\left|\det(\psi_i,\psi_j)\right|^2.
]
Jedna čistá větev leží na nulové hranici. Dvě nekolineární kladně vážené větve vytvářejí časupodobný vnitřek. V tomto přesném smyslu:
[
\boxed{\text{časupodobná existence vzniká jako invariant vzájemné nekolinearity čistých nulových větví.}}
]
**Statusy:**
* algebra projektorů, Hermitovský kužel, determinant a Cauchy-Binet: `[candidate-T]`;
* Bornův a kauzální výklad téhož kužele: `[candidate-D]`;
* tvrzení, že právě tato konstrukce je úplnou ontologií fyzického vesmíru: `[candidate-H]`.
Nejstručnější výsledek handoveru tedy není „všechno je Herm2". Je přesnější:
[
\boxed{
\text{Rozdělená jednička žije v Herm slotu jako kauzální tvar,
ale její úplná aritmetická fáze žije až v páru Herm + Sym.}
}
]
