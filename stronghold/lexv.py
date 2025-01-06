arr,n =[],0
with open('./testcase/rosalind_lexv.txt','r') as f:
    arr = f.readline().strip().split()
    n = int(f.readline())

def backtrack(i,s): 
    global arr,n
    print(''.join(s))
    if i == n: return
    for c in arr:
        s.append(c)
        backtrack(i+1,s)
        s.pop(-1) 
for c in arr: 
    backtrack(1,[c])