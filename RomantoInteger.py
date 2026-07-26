class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1, 5, 10, 50, 100, 500, 1000]
        roman_dict = dict(zip(symbol, value))
        # print(roman_dict)

        total = 0
        for i in range(len(s)):
            current_value = roman_dict[s[i]]
            # Check if there's a next character and if the current value is less than the next
            if i + 1 < len(s) and current_value < roman_dict[s[i+1]]:
                total -= current_value
            else:
                total += current_value
        return total

sol = Solution()

case_1 = "III"
result = sol.romanToInt(case_1)
print(result)

case_2 = "LVIII"
result = sol.romanToInt(case_2)
print(result)

case_3 = "MCMXCIV"
result = sol.romanToInt(case_3)
print(result)
