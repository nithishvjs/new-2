# Function to calculate the sum of even numbers in a list
def sum_of_evens(numbers):
    sum_evens = 0
    for num in numbers:
        if num % 2 == 0:
            sum_evens += num
    return sum_evens

# Sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the sum of even numbers in the list
result = sum_of_evens(sample_list)

# Print the result
print("Sum of even numbers:", result)
