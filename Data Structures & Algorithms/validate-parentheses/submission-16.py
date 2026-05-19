class Solution:
    def isValid(self, s: str) -> bool:
        pairs={'(': ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                if pairs[stack[-1]]==i:
                    #return True
                    stack.pop()
                else: return False
                
        return len(stack)==0
               

