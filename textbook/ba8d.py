from math import e

def d(x,y,m):
    return (sum((x[i]-y[i])**2 for i in range(m))**0.5)

def soft_k_means_clusterting(centers,data,k,m,beta,iter=100):
    for _ in range(iter):
        hidden_matrix = [[e**(-beta*d(x,y,m))/sum(e**(-beta*d(c,y,m)) for c in centers) for y in data] for x in centers]
        new_centers = []
        for i in range(k):
            new_center = []
            total_weight = sum(hidden_matrix[i])
            for dim in range(m):
                weighted_sum = sum(hidden_matrix[i][j]*data[j][dim] for j in range(len(data)))
                new_center.append(weighted_sum/total_weight)
            new_centers.append(new_center)
        centers = new_centers
    return [tuple(c) for c in centers]

with open('./testcase/rosalind_ba8d.txt','r') as f:
    k,m = map(int,f.readline().split())
    beta = float(f.readline())
    data = [tuple(map(float,s.split())) for s in f.readlines()]
    centers = data[:k]
    print('\n'.join(' '.join(f'{x:.3f}' for x in pt) for pt in soft_k_means_clusterting(centers,data,k,m,beta)))