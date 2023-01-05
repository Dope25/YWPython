# https://colab.research.google.com/drive/14ecL_WXePLsDWw057FEyObQeuR45OsDR?usp=sharing

def task_1():
    name = 'Vlad'
    lastname = 'Zavgorodny'
    age = 27
    phone_number = '0545327245'
    print(f"Name: {name} {lastname}\nAge: {age}, Phone number: {phone_number}")


def task_2():
    _string = "discombobulated"
    if (len(_string) < 10):
        print(False)
    elif ('abc' in _string[7:10]):
        print(True)
    else:
        print(False)


def task_3():
    _str1 = "Germany"
    _str2 = "Poland"
    if (len(_str1) < 3 or len(_str2) < 3):
        print("One or more strings are too short")
    else:
        _newstring = _str2[0:2] + _str1[2:] + ' ' + _str1[0:2] + _str2[2:]
        print(_newstring)


def task_4():
    _str = "string"
    if (len(_str) < 3):
        print(f"String '{_str}' is too short.")
    elif ('ing' == _str[-3:]):
        _str += 'ly'
        print(_str)
    else:
        _str += 'ing'
        print(_str)


def task_5():
    _str = "Californication"
    _str = "afffbeeec"
    if (len(_str) < 3):
        print(f"String '{_str}' is too short.")
    else:
        _middle = len(_str)//2
        _newstr = _str[_middle] + _str[1:_middle] + _str[-1] + _str[_middle+1:-1] + _str[0]
    print(_newstr)


# def task_6():
    