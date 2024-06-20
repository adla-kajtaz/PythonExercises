# Exercise 22

### Garbled String Decoder

One of the exercises included in this repository is to decipher a garbled string. The garbled string has two issues: it is backwards and contains extra "X" characters.

### Steps to Implement the Garbled String Decoder:

1. Reverse the String

   - Reverse the garbled string to correct the first issue.

2. Filter Out the 'X' Characters

   - Use the `filter()` function combined with a lambda expression to filter out the "X" characters from the reversed string.

3. Print the Decoded Message
   - Print the resulting message to the console.
