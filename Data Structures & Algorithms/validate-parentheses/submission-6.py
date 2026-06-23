class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for char in s:
            if not stack and char not in map.keys():
                return False
            if char in map.keys():
                stack.append(char)
                continue
            if stack and map[stack[-1]] == char:
                stack.pop()
                continue
            if stack and map[stack[-1]] != char:
                return False
        if len(stack) == 0:
            return True
        return False

        