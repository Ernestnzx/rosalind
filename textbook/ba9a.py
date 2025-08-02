class Node:
    def __init__(self,id):
        self.neigh = {}
        self.id = id
        self.is_word = 0

class Trie:
    def __init__(self,patterns):
        self.root = Node(0)
        self.size = 1
        for pattern in patterns:
            curr = self.root
            for c in pattern:
                if c not in curr.neigh:
                    curr.neigh[c] = Node(self.size)
                    self.size += 1
                curr = curr.neigh[c]
            curr.is_word = 1

    def traverse(self,u=None):
        if not u: u = self.root
        for k,v in u.neigh.items():
            print(f'{u.id}->{v.id}:{k}')
            self.traverse(v)

with open('./testcase/rosalind_ba9a.txt','r') as f:
    Trie([s.strip() for s in f.readlines()]).traverse()
