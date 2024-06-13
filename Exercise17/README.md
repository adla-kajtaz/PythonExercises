# Exercise 17

### Scrabble Score Function

One of the exercises included in this repository is to create a function that calculates the Scrabble score for a given word.

### Steps to Implement the Scrabble Score Function:

1. Define the Function

   - Create a function named `scrabble_score` that accepts one argument: `word`, which is a string representing the word to be scored..

2. Convert to Lowercase

   - Convert `word` to lowercase using the `lower()` method to handle case insensitivity.

3. Initialize the Score Dictionary

   - Define a dictionary `score` that maps each letter to its Scrabble point value.

4. Calculate the Total Score

   - Initialize a variable `total` to 0.
   - Use a for loop to iterate over each letter in `word`.
   - For each letter, add the corresponding value from the `score` dictionary to `total`.

5. Return the Total Score

   - Return the value of `total`.
