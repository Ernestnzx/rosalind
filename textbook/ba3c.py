with open('./testcase/rosalind_ba3c.txt','r') as f:
    dna = [s.strip() for s in f.readlines()]
    al,n = {},len(dna)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            s,t = dna[i],dna[j]
            if s[1:] == t[:-1]:
                if s not in al:
                    al[s] = []
                al[s].append(t)
    print('\n'.join(f'{u} -> {','.join(v)}' for u,v in al.items()))