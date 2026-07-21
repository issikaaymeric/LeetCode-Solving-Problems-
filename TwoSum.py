from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for x in range(len(nums)):
      for y in range(x+1, len(nums)):
        if nums[x] + nums[y] == target:
          return [x, y]
    return None, None 


sol = Solution()
# Case 1
case1 = sol.twoSum([2, 7, 11, 15], 9)
print(case1)

# Case2
case2 = sol.twoSum([3, 2, 4], 6)
print(case2)

# Case3
case3 = sol.twoSum([3, 3], 6)
print(case3)
