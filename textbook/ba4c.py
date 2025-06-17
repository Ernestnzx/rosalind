with open('./testcase/rosalind_ba4c.txt','r') as f:
    p = f.readline().strip()
    mass_table = {
        i.split()[0] : int(i.split()[1][:-6]) 
        for i in open('./testcase/mass_table.txt','r').readlines()
    }
    n,pm = len(p),sum(mass_table[c] for c in p)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] += prefix[i] + mass_table[p[i]]
    ans = [0,pm]
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans.append(prefix[j]-prefix[i])
            ans.append(pm-(prefix[j]-prefix[i]))
    print(*sorted(ans))
