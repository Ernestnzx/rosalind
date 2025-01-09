from Bio import SeqIO
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_ctea.txt','fasta'))
n,m=len(s),len(t); 
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
count=[[0 for _ in range(m+1)] for _ in range(n+1)]
count[0][0],MOD = 1,(1<<27)-1
for i in range(max(n,m)+1): 
    dp[min(i,n)][0] = dp[0][min(i,m)]= i
    count[min(i,n)][0] = count[0][min(i,m)] = 1
for i in range(1,n+1):
    for j in range(1,m+1):
        a,b,c=dp[i-1][j-1]+(s[i-1]!=t[j-1]),dp[i-1][j]+1,dp[i][j-1]+1
        dp[i][j] = min(a,b,c)
        if dp[i][j] == a: count[i][j] += count[i-1][j-1]
        if dp[i][j] == b: count[i][j] += count[i-1][j]
        if dp[i][j] == c: count[i][j] += count[i][j-1]
        count[i][j] %= MOD
print(count[n][m])