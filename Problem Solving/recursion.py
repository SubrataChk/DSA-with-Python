# Recursion ki?
# Recursion mane hocche ekta function nijeke nijei call kore, 
# choto choto version-er problem solve kore, shesh e mool
# problem-er answer ber kora.
# Eta bujhar shohoj way: "Trust the process" — dhoro tumi jano choto version-er 
# problem-er answer ase (base case), tahole
# boro version ta oi choto answer diye build kora jay.
# Recursion-er duita must-have part
# 1.
# 2.
# Base Case — jekhane recursion thambe (stop condition). Eta na thakle infinite recursion hobe ar
# RecursionError ashbe.
# Recursive Case — jekhane function nijeke choto input diye call kore.




# def countdown(n):
#     if n <= 0:
#         print("Done")
#         return
#     print(n)
#     countdown(n-1)

# countdown(6)



# Factorial (Classic Recursion Example)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# Time: O(n) — n bar call hoy. Space: O(n) — call stack e n ta frame thake.

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# Dry run: factorial(4)
# factorial(4) = 4 * factorial(3)
# = 4 * (3 * factorial(2))
# = 4 * (3 * (2 * factorial(1)))
# = 4 * (3 * (2 * 1))
# print(factorial(5))




# Fibonacci (Recursion + kicchu limitation dekha)
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ... — protiti number age-er duita number-er sum.

def fibonacci_new(n):
    if n <= 1:
        return n
    return fibonacci_new(n - 1) + fibonacci_new(n - 2)

# print(fibonacci_new(5))

# for i in range(7):
#     print(fibonacci_new(i), end=" ")

# Sum of Digits

def sum_of_digit(n):
    if n == 0:
        return False
    return n % 10 + sum_of_digit(n // 10)


print(sum_of_digit(123))