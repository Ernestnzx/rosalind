from math import sqrt
with open('./testcase/rosalind_sexl.txt','r') as f:
    a = [float(i) for i in f.readline().split()]
    b = [round(2*i*(1-i),3) for i in a]
    print(*b)