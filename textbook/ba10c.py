with open('./testcase/rosalind_ba10c.txt','r') as f:
    # Manually removing lines with '-' and table labels
    x = f.readline().strip()
    alphabet = f.readline().split()
    states = f.readline().split()
    n,m = len(x),len(states)
    trans = [[float(i) for i in f.readline().split()] for _ in range(m)]
    emit = [[float(i) for i in f.readline().split()] for _ in range(m)]
    prob = [[0]*m for _ in range(n)]; prev = [[-1]*m for _ in range(n)]
    for s in range(m): prob[0][s] = 1/m * emit[s][alphabet.index(x[0])]
    for t in range(1,n):
        idx = alphabet.index(x[t])
        for s in range(m):
            for r in range(m):
                new_prob = prob[t-1][r] * trans[r][s] * emit[s][idx]
                if new_prob > prob[t][s]: prob[t][s],prev[t][s] = new_prob,r                
    path = [0]*n
    path[n-1] = prob[n-1].index(max(prob[n-1]))
    for t in range(n-2,-1,-1):
        path[t] = prev[t+1][path[t+1]]
    print(''.join(states[i] for i in path))