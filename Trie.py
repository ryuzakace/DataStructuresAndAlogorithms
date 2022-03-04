class Node:
    def __init__(self):
        self.child = [0]*26
        self.eon = False
class Trie:

    def __init__(self):
        self.root = Node()

    def _return_index(self, a):
        return ord(a)-ord('a')

    def insert(self, data):
        l = len(data)
        pointer = self.root
        for i in range(l):
            ind = self._return_index(data[i])
            if not pointer.child[ind]:
                tn = Node()
                pointer.child[ind] = tn
            pointer = pointer.child[ind]
        pointer.eon = True
        return self.root

    def search(self, val):
        l = len(val)
        pointer = self.root
        for i in range(l):
            ind = self._return_index(val[i])
            if not pointer.child[ind]:
                return 'Not found'
            pointer = pointer.child[ind]
        # pointer.eon = True
        return 'Found'   
        


t = Trie()

ll = ['happy', 'happiness', 'happily', 'hop', 'apple']

for i in ll:
    t.insert(i)

ser = ['happiness','happ','ball','hop']

for i in ser:
    print(t.search(i))