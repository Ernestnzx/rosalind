def d(data_point,centers,m):
    return min(sum((data_point[i]-point[i])**2 for i in range(m))**0.5 for point in centers)

def farthest_first_travel(data,k,m):
    centers = [data[0]]
    while len(centers) < k:
        data_point,max_val = None,0
        for point in data:
            dist = d(point,centers,m)
            if dist > max_val:
                max_val,data_point = dist,point
        centers.append(data_point)
    return centers

with open('./testcase/rosalind_ba8a.txt','r') as f:
    k,m = map(int,f.readline().split())
    data = [tuple(map(float,s.split())) for s in f.readlines()]
    print('\n'.join(' '.join(str(i) for i in point) for point in farthest_first_travel(data,k,m)))
