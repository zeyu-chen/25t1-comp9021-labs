# Loop until valid input is received
while True:
    try:
        # Prompt user for input and convert to float
        num = float(input('Enter a floating point number between -1 and 1 excluded: '))
        # Validate if number is within range (-1, 1)
        if not (-1 < num < 1):
            raise ValueError
        # Exit loop if input is valid
        break
    except ValueError:
        # Handle invalid input (non-numeric or out of range)
        print('You got that wrong, try again!\n')
# Display the input value, formatted to 2 decimal places (rounding to nearest 0.01)
print(f'\nUp to +/-0.005, you input {num:.2f}')