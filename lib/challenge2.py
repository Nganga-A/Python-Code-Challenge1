def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2  #returns True if positive_count is equal to 2  and False if otherwise.


# Get user input
input_a = int(input("Enter the value for a: "))
input_b = int(input("Enter the value for b: "))
input_c = int(input("Enter the value for c: "))

# Call the function with user input
result = exactly_two_positive(input_a, input_b, input_c)

# Display the output
print("Exactly two of the numbers are positive:", result)


# Test cases
# print(exactly_two_positive(2, 4, -3))    # Output: True
# print(exactly_two_positive(-14, -3, -4)) # Output: False
