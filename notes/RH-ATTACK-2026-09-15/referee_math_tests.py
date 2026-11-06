from fractions import Fraction as F
from math import comb
def R(n): return [(-1)**(n-k)*comb(n,k)*comb(n+k+2,k+2) for k in range(n+1)]
# (a) direct a_n = sum_k b_{n,k} m_k with m_k = int_0^1 t^alpha t^{k+1} = 1/(k+2+alpha)
def a_direct(n, alpha): return sum(F(b, 1)/(k+2+alpha) for k,b in enumerate(R(n)))
# closed form from Rodrigues + n-fold parts: a_n = prod_{j=1..n}(alpha-j) / prod_{j=0..n}(alpha+2+j)
def a_closed(n, alpha):
    num=F(1); den=F(1)
    for j in range(1,n+1): num*= (alpha-j)
    for j in range(0,n+1): den*= (alpha+2+j)
    return num/den
for alpha in (F(-1,4), F(-3,8), F(-1,2)+F(1,32)):
    assert all(a_direct(n,alpha)==a_closed(n,alpha) for n in range(0,31)), alpha
print("closed form == direct Jacobi sum for n<=30, three alpha: OK")
# Parseval on g = t^{-1/4}: ||g||^2 = int t^{-1/2} = 2 ; tail 2 - S_N
alpha=F(-1,4)
S=F(0); rows=[]
for n in range(0,801):
    S+= (2*n+3)*a_closed(n,alpha)**2
    if n in (25,50,100,200,400,800): rows.append((n, float(2-S), float((2-S)*n), float((2-S)*n**0.5)))
print("DIAGNOSTIC g=t^{-1/4} (alpha=-1/4): N, 2-S_N, (2-S_N)*N, (2-S_N)*sqrt(N)")
for r in rows: print("DIAGNOSTIC  ", r)
# single-term decay exponent: alpha = -1/2 + delta, delta = eps/2, eps=1/4 -> alpha=-3/8
# lane's heuristic: (2n+3)a_n^2 ~ n^{-1-eps} = n^{-1.25}; my derivation: n^{-1-2eps} = n^{-1.5}
alpha=F(-3,8)
print("DIAGNOSTIC alpha=-3/8 (eps=1/4): n, (2n+3)a_n^2 * n^1.25 (lane), * n^1.5 (referee)")
for n in (50,100,200,400,800):
    v=float((2*n+3)*a_closed(n,alpha)**2)
    print("DIAGNOSTIC  ", n, v*n**1.25, v*n**1.5)
alpha=F(-1,2)+F(1,32)   # eps = 1/16
print("DIAGNOSTIC alpha=-15/32 (eps=1/16): n, (2n+3)a_n^2 * n^(1+1/16) (lane), * n^(1+1/8) (referee)")
for n in (50,100,200,400,800):
    v=float((2*n+3)*a_closed(n,alpha)**2)
    print("DIAGNOSTIC  ", n, v*n**(1+1/16), v*n**(1+1/8))
