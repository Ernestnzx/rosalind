with open('./testcase/rosalind_ba5c.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m = len(s),len(t)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else: dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    i,j,ans=n,m,[]
    while i and j:
        if i and j and s[i-1] == t[j-1]:
            ans.append(s[i-1]); i-=1; j-=1
        elif j and dp[i][j] == dp[i][j-1]: j-=1
        else: i-=1
    print(''.join(ans[::-1]))
