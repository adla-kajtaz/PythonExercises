# Exercise 10

### Anti-Vowel Function

One of the exercises included in this repository is to implement a function that removes all vowels from a given string.

### Steps to Implement the Anti-Vowel Function:

1. Define the Function

   - Create a function named `anti_vowel` that accepts a single argument `text`.

2. Initialize a New String

   - Inside the function, initialize an empty string `new_word` which will store the result.

3. Define Vowels

   - Define a string `vowels` containing all vowels: "aeiouAEIOU".

4. Iterate Over the Text

   - Use a for loop to iterate over each character in `text`.
   - Inside the loop, check if the current character is not in `vowels`.
   - If the character is not a vowel, append it to `new_word`.

5. Return the Result

   - After the loop completes, return the `new_word`.
