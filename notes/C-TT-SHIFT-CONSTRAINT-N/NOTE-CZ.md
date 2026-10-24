# C-TT-SHIFT-CONSTRAINT-N: co vyšlo, česky pro vlastníka

**NON-CANONICAL. Žádný status, žádné uzavření O/H, žádná změna kánonu.**
Základ v81, `main` 4fe37d3 (po sloučení #908). Prereg zmrazen
(`d38e9fb3…3026`), verifier zmrazen po statickém čtení a `py_compile`, první
běh 18 z 18, obě architektury bajtově shodně. Podrobnosti v README.md a
RESULT.md.

## Co to je

Lineární část tvého přijímacího objektu: jedna společná variační soustava
s lapsem a shiftem na planárním nosiči `Z/5`, přesně kalibračně invariantní
na mřížce, jejíž Noetherovy identity jsou diskrétní Bianchiho identity a
dávají zachování Hamiltonovy i hybnostních vazeb vývojem. Diskrétní
linearizovaná ADM akce, `K_ij = (Delta h_ij - D_i N_j - D_j N_i)/2` na
polovičních řezech, `n` a `h` na celých, jeden antisymetrický operátor
první diference `D`, `L = -D^2`. Kalibrační transformace:

```text
delta h_13 = D xi_1, delta h_23 = D xi_2, delta h_33 = 2 D xi_3,
delta N_i = Delta xi_i + delta_(i,3) D xi_0,
delta n = -(xi_0(n + 1/2) - xi_0(n - 1/2)).
```

Časové umístění není konvence dodaná potom: s `K` a `N` na polovičních
řezech a `n` na celých je to jediné rozložení, při kterém se variace
`K K - K^2` přesně zruší s variací `n R_1`. To odpovídá na tvou otázku po
časovém umístění, v lineárním řádu.

Dvě reprezentace, křížově ověřené: symbolová algebra
`Q[L, D, E, E^-1]/(D^2 + L)` (identity platí pro každý antisymetrický
cirkulant `D`, i iracionální) a explicitní polynomiální akce na
`Z/5 x Z/4` s racionální centrovanou diferencí `D_c` (identity ve všech
200 polních a 80 kalibračních proměnných; Euler-Lagrangeovy polynomy obou
reprezentací se shodují).

## Co je doloženo [candidate-T]

**Přesná kalibrační invariance.** Lineární část: čtyři Noetherovy
kombinace jsou nulový operátor. Kvadratická část: `S(G xi) = 0`. V
explicitním modelu `S(phi + G xi) - S(phi) = 0` jako polynomiální identita.
FA nestřílí.

**Vazby a jejich propagace.** `EL_n = (1/lambda) L tau - rho`
(Hamiltonova), `EL_N1 = (1/lambda) D K_13 + J_1`, `EL_N2` obdobně,
`EL_N3 = -(1/lambda) D Delta tau + J_3` (hybnostní; podélná bez shiftu,
jako ve spojitém `d_3 tau_dot = -lambda J_3`). Noetherovy identity:

```text
xi_0: (E - 1) EL_n = D EL_N3
xi_i: (E^-1 - 1) EL_N_i = D EL_h_i3   (i = 1, 2),   (E^-1 - 1) EL_N3 = 2 D EL_h33
```

Platí-li hybnostní vazby na všech polovičních řezech, je Hamiltonova vazba
konstantní v čase; platí-li vývojové rovnice, jsou hybnostní vazby
konstantní v čase. Vazby uložené na počáteční data se zachovávají. FB
nestřílí.

**Zákony zachování zdroje.** S předepsaným zdrojem je akce invariantní
právě když `(1 - E) rho = D J_3` a `(E^-1 - 1) J_i = D S_i3`. Kovektorové
napětí K1 (`J = 0`, `S_33 = -iota/2`) je porušuje pro každé slovo
(`D iota != 0`, `D` má hodnost 4) a pro šest slov i kontinuitu. To je
strukturální podoba F6 z #909, už nezávislá na testovaném pokračování.
Ale intenzity K1 samy mají zachovávané doplnění: `J_3 = D^-1 (rho_0 -
rho_1)` existuje a má nulový průměr, `S_33` plyne z hybnostního zákona
(slovo `0010`, `D_c`: `J_3 = (1/10, -2/5, 1/10, 1/10, 1/10)`). Příčné
napětí `S_11, S_22, S_12`, to, co zdrojuje `h_+` a `h_x`, se v žádném
planárním zákoně nevyskytuje a je volné. FE nestřílí: měnit se musí podélné
napětí a hybnostní hustota kovektorového modelu, ne slova ani okna K1.

**Svědek a redukce sektorů.** `h_13 = n f(r)` s `N = 0`: všechny rovnice
platí kromě hybnostní vazby `EL_N1`, která padá. S `N_1 = D^-1 f` platí
všechny: je to čistá kalibrace `xi_1 = n D^-1 f`. V kalibraci s nulovým
shiftem je vyloučen. FC nestřílí. V kalibraci `N = 0`, `ell = 0`, vakuum:
vazby `L tau = 0`, `D Delta h_13 = 0`, `D Delta h_23 = 0`, `D Delta tau =
0`; `D` i `L` mají na `Z/5` hodnost 4, takže na nenulových módech `tau = 0`
a `h_13, h_23` jsou v čase konstantní a odstranitelné časově nezávislým
`xi`. Zbývá TT pár s `(Delta^2 + L) h = 0`; čistá TT data s `n = N = tau =
ell = vektor = 0` splňují přesně všechny vazby i vývojové rovnice. FD
nestřílí v lineárním řádu.

**Nulový mód.** `D` i `L` zabíjejí konstanty, `k = 0` složka Hamiltonovy
vazby zní `-rho_hat_0 = 0`; s energií K1 statické ploché řešení není.
Homogenní složka tu není vyřešena, je přesně zaznamenáno, proč ji plochý
podklad neunese. FRW pozadí je příští konstrukce; propagační struktura
výše je to, co musí reprodukovat.

## Přesný fakt o `D` a veřejném stencilu

Pro `D = x(S - S^-1) + y(S^2 - S^-2)` je `-D^2 = 2(x^2 + y^2) - (x^2 +
2xy)(S^2 + S^-2) - (y^2 - 2xy)(S + S^-1)`, takže `-D^2 = L_public` žádá
`x^2 + 2xy = 65/324`, `y^2 - 2xy = 29/324`, tedy `t = y/x` kořen `65 t^2 -
188 t - 29 = 0` s diskriminantem `42884 = 4 . 71 . 151`, což není čtverec.
Žádná racionální antisymetrická první diference na `Z/5` se neumocní na
veřejný stencil; potřebné `D` žije v `Q(sqrt(10721))`, `10721 = 71 . 151 =
53605/5`, tytéž prvočísla jako ve jmenovatelích polí z #909. Racionální
centrovaná diference dává jiný laplacián `L_c` (`1/2` na diagonále,
`-1/4` na posunech `+-2`).

Vidlice pro tebe, tady nerozhodnutá: (alfa) nechat veřejné `L` pro
metrický a TT sektor a přijmout algebraické `D` v sektoru shiftu a
kalibrace, kde nikdy nevstupuje do fyzikálního odečtu; (beta) přijmout
racionální `D` a jeho `L_D` pro celou vázanou soustavu, což posune
propagační operátor TT sektoru mimo registrovaný stencil. Identity výše
platí v obou.

## Co tu není

Druhý řád: TT samozdrojování (`sigma` z #909) potřebuje kubickou mřížkovou
akci s mřížkovou křivostí. Lineární struktura mu ale předem určuje časové
umístění: `K` žije na polovičních řezech, takže Hamiltonova vazba druhého
řádu na řezu `n` ponese členy typu `K(n - 1/2) K(n + 1/2)`, ne
stejnořezové `(Delta h)^2` transkripcí (i)/(ii). Ty zůstávají nerozhodnuté.
FRW pozadí: nulový mód je zablokován, ne vyřešen. 3D nosič a RW koeficient:
neřešeno. Fyzikální význam `tau`, `P_S`, `r_T`: beze změny, otevřeno.

## Účet

```text
FA kalibrační invariance ....... nestřílí
FB propagace vazeb ............. nestřílí
FC svědek ...................... nestřílí (vyloučen hybnostní vazbou; čistá kalibrace)
FD ne-TT radiační sektor ....... nestřílí v lineárním řádu, nenulové módy
FE K1 bez zachovávaného doplnění nestřílí (padá kovektorové napětí, ne K1)

C2 splněno v lineárním řádu, teď i s hybnostními vazbami
C3 splněno v lineárním řádu na nenulových módech, vakuum
C1, C4, C5 beze změny proti #909 (C5: okna K1 nedotčena, padá jen napětí)

Uzavřených O/H: 0.   Posunů statusu: 0.
```

Přijímací objekt jsi definoval jako úplnou kompatibilní konstrukci
počátečních dat a propagace vazeb, nebo přesný protipříklad. Tohle je ta
konstrukce v lineárním řádu na nenulových módech, a přesný záznam
překážky na módu nula. Druhý řád a FRW pozadí jsou další dva kroky, oba
s předem známým časovým umístěním.
