class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            if i in [")", "}", "]"]:
                if len(stack) == 0:
                    return False
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return false
        if stack == []:
            return True
        else:
            return False