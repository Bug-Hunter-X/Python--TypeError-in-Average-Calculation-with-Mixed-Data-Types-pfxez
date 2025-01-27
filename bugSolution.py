def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")  # Output: Average: 0

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}")  # Output: Average: 3.0

my_list = [1, 2, 3, 4, 'a']
result = calculate_average(my_list)
print(f"Average: {result}")  # Output: Average: 2.5