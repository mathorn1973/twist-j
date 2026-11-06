# Source access, profile selection and complete-control boundaries

NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Candidate analytical proof under [CONTRACT.md](CONTRACT.md).
This proof supplies conditional mathematical boundaries. It does not admit
the physical interface or close QUADRATIC-MEMORY-NATIVE-CONTACT.
No new scientific program or enumeration was executed.

## 1. Complete source-table reduction

Use the full carrier X, factor F=D x {0,1}, maps I=b_x b_y,
tau_i=e_i d_i, and mixed determinant h from the contract. In particular,

    h(I s)=-h(s),  I tau_i I=tau_i^-1,
    W(s,eta)=(I^a(h(s),eta) s, beta(h(s),eta)).

Here s includes all twelve field coordinates. The map I negates both q
and both r, as well as applying the negative row swap to each piston.

On each nonzero sign pair {k,-k}, k=1,2, write h=(-1)^u k. Each data
orbit {s,I s}, with the two possible bits, has four labels (u,eta).
The control acts as an arbitrary permutation

    pi(u,eta)=(u xor a((-1)^u k,eta), beta((-1)^u k,eta)).

It is the same permutation on every such orbit in the sign pair. On
h=0 its form is (u xor a(0,eta), beta(0,eta)) on every free I orbit;
bijectivity requires beta(0,.) to permute the bits. Hence W commutes
with I there. The same statement holds at I-fixed points directly.

Let j(u,eta)=(u xor 1,eta) and t(u,eta)=(u,eta xor 1).
These lower-case permutation symbols are not the algebraic axiom J.
The three conjugates of j in S4 are j, t and jt. Thus the complete
map E_W=W I W^-1 has the form

    E_W(s,eta)=(I^chi(h) s, eta xor epsilon(h)),                 (1)

where chi,epsilon are even in h, (chi(0),epsilon(0))=(1,0), and each
nonzero pair independently has (chi,epsilon)=(1,0),(0,1) or (1,1).
These are complete data actions, including q and r.

Since tau_i preserves h and eta, (1) gives

    E_W tau_i E_W = tau_i^((-1)^chi(h)),
    K_(W,i)=[E_W,tau_i]: q_i -> q_i+3 chi(h).                  (2)

Every other coordinate is fixed, and the inverse subtracts 3 chi(h).
The four-label argument classifies W; it does not assume that tau_i
preserves one chosen I orbit. Formula (1) and the full native inversion
identity prove (2) on all X, including arbitrary q,r and occupied eta.

This also rederives the needed part of the [predecessor proof][class].
Its four profiles and reduced polynomials are

| chi(1)chi(2) | chi(h) |
|---|---|
| 00 | 1-h^4 |
| 01 | 1+2h^2+2h^4 |
| 10 | 1+3h^2+2h^4 |
| 11 | 1 |

They concern each fixed port i=x or i=y separately.

## 2. An inactive pair requires both directions of transfer

**Proposition 1.** On a nonzero sign pair, chi(k)=0 if and only if,
for one bit c and one Boolean function d of eta,

    pi(u,eta)=(eta xor c, u xor d(eta)).                       (3)

Equivalently,

    a((-1)^u k,eta)=u xor eta xor c,
    beta((-1)^u k,eta)=u xor d(eta).                          (4)

There are eight possibilities. Exactly two are involutions:

    (u,eta) -> (eta,u),
    (u,eta) -> (eta xor 1,u xor 1).                          (5)

**Proof.** By (1), inactivity is precisely pi j pi^-1=t. Write
pi=(v,zeta). The equivalent relation pi j=t pi gives

    v(u xor 1,eta)=v(u,eta),
    zeta(u xor 1,eta)=zeta(u,eta) xor 1.

Hence v depends only on eta, while zeta=u xor d(eta). Bijectivity
forces the two values of v to differ, so v=eta xor c. Conversely,
(3) is bijective: eta=v xor c and u=zeta xor d(eta). It has the
required conjugation. Two choices of c and four choices of d give eight.
Its second iterate has first coordinate u xor d(eta) xor c. It is an
involution exactly when d(0)=d(1)=c, which also restores the second
coordinate and yields (5). This proves the full characterization.

Consequently each of these separate restrictions excludes inactivity
on the pair:

| Restricted access | Exact restriction |
|---|---|
| No source-orientation transfer to the bit | beta(-h,eta)=beta(h,eta) |
| No bit control of the data action | a(h,0)=a(h,1) |
| No sign information in the data decision | a(-h,eta)=a(h,eta) |

Each restriction contradicts one equality in (4). In particular no
data-to-bit writing, beta(h,eta)=b(eta), is too weak an interface.
If one of these restrictions holds on both nonzero pairs, (2) has
profile 11. If both table decisions are sign-blind, there is also a
direct proof: WI=IW, so E_W=I and K_(W,i)=tau_i^3.

The data's old sign is transferred to the output bit, while the old bit
determines the output sign. This is reversible transfer of information;
it is not a read-only extraction. Equation (3) is a necessary and
sufficient condition for inactivity within the table class. It is not
an independent reason to admit that class or to require inactivity.

### 2.1 Relation to original native words

Every original slotwise a,b,c,d,e and each whole-cell shear P,Q_cs fixes
eta. Every fixed word and inverse in that alphabet therefore fixes eta.
Any such word that also lies in the declared table class has profile 11
by Proposition 1. In particular the supplied W_b is not such a word.

Conversely the table class does not contain every native word. The word
tau_x=e_x d_x changes q_x while keeping all pistons. On the h=1 piston
witness p_x=(1,0,0,0), p_y=(0,0,0,2), I changes the pistons. Neither
identity nor I can have that tau_x output. Thus limiting data actions to
{s,I s} is itself a class restriction, not a completeness consequence
of the original alphabet.

These are exact statements about fixed words with a passive appended
bit. They do not concern all possible autonomous or physically admitted
architectures. The original U acts on a different full carrier with its
native counter and a state-selected letter; its selector reads q.
The separate canonical three-preimage obstruction for its literal
common-ready reversible lift is not reinterpreted here.

## 3. Two complete separate quadratic records lose needed sign information

The canonical QDD-DIRECT-RECORD-E-NONCONGRUENCE theorem gives, on the
native piston block,

    D_P(p)=D_P(p') if and only if p'=p or p'=-p.               (6)

Let Q_pair=(D_P(p_x),D_P(p_y)). By bilinearity,

    Q_pair(-p_x,p_y)=Q_pair(p_x,p_y),
    h(-p_x,p_y)=-h(p_x,p_y).                                (7)

**Proposition 2.** Suppose the two table decisions a,beta are set
functions only of (Q_pair,eta), with the same decision for equal inputs.
Then their full contact has profile 11. Nevertheless h^2 and all four
functions chi(h) are set functions of Q_pair.

**Proof.** The witnesses p_x=(1,0,0,0), p_y=(0,0,0,2h) realize every
h. Applying (7) to each witness forces a(-h,eta)=a(h,eta) and the
same equality for beta. Proposition 1 applies. Conversely (6) determines
each piston up to its own sign. Changing either representative only
negates h, so h^2 is well-defined on Q_pair. Every chi in (2) is an
even function of h and hence is likewise well-defined.

The endpoint coefficient 1-h^4 can therefore be read from these two
records, although the controls implementing an inactive pair cannot
choose their two decisions from those records alone. The restriction
is on this specified control input. It does not exclude a joint signed
source record, another carrier, or another independently admitted
interface. Existence of a set function is also not physical acquisition.

## 4. Factor-only words cannot record a factor-trivial contact

Call a complete permutation F factor-compatible when

    rho F = Fbar rho                                          (8)

for a map Fbar on the factor. No forgotten q then influences the
factor output. Since every rho fibre has the same finite size 25,
bijectivity of F implies bijectivity of Fbar: two different fibres
cannot inject into the same 25-state fibre. Thus (8) is preserved by
composition and inverse.

Every original compiler letter, both shears, and every source-table W
obey (8). The native factor formulas do not use q, and h and the two
table decisions also do not use q. This includes the supplied W_a.

**Proposition 3.** For arbitrary fixed preword A and postword B in this
alphabet, and O either identity or K_(W,i),

    rho B O A = Bbar Abar rho.                              (9)

Hence no fixed factor-only endpoint read can distinguish these two
experiments, for any complete input or preparation, using the same A,B.

**Proof.** Equation (2) gives rho O=rho for both experiments. Apply
(8) to B and then A. This is pointwise equality on the whole carrier;
arbitrary word lengths, occupied bits and correlations in a classical
preparation do not change it.

The supplied Ucal_i makes r_i depend on q_i and does not obey (8).
For example r_i=0 is fixed at q_i=0 but sent to 2 at q_i=2 by the
canonical P_q table. Its explicit q-to-factor access is exactly a
missing capability for this word class. The theorem does not show that
this particular Ucal is unique or physically admitted, and it does not
apply (8) to the actual state-selected U.

## 5. Conditional selection distinguishes endpoints from letters

For lambda in F5^x define the mathematical comparison S_lambda by
right-multiplying both piston matrices by diag(lambda,1) and fixing
q,r,eta. Determinant polarization and left/right multiplication give

    h S_lambda=lambda h,
    S_lambda I=I S_lambda,
    S_lambda tau_i=tau_i S_lambda.                         (10)

This is a completely specified carrier map. It is not asserted to be a
physical symmetry, an original native word or a symmetry of the whole U.

**Proposition 4.** Within (2),

    chi(h)=1-h^4
      iff [K S_2=S_2 K] and [chi is nonconstant].           (11)

**Proof.** Since S_2 fixes q, the commutation is exactly chi(2h)=chi(h).
Multiplication by 2 cycles through all four nonzero field elements.
Thus chi is constant on h!=0 and its two pair values coincide. The only
remaining profiles are 00 and 11. Nonconstancy excludes 11, because
chi(0)=1 is already forced. The displayed profile has both properties.

| Additional condition on the endpoint response | Remaining profiles |
|---|---|
| Sign invariance chi(-h)=chi(h) | 00, 01, 10, 11 |
| Nonconstancy of chi | 00, 01, 10 |
| Commutation of K with S_2 | 00, 11 |
| Both conditions in (11) | 00 |

Both conditions in (11) remain explicit selection premises. Their
wording omits L5, but no independent physical derivation is supplied.
Ordinary common scalar rescaling p_x,p_y -> c p_x,c p_y only multiplies
h by c^2 in {1,4}; it gives sign invariance and leaves all four profiles.
It cannot substitute for the nonsquare multiplier in S_2.

### 5.1 Imposing the symmetry on W has a different consequence

If W S_2=S_2 W with the bit fixed by S_2, its table must satisfy
a(2h,eta)=a(h,eta) and beta(2h,eta)=beta(h,eta) on nonzero h.
The data I action is faithful there because h changes sign. The table
is therefore sign-blind, E_W=I and its profile is 11. At h=0 W already
commutes with I. The same conclusion follows from sign blindness alone.

Thus the endpoint symmetry in (11) cannot be imposed on the literal
letter without changing the result. Any alternative simultaneous action
on the bit or on a larger control description has to be specified and
proved separately.

### 5.2 Preserving h at three different boundaries

Equation (1) gives h E_W=(-1)^chi(h) h. Therefore

    h E_W=h  iff the profile is 00.                         (12)

At h=0 this holds automatically; at every nonzero h it forces chi=0.
For that profile (1) is the unique full map

    E_00(s,eta) = (I s,eta)        if h=0,
                  (s,eta xor 1)   if h!=0.                  (13)

Every one of the 512 reversible profile-00 controls has (13). Equation
(12) is an equivalent selection premise inside this class, not an
explanation of why that premise should hold physically.

| Boundary at which h is preserved | Consequence |
|---|---|
| Complete K | All four profiles already preserve h and all G |
| Conjugate E_W | Exactly profile 00 and the complete map (13) |
| Individual W | Only profile 11 |

For the last row, h-preservation at nonzero h forces a(h,eta)=0.
This contradicts (4) for an inactive pair. It need not force the bit
part of E_W to be trivial, so no stronger assertion E_W=I is made there.

### 5.3 Some other proposed principles select 11 or exclude the class

All four K read at most two piston cells and change one q_i; merely
bounding that support by two cells does not select a profile. Requiring
independence from the other piston does select 11: with
p_x=(1,0,0,0), variation of p_y=(0,0,0,2h) attains every h, forcing
chi to be constant.

The constant profile 11 has reduced polynomial degree zero in h; the
three other profiles have degree four. In native piston variables they
have degree eight: the nonzero h^4 coefficient leaves a nonzero
p_(x,1)^4 p_(y,4)^4 term. All individual exponents are at most four,
so these are already unique reduced function polynomials over F5.
Minimizing degree selects 11; requiring a nonconstant polynomial still
leaves all three other profiles.

The locus h=0 is neither G=0 nor the degeneracy locus of the 2-by-2
Gram. For X_p=identity, Y_p=0, G=(1,0,0); for
X_p=identity, Y_p=diag(1,4), G=(1,0,4) and alpha gamma-h^2=4.
Both have h=0 and every profile must respond with chi=1. A proposed
requirement of zero response for Y_p=0, or of response only at a
degenerate Gram, would therefore exclude this entire table class.
Interpreting zero pistons as physical absence is not a premise here.
Likewise preserving the whole G after E_W is impossible on all X:
at h=0 E_W=I sends G to -G, including (1,0,0) to (4,0,0).

## 6. Complete group classification inside the 24 involutions of profile 00

Hold the supplied W_a and all other v100 compiler letters fixed. Replace
only W_b by an involutive source-table W of profile 00. Let Gamma(W)
be the group of their induced permutations on F, of size
|F|=19531250. This is a factor group statement, not a classification
of full X permutations, physical interfaces or shortest words.

**Proposition 5.** Exactly

    Gamma(W)=Alt(F) if beta(0,eta)=eta       (16 controls),
    Gamma(W)=Sym(F) if beta(0,eta)=1-eta     ( 8 controls).   (14)

All 24 have the same complete E_W and K_(W,i). Their A1--A18 macro
maps in the frozen [CW-ALG-1 source][spec] remain exactly the same,
including their full q action. The whole group, individual W letters,
all word prefixes and the syntax-defined compiled word are different
questions.

### 6.1 Counting the controls and preserving the seed

On each nonzero pair Proposition 1 gives two involutions: in labels
2u+eta they are (12) and (03). At h=0 there are four choices when
beta=id (arbitrary a(0,0),a(0,1)), and two when beta flips (the two
a values must be equal). Hence (4+2)*2*2=24, split 16 and 8.

Their common complete E_W is (13), not merely a shared factor map.
In the source macro definitions A1--A18, W_b occurs only through
E_b=W_b I W_b in A3. A1--A2 do not use it. A3 uses unchanged E_a
and unchanged complete E_b; A4--A17 are compositions, powers and
inverses of unchanged maps. A18 uses the unchanged W_a separately.
Structural induction therefore preserves every complete macro map,
including any action on q, not only its restriction to q=0.

In particular the source isolated three-cycle C_* survives with its
exact support and orientation. Its three factor states have pistons
p_x=(3,0,3,0), p_y=(4,1,1,4), bit 0, and respective reference pairs
(2,0),(0,1),(3,0). It fixes every other factor state. This is the
existing A18 theorem applied by equality of its complete building maps;
it is not a newly enumerated seed.

### 6.2 Primitivity, including changed zero branches

The source A1--A2 words supply every translation of D, acting identically
on both bit layers. W_a joins some states between the layers, so the
group is transitive. A translation-invariant block system has either
separate layer blocks, cosets of H_eta <= D, or joined blocks

    ((z+H) x {0}) union ((z+d+H) x {1}).                    (15)

For completeness, a block containing (0,0) has layer-0 intersection
its translation stabilizer H. If it meets layer 1, that intersection
is one coset of the same H. Its translates give (15). If it does not,
the two layers are classified separately. Over F5 these additive
subgroups are vector subspaces.

In the separate case, the output bit of unchanged W_a must be constant
on each coset. As functions of h its two input-bit rows are

    f_0(h)=1_{h in {3,4}},   f_1(h)=1_{h not in {1,2}}.

The common radical of the quadratic form h on D consists of r_x,r_y.
The periods of either f_eta composed with h are exactly that radical.
Indeed, if a period v has h(v)!=0, the line tv visits h values
0,h(v),-h(v), whose f_eta values are not all equal. If h(v)=0 but v
is outside the radical, choose z with nonzero polarization against v;
h(z+tv) then runs through F5 and f_eta is again nonconstant. Radical
vectors are periods directly. Thus H_eta is inside span(r_x,r_y).
The original c_x,c_y transfer a nonzero r component into a piston
component, so invariance under their linear parts forces H_eta=0.
Only singleton blocks remain in this case.

In the joined case, original affine letters act equally on both layers,
so L_g H=H and L_g d-d is in H. Writing d=(d_x,d_y), P gives
(0,d_x) in H; applying Q_cs and subtracting gives (d_x,0) in H.
The analogous argument gives (d_y,0),(0,d_y) in H, hence d in H.
We may set d=0 in (15).

For h(z)!=0 the two inputs (z,0),(z,1) lie in the same block.
Both allowed involutions (5) send their data to the unordered pair
{z,I z}. Their images lie in one block, so (I-Id)z is in H.
The unchanged W_a gives (I_a-Id)z in H in the same way. This argument
uses no value of the replaced W on h=0.

The vectors h!=0 span D: for arbitrary w choose active v; the polynomial
h(v+tw), of degree at most two and nonzero at t=0, cannot vanish at
all four nonzero t. For one such t both v and v+tw are active and
w=t^-1((v+tw)-v). Thus H contains both full linear images
im(I-Id) and im(I_a-Id).

To finish explicitly, use the source Walsh coordinates (s,v,u,t,r)
in each cell. The linear parts of a,b,c are respectively

    (s,v,-u,-t,r),
    (-s,v,-u,t,-r),
    (-s,v+2r,-u,t-2r,-r).

The first two images contain every s,u,t,r direction in both cells.
Applying the c linear part to an r direction also supplies the missing
v direction. Hence H=D. The only joined block is all F, proving
primitivity for every one of the 24 controls.

### 6.3 Why the alternating group is contained

The unchanged C_* and primitivity are precisely the hypotheses of the
source constructive argument in section 5.3 and B1--B7. Its proof uses
the support triples of w C_* w^-1 for words of length at most |F|.
Their component partition must stabilize; a stabilized partition is
generator-invariant. Primitivity and a three-point initial edge force
one component. Before stabilization the number of components strictly
decreases, so the stated finite bound suffices. The explicit gluing
identities in B3--B6 then generate all three-cycles on that component.
Therefore Alt(F) is contained in Gamma(W).

This argument requires inverse-closed generators, primitivity and one
three-cycle; it does not require every generator to be even. Those
hypotheses have just been preserved. No new outside group-classification
theorem, finite census or unexpanded target word is substituted for it.

### 6.4 Parity on the complete factor

The bilinear form h between two four-dimensional pistons is
nondegenerate. Its zero locus has

    625 + 624*125 = 78625

piston pairs: all second pistons at first piston zero, and 125 choices
for each nonzero first piston. Including the two r values gives

    N_0=25*78625=1965625                                    (16)

data points in D with h=0. This is not the smaller locus G=0.
For each fixed nonzero h there are 25*624*125=1950000 data points,
and hence 1950000 I pairs on each nonzero sign pair. Each carries
one transposition from (5), an even number of repetitions.

The fixed data of I on D number 5^4=625: each negative row swap has
two free piston coordinates, and both r must be zero. Their h is
automatically zero. The remaining h=0 data give

    (1965625-625)/2=982500

free I pairs, again an even number of repetitions of the same local
four-state table. Their contribution to parity is +1. On the 625 fixed
data W acts only by beta(0,.). Consequently

    sign(W)=sign(beta(0,.)).                               (17)

Every original letter and shear is even on F because it acts by the
same permutation on both layers. The unchanged W_a has 3900000
transpositions and is even, by the same nonzero-pair count. Thus beta=id
makes Gamma(W) a subgroup of Alt(F); the opposite inclusion was proved.
If beta flips, Gamma(W) contains Alt(F) and an odd permutation, hence
is Sym(F). This proves (14). Both groups are transitive; (14) is a
difference of available permutations, not of state-orbit counts.

## 7. Explicit prefix and conjugating-word witnesses

Keep the supplied W_b on h!=0 but define

    W_flip(s,eta)=(s,eta xor 1) if h=0,
                  W_b(s,eta)   if h!=0.                    (18)

It is an involution of profile 00 and has the same full E and K as
W_b, while its group is Sym(F) instead of Alt(F).
At the all-zero complete input W_b fixes eta=0 and W_flip changes it
to 1. The difference also appears within the actual twelve-leaf contact.
Its execution starts e_i,d_i,W. After e_i,d_i the all-zero input has
q_i=4 and all pistons,r,eta still zero. After W the two implementations
have different bits. Both complete contacts end at q_i=3, eta=0,
with all other coordinates restored. This is an exact hand-derived
prefix witness, not a measured trajectory.

Even adding W=id on h=0 does not identify W. On h!=0 let

    W_opp(s,eta)=(I^(1 xor sigma(h) xor eta) s, 1 xor sigma(h)),

and keep identity at h=0, with sigma(1)=sigma(2)=0 and
sigma(3)=sigma(4)=1. It uses the second involution in (5) on both pairs.
It has the same E,K and Alt(F) group as W_b. Yet at h=1,eta=0,
W_b is identity and W_opp applies I and sets the bit to 1. For instance
p_x=(1,0,0,0),p_y=(0,0,0,2),q_x=1 gives q_x'=4 under W_opp.
Thus equal groups also do not identify prefixes or full q actions.

There is a direct failure of substitution in the compiler's conjugating
words at the level of factor permutations. Use the unchanged piston
translations to move C_* to a cycle C_0 supported at zero pistons, on
bit layer 0. The following equalities and supports are on F:

    W_b C_0 W_b = C_0,

whereas W_flip C_0 W_flip is its corresponding three-cycle on bit
layer 1, with disjoint support. Both are words in the specified alphabet.
Equal E and equal A1--A18 do not preserve all conjugated seed supports.

The source B1--B7 construction inspects these supports to choose words.
With a changed W it can be applied again, since the common seed and
primitivity were proved, to compile every even factor permutation.
This means a new application with the changed letter maps and its own
determined word. It proves neither that literal replacement inside the
already frozen T_alg has the old factor action nor that its old
syntax-defined H_f on q is unchanged. No such target word was expanded
or executed here.

One specific prefix property does survive. Every source-table W fixes
or negates each r_j, so r_j^2 is invariant at its boundary. In the second
reader at port y, the remaining leaves either fix r_x or negate it.
Therefore the canonical protection of r_x^2 at every listed leaf
boundary survives these replacements, by induction on the list. This
uses the known form of each leaf, not equality of K alone, and says
nothing about the interior of a physical realization of W.

## 8. What the proof decides about admission

The proof establishes explicit restricted obstructions and conditional
selection statements. It has not established the first physical
admission obligation. In particular:

| Input needed for a stronger conclusion | What is established here |
|---|---|
| Why this complete table class is admitted | Its orbit/action restriction and bit access are explicit additional choices |
| An accessible oriented mixed source | The separate complete quadratic records do not determine the needed sign decisions |
| A reversible exchange with the bit | Its exact necessary and sufficient local form is (3) |
| Access from q to a readable reference | It is necessary to leave the factor-compatible word class in Proposition 3 |
| Why profile 00 is selected | (11) and (12) are conditional selectors with unadmitted premises |
| Which uses of W can be substituted | Shared E/K and A1--A18 are proved; prefixes, conjugating words and the old T_alg are separate |

None of these statements supplies the independent reading C, admission
of W_a, preparation S0, a physically selected readout, autonomous
execution, fresh memory, occurrence, energy, time, scale or a layer lift.
The live O owner remains open. Failure of a restricted interface is not
negative closure of the complete independently admitted native class.

[class]: https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/notes/C-CONTACT-INTERFACE-CLASSIFICATION-N/PROOF.md
[spec]: https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/probes/P-ALG-CONTACT-REALIZATION-1/SPEC.md
