# Exercise 18

### Median Function

One of the exercises included in this repository is to create a function that calculates the median of a list of numbers.

### Steps to Implement the Scrabble Score Function:

1. Define the Function

   - Create a function named `median` that accepts one argument: `list`.

2. Sort the List

   - Use the `sorted()` function to sort `list` and store the result in a variable `sorted_list`.

3. Calculate the Median

   - Determine the length of the sorted list.
   - If the length is odd, return the middle element using integer division to find the index.
   - If the length is even, calculate the average of the two middle elements and return the result.
