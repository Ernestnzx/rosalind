n,m=map(int,open('./testcase/rosalind_aspc.txt','r').readline().split())
dp,MOD=[[0 for _ in range(n+1)] for _ in range(n+1)],int(1e6)
for i in range(n): dp[i][0] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%MOD
ans=0
for i in range(m,n+1):
    ans = (ans+dp[n][i])%MOD
print(ans)