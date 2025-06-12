def number_to_pattern(i,k,a='ACGT'):
    if k == 0: return ''
    return number_to_pattern(i//len(a),k-1) + a[i%len(a)]

with open('./testcase/rosalind_ba1m.txt','r') as f:
    i,k = int(f.readline()),int(f.readline())
    print(number_to_pattern(i,k))