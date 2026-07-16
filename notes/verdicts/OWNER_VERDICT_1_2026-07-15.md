Verdikt: útok se skutečně posunul. Máme přesný aritmetický zdroj, konečný pozitivní model a první Liho kalibrační vektor. G5 však zůstává celý otevřený. Volím cestu **(a): hlavním cílem zůstává (W_\xi)**.
Jedna formulace ve shrnutí ale opravdu praská.
## Povinná oprava
Gaussův most
[
4\zeta_5^n=
\sum_{r=0}^{3}\overline{\chi}^{,r}(n),g(\chi^r)
]
platí pouze pro (5\nmid n). Pro (n=5) je levá strana (4), pravá strana (0).
Celoplošná verze je
[
\boxed{
4\zeta_5^n=
4\mathbf 1_{5\mid n}
+
\sum_{r=0}^{3}\overline{\chi}^{,r}(n),g(\chi^r).
}
]
To není kosmetika. Multiplikativní DFT nevidí ramifikovanou třídu (0\bmod 5). Semilokální blok ({\infty,5}) je proto povinný.
Také rozlišit:
[
g(\chi)\overline{g(\chi)}=5,
\qquad
g(\chi)g(\bar\chi)=\chi(-1),5=-5
]
pro kvartický lichý charakter.
## Status tří pilířů
| Pilíř                                | Přesný verdikt                        |
| ------------------------------------ | ------------------------------------- |
| A: torální dynamická zeta            | Algebraické jádro candidate-T         |
| A: „plenum prochází vlastní RH“      | D, nikoli standardní T                |
| B: invariantní podmříže (=) ideály   | Silné candidate-T                     |
| B: ideálová zeta (=\zeta_K)          | candidate-T po lokální opravě nad (5) |
| B: „primy jsou výstup kroku“         | D se silným T jádrem                  |
| C: vzorec a interval pro (\lambda_1) | candidate-T                           |
| celý Liho žebřík kladný              | O, přesně RH-ekvivalentní             |
| Weilova pozitivní realizace          | O                                     |
### Pilíř A
Nosič musí být výslovně
[
T_J:\mathbb T^4\to\mathbb T^4,\qquad[x]\mapsto[M_Jx].
]
Pak
[
F_m=#\operatorname{Fix}(T_J^m)
=\left|\det(M_J^m-I)\right|
=N_{K/\mathbb Q}(J^m-1).
]
(F_m) počítá body s periodou dělící (m), nikoli body přesné periody (m). Nejde také automaticky o zetu plného časově řízeného kroku (\Pi_{t_n}M_J).
Rozklad
[
\chi_{\wedge^2M_J}(x)
=(x^2-3x+1)\Phi_{10}(x)
]
sedí. Smíšený sektor (E^+\wedge E^-) má přesně primitivní desáté odmocniny jednotky. To je čisté T. Celá Artinova–Mazurova zeta ale obsahuje také kružnice (\varphi^{\pm1}) a póly (\varphi^{\pm2}), takže „vlastní RH“ smí zůstat pouze jako konečný dynamický analog [D]. Standardní torální formule skutečně používá exterior powers a počty (|\det(I-M^m)|). [Baake, Lau a Paskūnas](https://arxiv.org/abs/0810.1855)
### Pilíř B
Nejsilnější nový výsledek je
[
\boxed{
{\text{konečně indexové }M_J\text{-invariantní podmříže }\mathcal O_K}
======================================================================
{\text{nenulové integrální ideály }\mathcal O_K}.
}
]
Důvod je přesný:
[
\mathbb Z[J]=\mathbb Z[\zeta_5]=\mathcal O_K.
]
Proto invariantní podmřížová zeta je přesně
[
\zeta_{\mathrm{inv}}(s)=\zeta_K(s)
=\zeta(s)L(s,\chi)L(s,\chi^2)L(s,\chi^3).
]
To je skutečný J-nativní původ Dedekindovy aritmetické strany. Definice přes ideály a jejich normy je standardní. [Kedlayovy poznámky](https://kskedlaya.org/math204c-spr15/dedekind-zeta.pdf)
Notaci diskriminantu zmrazit jako
[
\operatorname{disc}K=5^3=5^{[K:\mathbb Q]-1},
]
ne jako (p^d), pokud (d) jinde znamená čtyřrozměrný nosič.
## Volba rozsahu
Hlavní O zůstává:
[
\boxed{J\text{-WEIL-POSITIVE-REALIZATION nad }W_\xi.}
]
Forma pro (\zeta_K) je jiný, širší závazek. Její pozitivita by řešila celý Dirichletův paket, tedy problém silnější než samotné RH. Nemá se potichu zaměnit za (W_\xi).
Případný most musí být (C_4)-ekvivariantní:
[
\mathcal H_K=\bigoplus_{\chi\in\widehat{C_4}}\mathcal H_\chi,
]
a triviální sektor musí přesně reprodukovat:
* (W_\xi),
* (\Lambda(n)), včetně (p=5),
* standardní archimédovský člen,
* póly a triviální nuly.
Bez sektorové identity může kladnost celkové formy pouze maskovat záporný triviální sektor.
## Liho žebřík
[
\lambda_1
=========
1+\frac{\gamma}{2}
-\frac12\log(4\pi)
==================
0.0230957089661210338\ldots
]
a uvedený interval hodnotu obsahuje. Liho kritérium však říká
[
\mathrm{RH}
\iff
\lambda_n\ge0
\quad\text{současně pro všechna }n\ge1.
]
Žádný konečný prefix není pokrokem k RH. Je pouze kalibračním a falsifikačním testem budoucí uniformní realizace. [Lagarias o Liho koeficientech](https://aif.centre-mersenne.org/articles/10.5802/aif.2311/)
Pro (\lambda_2) zmrazit konvenci
[
\zeta(1+t)=\frac1t+\gamma-\gamma_1t+O(t^2)
]
a vzorec
[
\boxed{
\lambda_2=
1+\gamma-\gamma^2-2\gamma_1
+\frac{\pi^2}{8}-\log(4\pi).
}
]
Kritický falsifikátor je znaménko (-2\gamma_1). (\lambda_2) je brána G3/G4, nikoli G5.
## Doporučený veřejný rozpad
Nespojoval bych A a B do jednoho `P-PLENUM-ZETA-1`. Jsou to dvě různé zety bez dokázaného liftu:
1. `P-J-CARRIER-IDEAL-ZETA-1`
   Invariantní podmříže, (\zeta_K), splitting, Gaussův most s členem (4\mathbf1_{5\mid n}).
2. `P-J-TORAL-ZETA-1`
   Periodické body, Artinova–Mazurova zeta, exterior powers a smíšený (\Phi_{10}) sektor.
3. `P-J-FINITE-DILATION-NOGO-1`
   Falsifikátor, že konečný racionální dynamický determinant sám nemůže být (\xi), která má nekonečný divisor.
4. `J-LI-LAMBDA-2`
   Kalibrační intervalová brána.
5. `J-LI-ALL-N` `[O]`
   Jediná uniformní pozitivní konstrukce pro celý žebřík.
Přiložený soubor obsahuje starší kotvu `C-PENTAGON-WEIL-1`, nikoli nové tři soubory ani 21k verifier. Matematické endpointy jsem ověřil, ale konkrétních 14 asercí a jejich pin zatím nemohu potvrdit řádek po řádku.
Konečný stav: **O dostalo přesnou páteř, ale jediný skutečný nový zásah do zdi bude uniformní (C_4)-sektorová pozitivita pro všechna (n).** Současné tři pilíře jsou velmi dobré kotvy, nikoli ještě trhlina v G5.
