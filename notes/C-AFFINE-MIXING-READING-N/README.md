# Čtvercové čtení vynucené skládáním a vratným promícháním

Datum: 21. října 2026. Autor zápisu: A. M. Thorn.

**Stav: NON-CANONICAL, L1, pracovní analytický výsledek candidate-T.**
Samostatný důkaz podmíněné věty; nejde o změnu veřejného kánonu ani o nárok na prvenství v matematické literatuře.

Na racionálním prostoru stačí zachování součtu dvou čtení při jediném přesně určeném promíchání, aby nezáporná čtení nulová v nule musela být stejnou kvadratickou formou. Není potřeba předpokládat mnohočlennost, spojitost ani měřitelnost. Již dokázaná afinní souměrnost TWIST-J potom určí právě stopovou normu, až na celkové měřítko.

Navazující rozbor nalezl toto promíchání přímo uvnitř již zadané párové involuce JM pro program z₀=(1,0,0,0,0,0,0,0). Na přesně popsané invariantní rovině působí maticí [[−3,4],[4,3]]/5. Pět prokládaných buněk kóduje dvě kopie K=Q(ζ₅); permutace těchto buněk realizují potřebnou afinní akci na tomtéž kódu. Existence vhodného promíchání tak v deklarované třídě složených buněčných operací již není otevřená.

Je uveden i přesný celočíselný nosič s pevným jmenovatelem, na němž stejné racionální promíchání zachovává součet zadaných buněčných účtů bez zásobníku. Tento omezený zdvih se odlišuje od univerzálního zdvihu zachovávajícího společný dělitel. Cena přípravy a řadiče celého zdroje z něj neplyne; původní U se neodvozuje.

\[
\text{sčítavý účet a zachování při promíchání}
\Longrightarrow \text{kvadratická forma}
\Longrightarrow_{\mathrm{AGL}_1(\mathbb F_5)}
c\,\operatorname{Tr}_{\mathbb Q(\sqrt5)/\mathbb Q}(x\bar x).
\]

První implikace je zde rozepsána bez předpokladu druhého stupně. Druhá používá existující `AFFINE-QUADRATIC-FORM-UNIQUENESS [T]`. Nenulovost a nezápornost vyberou kladné c; jedna kalibrace je určí.

Zesílená podoba připouští dokonce dvě předem různá nezáporná čtení, nulová v prázdném stavu. Totéž promíchání vynutí, aby byla obě stejnou kvadratickou formou. Společné měřítko bloků tak nemusí být vloženo předem.

Výsledek přináší i přesnou opravu slabšího předpokladu: samotné sčítání účtů nezávislých bloků druhý stupeň nevynucuje. Rodina součtů čtvrtých mocnin normy je protipříkladem. Rozhoduje jejich skutečné promíchání. Rovněž zachování účtu celého přístroje včetně měnícího se zásobníku tuto podmínku nenahrazuje.

Navazující krok přidává pevný referenční kanál uvnitř téže zdrojové involuce. Pro normalizované váhy tří výsledků P₀,P₁,P₂ stačí požadovat, aby poměr P₁/P₀ závisel jen na x, poměr P₂/P₀ jen na y a referenční váha P₀ se zachovávala při promíchání a afinních permutacích. Při nezápornosti a nulové váze nepřítomného signálu je pak nutně

\[
(P_0,P_1,P_2)=
\frac{(1,cq_+(x),cq_+(y))}{1+c(q_+(x)+q_+(y))},\qquad c\ge0.
\]

Tato podoba nepostuluje předem číselný součet dvou nenormalizovaných účtů: získává jej z poměrů k referenci. Nezávislost těchto poměrů ovšem zůstává výslovnou podmínkou čtení. Samotná existence pevného referenčního vektoru ji ani zachování P₀ neprokazuje. Vylučující příklady oddělují tyto podmínky od pouhé vratnosti a od pouhé normalizace výsledků.

Při kalibraci již zadanou metrikou pětibuněčného nosiče má zvolená jednotková reference c=2/25. Bez této kalibrace zůstává společné c volné. Alternativní dodatek odvozuje stopové pravděpodobnostní čtení ze slučitelnosti všech racionálních efektů; jde o silnější předpoklad než dostupnost uvedené involuce a buněčných permutací.

## Obsah

- [PROOF.md](PROOF.md): obecná věta, důkaz konečnými rozdíly, napojení na stopovou normu, přesný celočíselný zdvih a protipříklady.
- [EXISTING-SOURCE.md](EXISTING-SOURCE.md): nalezené promíchání v existujícím zdroji JM, společný kód, celočíselné provedení a přesná hranice čtení.
- [OPERATIONAL-READING.md](OPERATIONAL-READING.md): pevná reference, výběrová věta pro poměry výsledků, přímé zkoušky podmínek a protipříklady.
- [RATIONAL-EFFECTS.md](RATIONAL-EFFECTS.md): alternativní odvození ze všech racionálních efektů, s úplným důkazem a výslovnými dodatečnými předpoklady.
- [SCOPE.md](SCOPE.md): předpoklady, vztah k Public Canon v104 a přesný otevřený požadavek na existující vazbu.
- [SOURCES.md](SOURCES.md): ověřené zdrojové verze a rozsah analytické kontroly.
- [SHA256SUMS](SHA256SUMS): otisky dokumentů.

Zbývající otázka má nyní přesnou podobu: zda fyzikálně příslušné čtení sestupuje na racionální amplitudy a splňuje uvedenou nezávislost poměrů i zachování referenční váhy. Pokud ano a signál má někdy nenulovou váhu, celý řetězec k jediné kladné stopové normě je dokázán. Normalizované váhy samy neurčují společný násobek všech nenormalizovaných účtů ani mechanismus skutečných četností. Tato otázka jedinečnosti není dodatečnou podmínkou správnosti existenčních vět Public Canon v104.
