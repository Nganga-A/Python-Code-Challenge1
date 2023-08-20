# Python Phase3-Code-Challenge-1
![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Challenge 1 - Time Converter:
The program works to Convert a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030")!
It defines a function, which will be given an hour (always in the range of 1 to 12, inclusive), 
a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.
The program returns a four-digit string that encodes that time in 24-hour time.

## Challenge 2 - Two Positive Numbers:
This program defines a function that checks whether exactly two out of three given numbers are positive. 
It iterates through the provided numbers and counts the positive ones. 
If exactly two numbers are positive, the function returns True; otherwise, it returns False. 
The code demonstrates the function by accepting 3 user input numbers and printing the result.

## Challenge 3 - Consonant Value:
This is a program that defines a function that takes a string and removes the vowels (a, e, i, o, u) 
and then splits the string to create groups of consonant sequences. 
It calculates the value of each group by summing the position of each character in the alphabet plus one. 
The function returns the maximum value among these calculated values for each group of consonants. 
The code demonstrates the function by accepting a string into the function and printing the result.


## Project Setup
1. Clone the repository
```
git clone git@github.com:Nganga-A/Python-Code-Challenge1.git
```

2. Install required dependencies
```
cd into the project directory
```

## Project Composition
This repository contains three Python files

    1. challenge1.py - Time Converter

    2. challenge2.py - Exactly Two Numbers

    3. challenge3.py - String Strength Calculation

### 1. challenge1.py - Time Converter
    -This code snippet converts a time given in 12-hour format to 24-hour format.
    -You can test the time conversion function by running the script and providing inputs.

    ```python
    # Example usage
    print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
    print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"
    ```

### 2. challenge2.py - Exactly Two Numbers
    -This code checks if exactly two out of three given numbers are positive.
    -You can test the function by running the script and providing inputs.
    
    ```python
    # Example usage
    print(exactly_two_positive(2, 4, -3))    # Output: True
    print(exactly_two_positive(-14, -3, -4)) # Output: False
    print(exactly_two_positive(14, 3, 4)) # Output: False
    ```


### 3. challenge3.py - String Strength Calculation
    -This code calculates the "strength" of a string based on the sum of positions of consonant characters in the English alphabet.
    -You can test the strength calculation by running the script and providing a string input.
    
    ```python
    # Example usage
    print(solve("zodiacs"))   # Output: 26
    print(solve("strength"))  # Output: 57
    ```






## Author
Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)

## License
This project is licensed under the [MIT License](LICENSE).