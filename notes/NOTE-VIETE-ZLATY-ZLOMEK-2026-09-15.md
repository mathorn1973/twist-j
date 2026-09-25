# Vièteův součin, zlatý řetězový zlomek a dvě poloviny J

```text
STATUS   NON-CANONICAL. Výpočetní poznámka: kde se ve Vièteově součinu pro
         2/pi a ve zlatém řetězovém zlomku objeví polynomy J, a atribuční
         test. Nezakládá claim, nemění registr, frontier, status ani žádnou
         bránu. Není to sonda a není pinovaná. L1 aritmetika, žádný dekodér,
         míra ani fyzikální lift.
BASIS    Public Canon v86 (tag canon-v86, main d008270). Znění řádků
         CM-REAL-DIFFERENT-PRIMARY-SEAM, CM-ALTERNATING-PRIMARY-LATTICE-SEAM
         a J-HARMONIC-SEAM čteno z canon/REGISTRY.tsv na tomto commitu.
OVĚŘENO  16 z 16 kontrol, 12 exaktně (celá čísla, Fraction, Z[phi],
         Q(zeta5)), 4 numericky a označené NUM. Skript
         notes/NOTE-VIETE-ZLATY-ZLOMEK-2026-09-15.check.py, jen standardní
         knihovna, sha256 souboru
           c21282d693e0128177885343381ceba836063ed838b8a6ae64d327727a348c61,
         sha256 stdout
           370db993fd23c2396539d903214863d780f968aa7834f30aadcba823a64ef30f,
         tři běhy s byte-identickým stdout: x86_64 Linux CPython 3.12.3,
         aarch64 Linux CPython 3.12.3, arm64 macOS CPython 3.9.6. Pin před
         prvním spuštěním nebyl, takže je to auditní vstup, ne veřejná
         evidence, a nepovyšuje to nic.
DATUM    2026-09-15
PŮVOD    pracovní relace nad dvojicí vzorců, zlatým řetězovým zlomkem a
         Vièteovým součinem. Navazuje na poznámku o Bauerově řadě v PR #1008,
         ale nezávisí na ní.
```

## 0. Závěr napřed

```text
Vièteův součin je 2/pi zapsané bity. Totéž číslo jde zapsat vyváženými
číslicemi z F_5 a každý faktor je pak průměr pěti fází.

Ten průměr je w^-2 Phi_5(w) = q(|1+w|^2) s q(x) = x^2 - 3x + 1.
Kruhový polynom J stojí v součtu, jeho modulový stín q ve faktoru.

Dva kroky zlatého zlomku jsou matice ((2,1),(1,1)). Na celočíselné
hyperbolické mříži pullbacku J působí přesně tahle matice.
Chyby konvergentů mají čitatele u_n z J-HARMONIC-SEAM.

Kořeny q mají zlatý řetězový zlomek. Tady se oba vzorce potkají.

Zlomek z = 1 + zeta_5^2 J/z má pevné body J a delta = 1 - J
a k delta konverguje po spirále s násobitelem -conj(J).

Číslicový vzorec i spirála platí pro každé liché p, zlatý styčný bod
jen pro p = 5. Charakterizace, ne evidence.
```

## 1. Viète jako bity

Vzorec z obrázku, s n odmocninami v n-tém faktoru,

$$
\frac{2}{\pi}=\prod_{n\ge1}\frac{\sqrt{2+\sqrt{2+\cdots+\sqrt2}}}{2}
$$

je Vièteův součin kosinů cos(π/2ⁿ⁺¹). Každý faktor je průměr dvou fází e^(±iπ/2ⁿ⁺¹), tedy charakteristická funkce jednoho bitu. Náhodné číslo U = Σ εₙ2⁻ⁿ s nezávislými εₙ = ±1 je rovnoměrné na [−1, 1] a střední hodnota e^(iπU/2) je sin(π/2)/(π/2) = 2/π. [T, klasické; N1 na 45 míst]

## 2. Totéž číslicemi z F₅

Stejné rovnoměrné číslo jde zapsat vyváženými pětkovými číslicemi, U = 2 Σ dₙ5⁻ⁿ s nezávislými dₙ ∈ {−2, −1, 0, 1, 2}, tedy s F₅ v symetrickém zápisu. Pak

$$
\frac{2}{\pi}=\prod_{n\ge1}\frac{1}{5}\sum_{d=-2}^{2}e^{i\pi d/5^n}
$$

Chyba klesá zhruba 25krát na číslici. [T; N2 na 45 míst] Totéž platí pro každé liché p s číslicemi |d| ≤ (p − 1)/2, protože součin se teleskopicky složí z podílů sin(py)/(p sin y). [T; N3 pro p = 3 a 7] Registr z N číslic dává algebraické číslo, 2/π vznikne až v limitě.

## 3. Průměr pěti fází jsou polynomy J

Přímým roznásobením

$$
(w+1)^4-3w(w+1)^2+w^2=\Phi_5(w)
$$

Pro |w| = 1 je 2 + w + w̄ = |1 + w|², takže

$$
\sum_{d=-2}^{2}w^d=w^{-2}\,\Phi_5(w)=q\left(|1+w|^2\right),\qquad q(x)=x^2-3x+1
$$

[T, A2] Polynom q je v kánonu dvakrát: jeho kořen u = φ⁻² nese CM-REAL-DIFFERENT-PRIMARY-SEAM a jako hyperbolický faktor stojí v χ_P = (x² − 3x + 1)Φ₁₀(x) v CM-ALTERNATING-PRIMARY-LATTICE-SEAM. Kořeny q jsou |σ_a(J)|² = φ^(∓2). Faktor by vymizel přesně tehdy, kdyby w byla primitivní pátá odmocnina jedné, tedy kdyby 1 + w byl Galoisův konjugát J. Pro w = e^(iπ/5ⁿ) to nenastane. [T]

V reálném tvaru je faktor q(4cos²(π/(2·5ⁿ)))/5 = U₄(cos(π/(2·5ⁿ)))/5. Obecně platí U_{p−1}(c) = m_p(4c²), kde m_p je polynom s kořeny |1 + ζ_p^(2a)|²: m₃ = x − 1, m₅ = q, m₇ = x³ − 5x² + 6x − 1. [T, A1, A2]

## 4. Zlatý zlomek je hyperbolická polovina J

Krok z ↦ 1 + 1/z je matice ((1,1),(1,0)) s determinantem −1. Dva kroky dávají ((2,1),(1,1)) s charakteristickým polynomem q. [T, B1]

Druhá vnější mocnina násobení J na Z[ζ₅] v bázi 1, ζ, ζ², ζ³ má charakteristický polynom (x² − 3x + 1)Φ₁₀(x), ve shodě s řádkem. [T, B2] Celočíselná hyperbolická mříž ker q ∩ Z⁶ má bázi g₁ = e₀₁ + e₀₃ + e₂₃, g₂ = −(e₀₂ + e₁₂ + e₁₃), na které Λ²(M_J) působí přesně maticí ((2,1),(1,1)). V transponovaném tvaru W ↦ M_Jᵀ W M_J z řádku totéž platí s bází k₁ = −(e₀₁ + e₁₂ + e₂₃), k₂ = e₀₁ + e₀₂ − e₀₃ + e₁₂ + e₁₃ + e₂₃. [T, B3] Z[φ] má třídové číslo 1, takže celočíselné matice s charakteristickým polynomem q tvoří jedinou GL₂(Z)-třídu a výsledek na volbě báze nezávisí. [T, klasické] Dva kroky zlatého zlomku jsou tedy doslova pullback J na jeho hyperbolické mříži.

Chyba konvergentu F_{n+1}/F_n je (F_nφ − F_{n+1})/F_n a platí F_nφ − F_{n+1} = −ψⁿ. To je přesně u_n z J-HARMONIC-SEAM. [T, B4] Po každých dvou krocích se u_n zkrátí faktorem ψ² = φ⁻² = |J|².

Kořeny q mají řetězové zlomky φ² = [2; 1, 1, 1, …] a φ⁻² = [0; 2, 1, 1, …], se stejným ocasem jedniček jako φ. [T, B5] Tady se oba vzorce potkají: kořeny pětkového Vièteova multiplikátoru jsou čísla zlatého zlomku.

## 5. Zlomek, který se kroutí

Pro x ∈ μ₁₀ uvažuj zobrazení

$$
z\mapsto 1+\frac{\psi x\,(\psi x-1)}{z}
$$

s pevnými body ψx a A(x) = 1 − ψx, kde A je lineární funkce z J-HARMONIC-SEAM. Pro x = 1 je čitatel ψ(ψ − 1) = 1 a vznikne zlatý zlomek s pevnými body ψ a φ = A(1). Pro x = −ζ₅ je v hlavním vnoření ψ = −(ζ₅ + ζ₅⁴), ψx = J a čitatel J(J − 1) = ζ₅²J:

$$
z\mapsto 1+\frac{\zeta_5^2\,J}{z}
$$

Jeho pevné body jsou J a δ = A(−ζ₅) = 1 − J = −ζ₅². [T, C1, C3]

Pro z ↦ 1 + w/z s pevnými body a, b je násobitel v a roven b/a. Zlatý zlomek má v φ násobitel ψ/φ = −φ⁻²: převrácení a zkrácení, bez rotace. Zkroucený zlomek má v δ násobitel J/δ = −J̄ = e^(3πi/5)·φ⁻¹: otočení o 3π/5 a zkrácení faktorem 1/φ, tedy spirálu. [T, C2] Protože |J| = φ⁻¹ < 1 = |δ|, přitahuje δ. Po Galoisově čtvrtotáčce je |σ₂(J)| = φ a přitahuje naopak σ₂(J). O atraktoru rozhoduje bit, tedy rozdělení {1, 4} proti {2, 3}. [T, C4; C5 numericky]

## 6. Atribuce

- Číslicový vzorec z oddílu 2 a identita w^((p−1)/2)·m_p(2 + w + 1/w) = Φ_p(w) platí pro každé liché p, kontrola A2 pro p = 3 až 13. Pro p = 7 je multiplikátor x³ − 5x² + 6x − 1. Záměnu 5 → 7 to přežije, evidence to tedy není. [T]
- Kořen m_p má periodický řetězový zlomek jen tehdy, když je kvadratický (Lagrange), a m_p je ireducibilní stupně (p − 1)/2 (kontrola D1 pro p = 5 a 7, obecně klasické). Zlatý styčný bod tedy existuje jen pro p = 5. Je to stejná podmínka (p − 1)/2 = 2 jako u minimality, takže jde o charakterizaci, ne evidenci. [T]
- Zkroucený zlomek má torzní pevný bod 1 − J_p = −ζ_p² pro každé p. Který pevný bod přitahuje, závisí na |J_p| ve zvoleném vnoření. Pro p = 7 je v hlavním vnoření |J₇| = 2cos(2π/7) > 1 a přitahuje J₇. [T; C5 numericky]

## 7. Čtení

„Vièteův součin je bitový zápis 2/π, pětkový zápis nese v každém faktoru kruhový polynom J a jeho modulový stín.“ [H]

„Zlatý zlomek je nezkroucený člen rodiny. Zkroucený člen se od něj liší torzí z rozkladu O_K^× = μ₁₀ × ⟨φ⟩ v J-HARMONIC-SEAM.“ [H]

„π je podpis limity“: každý konečný registr číslic dává algebraické číslo. Fakta [T], čtení [H].

## 8. Reprodukce

```sh
python3 notes/NOTE-VIETE-ZLATY-ZLOMEK-2026-09-15.check.py
```

Poslední řádek stdout je `SOUHRN 16/16 PASS`, sha256 celého stdout je v hlavičce. Běh trvá řádově sekundy.
