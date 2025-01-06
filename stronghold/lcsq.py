from Bio import SeqIO
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_lcsq.txt','fasta'))
n,m=len(s),len(t)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
i,j,lcs = n,m,[]
while i and j:
    if s[i-1] == t[j-1]:
        lcs.append(s[i-1]);i -= 1;j -= 1
    elif dp[i-1][j] > dp[i][j-1]: i -= 1
    else: j -= 1
print(''.join(reversed(lcs)))
