#!/usr/bin/python3
import sys

length = len(sys.argv) - 1
if length == 0:
    print("0 arguments.")
elif length == 1:
    print("{} argument:".format(length))
else:
    print("{} arguments:".format(length))
for i in range(length + 1):
    if i != 0:
        print("{}: {}".format(i, sys.argv[i]))
