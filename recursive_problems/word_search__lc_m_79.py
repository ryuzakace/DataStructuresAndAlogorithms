'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
'''

import json

from sympy import false, true

board = json.loads(input())
word = input()

class Solution:
    def exist(self, board, word):
        self.output = False
        
        s1 = set()
        s2 = set(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                s1.add(board[i][j])
                
        # print(s1,s2)
        if s1.intersection(s2) != s2:
            return False

        def recursion(r,c,tmp_l = [], tmp_s = ''):
            # print(tmp_s, end=' ')
            if tmp_s == word:
                # print('xx')
                # global output
                self.output = True
                return

            for i,j in [(r-1,c), (r+1,c),(r,c-1),(r,c+1)]:
                if 0<=i<len(board) and 0<=j<len(board[0]) and ((i,j) not in tmp_l) and len(tmp_s) <len(word) and (board[i][j] == list(word)[len(tmp_s)]):
                    # print('--',i,j, tmp_l)
                    tmp_l.append((i,j))
                    tmp_s = tmp_s + board[i][j]
                    recursion(i,j,tmp_l, tmp_s)
                    tmp_l.pop()
                    tmp_s = tmp_s[:-1]
        # print(list(word)[0])
        
        for i in range(len(board)):
            if self.output:
                break
            for j in range(len(board[0])):
                if board[i][j] == list(word)[0]:
                    recursion(i,j,[(i,j)], board[i][j])
        return self.output


    
