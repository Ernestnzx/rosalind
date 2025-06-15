with open('./testcase/rosalind_ba3e.txt','r') as f:
    kmer = [s.strip() for s in f.readlines()]
    n,al = len(kmer),{}
    for k in kmer:
        s,t = k[:-1],k[1:]
        if s not in al: al[s] = []
        al[s].append(t)
    print('\n'.join(f'{u} -> {','.join(v)}' for u,v in al.items()))
