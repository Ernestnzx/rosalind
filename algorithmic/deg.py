with open('./testcase/rosalind_deg.txt','r') as f:
    n,m = map(int,f.readline().split())
    deg = [0]*n
    for _ in range(m):
        u,v = map(int,f.readline().split())
        deg[u-1] += 1; deg[v-1] += 1
    print(*deg)
