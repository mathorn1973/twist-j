from fractions import Fraction as F

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col))%5 for col in zip(*b)] for row in a]
def inv(a):
    n=len(a); m=[[x%5 for x in row]+[int(i==j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if m[i][k])
        m[k],m[p]=m[p],m[k]
        q=pow(m[k][k],-1,5);m[k]=[x*q%5 for x in m[k]]
        for i in range(n):
            if i!=k:
                q=m[i][k];m[i]=[(x-q*y)%5 for x,y in zip(m[i],m[k])]
    return [row[n:] for row in m]
M=[[1,1,3],[0,4,4],[1,3,1]]
Mi=inv(M)
g=[[2,4,0],[4,2,4],[0,4,2]]
# Images of the three public difference-basis vectors in sl2.
images=[]
for j in range(3):
    h,e,f=[row[j] for row in Mi]
    images.append([[h,e],[f,-h%5]])
G=[]
for a in images:
    G.append([])
    for b in images:
        prod=mm(a,b);G[-1].append((prod[0][0]+prod[1][1])%5)
assert G==[[(3*x)%5 for x in row] for row in g]
print('Trace-pairing Gram in the public W5 difference basis:',G)
print('tr(Psi(x)Psi(y)) = 3 g5(x,y): all 9 basis pairs PASS')
print('This equals candidate h_plus under the fixed normalization; no physical map follows.')
