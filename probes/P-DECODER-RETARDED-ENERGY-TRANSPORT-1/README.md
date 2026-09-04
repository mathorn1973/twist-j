# Source, D3 propagation and aperture energy

**NON-CANONICAL / PRE-PIN CANDIDATE / PHYSICAL COMPLETION UNRESOLVED**

`P-DECODER-RETARDED-ENERGY-TRANSPORT-1` is the focused extension reserved in
[issue #822](https://github.com/mathorn1973/twist-j/issues/822), based on
public main `2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97` and Canon v76.
The proposed claim is `DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT`.

The package connects three explicit mathematical maps:

```text
rational four-vector
  -> centered five-site D3 impulse from empty ready state
  -> actual selected two-slice wave propagation
  -> nonnegative local energy values on a fixed finite aperture.
```

Preparation gives the pair `(previous,current)=(0,S(a))` at post-kick cut
zero. Every subsequent numbered step follows the registered homogeneous D3
recurrence. The centered source satisfies `||S(a)||^2=m(a)`, the QDD
quadratic norm on the balanced source subset. This norm match is a disclosed
design choice. With the chosen energy convention, the initial global energy
is `m(a)/2`.

`Aperture(sites)` fixes canonical sorted distinct D3 sites.
`Reading(site_energy,total,kind)` contains exact local energy values at all
of those sites, including zeros, their aperture sum and `ZERO_READING` or
`ENERGY_READING`. Zero aperture energy does not mean
zero source. Reading uses both completed wave slices on the aperture plus
its finite stencil; transition flux needs the next current slice as well.
The record is passive: it neither absorbs the wave nor selects an outcome.

`prefix(a,aperture,length)` returns immutable `History(aperture,frames)`
with exactly `length` post-kick frames. A `Frame` carries its cut, reading
and the balance from the preceding free transition; that balance is absent
at cut zero. The separate forcing-sequence helper includes the ready state.
`balance` can evaluate arbitrary finite triples and forcing; its residual
is guaranteed zero only when the forced recurrence holds. Appending checks
consecutive cuts and compatible reading/balance records, without modifying
earlier entries. No reset interface is introduced.

| File | Role |
|---|---|
| `CONTRACT.md` | Source, state and aperture types; clock convention, choices and physical boundaries. |
| `PROOF.md` | Uniform conditional energy, continuity, forcing and locality arguments. |
| `PREREG.md` | Frozen claim, accepted program, finite audit gates and failure disposition. |
| `transport.py` | Exact mathematical implementation of the source, wave and reading maps. |
| `audit_transport.py` | Independent shell, pointwise, edge-sum and recursive Green references. |
| `verify.py` | Preregistered independent conformance audit. |
| Later `RUN.md`, `EXPECTED.txt`, `RESULT.md` | Actual pin, execution record and earned disposition; absent before the formal run. |

The source package must be publicly pinned and read back before scientific
execution. This README states no execution result. Exact program signatures,
commands and finite gate inputs are defined by the accepted source and
preregistration; no development invocation is a formal result.

After the public pin, generate a concrete exact readout from the repository root:

```sh
python3 probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py \
  --source 1/2 -2 1 1/3 --cuts 3 \
  --aperture-json '[[0,0,0],[1,1,0],[2,0,0]]'
```

The output is JSON with explicit numerator/denominator pairs. This is
mathematical energy and signed flux, not detector counts.

The imported transfer comes from the registered
[temporal-characteristic source pin](https://github.com/mathorn1973/twist-j/tree/fe5cbb4bc83dabd8e6704314e3b01c951e77cf42/probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1).
The preceding mathematical decoder remains at its own immutable
[source pin](https://github.com/mathorn1973/twist-j/tree/69c9dc34f57d5f9943681761eb6386a17d4bfc47/probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1);
its preparation is not rewritten by this extension.

This work concerns L1 encoded mathematics on finite-support rational wave
data. It does not finish the physical source-propagator-detector chain,
classify physical instruments, derive calibration, absorption, event counts,
Born probabilities or L6 measure. The #539 apparatus lane and #744 pole
identification remain unresolved. F3 under #756 remains NOT_SATISFIED and
production #742 remains FORBIDDEN. No Canon or old probe is changed.
