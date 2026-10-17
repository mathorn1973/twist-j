# Kladné meridiány pětičetného Kleinova větvení

**Status:** NON-CANONICAL, analytický návrh. Tento soubor byl odvozen ručně; před jeho napsáním nebyl v této větvi proveden žádný nový vědecký strojový běh. Konečné kontroly musí počkat na společně zmrazenou předregistraci. Tvrzení se týkají matematického nosiče a monodromie. Neudělují operacím nativní ani fyzikální přípustnost.

## 1. Pevné značení a přijatý základ

Pracujeme v

\[
K=\mathbb Q(j),\qquad \mathcal O=\mathbb Z[j],\qquad
1+j+j^2+j^3+j^4=0,
\]

se **zvoleným komplexním vložením** \(j=\exp(2\pi i/5)\). Matice působí na sloupcové vektory zleva. Kladný místní oběh v bázi mapy \(z\mapsto z^5\) zvedáme od \(z\) do \(jz\). Při převodu z literatury je nutné dodržet pořadí skládání cest; Broué používá při svém pořadí cest zobrazení do opačné grupy. Palindromická relace \(ABA=BAB\) se obrácením pořadí nezmění.

Položme

\[
a=j+j^4,\qquad s=j^2-j^3,\qquad \lambda=1-j.
\]

Použijeme identity

\[
a^2+a=1,\qquad s^2=a-2,\qquad a^{-1}=a+1,
\qquad j^2+j^3=-a-1.
\]

Z předchozího ověřeného základu přijímáme

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
A=T=\begin{pmatrix}j&1\\0&j^4\end{pmatrix},\quad
B=STS^{-1}=\begin{pmatrix}j^4&0\\-1&j\end{pmatrix},
\]

\[
A^5=B^5=I,\quad ABA=BAB=-S,\quad (AB)^3=-I,
\]

a grupu

\[
H=\langle A,B\rangle=\langle S,T\rangle\cong 2I,
\qquad |H|=120.
\]

\(H\) je dokonalá, tedy \([H,H]=H\). Existence a řád této značené grupy nejsou novým výsledkem tohoto zápisu.

## 2. Proč dosavadní dvojice sama nefixovala kladné geometrické meridiány

Položme

\[
G=\mu_5 H=\{j^k h:0\leq k<5,\ h\in H\}.
\]

Jde o přímý součin: skalární matice \(j^k I\) má determinant \(j^{2k}\), takže do \(H\subseteq\mathrm{SL}_2\) patří pouze pro \(k=0\). Proto \(|G|=600\).

Kladný místní meridián větvení řádu pět má na normálové přímce vlastní hodnotu \(j\) a na tečné přímce vlastní hodnotu \(1\). Jeho matice \(R\) tedy musí mít spektrum \(\{1,j\}\) a determinant \(j\). To je přesně distinguished reflection v konvenci Brouého [B, §2.10–2.14].

Rozklad \(R=j^k h\), \(h\in H\), je jednoznačný. Determinant vynutí \(2k=1\pmod5\), tedy \(k=3\), a

\[
\operatorname{spec}(h)=\{j^2,j^3\},\qquad
\operatorname{tr}(h)=-a-1=-\varphi.
\]

Původní \(A\) má naproti tomu spektrum \(\{j,j^4\}\) a stopu \(a\). Při požadovaném skaláru \(j^3\) dokonce

\[
\det(j^3A-I)=(j^4-1)(j^2-1)=2+2j+j^3\ne0.
\]

Matice \(j^3A\) tedy nemá pevnou přímku a není odrazem.

Matice \(jA\) odrazem je, ale její netriviální vlastní hodnota je \(j^2\), nikoli \(j\). Na formě stupně dvanáct působí skalárem \(j^{12}=j^2\); jde o druhou mocninu kladné místní setrvačnosti. Není to změna znaménka orientace: záporný jednoduchý oběh by měl vlastní hodnotu \(j^{-1}\).

**Opravený rozsah starého tvrzení:** \(A,B\) tvoří platný abstraktní meridiánový obraz do \(2I\). Jejich identifikace s determinantově jednotkovými složkami kladné geometrické monodromie při právě zvoleném vložení vyžaduje další přeznačení. Pouhá lineární změna báze ho nemůže zařídit, protože zachovává stopu.

## 3. Výslovná opravená dvojice

Definujeme

\[
\boxed{C=A^2=\begin{pmatrix}j^2&a\\0&j^3\end{pmatrix}},
\qquad
\boxed{D=B^3=\begin{pmatrix}j^2&0\\a&j^3\end{pmatrix}}.
\]

Přímým vynásobením trojic dostaneme

\[
CDC-DCD=
\begin{pmatrix}
0&a(j^4+j+a^2-1)\\
-a(j^4+j+a^2-1)&0
\end{pmatrix}=0,
\]

protože \(j+j^4=a\) a \(a^2+a=1\). Dále

\[
\det C=\det D=1,\quad C^5=D^5=I,
\quad\operatorname{tr}(CD)=j+j^4+a^2=1.
\]

Cayleyova–Hamiltonova věta dává

\[
(CD)^2-(CD)+I=0,
\quad\boxed{(CD)^3=-I}.
\]

Obě původní matice se obnoví:

\[
\boxed{C^3=A,\qquad D^2=B}.
\]

Proto \(\langle C,D\rangle=H\) a jeho řád zůstává \(120\).

Ireducibilitu lze zachytit krátkým certifikátem:

\[
CD-DC=\begin{pmatrix}a^2&-as\\-as&-a^2\end{pmatrix},
\qquad\boxed{\det(CD-DC)=a^2\ne0}.
\]

Společná invariantní přímka by nutila determinant tohoto rozdílu k nule.

Definujeme kladné odrazy

\[
\boxed{R_1=j^3C=\begin{pmatrix}1&j^3a\\0&j\end{pmatrix}},
\qquad
\boxed{R_2=j^3D=\begin{pmatrix}1&0\\j^3a&j\end{pmatrix}}.
\]

Pak

\[
R_1R_2R_1=R_2R_1R_2,\qquad R_i^5=I,
\]

\[
\chi_{R_i}(X)=(X-1)(X-j),\qquad
\det R_i=j,\qquad \operatorname{rank}(R_i-I)=1.
\]

Centrální člen je nyní jiný než u determinantově jednotkové dvojice:

\[
\boxed{(R_1R_2)^3=-j^3I},\qquad
\boxed{(R_1R_2)^6=jI}.
\]

Proto grupa generovaná \(R_1,R_2\) obsahuje \(jI\), následně \(C,D\), a tedy celé \(G\). Obrácená inkluze plyne z definice. Dostáváme

\[
\boxed{\langle R_1,R_2\rangle=G\cong 2I\times C_5,
\qquad |G|=600.}
\]

Klasická prezentace \(B_3/\langle\!\langle\sigma_1^5,\sigma_2^5\rangle\!\rangle\) je komplexní odrazová grupa \(G_{16}\), jak uvádí Chavli [C, úvod, str. 2; řád 600 též důsledek 4.11]. Naše matice poskytují výslovný obraz této prezentace; dosažený řád 600 ukazuje, že nejde o její další vlastní faktor.

## 4. Integrální Galoisův převod

Nechť \(\sigma_3:K\to K\) je automorfismus \(j\mapsto j^3\), použitý po koeficientech. Položme

\[
\boxed{Q=\begin{pmatrix}a&0\\-s&1\end{pmatrix}},
\qquad
\boxed{Q^{-1}=\begin{pmatrix}a+1&0\\s(a+1)&1\end{pmatrix}}.
\]

Rovnosti \(a(a+1)=1\) a \(s^2=a-2\) dávají přímým násobením

\[
\boxed{Q\sigma_3(A)Q^{-1}=C},\qquad
\boxed{Q\sigma_3(B)Q^{-1}=D}.
\]

Ekvivalentně

\[
R_1=Q\sigma_3(jA)Q^{-1},\qquad
R_2=Q\sigma_3(jB)Q^{-1}.
\]

Obě matice \(Q,Q^{-1}\) mají koeficienty v \(\mathcal O\). Determinant \(a\) je jednotka. Tento převod je tedy integrálně vratný i u \(\lambda\), na rozdíl od dřívější diagonalizace \(T\).

Jde o výslovný popis automorfismu značení grupy. Není to pokyn nahradit všechny výskyty \(j\), \(J\), geometrické metriky nebo fyzikálního čtení jejich Galoisovými obrazy. Kladná dvojice \(C,D\) je definována mocninami uvnitř původní grupy při původním vložení.

## 5. Příslušnost ke skutečnému Kleinovu pokrytí

Z předchozí práce přijímáme Kleinovy invarianty \(f,h,w\) pro **značenou** grupu \(H\), stupňů \(12,20,30\), s jediným vztahem

\[
w^2+h^3=1728f^5,
\qquad
\mathbb C[V]^H=\mathbb C[f,h,w]/(w^2+h^3-1728f^5).
\]

Pro konkrétní polynomiální test lze bez dělení použít

\[
L=\begin{pmatrix}s&a\\0&1\end{pmatrix},
\qquad
f(u,v)=f_0(su+av,v),
\qquad
f_0(x,y)=xy(x^{10}+11x^5y^5-y^{10}),
\]

a analogické dosazení do standardních \(h_0,w_0\). Všechny tři takto převzaté formy stále splňují stejný vztah. Nesměšujeme je zde s jinou primitivní normalizací u \(\lambda\).

Protože \(H\) zachovává všechny tři formy a skalár \(j^k\) působí podle stupně, platí

\[
f(j^khv)=j^{2k}f(v),\qquad
h(j^khv)=h(v),\qquad w(j^khv)=w(v).
\]

Z toho plyne

\[
\boxed{\mathbb C[V]^G=\mathbb C[h,w].}
\]

Například každý prvek \(\mathbb C[V]^H\) lze jednoznačně zapsat jako součet \(\sum_{m=0}^4 f^m p_m(h,w)\). Skalární invariance ponechá pouze \(m=0\), protože \(2m=0\pmod5\) právě pro tento zástupce.

Kvocient \(p:V\to V/G\cong\mathbb C^2\) tedy můžeme zapsat jako

\[
p(v)=(h(v),w(v)).
\]

Jeho větvení je křivka

\[
\Delta=\{w^2+h^3=0\}.
\]

Nad \(\Delta\) leží nulová množina \(f\), tvořená dvanácti různými komplexními přímkami. Mimo počátek má bod na takové přímce setrvačnost řádu pět. To lze vidět i přímo: pro \(j^kh\,v=v\ne0\) musí \(h\) mít vlastní hodnotu \(j^{-k}\); pokud \(k=0\), prvek \(h\in H\) je identita, jinak jde o vlastní přímku prvku řádu pět. Jejich množina je právě dvanáct nulových přímek \(f\). Generický bod takové přímky má přesně cyklický stabilizátor řádu pět.

Omezení

\[
p:V_{\rm reg}=\{f\ne0\}\longrightarrow\mathbb C^2\setminus\Delta
\]

je proto souvislé regulární pokrytí s grupou \(G\). Mezilehlý kvocient přes \(H\) je skutečné pětičetné Kleinovo pokrytí

\[
\{w^2+h^3=1728f^5\}\longrightarrow\mathbb C^2_{h,w},
\]

s kladným místním působením \(f\mapsto jf\).

Pro novou dvojici přímo vychází

\[
\boxed{(f,h,w)(R_i v)=(jf(v),h(v),w(v))},\qquad i=1,2.
\]

To dokazuje správné místní znaménko a správný charakter pětičetného pokrytí. Samo o sobě by to ještě neurčovalo společnou dvojici přístupových cest. Následující oddíl uzavírá právě tuto existenční otázku.

## 6. Krátký důkaz jednoznačnosti potřebné dvourozměrné dvojice

Nechť \(X,Y\in\mathrm{GL}_2(\mathbb C)\) tvoří ireducibilní dvojici, splňují \(XYX=YXY\) a mají obě spektrum \(\{1,j\}\). Označme

\[
\tau=1+j,\qquad\delta=j,\qquad\kappa=\operatorname{tr}(XY).
\]

Pro dvě matice řádu dva se stejnou stopou a determinantem dává polarizovaná Cayleyova–Hamiltonova identita

\[
XY+YX=\tau(X+Y)+(\kappa-\tau^2)I.
\]

Po vynásobení a použití \(X^2=\tau X-\delta I\), \(Y^2=\tau Y-\delta I\) dostaneme

\[
XYX=\delta Y+\kappa X-\tau\delta I,
\qquad
YXY=\delta X+\kappa Y-\tau\delta I.
\]

Proto

\[
0=XYX-YXY=(\kappa-\delta)(X-Y).
\]

Ireducibilita vylučuje \(X=Y\), takže \(\kappa=\delta=j\).

Diagonalizujme \(X=\operatorname{diag}(1,j)\) a zapišme \(Y=\begin{pmatrix}p&q\\r&t\end{pmatrix}\). Rovnice pro obě stopy a determinant určují

\[
p=-\frac{j^2}{1-j},\qquad
t=\frac1{1-j},\qquad
qr=-\frac{j(j^2-j+1)}{(1-j)^2}\ne0.
\]

Diagonalní změna báze komutující s \(X\) může zvolit jakoukoli nenulovou hodnotu \(q\); \(r\) je pak určen součinem. Všechny takové ireducibilní dvojice jsou proto současně lineárně sdružené. Jde o potřebný případ obecné věty Tuby a Wenzla [TW, věta 2.9(a)].

## 7. Existence skutečné kladné geometrické dvojice s obrazy R1, R2

Brouého věta 2.29, spolu s diagramem \(G_{16}\), dává na skutečném komplementu \(V_{\rm reg}/G\) dvojici kladných distinguished braid generators \(\beta_1,\beta_2\), jejichž jedinou relací je

\[
\beta_1\beta_2\beta_1=\beta_2\beta_1\beta_2.
\]

Jejich obrazy \(M_1,M_2\in G\), v pevné konvenci pro zdvih cest, generují \(G\) a mají spektrum \(\{1,j\}\). Jsou ireducibilní. Dvojice \(R_1,R_2\) má tytéž vlastnosti. Předchozí oddíl tedy poskytuje \(L_0\in\mathrm{GL}_2(\mathbb C)\) s

\[
L_0M_iL_0^{-1}=R_i\qquad(i=1,2).
\]

Oba páry generují stejnou podgrupu \(G\), takže \(L_0\) normalizuje \(G\), a tím i její komutátor \([G,G]=H\).

Pro binární ikosaedrickou grupu platí

\[
N_{\mathrm{GL}_2(\mathbb C)}(H)=\mathbb C^\times H.
\]

Kollár tento konkrétní normalizátor uvádí a odůvodňuje v příkladu 7 [K]: projektivní ikosaedrická grupa je maximální konečnou podgrupou \(\mathrm{PGL}_2\), a normalizátor se proto liší jen o skaláry. Můžeme tedy napsat \(L_0=cg\), kde \(g\in H\); skalár při sdružení odpadne.

Změna základního listu pokrytí, případně společná změna přístupové cesty reprezentující \(g\), provede právě takové vnitřní sdružení. **Existuje proto kladná geometrická generující dvojice skutečného Kleinova pokrytí, jejíž obrazy v našich souřadnicích jsou přesně \(R_1,R_2\).**

Tento existenční výsledek neudává jediné parametrizované přístupové cesty a neztotožňuje \(R_1,R_2\) s dvojicí cest, která by již byla nezávisle předem předepsána. Taková předepsaná dvojice by vyžadovala vlastní kontrolu zdvihů. Dřívější bod \(v_0\) s \(f(v_0)=0\) leží na větvení; není základním bodem komplementu.

Samotná abstraktní prezentace \(B_3\), samotná relace \(R_1R_2R_1=R_2R_1R_2\), ani samotné správné vlastní hodnoty by tento poslední závěr obecně nedávaly. Zde jej uzavírá kombinace skutečného invariantního kvocientu, geometrické prezentace z literatury, dvourozměrné jednoznačnosti a normalizátoru.

## 8. Redukce k součtovým stykům

Modulo \(\lambda\) platí \(j\mapsto1\), \(a\mapsto2\), \(s\mapsto0\), a

\[
\overline Q=K_0=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad K_0^{-1}=\begin{pmatrix}3&0\\0&1\end{pmatrix}.
\]

Původní matice součtových styků jsou

\[
A_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
B_0=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]

Opravená geometrická dvojice se redukuje na

\[
\boxed{\overline C=A_0^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}},
\qquad
\boxed{\overline D=B_0^3=\begin{pmatrix}1&0\\2&1\end{pmatrix}},
\]

a

\[
\boxed{\overline C=K_0A_0K_0^{-1},\qquad
\overline D=K_0B_0K_0^{-1}.}
\]

Protože \(j\mapsto1\), mají \(R_1,R_2\) stejné redukce jako \(C,D\). Rovnost podgrup a abstraktní braid relace zůstávají zachovány. **Při fixovaném označení fyzikálních buněk však druhá a třetí mocnina nejsou automaticky jediným spuštěním původních styků.** Současné přeznačení \(K_0\) je přípustná algebraická změna báze. Přípustnost odpovídajícího fyzikálního přeznačení, přípravy nebo řídicího kroku musí být doložena vlastním kontraktem.

## 9. Primární zdroje

- **[B]** Michel Broué, *Reflection Groups, Braid Groups, Hecke Algebras, Finite Reductive Groups*, Current Developments in Mathematics 2000, autorova verze 107 stran. §2.10–2.14: kladné odrazy a zdvihy; věta 2.29: geometrická prezentace; příloha 1, str. 91 a následující: diagram \(G_{16}\). https://webusers.imj-prg.fr/~michel.broue/boston.pdf
- **[C]** Eirini Chavli, *Universal deformations of the finite quotients of the braid group on 3 strands*, arXiv:1504.02279, úvod str. 2; důsledek 4.11. https://arxiv.org/pdf/1504.02279
- **[TW]** Imre Tuba a Hans Wenzl, *Representations of the braid group B3 and of SL(2,Z)*, arXiv:math/9912013, věta 2.9(a); potřebný dvourozměrný případ je samostatně dokázán v oddílu 6 tohoto souboru. https://arxiv.org/pdf/math/9912013
- **[K]** János Kollár, *Automorphisms and twisted forms of rings of invariants*, arXiv:2212.03772v2, příklad 7. https://arxiv.org/html/2212.03772v2

## 10. Hranice výsledku

Tento zápis opravuje a uzavírá znaménko i třídu geometrického meridiánového značení v matematickém modelu. Nedokazuje prostorový nosič v původním U, uskutečnění součtového styku v původním U, stabilitu uzlu, hmotnost, baryonové číslo ani elektromagnetickou korekci protonu. Nemění definici J ani nepřipouští Galoisovu změnu fyzikálního čtení bez samostatného odůvodnění.
