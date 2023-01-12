# 1)	Create a list with your identification information. For example my lists length will be 4. If I reach the
# value of the list on index 0, list[0] I will receive the “Alex”. Run with for loop over the list and print its
# content.

def question_1():
    _list = ["Vlad", "Earth"]
    print(_list)


# 2)	Create a program that receives two lists of the same length with integers as values, if the lists are not of
#       the same length the program must return the relevant error. The program will create a new list that will contain
#       the largest value between the two lists at a specific index. Example: Input of two lists: lst1 = [1,2,3,4,
#       5] lst2 = [5,4,3,2,1] output: [5, 4, 3, 4, 5] In the end of the program you must print the new list.
#
def question_2():
    _list1 = [1, 2, 3, 4, 5]
    _list2 = [5, 4, 3, 2, 1]
    _final_list = []
    if len(_list1) != len(_list2):
        print("The two lists do not match in size.")
    else:
        for _index in range(len(_list1)):
            if _list1[_index] >= _list2[_index]:
                _final_list.append(_list1[_index])
            else:
                _final_list.append(_list2[_index])
        print(f"List 1: {_list1}\nList 2: {_list2}\nFinal list: {_final_list}")


# question_2()

# 3)	Create a python program that will count the number of appearances of odd and even values in a list. In case
#       that the program encounters a string use break statement and return a print that says, “It’s a string!!!” and
# nullify the values of odd and even numbers counters. Example: •	list = [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Output
# : Number of even numbers : 5 Number of odd numbers : 4 •	list = [1, 2, 3, 4, “Oops”, 6, 7, 8, 9] Expected Output :
# “It’s a string!!!”

def question_3():
    _list = [*range(0, 100, 15)]
    # _list = [*range(20), ""]
    odd = even = 0
    for item in _list:
        if type(item) == str:
            print("It's a string!!!")
            return
        elif type(item) == int:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1
    print(f"Even numbers: {even}, odd numbers: {odd}")


# question_3()

# 4)	Build a function that will receive a list with integer values as its input. The function will calculate the
# sum of the integers in the list and will return the sum result.

def question_4():
    _list = [*range(20)]
    _result = 0
    for _item in _list:
        _result += _item
    print(f"List sum: {_result}")


# question_4()


# 5)	Build a function that will receive a list with integer values as its input. The function will multiply all
# values in the list and return the result.

def question_5():
    _list = [*range(1, 5)]
    _result = 1
    for _item in _list:
        _result *= _item
    print(f"List multiplied: {_result}")


# question_5()

# 6)	Build a function that will receive a list with integer values as its input. The function will find the minimal
# value in the list and return this value.

def question_6():
    _list = [*range(5, 50)]
    print(f"Smallest list member: {min(_list)}")


# question_6()

# 7)	Build a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters. Sample String: ‘Alex Kuznetsov’ Expected Output: No. of Upper case
# characters: 2 No. of Lower case Characters: 11

def question_7():
    _string = "Californication"
    _lowercase = _uppercase = 0
    for _char in _string:
        if _char.islower():
            _lowercase += 1
        elif _char.isupper():
            _uppercase += 1
    print(f"Uppercase letters: {_uppercase}, lowercase letters: {_lowercase}")


# question_7()


#   Challenges:


# 8)	Build a Python function that takes a list and returns a new list with unique elements of the first list.
#   Example:
#   •	Input list : [1,2,3,3,3,3,4,5]
#       •	Output list : [1, 2, 3, 4, 5]

def question_8():
    _list = [1, 2, 3, 3, 3, 3, 4, 5]
    _new_list = []
    for _item in _list:
        if _item not in _new_list:
            _new_list.append(_item)
    print(f"Unique elements in list: {_new_list}")


# question_8()
# 9)	Write a Python program to construct the following pattern, using a nested loop.
#
# 	1
# 	12
# 	123
# 	1234
# 	12345
# 	123456
# 	1234567
# 	12345678

def question_9():
    for _line in range(1, 10):
        print(*range(1, _line), sep="")


# question_9()

# 10)	Write a Python program to print the following patterns:
#
#   ****
#   *
#   *
#    ***
#       *
#       *
#    ****

def question_10():
    print(4 * "*")
    print(2 * "*\n", end="")
    print(" " + 3 * "*")
    print(2 * "\t*\n", end="")
    print(" " + 4 * "*")


# question_10()
