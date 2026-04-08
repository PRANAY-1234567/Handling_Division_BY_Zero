# 🧮 Python Division with Exception Handling

## 📌 Description

This Python program performs division between two numbers entered by the user. It includes **exception handling** to prevent the program from crashing when a division by zero occurs.

---

## 🚀 Features

* Takes two integer inputs from the user
* Performs division operation
* Handles division by zero error gracefully
* Displays a user-friendly error message

---

## 🛠️ How It Works

1. The program asks the user to enter two numbers.
2. It attempts to divide the first number by the second.
3. If the second number is `0`, the program catches the error using `try-except`.
4. Instead of crashing, it prints:
   👉 `Cannot divide by zero`

---

## 💻 Code

```python
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## ▶️ Example Output

### ✅ Valid Input

```
Enter number: 10
Enter number: 2
Result: 5.0
```

### ❌ Invalid Input (Division by Zero)

```
Enter number: 10
Enter number: 0
Cannot divide by zero
```

---

## 📚 Concepts Used

* `input()` function
* Type casting (`int`)
* Arithmetic operation (`/`)
* Exception handling (`try-except`)

---

## 🎯 Use Case

This program is useful for beginners to understand:

* How to handle runtime errors
* Writing safe and robust Python code

---

## 🔧 Future Improvements

* Handle invalid input (like strings) using `ValueError`
* Add support for floating-point numbers
* Create a loop to allow multiple calculations

---

## 📄 License

This project is open-source and free to use.
