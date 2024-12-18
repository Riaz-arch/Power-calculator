def calculate_power(base, exponent):
    return base ** exponent

# Get input from the user
try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent (n): "))

    # Calculate the power
    result = calculate_power(base, exponent)

    # Display the result
    print(f"{base} raised to the power of {exponent} is {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for the base and exponent.")