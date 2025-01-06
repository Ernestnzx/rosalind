with open('./testcase/rosalind_fib.txt','r') as f:
    n,k=map(int,f.readline().split(' '))
    dp=[0 for _ in range(n)]
    dp[0]=dp[1]=1
    for i in range(2,n): 
        dp[i]=dp[i-1]+k*dp[i-2]
    print(dp[n-1])
