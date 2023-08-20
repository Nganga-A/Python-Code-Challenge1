def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  # period == "pm"
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    return f"{hour_24:02d}{minute:02d}" #2 decimal point with optional 0 at the beginning

# Get user input
input_hour = int(input("Enter the hour: "))
input_minute = int(input("Enter the minute: "))
input_period = input("Enter 'am' or 'pm': ").lower()

# Call the function with user input
converted_time = convert_to_24_hour(input_hour, input_minute, input_period)

# Display the output
print("Converted time in 24-hour format:", converted_time)




# Test cases
# print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
# print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"
