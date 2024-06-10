# Exercise 3

### Student Grade Management

One of the exercises included in this repository involves managing student grades using dictionaries and functions. The task is to create dictionaries for students, compute their averages, and determine their letter grades.

### Steps to Implement the Grade Converter:

1. Create Student Dictionaries

   - Define dictionaries for three students: `lloyd`, `alice`, and `tyler`.
   - Each dictionary should have keys `"name"`, `"homework"`, `"quizzes"`, and `"tests"`

2. Fill in Student Data
   - For `lloyd`, populate with provided scores.
   - Example
   ```
   lloyd = {
   "name": "Lloyd",
   "homework": [90.0, 97.0, 75.0, 92.0],
   "quizzes": [88.0, 40.0, 94.0],
   "tests": [75.0, 90.0]
   }
   ```
3. Create a List of Students

   - Combine the student dictionaries into a list called students.
   - Example

   ```
   students = [lloyd, alice, tyler]

   ```

4. Print Student Data

   - For each student in the list, print their name, homework, quizzes, and test scores.

5. Function to Calculate Average

   - Define a function `average()` that calculates the average of a list of numbers.

6. Function to Get Student Average

   - Define `get_average()` to compute the weighted average of a student's scores.
   - Weights: Homework 10%, Quizzes 30%, Tests 60%.

7. Function to Determine Letter Grade

   - Define `get_letter_grade()` that converts a numeric score to a letter grade.

8. Function to Calculate Class Average
   - Define `get_class_average()` to compute the average score for a list of students.
