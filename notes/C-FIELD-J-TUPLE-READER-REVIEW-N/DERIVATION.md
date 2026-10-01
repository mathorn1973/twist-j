# Independent total tuple reader derivation

**PUBLIC, NON-CANONICAL. Prospective independent L1 proof; unexecuted.**
The admitted sources and known exposures are fixed in PREREG.md. No
successor implementation or proof enters this derivation.

## 1. Normalize storage without executing its owner's methods

Use trusted builtin bindings. The actual type of an object x is type(x);
this operation does not request x.__class__. Test issubclass(type(x),tuple).
The right-hand argument is the actual builtin tuple type, so its ordinary
type subclass test checks the actual inheritance relation. The metaclass
of the left-hand type supplies no subclass predicate to this call. In
particular this does not ask the input, its actual type or its metaclass
for a Python-level __class__, __bases__ or __mro__ attribute. An actual
tuple subclass passes, a merely claimed tuple class does not.

This distinction matters: isinstance(x,tuple) may consult a non-tuple
object's claimed __class__, and a manual type.__getattribute__(T,'__mro__')
can still dispatch a metaclass data descriptor. Neither is needed here.

For a successful membership test, tuple.__len__(x) is the builtin tuple
length operation on that actual tuple object, and tuple.__getitem__(x,i)
is the builtin slot operation for an already checked in-range builtin int
i. Explicitly selecting the base descriptors bypasses corresponding
subclass methods. No iteration, x[i], len(x), normal attribute read,
equality, hash, truth conversion or string formatting on x is performed.

Check outer storage length three, retrieve slots zero, one and two, and
require type(e0) is int and type(e1) is int. Check nested actual tuple
membership and length four in the same manner. Retrieve exactly four
slots, requiring type(r_i) is int before testing 0<=r_i<5. Therefore bool,
integer subclasses and objects with numeric conversion hooks reject before
any arithmetic or comparison on them. Failure returns None. Successful
normalization constructs (e0,e1,(r0,r1,r2,r3)) from trusted values as fresh
plain tuple literals.

This is a finite straight-line decision with at most two inheritance tests,
two length operations and seven slot reads. All calls on a potential input
are explicit builtin storage/type operations. They do not evaluate its
user hooks, even if those hooks would raise or diverge. No write is made to
the input or its metadata. Hence malformed objects reject totally and all
normalized-equivalent admitted inputs produce the same six integer values.
The statement uses the target's fixed ordinary Python runtime semantics;
resource exhaustion and deliberate builtin replacement are not objects in
the mathematical input contract.

## 2. A complete finite coefficient domain before enumeration

Put Q=sum a_i^2. The target energies are

    e0=Q-a0*a2-a0*a3-a1*a3,
    e1=Q-a0*a1-a1*a2-a2*a3.

Twice the first form has matrix

    D=[[2,0,-1,-1],[0,2,0,-1],[-1,0,2,0],[-1,-1,0,2]],
    D^-1=(1/5)[[6,2,3,4],[2,4,1,3],[3,1,4,2],[4,3,2,6]].

In coordinate order (a2,a0,a3,a1), D is the A4 path Cartan matrix.
Its leading principal minors 2,3,4,5 prove positive definiteness.
The inverse is verified by integer multiplication. Cauchy-Schwarz in the
D inner product gives a_i^2 <= (D^-1)_ii*2e0. Thus e0<=5 implies
a0^2,a3^2<=12 and a1^2,a2^2<=8. Every possible integral input scalar is
in [-3,3] x [-2,2] x [-2,2] x [-3,3], which has 1225 points.
Positive definiteness also proves that e0=0 only for a=0.

The admitted cyclotomic identities are alpha*bar(alpha)=u+v*phi with
u=e1 and v=e0-e1, and

    N(alpha)=u^2+uv-v^2=-e0^2+3e0*e1-e1^2
            =(5*e0^2-(2e1-3e0)^2)/4.

For nonzero alpha this is a positive integer, hence on e0<=5 it is in
[1,31]. Its positivity implies e1>0. If e1>=14, maximizing the norm over
0<=e0<=5 gives -25+15e1-e1^2<=-11, a contradiction. Thus every valid
nonzero key lies in [1,5] x [1,13]; the zero key has both energies zero.

## 3. Uniqueness and the exact inverse

Equal e0,e1 give equal u,v, hence the same ordered positive squared
embedding magnitudes A and B. If two nonzero scalars with this datum and
the same four residues differed, their difference gamma=5 eta would be
nonzero integral and have N(gamma)>=5^4=625. The triangle inequality at
each complex embedding instead gives N(gamma)<=16AB<=16*31=496.
This is impossible. Zero cannot collide with a nonzero scalar because
its e0 is zero. E5 is therefore injective on all K5, including zero.

After storage normalization, reject energies outside [0,5] x [0,13].
When e0=0, accept just e1=0 and four zero residues. For e0>0 require
1<=N<=31. In each coordinate retain the integers in its proved interval
having the supplied residue modulo five. The second and third intervals
have exactly one representative each; the first and fourth have at most
two. Hence at most four coefficient tuples remain. Recompute both forms
on each and keep exact matches. Return None if none, otherwise (a,Ca).
The uniqueness proof precludes more than one survivor.

All loops have fixed finite bounds, and after normalization all arithmetic
is on genuine finite ints. Therefore this inverse terminates on every
contract input. An actual scalar is in the containing box and its residue
lifts, so it survives: completeness. A returned scalar has exactly the
claimed energies and residues, and e0<=5: soundness. Uniqueness gives its
exactness. The displayed C has integral coefficients, and tuple literals
construct plain length-four outputs containing genuine ints. This proves
the complete output contract and equality for normalized-equivalent inputs.

None of this treats every corruption as invalid. The scalars 1 and j have
energies (1,1) and different valid residues. Replacing one such residue by
the other must produce the corresponding other valid scalar.

## 4. Independent audit and limits

The frozen code constructs its reference image using H(y)=y^T B_f y/2
with y=Ca and the virtual transform (I+A_f^2)y, using only the admitted
fixed matrices. The reader uses the displayed coefficient forms and
residue-lift inverse. Their agreement is checked at every box point before
the object audit. The proven containing box makes the image exhaustive.
The census, norm maximum and all bounded semantic input keys are finite
checks; the logical arguments above carry the unbounded-input and
all-subclass claims.

The hostile fixtures cover base and nested tuple subclasses, malicious
metaclasses, forged or raising __class__, all rejected scalar-slot types,
lying methods and metadata. A shared hook counter detects dispatch even if
the implementation catches a hook's exception. No actually divergent hook
is invoked to establish a negative experiment; its irrelevance follows
from the explicit base-operation proof.

This is an L1 object-contract inverse on the selected small energy sector.
It selects no apparatus, acquisition method, physical clock or codebook and
changes neither the norm-941/modulo-25 theorem nor a physical frontier owner.
