# TWIST-J: značený most k trojlístku a mez nativních slov

Datum: 17. října 2026.

**NON-CANONICAL. Analytická výzkumná poznámka s pomocnými přesnými kontrolami.** Nové závěry tohoto balíčku nebyly přijaty do veřejného Canonu. Balíček není formální veřejnou sondou P ani důkazem fyzikální totožnosti protonu s uzlem.

## Hlavní výsledek

Mezi značenými maticemi \(2I\) a standardní Kleinovou invariantní plochou nyní existuje výslovný, přesně ověřený souřadnicový převod. Funguje nad \(K=\mathbb Q(j)\). U ramifikovaného místa \(\lambda=1-j\) nemůže být integrálně invertibilní. Po primitivní normalizaci má vztah tvar
\[
W^2+s^{10}H^3=1728F^5,\qquad s=j^2-j^3,
\]
a při redukci modulo \(\lambda\) se člen s \(H^3\) ztratí.

Pro uskutečnění značené trojlístkové meridiánové akce existuje samostatná překážka: grupa všech pevných slov v jednobuněčných nativních afinních generátorech má řád bez faktoru tři. V každé takové konečné grupě relace \(ABA=BAB\) nutně znamená \(A=B\). Konkrétní necyklický obraz \(2I\) tedy nelze uskutečnit touto třídou slov.

Již deklarované obousměrné součtové styky dvojice buněk naproti tomu poskytují přesně požadovanou dvojici matic v \(\mathrm{SL}_2(\mathbb F_5)\). Jejich skutečné připuštění a řízení z původního autonomního \(U\) zůstává samostatným úkolem.

## 1. Přesné souřadnice

Nechť
\[
j=e^{2\pi i/5},\quad
a=j+j^4=\varphi^{-1},\quad
s=j^2-j^3,\quad
r=j-j^4,\quad J=1+j^2=aj.
\]
Původní značení je
\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}j&1\\0&j^4\end{pmatrix}.
\]
Hledaný převod je
\[
P=\begin{pmatrix}1&-a\\0&s\end{pmatrix},
\qquad
B=sP^{-1}=\begin{pmatrix}s&a\\0&1\end{pmatrix}.
\]
Platí
\[
P^{-1}TP=\begin{pmatrix}j&0\\0&j^4\end{pmatrix}=D,
\qquad
P^{-1}SP=\begin{pmatrix}1/r&1/s\\1/s&-1/r\end{pmatrix}=E.
\]
Matice \(D,E\) jsou unitární s determinantem jedna. Všechny akce zde působí na sloupcové vektory.

Pro standardní Kleinovy formy \(f_0,H_0,W_0\) stupňů 12,20,30:
\[
W_0^2+H_0^3=1728f_0^5.
\]
Po dosazení \((x,y)=(su+av,v)\) vzniknou \(\widehat f,\widehat H,\widehat W\). Přesné minimální koeficientové valuace u \(\lambda\) jsou
\[
(10,20,25).
\]
Všechny formy
\[
F=\widehat f/s^{10},\quad
H=\widehat H/s^{20},\quad
W=\widehat W/s^{25}
\]
jsou integrální v \(\mathbb Z[j][u,v]\), u \(\lambda\) primitivní a invariantní pod přesně značenými \(S,T\).

Jejich redukce jsou
\[
\overline F=2E_6^2,\qquad
\overline H=4D_{20},\qquad
\overline W=4E_6^5,
\]
kde
\[
E_6=u^5v-uv^5,\qquad
D_{20}=(u^5-uv^4)^4+v^{20}.
\]

Přímý geometrický přenos je naproti tomu
\[
f_K=F/s^2,\quad H_K=H,\quad W_K=W/s^5,
\]
s původním standardním vztahem
\[
W_K^2+H_K^3=1728f_K^5
\]
a koeficientovými valuacemi \((-2,0,-5)\).

### Proč nelze rozdíl odstranit

Při redukci modulo \(\lambda\):
\[
\overline D=I,\qquad
\overline T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\ne I.
\]
Integrálně invertibilní změna souřadnic by jejich redukce musela sdružit. To je nemožné.

Ani skalární přenormalizování forem tento rozdíl neodstraní: standardní vztah pro \((cF,dH,eW)\) vyžaduje \(e^2=c^5\) a \(d^3=e^2s^{10}\). Primitivita první a třetí formy by vyžadovala \(3v_\lambda(d)=10\), což v \(K\) nejde.

Úplný důkaz, včetně integrality, znamének a invariantního okruhu, je v author/PROOF.md.

## 2. Bod obsahující \(J\)

Pro předem zadaný bod
\[
v_0=\binom{-a}{j^2}
\]
platí
\[
Bv_0=j^2\binom{J}{1},\qquad F(v_0)=0.
\]
Konkrétní invariantní Hermitova forma je
\[
M=(P^{-1})^\dagger P^{-1}
=\begin{pmatrix}1&a/s\\-a/s&1\end{pmatrix}.
\]
Je pozitivní v obou archimédovských vloženích, zachovává se pod \(S,T\), a
\[
v_0^\dagger Mv_0=1.
\]
Jde o zvolenou matematickou jednotkovou normalizaci. Fyzikální délková nebo energetická jednotka z této rovnosti neplyne.

## 3. Kde přesně je trojlístek

Po komplexním vložení je Kleinova invariantní plocha
\[
\mathcal X=\{(W_K,H_K,f_K):W_K^2+H_K^3=1728f_K^5\}.
\]
Projekce \((W_K,H_K,f_K)\mapsto(W_K,H_K)\) má obecně pět listů. Větví se nad křivkou
\[
W_K^2+H_K^3=0.
\]
Průnik této křivky s malou trojrozměrnou sférou v \(\mathbb C^2\) je trojlístek \(T(2,3)\). Link plochy je \(\Sigma(2,3,5)\), pětinásobné cyklické větvené pokrytí nad tímto uzlem. Klasická topologická část byla předmětem předchozího pokračování; nový výsledek odstraňuje chybějící explicitní převod značených souřadnic.

Je třeba rozlišit nosiče. V původním spinorovém \(\mathbb C^2\) je \(f_0=0\) sjednocením dvanácti komplexních přímek:
\[
f_0(x,y)=xy\prod_{k=0}^{4}(x-aj^ky)
                  \prod_{k=0}^{4}(x+\varphi j^ky).
\]
Jejich průnik s příslušnou jednotkovou sférou tvoří dvanáct Hopfových kružnic. Trojlístek je v prostoru báze větvení \((W_K,H_K)\). Žádný z těchto matematických prostorů není tímto výpočtem ztotožněn s fyzickým prostorem uvnitř protonu.

Skalární akce \(v\mapsto j^3v\) se souřadnicovým převodem komutuje. Stupně forem dávají
\[
(W_K,H_K,f_K)\mapsto(W_K,H_K,jf_K).
\]
To je přesná pětičetná akce na této algebraické konstrukci. Její uskutečnění původním \(U\) je další otázka.

Při redukci modulo \(\lambda\) zůstane
\[
\overline W^2=3\overline F^5.
\]
Tomuto vztahu v charakteristice pět zde nepřiřazujeme komplexní uzlový typ. Redukovaný obraz je
\[
\mathbb F_5[E_6^2,D_{20},E_6^5]
\subsetneq \mathbb F_5[E_6,D_{20}].
\]
To je přesně vyčíslená ztráta při přechodu mezi oběma nosiči.

## 4. Nativní mez a kladný vzor

Veřejně doložená grupa lineárních částí má řád 200. Jádro projekce z afinní grupy pevných slov je podgrupou posunů \(\mathbb F_5^6\), takže
\[
|\Gamma|=200\cdot5^r,\qquad 0\le r\le6.
\]
Její řád není dělitelný třemi. Obecné lemma dokazuje
\[
ABA=BAB\implies A=B
\]
v každé konečné grupě s touto vlastností. Celý důkaz a přesný rozsah jsou v NATIVE_PROOF.md.

Tento závěr vylučuje necyklické trojlístkové meridiány složené z pevných jednobuněčných slov a jejich skutečných grupových faktorů. Nevylučuje geometrické uzlové konfigurace ani libovolné stavově řízené programy a nově připuštěné styky.

Dosažitelný časově rozšířený ocas \(U\) je známou změnou souřadnic sdružen s
\[
(n,\ell)\mapsto(n+1,\ell).
\]
Proto samotný požadavek na cyklické čtení nevybírá pětku: pro každé \(m\ge2\)
\[
R_m(n,x)=n+G(\ell_n(x))\pmod m
\]
splňuje odpovídající propletení. Konstrukce používá čítač. Výběr přípustného geometrického čtení musí být podložen samostatně.

V deklarované rozšířené architektuře mají obousměrné součtové styky dvojice buněk přesný kladný vzor
\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
Platí
\[
A\ne B,\quad ABA=BAB=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\quad A^5=B^5=I,\quad (AB)^3=-I.
\]
Generují \(\mathrm{SL}_2(\mathbb F_5)\) řádu 120. Jsou přesně redukcí značené meridiánové dvojice \(T,STS^{-1}\). Zachování vnějšího součinu \(x\wedge y\) plyne z determinantu jedna; není to samo důkaz zachování uzlového typu.

## 5. Nejbližší navazující rozhodnutí

Před další vědeckou enumerací je potřeba připnout nezávisle připuštěný skutečný styk buněk a jeho úplný stav. Nesmí se dodatečně vybírat proto, že reprodukuje požadovaný uzel. Přesné zadání musí určit:

1. Přípravy zdroje, společný přijímač a veškeré řídicí a paměťové údaje.
2. Dvě přípustné složitelné operace na témže úplném nosiči a rovnost celých operací.
3. Zda mají příslušné operace necyklický obraz \(B_3\), případně právě značený \(2I\).
4. Jaká data nezávisle určují prostorové spojení a křížení.
5. Jak se vypočítá geometrický invariant a zda se zachová pod úplným skutečným krokem.

Faktor tři v řádu konečné grupy je nutná první algebraická podmínka. Samotná jeho přítomnost nestačí.

Veřejná větev [PR #1579](https://github.com/mathorn1973/twist-j/pull/1579), při kontrole otevřený nesloučený draft s head 03390dca1c0a69ab8989f0daada0810c9956791a, již ukazuje přenos rozdílu \(j,j^{-1}\) existujícím deklarovaným kontaktem do skutečných placených záznamů. Její vlastní rozsah ponechává W_b a Ucal jako dodaná rozhraní a nativní připuštění i autonomní řízení otevřené. Proto se tento výsledek nemá znovu vydávat za neprovedenou práci ani za důkaz nativního styku.

Aktuální výsledek poskytuje geometrický cíl a přesný algebraický požadavek na styk. Energetická stabilita, baryonové číslo, spin, elektrický náboj a hmotnostní poměr vyžadují další fyzikální argument.

## 6. Ověření a obsah balíčku

Před prvním novým strojovým vyhodnocením byl zmrazen soubor author/PREREG.md s otiskem

    d64ab46179bfe2acfaae3f61cbfdc9adc3c3c6a9e1048a92987d0e5bf7218053

Dvě samostatně napsané implementace použily pouze přesnou aritmetiku v \(\mathbb Q[j]/(\Phi_5)\):

| Kontrola | Výsledek | Rozsah |
|---|---|---|
| Autor | 59 kontrol PASS | Souřadnice, invarianty, relace, valuace, redukce, metrika a bod |
| Nezávislý oponent | 94 kontrol PASS | Stejné cíle, samostatná aritmetika, navíc kontrola dimenzí invariantů |
| Samostatná analytická kontrola nativní meze | Argument potvrzen | Afinní grupa, lemma bez faktoru 3, časové čtení, součtové matice |

Obě implementace běžely na jedné architektuře x86_64 s Pythonem 3.12.14. Nejde o veřejnou kontrolu na dvou architekturách. Důkazový základ tvoří přiložené analytické argumenty.

Oponent po prvním úspěšném pomocném běhu odstranil z výstupního JSON údaj elapsed_seconds a zopakoval běh pro deterministický výstup; původní názvy výstupů se přepsaly. Zmrazené cíle a matematické operace se nezměnily. Tato okolnost a obnovený první zdroj jsou v jeho auditním záznamu. Balíček nepředstírá neměnný veřejný pin verifieru.

Hlavní soubory:

- README.md: společný výsledek a rozsah.
- NATIVE_PROOF.md: úplný analytický důkaz nativní meze a kladného vzoru.
- author/PREREG.md: přesné předem stanovené cíle.
- author/PROOF.md: úplné odvození souřadnicového mostu.
- author/author_verify.py a JSON soubory: autorská přesná kontrola a koeficienty.
- author/AUTHOR-RUN.md: příkazy a evidence běhů.
- independent/: nezávislý verifier, report a auditní záznam.
- SOURCES.md: připnuté veřejné vstupy a primární matematické zdroje.
- SHA256SUMS: otisky předávaných souborů.

Autorův skript je přenositelný: přesný PREREG.md musí být ve stejné zapisovatelné složce. Běží z libovolného pracovního adresáře:

    python3 author/author_verify.py

Nezávislý skript zachovává původní cesty zmrazené pomocné kontroly. Jeho přesné pokyny k přenosu jsou v independent/INDEPENDENT-REPORT.md. Kvůli pohodlnějšímu balení nebyl přepsán.

## 7. Veřejná autorita a původ novosti

Použit byl Public Canon v103 ACTIVE, main a canon-v103 na commitu

    dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d

CANON.md má 1 052 518 bytů a SHA-256

    d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b

Všech pět normativních souborů bylo znovu porovnáno s veřejným manifestem. Reprodukce color-ladder už obsahuje značené invarianty, upravenou Kleinovu relaci i výslovnou kontrolu, že doslovná standardní redukce není invariantní v nesprávně převzaté bázi. Existence invariantní Hermitovy formy je rovněž již doložená. Tato poznámka nepřivlastňuje tyto starší výsledky: doplňuje explicitní převod, jeho přesné normalizace, pevný bod s \(J\) a použití obecného grupového lemmatu na konkrétní uzlovou realizaci.

