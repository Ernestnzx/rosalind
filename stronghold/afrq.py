from math import sqrt
with open('./testcase/rosalind_afrq.txt','r') as f:
    a = [float(i) for i in f.readline().split()]
    b = [round(2*sqrt(i)-i,3) for i in a]
    print(*b)
