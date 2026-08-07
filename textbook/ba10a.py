with open('./testcase/rosalind_ba10a.txt','r') as f:
    s = f.readline().strip(); n = len(s)
    for _ in range(4): f.readline()
    t = [[float(j) for j in i.split()[1:]] for i in f.readlines()]
    ans = 0.5; f = lambda x : x == 'B'
    for i in range(n-1): 
        ans *= t[f(s[i])][f(s[i+1])]
    print(ans)