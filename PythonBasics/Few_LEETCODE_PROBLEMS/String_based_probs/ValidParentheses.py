class Solution:
    def isValid(self, s: str) -> bool:
        # s = "()[]{}"
        stack = []
        # for i, n in enumerate(s):
        for n in s:
            # print(n)
            if n=='(' or n=='{' or n=='[':
                stack.append(n)
            else:
                 if not stack:
                    return False
                 else:
                    top = stack[-1] # stack.peek();
                    if top == '(' and n ==')' or top == '[' and n ==']' or top == '{' and n =='}':
                        stack.pop()
                    else:
                        return False
        return not stack

strVal = "()[]{}"
strVal = "()["
print(Solution().isValid(s=strVal) )

        