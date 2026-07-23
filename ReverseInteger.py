class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MIN = -2147483648  # -2^31
        INT_MAX = 2147483647   # 2^31 - 1

        # Handle negative sign explicitly since string slicing with '-' leaves it at the end
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying by 10 and adding the digit
            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num


sol = Solution()

case_1 = 123
result = sol.reverse(case_1)
print(result)  # Output: 321

case_2 = -123
result = sol.reverse(case_2)
print(result)  # Output: -321

case_3 = 120
result = sol.reverse(case_3)
print(result)  # Output: 21
