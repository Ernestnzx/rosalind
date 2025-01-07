with open('./testcase/rosalind_ini6.txt','r') as f:
    s,d = f.readline().strip().split(),{}
    for w in s:
        if w not in d: d[w] = 1
        else: d[w] += 1
    for k,v in d.items():
        print(f'{k} {v}')