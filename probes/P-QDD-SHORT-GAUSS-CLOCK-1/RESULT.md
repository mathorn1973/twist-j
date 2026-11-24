# Signed rotation, clock transfer and Gauss orientation

**Status: C.** Exact finite computation on the five-point register and initialized 13-position clock defined in [the preregistration](PREREG.md). The conditional Hamiltonian identities and their assumptions are given in [the proof](PROOF.md).

| Frozen prediction | Computed result |
| --- | --- |
| Signed rotation on the original pair \((0,k)\) | All 20 signed columns matched, with each spectator fixed at amplitude \(+1\). All coefficients of the 100 matrix-unit images from those columns matched. |
| Positive-time schedule | The four lengths were 12, 12, 10 and 12. The maximum active duration was \((4+2/\sqrt5)\pi/\omega\) in the declared switched model. |
| Reverse sign placement | All four words changed to their adjoints. On \(e_0\) the point-\(k\) probability stayed \(9/25\). The positive real sum analyzer gave \(49/50\) for the scheduled word and \(1/50\) for the altered word. |
| Joint evolution | All 25 columns initialized at clock position 0 arrived at 12 with common phase \(+1\) and the intended data, including idle. All earlier positions had zero amplitude at the predicted instant. |
| Altered first link | Setting 1 still delivered its clock to 12, with data \(e_2\) from input \(e_0\). The intended data were \((4e_0+3e_1)/5\). |
| Orientation of the primitive | The real sum and difference analyzers gave \(2/25\) and \(2/5\) for both pulses. The fixed complex analyzer gave \((6+2\sqrt5)/25\) for \(U\) and \((6-2\sqrt5)/25\) for \(U^\dagger\). |

No registered falsifier fired. The [run record](RUN.md) and [captured output](EXPECTED.txt) document the deterministic reproduction. The 13 clock positions describe a transient transfer at \(T=\pi/(2\lambda)\). Its largest link has frequency \(\lambda\sqrt{42}\). The clock has a separate Hamiltonian with supplied joint gate operators. The calculation assumes a shared five-level site and an independently oriented phase reference. Physical measurements: 0. The result concerns the stated model. The origin of these controls in native dynamics and the broader QDD instrument remain open.
