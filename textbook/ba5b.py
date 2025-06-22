with open('./testcase/rosalind_ba5b.txt','r') as f:
    n,m = map(int,f.readline().split())
    down = [[*map(int,f.readline().split())] for _ in range(n)]
    f.readline()
    right = [[*map(int,f.readline().split())] for _ in range(n+1)]
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n): dp[i+1][0] += dp[i][0] + down[i][0]
    for i in range(m): dp[0][i+1] += dp[0][i] + right[0][i]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i][j-1]+right[i][j-1],dp[i-1][j]+down[i-1][j])
    print(dp[n][m])