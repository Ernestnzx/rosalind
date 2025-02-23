from Bio import Align, SeqIO
# There are bugs in here and I can't find it...
# It passed the test case though, use it at your own risk
s,t=map(lambda x:x.seq,SeqIO.parse('./testcase/rosalind_gaff.txt','fasta'))
n,m,INF,d=len(s),len(t),int(1e9),Align.substitution_matrices.load('BLOSUM62')
V = [[0 for _ in range(m+1)] for _ in range(n+1)]
G = [[0 for _ in range(m+1)] for _ in range(n+1)]
F = [[-INF for _ in range(m+1)] for _ in range(n+1)]
E = [[-INF for _ in range(m+1)] for _ in range(n+1)]
a,b = 11,1; g = lambda l : a+b*(l-1); 
for i in range(1,n+1): 
    V[i][0] = F[i][0] = -g(i)
    E[i][0] = G[i][0] = -INF 
for j in range(1,m+1): 
    V[0][j] = E[0][j] = -g(j)
    F[0][j] = G[0][j] = -INF
for i in range(1,n+1):
    for j in range(1,m+1):
        G[i][j] = V[i-1][j-1]+int(d[s[i-1]][t[j-1]])
        F[i][j] = max(F[i-1][j]-b,V[i-1][j]-g(1))
        E[i][j] = max(E[i][j-1]-b,V[i][j-1]-g(1))
        V[i][j] = max(G[i][j],F[i][j],E[i][j])
i,j,x,y = n,m,[],[]
while i or j:
    if V[i][j] == G[i][j]:
        x.append(s[i-1]);y.append(t[j-1]);i-=1;j-=1
    elif V[i][j] == F[i][j]:
        x.append(s[i-1]);y.append('-');i-=1
    else:
        x.append('-');y.append(t[j-1]);j-=1
print(int(V[n][m]),''.join(x[::-1]),''.join(y[::-1]),sep='\n')