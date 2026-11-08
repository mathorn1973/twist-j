# Připnuté zdroje

## Veřejný TWIST-J základ

Kontrola provedena 17. října 2026.

- [STATUS.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/STATUS.md): Public Canon v103, ACTIVE.
- [CANON.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md): používané věty jsou jmenovány v README.md a NATIVE_PROOF.md.
- [color-ladder/verify.py](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/reproduce/color-ladder/verify.py): rung 10 obsahuje standardní f,H,T a rozdíl při nesprávně přenesené redukci; rung 11 obsahuje značené S,T, invarianty a ramifikovanou normalizaci.
- [P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/probes/P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1/RESULT.md): veřejný podklad řádu 200.
- [P-U-COUNTER-AMPLITUDE-CLASS-1](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/probes/P-U-COUNTER-AMPLITUDE-CLASS-1/RESULT.md): veřejná klasifikace čtení.
- [reproduce/kernel-connectivity](https://github.com/mathorn1973/twist-j/tree/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/reproduce/kernel-connectivity): již deklarované obousměrné součtové styky.
- [POLICY.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/POLICY.md) a [AGENTS.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/AGENTS.md): pravidla stavu, poznámek, formálních sond a přechodů mezi nosiči.

Normativní základ:

    main / canon-v103: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
    CONTENT_COMMIT: 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66
    CANON_BYTES: 1052518
    CANON_SHA256: d87657aeccc568dd668718fb9cbea6136643e5db32dd4e328e64f824b

Při kontrole měly požadované veřejné běhy úspěšné architektury a souhrnný check:

- [main: 39022927713](https://github.com/mathorn1973/twist-j/actions/runs/39022927713)
- [tag: 39022952253](https://github.com/mathorn1973/twist-j/actions/runs/39022952253)
- [publikace: 39033710211](https://github.com/mathorn1973/twist-j/actions/runs/39033710211)

## Sousední práce na zdrojovém styku

- [PR #1577](https://github.com/mathorn1973/twist-j/pull/1577), při kontrole open, nesloučený, head 9c6a2471b72252d13eb45d4e58c77620ed8dfb92. Původní port nerozlišuje pevné přípravy j a j^-1.
- [Draft PR #1579](https://github.com/mathorn1973/twist-j/pull/1579), při kontrole open, nesloučený, head 03390dca1c0a69ab8989f0daada0810c9956791a. Již deklarovaný kontakt tuto dvojici rozliší a přenese do skutečných placených záznamů. Vlastní text ponechává nativní/ fyzikální připuštění W_b a Ucal a autonomní řízení otevřené.

Tyto PR slouží k vymezení návaznosti a vlastnictví. Nepředstavují novou evidenci pro prostorovou topologii v tomto balíčku.

## Primární matematické zdroje

1. Peter Doyle a Curt McMullen, *Solving the quintic by iteration*, Acta Mathematica 163 (1989), 151–180. [Autorská kopie](https://people.math.harvard.edu/~ctm/papers/home/text/papers/icos/icos.pdf). Standardní icosahedrální formy, jejich kovarianty a Kleinova relace; v tomto balíčku se používá konkrétní normalizace z veřejné reprodukce.

2. John Milnor, *On the 3-dimensional Brieskorn manifolds M(p,q,r)*, v *Knots, Groups, and 3-Manifolds*, Annals of Mathematics Studies 84 (1975), 175–225. [Plný text](https://www.maths.ed.ac.uk/~v1ranick/papers/milnbries.pdf). Linky Brieskornových ploch a jejich cyklická větvená pokrytí nad torusovými uzly.

3. James W. Cannon, William J. Floyd, LeeR Lambert, Walter R. Parry a Jessica S. Purcell, *Bitwist manifolds and two-bridge knots*, Pacific Journal of Mathematics 284 (2016). [Plný text](https://msp.org/pjm/2016/284-1/pjm-v284-n1-p01-p.pdf). Použitý v předchozím pokračování k přesnému rozlišení orbifoldové grupy a grupy pětičetného pokrytí. Nové souřadnicové kontroly na tomto zdroji nezávisejí.

Nová explicitní matice P, její normalizace, označený bod a důsledek bez faktoru 3 jsou odvození této poznámky z uvedených vstupů; nejsou připsány externím článkům.

