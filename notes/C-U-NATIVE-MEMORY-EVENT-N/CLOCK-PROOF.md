# C-U-NATIVE-MEMORY-EVENT-N: exact clock and atom frequencies

Status: **NON-CANONICAL, candidate-T, L1 only.** This is an analytical
derivation within the frozen preregistration. It does not adopt a physical
measure or assert public promotion. The companion verifier audits the finite
identities and reports its own execution provenance. No finite sample is the
logical basis of the limiting-frequency theorem below.

## 1. The fixed-origin automatic word

Write `theta_m = popcount(m) mod 2` and

    S(0) = 0,                 S(m) = m - S(floor(m/2)),
    c_m = (m mod 5, S(m) mod 5, theta_m, theta_(m+1)).

The alphabet is `C = F5^2 x {0,1}^2`, with 100 elements. From the recurrences
for `S` and Thue-Morse,

    S(2m)   = 2m   - S(m),     theta_(2m)   = theta_m,
    S(2m+1) = 2m+1 - S(m),     theta_(2m+1) = 1-theta_m,

one obtains exactly

    c_(2m)   = T0(c_m),       T0(r,s,u,v) = (2r,2r-s,u,1-u),
    c_(2m+1) = T1(c_m),       T1(r,s,u,v) = (2r+1,2r+1-s,1-u,v).

Only the first two coordinates are reduced modulo five. The origin is
`c_0=(0,0,0,1)`, and `T0(c_0)=c_0`. Thus the length-two substitution
`sigma(c)=T0(c) T1(c)` is prolongable at `c_0`, and its infinite fixed word is
precisely `c_0 c_1 c_2 ...`.

More generally, the aligned block with indices
`a*2^j <= m < (a+1)*2^j` is `sigma^j(c_a)`. This follows by induction on `j`
from the two recurrences above, including leading zero digits. In particular,
the construction does not replace the fixed origin by a random origin.

## 2. Complete reachability and an explicit primitive certificate

Use the invertible change of coordinates `k=s+r` in `F5`. For a digit
`d in {0,1}`, the spatial part becomes

    (r,k) -> (2r+d, -k+2d).

The bit `u` is replaced by `u xor d`; digit zero sets `v=1-u` using the
unchanged `u`, whereas digit one retains `v`. In the table below, a word is
read from left to right as consecutive transitions. Since `2^4=1` in `F5`
and `(-1)^4=1`, every four-digit word has identity linear part on `(r,k)`.
Direct symbolic composition gives:

| Word | New `(r,k)` | New `u` | New `v` |
| --- | --- | --- | --- |
| `0000` | `(r,k)` | `u` | `1-u` |
| `0110` | `(r+1,k)` | `u` | `1-u` |
| `1010` | `(r,k+1)` | `u` | `1-u` |
| `1000` | `(r+3,k+3)` | `1-u` | `u` |

Consequently all 100 nominal states communicate. For clarity, explicit finite
bounds are available without discovering any graph numerically:

* From any state, apply `0000`, obtaining `v=1-u`. If `u=1`, apply `1000`
  to make `u=0`. At most four copies each of `0110` and `1010` then set
  `r=k=0`. This reaches `c_0` in at most `4+4+16+16=40` steps.
* From `c_0`, if the desired `u` is one, first apply `1000`. At most four
  copies each of `0110` and `1010` then reach any prescribed state with
  `v=1-u`, in at most 36 steps.
* A desired diagonal state `(r,k,u,u)` is the digit-one image of the unique
  spatial predecessor under the invertible map `(r,k)->(2r+1,-k+2)`, with
  predecessor bits `(1-u,u)`. That predecessor is off diagonal. Hence every
  diagonal target is reachable from `c_0` in at most 37 steps.

Let `M_ab` count digits `d` with `T_d(a)=b`. Every row of the nonnegative
integer matrix `M` sums to two. For any ordered pair of states `(a,b)`, the
paths just constructed go from `a` to `c_0` and from `c_0` to `b` in a total
of at most 77 steps. Insert as many digit-zero loops at `c_0` as needed to
make the total exactly 77. Therefore

    (M^77)_ab >= 1                 for every a,b in C.

This is an explicit primitive certificate. The graph has one strongly
connected component, its period is one, and its reachable alphabet from
`c_0` is all 100 states. A shorter certificate found by the verifier only
improves the bound; it is not needed for this proof.

## 3. Exact invariant vector

Set `P=M/2`. Define integer weights and the proposed probability vector by

    w(r,s,u,v) = 1 if u=v, otherwise 2,
    pi(r,s,u,v) = w(r,s,u,v)/150.

There are 25 choices of `(r,s)`, and the four bit pairs have weights
`1,2,2,1`, so the weights sum to 150. Both spatial digit maps are invertible.
For an off-diagonal target, its digit-zero predecessors have the two possible
old values of `v`, whose weights sum to three; its unique digit-one
predecessor is diagonal and has weight one. The total incoming weight is
therefore four. A diagonal target has no digit-zero predecessor and has one
off-diagonal digit-one predecessor of weight two. In both cases the incoming
weight is exactly twice the target weight. Thus

    w M = 2 w,                    pi P = pi.

Every entry is positive. In particular, for each `s` and `u`, summing over
the five values of `r` and both values of `v` gives

    pi(s,u) = 1/10,
    pi(s,u,v) = 1/30 if u=v, otherwise 1/15.

The next section proves that these invariant probabilities are the actual
fixed-origin letter densities. Stationarity alone would not do so.

## 4. Uniform dyadic blocks and every prefix length

Let `nu` be the uniform row probability vector on the 100 states, and let `J`
be the matrix with every row equal to `nu`. From the primitive certificate,
every entry of `P^77` is at least `2^-77`. Consequently

    eta = 100/2^77,                0 < eta < 1,
    P^77 = eta J + (1-eta) Q

for a row-stochastic nonnegative matrix `Q`. Multiplication by a stochastic
matrix does not increase the `l1` norm of a signed row vector: this follows
from the triangle inequality and the unit row sums. If that vector has zero
sum, its product with `J` is zero. Applying this observation to a probability
vector minus `pi`, and using `pi P=pi`, yields, for every letter `a` and
every `j>=0`,

    || e_a P^j - pi ||_1 <= 2 (1-eta)^floor(j/77).

The left side is exactly the distance between the normalized letter-count
vector of `sigma^j(a)` and `pi`. Hence convergence of every aligned dyadic
block is uniform in its starting letter and its position.

For an arbitrary prefix length `N`, fix `j` and partition the prefix into
complete aligned blocks of length `2^j` followed by a remainder shorter than
`2^j`. Let `F_N` be its normalized letter-count vector. The complete blocks
each satisfy the preceding bound. The remainder and an equally weighted
copy of `pi` differ in `l1` norm by at most twice the remainder's relative
length. Therefore

    || F_N - pi ||_1
        <= 2 (1-eta)^floor(j/77) + 2^(j+1)/N.

Taking `j=floor(log2(N)/2)` proves `F_N -> pi` along **all positive integer
lengths N**, not just powers of two. Equivalently, one may first fix `j`, let
`N` increase, and then let `j` increase. An arbitrary interval needs at most
two partial boundary blocks and obeys the same bound with `2^(j+2)/N` in
place of `2^(j+1)/N`, uniformly in its starting index.

In particular, every letter has positive limiting frequency, and every
letter occurs arbitrarily late. No finite clock sample, randomness
assumption, ergodicity hypothesis about an unproved measure, or selection of
the time origin enters this argument.

## 5. Pushforward to the native checkpoints

Fix any one of the 3125 inherited chart labels
`l=(alpha,beta,gamma,delta,epsilon)` and set
`w=(alpha,beta,gamma,delta)`. All formulas in this section are those frozen in
the preregistration and inherited from the sealed native-readback chart. Its
proof applies at native times `n>=3`; adding or deleting the two earlier
formal chart entries changes no limiting density.

For each `m`, the odd checkpoint at `n=2m+1` and the following even checkpoint
at `n=2m+2` are functions of `c_m`. Each parity contributes one half of native
time. This transport preserves all-length convergence: a prefix of native
time consists of complete adjacent odd/even pairs and at most a fixed number
of boundary checkpoints. For every fixed finite reading, the latter have
vanishing relative count.

Within either parity the checkpoint depends only on `(s,u)`. The phase `z`
determines `u`, and the checkpoint coordinate `r` then determines `s`:

    odd:  z=4-3u,  r=epsilon+s-1,
    even: z=1+3u,  r=-(epsilon+s-1).

Thus the ten pairs `(s,u)` give ten distinct checkpoints of each parity.
Because `pi(s,u)=1/10`, each parity-specific checkpoint has native-time
weight `1/20`. Substitution into the proposed protected vector gives

    V(x_(2m+1)) = w,              V(x_(2m+2)) = -w.

### Nonzero w

Since the characteristic is five, `w!=-w` when `w!=0`; no odd checkpoint
equals an even checkpoint. There are exactly 20 checkpoints, each with
weight `1/20`.

The odd decorated checkpoint has bit `theta_n=1-u`, independent of `v`, so
its weight remains `1/20=3/60`. The even decorated checkpoint has
`theta_n=v`. For each of its ten `(s,u)` pairs, the two possible `v` values
give weights `1/60` when `u=v` and `1/30=2/60` otherwise. Distinct parities
remain disjoint after decoration. The complete decorated atom multiset is
therefore

    10 atoms of weight 1/60,
    10 atoms of weight 2/60,
    10 atoms of weight 3/60.

### Zero w

All piston coordinates are then independent of `s,u` and parity. An odd and
an even checkpoint coincide precisely when

    u_even = 1-u_odd,
    s_even = 2-2*epsilon-s_odd       in F5.

These equations follow from equality of `z` and `r` above, and conversely
imply equality of every coordinate by the chart. They give a bijection
between the ten odd checkpoints and the ten even checkpoints. Consequently
there are ten distinct checkpoints, each of weight `1/10`.

At a coincident checkpoint, the odd decorated bit is
`1-u_odd=u_even`. Its odd weight `3/60` therefore joins the even diagonal
case of weight `1/60`. The other even bit has weight `2/60` and has no odd
contribution. The complete decorated atom multiset is

    10 atoms of weight 1/30,
    10 atoms of weight 2/30.

These formulas do not depend on `epsilon`, so they cover all 3125 chart
labels, with no choice of a label based on a target reading.

The checkpoint law depends only on the sign class `{w,-w}`, but the decorated
law retains its orientation. Explicitly let `b(1)=0` and `b(4)=1`. For
`w!=0`, the ten points with `V=w` carry decorated mass `3/60` at
`theta=b(z)` and zero at the opposite bit. The ten points with `V=-w` carry
mass `1/60` at `theta=b(z)` and `2/60` at the opposite bit. Replacing `w` by
`-w` interchanges these roles, and hence gives a different decorated law.
Different sign fibres are disjoint. There are consequently 313 distinct
checkpoint laws and 625 distinct decorated laws, the latter comprising two
orientations for each of 312 nonzero fibres and one zero law. The spectra of
attainable scalar frequencies may agree for these two orientations even
though their laws do not. Per-trajectory attainability does not authorize an
assumption that one global reader independently realizes arbitrary prescribed
rates on both orientations of the same fibre.

## 6. Positive recurrence and eventual records

The companion memory proof classifies the native invariant sign fibres and
their graph connectivity. The support just obtained is precisely the whole
fibre of `{w,-w}`: in the nonzero case it contains both oriented ten-point
sheets; in the zero case it contains the unique ten-point sheet. Every point
has strictly positive limiting frequency along every fixed chart trajectory
in that fibre. Thus every point recurs arbitrarily late along that actual
Thue-Morse trajectory, not just along some path with freely chosen bits.

Suppose a fixed checkpoint reader `f:X14->A` has an eventually constant value
`a` on one such trajectory: `f(x_n)=a` for all sufficiently large `n`. Every
point `y` of its fibre occurs after that threshold, so `f(y)=a`. Therefore
`f` was constant on the entire fibre; in particular it already had that
value at every synchronized checkpoint of the trajectory. Conversely a
reader constant on the fibre is invariant there.

This rules out a permanent blank-to-written change after synchronization for
this exact fixed checkpoint-reader class. It does not rule out information
stored by the initial choice of fibre, finite-duration changes, interventions,
larger reader classes, or an independently specified physical apparatus.

All atom frequencies above are exact densities of the registered native
word. Assigning atoms to LOW, HIGH and SILENT gives mathematical output
densities by finite addition; conditioning on nonempty acceptance divides
two such positive rational sums. Neither this operation nor the existence
of an atom assignment supplies a physical occurrence or selection rule.
