# Exercise 20

### Censor Function

One of the exercises included in this repository is to create a function that censors a specific word in a given text.

### SSteps to Implement the Censor Function:

1. Define the Function

   - Create a function named `censor` that accepts two arguments: `text` and `word`.

2. Split the Text

   - Use the `split()` method to split text into a list of words.

3. Create Asterisks

   - Create a string of asterisks (`stars`) with the same length as the `word`.

4. Replace the Word

   - Initialize a counter to keep track of the current word index.
   - Use a `for` loop to iterate through the list of words.
   - If a word matches the `word`, replace it with the `stars`.

5. Join the Words

   - Use the `join()` method to join the list of words back into a single string, with spaces in between.

6. Return the Result

   - Return the resulting censored text.
