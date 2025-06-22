from Bio.Align import *

with open('./testcase/rosalind_ba5f.txt') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m = len(s),len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    d = substitution_matrices.load(name='PAM250')
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(0,dp[i-1][j-1]+int(d[s[i-1]][t[j-1]]),dp[i][j-1]-5,dp[i-1][j]-5)
    pos,v = (),0
    for i in range(n+1):
        for j in range(m+1):
            if dp[i][j] > v:
                v,pos = dp[i][j],(i,j)
    i,j,x,y = *pos,[],[]
    while dp[i][j]:
        if i and dp[i][j] == dp[i-1][j]-5:
            x.append(s[i-1]); y.append('-'); i-=1
        elif j and dp[i][j] == dp[i][j-1]-5:
            x.append('-'); y.append(t[j-1]); j-=1
        else:
            x.append(s[i-1]); y.append(t[j-1]); i-=1; j-=1
    print(dp[pos[0]][pos[1]],''.join(x[::-1]),''.join(y[::-1]),sep='\n')
