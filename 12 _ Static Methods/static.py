# Define a class named TemperatureConverter
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        # Convert Celsius to Fahrenheit  and return the result
        return (c * 9/5) + 32
    
# Assign the Celsius temperature value to the variable 'temp'
temp = 45

# Call the static method to convert Celsius to Fahrenheit and store the result
result = TemperatureConverter.celsius_to_fahrenheit(temp)

# Print the conversion result in a formatted string
print(f"{temp}°C = {result}°F")
