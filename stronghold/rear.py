from collections import deque
with open('./testcase/rosalind_rear.txt','r') as f:
    lines = [tuple(map(int,line.split())) for line in f.readlines() if line.strip()]
    for i in range(0,len(lines),2):
        s,t = lines[i],lines[i+1]
        if s == t: print(0,end=' '); continue
        q1,q2,d1,d2 = deque([s]),deque([t]),{s:0},{t:0}

        def bfs(q,d,t):
            u = q.popleft()
            for i in range(10):
                for j in range(i+1,10):
                    v = u[:i]+u[i:j+1][::-1]+u[j+1:]
                    if v not in d:
                        d[v] = d[u]+1
                        q.append(v)
                        if v in t: return (1,d[v]+t[v])
            return (0,d[u])

        f1,f2,ans=0,0,0
        while q1 or q2:
            if f1 <= f2: 
                v,f1 = bfs(q1,d1,d2)
                if v: ans = f1; break
            else: 
                v,f2 = bfs(q2,d2,d1)
                if v: ans = f2; break
        print(ans,end=' ')
