from math import factorial
with open('./testcase/rosalind_cunr.txt','r') as f:
    n = int(f.readline())
    print(factorial(2*n-4)//(factorial(n-2)*2**(n-2))%int(1e6))