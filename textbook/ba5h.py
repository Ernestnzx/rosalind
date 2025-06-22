with open('./testcase/rosalind_ba5h.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m = len(s),len(t); d = lambda x,y : 1 if x == y else -1
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # Allowing suffix of s to be considered
    for i in range(1,n+1): dp[i][0] = 0
    for i in range(1,m+1): dp[0][i] = -10**9
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j-1]+d(s[i-1],t[j-1]),dp[i][j-1]-1,dp[i-1][j]-1)
    pos,v = (),0
    # Letting prefix of s to be considered
    for i in range(n+1):
        if dp[i][m] >= v:
            v,pos = dp[i][j],(i,j)
    i,j,x,y = *pos,[],[]
    while j:
        if i and dp[i][j] == dp[i-1][j]-1:
            x.append(s[i-1]); y.append('-'); i-=1
        elif j and dp[i][j] == dp[i][j-1]-1:
            x.append('-'); y.append(t[j-1]); j-=1
        else:
            x.append(s[i-1]); y.append(t[j-1]); i-=1; j-=1
    print(dp[pos[0]][pos[1]],''.join(x[::-1]),''.join(y[::-1]),sep='\n')
