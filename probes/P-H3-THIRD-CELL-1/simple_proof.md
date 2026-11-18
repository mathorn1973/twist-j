# A two-tick native switch in column 5

All coefficient tuples use the basis \((1,j,j^2,j^3)\). Let \(\rho=j^2\), \(J=1+\rho\), \(h(z)=z\bar z\), and \(\theta=h(J)\). At an admitted contact the second site's output on a rail with resident value \(a\) and first-site value \(b\) is
\[
P(a,b)=\frac{(1+\rho)a+(1-\rho)b}{2}.
\]
Different coefficient parity leaves the two words unchanged.

## Launch encoding and the first write

Choose writer output half-gaps \(o_+=jJ=(0,1,0,1)\) and \(o_-=\rho^3 o_+=(-1,-1,0,-1)\). Both have norm \(\theta\). B2 requires incoming matter half-gaps \(Jo_+\) and \(Jo_-\) to produce them. Let the writer's initial matter pair be \((u,-u)\) and the input site's pair be \((\pm s,\mp s)\). At tick 1 the ordered contact runs from \((5,3)\) to \((5,0)\). Solving the sum and difference of \(P(u,\pm s)=Jo_\pm\) fixes
\[
u=o_++o_-=-1,\qquad (1-\rho)s=J(o_+-o_-),\qquad s=(3,0,2,2).
\]
Both signs of \(s\) have the same parity as \(u\). The admitted contact gives matter half-gaps \((1,1,0,2)\) and \((-2,-1,-1,-2)\).

Choose writer radiation half-gap \(J\) and midpoint \(J+j\). Its launch CLK and CORR are \(2J+j=(2,1,2,0)\) and \(j\). CLK has odd coefficients and its vertical partner is zero. CORR has odd coefficients and its horizontal partner in column 6 is zero. Both contacts refuse. The radiation half-gap has norm \(\theta\), and both matter half-gaps have norm \(\theta^2\). B2 writes \((o_+,-o_+)\) and \((o_-,-o_-)\) on the two forward runs. In both it writes CLK \((J+j)+J^2=(1,0,2,-1)\).

## The second tick uses the same prepared reader

Choose reader matter pair \((v,-v)\) with \(v=(-1,-1,0,1)\), and CORR \(-j\). The desired incoming radiation half-gap is \(f=J+j\). With CORR fixed this requires CLK \(c=2J+j\) at 2 C. Solving \(P(a,(J+j)+J^2)=c\) gives the reader's launch CLK \(a=(1,0,0,-1)\). Its parity matches the writer's outgoing CLK.

At 1 C the reader's matter rails and CLK refuse contact against the empty site \((5,2)\). CORR refuses contact against the empty site in column 6. The reader's radiation half-gap at 1 B is nonintegral, so the whole reader stays at its prepared state. At 2 C the horizontal CORR partner lies in column 4, which is still empty. CORR stays at \(-j\) and the shared incoming radiation half-gap satisfies \(h(f)=\theta^{-1}\).

At 2 C the bit selects the ordered contact from \((5,0)\) to \((5,1)\). The parity of \(o_+\) differs from \(v\), so the plus arm keeps its half-gap \(v\). The parity of \(o_-\) agrees with \(v\), so the minus arm reads \(P(v,o_-)=-j\).

| Launch input | Reader matter half-gap at 2 C | Hermitian norm | Branch at 2 B | Output matter half-gap |
| --- | --- | --- | --- | --- |
| \(+s\) | \((-1,-1,0,1)\) | \(\theta^{-2}=(2,0,-3,-3)\) | B1 | \(Jv=(0,-1,-1,0)\) |
| \(-s\) | \(-j\) | \(1\) | B2 | \(-j/J=(0,0,1,1)\) |

Both B branches materially change the reader. They have the same four pre-C reader rails and the same post-C radiation. Exchanging the two exact writer pairs at 1 B leaves its radiation and every other rail fixed. Equal pair norms and zero matter sum conserve \(M,U,H,Q\). The exchange is its own inverse. With readiness fixed, either exchange produces the opposite reader outcome.

## Funding and scope

Use the initially empty site at index 6 as the fixed bank, with four rail values \((-5,1,-1,-3)\), \((-4,1,-1,0)\), \((-1,0,-2,5)\), and \((-1,0,-3,5)\). The bank is a choice of exact funding stock. Together with the new writer, reader and input it adds \(M=(-9,2,-2,-3)\), \(U=(1,1,-3,9)\), \(H=(193,0,58,58)\), and \(Q=328\) to either bare arm. Added to the bare account these give the target \(Q=774\) ledger. Swapping the input rails preserves the launch account.

The 85 bare inputs vary only in CORR words at indices \(0,1,4,5,8,9\). All six are preserved at launch. Columns 3, 4 and 6 start empty. The bit-1 horizontal pairing between columns 3 and 4 keeps column 4 empty through 1 B and therefore shields the reader's 2 C CORR input from the varying words. The bank in column 1 is outside these two-tick dependencies. The argument applies to both encodings for any of the 85 bare clocks in column 5. The column-7 comparison has different horizontal neighbors and is empirical.
