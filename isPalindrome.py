def isPalindrome(x: int):
  if x < 0: # Negative numbers are not palindromes
    return False

  # Convert the integer to a string to check for palindrome property
  str_x = str(x)
  reverse = str_x[::-1] # Reverse the string

  # Check if the reversed string is equal to the original string
  if str_x == reverse:
    return True
  else:
    return False

case_1 = 121
result = isPalindrome(case_1)
print(result)

case_2 = -121
result = isPalindrome(case_2)
print(result)

case_3 = 10
result = isPalindrome(case_3)
print(result)

case_4 = 0 # Test case for 0
result = isPalindrome(case_4)
print(result)
