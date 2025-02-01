from Bio import SeqIO
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_smgb.txt','fasta'))
n,m,max_v,pos=len(s),len(t),int(-1e9),(-1,-1)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
d = lambda s,t: 1 if s == t else -1
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j-1]+d(s[i-1],t[j-1]),dp[i-1][j]-1,dp[i][j-1]-1)
for i in range(n+1): 
    if dp[i][m] > max_v: 
        max_v,pos=dp[i][m],(i,m)
for i in range(m+1): 
    if dp[n][i] > max_v: 
        max_v,pos=dp[n][i],(n,i)
i,j,x,y=*pos,[],[]
while i and j:
    if dp[i][j] == dp[i-1][j]-1:
        x.append(s[i-1]);y.append('-');i-=1;
    elif dp[i][j] == dp[i][j-1]-1:
        x.append('-');y.append(t[j-1]);j-=1
    else:
        x.append(s[i-1]);y.append(t[j-1]);i-=1;j-=1
x,y = s[:i]+''.join(x[::-1])+s[pos[0]:],t[:j]+''.join(y[::-1])+t[pos[1]:]
x = '-'*(j-min(i,j))+x; x+='-'*(max(len(x),len(y))-len(x))
y = '-'*(i-min(i,j))+y; y+='-'*(max(len(x),len(y))-len(y))
assert(len(x) == len(y)) # Even black magic must obey logic
print(max_v,x,y,sep='\n')