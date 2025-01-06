with open('./testcase/rosalind_sq.txt','r') as f:
    tc=int(f.readline())
    for _ in range(tc):
        f.readline()
        n,m=map(int,f.readline().split())
        am = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u,v=map(int,f.readline().split());u-=1;v-=1
            am[u][v] = am[v][u] = 1
        is_sq = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if not am[i][j]: continue
                count = 0
                for k in range(n):
                    count += i != j != k and am[i][k] and am[j][k]
                if not is_sq and count > 1: is_sq = 1
        print(1 if is_sq else -1,end=' ')
        