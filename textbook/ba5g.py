with open('./testcase/rosalind_ba5g.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m = len(s),len(t);
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1): dp[i][0] = i
    for i in range(1,m+1): dp[0][i] = i
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = min(dp[i-1][j-1]+(s[i-1]!=t[j-1]),dp[i][j-1]+1,dp[i-1][j]+1)
    print(dp[n][m])
    