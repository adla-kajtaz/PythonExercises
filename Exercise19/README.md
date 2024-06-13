# Exercise 19

### Remove Duplicates Function

One of the exercises included in this repository is to create a function that removes duplicate elements from a list.

### SSteps to Implement the Remove Duplicates Function:

1. Define the Function

   - Create a function named `remove_duplicates` that accepts one argument: `inputlist`.

2. Handle Empty List

   - Check if `inputlist` is empty and return an empty list if true.

3. Sort the List

   - Use the `sorted()` function to sort `inputlist`.

4. Remove Duplicates

   - Initialize `outputlist` with the first element of the sorted list.
   - Iterate through `inputlist` and add elements to `outputlist` only if they are greater than the last element in `outputlist`.

5. Return the Result

   - Return `outputlist`.
