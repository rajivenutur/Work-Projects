# Simple Calculator
from collections import Counter

def add(numbers):
    total = 0
    for n in numbers[0:]:
        total = total+n
    return total

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = result - n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result
    
def power(numbers):
    result = int(numbers[0])
    if len(numbers) > 2:
        print("Not allowed")
    else:
        powenum = int(numbers[1])
        return result ** powenum
         

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
     if n == 0:
        return "Error: cannot divide by zero"
    else:
     return result / n
     return result

print("Array Calculator")
print("Enter numbers separated by commas, for example: 10, 5, 2")

while True:
    text = input("\nEnter numbers (or 'q' to quit): ").strip()
 
    if text.lower() == "q":
        print("Goodbye!")
        break
    
    try:
        numbers = [float(x.strip()) for x in text.split(",")]
    except ValueError:
        print("Please enter numbers separated by commas.")
        continue
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
        continue
    operation = input("Operation (+, -, *, **, /): ").strip()
    result = 0;    
    if operation == "+":
       result= add(numbers)
    elif operation == "-":
        result= subtract(numbers)
    elif operation == "*":
        result= multiply(numbers)
    elif operation == "/":
        result= divide(numbers)
    else:
        result= power(numbers)
    
    print("Result:", result)
    