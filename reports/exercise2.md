# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "True if the grade is 5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password does not check for at least one digit when the password is exactly 8 characters long, but the docstring requires "at least 8 characters and at least one digit". The current code uses > 8 for length, which excludes 8-character passwords.
Example: is_valid_password("abcdefgh1") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp incorrectly returns max(low, min(x, low)), which simplifies to low regardless of x, violating the docstring that says "x, limited to the range from low to high".
Example: clamp(10, 5, 15) returns 5, expected 10.
Fix: return max(low, min(x, high))
