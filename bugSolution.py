def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(5))
print(factorial(0))
try:
    print(factorial(-1))
except ValueError as e:
    print("Error:", e) #This will print Error: Factorial is not defined for negative numbers.