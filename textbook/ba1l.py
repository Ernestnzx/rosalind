def pattern_to_number(s,a='ACGT'):
    if not s: return 0
    return len(a)*pattern_to_number(s[:-1]) + a.find(s[-1])

with open('./testcase/rosalind_ba1l.txt','r') as f:
    print(pattern_to_number(f.readline().strip()))