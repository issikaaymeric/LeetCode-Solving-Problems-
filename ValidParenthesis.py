import re

class Solution:
  def isValid(self, s: str) -> bool:

    pattern = r"^(\(\)|\[\]|\{\})+$"

    if s not in ["()", "[]", "{}"]:
      return False

    if re.match(pattern, s):
      return True
    else:
      return False

sol = Solution()

case_1 = "()"
result = sol.isValid(case_1)
print(result)

case_2 = "()[]{}"
result = sol.isValid(case_2)
print(result)

case_3 = "(]"
result = sol.isValid(case_3)
print(result)

case_4 = "([])"
result = sol.isValid(case_4)
print(result)

case_5 = "{[]}"
result = sol.isValid(case_5)
print(result)

case_6 = "|"
result = sol.isValid(case_6)
print(result)
