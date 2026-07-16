Hotovo. Provenance mezera je uzavřená v projektu; GitHub větev je připravená, ale kvůli chybějícímu autentizovanému gh zatím není pushnutá.

1. Provenance verdikt

Tvrzení druhé seance bylo lokálně správné: artefakt nebyl v Git repu ani v jejím projektovém prostoru. Globálně však už existoval v Library, jen bez společného repo ukotvení. Nyní je sjednocen v trvalé složce:

TWIST - J/J-LI-SCHOENBERG-2/

Obsah:

opravený kandidátní dokument rev3;

přesný verifier 170cb04a…61bb8f;

přesný stdout 1dff8214…992e3;

SHA256SUMS;

Git patch pro vložení do repa.


Repo-ready soubory jsou také zde:

README.md



EXPECTED.txt

SHA256SUMS

Git patch


Lokální repo stav:

base:    6bb013bafb2d1c06fcb295fdbfce0f86198fd685
branch:  agent/j-li-schoenberg-2-incubation
commit:  913d1ea6ab6493af29b404a963c399ab580115fc
patch:   6805605045ddb16c89c374dac53a0ff1821e8684853bf9f53763bf01fe4d164c

main, Canon, registr ani veřejné claimy nebyly změněny. Zakázaný e-mail se nikde nevyskytuje.

Kontroly:

SHA256SUMS                    PASS
verifier == EXPECTED.txt     PASS
x86_64 Python 3.12.3         6/6 PASS
aarch64 Python 3.12.3        6/6 PASS
stdout byte-identical        PASS
POLICY                       PASS
CANON v6, 176 claims         PASS
LEDGER                       PASS
38 unit tests                PASS
git diff --check             PASS

2. Matematický audit amendmentu 2

Fixy 1, 2, 4 a 5 jsou správné. U Fixu 3 zůstává jedna nutná slovní korekce.

Pro skutečně aditivní větev

\[
Z_{\rm add}(s)=\sum_{\chi\bmod5}L(s,\chi)
\]

je Dirichletův koeficient

\[
b(n)=\sum_{\chi\bmod5}\chi(n)
=
\begin{cases}
4,&n\equiv1\pmod5,\\
0,&\text{jinak}.
\end{cases}
\]

Proto „první divergence přesně při \(n=16\)" není globálně pravda:

už při \(n=1\): \(b(1)=4\), zatímco \(a_K(1)=1\);

při \(n=5\): \(b(5)=0\), zatímco \(a_K(5)=1\), pokud ramifikovaný blok nebyl připojen;

i po odděleném ošetření \(5\) je při \(n=6\): \(b(6)=4\), ale \(a_K(6)=0\).


Hodnota \(n=16\) je výborný svědek v užším testu nezramifikovaných prvočíselných mocnin:

\[
b(16)=4,\qquad a_K(16)=1,
\]

zatímco pro rozštěpené prvočíslo \(11\):

\[
b(11)=a_K(11)=4.
\]

Ledgerová věta tedy musí znít přibližně:

> Mezi vybranými nezramifikovanými prvočíselnými mocninami první použitý rozlišující svědek je \(n=16\); jako globální Dirichletovy řady se aditivní součet a \(\zeta_K\) rozcházejí dříve.



Druhé statusové zpřesnění: AN1, AN3 a AN4 jsou dobré strojové regresní testy, ale jejich konečné rozsahy samy nedokazují obecné věty. T vzniká z algebraických identit:

\[
Q_\theta(a)
=
-\frac12\bigl(|A(\theta)|^2+|A(-\theta)|^2\bigr),
\]

\[
K_N=\frac12L_NT_{N-1}L_N^\ast,
\]

\[
\det(I-xF)^{-1}
=
\exp\!\left(\sum_{m\ge1}\frac{x^m}{m}\operatorname{Tr}(F^m)\right),
\]

a z Artinovy faktorizace. Verifiery jsou jejich auditem.

Konečný stav

\[
\boxed{\text{Provenance mezera uzavřena v projektu.}}
\]

\[
\boxed{\text{Rev3 matematicky drží po kvalifikaci svědka }n=16.}
\]

\[
\boxed{\text{J-LI-SCHOENBERG-2 je candidate-T-ready, nikoli veřejné T.}}
\]

\[
\boxed{\text{J-LI-COCYCLE-REALIZATION [O], RH [O].}}
\]

Pro budoucí veřejný probe se historické běhy nesmějí retroaktivně prohlásit za formální: musí vzniknout nový PREREG a nový pin před prvním veřejným během. zkus pokračovat na J nativní uniform cocycle
