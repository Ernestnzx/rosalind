with open('./testcase/rosalind_ba5a.txt','r') as f:
    m = int(f.readline()); dp = [10**9]*(m+1)
    change = [*map(int,f.readline().split(','))]
    dp[0] = 0
    for i in range(1,m+1):
        for c in change:
            if i-c < 0: continue
            dp[i] = min(dp[i],dp[i-c]+1)
    print(dp[m])
    