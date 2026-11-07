class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        point = 0
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                stack.append(s[i])
            else:
                if len(stack) < 1:
                    return False
                left_brack = stack.pop()
                match left_brack:
                    case '[':
                        if s[i] != ']': return False
                    case '{':
                        if s[i] != '}': return False
                    case '(':
                        if s[i] != ')': return False
        if not stack:
            return True
        else:
            return False
        