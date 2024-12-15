def isPalindrome(x: int) -> bool:
    number = x
    palindrome = 0
    while x>0:
        palindrome = palindrome * 10 + x % 10
        x //= 10
    return palindrome == number

num1 = 121
print(f"Input: x = {num1}")
print(f"Output: {isPalindrome(num1)}")

num2 = -121
print(f"Input: x = {num2}")
print(f"Output: {isPalindrome(num2)}")

num3 = 10
print(f"Input: x = {num3}")
print(f"Output: {isPalindrome(num3)}")
