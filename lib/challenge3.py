def strength_checker(str):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0

    for char in str:
        if char in consonants:
            current_value += ((ord(char) - ord('a')) + 1)  
            #calculates the offset between the Unicode code points of the given character 
            # and the lowercase letter 'a'. This offset represents the position of the character in the English alphabet. 
            max_value = max(max_value, current_value)
        else:
            current_value = 0 #if character is not a consonant

    return max_value

# Get user input
input_string = input("Enter a string: ")

# Call the function with user input
result = strength_checker(input_string)

# Display the output
print("Strength of the string:", result)


