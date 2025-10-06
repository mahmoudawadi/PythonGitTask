def factorial(n):
    """
    Time complexity: O(n)
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def find_max(numbers):
    """
    Time complexity: O(n)
    """
    if not numbers:
        return None
    max_val = numbers[0]
    for x in numbers[1:]:
        if x > max_val:
            max_val = x
    return max_val
def linear_search(numbers, target):
    """
    Time complexity: O(n)
    """
    for x in numbers:
        if x == target:
            return True
    return False
def fibonacci_iterative(n):
    """
    Time complexity: O(n)
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
def fibonacci_recursive(n):
    """
    Time complexity: O(2^n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("Login successful.")
        return True
    else:
        print("Login failed.")
        return False
    
def parse_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        else:
            print("Enter a valid number.")

def parse_int_list(prompt):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Enter some numbers.")
            continue
        if ',' in s:
            parts = s.split(',')
        else:
            parts = s.split()
        try:
            return [int(p) for p in parts]
        except:
            print("Enter only integers separated by commas or spaces.")