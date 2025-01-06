with open('./testcase/rosalind_fibd.txt','r') as f:
    n,m=map(int,f.readline().split())
    fib=[1 for _ in range(n)]
    for i in range(2,n):
        fib[i] = fib[i-1]+fib[i-2]-(0 if i < m else fib[i-m-1])
    print(fib[n-1])
