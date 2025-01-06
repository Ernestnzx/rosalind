with open('./testcase/rosalind_maj.txt','r') as f:
    k,n = map(int,f.readline().split())
    for _ in range(k):
        arr = sorted(list(map(int,f.readline().split())))
        curr,c=arr[0],1
        for i in range(1,n):
            if arr[i] == curr:
                c += 1;
                if c > n//2: break
            else:
                curr = arr[i]
                c = 1
        print(curr if c > n//2 else -1,end=' ')
