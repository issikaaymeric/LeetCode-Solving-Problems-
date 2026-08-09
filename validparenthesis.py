class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in "([{":
                stack.append(char)

            elif char in ")]}":
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0


sol = Solution()

case_1 = "()"
print(sol.isValid(case_1))      # True

case_2 = "()[]{}"
print(sol.isValid(case_2))      # True

case_3 = "(]"
print(sol.isValid(case_3))      # False
