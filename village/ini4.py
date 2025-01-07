with open('./testcase/rosalind_ini4.txt','r') as f:
    a,b=map(int,f.readline().split())
    ans = 0
    for i in range(a,b+1):
        if i&1: ans += i;
    print(ans)