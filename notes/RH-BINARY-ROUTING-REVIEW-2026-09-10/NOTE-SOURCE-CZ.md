# RH: binární skládání, ortogonální vrstvy a přesná racionální norma

```text
STATUS   NON-CANONICAL. Revidovaný zdrojový text, uložen doslovně pro
         auditovatelnost revize v REVIEW-CZ.md. Autor: vlastník programu.
DATE     2026-09-10
```

**Pracovní poznámka, 10. září 2026. Není to důkaz RH.**

Tato sonda navazuje na otázku, zda lze Riemannovu hypotézu dokázat v původním celočíselném prostoru a teprve poté přenést výsledek do komplexní roviny. Nezasahuje do repozitáře ani do kánonu TWIST-J. Netvrdí bibliografickou novost uvedených elementárních odvození.

Výsledek má tři části. Máme přesný binární postup s geometricky klesající **celkovou** kvadratickou chybou. Víme, proč tento postup zatím není důkazem RH: neprokázali jsme přípustnost jeho výstupů v potřebném uzavřeném lineárním prostoru a přesná konečná přípustnost selhává již ve druhém kroku. A máme konečný racionální výpočet celé nekonečné normy každé periodické racionální posloupnosti, tedy i všech konečných kombinací původních zbytků.

## 1. Přesné zadání a změna normy

Pro $n\ge1$, $k\ge2$ položme

$$r_k(n)=n\bmod k,\qquad \mathbf1=(1,1,\ldots).$$

Původní norma je

$$\|x\|_H^2=\sum_{n=1}^{\infty}\frac{|x_n|^2}{n(n+1)}.$$

Bagchiho posloupnostní formulace Nymanova–Beurlingova–Báez-Duarteova kritéria říká, že RH je ekvivalentní příslušnosti $\mathbf1$ k uzavřenému lineárnímu obalu zbytků. Je rovněž ekvivalentní hustotě tohoto obalu v celém $H$ [1]. Bagchi používá $r_k/k$; násobení jednotlivých generátorů nenulovými čísly jejich lineární obal nemění.

Použijeme rovnocennou normu

$$\|x\|_B^2=\sum_{j=0}^{\infty}4^{-j}\sum_{n=2^j}^{2^{j+1}-1}|x_n|^2.$$

Pro $2^j\le n<2^{j+1}$ máme

$$\frac1{n(n+1)}\le4^{-j}\le\frac4{n(n+1)}.$$

Proto

$$\|x\|_H^2\le\|x\|_B^2\le4\|x\|_H^2.$$

Normy mají stejné konvergentní posloupnosti a stejné uzavřené lineární podprostory. Označme

$$V=\overline{\operatorname{span}_{\mathbb Q}\{r_k:k\ge2\}}.$$

Pracujeme s reálnými posloupnostmi; konečné racionální kombinace mají stejný uzávěr jako konečné reálné kombinace. Po případném komplexním rozšíření tedy platí známé kritérium beze změny:

$$\mathrm{RH}\iff\mathbf1\in V\iff V=H.$$

Normalizace: $\|\mathbf1\|_H^2=1$, ale **$\|\mathbf1\|_B^2=2$**.

## 2. Přípustné opakování souřadnic

Při pomocné konvenci $x_0=0$ definujme

$$(D_mx)_n=x_{\lfloor n/m\rfloor},\qquad m\ge2.$$

Z teleskopické rovnosti

$$\sum_{n=ma}^{m(a+1)-1}\frac1{n(n+1)}=\frac1m\frac1{a(a+1)}$$

plyne

$$\|D_mx\|_H^2=\frac1m\|x\|_H^2.$$

Z dělení se zbytkem navíc přímo dostaneme

$$D_mr_k=\frac{r_{mk}-r_m}{m}.$$

Proto $D_mV\subseteq V$. Tato dilatační struktura odpovídá semigrupě z [1]; zde je přepsána do celočíselných souřadnic bez odmocnin v definici zobrazení.

Pro $m=2$ platí také přesná binární identita

$$\|D_2x\|_B^2=\tfrac12\|x\|_B^2.$$

Samotné opakování však neřeší cílovou úlohu. Iterace $f_{J+1}=r_2+D_2f_J$, $f_0=0$, konverguje k počtu jedniček v binárním zápisu $n$, nikoli ke konstantě jedna. Již pro $n=3=(11)_2$ dává limitně hodnotu dva.

### Pevná překážka pro pouhé mocniny dvojky

Každá konečná kombinace $r_{2^j}$ splňuje

$$f(3)=f(1)+f(2).$$

Tato podmínka přetrvá při normové limitě, protože vyhodnocení libovolné pevné souřadnice je spojité. Konstantní posloupnost ji nesplňuje.

Přesněji, funkcionál $\ell(x)=x_1+x_2-x_3$ má v binární normě čtverec normy $1+4+4=9$. Pro každý prvek dyadického uzavřeného obalu proto

$$\|\mathbf1-f\|_B^2\ge\frac19.$$

Jde o zákaz omezení **modulů na mocniny dvojky**, nikoli o zákaz binárního počítání se všemi moduly.

## 3. Binární směrování: správný cíl a přesný Pythagoras

Definujme druhé lineární zobrazení

$$(Cx)_{2n}=x_n,\qquad (Cx)_{2n-1}=0,\qquad n\ge1.$$

Na rozdíl od $D_2$ neopakuje hodnotu do obou potomků; ukládá ji pouze do sudé souřadnice. Protože binární váha splňuje $w_B(2n)=w_B(n)/4$,

$$\boxed{\|Cx\|_B^2=\tfrac14\|x\|_B^2.}$$

V původní normě platí $\|C\|_H^2=1/3$, neboť poměr vah je $(n+1)/(2(2n+1))$ a maxima nabývá pro $n=1$. Pro další práci je výhodnější přesná binární rovnost.

Nyní máme přesnou rovnici

$$\mathbf1=r_2+C\mathbf1.$$

Iterace

$$f_0=0,\qquad f_{J+1}=r_2+Cf_J$$

má explicitní řešení

$$f_J(n)=\begin{cases}0,&2^J\mid n,\\1,&2^J\nmid n.\end{cases}$$

Důkaz je indukce podle poslední binární číslice. Pro liché $n$ dá $r_2(n)$ jedničku a směrovaný člen je nula; pro sudé $n$ je nová hodnota starou hodnotou na $n/2$.

Chyba je tudíž $\mathbf1-f_J=C^J\mathbf1$ a

$$\boxed{\|\mathbf1-f_J\|_B^2=\frac2{4^J}.}$$

Nejde o odhad prvních souřadnic. Je to přesná hodnota celé nekonečné normy.

### Ortogonální celočíselné vrstvy

Položme

$$a_j=C^jr_2=\mathbf1_{\{n:2^j\mid n,\ 2^{j+1}\nmid n\}}.$$

Vrstva $a_j$ rozpoznává právě čísla s $j$ nulami na konci binárního zápisu. Vrstvy jsou navzájem ortogonální, protože mají disjunktní podpory, a

$$\mathbf1=\sum_{j=0}^{\infty}a_j,\qquad
\|a_j\|_B^2=\frac{3}{2\cdot4^j}.$$

Tedy

$$\|\mathbf1\|_B^2=\sum_{j=0}^{\infty}\|a_j\|_B^2=2.$$

Toto je skutečná pythagorejská stavba v prostoru celočíselných posloupností. Sama o sobě ještě neříká, že jednotlivé vrstvy patří do $V$.

## 4. Přesné místo, kde selže konečná realizace

První nová vrstva je

$$y=Cr_2,\qquad y(n)=\mathbf1_{\{n\equiv2\pmod4\}}.$$

**Tvrzení:** $y$ není žádnou konečnou lineární kombinací původních $r_k$, a to ani s libovolnými reálnými či komplexními koeficienty a moduly.

**Důkaz pouze v celých číslech.** Předpokládejme $y=\sum_{k\in F}c_kr_k$ pro konečnou množinu $F\subset\{2,3,\ldots\}$ a označme $c=\sum c_k$. V souřadnici jedna je $y(1)=c$, tedy $c=0$.

Zvolme $L$ dělitelné čtyřmi a všemi moduly v $F$. Pro každé $k\in F$ máme

$$r_k(L-1)-r_k(L-2)=1.$$

Proto by $y(L-1)-y(L-2)=c=0$. Ve skutečnosti $y(L-1)=0$, $y(L-2)=1$, takže rozdíl je $-1$. Spor.

Z toho plyne také, že $f_2=r_2+Cr_2$ není konečnou kombinací zbytků. Tento důkaz **nevylučuje normové přibližování** pomocí stále dalších modulů. Svědecké $L$ závisí na použitých modulech a nemáme zde pevný spojitý funkcionál, který by oddělil $y$ od celého uzavřeného obalu.

### Přesná podmínka přípustnosti

$$\boxed{\mathrm{RH}\iff C(V)\subseteq V.}$$

Pokud RH platí, známé kritérium dává $V=H$, takže přípustnost $C$ je samozřejmá. Opačně: při $C(V)\subseteq V$ leží celá iterace $f_J$ v $V$ a její normová limita je $\mathbf1$, což dokazuje RH.

Stačí slabší podmínka $a_j\in V$ pro každé $j$; i ta je RH ekvivalentní. Samotná příslušnost první nové vrstvy $a_1$ zde prokázána není a sama nebyla prokázána jako postačující.

Uzavřenost při směrování jsme tedy **nedokázali**. Její pouhé předpokládání by schovalo RH do definice přípustných kroků. Příbuzné formulace RH pomocí invariantnosti podprostorů při dalších operátorech existují také v literatuře [3]; nejde samo o sobě o vyřešení problému.

## 5. Co přesně se změní při převodu do komplexní roviny

Pro $\Re s>1/2$ je příslušný převod

$$\Pi(x)(s)=\frac1s\sum_{n\ge1}x_n\bigl(n^{-s}-(n+1)^{-s}\bigr).$$

Pro konečnou kombinaci zbytků

$$\Pi\!\left(\sum_kc_kr_k\right)(s)
=\frac{\zeta(s)}s\sum_kc_k(1-k^{1-s}).$$

U směrované vrstvy $y=Cr_2$ však přímý výpočet dává

$$\boxed{\Pi(y)(s)=\frac{(1-2^{-s})(2^{1-s}-1)\zeta(s)+\beta(s)}{2s},}$$

kde $\beta(s)=\sum_{m\ge0}(-1)^m/(2m+1)^s$ je Dirichletova beta funkce.

K ověření stačí rozdíly $\Delta y(n)$: při zbytcích $1,2,3,0$ modulo čtyři mají hodnoty $0,1,-1,0$. Koeficientově tedy

$$2\Delta y(n)=-1+3\mathbf1_{2\mid n}-2\mathbf1_{4\mid n}+\chi_4(n).$$

Sečtení Dirichletovou řadou pro $\Re s>1$ dá uvedenou identitu; do $\Re s>1/2$ pokračuje analytickou identitou. Součin před $\zeta$ má v $s=1$ odstranitelnou singularitu.

Při hypotetické nule $\rho$ funkce $\zeta$ s $\Re\rho>1/2$ by každý vektor z $V$ dával při tomto čtení nulu. Pro $y$ vychází $\beta(\rho)/(2\rho)$. Neprokazujeme zde, že toto číslo musí být nenulové; vzorec pouze přesně ukazuje dodatečný člen, který nelze přehlédnout.

## 6. Celá periodická norma je přesně racionální

Tato část odstraňuje potřebu numericky odřezávat nekonečný konec při výpočtech s konečnými kombinacemi zbytků.

Nechť $q_n$ je racionální periodická posloupnost s periodou $L$. Při výpočtu normy bude $q_n=|x_n|^2$, při skalárním součinu $q_n=x_ny_n$. Hodnoty periody indexujeme od $0$ do $L-1$. Definujme

$$S=\sum_{r=0}^{L-1}q_r,\quad \overline q=S/L,\quad
P(r)=\sum_{a=0}^{r-1}q_a,\quad \eta(r)=P(r)-r\overline q.$$

Pro součet prvních $M$ členů od indexu nula máme

$$A(M)=M\overline q+\eta(M\bmod L).$$

Označme $b_j=2^j\bmod L$. Součet v binárním bloku je

$$A(2^{j+1})-A(2^j)=2^j\overline q+\eta(b_{j+1})-\eta(b_j).$$

Proto

$$\sum_{j\ge0}4^{-j}\sum_{n=2^j}^{2^{j+1}-1}q_n
=2\overline q+\sum_{j\ge0}4^{-j}\bigl(\eta(b_{j+1})-\eta(b_j)\bigr).$$

Posloupnost $b_{j+1}=2b_j\bmod L$ má konečný počáteční úsek a pak cyklus. Nechť cyklus začne na indexu $h$ a má délku $t$. Pro $d_j=\eta(b_{j+1})-\eta(b_j)$ dostáváme konečný vzorec

$$\boxed{
2\overline q+\sum_{j=0}^{h-1}4^{-j}d_j
+\frac{4^{-h}}{1-4^{-t}}\sum_{a=0}^{t-1}4^{-a}d_{h+a}.
}$$

Všechny jeho členy jsou racionální. To dokazuje tvrzení pro libovolnou periodu; konečné testy ve skriptu pouze kontrolují implementaci.

Výpočet nepotřebuje společnou periodu všech použitých modulů. Jednotlivý skalární součin $\langle r_k,r_\ell\rangle_B$ pracuje s periodou $\operatorname{lcm}(k,\ell)$. Při větších modulech mohou být cykly a čitatele/jmenovatele velké; přesnost neznamená automaticky levný výpočet.

## 7. Přesný pokles skutečné chyby v přípustném prostoru

Pro $V_K=\operatorname{span}\{r_2,\ldots,r_K\}$ sestavíme racionální matici a vektor

$$G_{k\ell}=\langle r_k,r_\ell\rangle_B,\qquad b_k=\langle\mathbf1,r_k\rangle_B.$$

Matice $G$ je kladně definitní. Konečná lineární nezávislost zbytků plyne například z rozdílů: při $\sum c_kr_k=0$ je $\sum c_k=0$ a $\sum_{k\mid n}kc_k=0$; nejmenší index s nenulovým $c_k$ pak dává spor.

Řešení $Gc=b$ je proto racionální a dává skutečné globální minimum

$$d_K^2=2-b^{\mathsf T}G^{-1}b.$$

Například pro moduly dva a tři

$$G=\begin{pmatrix}3/2&13/10\\13/10&14/5\end{pmatrix},\qquad
b=\begin{pmatrix}3/2\\2\end{pmatrix}.$$

Odtud

$$c_2=160/251,\qquad c_3=105/251,\qquad d_3^2=52/251.$$

První přesné hodnoty jsou

| Největší modul $K$ | Globální minimum $d_K^2$ |
| ------------------ | -----------------------: |
| 2                  |                    $1/2$ |
| 3                  |                 $52/251$ |
| 4                  |                 $95/766$ |
| 5                  |        $987196/11709287$ |
| 6                  |         $168677/2018075$ |

Pro přidání dalšího generátoru máme přesný pythagorejský zákon. Je-li $P_K$ kolmý průmět na $V_K$, $e_K=\mathbf1-P_K\mathbf1$ a $z_{K+1}=r_{K+1}-P_Kr_{K+1}$, pak

$$\boxed{d_{K+1}^2=d_K^2-
\frac{|\langle e_K,r_{K+1}\rangle_B|^2}{\|z_{K+1}\|_B^2}.}$$

Racionalita všech členů plyne z předchozí části. Toto je pokles **celé** chyby uvnitř správného přípustného prostoru. Nezaručuje však, že součet všech poklesů vyčerpá počáteční hodnotu dva. Právě obecný důkaz $d_K\to0$ chybí. Konečná monotónnost ani zde uvedené hodnoty nejsou důkazem RH.

## 8. Místní rovnice a globální osvědčení

Binární směrování dává ještě pomocnou rovnost, použitelnou bez předpokladu RH. Pro libovolné $f\in H$ položme

$$R(f)=r_2+Cf-f.$$

Protože $\mathbf1=r_2+C\mathbf1$,

$$R(f)=(I-C)(\mathbf1-f).$$

Z $\|C\|_B=1/2$ plyne

$$\tfrac12\|\mathbf1-f\|_B\le\|R(f)\|_B
\le\tfrac32\|\mathbf1-f\|_B,$$

tedy

$$\boxed{\frac49\|R(f)\|_B^2\le\|\mathbf1-f\|_B^2\le4\|R(f)\|_B^2.}$$

Klesání této místní chyby pro nějakou posloupnost **přípustných** $f\in V_K$ by postačovalo. Jejich zbytky $R(f)$ jsou periodické a jejich normy lze opět spočítat přesně. To není automaticky snazší důkaz: jen přesný způsob, jak z osvědčení místní rovnice získat kontrolu celého nekonečného výsledku.

## 9. Rozsah ověření

Přiložený skript používá pouze celá čísla a `fractions.Fraction`. Výchozí běh skončil **44 390 úspěšnými kontrolami ve 14 skupinách**. Ověřuje váhy binárních potomků, původní teleskopické váhy, zbytkové dilatace, binární iteraci, normový zákon směrování, cyklický vzorec proti nezávislým mezím konce, celé binární chyby, svědka pro pouhé mocniny dvojky, konečnou překážku, koeficienty převodu se členem $\beta$, normální rovnice globálních minim pro $2\le K\le10$ a osvědčení místní chyby.

Spuštění:

```bash
python verify_rh_binary.py
```

Výstup `verification.json` obsahuje přesné zlomky, koeficienty a počty kontrol. Běh neověřuje žádný předpoklad o všech $K$ a není numerickým testováním nul zeta funkce.

## Závěr

Pythagorejská binární konstrukce je skutečná a úplná jako konstrukce v celém prostoru posloupností. Přenos na RH zatím neuzavíráme, protože přípustnost směrování ve zbytkovém podprostoru zůstává neprokázána. Naopak přesný konečný převod první nové vrstvy je vyvrácen.

Druhý výsledek je výpočetní, ale přesný: pro každou konečnou kombinaci zbytků umíme v rovnocenné normě vyčíslit celou chybu konečně a racionálně. To umožňuje hledat obecnou strukturu v přesných maticích a v přípustnosti sudého směrování místo odhadování odříznutého nekonečného konce.

## Prameny

[1] Bhaskar Bagchi: *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*. Proc. Indian Acad. Sci. (Math. Sci.) 116 (2006), 137–146; arXiv:math/0607733. Použito pro posloupnostní ekvivalenci, rovnocenné váhy a dilatační invariantnost.

[2] Luis Báez-Duarte: *A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis*. arXiv:math/0202141. Rozlišuje bodové přibližování od potřebné kvadratické konvergence.

[3] Boqing Xue: *On a Hilbert Space Reformulation of Riemann Hypothesis*. arXiv:1911.04029. Příbuzné operátorové kritérium prostřednictvím invariantnosti při sdružených operátorech; naše směrování $C$ není ztotožněno s operátory této práce.

[4] François Alouges, Sébastien Darses, Erwan Hillion: *Polynomial approximations in a generalized Nyman-Beurling criterion*. arXiv:2006.02953. Kontext rozdílu mezi přibližováním v rozšířeném prostoru a kontrolou, kterou potřebuje původní kritérium.

---

Poznámka revize: skript `verify_rh_binary.py` a výstup `verification.json`, na které se text odvolává v §9, nebyly revizi k dispozici; revize používá vlastní nezávislý skript `verify_rh_binary_review.py`.
