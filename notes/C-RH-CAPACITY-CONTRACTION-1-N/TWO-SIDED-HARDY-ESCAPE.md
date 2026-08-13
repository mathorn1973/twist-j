# TWO-SIDED HARDY ESCAPE

```text
STATUS: NON-CANONICAL generic lemma; source-bridge interpretation SUPERSEDED
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 0. Ruling after primary-source readback

The generic projection identities in this file are correct. The earlier claim
that they were needed to reconstruct the Connes--Consani prolate pair from two
Hardy half-space boundaries was wrong.

Primary-source readback shows that after the unitary map used in their
archimedean paper, `P1` is already the projection onto the two-sided interval
`[-1,1]`, and `P1_hat` is its Fourier-conjugate band projection. Their prolate
pair is therefore already a direct two-sided cutoff. See the corrected
`ARCHIMEDEAN-ESCAPE-DEFECT.md`.

Nothing below is source evidence for the Connes prolate pair. It is retained
only as a general operator lemma which may be useful for another
translation-invariant interval cutoff.

## 1. Generic interval as two ordered half-space boundaries

Let

```text
H_c = multiplication by 1_(-infinity,c),
C_a = H_a-H_(-a),
```

so `C_a` is the orthogonal projection onto `(-a,a)` up to null endpoints. Let
`U` be any translation-invariant unitary operator.

The complement splits orthogonally as

```text
1-C_a = H_(-a) + (1-H_a).
```

For interval input define

```text
B_L = H_(-a) U C_a,
B_R = (1-H_a) U C_a.
```

Since `C_a <= 1-H_(-a)` and `C_a <= H_a`,

```text
B_L = H_(-a)U(1-H_(-a))C_a,
B_R = (1-H_a)UH_aC_a.
```

## 2. Exact generic Pythagorean defect

The two output ranges are orthogonal, so

```text
B_a=[B_L;B_R],
B_a^*B_a=B_L^*B_L+B_R^*B_R.
```

With

```text
K_(-a)=H_(-a)U(1-H_(-a)),
K_a=(1-H_a)UH_a,
```

one has exactly

```text
B_a^*B_a
 = C_aK_(-a)^*K_(-a)C_a
   + C_aK_a^*K_aC_a.
```

**Status:** candidate-T, general projection algebra.

## 3. Translation covariance

If `H_c=T_cH_0T_c^*` and `U` commutes with translations,

```text
K_(-a)=T_(-a)[H_0U(1-H_0)]T_(-a)^*,
K_a=T_a[(1-H_0)UH_0]T_a^*.
```

Thus a generic interval escape decomposes into two translated one-sided
boundary defects.

**Status:** candidate-T.

## 4. What is withdrawn

The following earlier interpretation is withdrawn:

```text
Connes archimedean prolate defect
 = sum of two translated Hardy boundary defects.
```

It was based on misidentifying the source projection `P1` as a Hardy
half-space. In the source representation relevant to equations (62)--(70),
`P1` is already the interval projection and no such reconstruction is needed.

No conclusion about the relation between the generic lemma above and the source
prolate operator is retained without a new exact intertwining theorem.

## 5. Current use, if any

This lemma may still be used for the independent Suzuki/Paley--Wiener carrier
if that carrier is represented directly as a physical interval cutoff for a
translation-invariant convolution operator. Such use requires its own
normalization map and may not cite the Connes prolate equations as support.

The active source-comparison gate is now `ARCHIMEDEAN-GAUGE-DELAY` in
`ARCHIMEDEAN-ESCAPE-DEFECT.md`.
