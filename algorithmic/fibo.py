n = int(open('./testcase/rosalind_fibo.txt','r').readline())+1
dp = [0 for _ in range(n)]
dp[0] = 0; dp[1] = 1;
for i in range(2,n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1])
