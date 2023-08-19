def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2  #returns True if positive_count is equal to 2  and False if otherwise.

# Test cases
print(exactly_two_positive(2, 4, -3))    # Output: True
print(exactly_two_positive(-14, -3, -4)) # Output: False
