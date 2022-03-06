'''
Graph class with traverse method which performs graph traversal using DFS/BFS
'''

from collections import deque

class Graph:
    def __init__(self) -> None:
        self.adj_matrix = {}
        self.visited = set()
        self.queue = deque()

    def _dfs(self,val):
        print(val,end='->')
        self.visited.add(val)
        for i in self.adj_matrix[val]:
            if i not in self.visited: self._dfs(i)


    def _bfs(self,val):
        print(val, end='->')
        self.visited.add(val)
        for i in self.adj_matrix[val]:
            self.queue.append(i)
        while self.queue:
            v = self.queue.popleft()
            if v in self.visited:
                continue
            self.visited.add(v)
            for i in self.adj_matrix[v]:
                self.queue.append(i)
            print(v, end='->')

    def create_edge(self,node1,node2): #directed node1 -> node2
        if node1 in self.adj_matrix:
            self.adj_matrix[node1].append(node2)
            self.adj_matrix[node1] = list(set(self.adj_matrix[node1]))
        else:
            self.adj_matrix[node1] = [node2]
        if node2 not in self.adj_matrix: self.adj_matrix[node2] = []
        return self.adj_matrix
    
    def traverse(self,val, criteria = 'dfs'):
        self.visited = set()
        if criteria == 'dfs':
            self._dfs(val)
        else:
            self.queue = deque()
            self._bfs(val)



graph = Graph()

edge_list  = [(1,2),(1,3),(1,4),(2,5),(2,6),(3,7),(4,8),(4,9),(5,10),(8,10)]

for i in edge_list:
    p = graph.create_edge(i[0],i[1])
print(p)
print('dfs:')
graph.traverse(1)
print('\nbfs:')
graph.traverse(1,'bfs')
