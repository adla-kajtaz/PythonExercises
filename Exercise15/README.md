# Exercise 15

### Purify Function

One of the exercises included in this repository is to create a function that removes all odd numbers from a list and returns a new list containing only the even numbers.

### Steps to Implement the Purify Function

1. Define the Function

   - Create a function named `purify` that accepts one argument: `numbers`, which is a list of integers.

2. Initialize a New List:

   - Inside the function, initialize an empty list `new_list` to hold the even numbers.

3. Iterate Over the Input List:

   - Use a for loop to iterate over each element in the `numbers` list.
   - For each element in the list, check if it is even by using the modulo operator (%).

4. Append Even Numbers:

   - If an element is even (i.e., `number % 2 == 0`), append it to `new_list`.

5. Return the New List:

   - After the loop completes, return the `new_list`.
