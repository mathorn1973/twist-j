# Proof: complete quotient for total separable counter reads

**L1 exact classification.**

## 1. Intertwining reduces to checkpoint equality

Let

    R(n,x)=L^n F(x)

with L a bijection. For the public update

    U(n,x)=(n+1,g_(z(x)+2 theta_n)(x)),

the intertwining equation R o U=L o R is

    L^(n+1) F(g_(z(x)+2 theta_n)(x))
      = L^(n+1) F(x).

Since L is invertible, this is equivalent to

    F(g_(z(x)+2 theta_n)(x))=F(x).

Necessity of both frozen edge families follows already at n=0 and n=1,
because theta_0=0 and theta_1=1 and the domain is the complete product
N_0 x X. Thus every x obeys the two preregistered equalities.

Conversely theta_n is always either zero or one. If both equalities hold for
every x, the equality selected at every n holds, so R o U=L o R globally.
This proves the iff statement without using a coordinate model for E.

## 2. Universal quotient

Let G be the undirected graph whose vertices are X and whose edges are the two
required equality pairs from each x. If F satisfies the equalities, it is
constant along every edge and hence on every connected component. Conversely
an arbitrary function on the component set, pulled back to X, is constant on
every edge and is admissible.

Therefore X/~, the connected-component set of G, is the complete quotient for
all set-valued separable reads in the frozen class.

## 3. Free-linear quotient

Let V=Q^X with basis e_x and let D be the span of e_x-e_y over all graph
edges. On a connected component with m vertices, a spanning tree supplies
m-1 independent differences and every edge difference lies in their span.
Summing over components gives

    dim D = |X|-c,

where c is the number of components. Hence

    dim(V/D)=c.

This is exact graph linear algebra and requires no 15625 by 15625 matrix.
The verifier records a spanning-forest certificate with exactly |X|-c merge
edges.

## 4. Scope

The theorem is total on Omega=N_0 x F_5^6. A restricted preparation domain
can remove equality edges and therefore has a different quotient. The theorem
does not classify such restrictions.

The factor L^n is part of the declared comparison class. This proof does not
derive or select it. It decides only how much checkpoint information can
coexist with that factor while satisfying the actual public selector.
