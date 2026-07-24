def longestCommonPrefix(strs):
  if not strs:
    return ""

  prefix = strs[0]
  for i in range(1, len(strs)):
    while strs[i].find(prefix) != 0:
      prefix = prefix[:-1]
      if not prefix:
        return ""
  return prefix


case_1 = ["flower","flow","flight"]
result = longestCommonPrefix(case_1)
print(result)

case_2 = ["dog","racecar","car"]
result = longestCommonPrefix(case_2)
print(result)

case_3 = ["apple", "apricot", "application"]
result = longestCommonPrefix(case_3)
print(result)

case_4 = ["a"]
result = longestCommonPrefix(case_4)
print(result)

case_5 = ["", "b"]
result = longestCommonPrefix(case_5)
print(result)

case_6 = []
result = longestCommonPrefix(case_6)
print(result)
