# C-TM-SYM2-HADAMARD-CHARACTER-1-N result

```text
STATUS:       NON-CANONICAL
ISSUE LOCK:   #372
PUBLIC BASIS: Public Canon v46
RESULT:       candidate-T L5 character lemmas; DIAGNOSTIC, no L6 advance
PUBLIC ROWS:  unchanged
```

## 1. Quotient is exactly the Hadamard square

The public inputs give

```text
|W| = 48,
G = ker(chi_Q) intersect ker(chi_F),
|G| = 12.
```

For

```text
chi=(chi_Q,chi_F): W -> C2 x C2,
```

the kernel is exactly `G`. By the first isomorphism theorem,

```text
|im chi| = |W|/|G| = 48/12 = 4.
```

The codomain also has order four, so `chi` is onto and

```text
W/G ~= C2 x C2.
```

Relative to the already frozen characters, the four quotient classes are canonically labeled

```text
(++), (+-), (-+), (--).
```

[NON-CANONICAL candidate-T] No selector representative is involved in this quotient statement.

## 2. H4 is the exact character table

In the frozen class order,

```text
H4 = [[1, 1, 1, 1],
      [1, 1,-1,-1],
      [1,-1, 1,-1],
      [1,-1,-1, 1]].
```

Its rows are exactly

```text
1,
chi_Q,
chi_F,
epsilon_read=chi_Q chi_F.
```

Exact integer multiplication gives

```text
H4 H4^T = 4 I4,
H4^-1 = (1/4) H4.
```

Thus Hadamard here is not an analogy. It is the Fourier transform of the registered quotient `W/G`.

## 3. Four canonical rational projectors

For a `G`-invariant class vector `f` and character row `v_chi`, define

```text
hat f_chi = (1/4) v_chi^T f,
P_chi     = (1/4) v_chi v_chi^T.
```

Then exactly

```text
P_chi^2 = P_chi,
P_chi P_psi = 0  for chi != psi,
sum_chi P_chi = I4.
```

In particular,

```text
P_epsilon = (1/4)
 [[ 1,-1,-1, 1],
  [-1, 1, 1,-1],
  [-1, 1, 1,-1],
  [ 1,-1,-1, 1]].
```

Because both `f` and the characters are constant on each `G` coset, the same coefficient computed as an average over all 48 selectors equals the four-class coefficient. Arbitrary permutations of the 12 representatives inside any class do nothing.

[NON-CANONICAL candidate-T] `P_epsilon` is a representative-free orientation projector relative to the already registered character pair `(chi_Q,chi_F)`.

This is canonical only relative to those frozen characters. It does not prove that the characters themselves are the unique physical choice.

## 4. Current selector-independent outputs are purely trivial

For any selector-independent scalar component `X`, the quotient class vector is

```text
(X,X,X,X).
```

Therefore

```text
(1/4) H4 (X,X,X,X)^T = (X,0,0,0)^T.
```

Apply this componentwise to the two registered common mathematical outputs:

```text
nu_s(v_i)=1/6,
M_s=(1/3)P1+(2/15)P5.
```

Their `chi_Q`, `chi_F`, and `epsilon_read` components all vanish. The public mathematical `1/6` image carries no selector-orientation information.

This is not a physical-measure statement. It is the opposite: it proves that the already selector-independent mathematical output cannot be used to reconstruct the retained orientation bit.

## 5. Epsilon blindness is weaker than full selector independence

For a general class vector

```text
f=(a,b,c,d),
```

the orientation coefficient is

```text
hat f_epsilon = (a-b-c+d)/4.
```

Hence equal averages on the two epsilon fibers,

```text
a+d = b+c,
```

force only

```text
hat f_epsilon = 0.
```

They do not force `hat f_Q` or `hat f_F` to vanish. Exact witness:

```text
f=(3,5,7,9)
H4 f / 4 = (6,-2,-1,0).
```

This matters for the existing spectral-coherence result. The registered common characteristic polynomial is fully selector-independent, so all three nontrivial H4 modes vanish. The frozen battery is stated only not to separate the two `epsilon_read` classes; at that weaker scope H4 certifies only the vanishing of its epsilon component. No stronger conclusion is imported.

## 6. Linear orientation-source no-go for current common outputs

Hadamard is invertible. Therefore it cannot create a nonzero orientation mode from data whose `epsilon_read` coefficient is already zero.

Consequently, any future **linear** construction that consumes only the currently registered selector-independent outputs `nu_s` and `M_s` remains in the trivial H4 isotypic component. It cannot supply the retained orientation required by `TM-SYM2-PHYSICAL-MEASURE [O]`.

[NON-CANONICAL candidate-T, frozen input scope] A nonzero physical orientation channel requires additional L5 data with a nonzero epsilon component, or a separately typed nonlinear construction. The current common mathematical image is insufficient as the sole linear source.

This is a localization theorem, not a physical no-go.

## 7. Physical-measure bar

The open public row still lacks a successor L5 source, allowed action/coherence law, physical Born carrier, total L5-to-L6 map, normalization, and complete dependency graph. H4 supplies none of them.

The retained orientation type `epsilon_read` was already explicit in the public row before this incubation. Producing its projector is useful algebra but is not closure of a previously missing premise.

Therefore the preregistered `ADVANCE` bar is not met.

## 8. Decision

```text
G1  PASS        W/G ~= C2 x C2
G2  PASS        H4 exact character table
G3  PASS        four rational representative-free projectors
G4  PASS        common 1/6 and M_s outputs are purely trivial mode
G5  NO-ADVANCE  no previously missing L5-to-L6 premise supplied
G6  PASS        epsilon blindness isolated without over-killing Q/F modes
G7  PASS        independent breaker found no L5 algebraic counterexample
```

Final decision:

```text
DIAGNOSTIC.
```

Hadamard gives a clean canonical L5 diagnostic relative to the frozen characters and pinpoints the missing object: an orientation-carrying successor L5 source. It does not advance the physical measure to L6.

## 9. What survives

The useful statement is not `Hadamard solves TM-SYM2`. It is:

```text
W/G is exactly a two-bit Fourier square.
The residual reading orientation is one exact Walsh character.
The currently common selector outputs live entirely in the trivial character.
Therefore orientation cannot be recovered linearly from those outputs.
```

That is precise, selector-free, and falsifiable at L5.

No Canon, Registry, frontier, Born, decoder, physical probability, or L6 status moves.
