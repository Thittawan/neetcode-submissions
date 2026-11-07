class Solution:

    def matching(self, val1, val2, op):
        result = 0
        match op:
            case "+":
                result = val1 + val2
            case "-":
                result = val2 - val1
            case "*":
                result = val1 * val2
            case "/":
                result = val2 / val1
        return result


    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        total = 0
        for i in range(len(tokens)):
            num = tokens[i].replace('-', '')
            if num.isdigit():
                result.append(tokens[i])
            else:
                val1 = int(result.pop())
                val2 = int(result.pop())
                op = tokens[i]
                total = self.matching(val1, val2, op)
                result.append(total)
        print(result[0])
        return int(result[0])
        