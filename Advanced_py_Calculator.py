# Python-based Advanced Calculator
print("NOTE: *This is an advanced calculator that can perform operations on up to 10 numbers. No more than 10 numbers can be entered. We do not entertain any kind of invalid inputs or any mallicious or illegal activities. We are not responsible for any kind of loss or damage caused by using this calculator. Use it at your own risk.*")
print("Welcome to Ibrahim's Advanced Python Calculator!")
print("You can enter up to 10 numbers and perform operations on them.")
print("Operations available:")
print(" +  : Addition")
print(" -  : Subtraction")
print(" *  : Multiplication")
print(" /  : Division")
print(" ** : Exponentiation")
print(" %  : Modulus")
print("Enter 'done' when you finish entering numbers.")
print("Enter 'q' to quit.")
print("Let's get started!\n")


# Function to get user inputs
def get_numbers():
    numbers = []
    while len(numbers) < 10:
        user_input = input(f"Enter number {len(numbers) + 1} (or 'done' to finish): ")
        if user_input.lower() == 'done':
            if len(numbers) < 2:
                print("You must enter at least two numbers to perform an operation.")
                continue
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return numbers

# Function to perform calculation
def calculate(numbers, operator):
    if operator == "+":
        return sum(numbers)
    elif operator == "-":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    elif operator == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operator == "/":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    elif operator == "**":
        result = numbers[0]
        for num in numbers[1:]:
            result **= num
        return result
    elif operator == "%":
        result = numbers[0]
        for num in numbers[1:]:
            result %= num
        return result
    else:
        return "Invalid operator"

# Main loop
while True:
    numbers = get_numbers()
    operator = input("Enter an operator (+, -, *, /, **, %), or 'q' to quit: ").strip()
    
    if operator.lower() == 'q':
        print("Goodbye! Thanks for using Ibrahim's Advanced Python Calculator.")
        break
    
    result = calculate(numbers, operator)
    print(f"Result: {result}\n")
