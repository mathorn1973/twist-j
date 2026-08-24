# NOTE: most C_4 rozkladu 1+1+2 na Minkowského 1+3, ověření a zařazení

```text
STATUS   NON-CANONICAL poznámka k vlastníkově syntéze z 2026-08-01.
         Matematické části [T] ověřeny přesnou aritmetikou, jedna
         platforma, 51 kontrol PASS, kandidátní kontrola bez statusu.
         Fyzikální čtení nese [D] a [H] podle řádků níže. Žádný claim,
         žádná preregistrace, lane NEPŘEVZATA, žádná změna Canonu.
BASIS    Public Canon v30 (piny v CENSUS-DMATTER-MANIFEST_v30 a
         SYNTEZA-MISTO-PRULOMU_v30). Interní linie nekonzultována.
VERIF.   claude/verify_c4_minkowski.py
         sha256 4de2f4a2387ee8207a21a1e4e96fcd512201aa4653437ebfb69d6e5cf5e3d7b9
STDOUT   claude/verify_c4_minkowski.stdout.txt (ALL PASS: 51 checks)
         sha256 d0d1e565a51350e3e8bbb2ab96f659c65e107c5c7487f69709ad9acc84fbbcad
```

## Ověřené výroky [T, ověřeno výpočtem, jedna platforma]

```text
V1  Generátor sigma: zeta -> zeta^2 řadí embeddingy do orbity
    a_k = 2^k mod 5 = (1,2,4,3); akce na orbitálních souřadnicích je
    cyklický posun S, S^4 = I.
V2  R[C_4]: S u0 = u0, S u2 = -u2, S uc = us, S us = -uc na bázi
    u0=(1,1,1,1), u2=(1,-1,1,-1), uc=(1,0,-1,0), us=(0,1,0,-1);
    tedy R^4 = <u0> + <u2> + <uc,us>, rozměry 4 = 1 + 1 + 2.
V3  Bit je kvadratický charakter: u2 v orbitálním pořadí = chi5
    (Legendre mod 5) na (1,2,4,3). Tentýž charakter, jehož Gaussova
    suma tau = sqrt5 sedí v ALPHA-PREFACTOR-UNIFICATION [T] a jehož
    L-hodnota dává ln phi (lane eseje a C-SPLIT-UNIT-1).
V4  Gram G_p = p I - 1 1^T na nosiči rozměru p-1 má normalizované
    spektrum {1/p jednou (směr samých jedniček), 1 (p-2)krát},
    přesně pro p v {3, 5, 7, 11, 13} (rozsah ALPHA-SEED).
V5  Afinní zobrazení s 1 -> +1 a 1/5 -> -1 je jednoznačné:
    eta = (5/2) Ghat - (3/2) I = I - (1/2) 1 1^T,
    Spec(eta) = (-1, +1, +1, +1): minus na stopové přímce, plus na
    stopovém jádru. Minkowského signatura z veřejného Gramu jedinou
    afinní renormalizací.
V6  Pauliho tvar: X = [[t+z, x-iy],[x+iy, t-z]] je hermitovský,
    Tr X = 2t, det X = t^2 - x^2 - y^2 - z^2; přesně na 1296
    racionálních čtveřicích.
V7  Census prvočísel p < 100: reálná regulární reprezentace C_(p-1)
    má právě jednu invariantní přímku, právě jeden znaménkový směr a
    (p-3)/2 fázových rovin; (p-3)/2 = 1 právě pro p = 5; ekvivalentně
    hrubé čtení p - 2 = 3 právě pro p = 5. Jemné a hrubé čtení je
    táž věta: 1+1+2 = 1+(1+2) = 1+3.
```

## Co už veřejná linie nese (poznámka nenafukuje novost)

```text
ALPHA-SEED [T]                G = p I - 1 1^T, spektrum {1/p, 1...1},
                              směr jedniček vlastní; vlastníkovo Ghat
                              je jeho 1/p normalizace. Projektový
                              verifier verify_dmatter_direct_1.py totéž
                              spektrum hlídá v bráně C7.
KERNEL-CELL-DICTIONARY [D]    čas je tik hodin; prostor jsou tři F_5
                              směry stopového jádra, izotropní pod
                              Galoisovým Gramem. Hrubé 1+3 už je
                              veřejné slovníkové čtení.
WEINBERG vrstva               B_quark = 1/3 = 1/dim ker(Tr).
COLOR-LADDER-DICTIONARY [D]   su(3) na bezestopých ENDOMORFISMECH
                              stopového jádra.
Sekce 10 CANON.md             grupa generovaná ikosaedrickými rotacemi
                              a J boostem hustá v SO+(3,1), rapidita
                              ln phi; BOOST-READING-SPLIT [T],
                              BOOST-COUNT-LADDER [D].
OBSERVER-ALTERNATOR [D]       mu_4 čtené jako 1+3 proti orbitám 2+2.
Interně                       C-SPLIT-UNIT-1 rev 2 (candidate-T):
                              minimalita a jedinost J ve zmrazené
                              třídě, census bitu a fáze; esej
                              ESEJ-NECO-NIC rev 2 je jeho čtení.
```

## Co je na veřejné linii nové (recon 2026-08-01)

Grep CANON.md, REGISTRY.tsv, CORE.md na minkowski, signature, lorentz,
hermit, pauli: žádný řádek nenese signaturu ani metriku; v22 výslovně
"No end-to-end Lorentz closure is asserted". Interní linie neověřena.

```text
N1  Jemný rozklad 1+1+2 jako registrovatelný výrok (klasická teorie
    reprezentací, [T, literatura]; jako řádek Canonu nový).
N2  Spektrálně afinní most eta = I - (1/2) 1 1^T se Spec (-1,+1,+1,+1)
    nesený veřejným Gramem. Elementární, přesný, veřejně nepřítomný.
N3  Dvojí vynucení p = 5: jeden bit a jedna fáze, respektive jeden čas
    a tři prostorové směry, jsou jemné a hrubé čtení téže věty.
```

## Brzdy, zpřesněné [poctivé meze]

```text
B1  Afinní zobrazení je jednoznačné AŽ PO VOLBĚ cílové dvojice
    (+1, -1). Kanonický [T] obsah je jen spektrální rozštěp
    {1/p} proti {1}. Signatura je čtení, tedy slovníkový řádek [D],
    dokud odvození nepojmenuje, proč vyznačená vlastní přímka bere
    minus. Přesně jeden izolovaný volicí bod: modelový slot programu
    modulů ze SYNTEZA-MISTO-PRULOMU_v30.
B2  Že stopová přímka je čas, je už dnes slovníkové čtení
    (KERNEL-CELL-DICTIONARY), ne odvození. Netvrdit odvozeno.
B3  Čtení bit + fáze -> tři rotační směry přes su(2)/Cartan je [H].
    Kolizní varování: barva su(3) už sedí na bezestopých
    endomorfismech stopového jádra; prostorové so(3) musí být
    samostatný slovníkový řádek, nedědit.
B4  Konvenční slot: S je čtyřcyklus jen v orbitálním pořadí generátoru
    (1,2,4,3). Tvarem jde o read_convention_id datum.
B5  Minkowski je víc než signatura: mísení boosty, invariantní
    rychlost, kauzální kužel. Hustou podgrupu a rapiditu ln phi
    veřejná linie má; most z eta na tuto akci napsán není.
```

## Tvar kandidáta, pokud jej vlastník chce (NEPŘEVZATO)

```text
ID        C-C4-MINKOWSKI-SIGNATURE-1 (id volné na veřejné linii i v
          projektu k 2026-08-01; interní linie neověřena)
CÍL       při promoci veřejná linie: jeden řádek [T] (V1 až V7 jako
          přesné konečné výroky) a jeden řádek [D] (signaturové čtení
          eta s izolovaným volicím bodem pojmenovaným ve scope)
FALZIF.   [T] řádek: aritmetický, kterákoli kontrola V1 až V7 selže
          při nezávislém přepočtu.
          [D] řádek: breaker NONUNIQUE: exhibovat druhou neekvivalentní
          typovanou normalizační cestu z veřejného Gramu na signaturový
          tvar splňující tytéž deklarované podmínky; nález zvyšuje
          počet volicích bodů a řádek to musí říct.
POZN.     Šest polí preregistrace až po převzetí; před zmrazením
          neotvírat data ani výpočty nad rámec této poznámky.
```

Vazba: [[SYNTEZA-MISTO-PRULOMU_v30_2026-08-01]]. Tento most je modelová
instance věty o modulech: kanonický rozštěp [T], jeden pojmenovaný
volicí bod, zbytek vynucen. Ukazuje, že seznam voleb může být krátký a
explicitní.
