with open('./testcase/rosalind_root.txt','r') as f:
    MOD = 10**6
    def df(n): return 1 if n <= 1 else n*df(n-2)%MOD
    print(df(2*int(f.readline())-3))