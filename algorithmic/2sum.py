with open('./testcase/rosalind_2sum.txt','r') as f:
    k,n=map(int,f.readline().split())
    for _ in range(k):
        arr,comp,ans = list(map(int,f.readline().split())),{},None
        for i in range(n):
            if -arr[i] not in comp: comp[arr[i]] = i+1
            else: ans = (comp[-arr[i]],i+1)
        if ans: print(ans[0],ans[1])
        else: print(-1)
