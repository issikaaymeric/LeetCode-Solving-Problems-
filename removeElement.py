from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k += 1

        return k

sol = Solution()
case_1 = [3, 2, 2, 3]
value = 3
result = sol.removeElement(case_1, value)
print(result)

case_2 = [0, 1, 2, 2, 3, 0, 4, 2]
value = 2
result = sol.removeElement(case_2, value)
print(result)
