from itertools import permutations
n = int(open('./testcase/rosalind_sign.txt','r').readline())
arr = []
for perm in permutations([i+1 for i in range(n)]):
    for i in range(1<<n):
        temp = []
        for j in range(n):
            temp.append((1 if i&1<<j else -1) * perm[j])
        arr.append(temp)
print(len(arr))
for i in arr:
    for j in i:
        print(j,end=' ')
    print()