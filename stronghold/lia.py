from math import comb
k,n=map(int,open('./testcase/rosalind_lia.txt','r').readline().split())
N,ans = 1<<k,0
#Pr[X>=N] = 1-Pr[X<=N]
for i in range(n):
    ans += comb(N,i) * 0.25**i * 0.75**(N-i)
print(f"{1-ans:.3}")
