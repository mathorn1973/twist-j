# PREREG. P-C20-TEICHMULLER-SPLIT-2

Public lock: issue [#126](https://github.com/mathorn1973/twist-j/issues/126),
created `2026-07-22T19:04:02Z` before this branch, path, commit, verifier
execution, or formal data. The issue claims exactly this probe, branch, path,
owner, and L1 scope. Its collision audit found no competing `-2` issue,
branch, probe, pull request, registry row, or note. An independent pre-pin
review then type-corrected the matrix clause from the public integer `M_J` to
its explicitly defined reduction `M_R=M_J mod 5`; the correction is recorded
in the issue body and
[comment 5050342292](https://github.com/mathorn1973/twist-j/issues/126#issuecomment-5050342292),
still before any commit, compilation, import, execution, or formal data.

Base: Public Canon v15, tag `canon-v15`, activation commit
`8f4e176c5d76f519d3493e56e438aba7856e1f01`, Canon content commit
`a850753348583e611bf7ccd5aa074030dc7e12f5`, Canon SHA-256
`53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b`,
89288 bytes, branch parent
`633940a0187f7bdac83eae5639844622ad955d9f`.

```text
LAYER:  L1 exact state and carrier arithmetic only. No lift to L2-L6.
TARGET: the exact C_4 times C_5 split of the J-cycle in the fourth
        ramified quotient, its complete root census there, the forced
        C_4 two-primary subgroup throughout the declared ramified tower,
        and the independently reconstructed mod-5 public J-STEP operator.
```

No scientific status is earned by this preregistration. Any Canon, registry,
frontier, dependency, or dictionary disposition is separate reviewed work.

## Protocol repair and known-result disclosure

`P-C20-TEICHMULLER-SPLIT-1` is quarantined and is not evidence for this
probe. Its public branch retains pin
`22b33ed99fce414f3cce53f664900610a990ef3e`, records
`e479095c422753000db4b3ff035ef29edde50630`, verifier SHA-256
`c0909d286b634edeaae867767549a5f8d98a8e80102462a10ea6b368e7ec43fe`,
and known stdout SHA-256
`5f4822f9b49d3936d98289f9374de291d2810d27daeada2a16a468670fd05e9e`
(918 bytes, `6/6 ALL PASS`). Neither frozen predecessor file is amended.

The predecessor is protocol-invalid and its broader statement is not
accepted as typed. It had no public issue before its pin; its run record
deferred the public lock until pull-request time; the same verifier bytes and
result were known from a pre-pin dry run; its all-depth proof silently changed
the declared carrier; it promoted an interpretation from a C-status row into
a proposed T clause; it made an undefined exclusivity claim about another
carrier; its dependency list omitted the direct `J-STEP [T]` input; and its
matrix leg hard-coded a matrix and audited only one basis orbit. It never
received a pull request or required GitHub leg.

This does not assert that the narrowed algebra below is false. The predecessor
result is known, so `-2` is a transparent proof-first protocol repair and
fresh reproduction, not blind discovery. Old EXPECTED, RUN, and RESULT files
are not copied. Any new difference or failure is preserved. As of this
pre-pin registration the `-2` verifier has not been compiled, imported, or
executed.

## Frozen carrier and maps

Let

```text
O       = Z[j], j = zeta_5, Phi_5(j)=j^4+j^3+j^2+j+1=0,
lambda  = 1-j,
A_m     = O/(lambda^m), m >= 1,
R       = A_4 = O/(5),
J       = 1+j^2.
```

The equality `R=A_4=O/(5)` is an equality of quotients because the ideals
`(5)` and `(lambda)^4` are equal in O; no element equality `5=lambda^4` is
asserted. In R use the ordered F_5 basis `(1,j,j^2,j^3)`. The residue map is

```text
rho_m : A_m -> A_1 = F_5,  j -> 1.
```

The public `J-STEP [T]` map on the integer lattice is

```text
step(a,b,c,d) = (a-c+d, b-c, a, b-c+d).
```

Write `M_J` for its integer matrix in the displayed basis and define, with
types kept explicit,

```text
M_R = M_J mod 5 in Mat_4(F_5) = End_F5(R).
```

No nilpotence statement about the integer matrix `M_J` is in scope.

## Frozen statement

```text
(A) MODEL    A_m is a finite local ring with residue field F_5,
             |A_m|=5^m, and maximal ideal (lambda)/(lambda^m). In R,
             rho_4(a+bj+cj^2+dj^3)=a+b+c+d mod 5; R has 625 elements,
             exactly 500 units, and x is a unit iff rho_4(x)!=0.

(B) CYCLE    In R, J^5=2, J^10=-1, J^15=3, and ord(J)=20.

(C) SPLIT    In R put t=J^5=2 and u=J^16=3J. Then ord(t)=4,
             ord(u)=5, (u-1)^4=0!=(u-1)^3, J=tu, and
             <t> intersect <u>={1}. Thus
             <J>=<t><u>=<t> x <u>, with <t> isomorphic to C_4 and
             <u> isomorphic to C_5.

(D) ROOTS    In R, mu_8(R)=mu_4(R)=F_5^*, embedded as the four nonzero
             scalar constants. Hence R has no element of order 8 and
             the two-primary subgroup of <J> is <t> isomorphic to C_4.

(E) DEPTH    For every m>=1, |A_m^*|=4*5^(m-1). The reduction
             A_m^* -> F_5^* has 5-group kernel, so the two-primary
             subgroup maps isomorphically to F_5^* and is C_4. Hence
             no A_m contains an element of order 8. The literal-scalar
             description in (D) is asserted only for R=A_4.

(F) MATRIX   Construct M_R from the four reduced public step(e_i)
             columns and independently construct multiplication by J on
             R. They agree. For all 625 vectors v,
             step(v)=M_R v=Jv. For every 0<=k<20 and every one of the
             four basis vectors e_i, M_R^k e_i=J^k e_i. In Mat_4(F_5),
             M_R has order 20, M_R^5=2I, M_R^10=-I,
             M_R^16=3M_R, (M_R-2I)^4=0!=(M_R-2I)^3; for
             U=M_R^16, (U-I)^4=0!=(U-I)^3.
```

The statement is restricted to these exact rings and maps. It makes no
decoder, physical-carrier, clock, scale, uniqueness, or L2-L6 claim and says
nothing about carriers outside the declared lambda-adic tower.

## Frozen proof

1. The cyclotomic prime above 5 is `(lambda)` and
   `(5)=(lambda)^4` as ideals. Each successive quotient
   `(lambda)^r/(lambda)^(r+1)` has five elements. Therefore `A_m` is local,
   its residue field is F_5, and `|A_m|=5^m`. An element is a unit exactly
   when its residue is nonzero. At `m=4` this gives `R=O/(5)`, the displayed
   four-coefficient model, and `4*5^3=500` units.
2. In characteristic 5 the freshman's-dream identity and `j^5=1` give
   `J^5=(1+j^2)^5=1+j^10=2`. Thus `J^10=4=-1`, `J^15=3`, and `J^20=1`.
   Every proper divisor of 20 divides 10 or 4. The first possibility is
   excluded by `J^10=-1`. If the order divided 4, then `J=J^5=2`, contrary
   to their distinct basis coordinates in R. Hence `ord(J)=20`.
3. The element `t=J^5` has order 4. The order of `u=J^16` is
   `20/gcd(20,16)=5`, and `u=J^15 J=3J`. With `j=1-lambda`,
   `u-1=3(1+j^2)-1=lambda(-1+3lambda)` in R. Its second factor has
   nonzero residue and is a unit, while `lambda^4=0!=lambda^3`; hence
   `u-1` has nilpotency index exactly 4. Also `tu=J^21=J`. The two cyclic
   subgroups have coprime orders, so their intersection is `{1}`; their
   20 products lie in `<J>` and contain J, proving the internal product.
4. Reduction gives an exact sequence
   `1 -> K_4 -> R^* -> F_5^* -> 1` with `|K_4|=5^3`. Its kernel has no
   nontrivial element of two-power order. The four nonzero scalar constants
   are fourth roots in R. Any fourth or eighth root maps injectively into
   `F_5^*`, and two such roots with the same residue have quotient in the
   odd-order kernel, so the scalar lifts are unique. Thus both root sets are
   exactly `F_5^*` and contain no element of order 8.
5. For general m the unit reduction sequence is
   `1 -> K_m -> A_m^* -> F_5^* -> 1`, with
   `|K_m|=|A_m|/5=5^(m-1)`. Consequently
   `|A_m^*|=4*5^(m-1)`. The finite abelian unit group's Sylow 2-subgroup
   maps injectively to, and has the same order as, the cyclic group
   `F_5^*`; it is therefore C_4. Lagrange excludes order 8 for every m.
6. By `J-STEP [T]`, the integer step is multiplication by J. The verifier
   nevertheless reconstructs its reduced matrix only from the four
   `step(e_i)` values and reconstructs the ring-action matrix through a
   separate multiplication routine. Equality on all four columns fixes the
   operator; the exhaustive all-vector and 80 column-power comparisons audit
   it. The matrix identities follow from (B)-(C), while
   `M_R-2I` is multiplication by `J-2=-lambda(j+1)`, whose cofactor is a
   unit; hence its index is 4. Also `U-I=3(M_R-2I)` in characteristic 5,
   so U has the same nilpotency index.

The proof, not the finite depth prefix, is the proposed basis for theorem
status. The verifier exhausts every finite claim in R and audits the exact
lattice determinant underlying the all-m proof.

## The six frozen fields

```text
EQUATION     Statements (A)-(F) exactly as written above. The novel scope is
             purely algebraic: the internal C_4 x C_5 split in R, the exact
             fourth/eighth-root census in R, the two-primary exclusion
             throughout A_m, and the independently reconstructed reduced
             public step.

CODE         verify.py, SHA-256
             5ba3680f2cca840ab458e72e8a2f0febb99c732fcacaeadd68c71c020baacd41
             (9079 bytes). Python standard library only; exact integer and
             mod-5 arithmetic; deterministic ASCII with explicit LF through
             one binary stdout write; no floats, argv or environment input,
             filesystem reads or writes, network, subprocesses, randomness,
             dynamic code, or predecessor-output input.

CARRIER      all 625 elements of R; all units and nonunits; the full J, t,
             and u cycles; the complete fourth- and eighth-root censuses;
             the lambda multiplication lattice with exact determinant audit
             for m=1..16; all 625 public-step vectors; and all four basis
             columns for every 0<=k<20. The all-m conclusion rests on the
             frozen proof, not an extrapolation from m<=16. No external data.

SYSTEMATICS  exact arithmetic throughout. The predecessor, its known result,
             and every invalidity are disclosed above but are not evidence
             or decision inputs. The new verifier has fresh labels and
             coverage, constructs both operator matrices from columns, and
             never imports the old transcript. It has not been compiled,
             imported, or executed as of this preregistration. A defect in
             PREREG.md or verify.py after the public pin invalidates this
             name: stop, preserve both files, and open a fresh named probe.

THRESHOLD    KILL the candidate if the carrier, ideal identification,
             residue, locality, unit criterion, cycle, split, root census,
             all-depth proof, two-primary conclusion, public-step type, or
             ring/matrix agreement is incorrect; if a nonconstant fourth or
             eighth root occurs in R; if an element of order 8 occurs in any
             A_m; if a declared exhaustive vector or column check fails; if
             a dependency falls below the use made here; or if any gate is
             unreconciled. A formal leg passes only with exit 0, empty
             stderr, six PASS lines, `RESULT 6/6 ALL PASS`, and exact stdout.
             The formal clean aarch64 run and required GitHub x86_64 check
             must use the pinned verifier hash and byte-identical stdout.

LAYER        L1 exact algebraic state/carrier arithmetic only. No decoder,
             boundary, support, stream, measure, physical, SI, or L2-L6 lift.
```

## Dependencies and scope firewall

Frozen public input:

```text
J-STEP [T]    the regular-representation step for multiplication by J on Z^4
```

The Canon definitions `J=1+zeta_5^2` and `M_J` as multiplication by J are
notation, not additional claims. `FIB-ROOT-TIES [T]` is only a consistency
comparison for the reduced Jordan block and is not a premise.

`TIME-QUANTUM-TOWER`, `RAMIFIED-TM-LIFT`, `PENTIT-ROOT-FACTS`, C8, and all
decoder or metrology rows are not premises. This probe supplies no reading
of its algebra and makes no exclusivity statement about another carrier.

Before the first formal execution, this file and `verify.py` must pass static
content, dependency, type, protocol, and security review, then be committed
and publicly pushed together. Their commit, SHA-256 values, byte counts, and
Git blobs must be read back on issue #126. They are immutable after that pin.
