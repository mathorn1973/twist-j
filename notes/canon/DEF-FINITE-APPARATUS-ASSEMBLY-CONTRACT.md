<!-- SPDX-License-Identifier: Apache-2.0 -->

# DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT

Status: **NON-CANONICAL / STOP-DEFINITION / NO SCIENTIFIC AUTHORITY**.
Revision: `DEF-FINITE-APPARATUS-ASSEMBLY-CONTRACT-v0`, 2026-11-08.
Basis: Public Canon v109, tag `canon-v109`, content commit
`2b0f94ec1e0874bff9141259e0b7da80e6681ea6`, `canon/CANON.md` SHA-256
`035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383`,
1464066 bytes. Public `main` was `a8482d06` (merge of PR #1673) when this
revision was written; `STATUS.md` alone declares authority.
Companion map: `notes/STAVBA-STROJE-2026-11-08/`.

Two earlier definition surfaces are related but distinct:
`notes/canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md` types one apparatus
profile at the L4 to L5 boundary (manifest fields, carriers, equalities) and
`notes/canon/C-V106-APPARATUS-SYNTHESIS-N/` proposed the v106 apparatus
theorems with their admission obligations. This note types the cycle that
joins such profiles end to end; it does not replace either. The v109 fold
audit `notes/canon/V109-SYNTHESIS/README.md` states the separation of the
contact and native carriers that section 4 takes as its fixed input.

This note proposes one typed manifest for the object the apparatus program
has been assembling piece by piece since Public Canon v100: a complete finite
apparatus cycle, called "the machine" in the owner's working language. It
creates no claim, status, scope, dependency, gate, evidence, probe or Canon
version. It changes no file under `canon/`. It is a specification surface
against which a later preregistration, review or fold can be typed and
audited. Where this note and `canon/REGISTRY.tsv` disagree, the registry wins.

The motivating obligations remain with their registered owners and are not
moved by this note:

```text
QDD-INSTRUMENT-APPARATUS [O]            physical apparatus, realized event, occurrence
QDD-TERMINAL-EVENT-SEMANTICS [O]        physical meaning of a completed event
QDD-INSTRUMENT-CLASS-COMPLETENESS [O]   complete admissible apparatus class
QUADRATIC-MEMORY-NATIVE-CONTACT [O]     a native global permutation with exact readout
MINIMAL-READ-DERIVATION [O]             whether the architecture forces the minimal read
```

## 1. Why a contract and not another construction

Every apparatus theorem of v100 to v109 is an exact L1 construction on a
declared carrier with supplied preparations, operations and resources. The
Canon says of each that the carriers "keep separate laws and interfaces", that
"neither carrier supplies autonomous input selection, retained-archive
regeneration or an identification with the other", and that physical
preparation, occurrence and reset remain open. The constructions therefore
accumulate without a statement that says when the machine is finished.

The frontier program table marks the apparatus owners `STOP`: definition work
is required before computation is meaningful. This contract is that
definition work for the assembly question only. It fixes the stages of a
closed cycle, the carriers on which stages exist today, the bridges a single
carrier would need, and decision conditions for each bridge. It does not
decide any bridge.

## 2. The closed cycle

A **closed finite apparatus cycle** is a tuple of nine typed stages. Each
stage declares its carrier, its law or alphabet, its resource account, its
input and output types and its equality. A stage with no declared carrier is
`EMPTY`. A stage whose output type is not the next stage's input type on the
same carrier is `UNMATCHED`.

```text
S0 ENVIRONMENT   declared resource states and their functional (thermal
                 factors, fuel, fresh blank banks); nothing is prepared yet
S1 BOOTSTRAP     from S0 states to a charged work store, a running master
                 clock and a loading cursor, with an explicit error
S2 PREPARATION   near-clean registers, a prepared input family I (finite),
                 and one common auxiliary state for all members of I
S3 LOAD          one fixed program that moves a member of I from stock into
                 the active input slots without selecting a word by the input
S4 RUN           the dynamical core for a declared horizon: native U on
                 Omega = N_0 x F_5^6, or a fixed contact word on O^m
S5 RECORD        a first record written into a fresh bank; retained records
                 that later stages do not address
S6 READ          an exact reader from the archives alone to the input
                 identity or the declared observable, with its information
                 boundary stated
S7 RESTORE       return of work core, source, clock and controls to their
                 preparation, with every consumed fresh resource counted
S8 REPEAT        k cycles for a declared finite horizon k, with the complete
                 account, the archive count and the stock consumption as
                 functions of k
```

The cycle is **closed on a carrier K** when all nine stages are declared on
K with matching types, the composite map is a bijection of the complete
carrier (so the literal inverse exists), and the resource account of K is
conserved by every primitive. The cycle is **closed across carriers** when a
bridge of section 4 is proved for every carrier change.

Three things are deliberately outside the cycle and stay with their owners:
autonomous choice of the next input (the program is a supplied schedule),
regeneration of retained archives (a retained record is consumed storage),
and the occurrence of one outcome (the L5 to L6 lift adopted in ETH-QDD-1
and ETH-QDD-2 at [D]). A cycle theorem would say nothing about them.

## 3. Carriers on which stages exist at v109

Six carriers carry apparatus results today. The claim identifiers below are
examples with their registry status; the complete slot table with every
identifier is `notes/STAVBA-STROJE-2026-11-08/ASSEMBLY.tsv`, checked
mechanically against the registry by `check_assembly.py` in the same
directory.

| Carrier | State and law | Account | Representative claims |
|---|---|---|---|
| K1 native | `Omega = N_0 x F_5^6`, update `U` with the five affine involutions `a..e` and the Thue-Morse selector | no additive account; conserved chart labels of `U-NATIVE-CHART-AND-QDD-READBACK` | `U-NATIVE-RAW-RESIDUE-READOUT [T]`, `U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO [T]`, `U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS [T]` |
| K2 contact | `O^m`, `O = Z[j]`, total contact `C_rho` with parity admission and whole-slot `SWAP` | half-trace account `Q`, ring sum, labelled residues modulo `1-j` | `RELATIVE-CONTACT-INTEGRAL-LAW [T]`, `RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T]`, `RELATIVE-CONTACT-FINITE-WORKBANK-REUSE [T]` |
| K3 register | `F_5` cells under the primitives `SUM, EQ, MUL, SHIFT, REFLECT, SCALE` of the arithmetic compiler | none beyond reversibility | `U-CARRY-MIRROR-FINITE-CIRCUIT [C]`; `P-J-LAMBDA-CARRY-ARITHMETIC-1`, `P-CARRY-MOMENT-DEPTH-1` (NON-CANONICAL) |
| K4 integer field cell | declared integer automata, Cartesian integer cell sources, funded reversible gates | declared positive integer energy or resource functional | `FIELD-CONSERVATIVE-CHAIN-LAW [T]`, `AUTONOMOUS-SOURCE-WORK-RECORD-CHAIN [T]`, `JM-FUNDED-INTEGER-PAIR-SOURCE [T]` |
| K5 coherent walk | `W = exp[-i(2 pi/5) P_0] S G` on `l^2(Z_R x Z_r) (x) C^4`, the recording step `U_rec` | spectral energy `H = i Log_alpha W`, selected battery energy | `CONTACT-W-SPECTRAL-READING [T]`, `SELECTED-SPECTRAL-ENERGY-SOURCE [T]`, `HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T]` |
| K6 thermal | finite qubit and multilevel registers under one positive static local Hamiltonian `H = H_0 + H_prop` | bare energy `H_0`, Gibbs factors, entropy of retained defects | `THERMAL-ORIGINAL-PORT-APPARATUS [T]`, `LOCAL-THERMAL-TWO-ATTEMPT [T]`; `C-THERMAL-WORK-CLOCK-BOOTSTRAP-N` (NON-CANONICAL) |

The six accounts are six different quantities. No registered row identifies
two of them. The Canon states this explicitly for the thermal, spectral and
contact accounts ("none of these statements equates its conserved account with
every other time generator") and for the native and contact carriers.

Stage coverage at v109, in the status vocabulary of the sources:

```text
         S0   S1   S2   S3   S4   S5   S6   S7   S8
K1 native -    -    T    -    T    T    T    -    -      prepared heads retained; receiver records; carry mirror [C]
K2 contact -   -    T  T+cand T    T    T    T    T      S3: supplied swaps load prequeued inputs [T]; the 322-contact loader is NON-CANONICAL and in another input dialect
K3 register -  -    -    -   T+C   C    C    C    -      three carry theorems [T]; the 62-register two-pass circuit [C]
K4 field  -    -    T    -    T    T    T    T    -      return of the original receiver, not full reset
K5 walk   -    -   cand  -    T    T    T    -    -      forward-only filter (NON-CANONICAL); capture asymptotic
K6 thermal cand cand T+cand cand T  T    T    T    T      S0, S1, S3 analytical candidates, no verifier; S2 has one [T]
```

`T`, `C` are registry statuses; `cand` means a merged NON-CANONICAL
candidate; `-` means `EMPTY`. K6 groups the finite register apparatuses
under one positive static Hamiltonian; the 140-gate compact device
(`COMPACT-ACTIVE-RECORD-APPARATUS [T]`) is a distinct supplied
implementation whose locality and energy operator the Canon does not
identify with the thermal port apparatus, and the map lists it on K6 only
as a second implementation of the same stages. The table is the reading of
the map at the date above and is not a registry object.

## 4. Bridge obligations

A carrier change inside one cycle needs a bridge: a typed map between the two
state spaces that carries the account, the preparation family and the record
semantics. Four bridges would close the cycle on the carriers that exist. Each
is written in the registry's decision-condition form. None is registered.

### B1 contact to native (K2 to K1)

Question: does any fixed contact and swap word on `O^m` realize one native
update `U` on a declared embedding of `F_5^6`?

Fixed input: `RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY [T]` says that
every fixed word changes the complete residue vector modulo `1-j` by one
input-independent permutation of slots. On the native side the generators
`a..e` are affine involutions of `F_5^6` and only `a` is a coordinate
permutation; `b`, `c`, `d`, `e` contain negations and translations. A
literal residue-level identification of a contact word with `U` is therefore
excluded for every word that is not the identity or `a` on residues. This is a
remark derived from two registered rows, not a new claim; it says where a
bridge cannot be and nothing about where it can.

Decision: closes positively only with an explicitly declared embedding of
the native checkpoint into `O^m` that is not the residue map, a fixed word
whose action on the embedded image equals `U` on a declared ready set, an
exact inverse and an all-reachable-state certificate; closes negatively only
by a proof over the complete frozen class of embeddings and words; `STOP`
while the embedding class is not frozen. `QUADRATIC-MEMORY-NATIVE-CONTACT [O]`
owns the related native-side question and is not moved.

### B2 native to register (K1 to K3)

Fixed input: `U-CARRY-MIRROR-FINITE-CIRCUIT [C]` already executes the actual
native first-receiver tick with a supplied affine transfer on 62 `F_5`
registers for all 500 admitted inputs. The bridge exists as a finite
computation. It is `C` because the circuit, wiring, clean workspace and
separately enabled native origins are supplied, because its inverse is the
forward word in reverse order with each primitive inverted rather than an
independently compiled inverse, and because the native updates are not
globally inverted.

Decision: lifts to a proved bridge when the register program is shown to
realize the native tick on the complete declared ready set with an exact
inverse and no supplied origin; remains `C` while the native global inverse
is missing; closes negatively only with a proved obstruction over the
complete register class.

### B3 register or contact to coherent walk (K2, K3 to K5)

Question: does the integer carrier embed into the coherent walk so that the
half-trace account or the register reversibility corresponds to the selected
spectral energy?

Fixed input: `COHERENT-W-LOCALIZED-RING-CLOSURE [T]` separates raw `O`,
amplitudes `O[1/5]` and `F_5` residues and proves that no unital
`O[1/5] -> F_5` map exists. `C-COMMON-COUNTER-PATH-PHASE-N` (NON-CANONICAL)
records that on the contact carrier the path-sensitive five-position quantity
is a count and that the half-trace and Hermitian sum are endpoint functions,
so a relation between the two kinds would be an amplitude normalization that
no result supplies.

Decision: closes positively only with a declared embedding, an exact
statement of which account maps to which energy, and a proof on a declared
preparation family; closes negatively only over a complete frozen embedding
class; `STOP` while the amplitude normalization is unfixed. This is the
owner's "common carrier and unification of conserved accounts" task in his
own list of five.

### B4 thermal to coherent walk (K6 to K5)

Fixed input: the thermal apparatus theorems and the three bootstrap notes
prepare the source, the work store and the master clock that the recording
step `U_rec` consumes, under one positive static local Hamiltonian with
explicit errors. `THERMAL-ORIGINAL-PORT-APPARATUS [T]` executes three `U_rec`
steps at original ports. The bridge therefore exists at the level of the
original-port device, with "own conserved energy, no equality with original
Q".

Decision: closes positively when one Hamiltonian is shown to carry S0 to S7
with the spectral energy of K5 as its conserved account on the active
sector, or when the two accounts are proved to agree on a declared sector;
remains conditional while the temperature contrast, nonstationarity and
product boundary are supplied rather than derived, as the bootstrap notes
state.

## 5. The target statement

The assembly question has one natural target, written here as a proposed
obligation and not as a registry row:

```text
FINITE-APPARATUS-CLOSED-CYCLE (proposed, unregistered)

  There exist one carrier K, one fixed program P on K, one declared
  environment state in S0, a finite prepared input family I and a horizon
  k >= 1 such that the composite of S0 to S8 is a bijection of the complete
  carrier; every primitive conserves the account of K; the k records are
  recoverable from the archives alone; after every cycle the work core,
  source, clock and controls equal their preparation; the fresh resources
  consumed are an explicit function of k; and the bootstrap error, the
  accepted weight and the unwanted fraction are explicit.

  Decision: closes positively by one construction with an exact verifier
  on two architectures and an independent proof of the all-k clause; closes
  negatively only by a proof over a complete frozen class of carriers and
  programs; STOP while any stage of section 2 is EMPTY or UNMATCHED on the
  chosen carrier and no bridge of section 4 covers the gap.

  Not asserted by a positive closure: autonomous next-input choice,
  regeneration of retained archives, an occurrence law, a physical
  interface, an SI scale, or derivation of the carrier from J or from U.
```

Two restricted targets are already close to their hypotheses and would be
stated first:

- `CC-CONTACT`: the cycle on K2 alone, with S0 and S1 declared `EMPTY` and
  S2 to S8 taken from the v107 to v109 theorems (preparation minima and bank
  capacity at v107, the common apparatus at v108, the workbank reuse at
  v109) and the 322-contact loader. The supplied whole-slot swaps that load
  prequeued inputs are a proved S3 for inputs prepared in the apparatus
  dialect; what is missing is a proved S3 from stock whose output type is
  the active input of the variable-arrival apparatus. Today the loader
  prepares a pole height on a six-slot carrier and the apparatus reads a
  source orbit and a clock pair, which are different input dialects of the
  same contact law; the companion map records this as an `UNMATCHED`
  stage pair.
- `CC-THERMAL`: the cycle on K6 with K5 as its active sector, with S0 to S3
  taken from the bootstrap notes after independent acceptance and S4 to S8
  from the original-port and two-attempt theorems. What is missing is a
  reader S6 from archives alone and the agreement of accounts of B4.

A positive `CC-CONTACT` would be the first theorem that says "this is a
whole machine" on one integer carrier. It would still be a conditional L1
statement with a supplied schedule.

## 6. Conformance fields for a profile

A profile claiming the cycle, or one of the restricted targets, publishes:

```text
profile_id, basis_commit, carrier_id, account_id
stage table S0..S8: carrier, law, input_type, output_type, equality, status
bridge table: for every carrier change, the bridge id of section 4 and its
              decision state
resource table: fresh resources consumed per cycle, as a function of k
reader: the archive-only reader and its information boundary
not_asserted: the fixed list of section 5, verbatim
```

A profile with any `EMPTY` or `UNMATCHED` stage is `STOP-DEFINITION`.
Shared syntax creates no shared scientific edge: a conforming profile on K2
does not close a profile on K6.

The companion map records every adjacent stage pair with one of four edge
kinds. `proved-composition`: a registered theorem or a merged note composes
the two stages on one carrier. `same-carrier-composable`: same carrier and
law, literal concatenation is meaningful, no composition theorem.
`declared-not-identified`: the Canon states that the two objects are not
identified. `missing-bridge`: no object connects them; on one carrier this
is the `UNMATCHED` case of section 2, across carriers it is a bridge of
section 4 that does not exist.

## 7. What this note does not do

It does not register a claim, a gate or a dependency. It does not identify
any two accounts. It does not promote the thermal bootstrap notes, the loader
or the carry circuit beyond their stated statuses. It does not decide
`QDD-INSTRUMENT-APPARATUS`, `QUADRATIC-MEMORY-NATIVE-CONTACT` or
`MINIMAL-READ-DERIVATION`, and it does not touch the occurrence law. Any use
of this contract to claim completion requires the preregistration, verifier,
two-architecture replay and reviewed fold of `POLICY.md`.
