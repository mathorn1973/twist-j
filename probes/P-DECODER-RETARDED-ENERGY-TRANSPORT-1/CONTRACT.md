# Retarded wave transport and local energy reading

**NON-CANONICAL / PRE-PIN CANDIDATE / NO SCIENTIFIC STATUS ASSIGNED**

This contract specifies one mathematical extension from an explicit source
to the selected D3 wave recurrence and then to an exact local aperture
reading. It is not a whole-decoder completion manifest or a physical
source/detector realization. The proposed claim is
`DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT`; its proof is in `PROOF.md` and its
formal gates and disposition belong to `PREREG.md` and the later result.
No execution result is asserted by this source document.

```text
probe: P-DECODER-RETARDED-ENERGY-TRANSPORT-1
public_lock: https://github.com/mathorn1973/twist-j/issues/822
source_base: 2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97
authority: Public Canon v76
canon_content: 07910adb8418742bf52a0d204577b84b38009b18
canon_sha256: c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112
canon_bytes: 420539
action_layer: L1 encoded mathematical transport and reading
physical_completion: UNRESOLVED
```

## 1. Source and state types

Let `D3={x in Z^3: x_0+x_1+x_2 is even}`. A wave is an exactly represented
finitely supported rational function on D3. The wave-pair type is

```text
Wave = C_c(D3,Q),
Pair = Wave x Wave,
Pair(previous,current) = (u,v).
```

Coordinate, rational and function equality are literal; sparse encodings
sort distinct sites and omit zero coefficients. The pair order is fixed.
There is no spatial wrapping, truncation, projective quotient or phase
identification. Global energy is defined on this finite-support domain,
not on every function in the Canon's larger `Map(D3,C)` carrier.

The admitted source parameter is `a=(a_0,a_1,a_2,a_3) in Q^4`. Distinguish
this source parameter from the current wave slice `v`. Choose

```text
p_0=(0,0,0), p_1=(1,1,0), p_2=(1,0,1),
p_3=(0,1,1), p_4=(2,0,0),
b(a)=(a_0,a_1,a_2,a_3,0)-(sum_i a_i)/5 * (1,1,1,1,1),
S(a)=sum_(j=0)^4 b_j(a) delta_(p_j).
```

Thus `sum b_j=0` and

```text
||S(a)||^2=sum_i a_i^2-(sum_i a_i)^2/5 = m(a).
```

On the balanced QDD source subset, `m(a)` equals the registered QDD total
weight. The same rational quadratic expression on all Q^4 is an explicit
extension of the source domain. This norm match was known when selecting
the centered five-site injection; it is a result-exposed design choice,
not an independent derivation of a physical QDD-to-photon coupling. No
LOW/HIGH branch weights are identified with spatial aperture readings.

## 2. Preparation and propagation

Use every displacement in the five complete symmetric D3 shells of squared
lengths `2,4,8,10,16`, with weights `6,1,15,1,1`. Write `B` for their union,
`c_z=w_(|z|^2)/324`, and

```text
s_0=sum_(z in B) c_z=8/9,
(L f)(x)=sum_(z in B) c_z [f(x)-f(x+z)].
```

This is the registered flat-flux operator `A_F0`, with its existing
dimensionless normalization. A general forced mathematical step is

```text
ForcedStep((u,v),f)=(v,w),
w=2v-u-Lv+f,                       f in Wave.
```

The actual source-driven family in this probe uses exactly one impulse:

```text
ready=(0,0),
prepare(a)=ForcedStep(ready,S(a))=(0,S(a))=:P_0,
P_(n+1)=ForcedStep(P_n,0),          n>=0.
```

`P_0` is the post-kick cut. The ready state precedes that cut and is not
silently counted as another propagation step. Preparation never repeats
during free continuation. A generic finite forcing `f` may appear in the
source-work identity, but the declared prepared trajectory has `f=0` on
every subsequent numbered transition.

Each step uses a finite stencil and finite-support data. Propagation is the
actual recurrence on D3, not repeated output of a source label or static
norm. A local energy reading has an additional stencil halo around wave
values; its support is not identified with the support of a single wave
slice. Retarded dependence means dependence on the prepared source and
completed successive slices, not a physical speed or causal-cone claim.

## 3. Energy and locality

For `(u,v) in Pair`, define the chosen quadratic invariant

```text
E(u,v)=1/2 ||v-u||^2 + 1/2 <u,Lv>,
<u,v>=sum_(x in D3) u(x)v(x).
```

Fix the following local representation, where `d_x=v(x)-u(x)`:

```text
e_x(u,v)=(2-s_0)/4 * d_x^2
       + 1/8 sum_(z in B) c_z [
           (v(x+z)-u(x))^2 + (u(x+z)-v(x))^2
         ].
```

Its coefficients are positive, so each local value is nonnegative. The
intended exact identities are `sum_x e_x=E`, conservation under a free
step, and `E=0 iff u=v=0` on the stated finite-support D3 domain. Strict
positivity is not asserted on a periodic finite box, where a constant
equal-slice mode would require separate treatment. After the one source
kick, `E(P_0)=m(a)/2`; the factor one half is part of this energy convention.

`PROOF.md` fixes the oriented local flux and forced source-work expressions
and proves their balance identity. The balance functional accepts any
finite-support triple `(u,v,w)` and finite forcing `f`; its residual is
claimed to vanish only when `w=2v-u-Lv+f`. Its signs and slice order belong
to that identity and may not be altered after the source pin. The flux is a
signed mathematical transfer, not a nonnegative count or an occurrence
probability. Conservation of a quadratic expression does not uniquely
select a physical energy density, current or detector coupling.

To read `e_x` for `x in R`, the necessary wave values lie in `R+(B union
{0})` for both slices. The density of a pair may be read only after its
current slice is available. A transition-flux/source-work record needs the
old pair together with its newly computed current slice and any declared
forcing; it is available only after that transition is complete. No future
slice is supplied by an outcome target or a detector record.

## 4. Aperture context and output records

An aperture context is an immutable canonical tuple `R` of distinct D3
sites in lexicographic order, including the empty tuple. Equality compares
that canonical tuple and its exact site coordinates. It is an explicit input context,
fixed independently of the trajectory values and of any desired reading.
The contract does not search for an aperture that produces a target result.

At cut `n`, `readout(P_n,aperture)` returns the immutable
`Reading(site_energy,total,kind)`. Its ordered `site_energy` includes
every aperture site, including entries with value zero. The total and kind
are

```text
aperture_total=sum_(x in R) e_x(P_n),
kind=ZERO_READING    iff aperture_total=0,
kind=ENERGY_READING  iff aperture_total>0.
```

The record's total means the aperture sum. Global `E(P_n)` is a separate
functional and must be named separately if reported. A ZERO_READING can
occur for a nonzero source outside the aperture's current energy support;
it never asserts zero source, no physical particle or failed preparation.
The global zero state and the empty aperture have an explicit zero reading.

The other record types are

```text
Aperture(sites),
Balance(change,outward_flux,work,residual),
Frame(cut,reading,balance_from_previous),
History(aperture,frames).
```

`balance((u,v),w,f,aperture)` uses the triple and the aperture stencil
footprint. Here `change=E_R(v,w)-E_R(u,v)` and
`residual=change+outward_flux-work`. A balance value is defined even for a
triple that fails the forced recurrence; zero residual is the conditional
identity, not a constructor default.

`prefix(a,aperture,length)` starts at post-kick cut zero and returns exactly
`length` frames, then advances by free steps only. At cut zero,
`balance_from_previous` is the explicit absent option. Each later frame
contains the balance from its preceding free transition. The forcing
sequence helper `forced_history(forcings)` separately includes the ready
state; it does not change the post-kick convention of `prefix`.

The reader has unit mathematical gain. It does not absorb, scatter or alter
the wave and takes no source parameter. Repeating a read of the same pair
and context returns the same record and creates no additional interaction.
Histories are immutable ordered tuples. `append_history(history,frame)`
checks consecutive cuts, consistency with the aperture and the balance
change between consecutive reading totals. Those record checks are distinct
from independently checking the underlying recurrence. Earlier entries are
unchanged by a longer requested prefix. There is no reset operation or
mutating truncation; fresh history construction and append are explicit.
Transition balance is distinguished from pair energy by its record type.
No clock time, random seed, external data, outcome-selected normalization or
unstated phase is an input.

The remaining preparation, forced/free transition, pair-energy and local
density operations implement the maps above. All accepted signatures are
frozen in `transport.py` together with this contract and the preregistration.
Any CLI serialization is a lossless representation of the same exact data,
not another selection or measurement operation.

## 5. Explicit choices and unchanged obligations

| Choice ID | Chosen datum |
|---|---|
| `CH-RET-SOURCE` | Q^4 source parameter and centered five-site injection with exposed QDD norm match. |
| `CH-RET-PREPARATION` | Empty ready pair, one finite impulse, post-kick cut zero, then free propagation. |
| `CH-RET-DOMAIN` | Exact rational finite support on the infinite marked D3 carrier. |
| `CH-RET-PAIR-ORDER` | Pair(previous,current), with flux records delayed until the next current exists. |
| `CH-RET-ENERGY` | The displayed invariant, local square decomposition and the oriented balance representative in PROOF.md. |
| `CH-RET-APERTURE` | Explicit finite canonical sorted unique site context and unit gain. |
| `CH-RET-ZERO` | ZERO_READING describes zero aperture energy only. |
| `CH-RET-HISTORY` | Immutable ordered exact records, passive rereading and no saturation quotient. |

The homogeneous operator and its normalization are imported at the exact
scope of `PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]` and
`PHOTON-TEMPORAL-CHARACTERISTIC [T]`. The new preparation, energy reading
and aperture choices are not consequences of that dictionary's adoption.
The former pointed decoder's source injection and initialization are not
modified; this is a separately named extension with its own definitions.

The following remain unresolved: physical source and wave coupling;
identification of this scalar wave with an emitted photon; physical detector,
pointer, reduction, absorption or post-state law; physical calibration and
SI energy; realized event/occurrence law; completeness or uniqueness of an
admissible physical apparatus family; Born outcome selection, probability,
self-location and every L6 measure claim. Mathematical forcing acts on the
wave pair only. No reader output changes it, the source parameter or
autonomous U. This contract introduces no U write port.

The public boundaries remain separate:

- [#539](https://github.com/mathorn1973/twist-j/issues/539) remains the
  STOP-DEFINITION typed-apparatus lane; this local functional does not close
  its physical profiles or their equality/class requirements.
- [#744](https://github.com/mathorn1973/twist-j/issues/744) still owns the
  pending pole/residue/polarization and normalization identification. This
  scalar energy identity supplies none of its missing S1-S7 chain.
- [#756](https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5500304645)
  retains F3 NOT_SATISFIED. Production under
  [#742](https://github.com/mathorn1973/twist-j/issues/742) remains FORBIDDEN.
  No dual/Ward ensemble, production state or phase-evidence computation is
  opened by this probe.

Only a separately preregistered and reviewed result may assign a status to
the proposed conditional mathematical claim. This source package changes
no Canon file, old probe, production freeze or physical gate.
