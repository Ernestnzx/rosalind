from Bio import SeqIO,Align
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_loca.txt','fasta'))
n,m,d=len(s),len(t),Align.substitution_matrices.load('PAM250')
dp,max_v,pos = [[0 for _ in range(m+1)] for _ in range(n+1)],0,(-1,-1)
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(0,dp[i-1][j-1]+d[s[i-1]][t[j-1]],dp[i-1][j]-5,dp[i][j-1]-5)
        if dp[i][j] > max_v: max_v,pos=dp[i][j],(i,j)
i,j,x,y = *pos,[],[]
while dp[i][j]:
    if dp[i][j] == dp[i-1][j-1]+d[s[i-1]][t[j-1]]:
        x.append(s[i-1]);y.append(t[j-1]);i-=1;j-=1
    elif dp[i][j] == dp[i-1][j]-5:
        x.append(s[i-1]);i-=1
    else:
        y.append(t[j-1]);j-=1
print(int(max_v),''.join(x[::-1]),''.join(y[::-1]),sep='\n')