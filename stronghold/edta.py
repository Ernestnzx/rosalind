from Bio import SeqIO
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_edta.txt','fasta'))
n,m=len(s),len(t); dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(max(n,m)+1): dp[min(i,n)][0] = dp[0][min(i,m)]= i
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1]
        else: dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
i,j,a,b=n,m,[],[]
while i or j:
    if s[i-1] == t[j-1] or dp[i][j] == dp[i-1][j-1]+1:
        a.append(s[i-1]);b.append(t[j-1]);i-=1;j-=1
    elif dp[i][j] == dp[i-1][j]+1:
        a.append(s[i-1]);b.append('-');i-=1
    else:
        a.append('-');b.append(t[j-1]);j-=1
print(dp[n][m])
print(''.join(a[::-1]))
print(''.join(b[::-1]))
