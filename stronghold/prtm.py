with open('./testcase/mass_table.txt','r') as f:
    s,d=open('./testcase/rosalind_prtm.txt','r').readline().strip(),{}
    for line in f.readlines():
        line = line.strip().split()
        d[line[0]] = float(line[1])
    print(sum([d[c] for c in s]))