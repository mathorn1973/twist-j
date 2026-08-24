# Tenkost krát zarovnání: exaktní rozklad z dat, která už existují

Status: NON-CANONICAL analýza, gates nothing. 2026-08-12.
Anglická verze je v handoff repu jako
`NOTE-K4-ALIGNMENT-FACTORIZATION_2026-08-12.md`, commit 01f5a1d,
sha256 6d544c5d4accc1eb8ae1e7a0881e3f7575e55ff28917fc2b79d2164b233cb7c1.

**Sekce 4 je SUPERSEDED sekcí 7 a zůstává nezměněná.** Observable `g = m/d`
je exaktní sekanta, ne lokální sklon, za jaký jsem ji vydával.

Veřejná báze při psaní: Public Canon v45, ACTIVE, tag `canon-v45`, content
commit `cbd248274d67a861611787ba6e7be3e6a13b29f1`, `canon/CANON.md` sha256
`f3f8954bda620836e604d08d9088587ea84429ecdadfc27737e83b0f8031128b`,
214608 bytů, `canon/SHA256SUMS` 5 z 5 OK. Nic zde není canon.

## 1. Dvě opravy, obě přijaty

```
O1  „lichý rank vylučuje bezkořenovost" bylo přestřelené. Platí jen
    deg <= rank(Delta), s rovností právě když je A|ker(Delta)
    nedegenerované, a pokles stupně může změnit paritu. Teorém je tedy
    o SKUTEČNÉM lichém stupni, ne o ranku: 485 ze 496 má lichý stupeň a
    tam je reálný kořen věta, 11 má sudý stupeň a tam je to empirie.
O2  side-conditioned křivky nejsou doslova monotónní a skok pooled sazby
    11 -> 12 není jen kompozice: 4.77 bodu zevnitř stran, 2.57 z jejich
    zastoupení.
```

## 2. N2 přežila, ale je to lokalizace, ne mechanismus

Spektrální tenkost minusových středů drží na absolutní i scale-free škále,
přežívá při identickém Delta a není artefaktem měřítka: minusová A mají
naopak VĚTŠÍ ||A||_inf (297.21 proti 243.31).

## 3. N1: není to posun, je to SMĚS

```
50 párů s minusovým crossingem   plus stěna dál 50 z 50, medián d+/d- = 8.215
96 párů s oběma kořeny vně       dominance 50 ku 46, medián poměru 1.034
 1 minusový pencil               bez konečného reálného kořene
```

## 4. Návrh rozkladu, SUPERSEDED sekcí 7, ponecháno nezměněné

```
lambda(t) = lambda_0 + t (u^T Delta u) + O(t^2)
g = |lambda_min(A)| / |t*|
```

s kontrolou `g <= ||Delta||_2`. Obojí je v sekci 7 opraveno.

## 5. a 6. Otázky Q1, Q2 a stav v původním znění

Q1 stranová neutralita `g`; Q2 co odlišuje 50 hlubokých párů od 96
symetrických při identickém Delta. Q2 byla zodpovězena, viz sekce 7.

## 7. REV 2: observable byla špatná a měření rozhodlo

### 7.1 Oprava

`g = m/d` je exaktní **sekanta**, ne derivace. Míchá lokální sklon se vším
nelineárním mezi 0 a `t*`. Správný lokální faktor je

```
q = u^T Delta u = -P_t(lambda_0, 0) / P_x(lambda_0, 0)
tau_FO = m / |q|
```

Dvě věci v sekci 4 byly moje a byly špatně. Za prvé tvrzení, že `g` je jako
číslo exaktní a první řád je „jen jeho čtení": formálně pravdivé, věcně
vyhýbavé, slovo exaktní tam dělalo práci, kterou si nezasloužilo. Za druhé
kontrola `g <= ||Delta||_2` screenovala špatný objekt, ta mez platí pro
derivaci, ne pro sekantu. Exterior stratum to ukazuje na jednom řádku:
`g+/g- = 1.731` míří opačně než `|q+|/|q-| = 0.5135`.

### 7.2 Měření, 147 kanonických fixed-Delta párů, as reported

```
stratum              m+/m-   |q+|/|q-|   tau+/tau-   g+/g-    d+/d-
50 minus-cross       4.660      0.1141       39.93   0.4688   8.296
96 oba exterior      1.941      0.5135        4.535  1.731    1.0385

hluboké stratum, per pár
  plusový střed dál od singularity     44 z 50
  minusový lokální sklon větší         45 z 50
  m- asi 4.66x menší, |q-| asi 8.76x větší, oba efekty stejným směrem

absolutní mediány    m+ = 0.1793     m- = 0.04662
                     |q+| = 0.00999  |q-| = 0.10617
po ||Delta||_2       0.0012006  proti  0.0097846
```

Jednofaktorová lokalizace je mrtvá. Minusová strana je současně tenčí v `M`
a silněji lokálně zarovnaná s pevným `Delta`.

### 7.3 Dvě kontroly, obě prošly, zapsané ať se tabulka nečte jako spor

```
C1  mediány poměrů nekomponují. (m+/m-)/(d+/d-) = 0.562 proti g+/g- = 0.4688
    a (m+/m-)(|q-|/|q+|) = 40.84 proti tau+/tau- = 39.93. Není to spor,
    medián součinu není součin mediánů.
C2  normalizace q pomocí ||Delta||_2 je uvnitř páru TAUTOLOGIE, Delta je tam
    identické a poměr se nezmění. Informativní je pro poolované mediány,
    pro párové tvrzení nenese váhu. Párový faktor 8.76 je normalizačně
    invariantní z konstrukce a je silnější.
```

### 7.4 Nelinearita je kompenzační kanál, ne reziduum

```
                první řád   realizované   kompenzace
hluboké             39.93         8.296        4.813
exterior             4.535        1.0385       4.367
```

Ta dvě čísla jsou blízko. Kdyby to přežilo pořádné měření, celý rozdíl mezi
straty sedí v prvním řádu a nelineární korekce je stratum-nezávislý
multiplikátor, což je jednodušší popis než tři volné souřadnice. VÝHRADA je
stejná jako v sekci 4: obě čísla jsou odvozena z poměrů mediánů, které
nekomponují, takže je to hypotéza, ne měření. Rozhodující levný test je
per-pár veličina `log(d+/tau+) - log(d-/tau-)` a otázka, zda obě strata
sdílejí polohu.

### 7.5 Čtyři záznamy s q identicky nula: navržený exaktní mechanismus

`8458-`, `35887+`, `35887-`, `50274+` mají `P_t(x,0) = 0` identicky, tedy
`q = 0` na všech midpointových větvích, přesto konečné kořeny, pencil přesně
sudý, nejbližší kořeny `+-d`.

MECHANISMUS. Existuje ortogonální involuce `S`, `S = S^T`, `S^2 = I`, s

```
S A S = A          a          S Delta S = -Delta
```

```
determinant   det(A + t Delta) = det(S(A + t Delta)S) = det(A - t Delta),
              pencil je přesně sudý a kořeny chodí v +-d
sklon         S komutuje s A, midpointová spektra jsou jednoduchá, takže
              každý vlastní vektor je automaticky vlastním vektorem S,
              Su = eps u, a pak
                  q = u^T Delta u = -(Su)^T Delta (Su) = -eps^2 u^T Delta u,
              tedy q = 0 na KAŽDÉ větvi
```

Druhé tvrzení je ostře silnější než sudost determinantu a přesně to bylo
pozorováno. Přirozený kandidát na `S` v tomto substrátu je maska sama, celá
lane stojí na dvojici `v` a `v xor m`.

FALZIFIKÁTOR, konečné exaktní hledání: pro každý ze čtyř záznamů hledej `S`
v signované symetrické grupě substrátu. Pokud pro některý `S` neexistuje a
determinant je přesto přesně sudý, má sudost jinou příčinu a tohle padá.
Obrácená implikace neplatí automaticky, takže test není prázdný.

`35887` je tam z OBOU stran. To ukazuje na vlastnost dvojice skeleton a
maska, ne strany.

Pro tyto čtyři je správný lokální faktor druhého řádu:

```
q2 = sum_{k != 0} |u_k^T Delta u_0|^2 / (lambda_0 - lambda_k)
tau_SO = sqrt(m / |q2|)
```

### 7.6 Otevřené je exterior stratum, ne to hluboké

Vyrušit asymetrii prvního řádu `4.535` na `1.0385` napříč 96 páry není šum.
Nejlevnější vysvětlení nepotřebuje sumační pravidlo: pokud `d` realizuje jiná
větev než ta u nuly, je `tau` špatný prediktor a `d` určuje větev se
stranově neutrální statistikou. Napojuje se to přímo na reportovaných 22 ze
146 konečných minusových záznamů s certifikovaným branch mismatchem.

TEST. Identifikuj větev, která realizuje `d`, a zkontroluj, zda **její**
`(m_k, q_k)` predikuje `d` a zda je stranově neutrální.

### 7.7 Stav

Minimální poctivý popis má tři souřadnice: tenkost `m`, lokální zarovnání
`q`, nelineární reziduum `log(d/tau)`. Sekce 7.4 až 7.6 jsou tři pokusy
stlačit to zpátky ke dvěma, každý s vlastním testem a vlastním způsobem,
jak selhat. V hlubokém stratu je minusový crossing blízko prvnímu řádu a
plusová stěna silně nelineární, medián `tau/d` asi `8.94` plus proti `1.43`
minus pro shodnou nenulovou větev. `T-A` zůstává `H`.
