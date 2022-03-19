'''
Given n, print all valid parenthesis
'''

class Parenthesis:
    def __init__(self, size) -> None:
        self.n = size
        self.result = []
    def printall(self, op = 0, close = 0, st = []):
        if op == close == self.n:
            self.result.append(''.join(st))
        if op < self.n:
            st.append('(')
            self.printall(op+1,close,st)
            st.pop()
        if close < op:
            st.append(')')
            self.printall(op,close+1,st)
            st.pop()
        
p = Parenthesis(int(input()))
p.printall()
print(p.result)



        
        



