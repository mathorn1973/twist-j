# Two recurrent writes select different operations at the same H3 receiver

**Candidate C, finite L1 computation.** On the original rank-43 trajectory, site 1 produces two different material words by repeating two native B2 writes. Both words remain intact at site 1 until contact C with site 2. Each contact changes both material rails at site 2. With the same four pre-C receiver rails, matching bit and incoming radiation, site 2 executes B1 on the first encounter and B2 on the second. The trajectory runs solely under the original C and B updates. [Exact records](EXPECTED.txt) · [Preregistration](PREREG.md)

## The two encounters

The table gives the first rail of each ordered material pair $(a,-a)$ in the basis $(1,j,j^2,j^3)$. Both reads use the directed edge $1\to2$ with matching bit one. The times are counted from the same launch.

| Earlier identical B2 episode | Repeated B2 emission | Emitted word $a$ | Read | Receiver material after C | Operation | Receiver material after B |
| ---: | ---: | --- | ---: | --- | --- | --- |
| 7,316,785 | 7,390,473 | $(0,0,0,2)$ | 7,390,475 | $(0,0,1,2)$ | B1 | $(1,-1,0,1)$ |
| 8,176,761 | 9,915,381 | $(0,-2,0,-2)$ | 9,915,383 | $(2,-1,1,1)$ | B2 | $(1,0,1,2)$ |

At each emission, the earlier occurrence matches the writer, matching bit, all four pre-C writer rails, ordered upstream donor material, incoming radiation and ordered material output. At all four writer events the upstream contact moves material at both ends and B2 changes the writer's material. Each emitted pair stays at site 1 through C and B of the intervening tick and is present there immediately before the receiving contact two ticks after emission. The two events have different histories outside the matched local inputs. In particular, site 2 is also site 1's upstream material neighbor on the two emission ticks.

## What selects the branch

Both times site 2 starts with ordered material $\pm(2,2,2,2)$ and radiation rails $(4,2,4,2)$ and $(3,2,0,4)$. Its two radiation rails after C are $(4,2,4,2)$ and $(6,2,2,4)$ in each encounter. C gives different material half-differences $d_1=(0,0,1,2)$ and $d_2=(2,-1,1,1)$, with identical nonzero radiation half-difference $f=(-1,0,1,-1)$.

Let $s=j^2+j^3$, so $s^2=1-s$, let $h(x)=x\bar x$, and put $\Theta=h(J)=2+s$. The two branch tests can then be checked directly in the real subfield.

| Read and operation | Material norm | Common radiation norm | Exact branch equality |
| --- | --- | --- | --- |
| 7,390,475, B1 | $h(d_1)=3-2s$ | $h(f)=4+s$ | $(2+s)(3-2s)=4+s$ |
| 9,915,383, B2 | $h(d_2)=9+5s$ | $h(f)=4+s$ | $(2+s)(4+s)=9+5s$ |

## Coverage and scope

The registered search stopped on its first launch, rank 43, after 9,915,383 ticks. The native scan counted 784,474 repeated B2 writes meeting the full source predicate and 3,222 encounters at which a held recurrent output changed the receiver's material at C and the receiver changed it again at B. These are counts through the stopping tick. The inverse recovered the original complete launch and matching. The other 84 launches were outside the executed search after that stop.

The [preceding census](https://github.com/mathorn1973/twist-j/pull/2047) recorded zero pairs with two recurrent sources and two material transfers within its shorter horizons, including the first 1,048,576 ticks on rank 43. Both new reads occur beyond that horizon. They come from writer 1, distinct from the earlier functional-renewal experiment at writer 28. This witness establishes existence on one finite H3 trajectory. Q9 stays open. [Execution and reproduction](RUN.md)
