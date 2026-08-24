# BREAK: nezávislý pokus rozbít Omega_0 start-family freeze (PR #190)

```text
LANE BREAKER, inkubační lano projektu. ŽÁDNÁ AUTORITA. Nic nepromuje,
nic nemrazí, nemění status, scope, registry ani frontier.

PŘEDMĚT   notes/canon/P-DMATTER-TOTAL-1-OMEGA0-START-FAMILY-OWNER-FREEZE.md
          v draft PR #190, commit cd2cb46c, SHA-256 ae488099..., 16884 B.
METODA    nezávislá cesta. Generátory a,b,c,d,e postaveny ze slovní
          definice v canon/CANON.md sekce 3 a update ze sekce 2. Žádný
          vzorec odvozený uvnitř freeze dokumentu není použit jako vstup;
          tabulka listů, fázový zákon i rovnice (3), (4), (5) jsou
          přepočítány, ne citovány.
FALZIFIKÁTOR tohoto breakeru: jakýkoli PASS, který nelze reprodukovat
          spuštěním přiloženého skriptu, je chyba tohoto dokumentu.
```

## 1. Řetěz a měna, ověřeno klonem

```text
main                f6f797739be21acfa70851be544c994ea17b7f5a, Canon v24
canon/SHA256SUMS    5 z 5 OK na hlavě #190
řetěz ancestry      dfea3e2 (#183) < 486c4d2 (#188) < 35c98d6 (#189)
                    < cd2cb46 (#190), striktně lineární
artefakt SHA-256    ae488099bdf0c1a66bd234be74f8909110d04c7f817789c81de9ef83509412dc
                    16884 B, souhlasí s vlastníkovým záznamem
canon/ dotčeno celým řetězem   0 souborů
diff #190 proti main           4 soubory, všechny notes/canon/
```

Kontroly na hlavě #190, čistý strom:

```text
tools/check_policy.py       POLICY PASS
unittest discover -s tools  OK, 59 testů
tools/check_canon.py        CANON PASS v24 claims=208
tools/check_ledger.py       LEDGER PASS claims=208 items=224 dependencies=330
```

Merge dry-run proti main: #183, #188, #189, #190 i #180 jsou všechny
MERGEABLE, a #180 zůstává mergeable i po #190.

DŮSLEDEK, KTERÝ SE VYPLATÍ VYSLOVIT. Řetěz je kumulativní. `#190` obsahuje
všechny čtyři commity, takže merge samotného `#190` přinese všechny čtyři
soubory. Pořadí `#183 -> #188 -> #189 -> #190` je tedy požadavek na
readback, ne na obsah.

## 2. Breaker, 0 zabití

Skript: `claude/break_omega0_start_family.py`

```text
soubor SHA-256   3f359c1b310a2e49d8f045f816851a715c49873121ffae03a534b462ac1023b1
bytes            7870
stdout SHA-256   aff807770f7abcaf0a00db12803cd3a11cc175d74fe922ea70a58996944afc32
běh              x86_64, Python 3.11.15, LC_ALL=C TZ=UTC PYTHONHASHSEED=0
doba             pod 1 s
aritmetika       pouze celá čísla mod 5; 0 dělení, 0 float literálů,
                 ověřeno AST průchodem; jen standardní knihovna
```

Toto NENÍ probe-grade verifier. Nebyl preregistrován, nebyl pinnut před
během a neběžel na dvou architekturách. Je to lane breaker.

Co bylo přepočítáno vyčerpávajícím průchodem všech 15 625 stavů:

```text
A  a^2=b^2=c^2=d^2=e^2=id a (bc)^5=id                          PASS
B  fázový zákon z_6(g(x)) pro všech pět generátorů             PASS
C  tabulka listů t=0 a t=1, spočtena, ne citována              PASS
D  (theta_0,theta_1,theta_2)=(0,1,1); obrazové listy
   {0..4}, {0,4}, {1,2}, {1} pro n=0,1,2,3                     PASS
E  hodnosti obrazů E_0..E_6 = 15625, 6250, 6250, 3125,
   3125, 3125, 3125                                            PASS
F  E_3|X_z : X_z -> X_1 bijekce pro všech pět z                PASS
G  tail kvocient Z DEFINICE, ne z rovnice (4): rozklad
   indukovaný E_n má 15625, 6250, 6250, 3125, 3125, ...
   tříd, tedy stabilizuje přesně v n=3; |K0|=15625,
   |Ktail_0|=3125, každá třída má právě pět hlav, právě
   jednu v každém počátečním listu                             PASS
H  obě přesné kontroly citované ve freeze, včetně
   F_0(x)=F_0(y)=(2,1,3,4,4,0) a E_3(x')=E_3(y')=(0,0,0,0,0,1) PASS
I  všech 31 neprázdných listových podrodin: kvocient je
   kanonicky X_1 a vlákno má velikost |Z|                      PASS
J  hlava, úplná stopa a A_0 nesestupují; časová čtení
   sestupují pro každé n>=3, ověřeno do n=7                    PASS
```

Minimalita hloubky 3 je ověřena tvrdě, ne slovně: rozklad v n=2 má 6250
tříd, tedy ostře více než 3125, takže n=3 je skutečně první čas, kdy
kvocient dosedne.

**Výsledek: 0 zabití. Každé tvrzení freeze se reprodukuje přesně.**

## 3. Jediný nález: univerzalita je saturace, ne obecná věta

Sekce K breakeru. Tvrzení „pro všech 31 neprázdných listových podrodin je
tail quotient kanonicky tentýž X_1“ je pravdivé, ale třída rodin je zvolena
přesně tam, kde je tvrzení vynucené. Listová sjednocení jsou totiž právě ty
rodiny, které protínají každé E_3-vlákno. Jakmile se z té třídy vyjde,
kanonicita padá:

```text
rodina                                   počet tail tříd
jeden bod                                              1
jedno celé E_3-vlákno (5 bodů, 1 z každého listu)      1
deterministická podmnožina 3125 bodů (každý pátý)   1250
1000 bodů z X_0                                     1000
```

Obecné a poctivější znění je: pro libovolnou neprázdnou `S` je tail
kvocient rodiny `{0} x S` kanonicky `E_3(S) subset X_1` s vlákny
`|S ∩ E_3^-1(bod)|`, a rovná se celému `X_1` právě tehdy, když `S` protíná
každé E_3-vlákno. Listová sjednocení to splňují automaticky.

To freeze nezabíjí. Freeze sám říká, že jde o „adversarial control on the
owner premise“ a že „tail agreement alone cannot force the all-five-sheet
choice“, což je přesně správný, slabší závěr. Ale formulace „budoucnost je
lokálně univerzální“ je silnější, než co bylo dokázáno, a při přenosu do
prózy je to místo, kde se tvrzení nafoukne. Doporučené znění: univerzalita
platí na E_3-saturovaných rodinách, a listová sjednocení jsou jejich
speciální případ.

## 4. Co se tímto NEpohnulo

```text
QUADRATIC-DECODER-DATA        O / STOP, nezměněno
READY-FOR-CLASSIFICATION      NO
veřejné K                     UNRESOLVED
dom(D_matter)                 UNRESOLVED
registry, frontier, canon     beze změny, 208 claimů, 27 živých
```

Freeze sám vypisuje šestnáct polí `public_K_*` a `public_Dmatter_*` jako
UNRESOLVED. Ten seznam je celá vzdálenost mezi
`READY-FOR-CLASSIFICATION: NO` a `YES`. Nic jiného QDD ze STOP nesundá.

## 5. Stav lana, měřeno

Dnešní kadence QDD lana ve veřejné lince:

```text
#183  14:51   notes: expose QDD context-origin obstruction
#188  15:28   notes: adopt conditional adjacent QDD dictionary
#189  15:54   notes: predefine public K orbit representations
#190  16:35   notes: freeze Omega0 start family
```

Čtyři PR za necelé dvě hodiny, ani jeden zmergovaný, zásobník čtyři hluboký
a `#190` má ve vlastním textu instrukci, že se nesmí mergovat, dokud
`#183`, `#188` a `#189` nebudou zmergovány a přečteny zpět z veřejného
`main`, v tomto pořadí.

Křížově s měřením z `claude/AUDIT-EXTERNAL-NADHLED-V24_2026-07-27.md`:
za sedm zapečetěných foldů v18 až v24 přibylo D +0 a C +0, READY kleslo
10 na 7 a STOP stouplo 5 na 12. Dnešní čtyři PR ten trend nelámou, pokračují
v něm. Produkce definic je rychlejší než jejich ratifikace, a rozdíl se
kumuluje v zásobníku, ne v registru.

## 6. Doporučené pořadí

```text
P0  Zmergovat zásobník. Obsah je notes-grade, canon se nemění ani o bajt,
    všechny kontroly zelené a všech pět PR je mergeable. Nic to neblokuje
    kromě stisknutí tlačítka. Každý další článek přidává jeden readback
    a jednu příležitost k rozvětvení.
P1  Vybrat vidlici, kterou freeze sám vypisuje: A retain Omega_0,
    B přejít na S_3 a explicitně přijmout ztrátu pětinásobné genesis
    identity, C jiná rodina, D STOP. Sekce 5 freeze už ukazuje, že pod
    podmínkou zachování hlavy, stopy a A_0 je přípustná právě jedna
    třída, tedy A. To je jeden podpis, ne další dokument.
P2  Teprve pak šestnáct UNRESOLVED polí public_K_* a public_Dmatter_*.
    To je jediný seznam, jehož uzavření hne QDD.
```

Poznámka k dřívějšímu doporučení. Audit z dnešního rána navrhoval jako P0
rozhodnout `C-ARCH-UNIVERSALITY-1`. Freeze v sekci 0 uvádí ten balík jako
`rejected`. Rozhodnutí padlo, dřívější P0 se tímto stahuje.
