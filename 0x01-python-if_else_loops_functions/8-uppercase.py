#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        tester = ord(i)
        if tester >= 97 and tester <= 122:
            tester -= 32
        new_str += chr(tester)
    print("{}".format(new_str))
