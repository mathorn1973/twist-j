# Algebraický kontakt: veřejný přezkumný návrh

**NON-CANONICAL, L1, candidate-T. Stav: přezkumné notes; piny dosud nepřijaty, veřejný běh NOT RUN.**

Pro navrhovanou samostatnou sondu `P-ALG-CONTACT-REALIZATION-1` je v [issue #1386](https://github.com/mathorn1973/twist-j/issues/1386) rezervován název a vlastník, pojmenovaná relace `v100-algebra-review-20261006`. Veřejná větev této předlohy je `codex/alg-contact-realization-review-1`. Tato rezervace ani zveřejnění notes nejsou přijatým frozen probe, souhlasem ke spuštění, veřejným výsledkem ani začleněním v100. Zvolená cesta veřejného přezkumu je organizačním postupem této práce; sama nevytváří novou univerzální povinnost repozitáře.

- [SPEC.md](SPEC.md) obsahuje celý matematický návrh Pi_alg a přesně fixovaného kompilátoru CW-ALG-1, včetně úplného q liftu, inverze a dosažitelné domény.
- [PREREG-DRAFT.md](PREREG-DRAFT.md) je návrh omezené kontroly a architekturního kontraktu před přijetím pinů. Neobsahuje oprávnění k běhu.
- [SOURCE_PROVENANCE.json](SOURCE_PROVENANCE.json) zachovává SHA-256 původních podkladů. Nejde o přijaté zmrazení této sondy.

Aktuální obsahový SHA-256 SPEC.md (pro kontrolu přezkoumávaného obsahu, nikoli přijatý veřejný pin):

```text
bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656
```

Před každým veřejným během se postupuje podle tehdy aktuálního repozitáře. Po přijetí pinů se zmrazené vstupy nemění, nerebasují, neamendují, nepřepisují force-pushem ani znovu nepoužívají pro upravenou sondu; případná náprava se řídí aktuální politikou dispozice a nástupce.

`P-CONTACT-RECORD-1` zůstává samostatnou sondou v původním rozsahu. Nová spojovací věta pro V=A_y T_alg A_x a společné začlenění v100 jsou následné, odděleně přezkoumávané kroky. Starší místní reporty zůstaly beze změny. Při přípravě tohoto balíku nebyl spuštěn verifier, veřejná sonda ani obrovská expanze T_alg.

## Konkrétní kód doplněný do této předlohy

[verify.py](verify.py) a [compiler_identity_checks.py](compiler_identity_checks.py)
jsou konkrétní implementace navrženého omezeného auditu. [CHECK-MAP.md](CHECK-MAP.md)
mapuje funkce, přesné konečné množiny, symbolické identity a obecné důkazní
závislosti. Jde o doplnění existujícího PR #1389, nikoli další definici CW-ALG-1.
SPEC.md i původní PREREG-DRAFT.md zůstávají bajtově nezměněny.

Kód je předložen k přijetí. Dosavadní kontroly zahrnují pouze čtení zdroje,
AST/syntaktickou kompilaci bez jeho spuštění, kontrolu závislostí a statický
přezkum. Žádné vědecké assertiony se zatím nevyhodnocovaly. Formální pin,
EXPECTED.txt, RUN.md, RESULT.md a dvouarchitekturní vědecká reprodukce dosud
neexistují. Před jejich vznikem je třeba přijmout přesný kód i vymezený
rozsah, poté postupovat podle aktuální POLICY. Samotné notes CI nemá význam
vědeckého běhu těchto souborů.
