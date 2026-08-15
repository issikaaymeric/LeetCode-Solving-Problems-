from typing import List

class Solution():
  def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
      return 0

    for i in range(len(nums) - 1, 0, -1):
      if nums[i] == nums[i - 1]:
        del nums[i]

    return len(nums)

sol = Solution()
case_1 = [1, 1, 2]
result = sol.removeDuplicates(case_1)
print(result)
print(case_1)

case_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = sol.removeDuplicates(case_2)
print(result)
print(case_2)
