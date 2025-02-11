from Bio import SeqIO
INF=int(1e9)
s,t = map(lambda x : x.seq, SeqIO.parse('./testcase/rosalind_mgap.txt', 'fasta'))
n,m = len(s),len(t); dp = [[-INF for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1): dp[i][0] = -i
for i in range(1,m+1): dp[0][i] = -i
for i in range(n+1):
    for j in range(m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
        dp[i][j] = max(dp[i][j],dp[i-1][j]-1,dp[i][j-1]-1)
ans=0
while n > 0 or m > 0:
    if n > 0 and dp[n][m] == dp[n-1][m]-1: n-=1;ans+=1
    elif m > 0 and dp[n][m] == dp[n][m-1]-1: m-=1;ans+=1
    else: n-=1;m-=1
print(ans)