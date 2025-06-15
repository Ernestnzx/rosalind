with open('./testcase/rosalind_ba3d.txt','r') as f:
    k = int(f.readline()); s = f.readline().strip()
    kmer = [s[i:i+k] for i in range(len(s)-k+1)]
    al,n = {},len(kmer)
    for s in kmer:
        u,v = s[:-1],s[1:]
        if u not in al: al[u] = []
        al[u].append(v)
    print('\n'.join(f'{u} -> {','.join(v)}' for u,v in al.items()))
