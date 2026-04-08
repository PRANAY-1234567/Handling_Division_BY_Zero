try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))

    result = num1 / num2
    
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
