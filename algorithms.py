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