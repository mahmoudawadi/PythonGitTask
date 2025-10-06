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


def main_menu():
    logged_in = False
    while True:
        print("\nChoose an option:")
        print("1. Factorial")
        print("2. Find Max")
        print("3. Linear Search")
        print("4. Fibonacci")
        print("5. Login")
        print("6. Exit")

        choice = input("Enter option number: ").strip()

        if choice in ['1', '2', '3', '4'] and not logged_in:
            print("You must be logged in first.")
            continue

        if choice == '1':
            n = parse_int("Enter a number for factorial: ")
            print(f"{n}! = {factorial(n)}")

        elif choice == '2':
            nums = parse_int_list("Enter integers (comma or space separated): ")
            maximum = find_max(nums)
            if maximum is None:
                print("List is empty.")
            else:
                print("Maximum is:", maximum)

        elif choice == '3':
            nums = parse_int_list("Enter integers (comma or space separated): ")
            target = parse_int("Enter number to search for: ")
            print("Found." if linear_search(nums, target) else "Not found.")

        elif choice == '4':
            n = parse_int("Enter n for Fibonacci: ")
            method = input("Choose method (i = iterative / r = recursive): ").strip().lower()
            if method == 'r':
                print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")
            else:
                print(f"Fibonacci({n}) = {fibonacci_iterative(n)}")

        elif choice == '5':
            logged_in = login()

        elif choice == '6':
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "_main_":
    main_menu()