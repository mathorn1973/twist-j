# Relativní kontakt: úplný důkaz dvou chronologických překážek

**C-U-RELATIVE-CONTACT-CHRONOLOGY-N — NON-CANONICAL, candidate-T, L1.**

Analytický důkaz; nový vědecký program nebyl spuštěn. Veřejný základ, původní výsledky a jejich autorita jsou uvedeny v [SOURCES.md](SOURCES.md); přesný rozsah kontroly v [REVIEW.md](REVIEW.md) a [VALIDATION.md](VALIDATION.md).

## 1. Původ vazby a rozsah výsledku

Rodina C_κ(x,y,a)=(x,y+κ(x−a),a), κ∈F₅, je již podmíněně klasifikována v [issue 990](https://github.com/mathorn1973/twist-j/issues/990#issuecomment-5654429916). Její odvození předpokládá afinní tvar, kovarianci vůči posunutí přijímače, nulový signál při x=a a zachování příslušné relativní vnější formy. Jednotková odezva vybírá κ=1 až jako další podmínka. Tato poznámka nepřipisuje původní klasifikaci sobě a fyzikálně nevybírá hodnotu κ.

Zde C=C₁. Dokazujeme selhání dvou přesně zadaných rozkladů při skutečných vložených nativních ticích: čtyři případy jedné mezery a všech šestnáct časových kontextů pětitaktu. Na skutečně připraveném nulovém vstupu dáváme navíc invariant, který vylučuje nápravu libovolně dlouhým čistě nativním čekáním. Tvrzení se týká těchto rozkladů, nikoli všech možných kontaktů. [IMPLICATIONS.md](IMPLICATIONS.md) obsahuje také kladný podmíněný dvoutakt.

## 2. Přesná buněčná dynamika

Veškerá následující buněčná aritmetika probíhá v F₅. Buňku zapisujeme v=(p₁,p₄,p₁′,p₄′,q,r) a její stopu z jako součet šesti souřadnic modulo 5. Symbol a se podle argumentu používá buď pro referenční buňku, nebo pro první generátor; C vždy přijímá tři buňky v pořadí zdroj, přijímač, reference.

```text
a(v) = (p₄, p₁, p₄′, p₁′, q, r)
b(v) = (−p₁′, −p₄′, −p₁, −p₄, −q, −r)
c(v) = (2−p₁′, 1−p₄′+r, 2−p₁, 1−p₄−r, 1−q, −r)
d(v) = (2−p₁, 1−p₄, 3−p₁′, 4−p₄′, 1−q, 1−r)
e(v) = (2−p₁, 1−p₄, 3−p₁′, 4−p₄′, 2−q, 1−r)
```

Řídicí bit je skutečný θₙ=popcount(n) mod 2. Mapa fₜ zvolí generátor s indexem z+2t mod 5 v pořadí a,b,c,d,e. Dₙ označuje souběžné působení f_(θₙ) na všechny tři buňky.

Stopové mapy mají v pořadí vstupů z=0,1,2,3,4 přesné tabulky:

```text
τ₀ = (0,4,0,4,4)
τ₁ = (2,1,1,3,1)
```

Posuzujeme připravenou vrstvu v čase n≥3, na níž všechny tři buňky mají stopu sₙ=4−3θ_(n−1). Zbytek každé buňky je volný. Označení Hₛ znamená celou afinní nadrovinu z=s; Hₛ³ má patnáct volných souřadnic.

### Připravená vrstva je úplný obraz původního nosiče

Každý z pěti uvedených generátorů je afinní involuce na V=F₅⁶. Jeho stopa je ±z plus konstanta. Na jednotlivé vrstvě H_s proto vybraný generátor dává bijekci na H_{τ_t(s)}. Samotná mapa f_t na sjednocení vrstev obecně bijektivní není: odlišné vstupní vrstvy mohou přejít na tutéž výstupní.

Skutečné první tři bity jsou 011. Množiny dosažených stop se tedy mění přesně takto:

```text
{0,1,2,3,4} --τ₀--> {0,4} --τ₁--> {1,2} --τ₁--> {1}.
```

Každý dílčí obraz je celá příslušná vrstva, takže obraz celého V po třech skutečných krocích je přesně H₁. Pro s∈{1,4} platí τ_t(s)=4−3t. Indukcí je v každém čase n≥3 úplný obraz přesně H_{s_n}. Pro tři nezávisle zvolené počáteční buňky pod stejnými hodinami je obraz přesně H_{s_n}³.

To opravňuje univerzální tvrzení na celé patnáctirozměrné afinní vrstvě. Jde o matematickou dosažitelnost z úplného původního nosiče; fyzická možnost připravit libovolný jeho stav tím odvozena není.

Kompatibilita hotové vazby C je přesná. Na společné stopě všechny buňky volí stejný afinní generátor g(v)=Lv+b a platí g(y+x−a)=g(y)+g(x)−g(a). Proto C Dₙ=Dₙ C na příslušné připravené vrstvě. Tato rovnost však neříká, že můžeme jednotlivé sčítací podkroky přesouvat přes nativní tik.

## 3. Jedna vložená mezera

Nechť P přičte zdroj k přijímači a Q odečte aktuální referenci. Pro zadaný bit t označme Δₜ=fₜ×fₜ×fₜ. Bez vloženého tiku je QP=C. Při chronologii Q Δₜ P má přijímač po P stopu 2s a reference stopu s. Koncová přijímačová stopa je proto τₜ(2s)−τₜ(s), zatímco ideál Δₜ C má stopu τₜ(s).

| Společná stopa s | Bit t | Ideální stopa | Stopová hodnota po rozkladu | Rozdíl modulo 5 |
|---|---|---|---|---|
| 1 | 0 | 4 | 1 | 2 |
| 1 | 1 | 1 | 0 | 4 |
| 4 | 0 | 4 | 0 | 1 |
| 4 | 1 | 1 | 2 | 1 |

Rozklad se tedy neshoduje s požadovanou mapou pro žádnou z těchto čtyř dvojic a pro žádnou volbu zbývajících vstupních souřadnic.

Stopové mapy nejsou invertibilní. Pouhý rozdíl stop by ještě nevylučoval pozdější synchronizaci. Tu pro konkrétní nulový vstup vyloučí invariant odvozený níže.

## 4. Úplný pětitaktový zákon

Druhá zkoušená cesta používá pouze kladné přičítání: jednou zdroj a čtyřikrát referenci, protože 4a=−a v F₅. Mezi každými dvěma podbranami ale skutečně uběhne nativní čas, a reference se tím mění.

Explicitně přidaný řadič j má pět hodnot. Celý testovaný krok je:

```text
Q₀(x,y,a) = (x,y+x,a)
Qⱼ(x,y,a) = (x,y+a,a)       pro j=1,2,3,4

W(n,x,y,a,j) = (n+1, Dₙ Qⱼ(x,y,a), j+1 mod 5)
```

Od j=0 porovnáváme W⁵ s ideálem C D_(n+4) D_(n+3) D_(n+2) D_(n+1) Dₙ. V obou popisech jsou na konci n+5 a j=0. Během všech podkroků se nativně vyvíjí také zdroj a reference. Řadič a přičítací podbrány jsou přiznané předpoklady této zkoušené implementace.

Šestibitový kontext je slovo u₀…u₅=θ_(n−1)…θ_(n+4). Položme s(u)=4−3u a δ=z_přijímače−s(u). Při jednom přičtení a nativním tiku t je:

```text
δ' = τₜ(δ+2s(u)) − s(t)
```

Ze startu δ=0 zůstává δ v množině {0,1,2}. Pro vstupní pořadí δ=0,1,2 jsou přechody a přijímačová písmena:

| Dvojice předchozího a současného bitu | Tři výstupy δ′ | Tři vybraná písmena |
|---|---|---|
| 00 | 0,0,1 | d,e,a |
| 01 | 2,0,1 | a,b,c |
| 10 | 1,0,0 | c,d,e |
| 11 | 0,2,0 | e,a,b |

Tato stopová tabulka je stejná pro přičtení zdroje i reference, protože oba dárci mají v daném čase stejnou stopu.

## 5. Všech šestnáct skutečných kontextů

Thueova–Morseova posloupnost je fixním bodem substituce μ(0)=01, μ(1)=10. Každý její šestibitový faktor se vejde do dvou sousedních osmibitových bloků μ³(a)μ³(b). Čtyři možná bloková slova jsou:

```text
μ³(00) = 0110100101101001
μ³(01) = 0110100110010110
μ³(10) = 1001011001101001
μ³(11) = 1001011010010110
```

Oba osmibitové bloky obsahují všechny čtyři sousední dvojice 00,01,10,11. Každá dvojice se proto v posloupnosti vyskytuje libovolně pozdě a každý faktor následující tabulky skutečně nastává i pro n≥3. Tabulka není výběrem z konečně dlouhého prefixu.

| Kontext | Přijímačová písmena | Koncové δ | Důvod nerovnosti celé mapy |
|---|---|---|---|
| 001011 | daeab | 0 | Koeficient referenčního r je 0 místo 1 |
| 001100 | dabce | 0 | Koeficient přijímačového r je +1 místo −1 |
| 001101 | dabcb | 0 | Koeficient přijímačového r je +1 místo −1 |
| 010010 | aedae | 0 | Koeficient referenčního r je 2 místo 1 |
| 010011 | aedab | 0 | Koeficient referenčního r je 2 místo 1 |
| 010110 | aeabc | 1 | Rozdílná koncová stopa |
| 011001 | abcea | 2 | Rozdílná koncová stopa |
| 011010 | abcbc | 1 | Rozdílná koncová stopa |
| 100101 | ceaea | 2 | Rozdílná koncová stopa |
| 100110 | ceabc | 1 | Rozdílná koncová stopa |
| 101001 | cbcea | 2 | Rozdílná koncová stopa |
| 101100 | cbece | 0 | Zbytkový lineární člen +2E |
| 101101 | cbecb | 0 | Zbytkový lineární člen −2E |
| 110010 | eceae | 0 | Koeficient přijímačového r je +1 místo −1 |
| 110011 | eceab | 0 | Koeficient přijímačového r je +1 místo −1 |
| 110100 | ecbce | 0 | Zbytkový lineární člen +2E |

Je to úplné rozdělení 6+4+3+3. Ve všech šestnácti případech se liší zákony na celém Hₛ³. V šesti stopových případech se liší každý vstup. V ostatních deseti se netvrdí, že neexistuje jednotlivý vstup se shodným výsledkem.

## 6. Koeficientový důkaz zbývajících deseti případů

Připravené zdrojové a referenční buňky volí pouze b,d,e. Každý z těchto generátorů neguje lineární část souřadnice r, takže po pěti ticích má ideální přijímač koeficient −1 u vstupního r_y a +1 u vstupního r_a.

Ve čtyřech uvedených přijímačových slovech se jednou vyskytuje a, které r neneguje, a čtyřikrát jiný generátor. Výsledný koeficient r_y je tedy +1. V dalších třech případech se sečtou čtyři příspěvky postupně přidávané reference. Označíme-li ρᵢ znaménko přijímačového r v i-tém písmenu, je koeficient r_a roven součtu pro i=1,…,4 z výrazu (ρ₄…ρᵢ)(−1)ⁱ. Dává 0,2,2 v pořadí daeab,aedae,aedab.

Poslední tři případy rozhodne pístový člen. Nechť B zaměňuje první a třetí, druhou a čtvrtou souřadnici a ponechá q,r. Položme v=(0,1,0,−1,0,0), E=v e_rᵀ. Platí:

```text
L_b = −B
L_c = −B+E
L_d = L_e = −Id

B² = Id,   BE = −E,   EB = E,   E² = 0
```

Ideální lineární část po pěti skutečných ticích je A₅=−B^(u₀ xor u₅), protože výměna nastává právě při změně sousedních bitů.

Chronologická slova cbece a ecbce mají přijímačovou lineární část L_c L_b L_c=−B+2E. Slovo cbecb má část −(L_b L_c)²=−Id−2E. Rozdíly vůči A₅ jsou tedy přesně +2E,−2E,+2E.

Tyto rozdíly nejsou jen rozdíly mimo přípustnou vrstvu. Směr w=(0,0,0,0,−1,1) má nulovou stopu, patří tedy do tečného prostoru Hₛ, a E w=v≠0. Stejný směr dovoluje měnit r při pevné stopě i v předchozích koeficientových případech.

Pro úplnou konstrukci map lze zapsat nativní prefix Hᵢ(v)=Aᵢv+bᵢ, přijímačová písmena Rᵢv+tᵢ a rekurzi Y₀=y, Y_(i+1)=Rᵢ(Yᵢ+Zᵢ)+tᵢ, kde Z₀=x a Zᵢ=Hᵢ(a) pro i=1,…,4. Tím vzniká afinní mapa patnácti volných vstupních souřadnic. Výše uvedené nenulové koeficienty samy postačují k důkazu nerovnosti, bez enumerace 5¹⁵ vstupů.

## 7. Skutečně připravený nulový vstup

Pro všechny tři buňky zvolme v čase 0 stejný stav w=(2,1,3,4,0,1). Skutečné první bity θ₀θ₁θ₂=011 vyberou generátory b,b,d a provedou:

```text
(2,1,3,4,0,1)
  → (2,1,3,4,0,4)
  → (2,1,3,4,0,1)
  → e_q = (0,0,0,0,1,0)
```

V čase n=3 tedy skutečně nastane x=y=a=e_q. Není nutné předpokládat nedoložené vložení buňky do pozdějšího času. Relativní signál x−a je nulový, takže C na tomto trojstavu působí jako identita.

Pro pětitakt odpovídá časový kontext slovu 101001. Následují tyto úplné stavy:

| Čas po podkroku | Přijímač při pěti přičteních | Zdroj a reference při nativním vývoji |
|---|---|---|
| 4 | (2,1,2,1,4,0) | (0,0,0,0,4,0) |
| 5 | (3,4,3,4,2,0) | (0,0,0,0,1,0) |
| 6 | (4,2,4,2,3,0) | (0,0,0,0,4,0) |
| 7 | (3,4,4,2,0,1) | (2,1,3,4,3,1) |
| 8 | (0,0,1,2,3,2) | (2,1,3,4,2,4) |

Ideální přijímač v čase 8 je (2,1,3,4,2,4). Skutečný je (0,0,1,2,3,2).

Protože x=a během každého mezikroku, je na tomto vstupu každé přičtení zdroje stejné jako přičtení reference. Stejný chybný konec proto dostaneme pro všech pět možných umístění jediného zdrojového přičtení. Ani volba tohoto umístění podle stavu by na tomto svědku nepomohla.

Pro chronologii s jednou mezerou už první tik dává:

```text
P:        y = 2e_q
D₃:       y = (2,1,2,1,4,0),  a = (0,0,0,0,4,0)
Q:        y = (2,1,2,1,0,0)

Ideál D₃ C: y = (0,0,0,0,4,0)
```

Zápis D₃ zde znamená skutečný nativní krok v čase 3; používá bit θ₃=0.

## 8. Proč žádné další čekání nepomůže

Definujme z a S jako součet všech šesti, respektive prvních čtyř souřadnic. Dále:

```text
A(v) = S(v) − 1_[z(v)=0]
I(v) = A(v)² mod 5
```

Z přímých generátorových vzorců plyne:

| Generátor | S po kroku | z po kroku |
|---|---|---|
| a | S | z |
| b | −S | −z |
| c | 1−S | 2−z |
| d | −S | 2−z |
| e | −S | 3−z |

Po skutečném výběru generátoru jde o následujících deset úplných algebraických případů:

| Řídicí bit t | Vstupní z | Generátor | Výstupní z | Přesná identita |
|---|---|---|---|---|
| 0 | 0 | a | 0 | A′=A |
| 0 | 1 | b | 4 | A′=−A |
| 0 | 2 | c | 0 | A′=−A |
| 0 | 3 | d | 4 | A′=−A |
| 0 | 4 | e | 4 | A′=−A |
| 1 | 0 | c | 2 | A′=−A |
| 1 | 1 | d | 1 | A′=−A |
| 1 | 2 | e | 1 | A′=−A |
| 1 | 3 | a | 3 | A′=A |
| 1 | 4 | b | 1 | A′=−A |

Proto I(f₀(v))=I(f₁(v))=I(v) pro každou buňku, včetně stavů mimo synchronizovanou vrstvu.

| Konec příslušné chronologie | Čas | Přijímač | I |
|---|---|---|---|
| Ideál po jednom tiku | 4 | (0,0,0,0,4,0) | 0 |
| Jedna mezera | 4 | (2,1,2,1,0,0) | 1 |
| Ideál po pěti ticích | 8 | (2,1,3,4,2,4) | 0 |
| Pět kladných podbran | 8 | (0,0,1,2,3,2) | 4 |

Hodnoty 0,1,4 jsou všechny možné čtverce v F₅. Každé další čistě nativní pokračování zachová příslušnou hodnotu. Ani libovolně dlouhé čekání, ani rozdílné délky či rozdílné řídicí bity na porovnávaných stranách proto nemohou sjednotit konce s různými I.

Tento důkaz se vztahuje na libovolnou délku čekání. Nepotřebuje konečnou simulaci. I je zde přesný rozlišující invariant nad F₅; není tím identifikována fyzikální energie.

## 9. Přesná hranice závěru

Nerovnost na jednom nulovém vstupu stačí k vyvrácení rovnosti obou úplných zákonů na deklarovaném oboru. Trvalost svědka se týká pouze dalšího působení vybraných f₀,f₁. Libovolná nová interakce, jiný rozklad, příprava jiného nosiče nebo změna pozorování tím vyloučeny nejsou.

Pro pozorování R je postačující podmínkou přetrvávajícího rozlišení existence funkce h s I=h∘R na posuzovaném oboru. Jestliže R hodnotu I zahodí, tento invariant sám nerozhoduje o shodě čtení. Takové zahození ještě nedokazuje správné budoucí pozorování ani jeho slučitelnost s dalšími kontakty.

Rozšíření o pomocné buňky, přesný kladný dvoutakt zachovávající společnou stopu a důsledky pro výběr zákona jsou dokázány v [IMPLICATIONS.md](IMPLICATIONS.md). Identita I není ztotožněna s fyzikální energií, entropií ani kontaktním štítkem jiné vrstvy.

Autor: A. M. Thorn. Původní text a důkaz: Apache-2.0. Asistentský přezkum je přiznán samostatně.
