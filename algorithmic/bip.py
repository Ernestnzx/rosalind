with open('./testcase/rosalind_bip.txt','r') as f:
    tc = int(f.readline());
    for _ in range(tc):
        f.readline()
        n,m = map(int,f.readline().split())
        al,colors,is_b = [[] for _ in range(n)],[0]*n,1
        for _ in range(m):
            u,v=map(int,f.readline().split());u-=1;v-=1;
            al[u].append(v); al[v].append(u)
        def dfs(u,c):
            global is_b
            colors[u] = c
            for v in al[u]:
                if not colors[v]: dfs(v,-c)
                elif colors[u] == colors[v]:
                    is_b = 0; return
        for u in range(n):
            if not colors[u]:
                dfs(u,1)
        print(1 if is_b else -1,end=' ')
