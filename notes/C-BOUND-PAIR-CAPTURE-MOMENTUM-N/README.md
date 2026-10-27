# Vázaná dvojice, dva výstupy a závislost záchytu na hybnosti

**NON-CANONICAL / L1 / podmíněná analytická konstrukce.**
Autor: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Vymezení práce: [#1812](https://github.com/mathorn1973/twist-j/issues/1812).
Základ: veřejný Canon v106, `a193e389fb1ddb0bdc89165b015c95a17eb1e425`.

Tato práce navazuje na autorův návrh začít společnou stavbu fotonu,
elektronu a jejich interakce u již dokázané vázané dvojice. Prvním
výpočtem je záchyt dvojice v závislosti na její vstupní hybnosti.

## Dva výsledky

**Společný místní kontakt lze napsat přesně.** Původní dvojice běží
beze změny v jednom vlastním stavu přidaného dvoustavového portu.
Jiná příprava téhož portu dává výstupy spolu/proti sobě, s koeficientem
`1/(2 phi)` na shodě poloh. Je výslovně dokázáno, proč obě přípravy
nelze zaměnit. Zlaté čtení při pohybu obecně způsobí únik z původní
vázané větve. Samotný společný nosič tedy neodvozuje jejich totožnost
v jednom měřeném postupu.

**Pro pevně připravené záchyty je odvozena celá normalizovaná závislost
na hybnosti.** Mění se pouze střed `p` vstupního hybnostního okna.
Jeho šířka, energetické rozdělení, kontakt, nosič i přijímač zůstávají
stejné. Pravděpodobnost společného záchytu a záznamu je sudá a při
rostoucím `|p|` přísně klesá. Úzké přesné meze jejího poměru k hodnotě
v `p=0` lze určit bez nahrazení úplného rozptylového jmenovatele.

## Přesný význam děje

Vstupem je **nevázaná dvojice a stojící nosič**. Výstupem v úspěšné
větvi je **vázaná dvojice, odcházející pulz a záznam**. Přejímáme
celý model `HOMOGENEOUS-CAPTURE-CURRENT-RECORD`, včetně jeho
26 značek, obsazené paměti, všech rozptylových kanálů a energetického
okna bez záměny fází lišících se o celou otočku.

Vnitřní vazba dvojice používá `mu=2`, `g=2*pi/5`. Záchytná rotace
mezi stojícím a pohyblivým nosičem používá samostatné koeficienty
`3/5,4/5`. Tyto dva kontakty se nezaměňují. Zachovaný počet obsazení
a spektrální energie zůstávají odlišné účty převzatého modelu.

Vodorovná osa je střed hybnosti **příchozí dvojice**. Není to celková
hybnost dvojice a dalšího nosiče ani hybnost fyzikálně určeného fotonu.
Při posunu okna se zachovává stejné energetické rozdělení. Původní
příprava je přesně bod `p=0`.

## Čtení balíku

- [PROOF_PORT_LIFT.md](PROOF_PORT_LIFT.md): úplný dvouportový krok,
  zachování původní vázané větve, zlatý součinitel a přesná porucha
  způsobená jiným čtením.
- [PROOF_CAPTURE_PROFILE.md](PROOF_CAPTURE_PROFILE.md): zjednodušení
  skutečné vstupní hustoty, pevná rodina normalizovaných stavů,
  celý záchytný funkcionál, monotonicita a konečné obaly poměru
  pravděpodobností.
- [SOURCES.md](SOURCES.md): přesné veřejné zdroje a jejich otisky.
- [VALIDATION.md](VALIDATION.md): rozsah oddělených kontrol v této relaci.
- [P-BOUND-PAIR-CAPTURE-MOMENTUM-1](../../probes/P-BOUND-PAIR-CAPTURE-MOMENTUM-1/):
  předem zmrazený výpočet jedenácti racionálních intervalů.

## Co výsledek neříká

Absolutní průběh pravděpodobnosti nebyl vyčíslen. Pro všechny zvolené
vstupy je dokázaná kladná dolní mez `1/10^28`; ta není odhadem skutečné
velikosti. Číselný výsledek tohoto balíku jsou meze **relativního**
průběhu `P_win(p)/P_win(0)`.

Výsledek zůstává asymptotický a předpokládá výslovně zadanou spektrální
přípravu. Úspěch zahrnuje projektor na vázaný stav; samotný zápis v
přijímači vazbu nepotvrzuje. Náboj, spin a výměnná statistika elektronu,
polarizace a elektromagnetická povaha fotonu ani jejich fyzikální
totožnost nejsou z této konstrukce odvozeny. Následný rozptyl už
vázané dvojice s dopadajícím pulzem je samostatná další úloha.

Canon, jeho 26 otevřených H/O a všechny původní důkazy zůstávají beze
změny. Nové důkazy čekají na samostatné nezávislé přijetí.
