l1 = [3, 4, 5, 6, -5, -56, 95, 1, -69, 5, -56, 25, 4, 81, 5, -5, 58, 59, 4, 5, -6, -5, 79, 1, -98, 51, 5, 99]

# Function to check if the number is negative
def is_negative(num):
    return num > 0  # returns True if the number is negative

# Now, filter the list to get all negative numbers
negative_numbers = list(filter(is_negative, l1))

print(negative_numbers)
