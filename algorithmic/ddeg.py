with open('./testcase/rosalind_ddeg.txt','r') as f:
    n,m = map(int,f.readline().split())
    al,deg = [[] for _ in range(n)], [0]*n
    for _ in range(m):
        u,v = map(int,f.readline().split()); u-=1;v-=1;
        al[u].append(v); al[v].append(u)
        deg[u] += 1; deg[v] += 1
    for u in range(n):
        ans = 0
        for v in al[u]:
            ans += deg[v]
        print(ans,end=' ')
