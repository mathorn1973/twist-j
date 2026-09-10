# Revize: RH, binární skládání, ortogonální vrstvy a přesná racionální norma

```text
STATUS      NON-CANONICAL. Revizní poznámka k pracovní sondě z 2026-09-10.
            Žádný pohyb statusu, žádný řádek registru, žádná sonda, žádná
            změna Kánonu.
BASIS       Public Canon v83, tag canon-v83,
            content commit 528e868abaa368403ac3c7e81ebd326a3d81b588
DATE        2026-09-10
LAYER       NOT_APPLICABLE (analytická teorie čísel; žádný L1–L6 zdvih)
RH          zůstává otevřenou obligací programu; tato revize RH nedokazuje,
            nevyvrací ani nepředpokládá
SOURCE      NOTE-SOURCE-CZ.md (revidovaný text, doslovně)
VERIFIER    verify_rh_binary_review.py, pouze int a fractions.Fraction;
            stdout a JSON přiloženy
```

Značení je převzato ze sondy: $r_k(n)=n\bmod k$, $\mathbf1$ konstantní
posloupnost, $H$ prostor s váhou $1/(n(n+1))$, $\|\cdot\|_B$ binární norma,
$V$ uzavřený obal zbytků, $E=\operatorname{span}_{\mathbb Q}\{r_k:k\ge2\}$
konečný obal, $D_m$ dilatace, $C$ směrování, $a_j=C^jr_2$ vrstvy,
$P_m$ prostor $m$-periodických posloupností (s konvencí $x_0=x_m$),
$\Delta x(n)=x_n-x_{n-1}$ s $x_0=0$.

## 0. Verdikt

1. **Matematický obsah sondy je správný.** Nezávislý skript s přesnou
   aritmetikou (487 677 kontrol v 10 skupinách) reprodukuje každou identitu
   §1–§8, každý zlomek tabulky §7 včetně $c_2=160/251$, $c_3=105/251$,
   $d_3^2=52/251$, a cyklickou formuli §6 proti nezávislému oboustrannému
   uzávěru nekonečného konce. Žádná chyba nebyla nalezena; několik
   upřesnění je v §2.
2. **Sonda RH nedokazuje a říká to správně.** Chybějící krok, přípustnost
   směrování $C(V)\subseteq V$ nebo příslušnost vrstev $a_j\in V$, je s RH
   ekvivalentní. Lemma 3.5 níže ukazuje, že totéž platí pro každou další
   „přirozenou“ invarianci ($T$-posun, $TC$, celé periodické prostory).
   Žádný strukturální argument o přípustnosti tedy nemůže být levnější než
   důkaz RH.
3. **Důkaz jsme neuzavřeli.** Určili jsme přesně, kde by musel proběhnout
   (§4): je to kvantitativní aproximační úloha pro jedinou pevnou posloupnost
   $a_1=\mathbf1_{n\equiv2\ (4)}$, popřípadě pro nekonečně mnoho vrstev,
   jejíž Mellinův obraz obsahuje Dirichletovu betu. Přirození kandidáti na
   aproximanty konvergují právě tehdy, když je $1/\zeta$ kontrolována
   v $\Re s>1/2$, což je RH.
4. **Tři výsledky jsou nové vůči textu sondy** (§3, s důkazy):
   (a) $\mathbf1\in V\Rightarrow V=H$ plyne ve dvou řádcích z dilatační
   invariance a nepotřebuje [1];
   (b) konečný obal je přesně popsán: $E\cap P_m=\operatorname{span}\{r_k:k\mid m,
   k\ge2\}$ má dimenzi $\tau(m)-1$ uvnitř $m$-rozměrného $P_m$; překážka §4,
   selhání každého jiného základu než 2 a diskrétní verze „konečné
   prvočíselné podpory“ jsou její důsledky;
   (c) Hurwitzovo čtení vrstev: $a_j\in V$ pro **nekonečně mnoho** $j$
   už implikuje RH; sonda potřebovala všechna $j$.
5. **Vůči dosavadní práci TWIST-J je to nový nosič téhož jevu, ne nová
   věta.** Dyadická překážka §2 je diskrétním dvojčetem zabité trasy
   `PENTAGON-ONLY-DILATIONS [F]` (konečná množina prvočísel nikdy nedosáhne
   cíle) a Věta 3.4 ji zobecňuje na libovolnou konečnou množinu prvočísel
   v obou normách. Podle pravidla počítání z
   `notes/RH-ONE-WALL-CROSSREF_2026-08-17.md` jde o další čtení jedné zdi.
6. **Lean.** Elementární část je formalizovatelná v prostředí
   `notes/lean-j-cyclotomic` (Lean 4.30.0, pinovaný Mathlib); Bagchiho věta
   v Mathlibu není a zůstane explicitní hypotézou. Plán je
   v `LEAN-PLAN-CZ.md`. V tomto sezení nebylo možné Lean nainstalovat, žádný
   Lean kód zde tedy není přeložen.

## 1. Co bylo ověřeno

| §  | Tvrzení sondy | Výsledek | Jak |
|----|---------------|----------|-----|
| 1  | $w_H(n)\le w_B(n)\le4w_H(n)$; $\|\mathbf1\|_H^2=1$; $\|\mathbf1\|_B^2=2$ | platí | přesně pro $n<5000$; teleskop; cyklická formule s periodou 1 |
| 2  | $D_mr_k=(r_{mk}-r_m)/m$ | platí | přesně pro $2\le m,k\le8$, $n<400$; obecný důkaz v §2 |
| 2  | $\|D_mx\|_H^2=\|x\|_H^2/m$, $\|D_2x\|_B^2=\|x\|_B^2/2$ | platí | přesně na náhodných konečně nosných vektorech |
| 2  | iterace s $D_2$ dává počet jedniček; $f(3)=2$ | platí | přesně pro $n\le1024$ |
| 2  | $f(3)=f(1)+f(2)$ pro $r_{2^j}$; $\|\ell\|_B^2=9$; mez $1/9$ | platí | přesně; zobecněno ve Větě 3.4 |
| 3  | $\|Cx\|_B^2=\|x\|_B^2/4$; $\|C\|_H^2=1/3$ | platí | přesně; poměr vah $(n+1)/(2(2n+1))$ klesá od $1/3$ k $1/4$ |
| 3  | $\mathbf1=r_2+C\mathbf1$; $f_J=\mathbf1_{2^J\nmid n}$; $\|\mathbf1-f_J\|_B^2=2/4^J$ | platí | přesně pro $J\le10$, $n\le4096$; norma cyklickou formulí |
| 3  | $a_j=\mathbf1_{v_2(n)=j}$, ortogonalita, $\|a_j\|_B^2=3/(2\cdot4^j)$, součet 2 | platí | přesně pro $j\le7$ |
| 4  | $y=Cr_2$ není konečnou kombinací zbytků | platí | přesná hodnost rozšířené matice pro všech 162 podmnožin $F\subseteq\{2..9\}$ velikosti $\le4$; svědek $L$ |
| 4  | $\mathrm{RH}\iff C(V)\subseteq V\iff a_j\in V\ \forall j$ | platí | důkaz sondy je úplný; zesíleno ve Větě 3.6 |
| 5  | $2\Delta y=-1+3\mathbf1_{2\mid n}-2\mathbf1_{4\mid n}+\chi_4(n)$; identita s $\beta$ | platí | přesně pro $n<5000$; prefaktor jako polynomiální identita v $u=2^{-s}$ |
| 6  | cyklická formule pro periodickou binární sumu | platí | 213 náhodných period $L\le1000$ proti hrubé sumě 14 bloků s oboustranným uzávěrem konce; invariance vůči násobku periody |
| 7  | $G$, $b$, $c$ a $d_K^2$ pro $K\le6$; kladná definitnost; pythagorejský zákon poklesu | platí | přesně; tabulka rozšířena do $K=40$; normální rovnice ověřeny bodově |
| 8  | $R(f)=(I-C)(\mathbf1-f)$; $\tfrac49\|R\|^2\le\|\mathbf1-f\|^2\le4\|R\|^2$ | platí | přesně pro minimizéry $K=2,3,4,6$ |
| 9  | 44 390 kontrol ve 14 skupinách | neověřeno | skript sondy nebyl k dispozici; vlastní skript, viz §6 |

## 2. Upřesnění k textu sondy

Nic z toho nemění závěry sondy.

- **§1, import z [1].** Síťový přístup na arxiv.org byl v tomto sezení
  blokován, citace [1]–[4] nebyly znovu ověřeny. Revize znovu odvodila
  elementární směr kritéria: je-li $\rho$ nula $\zeta$ s $\Re\rho>1/2$, je
  $\lambda_\rho(x)=\Pi(x)(\rho)$ omezený funkcionál na $H$ (odhad
  $|n^{-\rho}-(n+1)^{-\rho}|\le|\rho|n^{-\Re\rho-1}$ a
  $\sum n(n+1)n^{-2\Re\rho-2}<\infty$), nulový na každém $r_k$, ale
  $\lambda_\rho(\mathbf1)=1/\rho\ne0$; tedy $\mathbf1\in V\Rightarrow$ RH.
  Opačný směr, RH $\Rightarrow\mathbf1\in V$, je import z [1] a sonda by ho
  měla označit stejně, jako incubační lane
  `C-RH-PYTHAGORAS-HALFANGLE-N` označuje import Suzukiho věty. Druhá
  ekvivalence „$\mathbf1\in V\iff V=H$“ import nepotřebuje (Lemma 3.1).
- **§2, $D_mV\subseteq V$.** Krok z $D_mr_k\in E$ na $D_mV\subseteq V$
  vyžaduje spojitost $D_m$; ta platí s $\|D_m\|_H=m^{-1/2}$ a
  $\|D_2\|_B=2^{-1/2}$.
- **§2, iterace s $D_2$.** Konvergence k počtu jedniček platí i v normě:
  $D_2$ je kontrakce, pevný bod je počet jedniček a ten leží v $H$, protože
  je nejvýše $\log_2n+1$.
- **§3.** V binární normě je $C$ přesně $\tfrac12$-násobek izometrie; v $H$
  je $\|C\|_H^2=1/3$ ostrá hodnota, nabytá jen v $n=1$.
- **§4, poslední odstavec.** Tvrzení „stačí $a_j\in V$ pro každé $j$“ je
  správné; Věta 3.6 je zesiluje na nekonečně mnoho $j$ a dává pro každé
  jednotlivé $j$ konkrétní nutnou podmínku v Hurwitzově zetě.
- **§5.** Funkcionál $\Pi(\cdot)(\rho)$ je omezený jen pro $\Re\rho>1/2$;
  argument se tedy vztahuje přesně na hypotetické nuly mimo kritickou
  přímku, jak sonda říká. Že $\beta(\rho)\ne0$, není známo; Věta 3.6 tuto
  neznámou obchází.
- **§6, implementace.** Předperioda je $h=v_2(L)$ a délka cyklu
  $t=\operatorname{ord}_{L/2^h}(2)$; formule je použitelná i pro $L=1$ a $L=2$.
- **§7, rychlost poklesu.** Tabulka rozšířená do $K=40$ (JSON do $K=24$
  přesně) a diagnostika s plovoucí čárkou ukazují
  $d_K^2\log K\approx0{,}10$ pro $8\le K\le40$: pokles je nejvýše řádu
  $1/\log K$, ne geometrický. Srovnání v $K=2^J$: $d_4^2=95/766\approx0{,}1240$
  je nepatrně **pod** binární chybou $2/16=0{,}125$, ale
  $d_8^2\approx0{,}0517$ proti $2/64\approx0{,}0313$ a
  $d_{16}^2\approx0{,}0374$ proti $2/256\approx0{,}0078$. Geometrický pokles
  sondy je koupen opuštěním $V$.
- **§9.** Skript `verify_rh_binary.py` a `verification.json` nebyly
  revizi k dispozici; počty kontrol sondy nejsou reprodukovány, nahrazuje je
  vlastní skript (§6).

## 3. Nové výsledky

### 3.1 Lemma (hustota z dilatace)

*Je-li $\mathbf1\in V$, pak $V=H$.*

Důkaz. $(D_m\mathbf1)_n=\mathbf1_{\lfloor n/m\rfloor}$, což je $1$ pro
$n\ge m$ a $0$ jinak, tedy $D_m\mathbf1=\mathbf1_{[m,\infty)}$. Z §2 sondy je
$D_mV\subseteq V$, takže $\mathbf1_{[m,\infty)}\in V$ pro každé $m\ge1$.
Rozdíly $\mathbf1_{[m,\infty)}-\mathbf1_{[m+1,\infty)}=\delta_m$ dávají
všechny jednotkové vektory, konečně nosné posloupnosti jsou v $H$ husté
(konce $\sum_{n>N}|x_n|^2w_n\to0$) a $V$ je uzavřený. $\square$

Ekvivalence $\mathrm{RH}\iff\mathbf1\in V\iff V=H$ tedy potřebuje [1] jen
pro směr RH $\Rightarrow\mathbf1\in V$.

### 3.2 Lemma (struktura konečného obalu)

*Pro $f\in E$ s moduly $F$ a $L=\operatorname{lcm}F$ platí $f(0)=0$ a
$\Delta f(n)=\phi(\gcd(n,L))$ pro funkci $\phi$ na dělitelích $L$ s nulovým
průměrem $\sum_{n=1}^{L}\phi(\gcd(n,L))=0$. Naopak každá dvojice $(L,\phi)$
s nulovým průměrem dává prvek $f(n)=\sum_{i\le n}\phi(\gcd(i,L))$ z $E$
s moduly dělícími $L$.*

Důkaz. $\Delta r_k(n)=1-k\,\mathbf1_{k\mid n}$, tedy pro
$f=\sum_{k\in F}c_kr_k$ je $\Delta f(n)=c-\sum_{k\in F}kc_k\mathbf1_{k\mid n}$
s $c=\sum c_k$; protože $k\mid L$, je $k\mid n\iff k\mid\gcd(n,L)$. Nulový
průměr je $f(L)-f(0)=0$. Naopak indikátory $\mathbf1_{k\mid n}$, $k\mid L$,
generují právě funkce $\gcd(n,L)$ (Möbiova inverze
$\mathbf1_{\gcd(n,L)=d}=\sum_{d\mid k\mid L}\mu(k/d)\mathbf1_{k\mid n}$),
takže $\phi(\gcd(n,L))=\sum_{k\mid L}g_k\mathbf1_{k\mid n}$; nulový průměr
znamená $g_1=-\sum_{k\ge2}g_k/k$ a volba $c_k=-g_k/k$ dává
$\sum_{k\ge2}c_k\Delta r_k=\phi(\gcd(\cdot,L))$. Obě strany mají $f(0)=0$
a stejné rozdíly. $\square$

**Důsledek.** Je-li $x\in E$ navíc $m$-periodická, je $\Delta x(n)$ funkcí
$\gcd(n,m)$ (čínská věta o zbytcích umožňuje volit v každé třídě mod $m$
zástupce s $\gcd(n'',L)=\gcd(n,m)$). Proto

$$E\cap P_m=\operatorname{span}\{r_k:k\mid m,\ k\ge2\},\qquad
\dim(E\cap P_m)=\tau(m)-1,\qquad \dim P_m=m .$$

To je přesná velikost mezery: v $m$-periodických posloupnostech vidí konečný
obal jen $\tau(m)-1$ směrů z $m$; zbytek musí zaplnit uzávěr přes stále delší
periody. Například $E\cap P_4=\operatorname{span}(r_2,r_4)$ neobsahuje
$a_1=\mathbf1_{2\ (4)}$, což je překážka §4 sondy.

### 3.3 Důsledek (třídy zbytků; základ 2 je vynucen)

*Pro $m\ge3$ není žádný indikátor $\mathbf1_{n\equiv b\ (m)}$ v $E$; pro
$m=2$ je v $E$ pouze $\mathbf1_{n\ \mathrm{lich\acute e}}=r_2$. Rovněž
$f_J=\mathbf1_{2^J\nmid n}\notin E$ pro $J\ge2$ a
$\mathbf1_{m\nmid n}\notin E$ pro $m\ge3$.*

Důkaz. $\Delta\mathbf1_{b\ (m)}$ nabývá $-1$ přesně ve třídě $b+1$ a $+1$
přesně ve třídě $b$. Má-li být funkcí $\gcd(n,L)$ s $m\mid L$, musí každé
vlákno $\{n:\gcd(n,L)=g\}=g\cdot(\mathbb Z/(L/g))^\times$ ležet v jediné
třídě mod $m$, tedy $m\mid g(u-1)$ pro všechny jednotky $u$ mod $L/g$;
surjektivita redukce jednotek na $(\mathbb Z/m')^\times$, $m'=m/\gcd(m,g)$,
vynutí $\varphi(m')=1$, tj. $m\mid2g$, a tak $b+1\in\{0,m/2\}$ mod $m$.
Stejně $b\in\{0,m/2\}$. Dvě po sobě jdoucí třídy v $\{0,m/2\}$ existují jen
pro $m=2$. Pro $f_J$ a $\mathbf1_{m\nmid n}$ stačí, že třídy $1$ a $2$ (resp.
$1$ a $3$) mají stejný $\gcd$ s modulem, ale různý $\Delta$. $\square$

Skript to potvrzuje přesnými testy hodnosti pro $m\le8$, $F=\{2,\dots,9\}$.
Praktický důsledek pro sondu: rovnice $\mathbf1=\mathbf1_{m\nmid n}+C_m\mathbf1$
platí pro každý základ $m$, ale její semínko $\mathbf1_{m\nmid n}$ leží
v konečném obalu **jen pro $m=2$**. Binární volba sondy tedy není
kosmetická; je to jediný základ, pro který nultá vrstva je přípustná
konečně. Zejména nelze směrování „pentagonizovat“ na základ 5.

### 3.4 Věta (konečná prvočíselná podpora)

*Nechť $S$ je konečná množina prvočísel, $V_S$ uzavřený obal
$\{r_k:k\ \text{je }S\text{-hladké},\ k\ge2\}$ a $q$ nejmenší prvočíslo mimo
$S$. Pak každé $x\in V_S$ splňuje $x_1+x_{q-1}-x_q=0$, a proto*

$$\operatorname{dist}_B(\mathbf1,V_S)^2\ \ge\ \frac1{1+4^{\lfloor\log_2(q-1)\rfloor}+4^{\lfloor\log_2q\rfloor}},
\qquad
\operatorname{dist}_H(\mathbf1,V_S)^2\ \ge\ \frac1{2+2q^2}.$$

*Obecněji $\Delta x(n)=\Delta x(n')$, kdykoli $n,n'$ mají stejnou
$S$-část; $V_S$ má tedy v $H$ nekonečnou kodimenzi.*

Důkaz. Podle 3.2 je $\Delta f(n)$ pro $f\in E_S$ funkcí $\gcd(n,L)$ s $L$
$S$-hladkým, tedy funkcí $S$-části $n$. Čísla $1$ a $q$ mají $S$-část $1$,
takže $f(1)-f(0)=f(q)-f(q-1)$ s $f(0)=0$. Vyhodnocení pevných souřadnic je
spojité, podmínka přechází na $V_S$. Funkcionál $\ell(x)=x_1+x_{q-1}-x_q$ má
$\ell(\mathbf1)=1$ a duální normu $\|\ell\|^2=\sum|\ell_n|^2/w_n$. $\square$

Pro $S=\{2\}$, $q=3$ je to přesně mez $1/9$ sondy (§2) a v $H$-normě $1/20$.
Další hodnoty: $S=\{2,3\}$ a $S=\{2,3,5\}$ dávají $1/33$ v $B$-normě
($1/52$, resp. $1/100$ v $H$-normě); $S=\{3\}$, $\{5\}$, $\{3,5\}$ dávají
$1/6$ ($1/10$). Skript ověřuje rovnici $\ell=0$ a rovnost rozdílů na stejných
$S$-částech na náhodných kombinacích pro sedm množin $S$.

Tato věta je diskrétní protějšek registrovaného výsledku
`J-LI-PENTAGON-DILATION-DEFICIENCY [T]` / `PENTAGON-ONLY-DILATIONS [F]`
(spojité NB funkce $g_n(x)=\{nx\}-1/2$, vzdálenost $\tfrac1{12}(1-1/q^2)$ od
obalu $g_{5^m}$) a cíle opuštěné sondy
`probes/P-FINITE-PRIME-SUPPORT-DILATIONS-1` (libovolná konečná množina
prvočísel). V diskrétním nosiči je důkaz dvouřádkový. Podle POLICY §3 by
formální nástupce musel dostat nový identifikátor a jmenovat opuštěného
předchůdce; tato revize žádný nezakládá.

### 3.5 Lemma (všechny přirozené invariance jsou RH)

Nechť $(Tx)_n=x_{n-1}$ je posun ($\|T\|\le1$ v obou normách, váhy jsou
nerostoucí). Každé z následujících tvrzení je ekvivalentní s RH:

1. $C(V)\subseteq V$ (sonda, §4);
2. $TC(V)\subseteq V$;
3. $T(V)\subseteq V$;
4. $P_m\subseteq V$ pro některé $m\ge1$;
5. $\mathbf1_{n\equiv b\ (m)}\in V$ pro všechna $b$ při některém $m$;
6. $a_j\in V$ pro nekonečně mnoho $j$ (Věta 3.6).

Důkaz. RH $\Rightarrow V=H$ dává vše. Naopak: (2) $D_2=C+TC$ a
$D_2V\subseteq V$, tedy (1) $\iff$ (2). (3) $(I-T)r_2=\Delta r_2
=\mathbf1-2\cdot\mathbf1_{2\mid n}=2r_2-\mathbf1$, takže $\mathbf1\in V$.
(4) a (5): $\mathbf1\in P_m$, resp. $\mathbf1=\sum_b\mathbf1_{b\ (m)}$. $\square$

Poučení pro sondu: přípustnost směrování nelze získat z žádné další
symetrie $V$, která by sama nebyla RH. Každá z položek je pouze jiné
oblečení téže obligace.

### 3.6 Věta (Hurwitzovo čtení vrstev)

*Pro $j\ge0$ a $\Re s>0$*

$$\Pi(a_j)(s)=\frac1s\Bigl[2^{-js}(1-2^{-s})\zeta(s)
-2^{-(j+1)s}\,\zeta\!\bigl(s,\tfrac12+2^{-j-1}\bigr)\Bigr],$$

*kde $\zeta(s,a)=\sum_{l\ge0}(l+a)^{-s}$ je Hurwitzova zeta. Pro $j=1$ je to
identita §5 sondy, protože $4^{-s}\zeta(s,\tfrac34)=\tfrac12[(1-2^{-s})\zeta(s)-\beta(s)]$.*

Důkaz. Pro omezené $x$ a $\Re s>1$ dává Abelova sumace
$\Pi(x)(s)=\frac1s\sum_n\Delta x(n)n^{-s}$. Je $\sum_n a_j(n)n^{-s}
=2^{-js}(1-2^{-s})\zeta(s)$ a $\sum_n a_j(n-1)n^{-s}=\sum_{v_2(m)=j}(m+1)^{-s}$;
čísla $m=2^j(2l+1)$ dávají $m+1=2^{j+1}\bigl(l+\tfrac12+2^{-j-1}\bigr)$, což je
$2^{-(j+1)s}\zeta(s,\tfrac12+2^{-j-1})$. Obě strany jsou analytické v
$\Re s>0$: levá absolutně konverguje, pravá má v $s=1$ residua
$2^{-j-1}-2^{-j-1}=0$. $\square$

**Důsledek.** *Je-li $\zeta(\rho)=0$ s $\Re\rho>1/2$ a $a_j\in V$, pak
$\zeta(\rho,\tfrac12+2^{-j-1})=0$. Platí-li $a_j\in V$ pro nekonečně mnoho
$j$, pak RH.*

Důkaz. $\lambda_\rho$ je omezený funkcionál nulový na $V$ (§2), takže
$\Pi(a_j)(\rho)=0$ a s $\zeta(\rho)=0$ zbývá
$2^{-(j+1)\rho}\zeta(\rho,\tfrac12+2^{-j-1})=0$. Pro pevné $\rho\ne1$ je
$a\mapsto\zeta(\rho,a)$ analytická na $\Re a>0$ a není identicky nulová,
neboť $\zeta(\rho,a)=a^{-\rho}+\zeta(\rho,a+1)$ a $|a^{-\rho}|\to\infty$ pro
$a\to0^+$, zatímco $\zeta(\rho,a+1)$ zůstává omezená. Její nuly jsou tedy
izolované; body $\tfrac12+2^{-j-1}$ se hromadí ve vnitřním bodě
$\tfrac12$, takže nekonečně mnoho z nich nulami být nemůže. Hypotetická nula
$\rho$ tedy neexistuje. $\square$

Sonda potřebuje všechna $j$ (pythagorejský součet). Zde stačí nekonečná
podmnožina a argument je zcela jiný: analytičnost v parametru Hurwitzovy
zety místo Pythagora. Pro jediné $j$ tento argument RH nedává: dává jen
nutnou podmínku „společná nula $\zeta(\cdot)$ a $\zeta(\cdot,\tfrac12+2^{-j-1})$“,
pro $j=1$ tedy $\beta(\rho)=0$, jak sonda uvádí.

### 3.7 Poznámka (Hardyho prostor)

$\Pi(x)(s)=\int_0^1F_x(u)u^{s-1}\,du$ s $F_x(u)=x_{\lfloor1/u\rfloor}$ a
$\|F_x\|_{L^2(0,1)}=\|x\|_H$. Mellinova–Plancherelova věta činí z
$x\mapsto\Pi(x)(\tfrac12+it)$ izometrii (až na $\sqrt{2\pi}$) $H$ na
uzavřený podprostor Hardyho prostoru $H^2(\Re s>\tfrac12)$; $V$ odpovídá
uzávěru $\{\zeta(s)P(s)/s\}$ přes Dirichletovy polynomy $P$ s $P(1)=0$ a
$\mathbf1$ odpovídá $1/s$. Sonda tedy žije v témže $H^2$, ve kterém pracují
lanes `C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N` a
`C-RH-CAPACITY-CONTRACTION-1-N/MODEL-SPACE-LIFT.md`, ale s jiným objektem:
schodovitý podprostor a $\zeta$-násobky Dirichletových polynomů místo
Suzukiho prostoru $V(0)$ a modelových prostorů $K_\Theta$. Žádné ztotožnění
se netvrdí.

## 4. Proč důkaz zde neuzavíráme

**Řetězec ekvivalencí.** Z §1–§4 sondy a §3 této revize

$$\mathrm{RH}\iff\mathbf1\in V\iff V=H\iff C(V)\subseteq V\iff
a_j\in V\ \forall j\iff a_j\in V\ \text{pro nekonečně mnoho }j
\iff T(V)\subseteq V\iff\dots$$

Každý směr „$\Leftarrow$ RH“ používá těžký směr [1]; každý směr
„$\Rightarrow$ RH“ je elementární přes $\lambda_\rho$. Žádný článek řetězce
není opěrný bod: dokázat kterýkoli bez předpokladu znamená dokázat RH.

**Kde by důkaz musel proběhnout.** Stačí jediná pevná posloupnost, například
$a_1=\mathbf1_{2\ (4)}$, pokud by se ukázalo, že $a_1\in V$ implikuje
$a_j\in V$ pro nekonečně mnoho $j$ (to není známo), nebo přímo nekonečná
rodina vrstev. Úloha „$a_1\in V$“ je v Mellinově obrazu: najít Dirichletovy
polynomy $Q_K$ s

$$\Bigl\|\frac{\zeta(s)Q_K(s)}{s}-\frac{\beta(s)}{2s}\Bigr\|_{H^2(\Re s>1/2)}\to0 .$$

Formálně $Q_K\to\beta/(2\zeta)=\tfrac12\sum_n(\mu*\chi_4)(n)n^{-s}$.
Přirození kandidáti (Möbiem vážené truncace, jako u Báez-Duarteho [2])
konvergují právě tehdy, když je $1/\zeta$ kontrolována v $\Re s>1/2$, tj.
RH. Binární struktura tedy převádí RH na jednu konkrétní „zkroucenou“
Nymanovu–Beurlingovu úlohu s cílem $\beta(s)/s$ místo $1/s$; není známo, že
by byla snazší.

**Co říkají čísla.** Uvnitř $V_K$ klesá přesné minimum jako
$d_K^2\log K\approx0{,}10$ pro $8\le K\le40$ (diagnostika). Ve spojitém NB
prostředí jsou známy dolní meze tvaru $\liminf d_N^2\log N\ge\sum_\rho
m_\rho^2/|\rho|^2$ přes nuly na kritické přímce (Burnol) a domněnka
$d_N^2\sim(2+\gamma-\log4\pi)/\log N$ (Báez-Duarte, Balazard, Landreau,
Saias); tyto výsledky nebyly v tomto sezení ověřeny a jejich přenos do
$B$-normy zde není proveden. Pozorovaná rychlost je s takovým chováním
slučitelná a geometrický pokles $2\cdot4^{-J}$ sondy se v $V_K$ nekoná.
Konečná tabulka není pokrokem k RH, v souladu s vlastnickým verdiktem
„Žádný konečný prefix není pokrokem k RH“ (`notes/verdicts`).

**Co sonda skutečně přináší.** (i) Přesný, konečný a racionální způsob, jak
vyčíslit celou nekonečnou chybu každého přípustného kandidáta (§6–§8);
(ii) přesnou identifikaci nejmenší chybějící posloupnosti $a_1$ a jejího
Mellinova obrazu; (iii) po této revizi: přesnou velikost mezery $\tau(m)-1$
z $m$ (3.2), vynucenost základu 2 (3.3), a Hurwitzův test nutných podmínek
pro každou vrstvu (3.6). Nic z toho není důkaz RH ani jeho část.

## 5. Propojení s dosavadní prací TWIST-J

- **Jedna zeď, další čtení.** `notes/RH-ONE-WALL-CROSSREF_2026-08-17.md`
  eviduje čtyři úrovně jedné překážky (leg, kernel, measure, capacity) a
  pravidlo počítání. Tato sonda je čtení na NB úrovni: Gram/Schurův objekt
  $d_K^2=2-b^{\mathsf T}G^{-1}b$ je Schurův doplněk ohraničené Gramovy
  matice $\begin{pmatrix}2&b^{\mathsf T}\\ b&G\end{pmatrix}$, tedy přesně
  typ objektu, který požaduje otázka F3 v
  `notes/C-RH-PYTHAGORAS-HALFANGLE-N/PREREG.md`, ale na straně cíle
  ($\mathbf1$), ne na straně prvočísel. Ortogonální vrstvy sondy rozkládají
  cíl, half-angle lane rozkládá prvočíselnou stranu na čtverce; nejde o týž
  objekt a nesmí být účtovány jako táž věta.
- **Zabitá NB trasa.** `probes/P-PENTAGON-ONLY-DILATIONS-1`
  ($\to$ `J-LI-PENTAGON-DILATION-DEFICIENCY [T]`, `PENTAGON-ONLY-DILATIONS [F]`)
  a opuštěná `probes/P-FINITE-PRIME-SUPPORT-DILATIONS-1`: Věta 3.4 je jejich
  diskrétní dvojče a rozšíření. Recon v `notes/C-WEIL-REALIZATION-1`
  (Route 3, Nyman–Beurling / Báez-Duarte, „Expected KILL“) očekával přesně
  tento typ výsledku pro pentagonové dilatace. Sonda pentagonové omezení
  nemá; používá všechny moduly a základ 2 jen pro účetnictví a směrování.
- **2-adické versus 5-adické.** Program má 5-adickou mřížku
  ($2\pi\tfrac14\mathbb Z[1/5]$, délky cyklů $4\cdot5^a$,
  `LAMBDA-COCYCLE-GRID-EQUIVALENCE [T]`). Podle 3.3 je binární základ sondy
  vynucen přípustností semínka; přechod na základ 5 by semínko
  $\mathbf1_{5\nmid n}$ vyvedl z konečného obalu. NB-binární trasa tedy
  není J-nativní a nemá s pentagonovou strukturou přímé spojení; to je
  zjištění, ne vada.
- **RH jako programová závislost.** V letu je návrh
  `notes/canon/RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md` (větev
  `notes/rh-program-dependence-2026-09-08`) registrovat `RH-PROGRAM-DEPENDENCE [H]`;
  živé obligace `LAMBDA-COCYCLE-ANGLES [H]` a
  `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` mají RH-sílu. Sonda je kandidátní
  cesta k téže závislosti, nezávislá na J-nativních nosičích; nic z ní
  nemění status těchto řádků.
- **Hardyho/modelové prostory.** Viz 3.7: stejný $H^2(\Re s>1/2)$, jiný
  objekt. Případné ztotožnění schodovitého podprostoru se Suzukiho $V(0)$
  by byla samostatná otázka s vlastním identifikátorem.
- **Lean laboratoř.** `notes/lean-j-cyclotomic` (Lean 4.30.0, Mathlib
  `c5ea0035…`, ruční build, bez CI gate) je jediné prostředí, kde
  formalizace může proběhnout beze změny politiky; viz `LEAN-PLAN-CZ.md`.

**Co by mohlo být formálním krokem a co ne.**
Kandidát `T` s ověřovačem: Věta 3.4 v diskrétním nosiči (elementární,
úplný důkaz, nový identifikátor, jmenovat opuštěného předchůdce).
Kandidát `C`: přesná racionální tabulka $d_K^2$ a koeficienty pro
$K\le K_0$ (výpočet bez RH obsahu, dvouarchitekturová brána stdout).
Nic zde není pohyb statusu RH; RH zůstává `O`-silná obligace.

## 6. Rozsah ověření

`verify_rh_binary_review.py` byl napsán z matematických tvrzení sondy, ne
z jejího skriptu. Používá jen `int`, `fractions.Fraction`, `itertools`,
`random` se semínkem `20260910` a `json`. Běh: **487 677 úspěšných kontrol
v 10 skupinách** (stdout přiložen, exit 0, prázdný stderr, asi 70 s CPU):

```text
A weights                    5005
B dilation                   20726
C routing                    78809
D obstruction                232828
E Dirichlet coefficients     50041
F periodic formula           650
G Gram                       534
D2 residue classes           51
D3 finite prime support      79928
H density from D_m           19105
```

Skupina F testuje cyklickou formuli proti hrubé sumě prvních 14 bloků
s oboustranným uzávěrem konce $2^{1-J}\min q\le\text{konec}\le2^{1-J}\max q$
a proti invarianci vůči násobku periody; to je nezávislé na odvození §6.
Skupina G reprodukuje tabulku §7, rozšiřuje ji do $K=40$ a ověřuje
pythagorejský zákon poklesu pro každé $K$. Jediný blok s plovoucí čárkou je
označen jako diagnostika a nic netvrdí. Běh neověřuje žádné tvrzení o všech
$K$ ani nulách $\zeta$.

## 7. Prameny

Citace [1]–[4] jsou převzaty ze sondy (viz `NOTE-SOURCE-CZ.md`); v tomto
sezení nebylo možné je síťově ověřit. Dodatečný kontext pro §4, rovněž
neověřený v tomto sezení: J.-F. Burnol, *A lower bound in an approximation
problem involving the zeros of the Riemann zeta function*, Adv. Math. 170
(2002); L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias, *Notes sur la
fonction ζ de Riemann, 3*, Adv. Math. 149 (2000).
