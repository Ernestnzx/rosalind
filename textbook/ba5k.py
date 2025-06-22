from Bio.Align import *

def align(s,t,d,p,rev=0):
    n,m = len(s),len(t)
    x,dir = [i*p for i in range(n+1)],[-1]*(n+1)
    for i in range(1,m+1):
        y = [0 for _ in range(n+1)]; y[0] = i*p+x[0]
        for j in range(1,n+1):
            val = (y[j-1]+p,x[j]+p,x[j-1]+d[t[i-1]][s[j-1]])
            y[j] = max(val)
            dir[j] = val.index(y[j])
        x = y
    if rev: x,dir=x[::-1],dir[::-1]
    return x,dir
 
def middle_edge(s,t,d,p):
    n,m = len(s),len(t); m = m//2
    left,ldir = align(s,t[:m],d,p)
    right,rdir = align(s[::-1],t[m:][::-1],d,p,rev=1)
    total = [a+b for a,b in zip(left,right)]
    i = total.index(max(total))
    x,moves = (i,m),[(i,m+1),(i+1,m),(i+1,m+1)]
    y = moves[rdir[i]]
    return (x,y)

with open('./testcase/rosalind_ba5k.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    print(*middle_edge(s,t,substitution_matrices.load('BLOSUM62'),-5))
