with open('./testcase/rosalind_ba4d.txt','r') as f:
    n = int(f.readline())
    mass_table = set(
        int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    )
    dp = [0]*(n+1); dp[0] = 1
    for i in range(1,n+1):
        for j in mass_table:
            if i - j < 0: continue
            dp[i] += dp[i-j]
    print(dp[n])
