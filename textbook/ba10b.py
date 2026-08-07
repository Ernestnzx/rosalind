with open('./testcase/rosalind_ba10b.txt','r') as f:
    x = f.readline().strip(); f.readline()
    a = f.readline().strip().split(); f.readline()
    y = f.readline().strip(); f.readline()
    b = f.readline().strip().split(); f.readline(); f.readline()
    t = [[float(j) for j in i.split()[1:]] for i in f.readlines()]
    n,ans = len(x),1
    for i in range(n):
        ans *= t[b.index(y[i])][a.index(x[i])]
    print(ans)