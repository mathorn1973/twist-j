# Pencil parity: hypotéza vyvrácena, a s ní i rigidita komory

Status: NON-CANONICAL recon, gates nothing. Nabídka do K4 lane. 2026-08-12.
Skript ~/jam/claude_scratch/recon_k4_pencil_parity.py, exaktní celočíselná
aritmetika, Bareiss plus přesná Lagrangeova interpolace, žádný float.

## 0. Dvě opravy vlastníka, obě přijaty

```
O1  „sign-blind null čeká polovinu" NEPLYNE ze slepoty ke znaménku ani
    z podmínění. Musí se explicitně postulovat relative-sign-fair null,
    tedy invariance vůči převrácení právě jednoho konce; swap konců ani
    Delta -> -Delta relativní znaménko nemění. Bez toho postulátu není
    4046.5 kalibrované očekávání. MOJE CHYBA, přijato; číslo se smí
    citovat jen s tím postulátem vysloveným.
O2  moje věta o w2 byla stale. Těch 1512 nebyl úplný census, ale šest
    deterministic-prefix řešení na každý z 252 patternů, s exaktním
    rozpadem 1457 S_4 a 55 nonorbit, a existuje konkrétní nonorbitový
    nonisospektrální w2 pár. Bezpečná formulace: w2 prefix byl silně
    S_4-dominovaný (96.4 %), ve w4 cílové diagonále je S_4 vysvětlení
    menšinové (35.5 %). Kontrast je kvantitativní, ne kvalitativní.
```

## 1. Hypotéza, kterou jsem postavil

Z A = K + K' = 2M a B = Delta definuj celočíselný pencil

```
D(t) = det(A + t B),  stupeň nejvýše 16, střed t = 0, konce t = -+1.
```

Tvrzení, které jsem chtěl ověřit: D je SUDÝ v t. Motivace byla, že kdyby
byl flip realizován permutací P s vlastností, že dvojí použití vrací
tabulku, pak P M P^T = M a P Delta P^T = -Delta, takže D(-t) = D(t)
identicky a rovnost inercie obou konců by byla automatická. Otázka pak
zněla, jestli jsou sudé i nonorbitové páry, tedy jestli je za tím skrytá
involuce.

## 2. Výsledek: NE, a hypotéza padá na obou stranách

200 cílových diagonálních párů, nezávislý sampler, jiný seed než Phase A:

```
orbitové, D sudé          9
orbitové, D LICHÉ        54
nonorbitové, D sudé       0
nonorbitové, D LICHÉ    137
```

Dvě čtení, obě negativní:

```
1  Nonorbitové páry NEJSOU nikdy sudé, 0 ze 137. Skrytá involuce tedy
   mechanismem není. Hypotéza vyvrácena.
2  A moje odvození bylo navíc přestřelené i pro orbitové páry: sudost
   platí jen tehdy, když realizující permutace na TÉ tabulce splňuje
   g^2 . v = v. Pro prvky řádu 3 nebo 4 v S_4 to neplatí, a data to
   ukazují: sudých je jen 9 z 63 orbitových, tedy 14 %. Věta zní
   správně takto: D je sudý právě pro orbitové páry realizované prvkem,
   který danou tabulku fixuje po dvojím použití. To je menšina menšiny.
```

Svědci lichosti jsou robustní, nejsou to zaokrouhlovací drobty:
koeficienty u t^1 a t^3 řádu 10^16.

Vedlejší nezávislé potvrzení Phase A: v mém vzorku je 137 ze 200
nonorbitových, tedy 68.5 %, proti jejich 64.49 % na 8093 párech. Jiný
sampler, jiný seed, tentýž řád. Headline poměr Phase A tím není jen
vlastní měření.

## 3. A z midpoint dat plyne, že padá i druhé vysvětlení

Vlastníkův exaktní midpoint census dává 354 midpointů (8,0,8) při koncích
(7,0,9) a 61 midpointů (10,0,6) při koncích (9,0,7). V obou případech se
n_+ mění 9 -> 8 -> 9, respektive 7 -> 6 -> 7. Všechny midpointy jsou
regulární, takže to nejsou dotyky, jsou to průchody.

```
DŮSLEDEK  nejméně 415 z 8093 tětiv PROKAZATELNĚ opouští komoru konce a
          vrací se do ní. Rigidita komory tedy také není mechanismem.
```

Takže obě jednoduchá vysvětlení jsou mrtvá: ani symetrie pencilu, ani
setrvání v jedné inerciální komoře.

## 4. Co tím zbývá, přesně

Invariantem není spektrum, není to symetrie a není to komora. Je to NÁVRAT:

```
OTÁZKA  proč se počet průchodů nulou na (-1, 0) rovná počtu na (0, 1)
        pro každý fiber pár, když pencil není symetrický?
```

Tím se vlastníkův navržený krok stává správným a můj test ho nenahrazuje,
nýbrž ho odblokoval: exaktní počet kořenů D na obou polovinách zvlášť teď
měří jedinou přeživší formulaci. Doplnil bych k němu tři readouty, které
nic nestojí navíc, protože kořeny se stejně počítají:

```
R1  rozdělení počtu kořenů na každé polovině. Nula na obou znamená
    lokální rigiditu tam, kde midpoint souhlasí; nenulové rovné počty
    jsou ten návrat v čisté podobě.
R2  párování průchodů podle vlastního čísla: je to táž větev, která
    odejde a vrátí se, nebo jiná? To rozliší lokální jev od globálního
    a je to přesně to, co by strukturní důkaz musel řídit.
R3  korelace lichosti pencilu s asymetrií stran. Kladná strana drží
    profil středu na 99.72 %, záporná jen na 68.71 %; stojí za to
    vědět, jestli se liší i velikostí lichých koeficientů, protože ta
    asymetrie je zatím jediné vodítko, které rozlišuje obě strany.
```

## 5. Poctivá bilance tohoto kola

```
vyvráceno mnou    sudost pencilu jako mechanismus (0 ze 137 nonorbitových)
vyvráceno daty    rigidita komory (415 doložených návratů)
opraveno vlastníkem  kalibrace sign-blind nullu, stale w2 věta
opraveno mnou     vlastní odvození sudosti platí jen pro involutivní
                  realizaci, ne pro orbitové páry obecně
potvrzeno         nonorbitový podíl Phase A nezávislým samplerem
zbývá             návrat průchodů, měřitelný přesně tím, co vlastník
                  navrhl, a teď bez konkurenčních hypotéz
```

T-A zůstává H. Nic z toho ji nefalsifikovalo ani nedokázalo.
