# PROP-2 konsolidovaně: opravy přijaty, PROP-2C ověřeno, PROP-2D nově

Status: candidate-T support, NON-CANONICAL, no authority. 2026-08-12.
Nahrazuje claude/PROOF-PROP-2-RAPIDITY-TORSION-NOGO_2026-08-11.md jako
pracovní text; starý dokument se NEMAŽE, zůstává jako záznam stavu před
recenzí. Autorská stopa: PROP-2 navrhla PUBLIC recenze meditace, PROP-2b
přidala tato session, PROP-2C přidala nezávislá noční recenzní session
(breaker_prop2_torsion_nogo.py, sha 853d6a38, 52878 testů, 0 protipříkladů),
PROP-2D přidává tato session níže.

## 0. Tři opravy recenze, všechny PŘIJATY

```
C3-NORM     PŘIJATO, byla to skutečná chyba mého dokumentu. Setting line
            psala |w|_1 = sqrt(p) e^t, což je split specializace. C3
            (nulovou třídu obývají VŠECHNA inertní prvočísla a ramifikované
            místo) je pravdivé jen v normové normalizaci. Opraveno v sekci 1
            na |w|_1 = N(P)^(1/2) e^t. Pod tou normalizací inertní P = (p)
            má |p|_1 = p = N(P)^(1/2), ramifikované P = (sqrt5) má
            |sqrt5|_1 = sqrt5 = N(P)^(1/2), obojí t = 0 přesně.
LEMMA-E     PŘIJATO jako zjednodušení. F je totálně reálné, takže place 1
            je INJEKTIVNÍ vnoření tělesa do R: z |u|_1 = 1 plyne
            sigma_1(u) = +-1 = sigma_1(+-1), tedy u = +-1 přímo. Hypotézy
            |u|_1 = |u|_2 a N(u) = +1 sloužily jen k odvození |u|_1 = 1.
            Důsledek, který recenze správně vidí: v PROP-1 A1 odpadá celá
            větvová analýza ab = 0. Lemma 1 (racionální čtverce v F) zůstává,
            A2 ho potřebuje.
PROP-2b     PŘIJATO jako oprava formulace, ne důkazu. "with any orientations"
            zve případ Q = sigma(P) nad TÝMŽ p, kde je (iii) nepravdivé
            identitou (r(sigma P) = -r(P)). Důkaz je v pořádku, používá
            p != q. Závěr se od teď nese na neuspořádané třídě.
```

## 1. Opravené znění

Setting. F = Q(sqrt5), O = Z[phi], sigma netriviální automorfismus,
O^x = {+-phi^m}, N(phi) = -1, h = 1. Pro prvoideál P s generátorem w
definuje rapiditu t vztah |w|_1 = N(P)^(1/2) e^t; r(P) = t mod (log phi)Z,
R(p) = {t, -t} neuspořádaná třída. Inertní a ramifikované P sedí v t = 0.

LEMMA E (jednomístná forma). u v F s |u|_1 = 1 je +-1; je-li navíc obraz
v place 1 kladný, u = +1. Důkaz: place 1 je injektivní vnoření F do R.

PROP-2 (torzní no-go). r(P) má nekonečný řád pro každý split prvoideál.
PROP-2b (izogenní stabilita), OPRAVENÝ ZÁVĚR: pro každé m >= 1 je zobrazení
p -> m R(p) = {m t, -m t} injektivní na split racionálních prvočíslech a
nikdy nerovno nulové třídě.

## 2. PROP-2C, druhé čtení této session: DRŽÍ

Znění. Pro po dvou různá split p_1..p_k a P_i nad p_i jsou reálná čísla
t_1, .., t_k, log phi lineárně nezávislá nad Q.

Ověřil jsem každý krok samostatně, ne jen přečetl:

```
1  |sigma(pi)|_1 = |pi|_2, protože netriviální automorfismus reálného
   kvadratického tělesa PROHAZUJE obě reálná místa. Odtud
   log|pi_i|_1 - log|sigma pi_i|_1 = 2 t_i: normové poloviny se ruší.
   Platí i pro N(pi) = -p, absolutní hodnoty znaménko nevidí.       OK
2  log|u|_1 = 2(sum m_i t_i - n log phi) = 0, tedy |u|_1 = 1 a u = +-1
   jednomístnou Lemma E.                                            OK
3  (u) = (1), (phi) = (1), takže prod P_i^(m_i) sigma(P_i)^(-m_i) = (1)
   ve VOLNÉ abelovské grupě zlomkových ideálů. Záporné exponenty jsou
   tam legální, na argumentu nic nemění.                            OK
4  Těch 2k prvoideálů je po dvou různých: P_i != sigma(P_i) ze splitu,
   a nad různými p_i nemůže být společný ideál (různá charakteristika
   reziduálního tělesa). Jednoznačnost rozkladu nuluje VŠECHNY
   exponenty, pak 0 = n log phi a n = 0.                            OK
5  Q-relace se vynásobením jmenovatelů převede na Z-relaci; obě verze
   jsou totéž tvrzení.                                              OK
```

Navíc jedna vlastnost, kterou recenze neuvádí a která se hodí: tvrzení je
NEZÁVISLÉ NA ORIENTACI. Volba sigma(P_i) místo P_i mění znaménko t_i, a
lineární nezávislost je vůči záměně znamének invariantní. PROP-2C tedy
nepotřebuje kanonickou sekci, stejně jako PROP-2b.

Novost: recenze poctivě říká, že to není nová matematika, je to injektivita
logaritmického vnoření na grupě generované split prvočísly a fundamentální
jednotkou. Souhlas. Cena je v tom, že je to elementární, bez analýzy, bez
floatu, a uvnitř programu.

Statut: PROP-2C má teď dvě čtení (autor a toto). Třetí, od jiného autora,
zůstává otevřenou položkou přesně jak recenze žádá.

## 3. PROP-2D: efektivní separace. Nový příspěvek této session

Pozorování, které PROP-2C otevírá. Pro split P je

```
2 t_p = log |beta_p|_1,   beta_p = pi / sigma(pi),   N(beta_p) = 1,
```

takže KAŽDÁ veličina v PROP-2C je logaritmus ALGEBRAICKÉHO čísla:
2 t_i = log|beta_i| a log phi je logaritmus jednotky. Zkoumaný výraz

```
Lambda = sum_i m_i log|beta_i| - 2n log phi
```

je tedy celočíselná lineární forma v logaritmech algebraických čísel.
PROP-2C říká: Lambda = 0 jen triviálně. Bakerova věta (Baker, Wustholz)
říká víc, a přesně to, co program potřebuje:

```
PROP-2D [candidate-T, podmíněno klasickou větou, bez výpočtu]
Existuje efektivně vyčíslitelná konstanta C, závislá jen na k, na stupni
tělesa a na výškách beta_1..beta_k a phi, tak že pro každý netriviální
celočíselný vektor (m, n) s B = max(|m_i|, |n|) platí
     |Lambda|  >  exp(-C log B).
```

Důsledek, který upgraduje C6 z kvalitativního na kvantitativní:

```
C6+  INTERVALOVÝ ROZVRH JE EXPLICITNÍ. Aby se oddělily třídy m R(p) od
     m R(q) pro všechna m <= M a všechna split p, q <= X, stačí počítat
     rapidity s přesností exp(-C(X) log M), tedy s počtem platných míst
     POLYNOMIÁLNÍM v log M. Není to jen "vždy lze zjemnit"; je to
     "tolik zjemnění stačí a víc není třeba".
```

To je přesně ten typ tvrzení, který chybí každé numerické konstrukci: ne
"kolize nenastane", ale "kolize nenastane a tady je modul". Pro DRAFT
prereg Gramova testu to znamená, že fázová část nosiče má certifikovaný
rozvrh přesnosti, ne jen naději na zjemnění.

Poctivě: konstanta C z Bakerovy věty je notoricky velká a tohle tvrzení
neděla nic praktického snadným; dělá ho ROZHODNUTELNÝM. A je to citace
klasické věty, ne nová matematika. Ověření, že hypotézy sedí (algebraická
čísla, nenulová forma z PROP-2C, celočíselné koeficienty), je celý obsah.

## 4. Důsledky, aktualizovaný seznam

```
C1  chi_k(P) není nikdy kořen jednoty pro k != 0. Účetnictví: řád M a
    index k se skládají jako m = M |k| >= 1. Stojí.
C2  Žádný pevný konečný fázový model nezachová separaci. Dvě půlky jsou
    různého druhu a zůstávají oddělené: kvocienty konečnou podgrupou jsou
    přesně m-škálování a padají na PROP-2b; libovolné zaokrouhlení do
    konečné množiny koliduje přihrádkovým principem a je deklarovaná
    ztráta. Stojí.
C3  Nulovou třídu obývají všechna inertní prvočísla a ramifikované místo;
    pětka je výjimečná ramifikací, ne samotou. Stojí V NORMOVÉ
    NORMALIZACI, viz oprava C3-NORM.
C4  Ekvidistribuce, ne jen nekolize. Weylovo kritérium na PROP-2C:
    posloupnost m -> (m t_1, .., m t_k) mod log phi je ekvidistribuovaná
    v k-toru. Ověřeno: <h, alpha> s alpha_i = t_i/log phi je iracionální
    pro každý nenulový celočíselný h, jinak by b sum h_i t_i = a log phi
    byla netriviální Q-relace. [candidate-T, podmíněno PROP-2C]
C5  Split třídy generují volnou abelovskou podgrupu nekonečné hodnosti.
C6  Intervalová cesta zesílena na libovolné konečné lineární testy.
C6+ a explicitní rozvrh přesnosti, PROP-2D.
```

## 5. Otevřené, beze změny

```
1  Třetí čtení PROP-2C od dalšího autora.
2  První nezávislé čtení PROP-2D (napsáno dnes, nula pokusů o rozbití).
3  Nic z toho neotevírá Gramův test. Žádný prereg bez explicitního ANO.
4  Toto je pracovní text, ne fold. Nic nepovyšuje.
```
