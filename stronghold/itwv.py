with open('./testcase/rosalind_itwv.txt','r') as f:
    s = f.readline().strip()
    dna = [t.strip() for t in f.readlines()]
    n = len(dna)
    ans = [[0 for _ in range(n)] for _ in range(n)]

    def f(s,t,u):
        n,m,o=len(s),len(t),len(u)
        for i in range(n-m-o+1):
            substr = s[i:i+m+o]
            dp = [[0 for _ in range(o+1)] for _ in range(m+1)]
            dp[0][0] = 1
            for b in range(m+1):
                for c in range(o+1):
                    if b and substr[b+c-1] == t[b-1] and dp[b-1][c]: dp[b][c] = 1
                    if c and substr[b+c-1] == u[c-1] and dp[b][c-1]: dp[b][c] = 1
            if dp[m][o]: return 1
        return 0

    for i in range(n):
        for j in range(i,n):
            ans[i][j] = ans[j][i] = f(s,dna[i],dna[j])
    for i in range(n):
        for j in range(n):
            print(ans[i][j],end=' ')
        print()
