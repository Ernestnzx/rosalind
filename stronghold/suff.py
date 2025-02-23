class Node:
    def __init__(self, c, idx):
        self.alphabet = c
        self.child = [None for _ in range(5)]
        self.idx = idx

class Trie:
    def __init__(self):
        self.root = Node('#',1)
        self.size = 1

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = 'ACGT$'.find(c)
            if not curr.child[idx]:
                curr.child[idx] = Node(c,self.size+1)
                self.size += 1
            curr = curr.child[idx]
    
    def traverse(self, u=None, path=()):
        if not u: u = self.root
        size = sum(map(lambda x : 1 if x else 0, u.child))
        if size != 1:
            if path: suffix_branch.append(''.join(path))
            path = ()
        for v in u.child:
            if not v: continue
            self.traverse(v,path + (v.alphabet,))
        
s = open('./testcase/rosalind_suff.txt','r').readline().strip()
trie = Trie()
for i in range(len(s)):
    trie.insert(s[i:])
suffix_branch = []
trie.traverse()
print(*sorted(suffix_branch),sep='\n')