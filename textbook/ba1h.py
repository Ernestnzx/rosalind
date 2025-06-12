with open('./testcase/rosalind_ba1h.txt','r') as f:
    t,s,d = f.readline().strip(),f.readline().strip(),int(f.readline())
    n,m,ans = len(s),len(t),[]
    for i in range(n-m+1):
        u = s[i:i+m]
        if sum(a!=b for a,b in zip(u,t)) <= d:
            ans.append(i)
    print(*ans)