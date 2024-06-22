# Exercise 26

### Weather Program

One of the exercises included in this repository is to create a Python program that fetches and displays weather information for a user-specified location using the OpenWeatherMap API.

### Steps to Implement the Weather Program:

1. Set Up the Environment

   - Install the `requests` library if you haven't already.

2. Import Necessary Libraries

   - Import the `requests` library to handle API requests.
   - Import the `pprint` function from the `pprint` module for pretty-printing the JSON response.

3. Define the API Key and Base URL

   - Define a variable `API_key` and assign it your API key from OpenWeatherMap.
   - Define the base URL for the OpenWeatherMap API.

4. Get User Input

   - Prompt the user to enter the name of a city for which they want to retrieve weather information.

5. Make the API Request

   - Construct the full API request URL by combining the base URL, the city name, and the API key.
   - Use the `requests.get()` function to make the API call and retrieve the weather data.

6. Handle the JSON Response
   - Parse the JSON response using the `.json()` method.
   - Use the `pprint` function to display the weather data in a readable format.
