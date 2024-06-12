# Exercise 13

### Prime Number Checker

One of the exercises included in this repository is to create a function that checks whether a given number is prime. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

### Steps to Implement the Prime Number Checker:

1. Define the Function

   - Create a function named `is_prime` that accepts one argument: `x`.

2. Check if Number is Less Than 2

   - Inside the function, add a condition to check if `x` is less than 2. If it is, return `False`.

3. Iterate and Check Divisibility

   - Use a for loop to iterate over a range of numbers from 2 to `x - 1`.
   - Inside the loop, use an if statement to check if `x` is divisible by the current number (n).
   - If `x` is divisible by `n`, return `False`.

4. Return True for Prime Numbers

   - If the loop completes without finding any divisors, return `True`.
