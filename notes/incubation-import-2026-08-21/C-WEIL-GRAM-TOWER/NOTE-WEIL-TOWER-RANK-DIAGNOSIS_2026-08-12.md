# NOTE: proč roste jádro Gramovy matice, a co z toho plyne pro prereg

Status: NON-CANONICAL analýza, gates nothing. Reakce na balení noční lane
(branch handoff/weil-tower-recon-20260812, commit fc1f182) a hlavně na
korekci 1 status page: "numericky nulových směrů přibývá s N, 62 ze 168 při
N = 12, rozlišovací schopnost s rostoucím řezem klesá". Datum 2026-08-12.

## 1. Administrativa, aby se neztratila: sigma je UZAVŘENÁ

Status page ji vede jako čekající na definici vlastníka. Není. Definice
byla v twisterovém k6 reportu z 2026-08-11 a v
claude/KONSOLIDACE-VECER_2026-08-11.md, sekce 1, a rozhodnutí je v
claude/REVIEW-NIGHT-ENGINE_2026-08-12.md, sekce 1:

```
sigma_W(z) = sum_r (POS_r - NEG_r) z^r  přes shelly r = 0..6 svědka W
64 sigma_A(1/2) = -64 +192 -240 +144 -44 +4 +1 = -7
64 sigma_B(1/2) = -64 +192 -208 + 96 -28 +4 +1 = -7
```

Oba svědci přesně -7/64, jmenovatel 2^6 je automatický, obsah je sdílený
čitatel -7. Kim-Sarnak sem nepatří. Rozhodčí invariant vs. náhoda je
integer readout 64 sigma_W(1/2) u každého dalšího k6 svědka, patří do
příštího k6 běhu. Položka se z čekacích seznamů může škrtnout.

## 2. V5 splňuje R1, a splňuje ji lépe než jsem žádal

Moje podmínka R1 zněla: doložit, že prvočíselná strana nekonzumuje
orientační volbu generátoru. V5 to dokazuje strukturně, ne jen testem:
koeficient 2 cos(m k theta_p) je SUDÝ v theta, takže záměna generátoru za
konjugovaný je identita na koeficientech (odchylka 3.3e-14 je float, ne
obsah). Konstrukce tedy konzumuje přesně kanonickou neuspořádanou třídu
R(p) z v44 řádku. Zmrazený konec E1 nenastává a je to checkovatelné.
To je uzavřené a dobře udělané.

## 3. Rostoucí jádro NENÍ numerický defekt. Je to tvar Weilovy formy

Diagnóza. Weilova forma na testovacím prostoru je, po rozvinutí,
kvadratická forma v g tvaru

```
W(g * g~) = sum over zeros rho  |g^(rho)|^2      (na kritické přímce)
```

To je součet čtverců přes NULY. Jeho hodnost je proto rovna počtu nul,
které testovací prostor umí ROZLIŠIT, nikoli dimenzi testovacího prostoru.
Jádro je přesně {g : g^ mizí na všech viditelných nulách}. Když se při
pevném cutoffu zvětšuje dimenze testovacího prostoru, přidávají se směry,
které konečně mnoho viditelných nul nemůže oddělit, a jádro roste
NUTNĚ. Pozorování 62 ze 168 tedy není porucha rozlišení; je to čtení
hodnosti: rám vidí zhruba 106 nul.

Tři důsledky, každý ostrý:

```
D1  PSD s velkým jádrem je slabé tvrzení. Informace není ve znaménku,
    je v HODNOSTI a v tom, které nuly forma vidí. "PSD na řezu dimenze
    168 s hodností 106" a "PSD na řezu dimenze 106" je totéž tvrzení.
D2  Lehce záporná minima v blocích zeta a chi_5 jsou očekávaná a
    neškodná: leží v blízkém jádru, kde je pravá hodnota nula nebo
    kladný příspěvek vzdálených nul pod float šumem. Intervalový LDL^T
    tam vrátí NEROZHODNUTO, a to je správná odpověď, ne selhání.
D3  Zvětšovat řez při pevném nosiči je kontraproduktivní: přidává jen
    jádro. Řez a nosič musí růst SPOLU.
```

TESTOVATELNÁ PREDIKCE, na kterou má engine všechno potřebné a je to
minutová kontrola: v každém kanálovém bloku se numerická hodnost rovná
počtu nul té L-funkce v efektivním okně rozlišení, tedy

```
dim(blok) - dim(jádra bloku)  =  #{nuly dané L-funkce ve výšce do T_eff}
```

Nulové výšky pro zeta i pro kanály konduktoru 5 už engine používá při
validaci. Jestli to sedí (a čekám, že ano, s odchylkou nejvýš o jednu
nulu na okraji okna), je degenerace VYSVĚTLENÁ a přestává být hrozbou.
Jestli to nesedí, je uvnitř něco jiného a je lepší to vědět teď.

## 4. Co z toho plyne pro DRAFT-PREREG, tři úpravy

```
U1  DESIGN RULE místo volného zvětšování řezu. Zmrazit podmínku
    dim(V) <= N_zeros(T_eff) s deklarovanou vazbou mezi nosičem
    testovacích funkcí a T_eff. Řez, který ji porušuje, se nezapočítává,
    protože jeho jádro je vyrobené konstrukcí.
U2  READOUT je CERTIFIKOVANÁ HODNOST A INERCIE, ne "PSD". Intervalový
    LDL^T vrací trojici (jistě záporné, nerozhodnuté, jistě kladné).
    Kandidátní tvrzení zní: jistě záporných je nula na věži a nenulově
    mnoho na DH. Nerozhodnutá dimenze se REPORTUJE, netlačí se k nule.
    Tím se konec E4 (znaménko závislé na normalizaci) stává
    kontrolovatelným, protože hodnost je invariant a minimum není.
U3  ŠKÁLOVÁNÍ. Aby bylo minimum vůbec srovnatelné mezi řezy, měřit
    zobecněný problém proti pevné referenční kladné formě (například
    archimedovské části samotné) místo absolutních minim. Absolutní
    minima klesající k nule jsou artefakt normalizace báze, ne signál.
```

## 5. Co tím zůstává v platnosti a co se deflatuje

```
STOJÍ    Separace v jedné konstrukci: nezáporná na věži, silně
         indefinitní na DH, s typově uzavřeným guardem a se smysluplným
         svědkem v plus větvi (-28.5). To je milník noci a nedotčen.
STOJÍ    V5 kanonicita, čtyřstranná validace, oddělení škál obou DH
         větví, odmítnutí citovat -9e6 jako sílu guardu.
DEFLATUJE Formulace "minima klesají exponenciálně k nule, rodina saturuje
         viditelné nuly, přesně struktura kterou GRH predikuje". Podle
         sekce 3 to není saturace nul rodinou, je to saturace HODNOSTI
         formy: přidávané směry nevidí žádné nové nuly. Status page to
         už opatrně říká v korekci 2; tato nota dává mechanismus.
```

Poslední poznámka, procesní: agent status page napsal ostřeji než noční
zprávu a sám si vynutil dvě korekce proti vlastnímu nočnímu textu. To je
přesně chování, které program chce, a stojí za to ho pojmenovat.
