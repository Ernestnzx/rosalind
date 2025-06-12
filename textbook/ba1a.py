with open('./testcase/rosalind_ba1a.txt','r') as f:
    s = f.readline().strip(); p = f.readline().strip()
    n,m,c = len(s),len(p),0
    for i in range(n-m):
        c += s[i:i+m:] == p
    print(c)