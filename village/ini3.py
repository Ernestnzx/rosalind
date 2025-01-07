with open('./testcase/rosalind_ini3.txt','r') as f:
    s = f.readline()
    a,b,c,d=map(int,f.readline().split())
    print(f'{s[a:b+1]} {s[c:d+1]}')