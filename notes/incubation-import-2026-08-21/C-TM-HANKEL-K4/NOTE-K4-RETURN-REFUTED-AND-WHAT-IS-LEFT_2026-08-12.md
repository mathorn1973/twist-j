# Návrat vyvrácen. Co zbylo, a proč je toho míň, než se zdá

Status: NON-CANONICAL analýza, gates nothing. Reakce na exaktní root census
nad všemi 8093 Phase A diagonálami. 2026-08-12.

## 1. Přijímám, moje formulace padla

Řekl jsem, že invariantem je návrat, tedy rovnost počtů průchodů na obou
polovinách. Census dává 117 z 8093 protipříkladů (55 krát 0/2, 61 krát 2/0,
1 krát 1/3), plus exaktního nonorbitového svědka attempt=13520 s 0 vlevo a
2 vpravo. Vyvráceno. Čtvrtá moje hypotéza v této lane, kterou zabila data
nebo já sám, a je to v pořádku; každá zavřela jedny dveře.

## 2. Logická poznámka: parita není zbytek, je to tautologie

Tady bych byl opatrnější, než zní shrnutí. Zbylá formulace r_- kongruentní
r_+ modulo 2 NENÍ nezávislý invariant, který přežil. Je to důsledek toho, co
pozorujeme, odvoditelný na tři řádky:

```
rovné inercie konců  =>  det(K) a det(K') mají totéž znaménko, obojí
                         (-1)^(n_-)
                     =>  D(t) = det(A + tB) má v t = -1 a t = +1 totéž
                         znaménko
                     =>  počet kořenů D na (-1,1) s násobností je SUDÝ
                     =>  r_- + r_+ sudé, tedy r_- kongruentní r_+ mod 2
```

Midpointy jsou regulární, takže v nule kořen není a rozdělení na dvě
poloviny nic nepřidává. Totéž platí o „opačném netto spectral flow": ten je
jen přepsáním rovnosti inercií konců přes střed.

Takže po tomto kole nezbyl ŽÁDNÝ strukturní invariant. Zbyla parita, která
je ekvivalentní pozorování samotnému, a silná empirická koncentrace
7976/8093 = 98.55 %, která je jev, ne zákon. To je poctivá bilance a je
lepší ji vyslovit než ji nechat vypadat jako přeživší tvrzení.

## 3. Kde je skutečný obsah té tabulky

Ne v paritě, ale v prvním řádku:

```
0/0   7561   93.4 %   tětiva NEPROTNE nadplochu vůbec
1/1    414            střed v jiné komoře, jeden průchod na stranu
2/0     61            exkurze celá v levé polovině
0/2     55            exkurze celá v pravé polovině
2/2      1
1/3      1
```

Dominantní jev je RIGIDITA, ne návrat: ve 93.4 % je inercie na celém
segmentu konstantní a není co vysvětlovat návratem. Zbylých 6.6 % je jiný,
menšinový jev. Otázka se tím rozpadá na dvě, a to je pokrok, protože jedna
z nich může mít odpověď i když druhá ne:

```
Q1  proč tětiva ve většině případů vůbec neprotne nadplochu
Q2  proč se v menšině, kde protne, inercie konců přesto shodne
```

Q1 je exaktně toto: kořeny D jsou zobecněná vlastní čísla páru (M, Delta) a
otázka zní, proč leží mimo interval |t| < 1. Jedna měřená okolnost sem
patří: Delta je VŽDY singulární, rank v mém censu nikdy nedosáhl 16 (rozsah
2 až 15), takže D má stupeň nejvýše rank(Delta) a konečných kořenů je od
začátku míň než 16.

## 4. Jedno rozhodující měření, levné na existujícím korpusu

Root census počítal jen kořeny UVNITŘ okna. Rozhodující je ale, kde leží ty
VNĚ, konkrétně:

```
R*  vzdálenost nejbližšího reálného kořene D k hranici okna, tedy
    min |t| přes reálné kořeny s |t| >= 1, na záznam
```

To rozhoduje mezi dvěma zcela různými světy a nic jiného to nerozhodne:

```
je-li tam MEZERA  (kořeny systematicky daleko od +-1)
    rigidita je strukturní, Q1 má šanci na větu, a T-A na váze 4 je
    kandidát na zákon
je-li tam TĚSNO   (záznamy s kořenem v 1.01 a podobně)
    konce jsou na téže straně jen o vlásek, near-return je koincidence
    škály, a T-A je nejspíš jen vzácnost, ne zákon; pak má smysl hnát
    Phase B jako lov svědka, protože svědek existuje a je jen řídký
```

Existence 0/2 a 2/0 záznamů už teď dokazuje, že kořeny do okna vstupují.
Otázka je jen, jak snadno.

## 5. K identitě větve: konvenci není potřeba vymýšlet

Vlastník správně říká, že determinant určí kořeny, ale identita analytické
větve přes degenerace vyžaduje dodatečnou konvenci, a chce místo toho zapsat
kanonickou posloupnost podepsaných crossingů. Navrhuji to udělat bez jakékoli
konvence a bez pojmu větve:

```
kanonická posloupnost = posloupnost INERCIÍ v otevřených intervalech mezi
po sobě jdoucími kořeny, spočtená exaktní kongruencí v libovolném
racionálním vnitřním bodě každého intervalu
```

Inercie je v každém regulárním bodě definovaná bez volby, celočíselná
kongruence ji dá exaktně, a rozdíl sousedních trojic je právě podepsaný
crossing. Analytická větev se tím nepotřebuje sledovat vůbec, degenerace
nevadí, a výsledek je invariantní vůči přeznačení konců. To je podle mě
přesně ta kanonická posloupnost, kterou vlastník chce.

## 6. Dvě čárky k tabulce

```
1  levá a pravá polovina jsou konvencí sampleru, ne vlastností páru: t=-1
   je K_L a t=+1 je K_R, a která tabulka je která, určuje pinovací
   konvence. Rozdíl 539 proti 529 a 61 proti 55 je proto nutné napřed
   symetrizovat, jinak se z artefaktu stane jev.
2  sudost pencilu je teď doměřená na celém korpusu, 0/5219 nonorbitových a
   78/2874 orbitových, což potvrzuje externí 200bodový test ostřeji a
   uzavírá tu hypotézu definitivně. Menšina sudých mezi orbitovými sedí s
   výkladem, že sudost platí jen pro realizaci prvkem, který tabulku
   fixuje po dvojím použití.
```

T-A zůstává H.
