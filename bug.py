def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # This will print 0 as expected

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"Average: {result}") # This will print 3.0 as expected

my_list = [1,2,3,4,'a']
result = calculate_average(my_list) # TypeError: unsupported operand type(s) for +: 'int' and 'str'