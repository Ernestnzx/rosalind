with open('./testcase/rosalind_2sum.txt','r') as f:
    k,n = map(int,f.readline().split())
    for _ in range(k):
        a = list(map(int,f.readline().split()))
        d = {}
        for i in range(n-1):
            for j in range(i+1,n):
                d[a[i]+a[j]] = (i,j)
        ans = []
        for i in range(n):
            if -a[i] in d:
                j,k=d[-a[i]]
                if i != j != k:
                    ans = [i+1,j+1,k+1]
                    break
        print(*(ans if ans else [-1]))
