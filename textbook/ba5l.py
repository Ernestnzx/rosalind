from Bio.Align import *

def align(s,t,d,p):
    n,m = len(s),len(t)
    x = [i*p for i in range(m+1)]
    for i in range(1,n+1):
        y = [0 for _ in range(m+1)]; y[0] = i*p
        for j in range(1,m+1):
            y[j] = max(y[j-1]+p,x[j]+p,x[j-1]+d[s[i-1]][t[j-1]])
        x = y
    return x
 
def nw(s,t,d,p):
    n,m = len(s),len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i*p
    for i in range(m+1): dp[0][i] = i*p
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j-1]+d[s[i-1]][t[j-1]],dp[i][j-1]+p,dp[i-1][j]+p)
    i,j,x,y = n,m,[],[]
    while i or j:
        if i and dp[i][j] == dp[i-1][j]+p:
            x.append(s[i-1]); y.append('-'); i-=1
        elif j and dp[i][j] == dp[i][j-1]+p:
            x.append('-'); y.append(t[j-1]); j-=1
        else:
            x.append(s[i-1]); y.append(t[j-1]); i-=1; j-=1
    return (''.join(x[::-1]),''.join(y[::-1]))
 
def hirschberg(s,t,d,p):
    if len(s) == 0: return ('-'*len(t),t)
    if len(t) == 0: return (s,'-'*len(s))
    if len(s) == 1 or len(t) == 1: return nw(s,t,d,p)
    smid = len(s)//2
    l = align(s[:smid],t,d,p)
    r = align(s[smid:][::-1],t[::-1],d,p)[::-1]
    sum = [a+b for a,b in zip(l,r)]
    tmid = sum.index(max(sum))
    lv,lw = hirschberg(s[:smid],t[:tmid],d,p)
    rv,rw = hirschberg(s[smid:],t[tmid:],d,p)
    return (lv+rv,lw+rw)

with open('./testcase/rosalind_ba5l.txt','r') as f:
    s,t = f.readline().strip(),f.readline().strip()
    d,p = substitution_matrices.load('BLOSUM62'),-5
    a,b = hirschberg(s,t,d,p);
    score = sum(d[a[i]][b[i]] if a[i] != '-' and b[i] != '-' else p for i in range(len(a)))
    print(int(score),a,b,sep='\n')
