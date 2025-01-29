import numpy as np
import math
with open('./testcase/rosalind_indc.txt','r') as f:
    n,arr,p = int(f.readline()),[],0.0
    for i in range(0,2*n+1):
        p += math.factorial(2*n)/(math.factorial(i)*math.factorial(2*n-i))*math.pow(0.5,2*n)
        arr.append(round(np.log10(p),3))
    print(*arr[:-1][::-1])