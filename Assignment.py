Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> x = 10
>>> print("Initial value of x:", x)
Initial value of x: 10
>>> x += 5
>>> print("After x += 5:", x)
After x += 5: 15
>>> x -= 3
>>> print("After x -= 3:", x)
After x -= 3: 12
>>> x *= 2
>>> print("After x *= 2:", x)
... x /= 4
SyntaxError: multiple statements found while compiling a single statement
>>> print("After x *= 2:", x)
After x *= 2: 24
>>> x %= 3
>>> print("After x %= 3:", x)
After x %= 3: 0
>>> x **= 2
>>> print("After x **= 2:", x)
After x **= 2: 0
>>> x //= 2
>>> print("After x //= 2:", x)
After x //= 2: 0
