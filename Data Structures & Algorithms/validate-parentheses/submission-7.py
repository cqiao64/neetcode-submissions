class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_p = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in valid_p:
                if stack and stack[-1] == valid_p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack: 
            return True 
        else:
            return False