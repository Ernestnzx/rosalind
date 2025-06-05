from Bio import SeqIO
arr = list(map(lambda x:x.seq,SeqIO.parse('./testcase/temp.txt','fasta')))
a,b,c,d,INF = len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),int(1e9)
dp = [[[[-INF for _ in range(d+1)] for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
def sp_score(idx):
    n,ans = len(idx),0
    for i in range(n-1):
        for j in range(i+1,n):
            a = '-' if idx[i] == 0 else arr[i][idx[i]-1]
            b = '-' if idx[j] == 0 else arr[j][idx[j]-1]
            ans += 0 if a == b else -1
    return ans
dp[0][0][0][0] = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            for l in range(d+1):
                for x in range(1,1<<4):
                    ts = [x >> y & 1 for y in range(4)]
                    pi,pj,pk,pl = i-ts[0],j-ts[1],k-ts[2],l-ts[3]
                    if pi < 0 or pj < 0 or pk < 0 or pl < 0: continue
                    dp[i][j][k][l] = max(
                        dp[i][j][k][l],
                        dp[pi][pj][pk][pl] + sp_score([i*ts[0],j*ts[1],k*ts[2],l*ts[3]]))
i,j,k,l = a,b,c,d
s,t,u,v = [],[],[],[]
while i or j or k or l:
    for x in range(1,1<<4):
        ts = [x >> y & 1 for y in range(4)]
        pi,pj,pk,pl = i-ts[0],j-ts[1],k-ts[2],l-ts[3]
        if pi < 0 or pj < 0 or pk < 0 or pl < 0: continue
        if dp[i][j][k][l] == dp[pi][pj][pk][pl] + \
                sp_score([i*ts[0],j*ts[1],k*ts[2],l*ts[3]]):
            s.append('-' if ts[0] == 0 else arr[0][i-ts[0]]); i -= ts[0]
            t.append('-' if ts[1] == 0 else arr[1][j-ts[1]]); j -= ts[1]
            u.append('-' if ts[2] == 0 else arr[2][k-ts[2]]); k -= ts[2]
            v.append('-' if ts[3] == 0 else arr[3][l-ts[3]]); l -= ts[3]
print(dp[a][b][c][d],''.join(s[::-1]),''.join(t[::-1]),''.join(u[::-1]),''.join(v[::-1]),sep='\n')
