# Exercise 12

### Grade Statistics Program

One of the exercises included in this repository is to create a program that computes various statistics for a set of grades.

### Task Description

To implement the grade statistics program:

1. Print Grades

   - Define a function called `print_grades` with one argument: a list called `grades_input`.
   - The function should iterate through `grades_input` and print each item on its own line.

2. Sum of Grades

   - Define a function called `grades_sum` that:
     - Takes in a list of scores, `scores`.
     - Computes the sum of the scores.
     - Returns the computed sum.

3. Average of Grades

   - Define a function called `grades_average` that:
     - Takes one argument, `grades_input`.
     - Calls `grades_sum` with `grades_input` to get the sum of grades.
     - Computes the average by dividing the sum by the number of grades.
     - Returns the average.

4. Variance of Grades

   - Define a function called `grades_variance` that:
     - Takes one argument, `scores`.
     - Computes the average of the scores.
     - Computes the variance by summing the squared differences between each score and the average, then dividing by the number of scores.
     - Returns the variance.

5. Standard Deviation of Grades

   - Define a function called `grades_std_deviation` that:
     - Takes one argument, `variance`.
     - Returns the square root of the variance.

6. Print All Statistics

   - Print out all of the following:
     - All of the grades.
     - Sum of grades.
     - Average grade.
     - Variance.
     - Standard deviation.

### Steps to Implement the Grade Statistics Program:

1. Define the Function

   - Create the necessary functions as described above.

2. Initialize Variables and Test the Functions

   - Use a sample list of grades to test each function.
