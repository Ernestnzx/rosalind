with open('./testcase/rosalind_scsp.txt','r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
n,m=len(s),len(t)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]: dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
i,j,lcs = n,m,[]
while i and j:
    if s[i-1] == t[j-1]:
        lcs.append((i-1,j-1));i -= 1;j -= 1
    elif dp[i-1][j] > dp[i][j-1]: i -= 1
    else: j -= 1
i=j=0
ans,lcs = [],lcs[::-1]
for a,b in lcs:
    while i < a: ans.append(s[i]); i+=1
    while j < b: ans.append(t[j]); j+=1
    ans.append(s[i]); i+=1; j+=1
while i < n: ans.append(s[i]); i+=1
while j < m: ans.append(t[j]); j+=1
print(''.join(ans))