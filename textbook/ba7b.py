with open('./testcase/rosalind_ba7b.txt','r') as f:
    n,j = int(f.readline()),int(f.readline())
    d = [list(map(int,line.split())) for line in f.readlines()]
    i = 0 if j else 1
    print(min((d[i][j]+d[j][k]-d[i][k])//2 for k in range(n) if i!=j!=k))
    # O(n^2) solution
    # print(min((d[i][j]+d[j][k]-d[i][k])//2 for i in range(n-1) for k in range(i+1,n) if i!=j!=k))