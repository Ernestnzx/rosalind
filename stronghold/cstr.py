with open('./testcase/rosalind_cstr.txt','r') as f:
    dnas = [s.strip() for s in f.readlines()]
    n,m = len(dnas),len(dnas[0])
    for i in range(m):
        c,ct,a,b = dnas[0][i],[],0,0
        for j in range(n):
            ct.append('1' if dnas[j][i] == c else '0')
            a += dnas[j][i] == c; b += dnas[j][i] != c
        if (a >= 2 and b >= 2): print(''.join(ct))