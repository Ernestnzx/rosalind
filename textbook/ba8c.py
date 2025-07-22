def dist(x,y,m):
    return sum((x[i]-y[i])**2 for i in range(m))

def lloyd(data,centers,k,m):
    grav = centers[:]
    while True:
        clusters = [[] for _ in range(k)]
        for i,x in enumerate(data):
            min_d,idx = float('inf'),None
            for j,y in enumerate(grav):
                d = dist(x,y,m)
                if d < min_d:
                    min_d,idx = d,j
            clusters[idx].append(x)
        temp = [tuple(sum(c_i)/len(cluster) for c_i in zip(*cluster)) for cluster in clusters]
        if temp == grav: break
        grav = temp
    return grav

with open('./testcase/rosalind_ba8c.txt','r') as f:
    k,m = map(int,f.readline().split())
    data = [tuple(map(float,s.split())) for s in f.readlines()]
    centers = data[:k]
    print('\n'.join(' '.join(f'{x:.3f}' for x in pt) for pt in lloyd(data,centers,k,m)))
