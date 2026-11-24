# Finite S2 extension: microscopic real Gauss mixing and conserved Z5 winding

**Status:** PUBLIC; NON-CANONICAL; candidate-T finite L4 proof extension, not accepted Canon.  
**Author:** A. M. Thorn.  
**Date:** 21 September 2026.  
**Source:** The finite transfer and polar unitary defined in the supplied `TRANSFER.md`, especially equations (13), (14), (20), and (21).  
**Scope:** Finite lattices only. No photon no-go, mass-gap theorem, infrared limit, native-U identification, or change to the fixed action or decision predicates.

This extension preserves the model and the previously hashed TRANSFER.md and audit.py. It derives additional consequences of the same finite transfer. The main new statement is that exact real Gauss law is not a preserved microscopic subspace of this transfer. Nevertheless, global winding modulo five is preserved exactly.

## 1. Definitions inherited from the finite proof

Let `N>=2`, `V_N=(Z/NZ)^3`, and let `E_N` consist of the positively oriented, labeled links `(x,i)`. Labels remain distinct at `N=2`. Let `P_s` be the positively oriented spatial plaquettes, indexed by `(x,i,j)` with `i<j`. Write

    e=|E_N|=3N^3,    p=|P_s|=3N^3,
    S_N={r in {0,+1,-1}^{E_N}: partial r=0 mod 5},
    partial r(x)=sum_i [r(x-e_i,i)-r(x,i)].

Use the orthonormal character basis `chi_r` of the carrier `S=span{chi_r:r in S_N}`. The finite transfer in this basis is

    Ttilde(r',r)=sqrt(ell(r')ell(r)) b(r'-r)/Lambda_N,
    ell(r)=10^(e-|supp r|) 5^|supp r|,
    b(delta)=sum_{n in {0,+1,-1}^{P_s}: partial_s n=delta mod 5}
                 2^(p-|supp n|).

Here `Lambda_N` is the largest eigenvalue of `mathbbT=M L M`. The matrix `Ttilde` is real symmetric, entrywise nonnegative, strictly positive definite as an operator, and has largest eigenvalue one, which is simple. It is unitarily equivalent to the normalized transfer `T` through the common polar unitary `Ucal` of the source proof.

Define the microscopic real Gauss operators on `S` by

    Gamma_x chi_r=-(partial r)(x) chi_r.

They correspond under `Ucal` to `(partial X)(x)`. Their joint zero subspace is

    R_N=span{chi_r: partial r=0 over the integers},

with orthogonal projection `P_R`. Thus `R_N` is a specified subspace of the actual finite carrier, not an additional constraint imposed on the transfer.

For a link, let `u_(x,i)` denote its unit integer edge field. Fix the plaquette boundary convention

    partial_s p_(x,i,j)
      =u_(x,i)+u_(x+e_i,j)-u_(x+e_j,i)-u_(x,j).

This convention satisfies `partial partial_s=0` over the integers. Reversing every plaquette orientation changes the corresponding coefficients below, but not the result.

## 2. Four plaquettes couple zero field to the 13-edge junction

**Proposition 1.** For every `N>=3`, the real Gauss subspace `R_N` is not invariant under `Ttilde`, or under `Htilde=-log Ttilde`. There is an explicit positive matrix element from zero field to the 13-edge junction of the source proof.

**Proof.** Put `A=(0,0,0)`, `B=A+e_x`, and `u=u_(A,x)`. Let `P_y+`, `P_y-`, `P_z+`, and `P_z-` denote the integer edge flows on the four directed detours

    (y,x,-y), (-y,x,y), (z,x,-z), (-z,x,z)

from `A` to `B`. Each detour is a signed sum of its three labeled links. The existing junction is

    r=u+P_y+ +P_y- +P_z+ +P_z-.

For `N>=3`, these five paths have pairwise disjoint labeled edges, so `r` has exactly 13 nonzero links, each equal to `+1` or `-1`. It satisfies

    partial r(A)=-5,    partial r(B)=+5,
    partial r(x)=0 otherwise.

In particular `r in S_N` but `chi_r` is orthogonal to `R_N`.

Take the signed four-plaquette field

    n=-p_(A,x,y)+p_(A-e_y,x,y)
      -p_(A,x,z)+p_(A-e_z,x,z).

The four plaquette labels are distinct. Directly from the displayed boundary convention,

    partial_s[-p_(A,x,y)]       =P_y+ -u,
    partial_s[ p_(A-e_y,x,y)]   =P_y- -u,
    partial_s[-p_(A,x,z)]       =P_z+ -u,
    partial_s[ p_(A-e_z,x,z)]   =P_z- -u.

Consequently

    partial_s n=r-5u,
    partial_s n=r mod 5.

Thus `n` is one admissible term in `b(r)`. Every term in `b` is nonnegative, and this particular term has four nonzero plaquettes. Hence

    b(r)>=2^(p-4)>0.                                      (F1)

Because `ell(0)=10^e` and `ell(r)=10^e 2^(-13)`,

    Ttilde(r,0)>=10^e 2^(p-21/2)/Lambda_N>0.              (F2)

For an entirely explicit bound, use `max W=4`, `||M||^2<=4^p`, and `||L||=10^e`. Therefore `Lambda_N<=4^p 10^e`, and

    Ttilde(r,0)>=2^(-p-21/2).                            (F3)

Since `chi_0 in R_N` and `chi_r` is orthogonal to `R_N`,

    ||(I-P_R) Ttilde chi_0||>=2^(-p-21/2)>0.             (F4)

This proves non-invariance under `Ttilde`. If `R_N` were invariant under the self-adjoint operator `Htilde`, it would also be invariant under `exp(-Htilde)=Ttilde`, a contradiction. Thus it is not invariant under `Htilde` either. The same assertions hold on the original physical-support candidate after conjugating by `Ucal`. QED.

The local commutator can also be exhibited directly:

    [Gamma_A,Ttilde](r,0)=5 Ttilde(r,0) != 0.             (F5)

It follows that `[Gamma_A,Htilde]` is nonzero, although this argument does not claim that its particular `(r,0)` matrix element is nonzero. The construction can be translated to any vertex.

The bounds in (F3)-(F4) depend strongly on `N`: `p=3N^3`. They are finite positivity bounds, not evidence of a nonvanishing thermodynamic or continuum effect. This proposition is stated only for `N>=3`; it does not use a degenerate `N=2` version of the four-detour witness.

## 3. The unique finite ground state has real-Gauss fluctuations

**Proposition 2.** For every `N>=3` and each vertex `x`, the unique normalized ground state of `Htilde` has

    <Gamma_x>=0,    <Gamma_x^2> > 0.                    (F6)

Thus the finite ground state itself is not in `R_N`. This is a microscopic statement about the fixed operators, not a statement about their possible infrared limits.

**Proof.** Let `psi(a)>0` be the normalized Perron eigenvector of the original strictly entrywise positive transfer `mathbbT`, so `T psi=psi`. Set `v=Ucal psi`, the unique normalized eigenvector of `Ttilde` with eigenvalue one. Its zero-label component is

    v_0=Lambda_N^(-1/2) sqrt(ell(0)) <chi_0,M psi> > 0,   (F7)

because `chi_0`, `M`, and `psi` are strictly positive pointwise.

Entrywise nonnegativity of `Ttilde` implies

    1=<v,Ttilde v> <= <|v|,Ttilde |v|> <= 1.

The last inequality uses its largest eigenvalue one and `||v||=|| |v| ||=1`. Equality implies that `|v|` is also a top eigenvector. Simplicity and `v_0>0` then give `v=|v|`: every coefficient is nonnegative.

For the junction from Proposition 1, the eigenvector equation and (F3) yield

    v_r=sum_s Ttilde(r,s) v_s
        >=Ttilde(r,0) v_0
        >=2^(-p-21/2) v_0>0.

Therefore

    <v,Gamma_A^2 v> >=25 v_r^2
                    >=25 2^(-2p-21) v_0^2>0.            (F8)

The construction at any other vertex gives the same strict conclusion there. No volume-independent lower bound is asserted.

Finally `b(-delta)=b(delta)` by `n -> -n`, and `ell(-r)=ell(r)`. Thus charge conjugation `C chi_r=chi_(-r)` commutes with `Ttilde`. Simplicity of the ground state and `v_0>0` imply `Cv=v`. Since `C Gamma_x C=-Gamma_x`, the first moment vanishes. Together with (F8), this proves (F6). QED.

A zero first moment is therefore not an exact real Gauss constraint: the strictly positive second moment distinguishes them. Conversely, finite microscopic fluctuations by themselves do not exclude an emergent constraint after projection, coarse graining, or a prescribed limiting construction.

## 4. Global winding modulo five is exactly preserved

For each direction `i`, fix a transverse cut and define

    w_i(r)=sum_{x:x_i=0} r(x,i) mod 5.                  (F9)

For `r in S_N`, changing the cut position leaves this value unchanged modulo five: sum `partial r=0 mod 5` over the slab between the two cuts. Write `w(r)=(w_x,w_y,w_z) in F_5^3`, and

    S_w=span{chi_r:r in S_N, w(r)=w}.

**Proposition 3.** For every `N>=2`, all 125 spaces `S_w` are nonzero, and

    S=direct_sum_{w in F_5^3} S_w,
    Ttilde S_w subset S_w,
    Htilde S_w subset S_w.                             (F10)

**Proof.** A plaquette boundary has zero signed flux through every transverse cut. Thus, if `b(r'-r)>0`, the relation `r'-r=partial_s n mod 5` gives `w(r')=w(r)`. The matrix elements of `Ttilde` between different winding sectors are therefore zero. Functional calculus gives the same conclusion for `Htilde`.

To see that every sector occurs, represent each desired component in `{0,+1,-1,+2,-2}`. In each direction use zero, one, or two parallel coordinate winding loops, with the appropriate sign. There are `N^2>=4` available parallel loops in each direction. Different directions use distinct edge labels; crossings at vertices do not affect divergence cancellation. The resulting edge field remains ternary, has zero integer divergence, and realizes the prescribed three winding values modulo five. QED.

Equivalently, the three commuting unitary operators

    W_i chi_r=exp(2*pi*i*w_i(r)/5) chi_r

commute with `Ttilde` and `Htilde`. Their conjugates by `Ucal` are corresponding conserved operators on the physical-support candidate. This is a decomposition into conserved global labels; no irreducibility within a sector or completeness of this list of symmetries is asserted.

The unique ground state belongs entirely to `S_(0,0,0)`: it has `v_0>0`, and a nonzero projection into another invariant winding sector would supply a second eigenvector with eigenvalue one. The junction in Proposition 1 also has zero winding modulo five because it is a plaquette boundary modulo five. Thus the local real-Gauss mixing and ground-state fluctuations already occur within the trivial global winding sector.

## 5. Consequence for subsequent work and promotion scope

The following finite statements can be proposed together for independent mathematical review:

1. The existing transfer is positive and has support `M S`; its normalized electric operators have the exact common-unitary representation and norm proved in the source note.
2. The microscopic integer Gauss-zero carrier is not preserved by that transfer for `N>=3`.
3. Its unique finite ground state has zero mean but strictly positive variance of microscopic real divergence at every vertex.
4. Global winding modulo five is nevertheless conserved in 125 nonempty sectors.

Selecting the integer Gauss-zero subspace by hand is consequently an additional model change: it is not an invariant restriction already supplied by the fixed transfer. Any proposed emergence of real transversality must identify the limiting or effective observables and states and prove how the unwanted microscopic divergence disappears in that construction.

None of these finite statements decides whether the prescribed infinite-volume and scaling procedure produces a massless pole, two polarizations, or a nonzero residue. In particular (F3) and (F8) do not supply a lower bound that survives those limits. They do not constitute a photon no-go and do not justify changing an existing phase or photon-pole acceptance predicate. Canon promotion remains a separate review and acceptance decision.

Original new text: Apache-2.0. No new computational evidence or imported theorem is used.
