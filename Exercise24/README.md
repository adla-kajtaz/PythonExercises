# Exercise 24

### Car and ElectricCar Classes

One of the exercises included in this repository is to create a class to represent a car and then extend this class to represent an electric car.

### Steps to Implement the Car and ElectricCar Classes:

1. Define the Car Class

   - Create a class named `Car`.
   - Define an `__init__()` method that takes `self`, `model`, `color`, and `mpg` as parameters.
   - Initialize the `model`, `color`, and `mpg` attributes in the `__init__()` method.
   - Add a class attribute `condition` and set it to "new".
   - Define a method `display_car()` that returns a string describing the car.
   - Define a method `drive_car()` that changes the condition to "used".

2. Create an Instance of the Car Class

   - Instantiate the `Car` class with a model, color, and mpg.
   - Print the value of `condition` attribute.
   - Call the `drive_car()` method and print the `condition` attribute again.

3. Define the ElectricCar Class

   - Create a class named `ElectricCar` that inherits from `Car`.
   - Define an `__init__()` method that includes an additional parameter for `battery_type`.
   - Initialize the `battery_type` attribute in the `__init__()` method.
   - Override the `drive_car()` method to set the condition to "like new".

4. Create an Instance of the ElectricCar Class
   - Instantiate the `ElectricCar` class with a model, color, mpg, and battery type.
   - Print the value of `condition` attribute.
   - Call the `drive_car()` method and print the `condition` attribute again.
