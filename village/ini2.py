with open('./testcase/rosalind_ini2.txt','r') as f:
    a,b=map(int,f.readline().split())
    print(a**2+b**2)