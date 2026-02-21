# Temperature Converter - Chapter 03 Project
# Demonstrates functions, parameters, return values, and exception handling

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Function to display the menu
def display_menu():
    print('')
    print('Temperature Converter')
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    print('3. Exit')

# Function to get valid numeric input
def get_temperature_input(prompt):
    while True:
        try:
            temperature = float(input(prompt))
            return temperature
        except ValueError:
            print('Invalid input! Please enter a number.')

# Function to perform conversion based on choice
def perform_conversion(choice):
    if choice == '1':
        celsius = get_temperature_input('Enter temperature in Celsius: ')
        result = celsius_to_fahrenheit(celsius)
        print(str(celsius) + ' Celsius = ' + str(round(result, 2)) + ' Fahrenheit')
        return True
    elif choice == '2':
        fahrenheit = get_temperature_input('Enter temperature in Fahrenheit: ')
        result = fahrenheit_to_celsius(fahrenheit)
        print(str(fahrenheit) + ' Fahrenheit = ' + str(round(result, 2)) + ' Celsius')
        return True
    elif choice == '3':
        print('Thank you for using Temperature Converter!')
        return False
    else:
        print('Invalid choice! Please select 1, 2, or 3.')
        return True

# Main program
print('Welcome to Temperature Converter!')

# Main loop
continue_program = True

while continue_program:
    display_menu()
    user_choice = input('Select an option (1-3): ')
    continue_program = perform_conversion(user_choice)