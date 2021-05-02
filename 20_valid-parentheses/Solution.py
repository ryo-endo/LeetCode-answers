class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)

            if c in brackets.values():
                if not stack:
                    return False
                if brackets.get(stack.pop()) != c:
                    return False

        return not stack


