# P-PHOTON-TEMPORAL-CHARACTERISTIC-1 result

Status: `CHARACTERISTIC-PROVED / PROOF-FIRST / PUBLIC TWO-ARCHITECTURE GATE
PASS / CANON UNCHANGED`

The immutable verifier completed with exit zero, empty stderr and exact stdout
equal to `EXPECTED.txt`. All twenty certificate gates passed and no frozen
scientific falsifier fired. Clean public x86_64 and aarch64 jobs reproduced
the same verifier and stdout byte for byte, and the aggregate check passed.
The frozen outcome is therefore `CHARACTERISTIC-PROVED` at exactly the
preregistered scope.

## Exact return

```text
ALL EXACT CERTIFICATES PASS: 20/20
Owner datum is D; the conditional characteristic is proof-first T.
L2-to-L5 only; Herm2 identification and physical photon remain open.
```

The exact audit establishes the following conditional result for the complete
selected tuple frozen in `PREREG.md`.

## Selected dictionary datum

The real spatial carrier is

```text
D3 = {x in Z^3 : x1+x2+x3 is even},
Gamma_D3 = 2pi Z^3 union (pi(1,1,1)+2pi Z^3).
```

The adopted shell weights are `W*=(6,1,15,1,1)` on squared norms
`{2,4,8,10,16}`, the normalization is `1/324`, and the flux is the fixed
trivial flux `F0=1`. Its scalar character symbol is

```text
s(k) = (1/324) sum_v w(v)(1-cos(<k,v>)),
0 <= s(k) <= 16/9,
s(k)=0 exactly for k in Gamma_D3.
```

Within the explicitly frozen scalar, nearest-neighbor, time-reversal
symmetric class

```text
psi_(m+2)+psi_m+(a+b s(k))psi_(m+1)=0,
```

the zero mode and unit tangent normalization uniquely force `a=-2` and
`b=1`. This selects

```text
psi_(m+2)-2psi_(m+1)+psi_m+A_F0 psi_(m+1)=0,
X_m=(psi_(m+1),psi_m),
X_(m+1)=T_op X_m,
T_op=[[2I-A_F0,-I],[I,0]].
```

This is the complete proposed dictionary row

```text
PHOTON-SPATIAL-TEMPORAL-TRANSFER [D], MULTI.
```

It is an owner selection, not a proof that no other temporal class or physical
dictionary can exist.

## Exact L5 characteristic theorem

On a spatial character,

```text
T(k) = [[2-s(k),-1],[1,0]],
det T(k)=1.
```

With `lambda=exp(-i omega)`, direct exact expansion gives

```text
det(exp(-i omega)I-T(k))
  = exp(-i omega)[s(k)-4sin^2(omega/2)].
```

Therefore the selected total characteristic set is exactly

```text
K_op = {([omega],[k]) : 4sin^2(omega/2)=s(k)}
```

on `(R/2pi Z) x T_D3`. For every nonzero spatial character its two distinct
frequency classes are

```text
omega_+(k)=+2asin(sqrt(s(k))/2),
omega_-(k)=-2asin(sqrt(s(k))/2)       modulo 2pi,
```

and the corresponding multipliers form a reciprocal conjugate pair on the
unit circle. The transfer is elliptic for `s>0`. At the unique zero character
the two roots meet at `lambda=1` and the transfer is non-identity unipotent,
hence parabolic with algebraic multiplicity two.

For every real `epsilon>0`, `Omega in R` and `k in R^3`, the lifted comparison
function

```text
q_epsilon(Omega,k)
  = 4sin^2(epsilon Omega/2)/epsilon^2
    - s(epsilon k)/epsilon^2
```

satisfies the global exact bound

```text
-(epsilon^2/12) Omega^4
  <= q_epsilon(Omega,k)-(Omega^2-|k|^2)
  <= (11/27) epsilon^2 |k|^4.
```

Thus it converges uniformly on bounded lifted sets to
`Omega^2-|k|^2`. This earns the conditional proposed row

```text
PHOTON-TEMPORAL-CHARACTERISTIC [T], L5,
```

with the public integrity gate now passed, and subject only to a later
separate Canon fold.

## Audit disposition

The verifier reconstructed the five complete shells, their signed-permutation
symmetry and exact moments; the `D3` support and reciprocal lattice; flat-flux
reversal and holonomy; the normalized Fourier symbol; uniqueness inside the
selected temporal class; determinant, roots, stability and apex type; the
global trigonometric remainder chain; temporal-spatial scaling; quotient zero;
and negative spatial, scale, dual, flux, temporal, transfer and bound controls.

Every one of G01--G20 passed. No exact counterexample to a displayed theorem
clause was found, so `CHARACTERISTIC-REFUTED` did not fire. The selected tuple
is completely typed and the run completed, so no scientific or local
integrity `STOP` fired. The denied host-launch preflight described in `RUN.md`
occurred before a verifier process existed and carries no scientific verdict.

## Public status disposition

The public two-architecture computation gate is complete. This probe earns
evidence for the complete proposed `D` tuple and conditional proof-first `T`
theorem, but it does not directly edit the Registry or Canon. Therefore:

- the public Registry and Canon remain unchanged;
- `GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC` remains open;
- `PHOTON-CONE-CONVERGENCE [O]` remains open.

A separate sealed Canon fold may now register the complete `D` tuple and
conditional `T` theorem and close only the L2-to-L5 temporal characteristic
gate. This probe itself makes no Canon, Registry, dependency, evidence, gate,
frontier, release or workflow edit.

## Scope firewall

The theorem is conditional on `D3`, `W*`, normalization `1/324`, flat flux,
unit forward counter and the displayed temporal class. It claims no
completeness outside that class, no bilateral physical time and no derived SI
speed or scale.

The two ambient representatives of the spatial zero are one point on the
`D3` momentum quotient. They are not two photons, polarizations or Born
halves. The two temporal branches are unit-modulus phases, not a
contraction/expansion pair in transfer-amplitude sense.

No Herm2 carrier, positive cone, Born rule, causal ontology, global cone
identity, Lorentz invariance, null-set convergence, physical continuum,
massless phase, propagator, polarization, apparatus, readout or physical
photon is established. The independent L4-to-L5 Herm2 identification gate
remains open under this positive result.

The proposed contraction/expansion, matter/light and visible/invisible reading
is therefore neither assumed nor refuted here. It remains motivation for a
later independently frozen bridge, not a premise smuggled into the earned
mathematics.

## Pin and local receipt

```text
public claim issue:       #734
pin commit:               fe5cbb4bc83dabd8e6704314e3b01c951e77cf42
verifier SHA-256:         3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       1208
local stdout SHA-256:     a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645
public workflow:          33447090686
public x86_64 job:        99668497852 PASS
public aarch64 job:       99668497583 PASS
public aggregate job:     99668558513 PASS
```
