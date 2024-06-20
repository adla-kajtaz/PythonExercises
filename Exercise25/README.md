# Exercise 25

### Point3D Class

One of the exercises included in this repository is to create a class to represent a 3D point in space.

### Steps to Implement the Point3D Class:

1. Define the Point3D Class

   - Create a class named `Point3D`.
   - Define an `__init__()` method that takes `self`, `x`, `y`, and `z` as parameters.
   - Initialize the `x`, `y`, and `z` attributes in the `__init__()` method.

2. Define the `__repr__()` Method

   - Inside the Point3D class, define a `__repr__()` method that returns a string in the format "(x, y, z)", where `x`, `y`, and `z` are the values of the instance variables.

3. Create an Instance of the Point3D Class

   - Outside the class definition, create a variable named `my_point` and set it to a new instance of `Point3D` with `x=1`, `y=2`, and `z=3`.

4. Print the Instance
   - Print the `my_point` variable to see the output of the `__repr__()` method.
