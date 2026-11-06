# Bauerova řada, ikosaedr X(5) a kroucená uzavírací stopa

```text
STATUS   NON-CANONICAL. Výpočetní poznámka: konečná obdoba Bauerovy řady
         pro 2/pi na hrotech X(5) a její atribuční test přes úrovně N.
         Nezakládá claim, nemění registr, frontier, status ani žádnou bránu.
         Není to sonda a není pinovaná. L1 aritmetika a teorie reprezentací,
         žádný dekodér, míra ani fyzikální lift.
BASIS    Public Canon v85 (tag canon-v85, main 7243f81). Znění řádků
         J-GALOIS-CIRCULAR-ODD-CHARACTER, COLOR-INTEGRAL-LIFT,
         COLOR-KLEIN-REDUCTION a J-HARMONIC-SEAM čteno z canon/REGISTRY.tsv
         na tomto commitu, normalizace formy f z reproduce/color-ladder.
OVĚŘENO  18 z 18 kontrol, 16 exaktně (celá čísla, Fraction, Q(sqrt5),
         Q(zeta5)), 2 numericky a označené NUM. Skript
         notes/NOTE-BAUER-IKOSAEDR-KROUCENA-STOPA-2026-09-15.check.py,
         jen standardní knihovna, sha256 souboru
           1b11da8e156c741550ea3610f1f8e43870e297fa9ddbdffa6bacc91151e3955a,
         sha256 stdout
           0d887d417e721d27496a80df40c77278c3cad649313a45fc55ecdb90b616adcd,
         tři běhy s byte-identickým stdout: x86_64 Linux CPython 3.12.3,
         aarch64 Linux CPython 3.12.3, arm64 macOS CPython 3.9.6. Pin před
         prvním spuštěním nebyl, takže je to auditní vstup, ne veřejná
         evidence, a nepovyšuje to nic.
DATUM    2026-09-15
PŮVOD    pracovní relace nad Bauerovou řadou a otázkou, co s ní má J.
         Dvě tvrzení první verze stažena jako F, jsou v oddílu 8.
```

## 0. Závěr napřed

```text
Bauerova řada je stopa Heckeho operátoru. Tři čtvrtotáčky se zavřou
do oktantu a 2/pi je relativní hustota toho uzavření.

Kruhový sektor sám obdobu nedává, nemá vektor pevný pod svou fází.

Obdoba žije na hrotech X(5), tedy na ikosaedru: krok S, kruh <T>.
Pro každé N >= 3:  Tr T_chi^3 = |PSL_2(Z/N)|/N^3 (chi(T)^3 + chi(T)^-3).

Na X(5) je předfaktor 12/25. Místo 2/pi stojí 24/25 a pro
chi(T) = zeta_5^2 stojí (12/25) zeta_5^4 J.

Vzorec platí pro každé N. Tvar „1 + jeden krok“ jen pro N = 5 a 7.
Spolu s komutativní Heckeho algebrou jen N = 5. Charakterizace, ne evidence.
```

## 1. Bauerova řada jako stopa

Řada 1 − 5(1/2)³ + 9(1·3/2·4)³ − 13(1·3·5/2·4·6)³ + … = 2/π má n-tý člen (4n+1)·P₂ₙ(0)³, liché Legendreovy polynomy v nule mizí. Je to tedy

$$
\sum_{l\ge 0}(2l+1)\,P_l(0)^3=\frac{2}{\pi}
$$

P_l(0) je hodnota zonální funkce spinu l v bodě otočeném o čtvrt obrátky. Operátor „posuň bod na sféře o 90° náhodným směrem“ působí na spinu l skalárem P_l(0) s násobností 2l+1, takže součet je stopa jeho třetí mocniny. Pravděpodobnostně: po dvou krocích leží bod rovnoměrně na hlavní kružnici přes start, jeho výška má arkussinovou hustotu 1/(π√(1−x²)), a třetí krok se vrátí jen z rovníku. Rovnoměrná sféra má hustotu výšky 1/2, takže 2/π je relativní hustota toho, že se tři čtvrtotáčky zavřou do oktantu. [T, klasické]

## 2. Proč ne kruhový sektor

Podle J-GALOIS-CIRCULAR-ODD-CHARACTER má komplexifikovaný P spektrum δ₁₀ᵏ pro k ∈ {1, 3, 7, 9}. Ani P, ani P² tedy nemá pevný vektor. Zonální funkce vůči kruhu potřebuje vektor pevný pod kruhem (násobnost reprezentace ve funkcích na G/K je dimenze K-invariant), takže v sektoru samotném Legendreova obdoba nevznikne. [T, přímo z řádku]

## 3. Ikosaedr je X(5) a J je jeho vrchol

COLOR-INTEGRAL-LIFT dává S = ((0,−1),(1,0)) a T = ((ζ,1),(0,ζ⁴)) nad Z[ζ₅] s redukcí modulo (1 − ζ) bijektivní na SL₂(F₅). Na úrovni 5 jsou redukce S a T = ((1,1),(0,1)). Hroty X(5) jsou primitivní vektory F₅² modulo ±1, hrana spojuje dvojici s determinantem ±1. Vyjde 12 vrcholů stupně 5 a genus 0, tedy ikosaedr; kruh ⟨T⟩ je stabilizátor vrcholu. [T, kontrola B4]

J je vrchol Kleinova ikosaedru. Vrcholová forma v normalizaci reproduce/color-ladder je f = u¹¹v + 11u⁶v⁶ − uv¹¹ a platí

$$
\Phi_5(u-1)=u^4-3u^3+4u^2-2u+1 \;\Big|\; u^{10}+11u^5-1
$$

takže f(J, 1) = 0. [T, K1] Ve stereografické souřadnici jsou kořeny f body 0, ∞, ζ₅^ν/φ a −ζ₅^ν φ: dva póly a dva prstence s cos θ = ±1/√5. Protože J = ζ₅·φ⁻¹, leží J v horním prstenci. Galoisovy konjugáty 1 + ζ₅^(2a) leží dva nahoře (a ∈ {1, 4}) a dva dole (a ∈ {2, 3}), bit je volba prstence. [T, K2] Tvrzení o vrcholu a výpočet stopy mluví o témže ikosaedru jako A₅-množině, souřadnice se liší a do stopy nevstupují.

## 4. Nekroucená stopa: 24/25

Na 12 vrcholech žijí právě ty ireducibilní reprezentace A₅, které mají vektor pevný pod ⟨T⟩: 1, 3, 3′, 5. Jejich zonální funkce mají na sousedním prstenci hodnoty 1, 1/√5, −1/√5, −1/5 (spektrum sousednosti ikosaedru 5, √5, −1, −√5 s násobnostmi 1, 3, 5, 3, děleno stupněm):

$$
1+3\left(\tfrac{1}{\sqrt5}\right)^3+3\left(-\tfrac{1}{\sqrt5}\right)^3+5\left(-\tfrac15\right)^3=\frac{24}{25}
$$

Rovník neexistuje, A₅ nemá čtyřčetnou osu. U Bauera lichá l mizí paritou, tady se 3 a 3′ vyruší přes √5 ↦ −√5. Kombinatoricky 24/25 = 12·10/125: dvanáct vrcholů, z každého deset uzavřených trojkroků ze 125. [T, stopa v kontrole A3]

## 5. Kroucená stopa a její důkaz

Kroucení: funkce na G s f(xk) = χ(k)⁻¹ f(x) pro charakter χ kruhu K = ⟨T⟩, operátor T_χ je krok S zprůměrovaný přes K s vahou χ.

Věta. Pro každé N ≥ 3 [T]

$$
\operatorname{Tr}T_\chi^3=\frac{|\mathrm{PSL}_2(\mathbb{Z}/N)|}{N^3}\left(\chi(T)^3+\chi(T)^{-3}\right)
$$

Důkaz. Stopa je (|G|/|K|³) krát součet χ(T)^(a+b+c) přes trojice (a, b, c), pro které TᵃSTᵇSTᶜS = ±I. Ten součin je

$$
T^aST^bST^cS=\begin{pmatrix}(ab-1)c-a & 1-ab\\ bc-1 & -b\end{pmatrix}
$$

Mimodiagonála vynutí ab = bc = 1, diagonála a = b = ∓1 pro ±I. Zbydou (1, 1, 1) se součinem −I a (−1, −1, −1) se součinem +I, obě orientace modulární relace. Kontrola B1 ověřuje množinu řešení a B2 celé histogramy holonomií pro N = 3 až 13.

Na X(5) je |PSL₂(F₅)| = 60 a

$$
\operatorname{Tr}T_\chi^3=\frac{12}{25}\left(\chi(T)^3+\chi(T)^{-3}\right),\qquad \chi(T)=\zeta_5^2:\quad \frac{12}{25}\left(\zeta_5+\zeta_5^4\right)=\frac{12}{25}\,\zeta_5^4\,J
$$

Pro páté odmocniny je χ(T)⁶ = χ(T), takže |Tr| = (12/25)|1 + χ(T)|. Pro netriviální χ obsahuje indukovaná reprezentace čtyřku A₅, jejíž spektrum na ⟨T⟩ tvoří čtyři primitivní páté odmocniny, stejně jako spektrum P² v kruhovém sektoru. Tady se sektor vrací. [T, Frobeniova reciprocita] Stopa závisí na volbě reprezentanta kroku fází, invariantní je modul a hermitovská hodnota. Hodnota (12/25)ζ₅⁴J je reálná a rovná (12/25)φ⁻¹: stopa vidí J až na torzi, tedy jeho jednotkovou část z rozkladu O_K^× = μ₁₀ × ⟨φ⟩ v J-HARMONIC-SEAM. [T]

Nezávislý model: ikosiány nad Q(√5), K řádu 10, všech 50 kroků do sousedního prstence a všech 10 charakterů dává |Tr|² = (12/25)²|1 + w^m|² s w = e^(iπ/5) (A2), hermitovské kroky dávají pro sudé m reálnou hodnotu (12/25)(w^(2m) + w^(−2m)) (A4) a pro w⁴ = ζ₅² přesně (12/25)ζ₅⁴J (A5). Liché, spinorové charaktery hermitovský krok nemají; v modulárním modelu s K = ⟨−T⟩ mají holonomie jen 2 a 3, každou 480krát (B7), takže opět |Tr| = (12/25)|1 + w^m|. Pro w^m = δ = −ζ₅² je to (12/25)|2 − J|. [T]

## 6. Kontinuum

Bauer má stejnou kostru. Rovnice

$$
R_z(\alpha_1)\,R_y(\tfrac{\pi}{2})\,R_z(\alpha_2)\,R_y(\tfrac{\pi}{2})\,R_z(\alpha_3)\,R_y(\tfrac{\pi}{2})=I
$$

má jen řešení se všemi α rovnými π/2 nebo všemi −π/2: třetí sloupec levé strany bez R_z(α₁) je (−cos α₃, cos α₂ sin α₃, sin α₂ sin α₃). [T, C1] Obě orientace oktantu nesou z Bauera a zrcadlové symetrie váhu 1/π, takže kroucená hustota by měla být

$$
\frac{1}{\pi}\left(e^{3im\pi/2}+e^{-3im\pi/2}\right)=\frac{2}{\pi}\cos\frac{m\pi}{2}
$$

Tohle odvození hustoty je náčrt a rovnost s řadou Σ(2l+1)·d^l_mm(π/2)³ je zatím jen numerická, pro m = 0 až 4 na osm míst s gaussovským vyhlazením (C2). [O]

Slovník je tím krátký. Váha jednoho řešení je 1/π v kontinuu a 12/25 na X(5), čtvrtotáčce kolem pólu odpovídá jeden krok T. Váha |PSL₂(Z/N)|/N³ = J₂(N)/(2N²) (B3) jde pro N = n! k 3/π². [T] π se tedy vrací jako součin přes všechna prvočísla a ne jako 1/π.

## 7. Atribuce

```text
N    genus   komut. Hecke   netwist. stopa   jeden krok
3    0       ano            8/9              ne
4    0       ano            3/4              ne
5    0       ano            24/25            ano
6    1       ano            2/3              ne
7    3       ne             48/49            ano
8    5       ano            3/4              ne
9    10      ne             8/9              ne
10   13      ano            18/25            ne
11   26      ne             120/121          ne
12   25      ano            2/3              ne
13   50      ne             168/169          ne
```

Vzorec z oddílu 5 platí pro každé N ≥ 3, sám tedy nic nevybírá. [T]

„Jeden krok“ znamená, že poměr orientací χ(T)⁶ je χ(T)^(±1) pro všechna χ. To nastane přesně pro N ∈ {5, 7}, protože 6 ≡ ±1 (mod N). Na úrovni 7 (24 vrcholů stupně 7, genus 3) tedy tvar přežije záměnu 5 → 7. [T, B6]

Komutativní Heckeho algebra, tedy skutečná obdoba Legendreových funkcí, vychází v rozsahu 3 až 13 přesně tehdy, když u² ≡ ±1 pro všechny jednotky u modulo N, tj. když (Z/N)^×/{±1} je elementární 2-grupa. [T, B5]

Obojí zároveň platí jen pro N = 5, a to obecně: jeden krok vynutí N ∈ {5, 7} a na sedmičce algebra komutativní není. [T] Podle pravidla o axiomu je to charakterizace třídy, ne evidence pro pětku.

## 8. Co padlo

Zlatý sourozenec jako most k J. [F] Numericky platí (D1, 45 míst)

$$
\sum_{n\ge 0}\binom{2n}{n}^3\,\frac{1+(5+\sqrt5)\,n}{64^n}\,\varphi^{-6n}=\frac{\varphi^{5/2}}{\pi}
$$

a parametr je φ⁻⁶ = (J·J̄)³ (D2). Jednotky Z[φ] jsou ale jen ±φᵏ a J·J̄ = φ⁻², takže shoda je vynucená a o J neříká nic kromě |J| = φ⁻¹. Identita zůstává numerickým pozorováním bez nároku na novost.

Věta „pětku vybírá podmínka 6 − k = 1“. [F] Pro pravidelné triangulace sféry platí, Eulerova formule připouští jeden krok jen pro k = 5. Povinná záměna 5 → 7 ale ukázala, že na X(7) je poměr orientací také jeden krok. Nahrazeno oddílem 7.

## 9. Čtení

„J je kroucená uzavírací amplituda ikosaedrické stěny“: obě orientace stěny přispívají χ(T)^(±3) a pro χ(T) = ζ₅² je jejich součet ζ₅⁴J. Algebra je [T], čtení [H].

„π je podpis limity“: každá konečná stopa je algebraická, 2/π se objeví až v kontinuu a 3/π² až v součinu přes všechna prvočísla. Fakta [T], čtení [H].

## 10. Reprodukce

```sh
python3 notes/NOTE-BAUER-IKOSAEDR-KROUCENA-STOPA-2026-09-15.check.py
```

Poslední řádek stdout je `SOUHRN 18/18 PASS`, sha256 celého stdout je v hlavičce. Běh trvá řádově deset sekund.
