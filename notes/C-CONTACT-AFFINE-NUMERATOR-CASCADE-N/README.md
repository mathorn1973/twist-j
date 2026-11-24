# Direct affine numerator synthesis and a division-depth archive

**NON-CANONICAL / L1.** Candidate-T conditional proofs and candidate-C exact
finite audit. Public lock: [issue #1863](https://github.com/mathorn1973/twist-j/issues/1863).

Two literal integral contacts create an encoded affine numerator from a
specified coherent linear source and one common reference. A fixed zero-port
cascade then leaves the normalized odd part and an actual depth record in
the current state. There is no lookup table of individual inputs or answers.

## Supplied source and direct word

Write rho=j^2, J=1+rho, u=1-rho. For a supplied positive gain q, load

    E_q(n)=(2(q-1)u*n, 2((q-1)u+2)*n, 2J), n>0.

The first two slots are fixed linear functions of n, not precomputed
qn+1, odd part or valuation. Their joint loading is an admitted source
interface; it is not constructed here from one raw scalar slot. The
reference 2J and following zero slots are common across every input.

The chronological prefix C01 C02 gives

    active = uJ(qn+1),
    slot1 = 2[q-(q-2)rho]*n,
    slot2 = q*u^2*n+J^2.

Set D=12 and append thirteen zero ports. The entire word is simply

    C01 C02 C03 ... C0,15.

It has **15 contacts and 16 core slots**. For v=v2(qn+1)<=12 and
m=(qn+1)/2^v, its final active value is uJ^(v+1)m. The first v cascade
ports are nonzero and the remaining ones are zero. An output-only reader
obtains v from this prefix, computes J^(-(v+1))*active=u*m, and reads m
as its constant j-basis coefficient. This unit normalization is a
mathematical reader, not another physical contact gate.

The proof covers all positive n satisfying the depth bound, without an
upper bound on n. The complete core account is

    Q(E_q(n))=[40q(q-1)+32]*n^2+12,

which for q=3 is **272n^2+12**, not a common constant across inputs.
Any old disjoint archive is counted and unchanged. Its two-slot finite
audit extends the complete system to 18 slots.

## What passed

Both publicly frozen implementations independently passed:

- All 2048 odd q=3 inputs through 4095, covering depths 1..12.
- All 576 q=1..9, odd n<=127 inputs, including depth zero for even gains.
- All 225 declared occupied-archive extensions.
- The explicit q=3,n=5461 depth-limit witness, outside the positive depth
  contract; it returns DEPTH_LIMIT and remains fully invertible.
- All 2850 complete native inverses, complete state formulas, sums,
  accounts and labelled residues; all 48772 distinct primitive pair inputs
  were audited for their five-cycle and invariants.

Both independently assembled words have SHA-256
`eb37b5b2b6918571a3498b6d0badc9188d61f4511cf891dd90d17d4b7bdcc0db`.
All 2048 complete core final states agree in canonical j coordinates, with
SHA-256 `e7aa8abf1acff43fcda83141b41ee238d854386d17e716d12c0d0a1a2c9e630e`.
The breaker uses a separately written rho-basis implementation and reader;
it did not read the author code/output before its own frozen execution.
Both runs are x86_64, not a public two-architecture scientific gate.

## Exact remaining obligations

The chosen source encoding supplies the gain q. The same word supports
other q, so it does not select three or derive the Collatz law from J.
The first contact prepares 2q*u*n; the second contact performs the affine
mixing with the common reference. The chosen loading coefficients are
therefore visible premises rather than a derivation of the gain.

The old source is still present in the two leftover slots, and the reference
has changed. The output is **not** a fresh E_q(m). Repeating the same word
does not implement a second arithmetic step. Reloading this exact q=3
source has sharp necessary boundaries: fixed labelled residues obstruct
3->5, and its source account would have to increase by at least **4352**,
before any additional record cost. PROOF.md states the general bound.

Source loading, deeper divisions, occupied-bank renewal, autonomous
iteration, native U, measured energy/time, occurrence and convergence remain
unprovided. This is a direct one-pass arithmetic construction on its declared
source, not a complete recurrent physical mechanism.

## Frozen sources and replay

Public source pin for PREREG.md, verify.py, blindbreak.py and BREAK-SCOPE.md:
`0fde5621d9954ce86526eb1657e9afa1f1120fc6`. All four were publicly read back
byte for byte before their first scientific executions. Frozen sources are
unchanged. The symbolic proof did not read either new implementation.

From the repository root:

```sh
python3 notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/verify.py
python3 notes/C-CONTACT-AFFINE-NUMERATOR-CASCADE-N/blindbreak.py
```

RUN.md, EXPECTED.txt, BREAK-EXPECTED.txt and REVIEW.md retain actual evidence;
COMPARISON.json records the independent comparison. SHA256SUMS binds the
package. Ordinary required repository CI does not replay notes/ science.

The contact authority is public Canon v107 at content
f5615ed4dcdfc672dc2e468399284a1dc03ce805. This source-specific construction
is distinct from #1861 (odd-head map), #1862 (binary finite-table compiler)
and #1857 (variable-arrival apparatus). No Canon file or workflow changes.
