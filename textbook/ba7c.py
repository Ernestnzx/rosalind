from bisect import *

def compute_limb_length(d,j,n):
    i = 0 if j else 1
    return min((d[i][j]+d[j][k]-d[i][k])//2 for k in range(n) if i!=j!=k)

def attach_limb(start,end,limb,x,limb_length,t):
    global size
    dist,p = {},{}
    dist[start],p[start] = 0,start
    def dfs(u):
        for v,w in t[u]:
            if v not in dist:
                dist[v],p[v] = dist[u]+w,u
                dfs(v)
    dfs(start); u,path = end,[]
    while u != start: path.append((dist[u],u)); u = p[u]
    path.append((dist[u],u))
    path = path[::-1]
    pos = bisect_right(path,(x,-1))
    du,u = path[pos-1]; dv,v = path[pos]
    w,dx = dv-du,x-du
    if dx == 0: 
        t.setdefault(u,[]).append((limb,limb_length))
        t.setdefault(limb,[]).append((u,limb_length))
        return 
    t[u].remove((v,w)); t[v].remove((u,w))
    a = size; size += 1
    t[u].append((a,dx)); t.setdefault(a,[]).append((u,dx))
    t.setdefault(a,[]).append((v,dv-x)); t[v].append((a,dv-x))
    t[a].append((limb,limb_length)); t.setdefault(limb,[]).append((a,limb_length))

def additive_phylogeny(d,n):
    if n == 2: return {0:[(1,d[0][1])],1:[(0,d[1][0])]}
    limb_length = compute_limb_length(d,n-1,n)
    for j in range(n-1):
        d[j][n-1] = d[n-1][j] = d[j][n-1]-limb_length
    k,x = next(k for k in range(1,n-1) if d[0][k] == d[0][n-1]+d[n-1][k]),d[0][n-1]
    t = additive_phylogeny(d,n-1)
    attach_limb(0,k,n-1,x,limb_length,t)
    return t

with open('./testcase/rosalind_ba7c.txt','r') as f:
    n,d = int(f.readline()),[list(map(int,line.split())) for line in f.readlines()]
    size = n
    print(*[f'{u}->{v}:{w}' for u,neigh in sorted(additive_phylogeny(d,n).items()) for v,w in neigh],sep='\n')
