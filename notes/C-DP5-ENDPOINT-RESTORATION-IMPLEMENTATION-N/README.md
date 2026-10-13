# Independent endpoint-restoration implementation

**NON-CANONICAL / L1 / lane B.** Apache-2.0, A. M. Thorn, 2026-10-13.
Design reservation [#1487](https://github.com/mathorn1973/twist-j/issues/1487).

The candidate implementation and self-contained arithmetic proof now live
in [P-DP5-ENDPOINT-RESTORATION-1](../../probes/P-DP5-ENDPOINT-RESTORATION-1/README.md),
reserved separately as [#1488](https://github.com/mathorn1973/twist-j/issues/1488).
They implement the target in the predecessor
[B design](../C-CLASSICAL-SIGNED-PORT-CONTRACT-N/RESTORATION_CERTIFIER.md).
The formal preregistration, source pin and first outcome govern execution.
No successful restoration is claimed by this implementation note.

[CUSTODY.md](CUSTODY.md) records the newly closed serialized-input content
and actual final-campaign receipt association. The implementation uses
directed 192-bit dyadic integer intervals, exact degree-8 normal ordering,
degree-256 scalar remainder bounds and all 720 pair/column slots.

Validity of the supplied branch alpha/Phi intervals and the inherited
propagation-error account remain premises. This work neither reruns the
old propagation nor supplies the native-to-classical source/contact bridge.
