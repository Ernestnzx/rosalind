from math import perm
n,k=map(int,open('./testcase/rosalind_pper.txt','r').readline().split())
print(perm(n,k)%1000000)