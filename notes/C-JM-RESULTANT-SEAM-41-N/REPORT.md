# Two polynomial records and the resultant-41 seam

**Status:** NON-CANONICAL. Candidate `C-JM-RESULTANT-SEAM-41-N`.
**Scope:** L1 algebra of explicitly specified integer modules and orders.
**Evidence:** candidate-T analytical implications below; candidate-C exact local
checks. Result-exposed, one local x86_64 architecture, no independent agent.
The user supplied the product polynomial, resultant, and first four counts.
The source audit changed no public repository. This publication archives it
under notes only, with custody in [issue #1670](https://github.com/mathorn1973/twist-j/issues/1670).
No Born occurrence, physical apparatus, spatial dimension, physical time,
or layer lift is claimed. See [PROVENANCE.md](PROVENANCE.md) for the exact
source-to-publication changes and the single-architecture evidence boundary.

## 1. Fixed objects

Let L=Z[x],

    f=x^4-3x^3+4x^2-2x+1,
    g=x^4-4x^3+8x^2-4x+1,
    h=fg=x^8-7x^7+24x^6-46x^5+54x^4-39x^3+20x^2-6x+1.

Put A=L/(f), B=L/(g), R=L/(h), S=A x B. The step is multiplication
by x. Its block representation on S is D=diag(C_f,C_g); on the power
basis of R it is H=C_h, where companion matrices act on columns.
The reduction inclusion C:R->S satisfies D C=C H and det C=41.
The Smith invariants are (1,1,1,1,1,1,1,41). Signs of unit invariant
factors in a non-normalized Smith form do not matter. The step matrices
D and H themselves are unimodular and have Smith form I_8.

The maps into the cyclotomic fields are

    J=1+j^2, Phi5(j)=0,
    M=1+m+m^2=(1+sqrt(2))*m, Phi8(m)=m^4+1=0.

These realize f and g exactly. The real dimensions of the comparison tori
are eight, but no physical spatial dimension is identified.

Over Q:

    R tensor Q = Q(zeta5) x Q(zeta8),

an eight-dimensional product algebra with zero divisors, not a field.
The compositum of the two full cyclotomic fields is Q(zeta40), degree 16.

## 2. Dynamical checks

Each factor has two expanding and two contracting real directions, with
moduli phi,phi^-1 and delta,delta^-1 respectively, each twice.
The characteristic polynomial gives trace 7 and determinant 1.
The standard topological entropy of the mathematical toral automorphism is
2 log(phi)+2 log(delta). This is not thermodynamic entropy.

Let F_n=|det(D^n-I)|=|det(H^n-I)|. Let P_n count points of least period n,
and O_n=P_n/n count orbits. Then:

| n | J fixed points | M fixed points | F_n | P_n | O_n |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 2 | 2 | 2 |
| 2 | 11 | 36 | 396 | 394 | 197 |
| 3 | 31 | 242 | 7502 | 7500 | 2500 |
| 4 | 55 | 1296 | 71280 | 70884 | 17721 |

F_n agrees for ALL n, since D and H are rationally similar and have the
same eigenvalues. The equality of these counts does not imply integral
conjugacy. The finite lattice inclusion induces a degree-41 torus covering,
not a unimodular coordinate change.

## 3. Exact seam

The resultant and modular factor roots are

    Res(f,g)=41,
    roots(f mod41)={11,17,19,38},
    roots(g mod41)={6,7,13,19},
    gcd(f,g) mod41=x-19.

An integer Bezout certificate is

    (14x^3-36x^2+43x+64) f
    +(-14x^3+22x^2-7x-23) g = 41.

Define u:A->F41 and v:B->F41 by evaluation x->19. Both are surjective.
The reduction image is contained in ker(u-v), which has index41 in S.
The computed determinant of C is41, so equality follows:

    R = {(a,b) in A x B : u(a)=v(b)} = A x_(F41) B.

Equivalently, there is an exact sequence of L-modules

    0 -> R -> A x B -> F41 -> 0,

where the last map is (a,b)->u(a)-v(b), and x acts on F41 by19.
The additive/module quotient S/R is F41. It is NOT a quotient ring by R:
R is a subring, not an ideal of S, and u-v is not a ring homomorphism.

The conductor of R in S is ker(u) x ker(v), equivalently

    g(J) A x f(M) B.

It has quotient S/conductor = F41 x F41; R/conductor is its diagonal F41.
Away from41, R and S become equal after localization. Their separation
idempotents e_A=(1,0), e_B=(0,1) lie in S but not R; the smallest positive
integer k with k e_A in R (equivalently k e_B in R) is41.

## 4. What exactly has 41 possibilities

Index41 by itself counts cosets, not ways to choose a ring.
There ARE precisely41 marked module-extension classes in the following
complete and explicit category:

    0 -> A -> E -> B -> 0

of L=Z[x]-modules, with the endpoint modules and the endpoint identifications
fixed. The free resolution 0->L --g--> L->B->0 gives

    Ext^1_L(B,A)=A/gA=L/(f,g)=F41.

An extension class k can be presented by a lift e of 1 in B satisfying

    g(x)e=k*1_A.

In the basis 1_A,x1_A,x^2 1_A,x^3 1_A,e,xe,x^2e,x^3e, the step is D with
one extra upper-right entry k in position (0,7).
The zero class is the split module S. The class1 is R, via the exact sequence
0->A --multiplication by g-->R->B->0. An explicit integral basis-change
certificate of determinant1 is checked in supplement.py.

Since 19 has order40 in F41*, the A-unit J acts transitively on the40
nonzero extension classes. If endpoint unit changes are allowed, these41
marked classes fall into TWO middle-module isomorphism types: split and
nonsplit. Their distinction is certified by the modular dynamics below.
This is a classification of this extension family, not of all integer
8-by-8 matrices with polynomial h, all orders, or all physical couplings.
Between the specifically embedded R and S there are only two intermediate
additive groups, hence only two intermediate rings, since [S:R] is prime.

## 5. The seam has observable integral dynamics

On the common quotient, t ->19t. One has

    19^8=37, 19^20=-1, 19^40=1 mod41,

so the multiplicative order is40. The common residue of a glued pair and
the mismatch residue of a general split pair both follow this update,
but they are distinct uses of F41. A glued pair has mismatch zero.

Reduction modulo41 gives

    S/41S = F41^8,
    R/41R = F41[epsilon]/(epsilon^2) x F41^6.

The double factor is at x=19. On it, x=19+epsilon and the step matrix is
19I+N with N^2=0 but N!=0. Consequently

    ord(D mod41)=40,
    ord(H mod41)=40*41=1640.

At the 40th step, the split matrix fixes all41^8 residue vectors, while the
glued matrix fixes41^7. The reduction map C has rank7 modulo41. Thus there
is a nonzero nilpotent class invisible in the naive seven-coordinate
reduction image. The seam quotient alone is a single field, but the entire
41-fiber is not a single field and not reduced. Both facts must be retained.

## 6. A separate index3 in the silver power order

The matrices of power bases in the full cyclotomic integer bases are

    BJ = [[1,1,0,-2],[0,0,-1,-2],[0,1,1,0],[0,0,-1,-3]], det=-1,
    BM = [[1,1,0,-5],[0,1,2,0],[0,1,3,5],[0,0,2,7]], det=-3.

Hence A=O5 but B=Z[M] is an index3 order in O8=Z[m]. Explicitly,

    m=(1-11M+7M^2-2M^3)/3.

The determinant establishes that this denominator cannot be removed in the
power basis. Equivalently disc(g)=2304=9*256, whereas disc(O8)=256.
The field equality Q(M)=Q(m) is true but the integer-order equality is false.

For O=O5 x O8:

    [S:R]=41, [O:S]=3, [O:R]=123.

Also disc(f)=125, disc(h)=484128000=32000*123^2, with disc(O)=32000.
The prime3 concerns a factor's nonmaximality; it is not an extra cross-seam
between the two fixed power orders. At the native local primes2 and5,
R tensor Z_p = S tensor Z_p = O tensor Z_p. The actual cross defect is at41,
not intrinsically at the two physical-dictionary places2 and5.

## 7. The inherited Born conjugation does not close on R

Use the componentwise CM conjugation in O5 x O8 and alpha=(J,M) in R.
The seam evaluations extend to O because3 is invertible modulo41. They are

    j ->10, m ->27,
    J ->19, M ->19,
    bar(j) ->37, bar(m) ->38,
    bar(J) ->17, bar(M) ->7.

Thus bar(alpha) fails the seam. Moreover the would-be Born squares have

    J bar(J) ->36,
    M bar(M) ->10,

so alpha bar(alpha) fails it as well. The order is not closed under the
inherited star, nor under that basic quadratic operation. This is not a
no-go for an external Hermitian reading of a raw record.

There is also a factor-level failure at3:

    bar(M)=(2-4M+2M^2-M^3)/3 not in Z[M].

The minimal subring of O containing R and closed under this conjugation is
in fact the WHOLE maximal product O. A compact exact certificate is

    123 bar(alpha) = 89-197alpha+162alpha^2-135alpha^3
                    +99alpha^4-101alpha^5+44alpha^6-10alpha^7.

The coefficient -10 is coprime to123, so the additive class of bar(alpha)
in O/R has order123. Since [O:R]=123, it generates that quotient:

    R + Z bar(alpha)=O, hence R[bar(alpha)]=O.

Adjoining the missing inherited conjugate is therefore not a seam-preserving
repair; it completely splits the two factors and fills the silver index3.
The star-stable intersection R intersect bar(R) instead has index123^2 in O,
because R+bar(R)=O, but it does not contain alpha. Its adoption would change
the declared carrier/step contract and is not silently made here.

A single prime field F41 has no nontrivial field automorphism. Since
conjugation sends the chosen primes to distinct primes, a single such
residue cannot carry the inherited complex-conjugation operation. Paired
conjugate residues, a typed R-to-bar(R) pairing, or another explicit target
carrier are separate constructions that could be studied. None is selected.

## 8. A precise conditional minimum

If a common finite residue field F_q must faithfully retain both a phase
of order5 and a phase of order8, then its cyclic multiplicative group must
have order divisible by lcm(5,8)=40. Thus q>=41, and F41 attains this bound.
This is a sharp smallest-CARDINALITY statement in that declared class.
It is not an unconditional minimum of physical coupling cost. Collapsed
phases, other rings, other carriers, or different admissibility conditions
are outside the class.

The compositum is useful as an arithmetic comparison, without adopting it
as the state carrier. With z=zeta40, J=1+z^16, M=1+z^5+z^10,

    N_(Q(zeta40)/Q)(J-M)=41.

Thus the ideal generated by J-M in the full compositum is a degree-one
prime of norm41. Of the16 primitive40th-root residues modulo41, only z->6
satisfies J=M. It yields j->10 and m->27. The congruence 41=1 mod40 explains
the complete split; it does not by itself select the marked pair. The
particular equality of the two steps does that.

## 9. Coupling and Born boundaries

On the stated pair carrier, T(a,b)=(Ja,Mb). Fixing b while changing an
admissible a does not change any future b. The seam is an initial-state
compatibility constraint/common factor, not an interaction writing new
information to the other factor. More strongly,

    Hom_(Z[x])(A,B)=Hom_(Z[x])(B,A)=0,

since f and g are coprime over Q and the target modules are torsion-free.
The nontrivial common quotient/Ext group is torsion; it does not supply a
nonzero full-carrier equivariant transfer map. Arbitrary noncommuting or
nonlinear contacts are not excluded, but need their own explicit contract.

The accepted TWO-PLACE-PHYSICS [D] dictionary does not turn this new L1
module construction into a physical gate. The construction fixes no positive
Hermitian pairing, source family, probability rule, event, occupied record,
renewal law, physical coupling strength, or empirical constant.

The most useful next question is a typed quadratic reading of the oriented
record and its conjugate: source, target, equality, positivity, normalization,
and actual residue compatibility must be fixed without importing target Born
probabilities. The failure of inherited star-closure above must not be hidden.

## 10. Evidence and reproduction

Run with Python3 and SymPy:

    python audit.py
    python conjugation_audit.py
    python supplement.py

The three successful scientific outputs are retained byte for byte next to
the unchanged scripts. [PROVENANCE.md](PROVENANCE.md) records the source
hashes and the report-only modular-rational conversion correction; superseded
code, intermediate erroneous output and empty stderr files are not imported.
This is one-session exact arithmetic and analytical proof with result
exposure, NOT a blind second-agent confirmation or a public two-architecture
probe. [replay.py](replay.py) checks these archived bytes without adding a
scientific claim. The repository's ordinary notes-only checks do not execute
these SymPy audits and must not be cited as their two-architecture validation.

The general toral-entropy formula is an external standard mathematical
comparison. One primary research source restating it is 'Symplectic partially hyperbolic
automorphisms of 6-torus', Journal of Geometry and Physics, article
S0393044023002905, Theorem1.2 (Bowen). This source is not used for any of the
new arithmetic results above.

Public authority: mathorn1973/twist-j main
 e7fe4e38048cdb6019df0599b47ad20a952475a9;
Public Canon v103, content01fb76f6b3b14a6a5ec05d0017ea922390ab6f66;
Canon SHA256 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. Normative hashes, policy/canon/ledger/gate checks and existing
public architecture checks passed. This establishes the comparison basis,
not the scientific status of this new candidate.
