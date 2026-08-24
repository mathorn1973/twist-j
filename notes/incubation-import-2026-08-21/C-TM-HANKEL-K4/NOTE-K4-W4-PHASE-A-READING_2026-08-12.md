# Čtení Phase A: symetrie padla jako vysvětlení, a co z toho plyne

Status: NON-CANONICAL analýza, gates nothing. Reakce na zapečetěnou Phase A
(400 000 pokusů, 366 665 platných fiber párů, 0 opačných; manifest
db7f8258, aggregate df84731f). 2026-08-12.

## 1. Hlavní výsledek NENÍ nula

Nula opačných párů je slabší zpráva než se zdá, a agent to sám správně
říká: 71.28 očekávaných při nezávislosti není kalibrovaná p-hodnota,
protože konce fiber páru nezávislé nejsou. Celý smysl měření je, že jsou
silně závislé, takže srovnání s nezávislostí jen opakuje, co už víme.

Hlavní výsledek je tenhle:

```
cílové diagonální páry             8 093
z toho genuinně nonorbitové        5 219   (64.49 %)
vysvětlené S_4                     2 874   (35.51 %)
```

Symetrie tedy NENÍ vysvětlení diagonální koncentrace na váze 4. Na váze 2
byla (všech 1512 párů je S_4 obraz), na váze 4 je menšinová. Známý w4
nonorbitový pár není výjimka, patří do hojné třídy o pěti tisících členech.
Tím padá nejpřirozenější hypotéza, že w4 je jen w2 znovu, a otázka se stává
skutečně novou.

## 2. Správný null není nezávislost, je to slepost ke znaménku

Nabízím kalibrovatelnou formulaci místo té popisné. Mechanismus, ať je
jakýkoli, prokazatelně sváže konce. Otázka nezní, jestli je vazba silná,
ale jestli je ORIENTOVANÁ. Podmiňme tedy tím, co je pozorováno:

```
páry, kde jsou OBA konce v cílovém stratu     8 093
z toho zarovnané (stejný profil)              8 093
z toho protilehlé (zrcadlový profil)              0
```

Null hypotéza „mechanismus váže velikost signatury, ale je slepý k jejímu
znaménku" předpovídá zhruba polovinu protilehlých, tedy řádově 4 000.
Pozorováno nula. To je odmítnutí s odstupem, který se nedá vysvětlit
vzorkovací mírou, protože podmiňujeme na pozorované závislosti a nepoužíváme
marginály. Tvrzení, které tím vzniká: mechanismus není jen zachovávající
velikost, je ZACHOVÁVAJÍCÍ ZNAMÉNKO.

Podmíněné readouty, které to nesou (a jsou robustní vůči zbylé asymetrii
4.20:1):

```
konec (7,0,9), partner (7,0,9)     13 352 ze 14 808   =  90.2 %
konec (9,0,7), partner (9,0,7)      2 834 ze  3 530   =  80.3 %
konec vzácný, partner zrcadlový                    0
```

## 3. Exaktní strukturní důsledek, který z Phase A plyne a nikdo ho nevyslovil

Dvě už dokázané věci se skládají:

```
(a) K je AFINNÍ ve znaménkovém vektoru, takže K' = K + Delta a Delta je
    mask-only                                    (recon z 2026-08-12)
(b) rovnost F_109 vynucuje Tr K' = Tr K a Tr K'^2 = Tr K^2
                                                 (K4 lane, dokázáno)
```

Z (b) první moment: Tr(Delta) = 0. Z (b) druhý moment, s Tr(K Delta) =
Tr(Delta K) pro symetrické matice: 2 Tr(K Delta) + Tr(Delta^2) = 0, tedy

```
Tr(K Delta) = -Tr(Delta^2)/2   je KONSTANTNÍ na celé fiber varietě,
                               závisí jen na masce, ne na v
```

a pro střed M = K + Delta/2 okamžitě

```
Tr(M Delta) = 0.
```

Ověřeno exaktně: Tr(Delta) = 0 na všech 29 478 weight-4 signed skeletonech
a na všech 252 weight-2 patternech, a obě identity na 40 vzorkovaných
skutečných fiber řešeních, bez jediné výjimky.

DŮSLEDEK, který mění tvar úlohy: každý fiber pár je SYMETRICKÁ DVOJICE

```
K = M - Delta/2,      K' = M + Delta/2,      Tr(M Delta) = 0,
```

tedy dva body ve stejné vzdálenosti na obě strany od středu, který je
trace-ortogonální ke směru přehození.

## 4. Proč je to zajímavé, a co přesně je teď záhada

V symetrickém obrázku je záměna Delta za -Delta přesně záměnou konců. Kdyby
signatura reagovala na poruchu ±Delta/2 LICHÝM způsobem, což je generický
případ (první řád poruchy vlastního čísla je lichý v poruše), pak by konce
šly na opačné strany a protilehlé páry by byly HOJNÉ, ne nulové. Data říkají
opak: odezva je SUDÁ. Ať se profil od středu pohne kamkoli, pohne se stejně
na obě strany.

To je ostrá formulace toho, co se má dokázat:

```
OTÁZKA  proč je odezva signatury na +-Delta/2 kolem trace-ortogonálního
        středu SUDÁ, když generický první řád je lichý?
```

Odpověď musí zabít první řád. Trace-ortogonalita Tr(M Delta) = 0 je jedna
lineární podmínka a sama o sobě jednotlivé první řády nenuluje, takže to
ještě není důkaz; je to přesně místo, kde má důkaz stát. Kandidáti, které
bych zkoumal v tomto pořadí: chová se párování u_i^T Delta u_i na těch
vlastních vektorech M, které jsou blízko nuly, jako sudé kvůli další
struktuře fiber rovnic; nebo má M na fiber varietě vynucený jádrový směr,
který dělá z prvního řádu degenerovaný případ.

## 5. Doporučení: přestat vzorkovat, jít do algebry

Phase A využila zhruba čtvrthodinu z plánovaného rozpočtu a Phase B se
správně nespustila. Můj názor na to, co dál:

```
1  Další uniformní vzorkování NEMÁ cenu. Podmíněná statistika je 8 093 ku
   nule; desetinásobek dá 80 000 ku nule a kvalitativně nezmění nic. Za
   svědkem se dál nehoní, když jich 366 tisíc pokusů nenašlo ani jeden a
   mechanismus je mezitím pojmenovaný.
2  Phase B ANO, ale s jiným účelem, než měla. Ne lov svědka, ale SBĚR
   KORPUSU: podmíněné vzorkování vzácného strata, aby vznikla knihovna
   řádově 10^5 nonorbitových diagonálních párů. Ta knihovna je vstup pro
   strukturní analýzu ze sekce 4, ne statistika.
3  Nejlevnější další měření, hodina práce a rozhodne hodně: na
   nonorbitových diagonálních párech spočítat inercii STŘEDU M a rozdělení
   nejmenších vlastních čísel M. Jestli M sedí systematicky na vzácném
   stratu nebo systematicky na (8,0,8), je to přímé vodítko k tomu, jestli
   je odezva sudá kvůli degeneraci prvního řádu.
4  T-A držet jako H, ne jako skoro-dokázanou. Phase A ji nefalsifikovala
   ani nedokázala a to je ta správná věta.
```

## 6. Co Phase A NEDOKÁZALA, aby to nikdo necitoval špatně

```
- neexistenci opačných párů v celé fiber populaci; 3/N je rule-of-three
  proxy na vzorkovací míře, ne interval na populaci
- nic o vahách nad 4
- nic o tom, že by diagonální koncentrace byla úplná; 90.2 % a 80.3 %
  znamená, že vzácný konec si asi v desetině případů vezme partnera
  (8,0,8), takže mechanismus nedrží profil, drží jen znaménko
```

Ta poslední čárka je vlastně další argument pro sekci 2: kdyby mechanismus
držel profil, nebyly by smíšené páry se středem. On drží stranu.
