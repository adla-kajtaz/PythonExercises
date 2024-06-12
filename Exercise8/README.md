# Exercise 8

### Digit Sum Calculator

One of the exercises included in this repository is a digit sum calculator. The objective of this exercise is to write a function that sums the digits of a given positive integer.

### Steps to Implement the Digit Sum Calculator:

1. Define the Function

   - Define a function named `digit_sum` that takes a single parameter `n`.

2. Initialize a Result Variable

   - Inside the function, initialize a variable `result` to `0`. This variable will store the sum of the digits.

3. Loop Through Digits

   - Use a while loop to iterate through the digits of `n` as long as `n` is greater than `0`.
   - Inside the loop:
     - Add the last digit of n to result. You can get the last digit using n % 10.
     - Remove the last digit from n by performing integer division n // 10.

4. Return the Result
   - After the loop completes, return the value of `result`.
