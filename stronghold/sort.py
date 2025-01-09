from collections import deque
with open('./testcase/rosalind_sort.txt','r') as f:
    lines = [tuple(map(int,line.split())) for line in f.readlines() if line.strip()]
    for i in range(0,len(lines),2):
        s,t = lines[i],lines[i+1]
        if s == t: print(0,end=' '); continue
        q1,q2,d1,d2 = deque([s]),deque([t]),{s:0},{t:0}
        p1,p2 = {s:(s,(0,0))},{t:(t,(0,0))}

        def bfs(q,d,t,p):
            u = q.popleft()
            for i in range(10):
                for j in range(i+1,10):
                    v = u[:i]+u[i:j+1][::-1]+u[j+1:]
                    if v not in d:
                        d[v] = d[u]+1
                        p[v] = (u,(i+1,j+1))
                        q.append(v)
                        if v in t: return (1,d[v]+t[v],v)
            return (0,d[u],u)

        f1,f2,ans=0,0,0
        while q1 or q2:
            if f1 <= f2: 
                v,f1,ans = bfs(q1,d1,d2,p1)
                if v: break
            else: 
                v,f2,ans = bfs(q2,d2,d1,p2)
                if v: break
        a = ans
        path=[]
        while a != p1[a][0]:
            path.append(p1[a][1])
            a = p1[a][0]
        path = path[::-1]
        while ans != p2[ans][0]:
            path.append(p2[ans][1])
            ans = p2[ans][0]
        print(len(path))
        for swap in path:
            print(*swap)