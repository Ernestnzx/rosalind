# Yes, I know the O(n lg k) solution exists but it's 
# tedious so I'm using the classic DP approach :)
def subseq(arr,n,f):
    dp=[1 for _ in range(n)]
    parent=[i for i in range(n)]
    for i in range(n):
        for j in range(i+1,n): 
            if f(i,j) and dp[j] < dp[i]+1:
                dp[j] = dp[i]+1
                parent[j] = i
    ans,t=[],dp.index(max(dp))
    while parent[t] != t:
        ans.append(arr[t])
        t = parent[t]
    ans.append(arr[t])
    for i in ans[::-1]:
        print(i,end=' ')
    print()

with open('./testcase/rosalind_lgis.txt','r') as f:
    n,arr=int(f.readline()),list(map(int,f.readline().split()))
    subseq(arr,n,lambda x,y:arr[x]<arr[y])
    subseq(arr,n,lambda x,y:arr[x]>arr[y])
