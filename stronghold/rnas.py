from functools import lru_cache
s = open('./testcase/rosalind_rnas.txt','r').readline().strip()
pairs={('A','U'),('U','A'),('C','G'),('G','C'),('U','G'),('G','U')}
@lru_cache(maxsize=None)
def f(i,j):
    if i >= j: return 1
    total = f(i+1,j)
    for k in range(i+1,j+1,1):
        if (s[i],s[k]) in pairs and k >= i+4:
            total += f(i+1,k-1)*f(k+1,j)
    return total
print(f(0,len(s)-1))