# Exact lambda-six reading, inverse, and pure-J data dynamics

Status: candidate-T, NON-CANONICAL until a separate public fold. L1 arithmetic. Provisional probe `P-J-LAMBDA6-DECODER-INTERFACE-1`. This concerns multiplication by J, not realization of the native autonomous map U. The old rational-modulus-25 decoder is unchanged.

## 1. Carrier and source facts

Let `O=Z[zeta]`, `Phi5(zeta)=1+zeta+zeta^2+zeta^3+zeta^4=0`, `lambda=1-zeta`, `J=1+zeta^2`, and `phi=-zeta^2-zeta^3`. Use the ordered integer basis `(1,zeta,zeta^2,zeta^3)`. The domain is exactly

`A941={alpha in O:1<=N(alpha)<=941}`.

Zero is excluded. There is no restriction to a selected codebook or a finite range of J exponents. For `alpha=(a,b,c,d)` put

```text
u=a*a-a*b+b*b-b*c+c*c-c*d+d*d
v=a*b-a*c-a*d+b*c-b*d+c*d
A=|sigma1(alpha)|^2=u+v*phi
B=|sigma2(alpha)|^2=u+v-v*phi
N(alpha)=A*B=u*u+u*v-v*v
S0=S(alpha)=2*u+v
S1=S(J*alpha)=3*u-v.
```

The two traces recover `u=(S0+S1)/5`, `v=(3*S0-2*S1)/5`, and consequently recover the ordered positive pair A,B. J is the integral unit with inverse `-zeta-zeta^2`; its coefficient actions are

```text
J(a,b,c,d)       = (a-c+d,b-c,a,b-c+d)
J^-1(a,b,c,d)    = (c,-a+c+d,-a-b+c+d,-b+d).
```

Its squared magnitudes are `phi^-2,phi^2`, giving trace recurrence `S_(n+2)=3*S_(n+1)-S_n` for every integer n.

These identities, the original oriented strip/range proof, and the observed-reader capacity class are inherited from J-TWO-TRACE-RESIDUE-INVERSE [T] and J-OBSERVED-SCALAR-CODE-CAPACITY [T], with public source `probes/P-J-TWO-TRACE-RESIDUE-DECODER-1/PROOF.md` sections 1-7 at baseline `5e872c22a18043c8126945a982efad55472cea82`, Public Canon v97. Canonical ramification C20-TEICHMULLER-SPLIT [T] gives `N(lambda)=5` and `(5)=(lambda)^4`. Previously exposed local minimum-depth witnesses are disclosed inputs; their direct proofs appear below. None is represented as a blind prediction.

## 2. Canonical ideal digits and their carries

The residue carrier is the ring `R6=O/lambda^6 O`. Evaluation at `zeta=1` modulo 5 is a surjection `O -> F5`. Its kernel is lambda O: multiplication by lambda acts by

`(a,b,c,d) -> (a+d,b-a+d,c-b+d,2d-c)`,

and for any `x=(a,b,c,d)` with sum divisible by 5 the explicit inverse is

`x/lambda=(a-t,a+b-2t,a+b+c-3t,t)`, `t=(a+b+c+d)/5`.

Direct substitution verifies that inverse. Thus membership in lambda O is equivalent to the coefficient sum being zero modulo 5.

For any scalar x, choose uniquely `r0=sum(x) mod5` in `{0,1,2,3,4}`, subtract `(r0,0,0,0)`, and divide by lambda. Repeat six times. This gives

`x=r0+r1*lambda+...+r5*lambda^5+lambda^6*q`.

Existence follows from the exact division just proved. If two six-digit expansions represent the same ideal class, reducing their difference modulo lambda forces their first digits equal; subtract and divide, and repeat. All six digits agree. Conversely equal digits imply equal ideal classes by the displayed decomposition. Hence the digits give exactly `5^6` distinct classes. They are ordered least significant first.

The ring has characteristic 25. The ideal identities `(5)=(lambda)^4` and `(25)=(lambda)^8` imply that 25 vanishes in R6. If 5 belonged to lambda^6 O, its norm 625 would be at least `5^6=15625`, a contradiction; hence 5 does not vanish. Its characteristic divides 25 and does not divide 5, so it is exactly 25. In particular the additive order of 1 is 25. Every element of the additive group of `F5^6` has order dividing 5, so there is no additive group isomorphism between these carriers. There is only a set bijection through the six digits unless further structure is explicitly transported. Arithmetic must include the ideal-ring carries; it is not componentwise digit arithmetic modulo five.

## 3. Uniform injectivity at depth six

Define `D6(alpha)=(S0,S1,alpha mod lambda^6 O)` on A941. Suppose `D6(alpha)=D6(beta)`. Equal traces recover the same A,B. If `delta=beta-alpha` is nonzero, the triangle inequalities at the two complex embeddings give

`N(delta)<= (2*sqrt(A))^2*(2*sqrt(B))^2 =16*N(alpha)<=15056`.

Equal residues instead give `delta=lambda^6*eta` with nonzero integral eta, whence `N(delta)=15625*N(eta)>=15625`. This contradiction proves alpha=beta. More generally the same proof works at depth k and norm bound X whenever `5^k>16X`. Only X=941 and depth six are implemented here.

This is the previously exposed norm argument, applied to the ramified ideal. It proves uniqueness but does not by itself recognize the image of D6. The next sections supply total image recognition.

## 4. Data steps and their exact inverses

A well-formed datum consists of two arbitrary exact integers and six canonical digits. Positivity and representability are not requirements for applying a data step. Define

```text
T6(s0,s1,r)         = (s1,3*s1-s0,J*r)
T6_inverse(s0,s1,r) = (3*s0-s1,s0,J^-1*r),
```

where the third component is multiplied in R6 and then written as its six unique canonical digits. This can be implemented by constructing the integral digit representative, multiplying by the coefficient formula for J or J^-1, and reducing again by exact lambda division. Choice of representative does not matter because multiplication preserves the ideal.

The integer trace matrices are inverse, and multiplication by J and J^-1 are inverse in R6. Therefore both compositions are the identity on all well-formed data. For each alpha in A941, the trace recurrence and ideal multiplication prove

`D6(J*alpha)=T6(D6(alpha))`, `D6(J^-1*alpha)=T6_inverse(D6(alpha))`.

The units preserve N. Both maps therefore preserve membership in the exact image of A941 in both directions: if a transformed datum were an image, applying the inverse identity would make the original datum an image as well. These facts do not identify T6 with U and do not introduce a separately supplied clock.

## 5. Total normalization, including nonrepresentable data

First reject malformed input types, noncanonical digits, nonpositive traces, a trace sum not divisible by 5, or inverse coordinates with N outside `[1,941]`. If the trace sum is divisible by 5, both inverse coordinates are integers because `3s0-2s1=3(s0+s1)-5s1`. Let the remaining inferred real numbers be `A=u+v*phi`, `B=u+v-v*phi`. They have positive sum s0 and positive product N. Thus both are positive, even when no scalar realizes them.

The original half-open strip is

`1<=A/B<phi^4`, equivalently `0<=v<u`.

Starting with exponent k=0 and the supplied data, perform the following exact steps until this condition holds:

- If `v<0`, apply T6_inverse and increment k by one.
- If `v>=u`, apply T6 and decrement k by one.

The actions on inverse coordinates are

`J: (u,v)->(2u-v,v-u)` and `J^-1:(u,v)->(u+v,u+2v)`.

They preserve N and positivity of A,B since they multiply these magnitudes by positive reciprocal factors. In particular u remains a positive integer: `u=(s0+s1)/5`, and both traces remain positive.

For a purely integer termination proof use the measure

`M(u,v)=2u+1_{v>=u}`.

This is positive. At `v<0`, the inverse step has `u'=u+v<u`; at `v>u`, the forward step has `u'=2u-v<u`. In each case u decreases by at least one, so M strictly decreases regardless of a possible one-unit change of its indicator. At the only remaining case `v=u`, the forward step sends `(u,u)` to `(u,0)`, so u is unchanged but the indicator drops from one to zero. Thus every iteration strictly decreases a positive integer. The algorithm terminates for every surviving arithmetic trace pair before scalar representability has been tested.

The boundary v=0 is accepted; the boundary v=u is excluded and moves in one step to v=0. Under multiplication by J, A/B changes by `phi^-4`, and under J^-1 by `phi^4`. The intervals `[phi^(4j),phi^(4j+4))`, `j in Z`, partition the positive real line. Hence a genuine scalar has exactly one oriented strip representative beta and one integer k with `alpha=J^k beta`. The loop records precisely this exponent. No sign restriction is made: the second case produces negative k when appropriate. No logarithm is evaluated.

## 6. Complete finite search and total inverse

For strip-normalized positive A,B with norm at most 941, set `x=sqrt(A/B)`. Then `1<=x<phi^2`, so

`s0=sqrt(N)*(x+1/x)<3*sqrt(N)<93`.

Thus integer s0 is at most 92. This numerical inequality is exact: `9*941<93^2`. For a scalar beta with coefficient vector c, the inherited positive quadratic form has

`2S(beta)=c^T(5I-11^T)c`, `(5I-11^T)^-1=(I+11^T)/5`.

Cauchy-Schwarz gives each `c_i^2<=4*S(beta)/5<=368/5<81`. Every coefficient of beta is therefore in `[-8,8]`.

Enumerate that entire box, retain exactly `0<=v<u` and `1<=N<=941`, and index each retained scalar by its two exact traces and its canonical lambda-six digits. This is a finite derivation from the carrier, not an assumed list of successful answers or an external oracle. Section 3 proves that no key has two scalars. The implementation may cache this complete index after its first construction without changing its mathematical content.

After normalizing an input, look up its complete key. If no beta is present, reject. Otherwise return `alpha=J^k beta`, beta, k, and N. Multiplication by integral J or J^-1, a finite number of times, reconstructs alpha for either sign of k. The implementation additionally checks that encoding alpha reproduces the original datum.

**Completeness.** Every alpha in A941 has a unique normalized beta. Transporting the exact data through the same unit steps produces beta's traces and its ideal class. The box proof includes beta, so the lookup finds it and returns the original alpha and correct k.

**Soundness.** Every accepted beta lies in the actual enumerated strip domain, and its traces and ideal class equal the normalized input. Reversing the exact data transformations with J^k gives alpha with N in `[1,941]` and exactly the originally supplied datum. Section 3 gives uniqueness. If a well-formed datum is not in the image, it either fails an initial arithmetic check or reaches a normalized key with no scalar; it cannot be accepted by this soundness argument.

**Totality.** Type and initial arithmetic checks are finite, normalization terminates by section 5, the box is finite, and k is a finite integer. Reconstruction and final comparison terminate. This proves rejection or exact inversion on every finite input of the declared types, including nonrepresentable trace pairs and incompatible residues. It does not assert immunity to machine resource limits for unbounded-size integers.

## 7. The exact minimum within the declared ideal-reading sequence

Let `D_k=(S0,S1,alpha mod lambda^k O)` and `K_k=|D_k(B941)|` for the complete original strip B941. The registered source supplies `|B941|=3150`. The three exposed pairs below have common endpoint traces and lie in that strip:

| Pair | alpha | beta | Common (u,v) | Norm | (beta-alpha)/lambda^5 |
|---|---|---|---|---:|---|
| A | (-3,-5,-3,-3) | (2,5,2,2) | (13,6) | 211 | (1,0,-2,-2) |
| B | (-2,1,1,3) | (3,1,1,-2) | (13,7) | 211 | (-1,-3,-3,-1) |
| C | (-6,-6,-5,-4) | (-1,-1,5,1) | (27,8) | 881 | (2,2,0,-1) |

Substitution in section 1 verifies u,v and norms. From `lambda^5=5(-1-2zeta+zeta^2-3zeta^3)`, multiplying by the three quotient vectors gives differences `(5,10,5,5)`, `(5,0,0,-5)`, `(5,5,10,5)`. Each quotient has `(u,v)=(5,8)` and norm 1, so each difference has norm 3125 and exact lambda valuation five.

Multiplying both endpoints of one pair by each of the ten units `+/-zeta^j`, `0<=j<5`, preserves u,v, strip membership, traces and the ideal congruence. Its two ten-element orbits are disjoint. If they met, beta would equal xi*alpha for a root of unity xi, and the integer norm identity `3125=N(alpha)*N(xi-1)` would force 211 or 881 to divide 3125, which is impossible. Within an orbit all ten values are distinct because alpha is nonzero. The three twenty-point families are mutually disjoint because their ordered u,v values differ. Thus there are thirty disjoint collision pairs at depth five.

Identifying those pairs alone reduces the 3150-element strip to at most 3120 classes. Hence `K_5<=3120<3125`, independently of the newly computed exact intermediate counts. Ideal reduction gives `K_k<=K_5` for every positive `k<=5`. Section 3 gives `K_6=3150`; larger depths remain injective. Therefore depth six is both the first injective depth and the first depth with at least 3125 strip keys. A single displayed pair already proves failure of full-domain injectivity at every depth at most five, while section 3 proves full-domain injectivity at six.

For the registered observed-reader class `R(n,x)=J^n G(label_n(x))`, integral nonzero generators of norm at most 941, every native label accessible at every `n>=3`, and no separately supplied n, the original normalization/offset argument applies because J is a unit modulo every lambda-power ideal. Selecting one normalized representative per distinct key attains `min(3125,K_k)` usable labels. If two generators normalize to the same key, their J offsets can be aligned at sufficiently large accessible sheets, proving the matching upper bound. Those exact hypotheses are essential. The minimum established here is within this declared observation sequence and reader class, not among all possible observables or state encodings.

## 8. Evidence and limits

The exact local eight-depth census was previously exposed; it is preserved separately with its original records. Its intermediate counts are not used as premises of the proofs above. This fresh formal verifier audits total recognition over the complete normalized arithmetic input set, all 15625 ideal residues, signed unit translations, exact boundary and malformed cases, data dynamics, characteristic 25, and the exposed thirty-pair certificate. An independent reviewer freezes its own code before exposure to the author implementation. Awareness of the mathematical target, source-code independence, and reproduction on two architectures are distinct records.

The proven residue alphabet decreases from `5^8` for O/25O to `5^6` here. The full datum still includes two unbounded integer traces. No speedup, finite total state space, physical resource saving, corruption detection, preferred dictionary, native contact, or realization of U follows. Changing one valid datum into another valid datum cannot be detected by exact image recognition. No L2-L6 bridge or physical occurrence law is supplied.
