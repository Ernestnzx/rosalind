from Bio.Align import *
with open('./testcase/rosalind_ba5j.txt','r') as f:
    s = f.readline().strip(); t = f.readline().strip()
    n,m,INF = len(s),len(t),10**9; d = substitution_matrices.load('BLOSUM62')
    lower = [[-INF for _ in range(m+1)] for _ in range(n+1)]
    middle = [[-INF for _ in range(m+1)] for _ in range(n+1)]
    upper = [[-INF for _ in range(m+1)] for _ in range(n+1)]
    lower[0][0] = middle[0][0] = upper[0][0] = 0
    for i in range(1,n+1): lower[i][0] = middle[i][0] = -11-(i-1)
    for i in range(1,m+1): upper[0][i] = middle[0][i] = -11-(i-1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            lower[i][j] = max(lower[i-1][j]-1,middle[i-1][j]-11)
            upper[i][j] = max(upper[i][j-1]-1,middle[i][j-1]-11)
            middle[i][j] = max(lower[i][j],middle[i-1][j-1]+d[s[i-1]][t[j-1]],upper[i][j])
    i,j,st,x,y = n,m,0,[],[]
    while i or j:
        if st == 0:
            if middle[i][j] == lower[i][j]: st = 1
            elif middle[i][j] == upper[i][j]: st = 2
            else: x.append(s[i-1]); y.append(t[j-1]); i-=1; j-=1
        elif st == 1:
            x.append(s[i-1]); y.append('-')
            if lower[i][j] == lower[i-1][j]-1: i-=1
            else: i-=1; st = 0
        elif st == 2:
            x.append('-'); y.append(t[j-1])
            if upper[i][j] == upper[i][j-1]-1: j-=1
            else: j-=1; st = 0
    print(int(middle[n][m]),''.join(x[::-1]),''.join(y[::-1]),sep='\n')
