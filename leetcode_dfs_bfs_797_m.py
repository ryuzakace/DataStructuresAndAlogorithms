'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3
'''

from pip import main
from sympy import li
import json


class Solution:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.final = len(self.graph) - 1
        self.answer = []

    def dfs(self, n, li):
        li.append(n)
        if n == self.final:
            print(li)
            self.answer.append(li.copy())
            return
        for i in self.graph[n]:
            self.dfs(i, li)
            li.pop()


if __name__ == "__main__":
    inp = input()
    inp_list = []
    for i in inp:
        if i == ',':
            continue
        if i == '[':
            tl = []
            continue
        if i == ']':
            inp_list.append(tl)
            continue
        tl.append(int(i))
    s = Solution(inp_list)
    s.dfs(0,[])
    print(s.answer)





