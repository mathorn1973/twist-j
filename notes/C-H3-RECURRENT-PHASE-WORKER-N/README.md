# Recurrent H3 phase worker

**NON-CANONICAL, L1.** In two finite preparations of an \(8\times20\) native
H3 torus, the port and time of the first change to a passive matter pair
identify all 85 ready phases of a four-row clock. Each preparation recurs after
3110 native ticks. The second stock choice gives a nonzero local scalar
matter change at every passive transfer. These are result-exposed finite
checks with exact arithmetic.

## Native law and four-row clock

Use \(O=\mathbb Z[j]\) with \(j\) a primitive fifth root of unity. Write
\(\rho=j^2\), \(J=1+\rho\), \(I=J^{-1}\), \(h(z)=zz^*\),
\(\phi=-(\rho+\rho^{-1})\) and \(\theta=h(J)=2-\phi\). The four rails
at each site are \((r_0,r_2,\mathrm{CLK},\mathrm{CORR})\).
A tick has three stages.

1. Transport the first three rails vertically and CORR horizontally. On each
   rail, the oriented matching starts at bit \(p\) and pairs \(p+2k\)
   with \(p+2k+1\) modulo its even length. A pair \((a,b)\) is unchanged
   if \(a-b\notin 2O\). Otherwise keep its midpoint and rotate its
   half-difference by \(\rho\).
2. Apply \(B\) at every site. If either rail difference is outside \(2O\),
   leave the site fixed. Otherwise write \(d=(r_0-r_2)/2\) and
   \(f=(\mathrm{CLK}-\mathrm{CORR})/2\). Keep both midpoints. Branch
   \(B_1\) replaces \((d,f)\) by \((Jd,If)\) if \(d\ne0\) and
   \(h(f)=\theta h(d)\). Otherwise \(B_2\) replaces \((d,f)\) by
   \((Id,Jf)\) if \(f\ne0\) and \(h(d)=\theta h(f)\). The remaining
   sites stay fixed.
3. Flip \(p\). The inverse first recovers \(p\), applies \(B\) again,
   then transports with multiplier \(\rho^{-1}\) at the recovered bit.

The [public H3 law](../../canon/CANON.md#1-the-whole-native-state-and-its-exact-law)
gives the conservation proof for the full sums \(Q_m,Q_r\) of the
matter and field rails and the full norm sum \(Q_h\). The scalar account
is \(Q=\mathrm{Tr}_{\mathbb Q(j)/\mathbb Q}(Q_h)/2\).

For the \(8\times4\) clock use bit zero, put \(P=2J\) and set
\[
b=J-\rho^2-2\rho J(2+\rho+\rho^2).
\]
The table specifies the complete seed.

| Sites | Rails |
| --- | --- |
| \(x=0,\ y=0,1\) | \((P,-P,1,-3)\) |
| \(x=0,\ y=2,3\) | \((P,-P,1,b)\) |
| \(x=1,\ y=0,1\) | \((0,0,0,-3)\) |
| \(x=2,\ y=0,1\) | \((0,0,0,5)\) |
| All other sites | \((0,0,0,0)\) |

Its norm sum is \(270-94\phi\), with scalar \(Q=446\). Define the
85 literal ready fields \(R_k\), \(0\le k<85\), by acting on the
three source CORR coordinates at \(x=0,1,2\) in both duplicate rows.
Start from \((-3,-3,5)\) and take \(k\) iterations of the two-contact
word left then right, with the native parity guard. Fix all other
seed coordinates and keep bit zero. This contact-only word enumerates
the inputs. The actual first-return map includes the collisions.

The check enumerates 85 distinct fields before the contact-only word
closes. For the native trajectory, raw marks are \(0,21,42,63,84\).
Away from a mark the next ready field is \(R_{k+1}\) after two ticks.
For \(k>0\) put \(g=\lceil k/21\rceil\), \(u=21g-k\), and for
\(k=0\) put \(g=u=0\). The arithmetic label of \(R_k\) is
\[
\sigma(k)=21(2g\bmod5)-u\pmod{85}.
\]
Reading labels in \(0,\ldots,84\), the native ready order increments by
one modulo 85. The first-return durations at labels \(0,21,42,63,84\)
are \(72,72,174,72,72\); the other 80 durations are two ticks. The
complete four-row field including the bit first returns after 622 ticks.
These trajectory facts are checked by exact execution from the literal
seed.

## Five paid ports

Repeat the four-row seed five times on one torus of height 20,
retaining all cross-group matching edges and the wrap. Add stock only
at column 1 and preserve its CORR. For port \(i=0,\ldots,4\), set
\[
F=1025,\qquad m_i=\rho^i,\qquad
v=-1+\rho+\rho^2,\qquad A_i=v-2J\rho^{1+3i}.
\]
A matter midpoint \(m\) and half-difference \(d\) specify rails
\((m+d,m-d)\).

| Rows at port \(i\), modulo 20 | Matter midpoint | Matter half-difference | CLK |
| --- | --- | --- | --- |
| Source \(4i,4i+1\) | \(H+m_i\) | \(JF\) | \(A_i+2F\) |
| Passive \(4i-1,4i+2\) | \(H+m_i+4\) | \(F\) | \(0\) |

The basic stock uses \(H=0\). The scalar-transfer stock uses
\(H=-2+2\rho+4\rho^2+6\rho^3+8\rho^4\). The reflected pairs in both
source copies of a port receive the same stock. The translation is even
in \(O\), so the two stocks have the same relative transport guards and
the same local resonance tests. At preparation each matter pair
contributes \(2h(m)+2h(d)\) to \(Q_h\). Summing the five copies and the
added stocks gives \(Q=3140-120F+180F^2=188992640\) for \(H=0\).
For the translation the added norm sum is \(40h(H)+80(H+H^*)\), whose
scalar contribution is 3680, giving \(Q=188996320\).

## The local comparison and passive transfer

At a marked rank \(21g\) the source at column zero writes on tick one.
The right contact exposes \(1-4\rho^{g+1}\) at column one on tick two.
The left contact on tick three combines that value with the source value
\(-3-2\rho\). Its column-one output is
\[
\frac{1-\rho}{2}(-3-2\rho)+\frac{1+\rho}{2}(1-4\rho^{g+1})
=v-2J\rho^{g+1}.
\]
It equals \(A_i\) exactly when \(3i=g\bmod5\), so \(i=2g\bmod5\).

For a head still carrying its prepared half-differences, let \(a\) be
the incoming CORR. Upon parity admission put \(\delta=(A_i-a)/2\), so
the field half-difference is \(F+\delta\). At either inequivalent
complex embedding, the nonnegative carrier norm sum \(270-94\phi\)
bounds \(|a|<19\), while \(|A_i|\le7\). Hence \(|\delta|<13\).
Branch \(B_2\) requires \(h(F+\delta)=F^2\). Taking the real quadratic
trace gives
\[
F\,\mathrm{Tr}(\delta+\delta^*)+\mathrm{Tr}(h(\delta))=0.
\]
The first term is an integer multiple of 1025 and the second is in
\([0,338)\). Therefore \(h(\delta)=0\) and \(a=A_i\).
Branch \(B_1\) would require \(|F+\delta|=\theta F\) at both embeddings,
which fails at the embedding with \(\theta>5/2\). At passive sites
\(|f|<19/2\) upon parity admission, whereas the matter half-difference
is \(F\); both resonance conditions fail there.

At equality \(B_2\) brings the source half-difference to \(F\). The
following odd matching can now rotate the difference between the source
and passive matter midpoints, leaving the common half-difference \(F\)
unchanged. In the same tick \(B_1\) restores the head's half-difference
and field rails while the passive matter rails keep their transported
values. A quiet head has the wrong matter residue for that cross.
Even matching pairs identical source rows and separates adjacent passive
ports by their distinct residues. The source CLK has nonzero residue
against the passive CLK. These guards persist as matter midpoints change
by even elements. After \(n\) productive crosses at a port, the two
midpoints, source first, are
\[
(H+m_i+2-2\rho^n,\ H+m_i+2+2\rho^n).
\]
Thus the passive midpoint changes by \(2\rho^n(\rho-1)\) even though
the head restores its prepared differences and field rails.

There are also two ordinary \(B_2\) writes per 622-tick lap, at ports 1
and 4 on ticks 212 and 220 from phase zero. These writes follow odd
right transport. At the next even matching the source copies face each
other, and the written CORR residue \(1+\rho^2\) refuses the left
clock edge against residue \(1\). The head inverts before it faces its
passive partner. A productive write follows even left transport and the
odd matching reaches the passive partner before restoration. The work
observable is a change in the passive matter rails.

## Phase, loading and recurrence

From \(R_k\), the clock takes \(u\) ordinary two-tick advances to the
next mark. The first passive change is at port \(i\) and delay \(D\)
given by
\[
i=2g\bmod 5,\qquad D=2u+4,\qquad
\sigma(k)=21i-(D-4)/2\pmod{85}.
\]
The 85 pairs are \((0,4)\) and all combinations of ports 1 through 4
with even delays 4 through 44. Both address and arrival time are
observed features of the native evolution. The formula interprets the
observations after the fact.

The recurrent run starts once at the seed. At raw ready ranks 15 and
19 the corresponding loaded cut already carries an ordinary head
write. Directly supplying blank heads at those bare ready fields
erases that state. The first measured moves then become \((1,2)\)
and \((4,2)\), in place of \((2,16)\) and \((2,8)\).
For arbitrary fresh input, supply the bare clock's immediately preceding
cut at bit one, attach the same blank stocks and take one native tick
before timing. This step performs no passive work and lets the two
ordinary writes enter the loaded state. The check reconstructs each
predecessor with the bare inverse and tests all 85 preparations.

There are nine productive crosses per port on each 622-tick lap. The
successive midpoint values distinguish \(n\bmod5\), and \(9\) has order
five under addition modulo five. Any complete recurrence must return
the carrier first, which can be recovered at dressed head sites by
undoing the transient field substitution. Five laps restore all
midpoints and rail differences, giving least period \(5\cdot622=3110\).
The check compares the full field to the initial state at every tick
and tests the true inverse \(B\) followed by inverse transport at the
old matching bit. Conservation of all four accounts is checked after
transport and after collision.

For the translated stock let \(b_k=2k+[k=i]\). The passive midpoint is
\(\sum_{k=0}^4 b_k\rho^k+2\rho^n\). Taking the fifth-root trace of
the change in the matter-pair norm gives the local scalar change
\(20(b_{(n+1)\bmod5}-b_{n\bmod5})\). Consecutive coefficients differ
including the wrap. All 450 individual passive-site transfers are
nonzero in this stock, and their signed sum over the orbit is zero.

## What this changes for the program

The native circuit now includes a causal chain from a particular clock state through a local guard to a change in separate matter rails. On the recurrent section, one radiation coordinate already has 85 distinct values. When the output is restricted to the passive matter pairs, observing them at one common delay gives at most 21 distinct vectors over the 85 origins in a carrier lap, even when every delay in the 3110-tick period is tried. At delay 34 the count reaches 21. Measuring which receiver moves first and when it moves recovers all 85 labels. These are three different observation contracts.

The first outstanding engineering question is how to transfer a phase distinction into a small matter register at a common cut, starting with the same auxiliary stock for every input. The scalar budget bounds a single isolated collision-only register to 39 possible pairs, or nine for the chosen integral gap \(F\). Two-site matter transport is therefore a necessary design ingredient for a *single-site* material register at these budgets when the other assumptions of the bound hold. A proposed first test couples a single four-row clock to one neighboring matter pair and asks it to select raw rank 44 against all 84 controls at one fixed latency. [Capacity bound](CAPACITY.md) · [Spatial construction and proposed experiment](RESEARCH.md)

The setup gives an L1 example of reusable conditional action under the public H3 law. The five calibrated copies, ready section and interpretation of the output are specified data. The physical dictionary, charge assignments, mass scale and interaction that would generate a mass spectrum require additional arguments. The public frontier distinguishes complete apparatus, event occurrence and physical observation from an algebraic record. [Scientific scope](../../canon/CORE.md#complete-state-observation-and-funded-propagation) · [Open obligations](../../canon/FRONTIER.md)

## Reproduce the finite checks

From the repository root, run the standalone standard-library checker.

~~~text
python -B notes/C-H3-RECURRENT-PHASE-WORKER-N/verify.py
~~~

The checker uses integer cyclic convolution in a fifth-root basis. For each full cut it serializes the next matching bit followed by all 640 ring elements in the ordered basis \(1,j,j^2,j^3\), using little-endian signed 32-bit coefficients. Each trajectory digest is compared with that of a separately coded native kernel. The expected file records the digests and the reproducible summary for both preparations. [Expected output](EXPECTED.txt)

The public verifier at commit `46f34d449a68aa65493cdb4d401f0a853d3c85f1` was replayed on Linux x86-64 and Linux aarch64 with Python 3.12.3. Both runs exited zero with empty stderr and matched all 1931 expected stdout bytes. The script SHA-256 is `54b9788e21dbed4cc3e311a0bb4aa43c8d5a621f7403b81617ac40bdf3aa408a`. The stdout SHA-256 is `c4fe151e78d45495b806c814bee36664bb3cb762800511f45266246ab067ebf9`. These replays check computational reproducibility. Independent scientific review remains open.

The two preparations, finite clock carrier, port references and paid stocks
are explicit inputs. All 85 origins and the two ordinary head aliases were
known during development. This record is a result-exposed reproduction of a
finite construction. The delay is relative to the chosen observation start.
Two ready origins in the same block can refer to the same eventual transfer.
A persistent numerical phase register, a preparer that constructs the stock
from uniform data, and a general material controller remain open for this
construction.

The public context is the [native H3 law](../../canon/CANON.md#1-the-whole-native-state-and-its-exact-law)
and the earlier [finite fixed-reference H3 record](../../reproduce/h3-referenced-record/README.md).
The latter concerns its own paid reference and observation horizon. The
85-phase worker uses the new literal preparation given here.
