# A sharp energy boundary and a compact occupied-record apparatus

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-25. License: Apache-2.0.
Reservation: [#1778](https://github.com/mathorn1973/twist-j/issues/1778).
Promotion dossier: **PROMO-C-COMPACT-ENERGY-RECORD-N**.
Independent scientific acceptance remains pending.

This successor answers two concrete questions left by PR #1777: whether
the nominated original spectral energy can be realized by bounded-range
physical occupation interactions, and whether the supplied active-source
measurement can be implemented without generic elimination on thousands
of occupation qubits. The answers have different scopes and must not be
combined into a claim that the new small apparatus realizes the old Q.

## 1. The global original-energy target has an exact obstruction

[ENERGY_BRIDGE.md](ENERGY_BRIDGE.md) fixes the complete original sector,
the actual occupation encoding and Q=E0 f(U_rec) with the already nominated
positive scalar logarithm. It proves

    ||I* Q_tilde I - Q|| >= pi E0

for every bounded compression of physical interactions with any fixed
finite spatial diameter. The same lower bound applies to the complete
intertwining-action error. It is sharp in the stated bounded comparison
class, independently of how large the finite range is allowed to be.

The physical support step uses the actual distinct pulse subbank: a term
moving a pulse from x to x' must contain both sites. The free translated
limit and translation averaging then turn this restriction into a
continuous polynomial in pulse momentum. The fixed spectral energy has
a transverse jump of 2pi E0 on an open set of the other momenta, which
forces the error floor. This is an actual physical-support conclusion,
stronger than restating the prior configuration-locality obstruction.

It excludes global uniform approximation in this class, including an
exact extension. It does not exclude finite prepared families, a chosen
safe channel, a different energy branch, extra branch information, or a
different physical encoding. Energies assigned to invalid sectors cannot
repair the failed compression in the frozen product encoding.

## 2. A direct small-register construction preserves the active experiment

[COMPACT_MODEL.md](COMPACT_MODEL.md) factorizes the original finite
coordinate step into eight explicit register gates, including its
receiver calibration and controlled scalar phase. It expands every
forward/inverse source call, keeps the exact active source preparation,
and performs the three original forward steps. A final coherent pointer
coupling records whether the original receiver label is d0. All outcome
branches and arbitrary old-memory/reference correlations remain present.

The construction gives a finite positive time-independent history
Hamiltonian with an explicit energy spectrum, input moments, complete
initial-resource inventory, finite read window, recurrence and error
budget. It uses 140 register gates and twelve physical register sites,
including one 561-level clock and a two-level pointer. Each Hamiltonian
term uses at most nine sites; the clock's incidence 1121 is explicitly
counted. These are not twelve qubits or two-site gates. The ideal
unfinished weight is less than (3/16)^140, and the pointer contrast is
greater than 1/100 without selecting completed runs. The note gives
explicit initial, gate or Hamiltonian, and final-effect error budgets
that preserve that contrast.

This is a smaller implementation of the prepared measurement channel in
a declared compact register encoding. The predecessor already supplied
the finite coordinate code; that code is not claimed as new. The new
result is the direct factorization and its complete counted realization.
Its clock, ready source, helpers and blank pointer are supplied resources;
they have not been prepared from thermal equilibrium. Original physical
occupation locality and the original energy Q are not inherited by
encoding positions into compact registers. The implemented pointer
coupling is part of the Hamiltonian; final classical outcome selection
and external reading retain the stated instrument premise.

## 3. A finite-source route remains testable

[ENERGY_CERTIFICATE.md](ENERGY_CERTIFICATE.md) gives a positive finite
Laurent approximation to the same original energy, together with an
exact source-specific action and finite-time error certificate. Its only
new source datum is a finite sum of original seed moments. A sufficiently
small certified error would preserve the inherited write contrast.

No passing moment instance has been computed. Finite configuration
propagation of the approximating polynomial is not a proof of bounded
physical occupation support. This conditional criterion is a precise
next test, not a completed positive energy bridge for the small device.

## 4. Sources, status and review

The prospective [CONTRACT.md](CONTRACT.md) is public at
`648148b20a14e28f4f221ccc9312834cc48f1d08`. The authoring and adversarial
reads in this session are not independent scientific acceptance. No
scientific executable, matrix enumeration, numerical search or simulation
was run. Repository integrity checks have their separate scope in
[VALIDATION.md](VALIDATION.md).

The sole public authority remains Canon v105, main/tag
`892a0b11089d34e241e1eb76d2c03247022d18e6`. Frozen source pins are:

| Source | Pin | Used scope |
| --- | --- | --- |
| [PR1777](https://github.com/mathorn1973/twist-j/pull/1777) | `191ab035be823bd9d6fdc9effba81528fa026e49` | Active source identities, complete preparation, finite-coordinate agreement, extension/compression boundary |
| [PR1772](https://github.com/mathorn1973/twist-j/pull/1772) | `3abf054e435e31c51e6e50528b09fe3cf7cffe13` | Fixed positive Borel logarithm, free strong limit and transverse spectral cut |
| [PR1774](https://github.com/mathorn1973/twist-j/pull/1774) | `3de02b0eb898f1756e3626ee2881d596c72d0094` | Comparison boundary: earlier finite-prefix spectral construction is distinct and not reproduced here |
| [PR1770](https://github.com/mathorn1973/twist-j/pull/1770) | `e23b0a08ed24667dfbedf948588211f977428d8e` | Comparison boundary: separate two-use review is preserved, not transferred |

All predecessor branches and files are unchanged. The proofs here do not
accept the pending active-source premises, promote any Canon claim,
derive the original six-pentit preparation, establish an incoming-unbound
capture experiment, identify a particle species, or supply renewed
unlimited operation. The energy no-go is a scoped negative result; the
compact construction is a scoped positive result; the finite-source
certificate has no claimed passing instance.
