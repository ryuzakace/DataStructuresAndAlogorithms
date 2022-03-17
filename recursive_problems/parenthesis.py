'''
Given n, print all valid parenthesis
'''

class parenthesis:
    def __init__(self, size) -> None:
        self.n = size
        self.result = []
    def printall(self,open = 0, close = 0, st = []):
        if open == close == self.n:
            self.result.append(''.join(st))
        if open < self.n:
            st.append('(')
            self.printall(open+1,close,st)
            st.pop()
        if close < open:
            st.append(')')
            self.printall(open,close+1,st)
            st.pop()
        
p = parenthesis(int(input()))
p.printall()
print(p.result)



        
        



