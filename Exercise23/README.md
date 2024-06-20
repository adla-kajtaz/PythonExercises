# Exercise 23

### Triangle and Equilateral Classes

One of the exercises included in this repository is to create a class to represent a triangle and then extend this class to represent an equilateral triangle.

### Steps to Implement the Triangle and Equilateral Classes:

1. Define the Triangle Class

   - Create a class named `Triangle`.
   - Define an `__init__()` method that takes `self`, `angle1`, `angle2`, and `angle3` as parameters.
   - Initialize the angles in the `__init__()` method.
   - Add a class attribute `number_of_sides` and set it to 3.
   - Define a method `check_angles()` that returns `True` if the sum of the three angles is equal to 180, otherwise returns `False`.

2. Create an Instance of the Triangle Class

   - Instantiate the `Triangle` class with three angles that sum to 180.
   - Print the value of `number_of_sides` for the created instance.
   - Print the result of the `check_angles()` method.

3. Define the Equilateral Class
   - Create a class named `Equilateral` that inherits from `Triangle`.
   - Define an `__init__()` method that initializes the three angles to 60.
