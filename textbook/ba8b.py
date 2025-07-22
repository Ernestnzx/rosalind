def d(data_point,centers,m):
    return min(sum((data_point[i]-point[i])**2 for i in range(m))**0.5 for point in centers)

def distortion(centers,data,m):
    return sum(d(data_point,centers,m)**2 for data_point in data)/len(data)

with open('./testcase/rosalind_ba8b.txt','r') as f:
    k,m = map(int,f.readline().split())
    centers = [tuple(map(float,f.readline().split())) for _ in range(k)]
    f.readline()
    data = [tuple(map(float,s.split())) for s in f.readlines()]
    print(f'{distortion(centers,data,m):.3f}')
