class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        prev= ''
        for val in command:
            if val=='(' or (val==')' and prev!='('):
                prev=val
                continue
            if val==')' and prev=='(':
                res+='o'
                prev=val
                continue
            res+=val
            prev = val
        return res