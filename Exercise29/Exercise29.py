def romanToInt(s: str) -> int:
    romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s)):
        current = romanValues[s[i]]
        if i+1<len(s) and current < romanValues[s[i+1]]:
            total -= current
        else:
            total += current
    return total

num1 = "III"
print(f"{num1} is : {romanToInt(num1)}")

num2 = "LVIII"
print(f"{num2} is : {romanToInt(num2)}")

num3 = "MCMXCIV"
print(f"{num3} is : {romanToInt(num3)}")
