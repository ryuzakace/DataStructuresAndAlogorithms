"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
"""
import json


visited = []

def bfs(k,l):
    q = [(k,l,1)]
    cc = 0

    if s[k][l] == 1:
        return -1
    visited.append((k,l))
    while len(q)!=0:
        print(q, cc+1)
        v = q.pop(0)
        cc+=1
        if (v[0],v[1]) == (n-1,n-1):
            return v[2]

        i,j,d = v
        for r,c in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
            if r < 0 or c < 0 or r > n-1 or c > n-1:
                continue
            if s[r][c] == 1:
                continue
            if (r,c) in visited:
                continue
            visited.append((r,c))

            q.append((r,c,d+1))

    return -1


s = json.loads(input())
n = len(s)

x = bfs(0,0)
if x == -1:
    print(-1)
else:
    print(x)