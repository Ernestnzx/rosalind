from Bio import SeqIO
s,t = map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_oap.txt','fasta'))
n,m,INF,d = len(s),len(t),int(1e9),lambda x,y : 1 if x == y else -2
dp = [[-INF for _ in range(m+1)] for _ in range(n+1)]
for i in range(n+1): dp[i][0] = 0 # start on the suffix of s
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j-1]+d(s[i-1],t[j-1]),dp[i-1][j]-2,dp[i][j-1]-2)
ans,pos = -INF,(-1,-1)
for i in range(m+1): 
    if dp[n][i] < ans: continue
    ans,pos = dp[n][i],(n,i)
i,j,x,y = *pos,[],[]
while j:
    if i and dp[i][j] == dp[i-1][j]-2:
        x.append(s[i-1]);y.append('-');i-=1
    elif j and dp[i][j] == dp[i][j-1]-2:
        x.append('-');y.append(t[j-1]);j-=1
    else:
        x.append(s[i-1]);y.append(t[j-1]);i-=1;j-=1
print(ans,''.join(x[::-1]),''.join(y[::-1]),sep='\n')