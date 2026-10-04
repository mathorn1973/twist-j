# Arbitrary finite paid banks for the admitted trace exchange

**NON-CANONICAL, L1 candidate-T, proof-only. No public authority or status promotion.**

This note is prepared under the prospective reservation [C-U-TRACE-CONTACT-CERTIFICATE-N, #1356](https://github.com/mathorn1973/twist-j/issues/1356). The proposed consequence was exposed symbolically before this note; it is not a new experimental discovery. No new scientific program was executed for this result. Any later finite implementation audit requires its own applicable source freeze and does not replace the proof below.

The source construction is [#1355](https://github.com/mathorn1973/twist-j/pull/1355), pinned to head [`2bd0b048d5e01d7d5bf260dbada338e4089b04b8`](https://github.com/mathorn1973/twist-j/commit/2bd0b048d5e01d7d5bf260dbada338e4089b04b8). Its admitted trace exchange, consumed sources, native quotient and fixed reader are retained. The extension supplies arbitrarily many, but beforehand finitely many, sequential contacts. It supplies neither a reset nor a physical realization of the exchange.

## 1. Complete cell law and admitted exchange

Write a native cell as

`psi=(p1,p4,p1p,p4p,q,r)=(P,q,r) in F5^6`,

and set `kappa=sum(P)`, `z=kappa+q+r`, `A=p1+p1p`, `B=p4+p4p`, `W=A^2`. All cell and source arithmetic below is in F5. Counter indices, operation counts and the integer-valued target `c(a)=floor((a+1)/5)` use ordinary integers, with `a in {0,1,2,3,4}`.

The exact native generators, in selector order `a,b,c,d,e`, are

```text
g_a(psi) = (p4,p1,p4p,p1p,q,r),
g_b(psi) = (-p1p,-p4p,-p1,-p4,-q,-r),
g_c(psi) = (2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
g_d(psi) = (2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
g_e(psi) = (2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

Let `theta_n=popcount(n) mod2` and `T_n(psi)=g_((z(psi)+2theta_n) mod5)(psi)`. Thus the selector is evaluated on the actual cell state, never replaced by a manually chosen word.

The one additional primitive is

```text
C(s,(P,q,r)) = (kappa+q+r, (P,s-kappa-r,r)).
```

In the bijective chart `(P,q,r) <-> (P,z,r)` it swaps `s` and `z`. It is therefore an involution on its complete seven-pentit domain and preserves `P,r,A,B`. This is an admitted operation and interface, not a derived native word, physical port or elementary two-body coupling.

## 2. Readiness, writing and retention lemmas

The complete native coordinate laws give the closed quotient

| Generator | z after | A after | B after |
|---|---|---|---|
| a | z | B | A |
| b | -z | -A | -B |
| c | 2-z | 4-A | 2-B |
| d | 2-z | -A | -B |
| e | 3-z | -A | -B |

For `z in {1,4}`, control zero selects `b` or `e`, and control one selects `d` or `b`. Hence, independently of the other coordinates,

```text
z after = 4 for control zero, 1 for control one;
A after = -A; B after = -B; W after = W.
```

Consequently `X14={z in {1,4}}` is invariant. The ready condition `A=B=0` is invariant within it, while every previously written value of `W` is retained there. This concerns the fixed reading; the complete receiver continues to evolve.

For any full cell and three actual successive driver bits `011`, the selected chronological words and resulting quotient are

| Initial z | Selected word | Final z | Final (A,B) |
|---|---|---|---|
| 0 | a,c,e | 1 | (B+1,A+3) |
| 1 | b,b,d | 1 | (-A,-B) |
| 2 | c,c,e | 1 | (-A,-B) |
| 3 | d,b,d | 1 | (-A,-B) |
| 4 | e,b,d | 1 | (-A,-B) |

Each row follows by substituting the quotient table into the next native selector. Thus a cell with `A=B=0` and `z=a+1` reaches `X14` with `W=c(a)` after three steps. No assumption on the remaining individual coordinates is needed. A displayed `W=0` alone is insufficient; both ready sums are specified.

For complete passive readiness data, define the six-coordinate sequence

```text
rho_0=(0,0,0,0,1,0),
rho_(n+1)=T_n(rho_n)=(P_(n+1),q_(n+1),r_(n+1)).
```

This recurrence and the displayed full generators specify every unused receiver state, not just its projection. The lemma proves `A(rho_n)=B(rho_n)=kappa(rho_n)=0` for all n, and its trace is

```text
beta(0)=1,
beta(n)=z(rho_n)=4-3theta_(n-1) for n>=1.
```

## 3. An explicit nonoverlapping contact calendar

For `k>=0` set `t_k=8k+4theta_k`. Its binary form is the binary form of k followed by `theta_k00`. The appended parity bit cancels the parity of k, while adding one or two introduces exactly one further set bit. Therefore

```text
(theta_(t_k),theta_(t_k+1),theta_(t_k+2))=(0,1,1).
```

Furthermore `t_(k+1)-t_k=8+4(theta_(k+1)-theta_k)` lies in `{4,8,12}`. Retain the first two contacts of #1355 and enumerate

```text
{0,6} union {t_k:k>=1} = {0,6,12,20,24,36,40,48,...}
```

as `tau_1,tau_2,...`. Explicitly, `tau_1=0`, `tau_2=6`, and `tau_i=8(i-2)+4theta_(i-2)` for `i>=3`. The bits at `6,7,8` are also `011`. The first two gaps are six and every later gap is at least four, so each three-step writing interval completes before the next contact.

## 4. Finite-bank theorem and proof

For every beforehand chosen `m>=1`, admit the complete carrier

```text
Omega_m = N0 x F5^m x (F5^6)^m
```

with state `(n,s_1,...,s_m,psi_1,...,psi_m)` and preparation

```text
(0,a_1+1,...,a_m+1,rho_0,...,rho_0).
```

All `5^m` source tuples are allowed. The receiver preparation is common and source-independent. All source ports are supplied and counted at the initial boundary; the theorem does not supply a later physical arrival or reloading mechanism.

At boundary n, apply `C` to `(s_i,psi_i)` if `n=tau_i` for `1<=i<=m`, leaving every other factor unchanged during this stage. Otherwise apply no exchange. Then update EVERY receiver by `T_n` on its post-exchange state, retain all source slots, and increment n. This is one autonomous discrete map on the displayed carrier. The fixed address law is admitted as part of that map. Intermediate exchange snapshots do not assert zero physical interaction time.

**Claim.** For every input tuple and every i,

```text
W(psi_i(n))=c(a_i) for every boundary n>=tau_i+3.
```

**Proof.** Before its contact, receiver i is exactly `rho_n`, since earlier exchanges address other factors only. Its source slot still holds `a_i+1`. At the contact, `C` preserves `A=B=0`, gives the receiver trace `a_i+1`, and exports its old trace to the source slot. Section 3 supplies the next three actual driver bits `011`, so section 2 proves the claim at `tau_i+3` and puts the receiver in `X14`.

Induct over subsequent updates. No later exchange acts on receiver i, and every native update preserves its `W` in `X14`. Equivalently, induct over contacts: every earlier record survives the exchange stage untouched and the native stage by invariance; the next unused receiver follows the common ready trajectory until it writes. The nonoverlapping intervals ensure each earlier write is already protected. These arguments use no particular source values and therefore cover all `5^m` tuples without their enumeration. Each full receiver trajectory depends only on its own source value and the fixed clock/calendar. QED.

## 5. Complete source exports and noninjectivity

The algebraic exchange snapshot at `tau_i` is exactly

```text
(a_i+1, rho_(tau_i))
    -> (beta(tau_i), (P_(tau_i),a_i+1-r_(tau_i),r_(tau_i))).
```

Here `kappa=0`, and all displayed cell coordinates are retained. Slot i holds `a_i+1` through its pre-contact boundary `n=tau_i`, then holds `beta(tau_i)` immediately after the exchange and at every boundary `n>=tau_i+1`. In particular the source exports at contacts `0,6,12,20,24,36,40,48` are respectively `1,4,1,1,4,1,4,1`. They are source-independent but remain part of the complete state.

The complete protocol is noninjective for every m. At the first contact, choose `a_1=0` or `a_1=1` and fix all later inputs identically. Slot 1 becomes 1 in both cases. The actual words `b,b,d` and `c,c,e` give the identical full receiver endpoint `(2,1,3,4,0,1)` at boundary 3. Every other source, receiver and the counter agree there as well. The complete enlarged states have merged and remain equal thereafter. The involution property of the added C does not imply reversibility of the subsequent state-selected native evolution.

## 6. Resources, finite-bank meaning and archive boundary

The bank uses `m` source pentits, `6m` receiver pentits, `m` addressed exchanges, the common initial preparation and the source-independent address calendar. At each fixed counter its complete carrier has `5^(7m)` states. Its last completion boundary is

```text
N_1=3; N_2=9;
N_m=tau_m+3=8m-13+4theta_(m-2) for m>=3.
```

Through that boundary EACH receiver has executed `N_m` actual native transitions: `mN_m` cell updates in total, in addition to the m exchanges. All receivers continue evolving afterward.

The factor `N0` is an explicitly unbounded counter. Thus this is a finite bank, or finitely many payload coordinates under the admitted unbounded clock, NOT a finite-state autonomous machine. Neither the preparation cost, hardware address selection, computation of the driver, clock realization nor all-time operation has been physically made free by writing a discrete transition law.

Every receiver is used once. No used cell is reset, no new receiver is supplied after initialization, and no infinite independent input stream is realized. All-future retention refers to the mathematical native continuation and the fixed reader, not protection against arbitrary interventions, noise or physical readout disturbance.

At a common time independent of the inputs, retaining every possible m-bit history requires at least `2^m` distinguishable memory states: select `a_i=0` or 4 to obtain each binary output tuple, and distinct tuples cannot share the same memory state under a fixed reader. If all available history-bearing memory has only D states, `2^m<=D` is necessary. The common counter has the same value for every history and does not remove that bound. Thus indefinite preservation of arbitrary independent records requires a growing archive or record export into a counted environment. Renewing a working receiver and retaining the archive are different obligations.

## 7. Ownership and exact scope

- [#987](https://github.com/mathorn1973/twist-j/issues/987), particularly [its proof/outcome](https://github.com/mathorn1973/twist-j/issues/987#issuecomment-5652509288), already owns the native carry write, fixed squared-pointer retention, source mergers, readiness qualifications, conditional fresh banks and reset boundary. This note does not claim the first general memory-bank construction.
- [#993](https://github.com/mathorn1973/twist-j/issues/993), particularly [its final proof record](https://github.com/mathorn1973/twist-j/issues/993#issuecomment-5655461040), owns the native-factor and already-running-reservoir freshness boundaries. Here an unused receiver may already be synchronized; its later write is enabled by the expressly added C, not by waiting or merely renaming that receiver.
- [#996](https://github.com/mathorn1973/twist-j/issues/996) owns added rearming/exchange programmes, repeat/retention distinctions and archive limitations. #1355 also preserves the neighboring ownership of #994, #998 and #1003; nothing here claims a first exchange, native port, or complete readiness-family classification.

The narrow extension is arbitrary finite sequential composition of the pinned #1355 scalar/trace exchange with the original contacts 0 and 6 retained, all receivers evolving from time zero, explicit source exports and protection of every earlier reading. Sources are consumed. No source-preserving SUM, closure of #1349, native synthesis of C, energy function, elementary interaction, spatial locality, physical controller, reset, occurrence semantics or indefinite renewal is supplied.
