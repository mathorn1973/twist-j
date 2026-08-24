# PROP-2 rodina, revize 2: po druhém a třetím čtení

Status: candidate-T support, NON-CANONICAL, no authority. 2026-08-12.
Nahrazuje claude/PROOF-PROP-2-CONSOLIDATED_2026-08-12.md; předchozí verze se
nemaže. Vstupy: druhé čtení (osmisekční, s rozborem C6+) a třetí čtení
(public-native, ověřilo v44 základ nezávisle). Obě PASS na jádru, obě našly
skutečné defekty v mém PROP-2D a C6+. Všechny přijaty.

## 0. Přijaté opravy, itemizovaně

```
R2-1  C3-NORM formulace: nulovou rapiditní TŘÍDU mají inertní a
      ramifikovaný prvoideál; t = 0 doslova má jen privilegovaný
      generátor (racionální p, respektive sqrt5). Po násobení phi^a je
      t = a log phi, táž třída. PŘIJATO.
R2-2  PROP-2C: doplnit explicitní definici u do textu. PŘIJATO, viz níže.
R2-3  PROP-2b psát jako KOROLÁR PROP-2C, ne samostatným větvením.
      PŘIJATO, stará větvová argumentace se ruší jako nadbytečná.
R2-4  PROP-2D: B' = max(3, |m_i|, 2|n|), protože koeficient u log phi je
      -2n. PŘIJATO.
R2-5  PROP-2D: exp(-C log(eB')), NE exp(-C log B). Při B = 1 by pravá
      strana byla 1, což není platná dolní mez. MOJE CHYBA, PŘIJATO.
R2-6  PROP-2D: konstanta závisí na A_i majorizujících výšku I velikost
      zvoleného logaritmu, ne jen na výškách. PŘIJATO.
R2-7  C6+ NEUZAVŘENO: chybí redukce generátorů (výšky), mez na n,
      koeficientové zesílení intervalové chyby a omezení "lineárně v
      log M při pevném X". PŘIJATO CELÉ, viz sekce 4 a 5.
R2-8  "víc není třeba" je nárok na optimalitu, který Baker nedává.
      MOJE CHYBA, PŘIJATO, věta škrtnuta.
R2-9  C2: T/T[m] je zase kružnice, konečné je jen jádro. PŘIJATO.
R2-10 C4 přejmenovat: je to ekvidistribuce NÁSOBKŮ pevné konečné sady,
      ne prvočísel při p -> nekonečno. PŘIJATO.
R3-1  PROP-2C má public-native důkaz přímo přes v44 řádek
      SPLIT-PRIME-RAPIDITY-CLASS, bez Lemma E a bez otázky normalizace.
      PŘIJATO A ADOPTOVÁNO jako primární důkaz.
R3-2  C6 v původním znění je příliš silné: kvalitativní nekolize nedává
      rychlost ani "žádný rozvrh nemůže být poražen". PŘIJATO, zúženo.
R3-3  C5: R(p) žije modulo znaménko, což není grupa. Grupová formulace
      až po volbě orientace. PŘIJATO.
R3-4  Breaker: konečný výpočet nedokládá globální class number one,
      dokládá principálnost testovaných ideálů. PŘIJATO jako oprava
      popisu běhu.
R3-5  C3-NORM ven z jakékoli veřejné verze: v44 už nulový kanál
      formuluje přes rho. Zůstává jako interní poznámka. PŘIJATO.
```

## 1. PROP-2C, public-native důkaz (adoptován z třetího čtení)

Pro po dvou různá split p_1..p_k, prvoideály P_i = (pi_i) a orientované
třídy r_i platí: z sum m_i r_i = 0 v R/(log phi)Z plyne m_i = 0 pro
všechna i. Ekvivalentně jsou t_1..t_k, log phi lineárně nezávislé nad Q.

Důkaz. Polož x = prod pi_i^(m_i). Veřejná věta SPLIT-PRIME-RAPIDITY-CLASS
[T, v44] dává bezlogaritmický ekvivalent [eta(x)] = 0 <=> rho(x) = +-phi^(2n).
Na hlavních ideálech tedy, protože phi je jednotka,

```
(rho(x)) = prod_i P_i^(m_i) sigma(P_i)^(-m_i) = (1).
```

Těch 2k prvoideálů P_i, sigma(P_i) je po dvou různých (split dává
P_i != sigma(P_i), různá reziduální charakteristika odděluje indexy).
Jednoznačnost rozkladu zlomkových ideálů nuluje všechny exponenty. qed

Verze s reálnými zdvihy: Q-relaci vynásob společným jmenovatelem a reduguj
modulo log phi. Orientace nehraje roli, záměna P_i za sigma(P_i) mění
znaménko t_i a lineární nezávislost je vůči tomu invariantní.

Starý důkaz přes u = phi^(-2n) prod (pi_i/sigma pi_i)^(m_i) a Lemma E je
správný a zůstává jako záložní čtení; explicitní definice u je tímto
doplněna (R2-2).

## 2. PROP-2 a PROP-2b jako koroláry

```
PROP-2   k = 1. Konečný řád m dává m t = n log phi, netriviální relace,
         spor s PROP-2C.
PROP-2b  m R(p) = m R(q) pro p != q dává m t_p -+ m t_q - n log phi = 0,
         netriviální relace ve třech členech, spor s PROP-2C. Nulová
         třída je vyloučena přímo PROP-2.
```

Kratší než původní argumentace a bez větvení. Ruší se stará verze
PROP-2b(ii)/(iii) s multimnožinovými rozbory.

## 3. PROP-2D, opravené znění

Redukovaní reprezentanti podle sekce 4. Polož alpha_i = eps_i pi_i/sigma(pi_i)
se znaménkem eps_i tak, aby sigma_1(alpha_i) > 0; pak log sigma_1(alpha_i) = 2 t_i.

```
Lambda = sum_i m_i log sigma_1(alpha_i) - 2 n log phi
B'     = max(3, |m_1|, .., |m_k|, 2|n|)
```

PROP-2C dává Lambda != 0 pro každý netriviální celočíselný vektor. Explicitní
věta o lineárních formách v logaritmech (Matvejev; Baker a Wustholz) pak dává
efektivně vyčíslitelnou C_* závislou na k, na stupni a na veličinách A_j,
které majorizují SOUČASNĚ absolutní logaritmickou výšku, velikost zvoleného
logaritmu a pevnou kladnou konstantu, takovou že

```
|Lambda| > exp(-C_* log(e B')).
```

Tvar log(e B') je nutný: při B' = 1 by exp(-C log B') = 1 nebyla dolní mez.

## 4. LEMMA H, doplněné výškové lemma (příspěvek této session)

Druhé čtení správně identifikuje díru: nahrazení pi -> phi^a pi mění
beta = pi/sigma(pi) o faktor (-1)^a phi^(2a), takže VÝŠKA roste s |a|, zatímco
rapiditní třída se nemění. Bez kanonické redukce tedy žádná jednotná C(X)
neexistuje. Druhé čtení navrhuje redukci a poznamenává, že výšková věta typu
h <= log p + O(1) "je přirozená, ale v textu není". Doplňuji ji, a vychází
přesně, bez O(1).

```
REDUKCE   Pro každý split prvoideál zvol generátor s t v (-L/2, L/2),
          L = log phi. Hranice nemůže nastat: 2 t = +-L znamená
          2 r(P) = 0, dvojtorzi, vyloučenou PROP-2. Redukce je tím
          jednoznačná až na znaménko a konjugaci.

LEMMA H   Pro takto redukovaný generátor pi split prvoideálu nad p:
              h(pi) = (1/2) log p   PŘESNĚ,
          a tedy h(alpha_p) <= 2 h(pi) = log p.
DŮKAZ     pi je algebraické celé číslo stupně 2, vedoucí koeficient 1.
          Konjugáty mají |pi|_1 = sqrt(p) e^t, |pi|_2 = sqrt(p) e^(-t) s
          |t| < L/2, takže oba jsou > 1 pro každé split p (nejmenší je
          11, a už sqrt(2) phi^(-1/2) > 1). Proto
          h(pi) = (1/2)[log(sqrt p e^t) + log(sqrt p e^(-t))] = (1/2) log p.
          Pro alpha = +- pi/sigma(pi): h(alpha) <= h(pi) + h(sigma pi)
          a výška je invariantní vůči konjugaci.
KONTROLA  Ověřeno pro 15 split prvočísel od 11 do 149: h(pi) souhlasí s
          (1/2) log p na plnou přesnost a oba konjugáty jsou v absolutní
          hodnotě > 1. Readout, ne důkaz; důkaz je výše.
```

Druhý zisk redukce, který stojí za vyslovení: |log sigma_1(alpha_p)| = |2 t_p|
< L = log phi, tedy VELIKOST logaritmu je omezená univerzální konstantou,
nikoli rostoucí s p. Právě to je druhá půlka veličiny A_j z R2-6.

DŮSLEDEK, EXPLICITNÍ ZÁVISLOST NA X. Pro p_i <= X je A_i majorizováno
řádově log X (výšková část dominuje, logaritmická část je O(1)), a pro phi je
A_(k+1) = O(1). Matvejevovský tvar pak dává

```
C_X  =  O( (log X)^k ),  s efektivně vyčíslitelnou konstantou.
```

Pro párový test C6+ je k = 2, tedy C_X = O((log X)^2). Tím padá i poznámka
třetího čtení, že se o závislosti na X nic netvrdí: tvrdit se dá, a je
polynomiální. Konstantu zde nepočítám.

## 5. C6+ uzavřené znění

```
C6+ [candidate-T, důsledek PROP-2C, PROP-2D a LEMMA H]
Zafixuj X. Pro každé split p <= X vezmi redukovaného reprezentanta
t_p v (-L/2, L/2) a jeho kladný avatar alpha_p. Existuje efektivně
vyčíslitelná C_X = O((log X)^2) taková, že pro každá dvě různá split
p, q <= X, každé 1 <= m <= M, OBĚ ZNAMÉNKA a každé celé n platí
      |m (t_p +- t_q) - n L|  >  (1/2) exp(-C_X log(2 e M)).
Rozsah n: po redukci je |t_p +- t_q| < L, takže pro m <= M stačí
|n| <= M a tedy B' <= 2M.
Intervalové šířky: jsou-li vstupy t_p, t_q, L známy s šířkou nejvýše
eta, chyba lineární formy je nejvýše řádu 3 M eta, takže k
certifikovanému rozhodnutí stačí
      eta  <  (1/(12 M)) exp(-C_X log(2 e M)).
Počet bitů je tedy O((log X)^2 log M): při pevném X lineární v log M.
NEDĚLÁ SE žádné tvrzení o optimalitě této přesnosti ani o tom, že
menší by nestačila.
```

Poslední věta nahrazuje moje původní "tolik zjemnění stačí a víc není
třeba" (R2-8). Baker dává postačitelnost, nikoli minimalitu.

## 6. Důsledky, opravený seznam

```
C1  chi_k(P) nikdy kořen jednoty pro k != 0. DRŽÍ.
C2  Žádný pevný konečný fázový model nezachová separaci. DRŽÍ, s
    hranicí: T/T[m] je zase kružnice, konečné je jen jádro; m-škálování
    padá na PROP-2b, zobrazení do konečné množiny koliduje přihrádkovým
    principem a je deklarovaná ztráta.
C3  Inertní prvoideály a ramifikovaný mají rapiditní TŘÍDU nula;
    privilegovaní generátoři mají t = 0 doslova. Interní poznámka, do
    veřejné verze nepatří: v44 to už říká přes rho.
C4  KRONECKER-MULTIPLE-EQUIDISTRIBUTION (přejmenováno z "ekvidistribuce"):
    posloupnost m -> (m t_1/L, .., m t_k/L) mod 1 je ekvidistribuovaná
    v k-toru. Je to ekvidistribuce NÁSOBKŮ pevné konečné sady rapidit.
    NENÍ to tvrzení o rozdělení prvočísel při p -> nekonečno; to je
    Heckeho ekvidistribuce, jiná věta, a v poznámkách této session se
    obojí nesmí slít do jedné věty.
C5  Po volbě jedné orientace nad každým split p tvoří třídy r(P) volnou
    abelovskou podgrupu nekonečné hodnosti v R/(log phi)Z; změna
    orientace nahrazuje generátory jejich zápory, takže podgrupa na
    orientaci nezávisí. R(p) samo žije modulo znaménko a grupou není.
C6  ZÚŽENO: pro každý PEVNÝ konečný soubor racionálních lineárních
    porovnání lze certifikované intervaly zjemnit tak, aby každou
    netriviální kombinaci oddělily od nuly. Žádná jednotná mez ani
    rychlost z toho neplyne; ty dodává až C6+.
C6+ viz sekce 5.
```

## 7. Otevřené

```
1  PROP-2C má tři čtení a public-native důkaz. Připraveno pro veřejný
   probe pod jménem SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T], s C4 a C5
   jako přesnými koroláry (návrh třetího čtení, souhlas).
2  LEMMA H a explicitní C_X = O((log X)^k) jsou napsány dnes a mají nula
   nezávislých čtení.
3  Popis breakeru opravit: doložena je principálnost testovaných ideálů
   a nalezení generátorů, ne globální class number one.
4  Nic z toho neotevírá Gramův test. Žádný prereg bez ANO.
```
