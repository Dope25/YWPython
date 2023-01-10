# https://colab.research.google.com/drive/14ecL_WXePLsDWw057FEyObQeuR45OsDR?usp=sharing


# 1)	Create a program that will print your identifications.
# Example my identifications:
# •	Name: Alex
# •	Last name: Kuznetsov
# •	Age: 27
# •	Phone number: 0527389001
def task_1():
    name = 'Vlad'
    lastname = 'Zavgorodny'
    age = 27
    phone_number = '0545327245'
    print(f"Name: {name} {lastname}\nAge: {age}, Phone number: {phone_number}")


# 2)	For a string that you created please check if:
# The character at index 7 equals ‘a’.
# The character at index 8 equals ‘b’.
# The character at index 9 equals ‘c’.
# If all conditions exists please print “True”,
# Else print False.
# Pay attention for edge cases like the length of the string and so on.
# Your program must not crash for any string.
def task_2():
    _string = "discombobulated"
    if len(_string) < 10:
        print(False)
    elif 'abc' in _string[7:10]:
        print(True)
    else:
        print(False)


# 3)	Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
def task_3():
    _str1 = "Germany"
    _str2 = "Poland"
    if len(_str1) < 3 or len(_str2) < 3:
        print("One or more strings are too short")
    else:
        _newstring = _str2[0:2] + _str1[2:] + ' ' + _str1[0:2] + _str2[2:]
        print(_newstring)


# 4)	Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
def task_4():
    _str = "string"
    if len(_str) < 3:
        print(f"String '{_str}' is too short.")
    elif 'ing' == _str[-3:]:
        _str += 'ly'
        print(_str)
    else:
        _str += 'ing'
        print(_str)


# 5)	For a string (three characters and more) that you have created please create a new string
# that follows the next rules:
# •	The first character of the new string is the middle character of the original string.
# •	The middle character of the new string is the last character of the original string.
# •	The last character of the new string is the first character of the original string.
# Example:
# •	For odd length case, length of 9 characters:
# Let’s assume that the middle character is 9/2 rounded down that’s means that it is 4.
# “afffbeeec” –> “bfffceeea”
# •	For even length case, length of 8 characters:
# The middle character is also 4 because 8/2 equals 4.
# “axxxbyyc” -> “bxxxcyya”
# 	Print your new string in the following way, for even length example:
# 	The rotated string is bxxxcyya
def task_5():
    _str = "Californication"
    _str = "afffbeeec"
    if len(_str) < 3:
        print(f"String '{_str}' is too short.")
    else:
        _middle = len(_str) // 2
        _newstr = _str[_middle] + _str[1:_middle] + _str[-1] + _str[_middle + 1:-1] + _str[0]
    print(_newstr)


# 6)	Write a Python function to insert a string in the space of the original string.
# You can assume that there is just one space in your string.
def task_6():
    _str1 = "House Chancellor"
    _str2 = "Academy"
    _str1 = _str1.split()
    print(f"{_str1[0]} {_str2} {_str1[1]}")


# 7)	Write a Python program to sort a string lexicographically. Look For relevant method.
def task_7():
    _str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua."
    print(sorted(_str.split()))


task_7()
