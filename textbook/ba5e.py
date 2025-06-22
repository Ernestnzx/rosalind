from Bio.Align import *

with open('./testcase/rosalind_ba5e.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m = len(s),len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    d = substitution_matrices.load(name='BLOSUM62')
    for i in range(1,n+1): dp[i][0] = -5*i
    for i in range(1,m+1): dp[0][i] = -5*i
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j-1]+int(d[s[i-1]][t[j-1]]),dp[i][j-1]-5,dp[i-1][j]-5)
    i,j,x,y = n,m,[],[]
    while i or j:
        if i and dp[i][j] == dp[i-1][j]-5:
            x.append(s[i-1]); y.append('-'); i-=1
        elif j and dp[i][j] == dp[i][j-1]-5:
            x.append('-'); y.append(t[j-1]); j-=1
        else:
            x.append(s[i-1]); y.append(t[j-1]); i-=1; j-=1
    print(dp[n][m],''.join(x[::-1]),''.join(y[::-1]),sep='\n')
    