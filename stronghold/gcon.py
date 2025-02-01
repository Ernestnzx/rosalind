from Bio import Align, SeqIO
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_gcon.txt','fasta'))
n,m,d=len(s),len(t),Align.substitution_matrices.load('BLOSUM62')
dp = [[int(-1e9) for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1): dp[i][0] = -5
for i in range(1,m+1): dp[0][i] = -5
# Slow af implementation, maybe can keep track of previous max
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i][j],dp[i-1][j-1]+d[s[i-1]][t[j-1]])
        for k in range(j): dp[i][j] = max(dp[i][j],dp[i][k]-5)
        for k in range(i): dp[i][j] = max(dp[i][j],dp[k][j]-5)
print(int(dp[n][m]))