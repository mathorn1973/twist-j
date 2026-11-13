# Důkaz vynuceného čtvercového čtení

Stav: NON-CANONICAL, L1, candidate-T. Všechny závěry jsou omezeny výslovnými předpoklady níže.

## 1. Samotné skládání nestačí

Nechť q je libovolná kladně definitní kvadratická forma na racionálním prostoru V. Pro každý počet bloků n definujme

\[
R_n(x_1,\ldots,x_n)=\sum_{i=1}^n q(x_i)^2.
\]

Rodina je nezáporná, nezávislá na pořadí bloků a zachovává všechny souměrnosti, které zachovávají q na jednotlivých blocích. Při spojení dvou seznamů bloků se účty přesně sčítají. Jednoblokové čtení má přesto čtvrtý stupeň.

Požadavek R(x+y)=R(x)+R(y) na jednom amplitudovém prostoru je jiný požadavek než součet účtů dvou oddělených bloků. Nesmějí se zaměnit. Totéž platí pro přímý součet amplitud a tenzorový součin kvantových stavů.

## 2. Věta o jednom promíchání

Nechť V je vektorový prostor nad Q a R:V→R je libovolná funkce s R(0)=0. Zvolme nenulová racionální čísla a,b s a²+b²=1. Definujme involuci

\[
S(x,y)=(ax+by,bx-ay),\qquad S^2=\mathrm{id}_{V\times V}.
\]

Následující podmínky jsou ekvivalentní:

1. Pro každá x,y∈V platí
   \[
   R(ax+by)+R(bx-ay)=R(x)+R(y). \tag{M}
   \]
2. Existuje symetrická Q-bilineární forma B:V×V→R taková, že
   \[
   R(x)=B(x,x).
   \]

Nevyžaduje se spojitost, měřitelnost, mnohočlennost ani nezápornost. Není předpokládáno, že R závisí pouze na nějaké předem dané normě.

### Důkaz implikace 1 ⇒ 2

Dosazení (x,0) a (0,x) do (M) dává

\[
R(ax)+R(bx)=R(x),\qquad R(bx)+R(-ax)=R(x).
\]

Proto R(ax)=R(-ax). Násobení nenulovým racionálním a je na V bijektivní, takže R je sudá.

Pišme Δ_hR(z)=R(z+h)−R(z). Na rovnici (M) aplikujme postupně rozdíl při nahrazení x hodnotou x+h a rozdíl při nahrazení y hodnotou y+k. Pravá strana má nulový smíšený rozdíl, a tedy

\[
\Delta_{ah}\Delta_{bk}R(u)
+\Delta_{bh}\Delta_{-ak}R(v)=0,
\qquad (u,v)=S(x,y). \tag{1}
\]

Protože S je bijekce, u,v probíhají nezávisle celé V. První člen (1) je proto stálý vzhledem k u a druhý vzhledem k v. Jelikož násobení a,b je bijektivní, každý druhý rozdíl Δ_pΔ_qR(u) je nezávislý na u.

Definujme

\[
C(p,q)=\Delta_p\Delta_qR(0)
=R(p+q)-R(p)-R(q).
\]

Forma C je symetrická. Identita

\[
\Delta_{p+r}\Delta_qR(u)
=\Delta_p\Delta_qR(u+r)+\Delta_r\Delta_qR(u)
\]

a nezávislost druhých rozdílů na počátečním bodu dávají

\[
C(p+r,q)=C(p,q)+C(r,q).
\]

Ze symetrie plyne sčítavost také ve druhé proměnné. Nad Q je sčítavost automaticky racionální linearitou: pro celé n≠0 platí C(p/n,q)=C(p,q)/n. Forma C je tedy Q-bilineární.

Sudost a R(0)=0 dávají C(x,−x)=−2R(x), zatímco bilinearita dává C(x,−x)=−C(x,x). Proto

\[
R(x)=\frac12C(x,x).
\]

Položíme B=C/2. Tím je implikace dokázána.

### Důkaz implikace 2 ⇒ 1

Rozvinutím obou kvadratických výrazů dostáváme

\[
B(ax+by,ax+by)+B(bx-ay,bx-ay)
=(a^2+b^2)B(x,x)+(a^2+b^2)B(y,y).
\]

Smíšené členy se zruší a a²+b²=1. To je (M). □

Pokud R(0) není stanoveno, stejné tvrzení po odečtení R(0) klasifikuje řešení jako kvadratickou formu plus konstantu. Podmínka nulového čtení prázdného stavu odstraňuje tuto volnost.

### Zesílení pro dvě předem různá čtení

Při nezápornosti nemusíme předem požadovat ani stejnou funkci na obou blocích. Nechť f,g:V→R≥0, f(0)=g(0)=0 a pro všechna x,y platí

\[
f(ax+by)+g(bx-ay)=f(x)+g(y). \tag{M2}
\]

Stejné smíšené rozdíly jako v (1) dávají

\[
\Delta_{ah}\Delta_{bk}f(u)+\Delta_{bh}\Delta_{-ak}g(v)=0.
\]

Nezávislost u,v proto opět vynutí stálé druhé rozdíly obou funkcí. Pro každou z nich je C biaditivní jako výše; po odečtení Q(x)=C(x,x)/2 zbývá sčítavá funkce L. Máme f=Q_f+L_f a g=Q_g+L_g, kde Q jsou kvadratické formy a L jsou Q-lineární.

Pro racionální t platí f(tx)=t²Q_f(x)+tL_f(x). Kdyby L_f(x)≠0, dostatečně malé nenulové racionální t opačného znaménka by dalo f(tx)<0. Proto L_f=0, a stejně L_g=0. Dosazení y=0 do (M2) nyní dává

\[
a^2f(x)+b^2g(x)=f(x),
\]

a z b²=1−a²≠0 plyne g=f. Jediné promíchání tedy vynutí nejen druhý stupeň, ale také stejné kvadratické čtení a stejné měřítko na obou blocích. Bez nezápornosti tento závěr pro dvě různé funkce neplatí: pro a=3/5,b=4/5 a libovolnou lineární ℓ splňují (M2) například f=2ℓ, g=ℓ. □

## 3. Napojení na již dokázanou afinní jedinečnost

Nyní V=K=Q(ζ₅), F=Q(√5), J=1+ζ₅². M_J označuje násobení J a u je Galoisův automorfismus u(ζ₅)=ζ₅². Nechť

\[
\mathcal G=\langle M_J-I,u\rangle\simeq\operatorname{AGL}_1(\mathbb F_5).
\]

Veřejné věty `AFFINE-READING-DEGREE-CENSUS` a `AFFINE-QUADRATIC-FORM-UNIQUENESS` určují jedinou invariantní symetrickou přímku

\[
\mathbb Q q_+,\qquad q_+(x)=\operatorname{Tr}_{F/\mathbb Q}(x\bar x).
\]

Přidáme-li k (M) podmínku R(gx)=R(x) pro všechna g∈𝒢, polarizace B je rovněž invariantní. Jednorozměrnost zůstává platná pro reálné koeficienty, protože invariantní matice řeší tutéž konečnou soustavu racionálních lineárních rovnic. Proto

\[
\boxed{R(x)=c\,q_+(x),\qquad c\in\mathbb R.} \tag{2}
\]

Pokud R≥0, pak c≥0. Pokud navíc R není identicky nulová, pak c>0. Například kalibrace R(1)=2 určí c=1, neboť q_+(1)=2.

V bázi (1,ζ₅,ζ₅²,ζ₅³) platí

\[
\operatorname{Gram}(q_+)=\frac12(5I_4-\mathbf1\mathbf1^{\mathsf T}),
\quad
G_{\mathrm{QDD}}=I_4-\frac15\mathbf1\mathbf1^{\mathsf T}
=\frac25\operatorname{Gram}(q_+).
\]

Nový krok tedy neurčuje jinou normu. Nahrazuje předpoklad kvadratického stupně podmínkou zachování účtu při promíchání.

## 4. Přesný příklad a vyloučení čtvrtého stupně

Zvolme a=3/5,b=4/5, tedy

\[
S(x,y)=\left(\frac{3x+4y}{5},\frac{4x-3y}{5}\right).
\]

Čísla 3,4,5 nejsou privilegovanou novou konstantou: věta platí pro každou nenulovou racionální dvojici a,b s a²+b²=1.

Čtvrtý stupeň z oddílu 1 selže již na (x,0), x≠0:

\[
q_+(3x/5)^2+q_+(4x/5)^2
=\frac{3^4+4^4}{5^4}q_+(x)^2
=\frac{337}{625}q_+(x)^2
\ne q_+(x)^2.
\]

Tento příklad vyvrací zachování při S, nikoli pouhou sčítavost účtů oddělených bloků.

## 5. Přesné celočíselné provedení promíchání

Zvolme racionální bázi V≅Q^d. Dvojici (x,y) reprezentujeme čitatelem Z∈Z^(2d) a kladným společným jmenovatelem D. Pracujeme na úplném nosiči

\[
\mathcal C=\mathbb Z^{2d}\times\mathbb Z_{>0},\qquad
A=\begin{pmatrix}3I_d&4I_d\\4I_d&-3I_d\end{pmatrix},\qquad A^2=25I.
\]

Pro každý (Z,D) položme

\[
m=\gcd(Z_1,\ldots,Z_{2d},D),\qquad
g=\gcd((AZ)_1,\ldots,(AZ)_{2d},5D),
\]

\[
\boxed{\widehat S(Z,D)=\left(\frac{mAZ}{g},\frac{5mD}{g}\right).} \tag{3}
\]

Dělení je přesné, jmenovatel zůstává kladný, společný obsah m se zachovává a

\[
\frac{Z'}{D'}=\frac{AZ}{5D}=S(Z/D).
\]

**Důkaz úplné vratnosti.** Pišme (Z,D)=m(z,d₀), kde gcd(z,d₀)=1. Pak g=mh s h=gcd(Az,5d₀). Z A²=25I plyne, že h dělí všechny souřadnice 25z i 25d₀, tedy h|25. Výstup (3) je m(Az/h,5d₀/h), jehož výraz v závorkách je primitivní. Při druhém kroku je příslušný primitivní dělitel

\[
\gcd(25z/h,25d_0/h)=25/h.
\]

Druhý krok proto vrátí m(z,d₀)=(Z,D). Pokud Z=0, máme m=D,g=5D a stav se přímo nemění. Tím je dokázáno \(\widehat S^2=\mathrm{id}\) na všech stavech, bez ztráty původního obsahu. □

Jde o stejnou obecnou metodu uchování obsahu, kterou Public Canon v104 používá v `JM-INTEGER-PAIR-INVOLUTION`, aplikovanou na jinou výslovně zadanou matici. Nejde o totožnost s tamním U_z ani s původním U. Cena zápisu čitatelů a jmenovatele je další veličina; (3) ji neprohlašuje za konstantní.

Výběrová věta platí pro čtení racionálního podílu Z/D. Není klasifikací všech funkcí rozšířeného celočíselného stavu: například libovolná funkce zachovaného obsahu m je další invariant a nemusí se přes racionální podíl rozkládat.

## 6. Proč zásobník může jedinečnost zrušit

Pro libovolné čtení R:V→R≥0 definujme E(x,y)=R(x)+R(y). Na dvojici z=(x,y) a zásobníku b≥0 stanovme

\[
\mathcal F(z,b)=
\begin{cases}
(Sz,b+E(z)-E(Sz)),&b+E(z)-E(Sz)\ge0,\\
(z,b),&\text{jinak}.
\end{cases}
\]

Toto je úplná involuce zachovávající E+b. Přijatý přechod má přijatý zpětný přechod, který přesně obnoví b. Odmítnuté stavy jsou pevné. Pokud má R racionální hodnoty, lze ponechat racionální zásobník.

Při R=q_+² a z=(x,0) se do zásobníku převede

\[
\frac{288}{625}q_+(x)^2.
\]

Proto ani úplná vratnost, nezápornost a zachování celého účtu přístroje samy nevylučují čtvrtý stupeň. K použití věty z oddílu 2 musí být součet R(x)+R(y) zachován sám, případně musí být ostatní účty prokazatelně beze změny. □
