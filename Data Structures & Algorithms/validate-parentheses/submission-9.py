class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if stack and c == brackets[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        return not stack