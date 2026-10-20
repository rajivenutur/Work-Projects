# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def power(a,b):
    return a ** b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print("Simple Calculator")
print("Operations: +, -, *, ** /")

while True:
    choice = input("\nEnter operation (or 'q' to quit): ").strip()

    if choice.lower() == "q":
        print("Goodbye!")
        break

    if choice not in ("+", "-", "*", "/", "**"):
        print("Invalid operation. Please choose +, -, *, **, or /.")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "+":
        result = add(a, b)
    elif choice == "-":
        result = subtract(a, b)
    elif choice == "*":
        result = multiply(a, b)
    elif choice == "**":
        result = power(a,b)
    else:
        result = divide(a, b)

    print("Result:", result)
