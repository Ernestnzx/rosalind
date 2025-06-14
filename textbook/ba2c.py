with open('./testcase/rosalind_ba2c.txt','r') as f:
    s,k = f.readline().strip(),int(f.readline())
    profile = [list(map(float,s.split())) for s in f.readlines()]
    max_p,ans = 0,''
    for i in range(len(s)-k+1):
        p = 1
        for j,c in enumerate(s[i:i+k]):
            p *= profile['ACGT'.find(c)][j]
        if max_p <= p: max_p,ans=p,s[i:i+k]
    print(ans)
